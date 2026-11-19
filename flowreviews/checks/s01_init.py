#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts"))
import check_docs

TEMPLATES = {
    "AGENTS.md": "templates/project/AGENTS.md",
    "README.md": "templates/project/README.md",
    "docs/documentation.md": "templates/project/docs/documentation.md",
    "docs/coolflow.yml": "templates/project/docs/coolflow.yml",
    "docs/development-flow.md": "templates/project/docs/development-flow.md",
    "docs/product.md": "templates/project/docs/product.md",
    "docs/roadmap.md": "templates/project/docs/roadmap.md",
    "docs/domain.md": "templates/project/docs/domain.md",
}
GITKEEPS = ["docs/features/.gitkeep", "docs/work/.gitkeep", "docs/work/archive/.gitkeep"]
CREATED_DIRS = ["docs", "docs/features", "docs/work", "docs/work/archive"]
CARDS = ["docs/product.md", "docs/roadmap.md", "docs/domain.md"]
PROTECTED = (".git", ".claude")
SOURCE_PREFIX = "https://raw.githubusercontent.com/CooLingLab/CoolFlow/"

GIT = ("git",)
GIT_FILE = ("file", ".git", "gitdir: /nonexistent/worktrees/demo\n")
CLAUDE = ("dir", ".claude")
CC_WRITES = ("dir", ".claude/.cc-writes")
SETTINGS = ("file", ".claude/settings.local.json", "{}\n")

CASES = {
    "a01-empty": ("accept", []),
    "a02-git-dir": ("accept", [GIT]),
    "a03-git-file": ("accept", [GIT_FILE]),
    "a04-claude-empty": ("accept", [CLAUDE]),
    "a05-claude-empty-git": ("accept", [GIT, CLAUDE]),
    "a06-cc-writes": ("accept", [CC_WRITES]),
    "a07-cc-writes-git": ("accept", [GIT, CC_WRITES]),
    "a08-cc-writes-settings": ("accept", [CC_WRITES, SETTINGS]),
    "a09-cc-writes-settings-git": ("accept", [GIT, CC_WRITES, SETTINGS]),
    "a10-cc-writes-transient": ("accept", [CC_WRITES, ("file", ".claude/.cc-writes/tmp-write", "x\n")]),
    "r01-readme": ("refuse", [("file", "README.md", "# Existing\n")]),
    "r02-directory": ("refuse", [("dir", "src")]),
    "r03-gitignore": ("refuse", [("file", ".gitignore", "node_modules/\n")]),
    "r04-ds-store": ("refuse", [("file", ".DS_Store", "\0\0\0\1Bud1")]),
    "r05-symlink": ("refuse", [("symlink", "notes", "missing-target")]),
    "r06-git-plus-file": ("refuse", [GIT, ("file", "README.md", "# Existing\n")]),
    "r07-claude-md": ("refuse", [("file", "CLAUDE.md", "# Rules\n")]),
    "r08-mcp-json": ("refuse", [("file", ".mcp.json", "{}\n")]),
    "r09-claude-settings-json": ("refuse", [CLAUDE, ("file", ".claude/settings.json", "{}\n")]),
    "r10-claude-commands": ("refuse", [("dir", ".claude/commands")]),
    "r11-claude-file": ("refuse", [("file", ".claude", "not a directory\n")]),
    "r12-claude-symlink": ("refuse", [("outside-symlink", ".claude")]),
    "r13-cc-writes-file": ("refuse", [CLAUDE, ("file", ".claude/.cc-writes", "x\n")]),
    "r14-settings-local-dir": ("refuse", [CC_WRITES, ("dir", ".claude/settings.local.json")]),
    "r15-cc-writes-symlink": ("refuse", [CLAUDE, ("outside-symlink", ".claude/.cc-writes")]),
}

NETWORK = re.compile(r"\b(curl|wget|git\s+clone|gh\s+api)\b|https?://", re.I)
WRITE_COMMAND = re.compile(r"(?:^|[;&|(]\s*)(?:sudo\s+)?(?:mkdir|touch|cp|mv|rm|tee|install|ln|git\s+(?:init|add|commit))\b|(?:^|[^&>=-])\d*>{1,2}\s*(?!/dev/null\b)[^&\s]")
SOURCE_LOOKUP = re.compile(r"(^|[/\s'\"])(standards|templates|methodology)(/|\b)")
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
ACTION_TOOLS = WRITE_TOOLS | {"Bash", "Read", "Glob", "Grep", "LS", "WebFetch", "WebSearch", "Agent", "Task"}


def build_case(root, ops, outside):
    root.mkdir(parents=True)
    for op in ops:
        kind = op[0]
        if kind == "git":
            subprocess.run(["git", "init", "-q", str(root)], check=True)
        elif kind == "dir":
            (root / op[1]).mkdir(parents=True, exist_ok=True)
        elif kind == "file":
            (root / op[1]).parent.mkdir(parents=True, exist_ok=True)
            (root / op[1]).write_text(op[2])
        elif kind == "symlink":
            (root / op[1]).parent.mkdir(parents=True, exist_ok=True)
            os.symlink(op[2], root / op[1])
        elif kind == "outside-symlink":
            target = outside / f"{root.name}-{op[1].replace('/', '_')}"
            target.mkdir(parents=True, exist_ok=True)
            (root / op[1]).parent.mkdir(parents=True, exist_ok=True)
            os.symlink(target, root / op[1])


def snapshot(root, skip_transient=False):
    entries = {}
    for current, dirs, files in os.walk(root, followlinks=False):
        here = Path(current)
        rel_here = here.relative_to(root).as_posix()
        if skip_transient and rel_here == ".claude/.cc-writes":
            dirs[:] = []
            files = []
        for name in sorted(dirs + files):
            path = here / name
            rel = path.relative_to(root).as_posix()
            if path.is_symlink():
                entries[rel] = ["symlink", os.readlink(path)]
            elif path.is_dir():
                entries[rel] = ["dir", None]
            else:
                entries[rel] = ["file", hashlib.sha256(path.read_bytes()).hexdigest()]
        dirs[:] = [d for d in dirs if not (here / d).is_symlink()]
    return entries


def claude_view(entries):
    return {
        path: value for path, value in entries.items()
        if (path == ".claude" or path.startswith(".claude/")) and not path.startswith(".claude/.cc-writes/")
    }


def git_identity(root):
    git = root / ".git"
    if git.is_symlink() or not git.exists():
        return None
    if git.is_file():
        return ["file", git.read_text()]
    head = git / "HEAD"
    return ["dir", head.read_text() if head.exists() else None]


def template_text(source, ref):
    if ref:
        return subprocess.run(
            ["git", "-C", str(REPO), "show", f"{ref}:{source}"],
            check=True, capture_output=True, text=True,
        ).stdout
    return (REPO / source).read_text()


def frontmatter_status(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    found = re.search(r"^status:\s*(\S+)", match.group(1), re.M)
    return found.group(1) if found else None


def link_problems(root):
    problems = []
    for path in sorted(root.rglob("*.md")):
        if any(part in PROTECTED for part in path.relative_to(root).parts):
            continue
        text = path.read_text(encoding="utf-8")
        for number, line in check_docs.prose_lines(text):
            for angled, plain in check_docs.LINK.findall(check_docs.INLINE_CODE.sub("", line)):
                target = angled or plain
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or "<" in target:
                    continue
                file_part, _, fragment = target.partition("#")
                destination = (path.parent / file_part).resolve() if file_part else path
                rel = path.relative_to(root).as_posix()
                if not destination.exists():
                    problems.append(f"{rel}:{number} {target}")
                elif fragment and destination.suffix == ".md" and fragment not in check_docs.anchors(destination):
                    problems.append(f"{rel}:{number} #{fragment}")
    return problems


def tool_calls(trace_path):
    calls = []

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "tool_use" and "name" in node:
                calls.append((node["name"], json.dumps(node.get("input", {}), ensure_ascii=False)))
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    for line in Path(trace_path).read_text(encoding="utf-8").splitlines():
        try:
            walk(json.loads(line))
        except json.JSONDecodeError:
            continue
    return [(name, data) for name, data in calls if name in ACTION_TOOLS]


def check_refusal_trace(calls):
    results = []
    network = [i for n, i in calls if n in ("WebFetch", "WebSearch") or (n == "Bash" and NETWORK.search(i))]
    writes = [i for n, i in calls if n in WRITE_TOOLS or (n == "Bash" and WRITE_COMMAND.search(json.loads(i).get("command", "")))]
    lookups = [i for n, i in calls if SOURCE_LOOKUP.search(i)]
    results.append(("trace: no network after refusal", not network, network[:2]))
    results.append(("trace: no write operations", not writes, writes[:2]))
    results.append(("trace: no standards/templates lookup", not lookups, lookups[:2]))
    return results


def check_accept_trace(calls, root):
    fetched = [i for n, i in calls if n == "WebFetch" or (n == "Bash" and NETWORK.search(i))]
    foreign = [i for i in fetched if "https://" in i and SOURCE_PREFIX not in i]
    local = [i for n, i in calls if str(REPO).lower() in i.lower() and str(root).lower() not in i.lower()]
    return [
        ("trace: templates fetched from canonical GitHub", bool(fetched) and not foreign, foreign[:2] or ([] if fetched else ["no fetch observed"])),
        ("trace: no local CoolFlow checkout used as source", not local, local[:2]),
    ]


def check_accept(root, before, ref):
    results = []
    after = snapshot(root, skip_transient=True)
    missing = [p for p in list(TEMPLATES) + GITKEEPS if not (root / p).is_file()]
    results.append(("required files and .gitkeep placeholders exist", not missing, missing))
    allowed = set(TEMPLATES) | set(GITKEEPS) | set(CREATED_DIRS)
    extra = [p for p in after if p.split("/")[0] not in PROTECTED and p not in allowed]
    results.append(("no unintended files or directories", not extra, extra[:10]))
    yml = root / "docs/coolflow.yml"
    yml_lines = [l.strip() for l in yml.read_text().splitlines() if l.strip()] if yml.is_file() else []
    results.append(("coolflow.yml is context_mode: auto", yml_lines == ["context_mode: auto"], yml_lines))
    differing = [
        target for target, source in TEMPLATES.items()
        if (root / target).is_file() and (root / target).read_text().rstrip("\n") != template_text(source, ref).rstrip("\n")
    ]
    results.append((f"files match templates at {ref or 'working tree'}", not differing, differing))
    statuses = {p: frontmatter_status((root / p).read_text()) for p in CARDS if (root / p).is_file()}
    bad = {p: s for p, s in statuses.items() if s != "not_started"}
    results.append(("progress cards keep status: not_started", not bad and len(statuses) == len(CARDS), bad))
    links = link_problems(root)
    results.append(("relative links resolve", not links, links[:5]))
    old, new = claude_view(before["entries"]), claude_view(after)
    changed = {p for p in set(old) | set(new) if old.get(p) != new.get(p)}
    same_git = before["git"] == git_identity(root)
    results.append(("pre-existing .git and .claude unchanged", not changed and same_git, sorted(changed)[:10]))
    return results


def check_refuse(root, before):
    after = snapshot(root)
    changed = sorted(p for p in set(before["entries"]) | set(after) if before["entries"].get(p) != after.get(p))
    return [("target tree and file hashes unchanged", not changed, changed[:10])]


def cmd_build(args):
    work = Path(args.workdir).resolve()
    if work.exists() and any(work.iterdir()):
        sys.exit(f"{work} is not empty")
    outside = work / "outside"
    outside.mkdir(parents=True)
    manifest = {}
    for case in select(args.only):
        expect, ops = CASES[case]
        root = work / "cases" / case
        build_case(root, ops, outside)
        manifest[case] = {"expect": expect, "entries": snapshot(root), "git": git_identity(root)}
    (work / "manifest.json").write_text(json.dumps(manifest, indent=2))
    for case in manifest:
        print(work / "cases" / case)


def cmd_check(args):
    work = Path(args.workdir).resolve()
    manifest = json.loads((work / "manifest.json").read_text())
    failed = False
    for case in select(args.only, manifest):
        root = work / "cases" / case
        before = manifest[case]
        results = check_accept(root, before, args.ref) if before["expect"] == "accept" else check_refuse(root, before)
        trace = work / "traces" / f"{case}.jsonl"
        if trace.exists():
            calls = tool_calls(trace)
            results += check_accept_trace(calls, root) if before["expect"] == "accept" else check_refusal_trace(calls)
        else:
            results.append(("trace checks", None, "no trace recorded"))
        for name, ok, detail in results:
            verdict = "NOT VERIFIED" if ok is None else ("PASS" if ok else "FAIL")
            failed |= ok is False
            suffix = f" — {detail}" if detail and ok is not True else ""
            print(f"{case}\t{verdict}\t{name}{suffix}")
    return 1 if failed else 0


def select(only, available=CASES):
    if not only:
        return list(available)
    chosen = only.split(",")
    unknown = [c for c in chosen if c not in available]
    if unknown:
        sys.exit(f"unknown cases: {', '.join(unknown)}")
    return chosen


def main():
    parser = argparse.ArgumentParser(description="S01 initialization fixtures and deterministic checks")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    build = sub.add_parser("build")
    build.add_argument("workdir")
    build.add_argument("--only")
    check = sub.add_parser("check")
    check.add_argument("workdir")
    check.add_argument("--only")
    check.add_argument("--ref", default="origin/main", help="Git ref whose templates the Skill fetched; empty for the working tree")
    args = parser.parse_args()
    if args.command == "list":
        for case, (expect, _) in CASES.items():
            print(f"{case}\t{expect}")
        return 0
    if args.command == "build":
        cmd_build(args)
        return 0
    return cmd_check(args)


if __name__ == "__main__":
    sys.exit(main())
