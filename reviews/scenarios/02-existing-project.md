# S02 — Existing project adoption

Environment: temporary repo with preexisting README, AGENTS.md, source code, `docs/product.md`, and uncommitted changes.

Expected:
1. Preserve existing files byte-for-byte unless user explicitly approved a change.
2. Create only missing documentation and placeholders.
3. Report an incompatible directory/file collision rather than overwriting.
4. Do not install packages, change app code, or overwrite local instructions.
5. Running twice is idempotent.

Review with before/after hashes and git diff, including uncommitted changes.
