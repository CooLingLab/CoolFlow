# Documentation review checks

Use this checklist with the bundled [CoolFlow documentation standard](documentation-standard.md) and the project's local rules. The standard is the comparison baseline for CoolFlow conformance. Local rules explain the project's actual document roles, paths, metadata, and conventions; credit arrangements the standard allows.

Each finding states its category:

- **Adopted-rule violation:** a rule the project has adopted is violated.
- **Mechanical defect:** an objectively broken local link or anchor (or mechanical formatting required by an applicable project rule), independent of whether a local standard exists.
- **CoolFlow difference:** the project differs from the baseline where the standard leaves room or the project has not adopted the related convention. For a project considering adoption, this is an opportunity, not a defect.
- **Unverified:** the evidence needed to decide is missing. Say what would resolve it.

Do not enforce initialization-only requirements on a project that was not initialized with CoolFlow. Do not require optional artifacts or unused lifecycle stages. Do not treat a missing optional document as a defect.

## 1. Placement and lifecycle

- Are documents mapped to the roles they actually serve? Equivalent names and paths count. Do not require the canonical tree.
- Is each accepted-behavior record describing implemented, accepted behavior? Planned or proposed behavior belongs in a roadmap or an open work record.
- Is discovery kept separate from a selected objective's Spec? A work objective may hold notes or prototypes without a Spec.
- Are optional records such as Solutions, ADRs, architecture, and feature maps present only for a real need?
- After acceptance, were accepted facts recorded before work was archived? Does the archive retain useful Specs, decision rationale, and verification evidence where the project archives?
- Is any document a second authority for a fact owned elsewhere?

## 2. Structure and purpose

Judge purpose using the standard's role descriptions, not a preferred heading list. For roles the project has, check that the content matches the role:

- Product brief: problem, audience, vision, value, boundaries, and current positioning. It is not a PRD.
- Roadmap: current/MVP scope, later direction, and priority, with planned versus accepted scope explicit.
- Domain: ubiquitous language, boundaries, and core rules. Provisional content is allowed.
- Features/accepted behavior: behavior, constraints, and verification, with links to evidence.
- Objective Spec: context, goal and non-goals; acceptance criteria; design decisions and trade-offs; implementation and validation approach; open questions distinguished from decisions.
- Solutions: one focused, verified, reusable finding with evidence, stating what now enforces it or why nothing can.
- ADRs: context, drivers, options, decision, and consequences; one consequential decision per file.
- Architecture: current system architecture, not decision rationale.
- Navigation in README/AGENTS: accurate entry points and links to the project's documentation rules.

## 3. Truth and status

- Are observed facts, user claims, decisions, unverified findings, assumptions, and open questions distinguishable?
- Is planned behavior labeled as planned or proposed rather than accepted or current?
- Is accepted behavior recorded in the appropriate current document, not only in a work record?
- Are `not_started` and `To decide` treated as unknown rather than completed?
- Are implementation, verification, human acceptance, release authorization, and release evidence reported separately and supported by evidence?
- Does a document invent requirements, decisions, dates, owners, or metrics?

### Progress metadata

When the project uses Step 1–5 progress metadata (CoolFlow's default or a local variant), check that required fields are valid, that cards do not duplicate a legacy status line, and that card claims match the body and evidence. When the project does not use this metadata, mark the dimension **not applicable**; do not require cards.

### Delivery progress

Where the project records delivery progress, check that each claim is supported for the stated objective and revision, and that no second record owns the same fact. Leave status corrections to the record owner. For `accepted_by_policy`, check that the project declares a valid acceptance policy with a `low_check`, that the record names the check's command, base and head revisions and a passing result, and that it is never reported as human `accepted`.

## 4. Single authoritative location

- Is the same fact stated substantively in more than one document? Name the likely owner and report the duplication; replacing copies with links needs confirmation.
- Are summaries clearly summaries that link to the authority?
- Is a new document justified, or should an existing document be updated?
- Are near-duplicate Solutions or ADRs reported for consolidation or supersession rather than merged automatically?
- Is history preserved, for example an ADR marked superseded rather than silently rewritten?

## 5. Links and navigation

- Do relative links resolve to existing files?
- Do anchors match actual headings?
- Do README, AGENTS, and navigation documents point to current paths?
- Are external links syntactically valid? Do not fetch them by default; state that they were not verified.

## 6. Naming, format, and safety

- Do filenames and language follow the applicable local convention? Do not enforce a filename convention the project has not adopted.
- Is the heading hierarchy coherent, without skipped levels?
- Are secrets, credentials, tokens, or private keys present? Report the location and type only; never copy a secret into the report.
- Is sensitive personal data handled according to project rules? If no rule applies, report only clear exposure.

## 7. Cross-document consistency

Run this deep pass only for a requested full review, an adoption assessment that needs it, or scoped documents that directly contradict each other:

- Product, roadmap, domain, and feature records contradict each other.
- Roadmap scope conflicts with accepted behavior.
- Navigation points to paths or documents that no longer exist.
- The same term is used with different meanings across documents.

Report contradictions; do not auto-reconcile them.

## Severity and fixability

| Severity | Use when | Examples |
|---|---|---|
| `error` | An adopted rule is violated, an internal reference is mechanically broken, accepted and planned behavior are confused, a fact is fabricated, or a secret is exposed. | `features/` says "planned for next release"; a relative link points to a missing file. |
| `warning` | A likely violation, contradiction, duplicate authority, or missing required content. | Two documents own the same fact; a Spec lacks acceptance criteria. |
| `info` | A meaningful difference from CoolFlow, ambiguity, or a possible improvement. | A summary could link to the canonical document; a document type could later be split by role. |

| Action | Meaning |
|---|---|
| `fix-safe` | Unambiguous mechanical defect outside governance documents, left unapplied in `check` mode and eligible for an explicitly authorized `fix-safe` run. |
| `fixed` | Unambiguous mechanical defect fixed during an explicitly authorized `fix-safe` run. |
| `needs decision` | Content, status, placement, deletion, merge, archive, or a governance document. Leave unchanged and report it. |
| `report only` | Verification unavailable, ownership ambiguous, or rules conflict. |

## Safe-fix examples

- Fix a relative link to an existing local file when there is only one evident target and the link is not inside a governance document.
- Fix an anchor after a heading rename when the target heading is unambiguous and the link is not inside a governance document.
- Remove trailing whitespace or duplicate blank lines when an applicable project rule requires it.

## Do-not-fix examples

- Change `planned` to `accepted` in a roadmap or feature record.
- Move a file into an archive directory.
- Merge or delete a "duplicate" without confirming the canonical owner.
- Fill `not_started` or `To decide` with a plausible value.
- Add acceptance criteria a human has not confirmed.
- Edit `AGENTS.md`, `docs/documentation.md`, or another governance document to make the project match the review.
- Apply adoption changes before the user approves a plan.
