# Documentation review checks

These are generic review prompts. The project's local documentation standard decides which checks apply and what counts as a violation. A check not covered locally is **not specified**, not a violation.

Use the local standard's own terms and examples. The notes below describe the canonical CoolFlow tree only as an illustration; a project may customize names and locations.

## 1. Placement and lifecycle

- Is the document in a location the local standard defines for its type?
- Are the documents the local standard requires at initialization present? Missing required documents are findings; do not create them during a review.
- Is a feature record describing only behavior that is actually implemented and accepted? Planned, proposed or future behavior belongs in the roadmap or an open work record.
- Was a work objective's `spec.md` created only when the objective entered Design Spec Loop? Discovery notes may exist without a Spec.
- Are optional records such as solutions, ADRs, architecture and feature maps created only for a real need? Is each fact in its narrowest durable home?
- After acceptance, were accepted facts synced before work was archived? Does the archive retain useful Specs, decision rationale and verification evidence?
- Is this document a second authority for a fact owned elsewhere?

Typical severity: `error` for a clear lifecycle violation, `warning` for a likely one, `info` when the local standard is silent.

## 2. Structure and purpose

Use the local standard's purpose statements, not a preferred template. For the canonical CoolFlow tree, check:

- `product.md`: problem, audience, vision, value, boundaries and current positioning; it is a Product Brief, not a PRD.
- `roadmap.md`: MVP/current version, later direction and priority; planned and accepted scope are explicit.
- `domain.md`: ubiquitous language, domain boundaries and core rules; provisional content is allowed.
- `features/`: accepted behavior, constraints and verification; link supporting evidence.
- `work/<objective>/spec.md`: context, goal and non-goals; user requirements and acceptance criteria; design decisions and trade-offs; implementation strategy, dependencies and validation; open questions and assumptions distinguished from decisions.
- `solutions/`: one focused, verified, reusable finding with evidence; not raw logs, unverified guesses or obvious code behavior.
- `adr/`: context, decision drivers, options, decision and consequences; one consequential decision per file; superseded records are retained.
- `architecture.md`: current system architecture, not decision rationale.
- `feature-map.md`: actual navigation, actions, stable test identifiers and verification steps; not a duplicate of `features/`.
- `README.md` and `AGENTS.md`: accurate navigation; `AGENTS.md` contains a self-contained lifecycle and working boundaries and references the local documentation standard.

Do not require every optional artifact. Do not enforce headings or sections the local standard does not require.

Typical severity: `warning` for missing required content, `info` for a possible improvement.

## 3. Truth and status

- Are observed facts, user claims, decisions, unverified findings, assumptions and open questions distinguishable?
- Is planned behavior labeled as planned or proposed, not described as accepted or current?
- Is accepted behavior recorded in the appropriate current document, not only in a work record?
- Are `Not started` and `To decide` treated as unknown, not as completed?
- Are test results, acceptance and release status accurate and evidenced?
- Does the document invent product requirements, user decisions, dates, owners or metrics?
- Is detailed unaccepted behavior kept in a work record or Spec rather than promoted to product, roadmap or domain documents?

Typical severity: `error` for fabricated facts or accepted/planned confusion, `warning` for ambiguous status.

## 4. Single authoritative location

- Is the same fact stated substantively in more than one document? Identify the canonical owner and report the duplication; replacing copies with links requires human confirmation.
- Are summaries clearly summaries that link to the authority?
- Is a new document justified, or should an existing document be updated instead?
- Are there near-duplicate solution records or ADRs that should be merged or superseded? Report the overlap; do not merge or rewrite history automatically.
- Is history preserved, for example an ADR marked superseded rather than silently rewritten?

Typical severity: `warning` for duplicate authority, `info` for a summary that could link instead of repeat.

## 5. Links and navigation

- Do relative links resolve to existing files?
- Do anchors match actual headings?
- Do README, AGENTS and navigation documents point to the current paths?
- Are external links syntactically valid? Do not fetch them by default; state that they were not verified.
- Are links used instead of duplicate paragraphs?

Typical severity: `error` for a broken internal link, `warning` for stale navigation, `info` for an unverified external link.

## 6. Naming, format and safety

- Do filenames follow the local convention? For ADRs, sequential descriptive names; for solutions, one focused finding per file.
- Is the heading hierarchy coherent, without skipped levels?
- Is the document language consistent with the local convention?
- Are secrets, credentials, tokens or private keys present? Report the location and type only; never copy the secret into the report.
- Is sensitive personal data handled according to project rules? If the local standard is silent, report only clear exposure.

Typical severity: `error` for exposed secrets, `warning` for convention violations, `info` for formatting.

## 7. Cross-document consistency (optional deep pass)

Run this only when the user asks for a full or corpus review, or when the scoped documents directly contradict each other:

- Product, roadmap, domain and feature documents contradict each other.
- Roadmap planned scope conflicts with accepted feature behavior.
- `AGENTS.md` or README navigation points to paths or documents that no longer exist.
- The same term is used with different meanings across documents.

Report contradictions; do not auto-reconcile them. The canonical owner decides.

## Severity and fixability

| Severity | Use when | Examples |
|---|---|---|
| `error` | An explicit local rule is violated, an internal reference is mechanically broken, accepted and planned behavior are confused, a fact is fabricated, or a secret is exposed. | `features/` says "planned for next release"; a relative link points to a missing file. |
| `warning` | A likely violation, contradiction, duplicate authority or missing required content. | Two documents own the same fact; a work Spec lacks acceptance criteria. |
| `info` | Ambiguity, a possible improvement, or a rule the local standard does not specify. | A summary could link to the canonical document instead of repeating it. |

| Fixability | Meaning |
|---|---|
| Safe | An unambiguous mechanical fix that does not change meaning, status, ownership or placement. |
| Needs decision | Content, status, placement, deletion, merge, archive or a governance document. Leave it unchanged and report it. |
| Report only | Verification is unavailable, ownership is ambiguous, or rules conflict. |

## Safe-fix examples

- Fix a relative link to an existing local file when there is only one plausible target and the link is not inside a governance document.
- Fix an anchor after a heading rename when the target heading is unambiguous and the link is not inside a governance document.
- Remove trailing whitespace or duplicate blank lines when the local standard requires it.

## Do-not-fix examples

- Change `Planned` to `Accepted` in a roadmap or feature document.
- Move a file from `docs/work/` to `docs/work/archive/`.
- Merge two similar paragraphs or delete a "duplicate" without confirming the canonical owner.
- Fill `Not started` or `To decide` with a plausible value.
- Rewrite a Spec to add acceptance criteria that the user has not confirmed.
- Edit the local documentation standard (including `docs/documentation.md`) or `AGENTS.md` to make the project match the review.
