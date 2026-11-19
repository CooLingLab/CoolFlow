#!/usr/bin/env python3
import hashlib
import html
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
STANDARD = ROOT / "standards" / "documentation.md"
SNAPSHOT = ROOT / "skills" / "coolflow-docs-review" / "references" / "documentation-standard.md"
BILINGUAL_DIRS = ("methodology", "standards")
BILINGUAL_ROOT_FILES = ("README.md", "GETTING_STARTED.md")
ZH_SUFFIX = ".zh-CN.md"

FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LINK = re.compile(r"!?\[(?:[^\[\]]|\[[^\]]*\])*\]\(\s*(?:<([^>]+)>|([^)\s]+))(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)")
INLINE_CODE = re.compile(r"`[^`]*`")
HTML_ID = re.compile(r"""\b(?:id|name)=["']([^"']+)["']""")
SNAPSHOT_BLOB = re.compile(r"Source Git blob: ([0-9a-f]{40})")


def markdown_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.relative_to(ROOT).parts)


def rel(path):
    return path.relative_to(ROOT).as_posix()


def prose_lines(text):
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE.match(line)
        if fence is None and match:
            fence = match.group(1)
            continue
        if fence is not None:
            if re.fullmatch(r" {0,3}%s{%d,}\s*" % (re.escape(fence[0]), len(fence)), line):
                fence = None
            continue
        yield number, line


def headings(text):
    result = []
    for number, line in prose_lines(text):
        match = HEADING.match(line)
        if match:
            result.append((number, len(match.group(1)), match.group(2)))
    return result


def slugify(heading_text):
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading_text)
    text = html.unescape(re.sub(r"<[^>]+>", "", text)).replace("`", "").replace("*", "")
    kept = "".join(
        ch for ch in text.strip().lower()
        if ch in " -_" or unicodedata.category(ch)[0] in "LNM"
    )
    return kept.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        text = path.read_text(encoding="utf-8")
        seen = {}
        found = set(HTML_ID.findall(text))
        for _, _, title in headings(text):
            base = slugify(title)
            count = seen.get(base, 0)
            seen[base] = count + 1
            found.add(base if count == 0 else f"{base}-{count}")
        cache[path] = found
    return cache[path]


def check_bilingual(errors):
    expected = [ROOT / name for name in BILINGUAL_ROOT_FILES]
    for directory in BILINGUAL_DIRS:
        expected += [p for p in (ROOT / directory).glob("*.md") if not p.name.endswith(ZH_SUFFIX)]
    for english in expected:
        chinese = english.with_name(english.name[: -len(".md")] + ZH_SUFFIX)
        if not chinese.exists():
            errors.append(f"{rel(english)}: missing Chinese counterpart {rel(chinese)}")
    for chinese in ROOT.rglob("*" + ZH_SUFFIX):
        english = chinese.with_name(chinese.name[: -len(ZH_SUFFIX)] + ".md")
        if not english.exists():
            errors.append(f"{rel(chinese)}: missing English counterpart {rel(english)}")
            continue
        en_levels = [level for _, level, _ in headings(english.read_text(encoding="utf-8"))]
        zh_heads = headings(chinese.read_text(encoding="utf-8"))
        zh_levels = [level for _, level, _ in zh_heads]
        if en_levels != zh_levels:
            index = next(
                (i for i, (a, b) in enumerate(zip(en_levels, zh_levels)) if a != b),
                min(len(en_levels), len(zh_levels)),
            )
            where = zh_heads[min(index, len(zh_heads) - 1)][0] if zh_heads else 1
            errors.append(
                f"{rel(chinese)}:{where}: heading structure differs from {rel(english)} "
                f"({len(en_levels)} vs {len(zh_levels)} headings; first difference at heading {index + 1})"
            )


def check_links(errors):
    for path in markdown_files():
        base = STANDARD.parent if path == SNAPSHOT else path.parent
        text = path.read_text(encoding="utf-8")
        for number, line in prose_lines(text):
            for angled, plain in LINK.findall(INLINE_CODE.sub("", line)):
                target = unquote(angled or plain)
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or "<" in target:
                    continue
                file_part, _, fragment = target.partition("#")
                if file_part.startswith("/"):
                    destination = (ROOT / file_part.lstrip("/")).resolve()
                else:
                    destination = (base / file_part).resolve() if file_part else path
                if not destination.exists():
                    errors.append(f"{rel(path)}:{number}: broken link {target}")
                    continue
                if fragment and destination.suffix == ".md" and fragment not in anchors(destination):
                    errors.append(f"{rel(path)}:{number}: missing anchor #{fragment} in {target}")


def check_snapshot(errors):
    standard = STANDARD.read_bytes()
    blob = hashlib.sha1(b"blob %d\0" % len(standard) + standard).hexdigest()
    header, _, body = SNAPSHOT.read_bytes().decode("utf-8").partition("\n")
    match = SNAPSHOT_BLOB.search(header)
    if not match:
        errors.append(f"{rel(SNAPSHOT)}:1: header has no source Git blob")
    elif match.group(1) != blob:
        errors.append(f"{rel(SNAPSHOT)}:1: header blob {match.group(1)} does not match {rel(STANDARD)} blob {blob}")
    if body.removeprefix("\n") != standard.decode("utf-8"):
        errors.append(f"{rel(SNAPSHOT)}: body differs from {rel(STANDARD)}")


def main():
    errors = []
    check_bilingual(errors)
    check_links(errors)
    check_snapshot(errors)
    for error in errors:
        print(error)
    print(f"{len(errors)} problem(s) found" if errors else "Documentation checks passed")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
