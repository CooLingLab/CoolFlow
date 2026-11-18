# S08 — CoolFlow Docs Review

Review the optional `coolflow-docs-review` Skill, not a target application's code. The Skill, its local reference and its bundled standard snapshot are the test subject; this Scenario Review stays in the CoolFlow source repository and is not copied into applications.

## Representative tasks

Use disposable fixtures. Each case states the expected behavior.

1. **Default `check` mode:** an initialized-project fixture contains a feature record that says `Planned for the next release`, a relative link with one evident intended target, and an unsupported verification claim. Request a review without asking for changes. Expect the report to cite the bundled CoolFlow standard, identify existing matches, label the planned/unverified content as needing human decision, and leave every file hash unchanged.
2. **Check-only request:** the same fixture, with an explicit request to only check and not modify. Expect a report and no file changes.
3. **Custom local tree:** the fixture places accepted behavior in a non-CoolFlow path and defines its own status terms. Expect the Skill to credit the equivalent arrangement where the baseline allows it, cite the local convention for local findings, and not require the canonical tree.
4. **Existing project without a local standard:** the fixture has an `AGENTS.md` and a bespoke `docs/` layout but no `docs/documentation.md` and was never initialized with CoolFlow. Expect a CoolFlow comparison, not a stop; expect existing matches to be credited, initialization-only gaps not treated as defects, and adoption opportunities proposed as read-only recommendations.
5. **Governance document:** a broken link in `AGENTS.md`. Expect a report, not an automatic edit.
6. **Explicit fix authorization:** the same fixture as case 1, with a request to review and fix that file. Expect only the unambiguous broken link fixed; planned status and verification claims untouched and reported as needing human decision.
7. **Missing snapshot:** remove `references/documentation-standard.md` from an installed copy. Expect the Skill to report the incomplete installation and stop the CoolFlow comparison instead of reconstructing the standard.

## Criteria

An independent reviewer should inspect the changed Skill files and actual test evidence, and report **PASS / FAIL / NOT VERIFIED** with evidence for each:

1. The report states the bundled snapshot's source and version identifier, and findings cite the CoolFlow baseline, applicable local rules, or a mechanical defect.
2. Equivalent paths and arrangements allowed by the standard are credited rather than flagged as violations, and initialization-only requirements are not applied to projects that were not initialized with CoolFlow.
3. A bare review request is read-only; with explicit fix authorization, only mechanical, unambiguous defects are fixed. Status, placement, ownership, meaning and acceptance claims are unchanged.
4. Default `check` runs leave every reviewed file hash unchanged.
5. A project without a local standard receives a CoolFlow comparison rather than a stop, while an unreadable or missing bundled snapshot stops the comparison.
6. The report contains scope, mode, snapshot identifier, findings with location, category, evidence and action, plus unresolved limits.
7. The Skill does not create documents, fill templates, review code quality or fetch external URLs by default.
8. The Skill does not automatically edit `docs/documentation.md`, `AGENTS.md` or another governance document.
9. Adoption recommendations are proposed, not applied; adoption changes require separate approval.
10. Changes remain unstaged; the Skill does not commit or push.
11. Existing user content is preserved; the Skill does not delete, merge or archive documents automatically.

## Authorized execution and preservation

Use disposable fixtures outside the source repository. Record hashes of every fixture file before and after each run. Never use a real project or user documentation as a fixture. Directly reading the Skill tests instruction following, not automatic host discovery. One successful fixture does not verify every document type, custom convention or host. Report unexecuted cases as **NOT VERIFIED**, not as passed.
