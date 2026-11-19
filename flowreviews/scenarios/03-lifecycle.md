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

Criteria marked **(M)** are mechanical: a script or a single command over the tree, diff or Git history can decide them. The rest need an independent reviewer.

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
7. The unified `spec.md` records `Repository layout` with source and test paths and build, run and test commands.
8. Every design-review finding cites a Spec section, code, a prototype result or data; unsupported risks are recorded as open questions, not blockers.
9. **(M)** The Spec is committed before any implementation commit.

### 3. Implementation Loop, first session

Ask the Agent to implement the smallest agreed increment, then stop the session before one required check is run.

10. **(M)** Production code and tests live in the recorded source tree, outside `docs/`, and nothing imports from `prototypes/`; the prototype file is unchanged.
11. **(M)** The diff adds no code comments other than tool directives, generated-code markers, license headers or published API documentation comments.
12. The code review records Spec conformance and a codebase-design check: existing patterns and naming against `docs/domain.md`.
13. The Spec's `Delivery progress` records what was implemented and verified, the outstanding check, and pending acceptance.

### 4. Resume in a new session

Start a fresh context with only the project directory and “Continue the current work.”

14. The Agent reads `AGENTS.md` and `docs/coolflow.yml` before enumerating work records.
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

21. Both bypasses are fixed at the root cause, not patched one by one.
22. A mechanism prevents recurrence: an API boundary, a type, a lint rule, a test or a CI check. **(M)** The reviewer reintroduces a bypass and the mechanism rejects it.
23. **(M)** No `AGENTS.md` rule restates what the mechanism enforces. Any new Solution explains the non-obvious reasoning and links the mechanism under Enforcement.

### 7. Evolution

Give three inputs in separate contexts: a defect in the accepted behavior; new evidence that contradicts an assumption in `product.md`; and a request for a new capability.

24. The defect is handled as an Implementation Loop iteration, or returns to Design Spec Loop if it exposes a material Spec flaw; it is not treated as product Evolution.
25. The new evidence triggers Evolution that revisits only the affected steps; the Agent does not restart all eight steps or require a roadmap change by default.
26. **(M)** The new capability lands in the roadmap or a new work objective, not in `docs/features/`.

An independent reviewer inspects the tree, Git history, diffs, Specs, review records, work records and command output, and reports PASS, FAIL or NOT VERIFIED per criterion with evidence. Release, post-release feedback, existing production codebases and other stacks are outside this scenario.

## Execution record

Not yet executed as a merged scenario. Before the merge, two partial runs covered some phases; their findings carry over as evidence for those criteria only.

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

Criteria 1, 2, 5, 6, 8, 11, 12, 18 and 21–26 have never been executed. Former S03 (work objective lifecycle), S04 (acceptance and archive), S06 (Evolution) and S14 (correction hierarchy) were specifications only.
