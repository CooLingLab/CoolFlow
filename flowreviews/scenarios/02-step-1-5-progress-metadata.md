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

- Behavioral use: the update and progress Skills now exist but have not been executed, so "update the card during a session", "summarize Step 1–5", and "distinguish `not_started` from no record" remain **NOT VERIFIED**. Static agreement between a Skill's instructions and the Standard is not evidence that an Agent follows them.
- Rendered GitHub anchors: the anchor was checked against the slug rule, not against a rendered page.
- The initialization path: `coolflow-init` fetches templates from GitHub `main`, so it cannot exercise these local edits until they are pushed.
- General YAML parsing: PyYAML is unavailable in the environment; the block was checked with a strict line-based parser only.

## Review instructions

Use the Standard text, the templates, and `git diff` as evidence. Report PASS / FAIL / NOT VERIFIED per criterion with concrete file and line evidence. Do not accept a narrative claim in place of the actual files. Do not mark behavioral criteria as PASS.
