# CoolFlow internal scenario reviews

This directory contains internal validation scenarios for **CoolFlow itself**. They check whether CoolFlow's Standards, templates, Skills and initialization guidance produce the expected results. They are not unit or integration tests for applications built with CoolFlow.

Keep these files in the CoolFlow source repository, including its public `main` branch and published source releases. They are repository-maintenance materials, not application templates. **Never copy `flowreviews/` into a target application** when initializing or adopting CoolFlow.

An independent Agent (using a different context from the implementer when practical) should inspect the scenario, applicable Standard, resulting files / diff, and any runnable evidence. It should report PASS, FAIL or NOT VERIFIED **for each criterion, with specific evidence**.

Suggested result format:
- Case ID and execution environment
- Expected vs actual changed files
- Per-criterion judgment plus file/diff evidence
- Critical failures and proposed corrections
- Explicitly state what could not be tested

Prefer deterministic checks wherever a criterion is mechanical. A scenario may ship a checker under `flowreviews/checks/` that builds its fixtures as code and judges file trees, hashes, contents and tool-call traces; the reviewer then judges only what the script cannot. S01 is the first scenario with a checker. A static rule about CoolFlow's own files, such as template content, belongs in `scripts/check_docs.py`, not in a scenario.

## Scenarios

| ID | Scenario | Subject |
| --- | --- | --- |
| S01 | [Empty project initialization](01-empty-initialization.md) | `coolflow-init`, including manual initialization without the Skill |
| S02 | [Existing project adoption](02-existing-project.md) | Adoption instead of initialization; no change before approval |
| S03 | [Development lifecycle](03-lifecycle.md) | One project from discovery through both Loops, acceptance, archive and Evolution |
| S04 | [Acceptance tiers](04-acceptance-tiers.md) | Opt-in `accepted_by_policy` |
| S05 | [Docs update](05-docs-update.md) | `coolflow-docs-update` |
| S06 | [Docs review](06-docs-review.md) | `coolflow-docs-review` ([results](06-docs-review-results.md)) |
| S07 | [Advisor](07-advisor.md) | `coolflow-advisor` ([results](07-advisor-results.md)) |
| S08 | [Skill creator](08-skill-creator.md) | `coolflow-skill-creator` ([results](08-skill-creator-results.md)) |

Each scenario starts with a `Covers:` line. Re-run a scenario when a file it covers changes; there is no requirement to run every scenario for every change. Execution records written before the 2026-11-19 renumbering may use earlier IDs.

## Keeping the set small

- Each Skill has one scenario, and the lifecycle has one. A new rule adds checkpoints or criteria to the scenario it affects rather than a new scenario.
- Add a scenario only for a boundary or risk that no existing scenario can exercise, and give it a `Covers:` line.
- Remove a scenario whose subject no longer exists, and keep a completed one-off experiment in Git history rather than in this directory.

Do not mark unexecuted cases as PASS. These scenarios remain in the CoolFlow source repository; they are not copied into application repositories.
