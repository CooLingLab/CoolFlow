---
name: coolflow-init
description: Initialize a new software project with the CoolFlow methodology and documentation structure. Use only when the user explicitly asks to initialize the current project and its root directory is empty or contains only a root .git directory or file. Do not use for existing or non-empty projects.
---

# CoolFlow Init

Initialize the documentation skeleton for a **new, empty project**. This Skill does not conduct product discovery, create an MVP work folder, write application code, install dependencies, or change CI.

## Mandatory preflight: verify the target directory is empty

The preflight is a hard gate and must finish before any source lookup, network request, or write operation.

1. Identify the exact target project root the user asked to initialize. Normally this is the current workspace root. Do not mistake the Skill installation directory, Agent configuration directory, or CoolFlow source repository for the target. Do not search child directories and choose one automatically.
2. Confirm the target exists and is a directory.
3. Enumerate **all entries at the target root, including hidden entries**. Use a filesystem listing that includes dotfiles; do not rely on a normal directory display or Git status alone.
4. Accept only either:
   - the directory contains no entries; or
   - the directory contains exactly one root entry named `.git`, and that entry is a directory or a regular file (a regular `.git` file is used by Git worktrees).
5. If any other entry exists—including `README.md`, `.gitignore`, `.DS_Store`, any other hidden file, directory, or symlink—**stop the Skill immediately**. Do not continue to the Source of truth section, inspect installation paths, search for standards/templates, make network requests, or run any further commands. Do not create, download, copy, or modify anything.
6. If the target root is ambiguous, does not exist, is not a directory, or its entries cannot be inspected reliably, stop and ask the user to resolve the issue. Never assume it is empty.

When refusing, explain that coolflow-init is only for an empty project directory (optionally containing only root-level `.git` metadata), identify the entries that made it ineligible, and ask the user to open or create a separate empty directory. Do not invoke this Skill for an existing project.

**Terminal refusal rule:** Once the preflight fails, the Skill's execution is over. The refusal response is the only remaining action. In particular, do not attempt to locate or read CoolFlow standards/templates after discovering a non-empty target.

## Source of truth — only after the preflight passes

The canonical standards and templates live in the public CoolFlow repository:

`https://github.com/CooLingLab/CoolFlow`

This Skill is normally installed separately in an Agent's global Skills directory. Its installation directory is **not** a CoolFlow source checkout. Never infer the CoolFlow repository root from the Skill's path or from a matching folder layout such as `skills/coolflow-init/`.

Do not look for `standards/`, `methodology/`, or `templates/` inside:
- the Skill installation directory;
- the Agent configuration directory (for example, an Agent's `~/.config/...` directory);
- the target application directory; or
- any other directory merely because its path appears to be a likely repository root.

After the preflight passes, retrieve the following files directly from the canonical repository using their raw GitHub URLs:

- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/standards/initialization.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/standards/documentation.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/methodology/flow.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/methodology/loops.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/templates/project/AGENTS.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/templates/project/README.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/templates/project/docs/documentation.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/templates/project/docs/product.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/templates/project/docs/roadmap.md
- https://raw.githubusercontent.com/CooLingLab/CoolFlow/main/templates/project/docs/domain.md

Read all required sources completely before writing anything. If any canonical source cannot be accessed or read completely, stop before writing and tell the user what is unavailable. Do not silently guess, clone the repository into the target directory, or copy internal `flowreviews/` materials into the application.

## Procedure

1. Complete and pass the mandatory empty-directory preflight. If it fails, stop immediately; none of the remaining steps apply.
2. Retrieve and read all source-of-truth documents and templates listed above from the canonical CoolFlow repository.
3. Create the following files and directories in the target project:
   - `AGENTS.md` from `templates/project/AGENTS.md`
   - `README.md` from `templates/project/README.md`
   - `docs/documentation.md` from the **complete** `templates/project/docs/documentation.md`
   - `docs/product.md`, `docs/roadmap.md`, and `docs/domain.md` from their matching project templates
   - `docs/features/.gitkeep`, `docs/work/.gitkeep`, and `docs/work/archive/.gitkeep` to preserve the required empty directories in Git
4. Do not create `docs/solutions/` or `docs/adr/` during initialization. They are optional and should appear only when a verified reusable finding or consequential decision warrants them.
5. Do not invent product facts. Keep template placeholders such as `To decide` or `Not started` unless the user explicitly supplied the relevant facts.
6. Do not create `docs/work/001-mvp/`, a Spec, PRD, design, tasks file, prototype, app code, dependencies, CI configuration, or architecture decisions.
7. Verify the created paths, required headings, links, and document completeness against the standards. Do not claim success without checking the actual filesystem or repository changes.
8. Report what was created and any verification limitations. State that the project is initialized and can begin **Step 1 — Idea → Brainstorm** when the user is ready. **Stop here**; do not automatically begin Brainstorm or any implementation.

## Important boundaries

- This Skill is a convenience entry point, not a prerequisite for using CoolFlow. Users may follow the manual instructions in Getting Started instead.
- The Skill is installed for the user's Agent; do not copy the Skill itself into the target application.
- After initialization, the target project follows its own `docs/documentation.md`. Do not require ongoing access to CoolFlow, installation of this Skill in the target project, or tracking of upstream CoolFlow versions.
- Existing projects are handled through **Existing Project Adoption** in Getting Started, not by this Skill. Inspect first, propose a selective adoption plan, and wait for user approval before making changes.
- If initialization fails after some files have been created, report the exact partial result. Do not automatically delete the partial files or bypass the empty-directory preflight on a later run; ask the user how they want to recover.
