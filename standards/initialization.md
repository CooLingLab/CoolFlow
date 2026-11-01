# Project initialization contract

**Invocation:** “参考 CoolFlow，帮我初始化当前项目的文件夹结构和开发文档。暂时不要开发 App。”

This is **initialization, not product discovery or implementation**.

## Required outcomes

- Follow the [canonical application documentation tree](documentation.md#canonical-application-documentation-tree); do not invent extra default folders or files beyond that tree.

- Check repository status and existing files first. Never overwrite, delete or silently rewrite user files.
- Create missing: `AGENTS.md`, `README.md`, `docs/product.md` (the project-level Product Brief, **not a PRD**), `docs/roadmap.md`, `docs/domain.md`.
- Ensure `docs/features/`, `docs/work/`, and `docs/work/archive/` exist using `.gitkeep` for Git-only empty directories.
- Do **not** create `docs/solutions/` or `docs/adr/` during initialization; both are optional and should appear only when a verified reusable finding or consequential decision warrants them.
- Fill **AGENTS.md** with self-contained concise eight-stage Flow, three Loops, documentation locations, accepted/in-progress separation, and agent behavior rules.
- Fill other docs with **templates**, not fabricated product facts. If user provides actual facts, fill only facts they authorized; otherwise keep `Not started`.
- Do **not** create `docs/work/001-mvp/`, `spec.md`, PRD, prototype, task file, app code, dependencies, CI, or architecture decisions during initialization.
- Run a consistency check on paths and required headings. Report new vs pre-existing files, conflicts, and next optional action. Stop.

## Existing project handling

- Idempotent: run again without altering existing content.
- Create only missing files/directories by default. If a file is already present but nonconforming, report that and offer a non-destructive proposed edit; do not silently replace it.
- `AGENTS.md` written for a new project summarizes guidance **within the project**; existing project-specific instructions take precedence over generic templates.
- Do not demand that the initialized project install `coolflow-init`, fetch CoolFlow on every run, or track upstream CoolFlow version.

## Template source

Canonical examples live in `templates/project/`. Copy the required files to the target paths; replace only explicitly supported placeholders. When original templates are unavailable, follow this contract and [documentation standard](documentation.md).

## Acceptance checks

1. Exactly the five minimum document *types* above exist (additional existing user documents are allowed).
2. Required directories exist in Git.
3. No unintended code, dependencies, product plans, or initial work objective was created.
4. Re-running initialization preserves current file contents.
5. All files and reports avoid fictitious facts.
