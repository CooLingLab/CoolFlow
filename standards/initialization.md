# Project initialization contract

**English** | [简体中文](initialization.zh-CN.md)

**Skill invocation:** “Use coolflow-init to initialize this empty project.”

This is **initialization, not product discovery or implementation**.

## Scope and empty-directory precondition

The coolflow-init Skill is exclusively for a new, empty target project.

- The target root must contain no entries, or exactly one root-level entry named .git.
- The .git entry may be a directory (a normal Git repository) or a regular file (a Git worktree).
- A root-level .claude/ directory created by Claude Code is ignored only under the narrow [Agent harness metadata exemption](#agent-harness-metadata-exemption) below.
- Inspect all root entries, including hidden files. After applying the exemption, any other file, directory, or symlink makes the target non-empty.
- If the target is non-empty, ambiguous, inaccessible, or cannot be inspected reliably, the Skill must stop **before writing anything**. It must not delete, move, rename, or overwrite files to make the directory eligible.
- Do not mistake the Skill's own installation directory or the CoolFlow source repository for the target project.

This restriction applies to coolflow-init. **Do not use the Skill for an existing project.** Follow [Existing Project Adoption in Getting Started](../GETTING_STARTED.md#b-existing-project--inspect-before-adopting) instead.

### Agent harness metadata exemption

Claude Code creates a root-level `.claude/` directory in every directory it opens, before the Skill can run. This is Agent metadata, not project content, so the preflight ignores it only under these constraints:

- `.claude` must be a real directory, not a regular file or symlink.
- All of its immediate entries, if any, must be from this list:
  - `.cc-writes/`, a real directory used by Claude Code for atomic-write staging. It is normally empty; treat its contents as transient Agent state and do not inspect them.
  - `settings.local.json`, a regular file created when the user approves local permissions.
- An empty `.claude/` directory is exempt.
- `.cc-writes` must be a real directory and `settings.local.json` must be a regular file; symlinks with these names are not exempt.
- Any other entry inside `.claude/`—including `settings.json`, `commands/`, `agents/`, or `skills/`—makes the target ineligible.

The exemption affects eligibility only. The Skill must not read the contents of `settings.local.json`, modify, delete, copy, or document this metadata, and must not create files inside `.claude/`. Initialization leaves it unchanged.

A root-level `CLAUDE.md`, `.mcp.json`, `.gitignore`, `.DS_Store`, or any other entry remains ineligible. Other Agents' project configuration directories are not exempt; do not generalize this rule without updating this contract.

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

## Template source and path resolution

Canonical templates live in `templates/project/` in the CoolFlow source repository. When `coolflow-init` is installed globally as a Skill, it must retrieve the standards and templates from the canonical CoolFlow GitHub repository after the target-directory preflight passes.

- Do not infer a CoolFlow repository root from the Skill installation path, Agent configuration directory, or target project directory.
- Do not expect `standards/` or `templates/` to exist beside the installed Skill or inside the Agent configuration directory.
- Do not create local copies of CoolFlow's `standards/` or `templates/` in the target application. Copy only the required project files listed in this contract.
- If the canonical source files cannot be retrieved completely, stop before writing and report the unavailable source.

Copy the required files to the target paths; replace only explicitly supported placeholders. The documentation template implements [the source standard](documentation.md) without links to CoolFlow-only files; keep both aligned when changing the standard.

## Acceptance checks

1. The six required documents exist, including a complete local docs/documentation.md usable without CoolFlow access.
2. Required directories exist in Git.
3. No unintended code, dependencies, product plans, or initial work objective was created.
4. The Skill accepts an empty directory, a directory containing only root-level .git metadata (directory or regular file), and either case combined with only the exempt Claude Code harness metadata (an empty `.claude/` or one containing only `.cc-writes/` and/or `settings.local.json`), leaving that metadata unchanged.
5. The Skill rejects every other root entry—including hidden files and unrecognized entries inside `.claude/`—before any source lookup, network request, or write; refusal leaves the target unchanged and triggers no standards/templates path search.
6. Existing Project Adoption inspects first and makes no changes before the user approves a specific plan.
7. Files and reports contain no fabricated facts.
