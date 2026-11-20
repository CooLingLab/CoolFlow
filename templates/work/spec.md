# Unified Spec — <objective>

> Status: Draft

## Context and problem

To decide.

## Goals and non-goals

To decide.

## User-facing behavior and acceptance criteria

To decide. Prefer observable and testable statements.

## Technical design

To decide. Link to `design.md` instead if this becomes too complex.

## Repository layout

To decide. Source code and test paths; build, run and test commands (`none` where a step does not exist); generated or vendored directories. Follow existing project conventions and keep production code outside `docs/`.

## Alternatives, assumptions and trade-offs

To decide.

## Implementation strategy

To decide. A separate `tasks.md` is optional; record critical dependencies here.

## Verification plan

For each acceptance criterion, the check that will prove it. Write the automated checks before the implementation.

| Acceptance criterion | Check | Kind |
| --- | --- | --- |
| To decide | To decide | automated test, type or lint constraint, or manual |

Design constraints enforced by types, lint rules or tests instead of review: To decide. Before feature code, the project needs one command that runs every automated check: the tests and the stack's usual static check (a type checker, or a linter where there is none), and CI that runs it once the repository has a hosted remote. Leaving any of these out is the human's decision: record it here.

## Review and approvals

To decide. Record independent design review findings with their evidence, and important human decisions when applicable. Findings without evidence stay open questions, not blockers.

After coding, record the code review's findings on Spec conformance and codebase design (existing patterns, module interfaces, names against `docs/domain.md` or this Spec's terms) with their evidence, or note that there were none.

## Delivery progress

<!-- Optional until there is evidence. Record each supported field and its scope or revision.
- Implementation: <not_started | in_progress | implemented> — observed changes and scope
- Verification: <not_verified | partially_verified | verified> — checks, results and gaps
- Acceptance: <pending | accepted | accepted_by_policy | changes_requested> — explicit human decision and scope, or, for accepted_by_policy, the declared check's command, base and head revisions, exit status and output summary
- Release: <not_released | released> — authorization, actual outcome and available post-release checks
Use an existing authoritative acceptance or delivery record if project conventions place this information there. -->
