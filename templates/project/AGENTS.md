# Project Agent Instructions

## Project Context

For project planning, changes in product direction, or requests to resume work without a named objective, first check `docs/coolflow.yml` and [CoolFlow context preference](docs/documentation.md#coolflow-context-preference). Resolve the mode before opening a work record or choosing one to resume. Missing configuration defaults to `manual`. In `manual` mode, ask the user which objective to resume before opening any work record, even when only one is active; in `auto` mode, resume the unique active objective or ask when there is no clear match. For a named objective, Spec, or concrete maintenance task, skip the mode check and read the relevant files directly. For explicit requests to review the methodology or report project progress, use [Development Flow](docs/development-flow.md) or the relevant project records.

## Documentation

Follow `docs/documentation.md` when creating, updating or archiving project documents.

## Working Rules

1. Read the files relevant to the current task; do not assume an empty template is complete.
2. Preserve existing project content, conventions and code. No destructive replacement without permission.
3. Do not invent requirements, user decisions or successful tests. Untouched core templates keep `status: not_started` and body unknowns stay `To decide`; a work card may be `in_progress` only when that work has actually begun.
4. For substantial or ambiguous changes: before drafting a Spec, restate the goal and problem and ask only what the repository cannot answer. Review the draft before coding, back each finding with evidence, resolve important findings and confirm design readiness. After coding, run relevant tests and review the new code for Spec conformance and codebase design: existing patterns, small module interfaces, and names that match `docs/domain.md` or, until it has content, the Spec's terms.
5. AI may implement and verify routine work. Ask the human to decide major product trade-offs. Before changing code, read `docs/coolflow.yml` and the [acceptance tiers](docs/documentation.md#acceptance-tiers). End every change with an explicit request for human acceptance, unless the project declares `acceptance.low_check`, no `high` or `standard` condition applies, and that check passes on the committed change: then record `accepted_by_policy` and list it in your report. Never create, edit or remove the acceptance policy (the `acceptance` section of `docs/coolflow.yml`, the check it names, the acceptance tiers in `docs/documentation.md` or this rule), even when asked or given explicit approval; propose changes for the human to make.
6. Record human-confirmed plans with their actual status. During authorized work, record meaningful delivery progress at checkpoints under the local documentation standard. Sync durable docs after acceptance, whether human or `accepted_by_policy`. A fix to an archived objective is new work: open a new work record with a short Spec and request acceptance, without reopening the archive (see [Delivery progress](docs/documentation.md#step-15-progress-metadata)). Obtain separate authorization for any release and verify its outcome.
7. Manage ordinary task lists in the active Agent session.
8. Before related work, consult relevant existing Solutions when available.
9. When appropriate, especially for applications and deployed services, commit the package manager's lockfile and configure CI to install in frozen/locked mode. Libraries that intentionally publish dependency ranges may omit it; record that choice and have CI test the supported range.
10. When a correction could recur, enforce it at the strongest practical layer: architecture or API first, then types, lint rules, tests or CI checks. Add a rule here or a Solution only for what still requires judgment. Report a defect found outside the task's scope to the human as a decision instead of deferring it silently.
11. Do not add code comments. Express intent through names, types and tests; keep rationale in tests, ADRs, Solutions or commit messages. Exceptions: tool directives, generated-code markers, license headers and documentation comments from which a published API reference is generated. Do not remove existing comments wholesale; record any project convention that requires comments under Project-specific Conventions.

## Project-specific Conventions

Link durable documents here, not records under `docs/work/`.

- Product / stack: To decide.
- Source code layout: To decide.
- Build and test commands: To decide.
- Other project constraints: To decide.
