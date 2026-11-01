---
name: coolflow-init
description: Initialize a new software project with the CoolFlow methodology and documentation structure. Use only when the user explicitly asks to initialize the current project and its root directory is empty or contains only a root .git directory or file. Do not use for existing or non-empty projects.
---

# CoolFlow Init

Initialize the documentation skeleton for a **new, empty project**. This Skill does not conduct product discovery, create an MVP work folder, write application code, install dependencies, or change CI.

## Mandatory preflight: verify the target directory is empty

This check is the first operation that may inspect the target project. Do not create, download, copy, or modify anything in the target directory before it passes.

1. Identify the exact target project root the user asked to initialize. Normally this is the current workspace root. Do not mistake the Skill installation directory or CoolFlow source repository for the target. Do not search child directories and choose one automatically.
2. Confirm the target exists and is a directory.
3. Enumerate **all entries at the target root, including hidden entries**. Use a filesystem listing that includes dotfiles; do not rely on a normal directory display or Git status alone.
4. Accept only either:
   - the directory contains no entries; or
   - the directory contains exactly one root entry named .git, and that entry is a directory or a regular file (a regular .git file is used by Git worktrees).
5. If any other entry exists—including README.md, .gitignore, .DS_Store, any other hidden file, directory, or symlink—**stop immediately without making any changes**. Do not delete, move, rename, ignore, or overwrite anything to make the directory pass.
6. If the target root is ambiguous, does not exist, is not a directory, or its entries cannot be inspected reliably, stop and ask the user to resolve the issue. Never assume it is empty.

When refusing, explain that coolflow-init is only for an empty project directory (optionally containing only root-level .git metadata), identify the reason, and ask the user to open or create a separate empty directory. Do not invoke this Skill for an existing project.

## Source of truth

After the preflight passes, read the canonical CoolFlow standards and templates. Do not guess or replace them with a summary.

When running from a CoolFlow source checkout, use:
1. standards/initialization.md
2. standards/documentation.md
3. methodology/flow.md
4. methodology/loops.md
5. The required files under templates/project/

When installed separately, retrieve those same files from the canonical repository:
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

If the canonical sources cannot be accessed or read completely, stop before writing and tell the user what is unavailable. Do not silently guess, clone the repository into the target directory, or copy internal flowreviews materials into the application.

## Procedure

1. Complete and pass the mandatory empty-directory preflight.
2. Read the source-of-truth documents and templates listed above.
3. Create the following files and directories in the target project:
   - AGENTS.md from templates/project/AGENTS.md
   - README.md from templates/project/README.md
   - docs/documentation.md from the **complete** templates/project/docs/documentation.md
   - docs/product.md, docs/roadmap.md, and docs/domain.md from their matching project templates
   - docs/features/.gitkeep, docs/work/.gitkeep, and docs/work/archive/.gitkeep to preserve the required empty directories in Git
4. Do not create docs/solutions/ or docs/adr/ during initialization. They are optional and should appear only when a verified reusable finding or consequential decision warrants them.
5. Do not invent product facts. Keep template placeholders such as To decide or Not started unless the user explicitly supplied the relevant facts.
6. Do not create docs/work/001-mvp/, a Spec, PRD, design, tasks file, prototype, app code, dependencies, CI configuration, or architecture decisions.
7. Verify the created paths, required headings, links, and document completeness against the standards. Do not claim success without checking the actual filesystem or repository changes.
8. Report what was created and any verification limitations. State that the project is initialized and can begin **Step 1 — Idea → Brainstorm** when the user is ready. **Stop here**; do not automatically begin Brainstorm or any implementation.

## Important boundaries

- This Skill is a convenience entry point, not a prerequisite for using CoolFlow. Users may follow the manual instructions in Getting Started instead.
- The Skill is installed for the user's Agent; do not copy the Skill itself into the target application.
- After initialization, the target project follows its own docs/documentation.md. Do not require ongoing access to CoolFlow, installation of this Skill in the target project, or tracking of upstream CoolFlow versions.
- Existing projects are handled through **Existing Project Adoption** in Getting Started, not by this Skill. Inspect first, propose a selective adoption plan, and wait for user approval before making changes.
- If initialization fails after some files have been created, report the exact partial result. Do not automatically delete the partial files or bypass the empty-directory preflight on a later run; ask the user how they want to recover.
