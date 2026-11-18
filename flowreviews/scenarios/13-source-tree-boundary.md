# S13 — Source tree boundary and prototype disposal

Use a disposable project initialized with the current CoolFlow project templates, an active objective, and a short discovery prototype followed by one implementation increment. The scenario checks that `docs/` remains documentation-only, the Spec records the source layout before implementation, production code and tests live in that source tree, and the prototype is not promoted in place.

## Procedure and expected evidence

1. Initialize an empty project with the current CoolFlow templates. Confirm the documentation skeleton is created, `AGENTS.md` contains `Source code layout: To decide`, and initialization creates no application code, dependencies, CI, prototype or work objective.
2. Start the objective's discovery and create a disposable Step 3 or Step 5 prototype under `docs/work/<objective>/prototypes/`. Record the question, method, result and decision in `brainstorm.md` or `validation.md`. Do not add production build configuration, dependencies, tests or application source under `docs/`.
3. Enter Design Spec Loop and draft the unified Spec. Confirm it records `Repository layout` with the intended source and test paths and build/run commands before implementation begins.
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

Not executed as of 2026-11-18. No PASS is claimed.