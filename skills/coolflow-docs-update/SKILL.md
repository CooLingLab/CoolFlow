---
name: coolflow-docs-update
description: Record confirmed work and delivery evidence in the current project’s documentation, including Step 1–5 progress cards and Step 6–8 progress in existing objective records. Use when asked to update docs, record this session’s work, save progress, or sync accepted facts. Do not use to author a Spec, review documentation compliance, grant acceptance, classify an acceptance tier or execute a release.
---

# CoolFlow Docs Update

Bring the project's relevant documents up to date with the work just done, then say exactly what changed. This is an on-demand record keeper, not a lifecycle stage, a compliance review, or an acceptance decision.

## Core rule

The project's own `AGENTS.md` and the documentation standard it references decide destinations, formats and wording. Resolve the standard from `AGENTS.md` or `README.md`; use `docs/documentation.md` only as the default. If the local standard omits progress metadata or the write-location rules below, follow the local convention and say what you could not apply — do not impose the CoolFlow repository's standard on a project that has customized its own.

Update what is already established. Ask only about what genuinely cannot be determined. Never invent a decision, a test result, an owner, a date or a completion.

## Inputs

1. Read `AGENTS.md` and the local standard before writing anything.
2. Determine what this session actually produced: decisions the human confirmed, observations, findings with sources, open questions, and things explicitly rejected or deferred.
3. Separate confirmed project-level decisions from exploratory notes and from raw discussion. A topic that was merely mentioned is not a decision.
4. If the session is unavailable, ambiguous, or the user is asking about work done elsewhere, ask what should be recorded rather than guessing.

## Where content goes

Follow the local standard's table when it exists. Otherwise use these defaults:

| Content | Destination |
|---|---|
| Confirmed product positioning, audience, value, boundaries | `docs/product.md` |
| Domain terms, boundaries, core rules, invariants | `docs/domain.md` |
| Version scope, non-goals, later direction, priorities | `docs/roadmap.md` |
| Step 1 exploration: problem, users, competitors, opportunity, hypotheses, evidence | `docs/work/<objective>/brainstorm.md` |
| Substantial competitor or market research maintained on its own | `docs/work/<objective>/competitive-landscape.md` |
| Validation: assumption tested, method, result, evidence strength, decision | `docs/work/<objective>/validation.md` |
| Prototype artifacts, spikes, screenshots | `docs/work/<objective>/prototypes/` |

Spec authoring and changes to requirements, design or acceptance criteria are outside this Skill. Delivery updates belong in the existing objective record described below.

Objective directories: create `docs/work/<objective>/` only when real work for that objective exists, and reuse an existing directory for the same objective. Use a short kebab-case name that describes the objective; an initial product journey may use `001-mvp`. Do not open a second directory for a subtopic of the same objective.

## Creating a missing document

Create a Step 1–5 work document only when content belongs there and the objective is known. Start from the project's own template when one exists; otherwise use this skeleton, which must stay consistent with `templates/work/` in the CoolFlow repository:

```markdown
---
status: in_progress
related_steps: [1]
---

# Brainstorm — <objective>

## Problem and users

## Competitive landscape

## Opportunity and hypotheses

## Evidence

## Open questions
```

For a validation record use `related_steps: [3]` and the sections `Assumptions under test`, `Method and timebox`, `Result and evidence`, `Decision and next step`; set `related_steps: [5]` instead when a UI or usability validation produced the evidence. Keep hypotheses in `brainstorm.md` and prototype artifacts in `prototypes/`; this record holds only what was tested, what happened and what was decided.

Write only the sections this session actually supplies. A new work document starts with real content, not a filled-in skeleton: omit sections that have nothing to record rather than writing `To decide` into them, and keep the card's optional fields out until real progress exists. Copy a full template only when the user asks for an empty starting structure.

## Updating the progress card

Apply the local standard's fields. In the default CoolFlow format:

- `status`: describe the work this document records. Use `in_progress` while work continues, `paused` when it stalls, and `complete` only when the recorded work reached its intended end. `complete` does not mean accepted or released.
- `related_steps`: keep the document's actual relation to Steps 1–5; add a step only when the document now records work for it.
- `progress_updated`: set to today's date in quotes.
- `current_progress`: one or two sentences on what is finished and what is under way, drawn from this session.
- `next_steps`: only concrete next actions the human or the work actually established.
- `open_questions`: unresolved items that belong to **this** document's own scope, preferably phrased as questions. The authoritative list stays in the document that owns the question — usually the work record — so do not copy every open question into every related card. A core document's card lists only questions that block that document's own content.

Do not carry stale text forward into `next_steps` or `open_questions`; remove items this session resolved. Keep one authoritative status location: if the document has a frontmatter card, do not also write a `> Status:` line.

## Recording delivery progress

For Steps 6–8, follow the local standard. The default CoolFlow destination is the `Delivery progress` section in the objective’s existing unified Spec. Reuse an existing authoritative acceptance or delivery record when local conventions assign it there. Link to evidence where it already lives. If the objective or destination cannot be resolved, report the gap and ask only if needed. Do not create a Spec or a tracker to record progress. Keep any separate Spec document status and update only affected delivery fields.

- **Implementation** (`not_started`, `in_progress`, `implemented`): use observable changes and their scope or revision. Set `implemented` when the agreed behavior is supported by evidence.
- **Verification** (`not_verified`, `partially_verified`, `verified`): record actual checks, results and gaps. Use `partially_verified` when part of the required verification remains open.
- **Acceptance** (`pending`, `accepted`, `accepted_by_policy`, `changes_requested`): record the human’s explicit decision and scope. Record `accepted_by_policy` only for a `low`-tier change that meets every condition of the local acceptance tiers, with the supporting facts; never record it as `accepted`. Use `pending` when a decision is known to be outstanding. After acceptance, sync affected durable documents within the authorized scope and under the local Documentation Sync rules.
- **Release** (`not_released`, `released`): record explicit authorization and actual outcome separately. Use `released` only with evidence of what shipped and where. Include available post-release checks. Do not initiate a release.

Omit unknown fields and report material evidence gaps. Use a negative status only when it is established for the stated scope. Keep earlier verification, acceptance and release evidence scoped to its prior version when later changes invalidate its applicability. Use evidence from the current task or linked records and explicit human decisions already given. Update at a meaningful checkpoint or before finishing authorized work. A separate recap from the user is only needed for missing information.

## Procedure

1. Read the local standard, `AGENTS.md`, and the in-scope documents. Read only what the session's content could plausibly touch; do not rewrite the whole tree.
2. Draft a short internal list: each item of content, its destination, and whether it is a confirmed decision, an observation with evidence, or an open question.
3. Write the confirmed items. Create a missing document only under the conditions above; otherwise extend the existing authoritative document.
4. Update the applicable Step 1–5 cards, including `progress_updated`, and the supported delivery fields for any affected objective.
5. When you replace a section's content, remove the template's guidance sentence for that section if it is still present after real content, and drop empty sections instead of leaving `To decide` under them.
6. Ask about the smallest set of unresolved points. Prefer one grouped question over a long interrogation. If the user declines to answer, leave the item in `open_questions` and say so.
7. Re-read the changed files. Check applicable frontmatter and status uniqueness, verify delivery claims against their evidence and scope, and confirm surrounding content was preserved.
8. Report the files actually changed, the fields updated, the questions left open, and anything the session could not record.

## Boundaries

- Record acceptance only from an explicit human decision, or `accepted_by_policy` only when every local `low` condition is already evidenced against the final diff; never decide the tier yourself. Record release only from evidence of its actual outcome. Never grant acceptance, authorize release or infer production readiness.
- Do not edit `AGENTS.md` or the local documentation standard unless the user separately asks; if the standard itself is unclear or contradictory, report it.
- Do not stage, commit, push or archive work unless the user explicitly asks.
- Do not summarize the chat into a document. Record decisions, evidence and open questions.
- Do not overwrite sections that the session did not touch. Preserve existing content, structure and formatting.
- Do not infer progress from a document's existence elsewhere. If another workspace or Agent did work you cannot see, say that it is unrecorded.
