# S13 — Source tree boundary and prototype disposal

Use a disposable project initialized with the current CoolFlow project templates, an active objective, and a short discovery prototype followed by one implementation increment. The scenario checks that `docs/` remains documentation-only, the Spec records the source layout before implementation, production code and tests live in that source tree, and the prototype is not promoted in place.

## Procedure and expected evidence

1. Initialize an empty project with the current CoolFlow templates. Confirm the documentation skeleton is created, `AGENTS.md` contains `Source code layout: To decide`, and initialization creates no application code, dependencies, CI, prototype or work objective.
2. Start the objective's discovery and create a disposable Step 3 or Step 5 prototype under `docs/work/<objective>/prototypes/`. Record the question, method, result and decision in `brainstorm.md` or `validation.md`. Do not add production build configuration, dependencies, tests or application source under `docs/`.
3. Enter Design Spec Loop and draft the unified Spec. Confirm it records `Repository layout` with the intended source and test paths and build/run commands. Commit the Spec before implementation so the ordering is mechanically verifiable.
4. Implement the smallest agreed increment in the recorded source tree. Production code and tests must not import from `docs/work/<objective>/prototypes/`, and the prototype must not be edited or extended into the application.
5. Inspect the tree and diff. `docs/` must contain no production source, package manifest, lockfile, dependency directory or build output. The prototype remains linked evidence; accepted behavior reaches `docs/features/` only after explicit human acceptance.

## Criteria

1. Initialization created only documentation, with no application code, dependencies, CI, prototype or work objective.
2. The prototype lives under `docs/work/<objective>/prototypes/` and remains disposable evidence; no production code, test or build setup depends on it.
3. The Spec records `Repository layout` with source and test paths and build/run commands before implementation.
4. Production code and tests are located at the recorded source tree, outside `docs/`.
5. `docs/` contains no application build or dependency setup, such as `package.json`, a lockfile, `node_modules/`, `dist/` or the equivalent for the chosen stack.
6. After acceptance, `docs/features/` records accepted behavior and the work record retains the prototype evidence and Spec; no prototype code was promoted by incremental cleanup.

An independent reviewer must inspect the initialized tree, the Spec, the code diff and the work records, and report PASS, FAIL or NOT VERIFIED per criterion with specific file or command evidence. One run does not establish behavior across stacks, frameworks or existing codebases.

## Execution record

The 2026-11-18 run used macOS Darwin 27.0.0, Node.js v24.22.2 and a disposable fixture at `/tmp/claude-501/s13-fixture`. A fresh executor initialized the fixture from the current project templates; an independent reviewer inspected the artifacts without modifying them. Fixture commits: `2b2e0dc` (baseline skeleton), `e5020e3` (implementation), `7c80584` (delivery progress), `617a1f3` (acceptance and feature sync). The final worktree was clean.

**Overall: 5 PASS, 0 FAIL, criterion 3 partially NOT VERIFIED; the overall run is NOT VERIFIED.**

| Criterion | Result | Evidence |
| --- | --- | --- |
| 1. Initialization only documentation | PASS | Baseline `git ls-tree` lists only `AGENTS.md`, `README.md` and `docs/`; no source, package files, CI, prototype or work objective. `AGENTS.md` contains `Source code layout: To decide`; `docs/documentation.md` contains the docs-only scope statement. |
| 2. Prototype location and disposal | PASS | The prototype is at `docs/work/001-habit-cli/prototypes/streak-prototype.mjs`, with its question and result recorded in `validation.md`. `grep` found no production or test import from `docs/work`, `prototypes` or the prototype, and no build setup under `docs/`. The prototype was added once and never edited; after acceptance it moved unchanged to `docs/work/archive/001-habit-cli/prototypes/streak-prototype.mjs`. |
| 3. Spec records Repository layout before implementation | NOT VERIFIED (content PASS) | `spec.md` records `src/`, `test/`, `Build: none`, `Run: node src/cli.mjs <command> [habit]` and `Test: node --test`, matching the actual tree. However, the Spec first appears in `e5020e3`, the same commit that adds all source and tests, and file timestamps also show the Spec written after the source. The ordering cannot be established from the artifacts. |
| 4. Production code and tests at the recorded source tree | PASS | Actual `src/` and `test/` files match the Spec's layout and remain outside `docs/`; no production code exists under `docs/`. |
| 5. `docs/` contains no build or dependency setup | PASS | `git ls-files docs/` contains documentation, `.gitkeep` markers, the prototype and later the feature record; no `package.json`, lockfile, `node_modules`, `dist`, build output or CI configuration. |
| 6. Post-acceptance feature record and retained evidence | PASS | The human operator explicitly accepted the fixture behavior on 2026-11-18. `docs/features/habit-cli.md` records accepted behavior, constraints, verification and links to the archived Spec, validation, prototype and brainstorm; 19 relative links checked, 0 broken. The work directory moved to `docs/work/archive/001-habit-cli/` with the Spec, validation, prototype and brainstorm retained; the prototype is byte-identical and was not promoted. The Spec records `accepted` and `not_released`. |

Independent checks: `node --test` reported 36 tests, 36 pass, 0 fail, exit 0; the archived prototype reported 12/12 cases passed, exit 0; `node src/cli.mjs list` printed `No habits yet.` and exited 0.

No criterion violation was found. One minor non-criterion defect remains: `docs/work/archive/001-habit-cli/validation.md` still contains the pre-archive command path `node docs/work/001-habit-cli/prototypes/streak-prototype.mjs`, which no longer resolves after the move; the archived path works. This weakens reproducibility from the archived record but does not invalidate the retained evidence.

Limitations: one Node.js stack, one greenfield run and one fixture; the executor's authorship independence and the human acceptance statement cannot be independently observed from the artifacts alone; the reviewer ran `list` and the test suites but not the manual `add`/`done` sequence, to keep the fixture read-only; cross-stack, existing-codebase, multi-day and concurrent-process behavior remain untested.

**Process change:** The procedure now requires committing the Spec before implementation. This run predates that change, so criterion 3's ordering remains NOT VERIFIED; a future run can establish it mechanically.
