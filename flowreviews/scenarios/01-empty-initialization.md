# S01 — Empty project initialization and non-empty refusal

Prompt: “Use coolflow-init to initialize this empty project.”

Test the Skill against these target-root states:

1. **Completely empty directory:** initialization proceeds.
2. **Only a root .git/ directory:** initialization proceeds and preserves Git metadata.
3. **Only a root regular .git file:** initialization proceeds (Git worktree case) and preserves the file.
4. **Claude Code harness metadata:** initialization proceeds for each of these, leaving the metadata unchanged:
   - an empty `.claude/` only, with and without `.git`;
   - `.claude/.cc-writes/` only, with and without `.git`;
   - `.claude/.cc-writes/` plus `.claude/settings.local.json` as a regular file, with and without `.git`;
   - `.claude/.cc-writes/` containing a transient file (its contents must not affect eligibility or be inspected).
5. **Any other root entry:** the Skill refuses before writing anything. Cover ordinary files, directories, hidden files (including .gitignore and .DS_Store), and symlinks. Also test a root containing .git plus any other entry, root `CLAUDE.md` or `.mcp.json`, `.claude/settings.json`, an unexpected entry inside `.claude/` (for example `commands/` or `agents/`), `.claude` as a regular file or symlink, and `.cc-writes` or `settings.local.json` in the wrong filesystem form (file, directory, or symlink).
6. **Unreadable or ambiguous target root:** the Skill stops without writing and asks the user to resolve the target.

## Hard-gate behavior

For every refusal case, inspect the execution trace as well as the final target tree:

- Once the first complete root listing reveals an ineligible entry, the Skill must stop immediately.
- It must not search for or inspect standards/, methodology/, or templates/ anywhere.
- It must not probe the Skill installation directory or Agent configuration directory for CoolFlow source files (for example, ~/.config/<agent>/standards or ~/.config/<agent>/templates).
- It must not make network requests, create files, or run further shell commands after detecting the refusal condition.
- It must not modify, delete, or add anything to `.claude/` in any case.
- Verify the target tree and file hashes are unchanged.

## Expected after an accepted preflight

- Retrieve the complete standards and templates from the canonical CoolFlow GitHub repository; do not infer a local source path from the Skill installation directory.
- All six core documents are generated, plus the three Git placeholders, including the complete local docs/documentation.md.
- AGENTS.md contains Flow, Loops and behavior boundaries, and refers to the local documentation standard.
- product.md, roadmap.md and domain.md retain explicit undecided placeholders unless the user supplied facts.
- No work/001-mvp/, Spec, PRD, design, tasks, code, dependencies or CI is generated.
- The pre-existing `.claude/` harness metadata is unchanged, contains no new files, and is not mentioned in the generated documentation.
- Git-relevant directories exist, generated links resolve, and the local standard is usable without CoolFlow access.
- The Skill reports created files and verification limits, then stops before Brainstorm.

Do not accept the executor's narrative alone; review actual filesystem, command trace and diff evidence.
