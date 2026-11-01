# Project initialization contract

**Skill invocation:** “Use coolflow-init to initialize this empty project.”

This is **initialization, not product discovery or implementation**.

## Scope and empty-directory precondition

The coolflow-init Skill is exclusively for a new, empty target project.

- The target root must contain no entries, or exactly one root-level entry named .git.
- The .git entry may be a directory (a normal Git repository) or a regular file (a Git worktree).
- Inspect all root entries, including hidden files. Any other file, directory, or symlink makes the target non-empty.
- If the target is non-empty, ambiguous, inaccessible, or cannot be inspected reliably, the Skill must stop **before writing anything**. It must not delete, move, rename, or overwrite files to make the directory eligible.
- Do not mistake the Skill's own installation directory or the CoolFlow source repository for the target project.

This restriction applies to coolflow-init. **Do not use the Skill for an existing project.** Follow [Existing Project Adoption in Getting Started](../GETTING_STARTED.md#b-existing-project--inspect-before-adopting) instead.

## Required outcomes

- Follow the [canonical application documentation tree](documentation.md#canonical-application-documentation-tree); do not invent extra default folders or files beyond that tree.
- After the empty-directory precondition passes, create:
  - AGENTS.md
  - README.md
  - docs/documentation.md
  - docs/product.md (the project-level Product Brief, **not a PRD**)
  - docs/roadmap.md
  - docs/domain.md
- Ensure docs/features/, docs/work/, and docs/work/archive/ exist using .gitkeep for Git-only empty directories.
- Do **not** create docs/solutions/ or docs/adr/ during initialization; both are optional and should appear only when a verified reusable finding or consequential decision warrants them.
- Fill **AGENTS.md** with the concise eight-stage Flow, three Loops and agent behavior rules; refer to docs/documentation.md for documentation rules.
- Copy the complete templates/project/docs/documentation.md to docs/documentation.md. It is the project's local standard after initialization and can evolve independently without accessing CoolFlow.
- Fill other docs with **templates**, not fabricated product facts. If user provides actual facts, fill only facts they authorized; otherwise keep Not started or To decide.
- Do **not** create docs/work/001-mvp/, spec.md, PRD, prototype, task file, app code, dependencies, CI, or architecture decisions.
- Run a consistency check on paths and required headings. Report created files, any verification limitations, and the next optional action. Stop without starting Brainstorm.

## Existing project adoption (separate from this Skill)

- Never invoke coolflow-init in a non-empty project.
- For an existing project, follow the inspect-first process in [Getting Started](../GETTING_STARTED.md#b-existing-project--inspect-before-adopting).
- First inspect the existing architecture, instructions, documentation, conventions and relevant work. Summarize the actual state and propose the smallest useful, selective adoption plan.
- Do not create the full CoolFlow documentation tree or modify any files before the user approves a specific plan.
- After approval, change only the agreed files. Preserve existing content, project-specific instructions, code, and uncommitted work. Report conflicts instead of silently replacing anything.
- Adoption does not require restarting at Idea or adopting every CoolFlow stage.

## Template source

Canonical templates live in templates/project/. Copy the required files to the target paths; replace only explicitly supported placeholders. The documentation template implements [the source standard](documentation.md) without links to CoolFlow-only files; keep both aligned when changing the standard. If the template is unavailable, provide an equivalent complete, self-contained local standard from that source, not a summary or broken links.

## Acceptance checks

1. The six required documents exist, including a complete local docs/documentation.md usable without CoolFlow access.
2. Required directories exist in Git.
3. No unintended code, dependencies, product plans, or initial work objective was created.
4. The Skill accepts an empty directory and a directory containing only root-level .git metadata (directory or regular file).
5. The Skill rejects every other root entry—including hidden files—before writing anything; refusal leaves the target unchanged.
6. Existing Project Adoption inspects first and makes no changes before the user approves a specific plan.
7. Files and reports contain no fabricated facts.
