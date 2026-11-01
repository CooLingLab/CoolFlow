---
name: coolflow-init
description: Initialize an existing or new software project using the CoolFlow documentation standard, generating a concise AGENTS.md, minimum project doc templates, and docs folder skeleton without beginning product development. Use when the user explicitly asks to initialize a project's folders/docs following CoolFlow.
---

# CoolFlow Init

Initialize **only** the documentation skeleton. Never perform brainstorming, create an MVP work folder, write application code, install dependencies, or change CI as a side effect.

## Source of truth

When running from the CoolFlow repository, read:
1. `../../standards/initialization.md`
2. `../../standards/documentation.md`
3. `../../methodology/flow.md`
4. `../../methodology/loops.md`

Templates are under `../../templates/project/`.

If the Skill was installed separately and the relative paths are absent, locate an accessible copy of the canonical [CoolFlow repository](https://github.com/CooLingLab/CoolFlow), read the same files, and *do not invent a substitute standard*. If unable to access them, report the blocker rather than silently guessing.

## Procedure

1. Identify the **target project** (not this Skill repository), its root, existing `AGENTS.md`, `README.md`, docs, and uncommitted user changes.
2. Read the canonical rules and templates; use current project conventions if stronger. Avoid reading unrelated user files.
3. Create only **missing** files at target paths:
   - `AGENTS.md` ← project AGENTS template.
   - `README.md` ← project README template.
   - `docs/product.md`, `docs/roadmap.md`, `docs/domain.md` ← core templates.
   - `docs/features/.gitkeep`, `docs/work/.gitkeep`, `docs/work/archive/.gitkeep` if needed for empty directories in Git.
4. Preserve existing files exactly. In particular, do not overwrite a preexisting project `AGENTS.md` or README. For conflicts or incompatible file types, explain the problem and request authorization before changing anything.
5. Do not fill product facts not provided by the user. The template's `To decide` markers are intentional. If the user explicitly supplied project facts, insert only those facts in their relevant template sections.
6. Verify paths, heading coverage, initial status and links. Re-run should be non-destructive/idempotent.
7. Summarize created, existing and unresolved items. **Stop.** Invite a separate, explicit instruction to start Idea/Brainstorm.

## Important boundaries

- The repository's Standard remains useful even when this Skill is not installed; do not require users to install it.
- Do not force projects to pin upstream CoolFlow versions or migrate when Standard changes.
- A separate `tasks.md` is not an initialization artifact, and is not normally required for everyday implementation.
- Do not claim the initialization succeeded without checking the filesystem or repository changes.
