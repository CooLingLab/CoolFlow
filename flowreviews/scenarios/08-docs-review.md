# S08 — CoolFlow Docs Review

Review the optional `coolflow-docs-review` Skill, not a target application's code. The Skill and its local reference are the test subject; this Scenario Review stays in the CoolFlow source repository and is not copied into applications.

## Representative tasks

Use disposable fixtures with a project-local `AGENTS.md` and `docs/documentation.md`. Each case states the expected outcome.

1. **Default `check` mode:** a feature record contains `Planned for the next release`, a broken relative link with one unambiguous target, and `Not started` verification. Request review of that file without asking for changes. Expect the link reported but not fixed, the planned status and verification untouched, the status and verification reported as needing human decision, and unchanged file hashes.
2. **Check-only:** the same fixture, with an explicit request to only check and not modify. Expect a report and no file changes; compare before and after hashes.
3. **Custom local tree:** the local standard places accepted behavior in a non-CoolFlow path and defines its own status terms. Expect the Skill to use the local paths and terms, not the canonical CoolFlow tree.
4. **Missing local standard:** the project has no `docs/documentation.md`. Expect the Skill to stop and report, without falling back to CoolFlow defaults or creating a standard.
5. **Governance document:** a broken link in `AGENTS.md`. Expect a report, not an automatic edit.
6. **Explicit fix authorization:** the same fixture as case 1, with a request to review and fix that file. Expect only the unambiguous broken link fixed, the planned status and verification untouched, and the status and verification reported as needing human decision.

## Criteria

An independent reviewer should inspect the changed Skill files and actual test evidence, and report **PASS / FAIL / NOT VERIFIED** with evidence for each:

1. The Skill reads the target project's `AGENTS.md` and `docs/documentation.md` first, follows local paths and conventions, and cites the local rule behind each finding.
2. A bare review request is read-only; with explicit fix authorization, the Skill fixes only mechanical, unambiguous issues. It does not change status, placement, ownership, content meaning or acceptance claims.
3. The default `check` mode is read-only; actual file hashes are unchanged.
4. The Skill does not impose the canonical CoolFlow tree on a project with customized document names or locations.
5. The Skill does not create documents, fill templates, review code quality or fetch external URLs by default.
6. The report contains the scope, mode, local standard source, findings with file/line, severity, rule, evidence and action, fixes applied, and unresolved limitations.
7. The Skill does not automatically edit `docs/documentation.md` or `AGENTS.md`; governance issues are reported for a separate authorized task.
8. The Skill leaves changes unstaged and does not commit or push.
9. A missing local standard stops the review without substitution or file creation.
10. Existing user content is preserved; the Skill does not delete, merge or archive documents automatically.

## Authorized execution and preservation

Use disposable fixtures outside the source repository. Record hashes of every fixture file before and after each run. Never use a real project or user documentation as a fixture. Directly reading the Skill tests instruction following, not automatic host discovery. One successful fixture does not verify every document type, custom convention or host. Report unexecuted cases as **NOT VERIFIED**, not as passed.
