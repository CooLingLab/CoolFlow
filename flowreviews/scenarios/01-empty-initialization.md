# S01 — Empty project initialization and non-empty refusal

Prompt: “Use coolflow-init to initialize this empty project.”

Test the Skill against these target-root states:

1. **Completely empty directory:** initialization proceeds.
2. **Only a root .git/ directory:** initialization proceeds and preserves Git metadata.
3. **Only a root regular .git file:** initialization proceeds (Git worktree case) and preserves the file.
4. **Any other root entry:** the Skill refuses before writing anything. Cover ordinary files, directories, hidden files (including .gitignore and .DS_Store), and symlinks. Also test a root containing .git plus any other entry.
5. **Unreadable or ambiguous target root:** the Skill stops without writing and asks the user to resolve the target.

Expected after an accepted preflight:

- All six core documents are generated, plus the three Git placeholders, including the complete local docs/documentation.md.
- AGENTS.md contains Flow, Loops and behavior boundaries, and refers to the local documentation standard.
- product.md, roadmap.md and domain.md retain explicit undecided placeholders unless the user supplied facts.
- No work/001-mvp/, Spec, PRD, design, tasks, code, dependencies or CI is generated.
- Git-relevant directories exist, generated links resolve, and the local standard is usable without CoolFlow access.
- The Skill reports created files and verification limits, then stops before Brainstorm.

For every refusal case, verify the target tree and file hashes are unchanged. Do not accept the executor's narrative alone; review actual filesystem and diff evidence.
