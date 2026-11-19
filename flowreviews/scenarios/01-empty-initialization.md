# S01 — Empty project initialization and non-empty refusal

Prompt: “Use coolflow-init to initialize this empty project.”

Test the Skill against these target-root states:

1. **Completely empty directory:** initialization proceeds.
2. **Only a root .git/ directory:** initialization proceeds and preserves Git metadata.
3. **Only a root regular .git file:** initialization proceeds (Git worktree case) and preserves the file.
4. **Claude Code harness metadata:** initialization proceeds for each of these, leaving the metadata unchanged:
   - an empty `.claude/` only, with and without `.git`;
   - `.claude/.cc-writes/` only, with and without `.git`;
   - `.claude/.cc-writes/` plus `.claude/settings.local.json` as a regular file, with and without `.git`;
   - `.claude/.cc-writes/` containing a transient file (its contents must not affect eligibility or be inspected).
5. **Any other root entry:** the Skill refuses before writing anything. Cover ordinary files, directories, hidden files (including .gitignore and .DS_Store), and symlinks. Also test a root containing .git plus any other entry, root `CLAUDE.md` or `.mcp.json`, `.claude/settings.json`, an unexpected entry inside `.claude/` (for example `commands/` or `agents/`), `.claude` as a regular file or symlink, and `.cc-writes` or `settings.local.json` in the wrong filesystem form (file, directory, or symlink).
6. **Unreadable or ambiguous target root:** the Skill stops without writing and asks the user to resolve the target.

## Hard-gate behavior

For every refusal case, inspect the execution trace as well as the final target tree:

- Once the first complete root listing reveals an ineligible entry, the Skill must stop immediately.
- It must not search for or inspect standards/, methodology/, or templates/ anywhere.
- It must not probe the Skill installation directory or Agent configuration directory for CoolFlow source files (for example, ~/.config/<agent>/standards or ~/.config/<agent>/templates).
- It must not make network requests, create files, or run further shell commands after detecting the refusal condition.
- It must not modify, delete, or add anything to `.claude/` in any case.
- Verify the target tree and file hashes are unchanged.

## Expected after an accepted preflight

- Retrieve the complete standards and templates from the canonical CoolFlow GitHub repository; do not infer a local source path from the Skill installation directory.
- All seven required documents and the three Git placeholders are generated. `docs/coolflow.yml` contains `context_mode: auto`.
- `AGENTS.md` contains stable working boundaries and points to the local context preference and documentation standard. `docs/development-flow.md` contains the eight stages and three Loops and is usable offline.
- product.md, roadmap.md and domain.md retain explicit undecided placeholders unless the user supplied facts.
- No work/001-mvp/, Spec, PRD, design, tasks, code, dependencies or CI is generated.
- The pre-existing `.claude/` harness metadata is unchanged, contains no new files, and is not mentioned in the generated documentation.
- Git-relevant directories exist, generated links resolve, and the local standard is usable without CoolFlow access.
- The Skill reports created files and verification limits, then stops before Brainstorm.

Do not accept the executor's narrative alone; review actual filesystem, command trace and diff evidence.

## Automated checks

`flowreviews/checks/s01_init.py` builds every root state in cases 1–5 as code and judges the mechanical criteria:

```sh
python3 flowreviews/checks/s01_init.py list
python3 flowreviews/checks/s01_init.py build "$TMPDIR/s01" [--only a01-empty,r04-ds-store]
python3 flowreviews/checks/s01_init.py check "$TMPDIR/s01" [--only ...] [--ref origin/main]
```

1. `build` creates each case under `<workdir>/cases/<id>/` and records its tree, file hashes and Git identity in `<workdir>/manifest.json`. Cases prefixed `a` must be accepted; cases prefixed `r` must be refused.
2. Run a fresh Agent in each case directory with the prompt above. Save its tool-call transcript (JSON Lines, such as `claude -p --output-format stream-json` output or a host transcript) as `<workdir>/traces/<id>.jsonl`.
3. `check` reports PASS, FAIL or NOT VERIFIED per criterion and exits non-zero on any FAIL. `--ref` names the Git ref whose templates the Skill fetched; `coolflow-init` fetches from the published `main`, so use `origin/main` until local changes are published.

| Checked by the script | Still needs a reviewer |
| --- | --- |
| Required files and `.gitkeep` placeholders; no other files; `context_mode: auto`; generated files equal the templates; progress cards `not_started`; links resolve; `.git` and `.claude` unchanged; a refused target is byte-for-byte unchanged; from the trace: no network, writes or standards/templates lookup after a refusal, templates fetched from the canonical repository and no local CoolFlow checkout used | Case 6 (unreadable or ambiguous root); whether the refusal message names the ineligible entries; whether the report states its limits and stops before Brainstorm; whether the Agent stopped *immediately* after the first listing |

Trace checks match tool names and command text, so they can miss an obfuscated command; treat their PASS as strong but not conclusive evidence.

## Execution record

**2026-11-19 pilot — 5 of 25 cases, one run each. Overall: 30 PASS, 0 FAIL; the scenario as a whole is NOT VERIFIED.**

Setup: macOS Darwin 27.0.0, Python 3.14.5. The installed `coolflow-init` Skill was byte-identical to `skills/coolflow-init/SKILL.md` (SHA-256 prefix `062fdac591dd179c`). It fetched templates from the published `main`, which matched local `origin/main` at `270a7d0`; the checks used `--ref origin/main`. Checker SHA-256 prefix `0267bf503b8cf23e`. Each case ran in a fresh subagent context with the prompt above plus the target path; the subagents' own transcripts served as traces.

| Case | Expect | Result | Observed |
| --- | --- | --- | --- |
| `a01-empty` | accept | 9/9 PASS | Listed the root, fetched the 12 sources with `curl` from `raw.githubusercontent.com`, wrote the 8 documents and 3 placeholders identical to the templates, checked links, deleted its temporary download. |
| `a09-cc-writes-settings-git` | accept | 9/9 PASS | Same as above; `.git` and the `.claude/` harness metadata were unchanged. |
| `r04-ds-store` | refuse | 4/4 PASS | One listing command, then refused naming `.DS_Store`. |
| `r09-claude-settings-json` | refuse | 4/4 PASS | One listing command (recorded twice in the transcript), then refused naming `.claude/settings.json`. |
| `r12-claude-symlink` | refuse | 4/4 PASS | One listing command with `stat`, then refused naming the `.claude` symlink. |

Reviewer judgment on the non-scripted criteria: all three refusals named the ineligible entry and asked for a separate empty directory; both accepted runs reported created files and limits and stopped before Brainstorm.

Checker self-test before the pilot: simulated correct initializations passed; an extra `docs/work/001-mvp/`, a changed progress card, a modified `settings.local.json`, a modified refused target and synthetic bad traces each failed as expected. The pilot exposed two checker defects, both fixed before the recorded result: trace checks counted the Agent's final report as a source lookup, and the local-checkout check missed a lower-case path to the same case-insensitive directory.

Limitations: the executors were subagents started from the CoolFlow repository with an explicit target path, not fresh Agent sessions opened in each case directory, so harness-created `.claude/` metadata was simulated rather than produced; 20 cases and case 6 were not run; one run per case does not measure variability; trace checks rely on tool names and command text.
