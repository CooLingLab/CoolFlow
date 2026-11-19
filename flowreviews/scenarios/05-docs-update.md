# S05 — Docs update: progress cards and delivery progress

Evaluate the `coolflow-docs-update` Skill and its supporting documentation rules. Keep this internal CoolFlow scenario in the source repository. Use a disposable project, a fresh Agent and direct reading of the Skill; this is not automatic-discovery testing.

Covers: `skills/coolflow-docs-update/`, the progress-metadata and delivery-progress sections of `standards/documentation.md` and `templates/project/docs/documentation.md`, `templates/project/docs/` cards, `templates/work/`. `scripts/check_docs.py` checks the template cards themselves: card first, `status: not_started`, the right `related_steps`, no legacy `> Status:` line.

## Step 1–5 card case

The project was initialized by copying `templates/project/` and committed. The session confirmed audience, problem and boundaries; produced a preliminary competitor comparison without links; left two questions open; and said nothing about UI, prototypes, validation, requirements or roadmap.

Ask the Agent to update the project documents from this session's work.

Expected:

1. It creates `docs/work/<objective>/brainstorm.md` and edits `docs/product.md` only: no `spec.md`, `prd.md`, `validation.md`, `prototypes/` or second objective.
2. Confirmed facts go to `product.md`; exploration and the unsourced comparison stay in `brainstorm.md`, labeled preliminary.
3. The new work document contains only sections with content: no `To decide` and no empty heading. Replaced template sections lose their guidance sentence.
4. Open questions appear on one card only, not duplicated across cards.
5. Cards parse with a YAML parser, `related_steps` stays correct, no `> Status:` line is added, and links resolve.
6. Nothing is committed and untouched documents are unchanged.

## Delivery progress case

The project has an existing search objective Spec and the default documentation standard. The session established that implementation is complete and code/Spec-conformance review found no unresolved issues; `npm test -- search` passed on 2026-11-18, the required manual empty-state verification was not run; the human explicitly accepted the actual flow on 2026-11-18; no release was authorized or performed.

Ask the Agent to update the project documents from this session's work.

Expected:

1. The existing Spec gains one `Delivery progress` record with `Implementation: implemented`, `Verification: partially_verified` including the test evidence and manual gap, `Acceptance: accepted` with the human's decision, and `Release: not_released`. The fixture already has an authoritative accepted-feature record for this behavior, so no new feature document is needed.
2. The Agent does not create a new Spec, tracker or status file, and does not add Step 1–5 cards to the Spec.
3. It preserves existing document content and does not claim release.
4. The report identifies the files and fields actually changed.
5. The documentation standard, its Chinese counterpart, project-local template, Spec template, Advisor and documentation-review guidance are consistent with this record's fields and evidence rules.

An independent reviewer must inspect the changed files and evidence, and report PASS, FAIL or NOT VERIFIED per criterion. One run per case does not establish automatic updating at every task end, repeatability or correct handling of later code changes.

## Execution record

**2026-11-18 — delivery progress case.** A fresh Agent read the revised Skill directly (SHA-256 `673c8df511b74f08d1053ca60f0a05a9821a64a1b8809546dcb91a60a1711417`) and updated the disposable fixture. The independent Agent reported PASS on all five criteria for this run.

| Criterion | Evidence |
| --- | --- |
| 1 | `docs/work/search/spec.md` gained one delivery section. For search r1 it recorded `implemented`, `partially_verified` with the test result and manual check gap, `accepted` with the human decision, and `not_released` with no authorization or execution. |
| 2 | The fixture file list stayed the same. The Spec retained `> Status: Approved` and gained no frontmatter card. |
| 3 | The before and after diff showed only the appended section. All five other project document hashes matched, including `docs/features/search.md`. |
| 4 | The executor named the Spec as the only changed project file and listed all four fields in its report. |
| 5 | Static review found matching field values and evidence rules across the standards, templates and relevant Skills. The English standard and project documentation template had identical delivery sections. |

The test command output was supplied as fixture input. No application test was run. Automatic discovery, repeated updates, handling of a later revision, and Advisor and review Skill behavior with delivery records remain unverified.

**2026-11-16 — Step 1–5 card case** (recorded then as S02, progress metadata). A separate Agent followed the Skill without seeing the expected outcome. All six criteria passed: it created `docs/work/001-mvp/brainstorm.md` and edited only `docs/product.md`; kept the unsourced comparison in `brainstorm.md`, labeled preliminary; left no `To decide` or empty heading and removed the replaced guidance sentence; put `open_questions` only on the work record's card; produced cards that parse as YAML with `related_steps: [1]` and no `> Status:` line; and committed nothing. An earlier run had failed criteria 3 and 4, which produced the `fix(coolflow-docs-update)` commit; the passing run is after that fix. The Skill hash was not recorded.
