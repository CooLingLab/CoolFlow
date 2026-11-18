# Project Agent Instructions

## Project Context

For project planning, changes in product direction, or requests to resume work without a named objective, first check `docs/coolflow.yml` and [CoolFlow context preference](docs/documentation.md#coolflow-context-preference). Resolve the mode before searching work records. Missing configuration defaults to `manual`. For a named objective, Spec, or concrete maintenance task, skip the mode check and read the relevant files directly. For explicit requests to review the methodology or report project progress, use [Development Flow](docs/development-flow.md) or the relevant project records.

## Documentation

Follow `docs/documentation.md` when creating, updating or archiving project documents.

## Working Rules

1. Read the files relevant to the current task; do not assume an empty template is complete.
2. Preserve existing project content, conventions and code. No destructive replacement without permission.
3. Do not invent requirements, user decisions or successful tests. Untouched core templates keep `status: not_started` and body unknowns stay `To decide`; a work card may be `in_progress` only when that work has actually begun.
4. For substantial changes: review the current Spec draft and related context before coding, resolve important findings and confirm design readiness; run relevant tests, review new code and verify Spec conformance after coding.
5. AI may implement and verify routine work. Ask the human to decide major product trade-offs and to accept the result.
6. Record human-confirmed plans with their actual status; sync durable docs describing accepted/current behavior after human acceptance. Obtain separate authorization for any release and verify its outcome.
7. Manage ordinary task lists in the active Agent session.
8. Before related work, consult relevant existing Solutions when available.
9. When appropriate, especially for applications and deployed services, commit the package manager's lockfile and configure CI to install in frozen/locked mode. Libraries that intentionally publish dependency ranges may omit it; record that choice and have CI test the supported range.

## Project-specific Conventions

- Product / stack: To decide.
- Build and test commands: To decide.
- Other project constraints: To decide.
