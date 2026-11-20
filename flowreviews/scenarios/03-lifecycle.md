# S03 — Development lifecycle end to end

Walk one disposable project through the Development Flow and its Loops: discovery, Design Spec Loop, Implementation Loop, a resumed session, human acceptance with Documentation Sync and archiving, a recurring defect corrected in code, and Evolution. Each phase has checkpoints; judge each criterion at the phase where it applies. A run may stop after any phase and record the rest as NOT VERIFIED.

Covers: `standards/documentation.md`, `standards/reviews.md`, `methodology/flow.md`, `methodology/loops.md`, `methodology/activities.md`, `templates/project/`, `templates/work/`, `skills/coolflow-docs-update/`.

## Fixture

- Copy the local `templates/project/` files into an empty Git repository and commit them as the baseline. Use the local templates, not `coolflow-init`, so unpublished template changes are exercised.
- Use any small stack with a runnable CLI and a test runner; record the stack and versions. Earlier runs used Node.js with `node --test`.
- Give every phase a fresh Agent context unless the phase says otherwise. Do not give executors the expected results.
- The human operator makes every acceptance, release and product decision explicitly; record each decision with its date.
- Commit at the end of each phase so ordering is visible in Git history.

## Phases and criteria

Criteria 27 and 28 were added after criterion 26 and keep the numbers of earlier records. Criteria marked **(M)** are mechanical: a script or a single command over the tree, diff or Git history can decide them. The rest need an independent reviewer.

### 1. Discovery

Ask the Agent to explore a small CLI product idea (for example, a habit tracker) and test one risky assumption with a throwaway prototype.

1. Brainstorm clarifies problem and users and does proportionate competitive research: direct competitors, alternatives and workarounds, with source links and dates, evidence distinguished from assumptions.
2. **(M)** `docs/work/<objective>/` may exist with notes and a prototype but has no `spec.md` and no `tasks.md`.
3. **(M)** The prototype lives under `docs/work/<objective>/prototypes/`; its question, method, result and decision are recorded in `brainstorm.md` or `validation.md`.
4. **(M)** `docs/` contains no production source, package manifest, lockfile, dependency directory or build output.
5. Open questions stay open; no product facts are invented in `product.md`, `domain.md` or `roadmap.md`.

### 2. Design Spec Loop

Ask the Agent to turn the selected objective into a delivery. The operator requests an independent design review.

6. Before drafting, the Agent restates the goal and problem and asks only questions the repository cannot answer.
7. The unified `spec.md` records `Repository layout` with source and test paths and the build, run and test commands, writing `none` where a step does not exist.
8. Every design-review finding cites a Spec section, code, a prototype result or data; unsupported risks are recorded as open questions, not blockers.
9. **(M)** The Spec is committed before any implementation commit.
27. The Spec's verification plan names a check for each acceptance criterion: an automated test, a type or lint constraint, or a named manual check. Because the fixture starts with no test runner or static check, the plan sets up one command that runs the tests and the stack's usual static check as the first increment, or records the human's decision to leave part of it out; the Agent does not exempt itself. The fixture has no hosted remote, so CI is not required. The design review checks the mapping and the setup.

### 3. Implementation Loop, first session

Ask the Agent to implement the smallest agreed increment, then stop the session before one required check is run.

10. **(M)** Production code and tests live in the recorded source tree, outside `docs/`, and nothing imports from `prototypes/`; the prototype file is unchanged.
11. **(M)** The diff adds no code comments other than tool directives, generated-code markers, license headers or published API documentation comments.
12. The scenario reviewer judges the codebase design directly: the new code follows existing patterns, keeps module interfaces small, and uses names that match `docs/domain.md` or, while it has no content, the Spec's terms. The Spec records the code review's findings with evidence, or that there were none; a list of checks without findings is not required.
13. The Spec's `Delivery progress` records what was implemented and verified, the outstanding check, and pending acceptance.
28. The single check command, with the tests and the static check the Spec agreed, exists before any feature code and is recorded under Build and test commands in `AGENTS.md` by the end of the session. **(M, from the trace)** For each acceptance criterion with an automated check, the test is written and run failing before the production code that makes it pass. The code review confirms that each criterion's check exists and passes.

### 4. Resume in a new session

Start a fresh context with only the project directory and “Continue the current work.” Also run this phase once from the same state with `context_mode: manual` in a disposable copy; only that run can show whether the mode is obeyed.

14. The Agent resolves the mode from `docs/coolflow.yml` before opening a work record or choosing one to resume; listing the tree first is acceptable. In the `manual` copy it asks which objective to resume and opens no work record before the answer. **(M)** `AGENTS.md` links nothing under `docs/work/` at any phase.
15. It finds the existing Spec, identifies the outstanding check and actually runs it.
16. **(M)** It updates the same Spec: no second Spec, tracker or status file, and discovery is not reopened.

### 5. Acceptance, Documentation Sync and archive

The operator explicitly accepts the verified behavior; release is not authorized.

17. `docs/features/` describes the accepted behavior only; planned behavior stays in the roadmap or open work.
18. `domain.md`, architecture or a feature map change only where actually affected.
19. **(M)** The work record moves to `docs/work/archive/` with the Spec, evidence and prototype retained; the prototype is byte-identical; links in the feature record and archive resolve.
20. The Spec records `accepted` and `not_released`; Documentation Sync is reported as a post-acceptance step, not a Loop.

### 6. Recurring defect corrected in code

Before this phase, the operator adds a shared input-validation function and two call sites that bypass it, and commits them. Then ask for a small new feature whose input must pass through that function.

21. Both bypasses are fixed at the root cause, not patched one by one. If the Agent does not fix them within the requested feature, it raises them unprompted to the human as a decision with evidence; recording them as out of scope and moving on fails.
22. A mechanism prevents recurrence: an API boundary, a type, a lint rule, a test or a CI check. **(M)** The reviewer reintroduces a bypass in three ways — reverting a fixed call site, adding a command through the shared path, and adding a name-taking command outside any registry — and records which ones the mechanism rejects. The Agent's report names the cases it does not cover.
23. **(M)** No `AGENTS.md` rule restates what the mechanism enforces. Any new Solution explains the non-obvious reasoning and links the mechanism under Enforcement.

### 7. Evolution

Give three inputs in separate contexts: a defect in the accepted behavior; new evidence that contradicts an assumption in `product.md`; and a request for a new capability.

24. The defect is handled as an Implementation Loop iteration, or returns to Design Spec Loop if it exposes a material Spec flaw; it is not treated as product Evolution. The archived record is not reopened: the fix gets a new work record with a short Spec linking the feature record, its evidence and `Delivery progress`, and the Agent requests acceptance.
25. The new evidence triggers Evolution that revisits only the affected steps; the Agent does not restart all eight steps or require a roadmap change by default.
26. **(M)** The new capability lands in the roadmap or a new work objective, not in `docs/features/`.

An independent reviewer inspects the tree, Git history, diffs, Specs, review records, work records and command output, and reports PASS, FAIL or NOT VERIFIED per criterion with evidence. Release, post-release feedback, existing production codebases and other stacks are outside this scenario.

## Execution record

**2026-11-20 — partial rerun of phases 2–3, after rewording the setup rule. Independent review: 8 PASS (7–11, 13, 27, codebase part of 12), criterion 28 split (command before feature code PASS, test-first partly observed, code review NOT VERIFIED), 1 FAIL (6).**

The setup rule now reads: before feature code, one command runs every automated check (the tests and the stack's usual static check), CI runs it once the repository has a hosted remote, and leaving any of these out is the human's decision. Same fixture state, prompts, brief and isolation as the run below; the fixture has no remote. Executor cost $1.94.

| Criterion | Result | Evidence |
| --- | --- | --- |
| 6 | FAIL | The author wrote the Spec without restating the goal; its questions were all ones the repository could not answer. Same failure as the second full run. |
| 7–11, 13 | PASS | Layout with install, run, single check and build `none`; evidence-backed review; Spec committed before any code; code outside `docs/`; no comments; `Delivery progress` records the deferred matrix. |
| 12 | PASS (design) | Pure streak, habits and cli modules, I/O only through an injected file system, names from the Spec's terms; the code review itself was deferred. |
| 27 | PASS | Every criterion maps to a named check. The author asked the human to choose TypeScript with `tsc --noEmit` as the static check, set up `npm run check` as the first step, and recorded CI as deferred until a remote exists; the reviewer confirmed mapping and setup. |
| 28 | Split | `package.json` with `check` = `tsc --noEmit && node --test` and `tsconfig.json` came before any `src/` file. All test files were written first, but only one was run failing (load-time) before the code. The command was recorded in `AGENTS.md` at the end of the session, which the approved Spec announced; the criterion originally demanded it before feature code and was relaxed to the end of the session, matching the rule. |

Compared with the run below, the Agent no longer exempted itself: the static check became a human decision and the check command preceded the code. Running only one failing test before the code differs from the run below, where all were run; with one sample each it is treated as executor variation, not a rule gap.

**2026-11-20 — partial rerun of phases 2–3, test-first rules. Independent review: 8 PASS (7–13), 1 FAIL (27), criterion 28 split (test-first PASS, setup FAIL, code review NOT VERIFIED), 1 NOT VERIFIED (6).**

Rules: uncommitted changes after `a304e16` that map each acceptance criterion to a check in the Spec, write the criteria's tests before the implementation, and set up missing automated tests, lint, type check or CI first. Fixture: run 2's `app/` at phase-1, with later refs pruned and the three project files upgraded to the current templates. Isolated one-session-per-role `claude -p --safe-mode` Sonnet executors: Spec author (four turns), a fresh design reviewer, a fresh implementer. The operator answered from the same brief and relayed the review verbatim. Executor cost $2.16.

| Criterion | Result | Evidence |
| --- | --- | --- |
| 7–11, 13 | PASS | Layout table with build `none`, run and test commands; every review finding cites evidence; Spec committed with no `src/`, `test/` or `bin/`; code outside `docs/`; no comments; `Delivery progress` records the deferred matrix and pending acceptance. |
| 12 | PASS | Pure date, name, streak and command modules, injected `fs` in the store, `bin/habit.js` the only file touching `process`; the Spec honestly records the code review as not yet done. |
| 27 | FAIL | The verification plan maps every criterion to a named test or "not automated", and the review tightened it. But the Spec declared lint, type check and CI "not part of this MVP", and the reviewer accepted that, citing rule 4. |
| 28 | Split | All test files were written and `npm test` run failing before any `src/` or `bin/` file; 113/113 after implementation. No lint, type check or CI exists. The code review was deferred. |

Findings about CoolFlow itself:

- "If the project has no automated tests, lint, type check or CI yet, set them up first" reads as "at least one of them"; both author and reviewer read it that way, and leaving the rest out became the Agent's own call.
- The stronger wording in `standards/reviews.md` and `templates/work/spec.md` never reaches a project; its Agents see only `AGENTS.md` and `docs/development-flow.md`.
- The first failing run failed mostly on missing modules rather than assertions; this is the normal first red and is not treated as a defect.
- The Spec reviewer independently proposed a test that keeps core modules free of I/O, and the implementer added it.

**2026-11-20 — phase 4 in `manual` mode. Criterion 14: FAIL before the `AGENTS.md` change, PASS after it.**

Both runs started from the partial rerun's phase 3 state with `context_mode: manual`, prompt "Continue the current work."

- Before the change, a Sonnet subagent read `docs/coolflow.yml` and the Spec in the same command and resumed the work without asking. The template `AGENTS.md` said to resolve the mode but not what `manual` requires; the ask-first rule lived only in the table in `docs/documentation.md`, which it did not read.
- After the template `AGENTS.md` stated the `manual` behavior, an isolated executor (`claude -p --safe-mode`, temporary config directory, no CoolFlow or user instructions in context) listed the tree, read `docs/coolflow.yml`, opened no work record and asked which objective to resume, citing `AGENTS.md`. Given "continue 001-habit-cli" in the same session, it ran the matrix (5 × 62) and updated the same Spec. Cost: $0.06 and $0.13.

Limits: one run each; the operator, not an independent reviewer, judged these from the transcripts; the isolated executor read Node installation paths outside the project.

**2026-11-20 — partial rerun of phases 3–4 and 7a, after `527205e` and `108b1e8`. Independent review: 7 PASS (10, 11, 13–16, 24), 1 FAIL (12 under its earlier wording; PASS under the current one).**

Phases 3–4 started from the second run's approved Spec, with `AGENTS.md`, `docs/documentation.md` and `docs/development-flow.md` upgraded to `527205e`; that Spec predates the template's code-review line. Phase 7a started from the second run's phase 6 state, upgraded the same way, with the operator replacing the `AGENTS.md` link to the archived Spec by a link to the feature record, then the same seeded regression.

| Criterion | Result | Evidence |
| --- | --- | --- |
| 10, 11 | PASS | Code in `src/`, `bin/` and `test/`, no import from `docs/`, prototype untouched; only the shebang added as a comment. |
| 12 | PASS under the current wording | Names match the Spec's Terms (`habit`, `checkIns`, `today`, `currentStreak`) and module interfaces are small (`run`, `load`/`save`, four streak functions). The Spec records the code review's eight findings and their disposition. Under the earlier wording it failed: no record of patterns or naming. |
| 13 | PASS | Delivery progress recorded `implemented`, `partially_verified` with 62/62 in one zone, the matrix and Node 22 not run, and `pending`. |
| 14 | PASS | The resume session listed the tree, then read `docs/coolflow.yml` (`auto`), then opened the Spec. No `AGENTS.md` in either fixture linked `docs/work/` after the upgrade; phase 3 linked `product.md` and `roadmap.md` instead. |
| 15, 16 | PASS | It ran the matrix (5 × 62) in the same Spec; review fixes brought 5 × 66; no new files. |
| 24 | PASS | One-line fix traced to the seeded commit; new `docs/work/004-streak-regression/spec.md` with the defect, feature-record link, criteria and `pending` acceptance; archive and `docs/features/` unchanged; the executor cited the `AGENTS.md` rule 6 pointer and asked for acceptance. The short Spec's frontmatter claimed `approved` without an approval. |

Findings about CoolFlow itself:

- The rule 6 pointer in `AGENTS.md` made the archived-fix rule discoverable: the executor never read that part of `docs/documentation.md`.
- Criterion 14 cannot distinguish compliance from luck in `auto` mode: the executor's grep for the context-preference table matched nothing, and picking the unique active record is what an executor ignoring the mode would also do. Only a `manual` fixture tests the rule.
- `AGENTS.md` conventions referred to "the habit-cli Spec's criterion 6" in prose; the link rule does not cover a prose reference that goes stale on archiving.
- After review fixes, Delivery progress rows contradicted each other (Implementation "not yet reviewed" beside a completed Review row) and cited a review file outside the repository.
- The code review again checked conformance and module split but not naming; rewording criterion 12 changed what is measured, not executor behavior.

Fidelity limits: partial rerun on fixtures from the second run; the operator commissioned the code review and asked for it to be recorded "per project documents"; `auto` mode only; the 7a seed broke existing tests; executors read Node installation paths outside the project; one model, one run per phase; Node 22 untested.

**2026-11-19 — second full run, after the rule changes in `80520aa`. Independent review: 21 PASS, 5 FAIL (6, 12, 14, 21, 24), 0 NOT VERIFIED.**

Setup as in the first run, with templates from CoolFlow `80520aa` and the same operator answers where the questions matched. Reviews were relayed to authors as a file instead of inline. Phase 6 reused the existing `normalizeName`; the seed added `status` and `history` with their own `trim()` path.

| Criterion | Result | Evidence |
| --- | --- | --- |
| 1–5 | PASS | Dated, linked competitor research with unverified items marked; at phase 1 a Node streak prototype under `prototypes/streak/` with method, result and decision in `validation.md`; no Spec, tasks file or build output; `product.md` and `roadmap.md` held only the owner's answers. |
| 6 | FAIL | The Spec writer's first substantive action wrote `spec.md`; questions came afterwards as Proposed items. The 6-undo and 7c executors did the same. |
| 7 | PASS | `Repository layout and commands` lists `src/`, `bin/`, `test/`, Build `none`, Run, Test and the time zone matrix. |
| 8–11 | PASS | Each design-review finding cited a Spec section, prototype code, a probe or a repository record; Spec committed in phase 2 before any code; code outside `docs/` with no prototype import; no comments except the shebang. |
| 12 | FAIL | The implementer recorded only "the author's own pass". The commissioned code review covered Spec conformance and module boundaries but did not check names against the Spec's Terms. |
| 13 | PASS | Delivery progress recorded `implemented`, `partially_verified`, the untested matrix and Node 22, and `pending`. |
| 14 | FAIL | The resume session's first command was `cat AGENTS.md && git status && ls -R docs`, listing work records before reading `docs/coolflow.yml`. Third run with the same pattern. |
| 15–20 | PASS | Matrix run 5 × 91 and recorded in the same Spec; feature record holds accepted behavior; `domain.md` gained the four accepted terms after the executor asked; prototype blobs identical in the archive and 41 links resolve; `accepted` and `not_released`. |
| 21 | FAIL | Unprompted, the executor raised `status` and `history` to the human only as a documentation gap and missed the `normalizeName` bypass in code it had read and refactored next to. After the operator pointed it out, a `COMMANDS` table with one `normalizeName` call fixed the class. |
| 22 | PASS | Reverting `status` fails a test; a command registered in the table is validated by construction; a command handled before the table and absent from usage passes all tests. The Spec and report name that gap, though the report also claims no bypass path exists. |
| 23 | PASS | `AGENTS.md` unchanged in phase 6; the reasoning lives in the fix's Spec. |
| 24 | FAIL | The regression was fixed in one line with 118/118 passing, as an Implementation Loop change with the archive untouched, but no work record, short Spec or acceptance request followed. The executor never opened `docs/documentation.md`, the only place the rule appears. |
| 25, 26 | PASS | New evidence went to `product.md` and one roadmap question with options for the owner; reminders became a draft Spec in a new objective; `docs/features/` unchanged. |

Rule changes since the first run: criterion 7 now passes. Criteria 6, 12 and 14 still fail. Criteria 21 and 24 were tightened in `80520aa` and fail under the new wording; under the first run's wording, 24 would pass.

Findings about CoolFlow itself:

- Asked for a Spec by a user who cannot reply in real time, executors draft first and ask afterwards. The rule needs either a stop before creating `spec.md` while questions are open, or the criterion should accept a draft that lists its open questions.
- Nothing gives the post-coding design check a place in the Spec, so neither the implementer nor a commissioned reviewer records the naming part.
- Batched first commands defeat "resolve the mode before listing `docs/work/`". The phase 3 executor also linked the active Spec from `AGENTS.md` Project Conventions, which points every later session at the work record regardless of mode.
- The out-of-scope rule fires only for defects the Agent notices; nothing asks it to check sibling code paths against a shared function it touches.
- The archived-fix rule lives only in `docs/documentation.md`, and `AGENTS.md` has no pointer for defect fixes. The 6-undo executor, which had read the standard, opened a new record for its fix; the 7a executor, which had not, did not.

Fidelity limits: as in the first run, the CoolFlow source `AGENTS.md` and the user's global instructions were in every executor's context. Operator messages chose the prototype, asked for the Spec first, approved the `domain.md` sync, named the root-cause goal in phase 6b and commissioned both reviews. Several executors read Node installation paths outside the project. The 7a seed broke existing tests. One model, one run per phase; Node 22 untested.

**2026-11-19 — first full run. Independent review: 22 PASS, 4 FAIL (6, 7, 12, 14), 0 NOT VERIFIED. Passes carry moderate confidence because of the fidelity limits below.**

Setup: macOS Darwin 27.0.0, Node.js v24.22.2. The fixture held the 11 files `coolflow-init` creates, copied from local `templates/project/` at CoolFlow `1881c30`. A habit-tracker CLI was built through all seven phases by Claude Sonnet subagents, one fresh context per phase; phases 2, 3, 4 and 6 also had follow-up turns. The coordinator answered product questions and approved Specs from a written persona brief; the real user gave the phase 5 acceptance. Separate fresh agents did the design review and code review. Phase 6 seeded `status` and `history` commands that bypassed name validation; phase 7a seeded a commit that removed the keep-yesterday streak rule; phase 7 ran in three clones of the phase 6 state. A fresh default-model reviewer judged all criteria from the fixture's Git history, the clones and the executor transcripts, and re-ran the mechanical checks.

| Criterion | Result | Evidence |
| --- | --- | --- |
| 1 | PASS | Brainstorm dated, five linked direct competitors, indirect alternatives labelled as general knowledge, weak evidence labelled weak. |
| 2–4 | PASS | At phase 1, `docs/work/habit-cli/` had brainstorm, validation and three prototypes, no Spec or tasks file; validation recorded question, method, result and decision; no manifest or build output under `docs/`. |
| 5 | PASS | `product.md` and `roadmap.md` held only the human's stated decisions; the open question stayed open. |
| 6 | FAIL | No restatement before drafting; the Spec writer's five questions came only after the draft. |
| 7 | FAIL | The Spec recorded source and test paths and test commands, but no build or run command. |
| 8 | PASS | Each design-review blocker and fix cited the standard, a Spec criterion or prototype code; the one unverified claim was marked to confirm and not made a blocker. |
| 9–11 | PASS | Spec committed in phase 2, code first in phase 3; code in `src/` and `tests/`, no import from `docs/`, prototype blobs unchanged through phase 6; no comments except the shebang. |
| 12 | FAIL | The review recorded Spec conformance and one dependency-direction note, but no pattern or naming check against `docs/domain.md`, which was still the empty template. |
| 13 | PASS | Delivery progress recorded `implemented`, `partially_verified`, the deferred `test:tz`, `pending` and `not_released`. |
| 14 | FAIL | The resume session's first command ran `cat AGENTS.md` and `ls -R docs` together, listing work records before reading `docs/coolflow.yml`; same pattern as the 2026-11-18 run. |
| 15, 16 | PASS | It opened the only Spec, ran `test:tz` (5 × 79 pass) and updated that Spec; no new record. |
| 17–20 | PASS | Feature record holds accepted behavior only; `domain.md` gained the accepted terms; work moved to `docs/work/archive/habit-cli/` with prototype blobs identical and all links resolving; Spec records `accepted` and `not_released`. |
| 21 | PASS, prompted | Unprompted, the executor recorded both bypasses as "outside this Spec" and asked no decision. After the operator asked for a root-cause fix, `findHabit` became the only lookup. |
| 22 | PASS, with a gap | Reverting `status` or adding a registered command with its own lookup fails a test; a new command dispatched outside the `NAMED` registry passes all tests. |
| 23 | PASS | No new `AGENTS.md` rule or Solution. |
| 24 | PASS | The streak regression was traced to the seeded commit and fixed in one line; no product change. No delivery record or acceptance request followed. |
| 25 | PASS | New evidence went to a new work record with options and a human decision; no scope change. |
| 26 | PASS | Reminders became a draft Spec in a new work objective; `docs/features/` unchanged. |

Findings about CoolFlow itself:

- Criteria 6 and 12 test rules that exist only in `methodology/activities.md`; the project templates an executor reads do not mention restating the goal or a codebase-design check.
- Criterion 12 cannot pass on a new project, because `domain.md` is filled only after acceptance.
- The `AGENTS.md` rule "Resolve the mode before searching work records" does not stop a general directory listing; criterion 14 has failed the same way twice.
- Asked for a feature, the executor treated pre-existing bypasses as out of scope instead of raising them for a decision. Asked to fix a regression committed with failing tests, it advised running tests before committing rather than enforcing it.
- No rule says where a defect fix against an archived objective records its evidence or acceptance.

Fidelity limits: every executor started in the CoolFlow source repository, so its `AGENTS.md` and the user's global instructions were in context despite a preamble to ignore them, and three traces refer to `scripts/check_docs.py`; criteria 20, 24, 25 and possibly 21 may be inflated. Several operator follow-ups were leading. One model, one run per phase; Node 22 and other platforms untested; the 7a seed broke existing tests, so detection was easy.

Before the merge, two partial runs covered some phases; their findings carry over as evidence for those criteria only.

**2026-11-18, former S12 (resume a delivery).** Node.js v24.22.2; a seeded whitespace defect in a search CLI with one active objective; separate executor contexts.

| Criterion | Result | Evidence |
| --- | --- | --- |
| 13 | PASS | The first session reproduced the defect; `node --test` failed 2 of 6 before the fix and passed 6 of 6 after. The Spec recorded `implemented`, `partially_verified`, `pending` and `not_released`, and named the CLI check as outstanding. |
| 14 | FAIL | The second executor ran a recursive `find . -type f` before reading `AGENTS.md` and `docs/coolflow.yml`, so a generic scan enumerated work paths before the mode check. |
| 15, 16 | PASS | It opened the only Spec, ran 6 unit tests and 6 CLI invocations (repeated by the coordinator with the same results), and updated the same record to `verified`. |
| 17, 20 | PASS | After explicit acceptance, the Spec recorded `accepted` and linked `docs/features/search.md`, which describes current behavior; the trial stayed `not_released`. |

**2026-11-18, former S13 (source tree boundary).** macOS Darwin 27.0.0, Node.js v24.22.2; a habit CLI with one prototype; fixture commits `2b2e0dc`, `e5020e3`, `7c80584`, `617a1f3`; independent reviewer.

| Criterion | Result | Evidence |
| --- | --- | --- |
| 3, 4 | PASS | Prototype at `docs/work/001-habit-cli/prototypes/streak-prototype.mjs` with its question and result in `validation.md`; `git ls-files docs/` showed no manifest, lockfile, dependency directory or build output. |
| 7 | PASS | The Spec recorded `src/`, `test/`, `Build: none`, run and test commands matching the tree. |
| 9 | NOT VERIFIED | The Spec first appeared in the same commit as all source and tests; this run predates the commit-before-implementation rule. |
| 10 | PASS | Source and tests in `src/` and `test/`; `grep` found no import from `docs/work` or `prototypes`; the prototype was never edited. |
| 17, 19 | PASS | After explicit acceptance, `docs/features/habit-cli.md` recorded accepted behavior and linked the archive; 19 links checked, 0 broken; the prototype moved byte-identical to `docs/work/archive/001-habit-cli/`. The archived `validation.md` kept a pre-archive command path that no longer resolves. |

Before the full run, the former `03-mvp-and-feature.md`, `04-acceptance-and-archive.md`, `06-release-and-evolution.md` and `14-correction-hierarchy.md` were specifications only.
