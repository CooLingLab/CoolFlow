# S02 — Step 1–5 progress metadata

Prompt: “Set the documentation standard for Step 1–5 progress metadata, then test what can be tested without executing the Skills.”

Scope of this case: the Standard [standards/documentation.md](../../standards/documentation.md), its Chinese counterpart, the project-local copy [templates/project/docs/documentation.md](../../templates/project/docs/documentation.md), the three core templates, and the initialization rules.

## Expected result

1. A dedicated progress-metadata section exists in the Standard, its `.zh-CN.md` counterpart, and the project-local `docs/documentation.md` copy, with the same field set and rule count.
2. The section scopes itself to Step 1–5 documents and explicitly excludes `AGENTS.md`, `README.md`, `docs/documentation.md`, `docs/features/`, `docs/solutions/`, `docs/adr/`, and `spec.md` / `design.md` / `tasks.md`.
3. Required fields are `status` and `related_steps`; `progress_updated`, `current_progress`, `next_steps` and `open_questions` are optional.
4. `product.md` → `[1]`, `domain.md` → `[2]`, `roadmap.md` → `[4]`, each with `status: not_started` and no invented progress text.
5. No core template keeps a legacy `> Status:` line alongside the frontmatter block; status has one authoritative location.
6. The frontmatter block is the first content of the file and precedes the level-one heading.
7. Initialization rules say templates are copied as-is and progress must not be invented.

## Expected vs actual changed files

Expected: `standards/documentation.md`, `standards/documentation.zh-CN.md`, `templates/project/docs/documentation.md`, `templates/project/docs/product.md`, `roadmap.md`, `domain.md`, `standards/initialization.md`, `standards/initialization.zh-CN.md`, plus the files that must stay consistent with the new standard: `templates/project/AGENTS.md` (Working Rules), `skills/coolflow-init/SKILL.md` (initialization placeholder rule), `flowecosystem/framework-comparison.md` and both `methodology/golden-rules*.md` (stale state wording), and the four implemented capabilities: `templates/work/brainstorm.md`, `templates/work/validation.md`, `skills/coolflow-docs-update/`, `skills/coolflow-progress/`, `skills/coolflow-docs-review/`, `README.md`, `README.zh-CN.md`.

Inspect `git diff` and the untracked files for exactly these paths and no unrelated edits.

## What cannot be verified by this case

- Rendered GitHub anchors: the anchor was checked against the slug rule, not against a rendered page.
- The initialization path: `coolflow-init` fetches templates from GitHub `main`, so it cannot exercise these local edits until they are pushed.
- Skill triggering: both new Skills were executed by reading `SKILL.md` directly, because they are not installed as invocable Skills. Whether an ordinary request activates them correctly is not tested. The full Skill also uses `date +%F`-style values; a real session must confirm the date comes from the environment rather than a stale example.

## Execution record

Run date: 2026-11-16. Two throwaway projects were initialized by copying `templates/project/` and committing the result; a separate Agent followed `skills/coolflow-docs-update/SKILL.md` and `skills/coolflow-progress/SKILL.md` without seeing the expected outcome.

**Update run (after the placeholder fix).** Input: confirmed audience, problem and boundaries; a preliminary competitor comparison with no links; two unresolved questions; nothing about UI, prototypes, validation, requirements or roadmap.

- PASS — created `docs/work/001-mvp/brainstorm.md` and edited `docs/product.md` only. No `spec.md`, `prd.md`, `validation.md`, `prototypes/` or second objective directory.
- PASS — confirmed facts went to `product.md`; exploration and the unsourced comparison stayed in `brainstorm.md`, with the comparison labeled preliminary.
- PASS — the new work document contains only the sections with content; it has no `To decide` and no empty heading.
- PASS — the replaced `Current position and evidence` section no longer ends with the template's guidance sentence.
- PASS — only the work record's card carries `open_questions`; `product.md`'s card omits them.
- PASS — cards parse with a real YAML parser (`progress_updated` is a string); `related_steps` is `[1]`; no `> Status:` line; the relative link resolves.
- PASS — nothing was committed and untouched documents were unchanged.

**Progress run.** Input: the same project plus a baseline commit.

- PASS — zero file changes; `git status` clean and HEAD unchanged.
- PASS — read only the progress cards; no document body was opened.
- PASS — all five steps listed, with `not_started` for Steps 2 and 4 and "no record found" for Steps 3 and 5.
- PASS — no step-level status was invented from `related_steps`, no percentage, no invented next action; the report noted that `complete` would not mean accepted and that other sessions and branches are invisible.

**Earlier failing run, kept for history.** The first run left `To decide` under an empty section in a new work document, left a template guidance sentence after real content, and duplicated the same open questions into both cards. Those failures produced the `fix(coolflow-docs-update)` commit; the rerun above is the evidence that the fix works. One occurrence of one scenario is not proof of general reliability.

## Review instructions

Use the Standard text, the templates, `git diff`, and the execution record above as evidence. Report PASS / FAIL / NOT VERIFIED per criterion with concrete file and line evidence. Do not accept a narrative claim in place of the actual files. Do not mark behavioral criteria as PASS without an execution record.
