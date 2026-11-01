# S02 — Existing project adoption (not CoolFlow Init)

Prompt: “Inspect my existing project and propose how to adopt CoolFlow for [specific feature or fix].”

Environment: temporary repo with preexisting README, AGENTS.md, source code, docs/product.md, docs/documentation.md, and uncommitted changes.

Expected:

1. The Agent does **not** invoke coolflow-init; the Skill is only for an empty target directory and must refuse this project.
2. The Agent inspects the actual project structure, instructions, architecture, documentation, conventions and relevant work before recommending changes.
3. It summarizes the current state and proposes the smallest useful, selective CoolFlow adoption plan for the specified need.
4. It makes **no file changes** before the user approves a specific plan. Existing files, local standards, code and uncommitted changes remain byte-for-byte unchanged during inspection.
5. The proposal does not require creating the full CoolFlow documentation tree, restarting at Idea, or adopting every stage.
6. After explicit approval, only the agreed changes may be applied; incompatible conventions and risks are reported rather than silently overwritten.

Review with before/after hashes and git diff, including uncommitted changes. The initial inspection-and-proposal phase must have no diff.
