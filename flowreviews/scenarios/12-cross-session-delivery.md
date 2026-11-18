# S12 — Resume a delivery from its Spec

Use a disposable Node.js CLI project with the CoolFlow project rules and documentation standard, `context_mode: auto`, and one active work objective. The fixture's search command performs case-insensitive substring matching. It initially returns `No matches` for `node bin/search.mjs ' APP '` even though `node bin/search.mjs 'APP'` returns `Apple`. The fix should ignore surrounding whitespace and preserve blank-query and substring behavior.

## Procedure and expected evidence

1. In the first Agent context, reproduce the bug through the CLI, draft a concise unified Spec, show a regression test failing against the original code, then fix the defect and run the unit tests. Leave the repaired CLI invocation for the next context. Record implementation and partial verification in the Spec, with the remaining check and pending human acceptance.
2. Start a fresh Agent context with the application directory and the request “Continue the current work.” Check whether it reads `context_mode` before looking up the objective, finds the existing Spec, identifies the outstanding check, and actually runs the CLI. Check that it updates the same Spec without duplicating the record or reopening discovery.
3. Review the code, tests, command output and before/after checkpoints independently. Keep human acceptance pending until the operator explicitly accepts the behavior. After that decision, verify that the acceptance record and affected durable document agree. Record actual release status for the trial.

Keep the execution results in this source repository. The trial project only needs its own project files and work records.

## Execution record

The 2026-11-18 run used Node.js v24.22.2 and separate executor contexts on a local fixture with one objective. The fixture contains a runnable CLI and uses Node's built-in test runner. The first executor read the recording Skill directly.

The first session reproduced the CLI mismatch on the baseline. With four additional unit cases, `node --test` failed 2 of 6 tests before the fix and passed all 6 after the fix. The objective Spec then recorded `implemented`, `partially_verified`, `pending` acceptance, and `not_released`. It identified the CLI check as outstanding. An independent reviewer checked the source diff, regression logs, and saved Spec checkpoint. The snapshot establishes the checkpoint contents. The initial drafting time remains unverified.

| Criterion | Result | Evidence |
| --- | --- | --- |
| Continue from the existing Spec | PASS | Given the app directory and “Continue the current work,” the second executor opened the unique Spec, identified the pending CLI checks, and updated the same record to `verified`. Acceptance remained `pending` at this checkpoint. |
| Resolve mode before searching work records | FAIL for file enumeration | The executor's access log reports a recursive `find . -type f` before reading `AGENTS.md` and `docs/coolflow.yml`. It opened the Spec content after reading `auto`. This run shows that a generic repository scan can enumerate work paths before the mode check. |
| Verify the actual behavior | PASS | The second executor ran 6 unit tests and 6 CLI invocations. The coordinator repeated both suites with the same results. `' APP '`, `' app '`, and `'APP'` printed `Apple`. An empty string and a whitespace-only string printed `No matches`. `'pea'` printed `Pear`. All invocations exited 0. |
| Record human acceptance and sync | PASS | The user explicitly accepted the verified fixture behavior. The existing Spec recorded `accepted` and linked to `docs/features/search.md`, which describes the current behavior and links back to the Spec. The trial remained local and `not_released`. |

This run covers one seeded defect in a disposable CLI with one active objective. Skill discovery, repeatability across tools, and work in an existing production project remain unverified.
