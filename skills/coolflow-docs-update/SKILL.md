---
name: coolflow-docs-update
description: Update the current project's Step 1–5 documents from work completed in this session, including each document's progress card. Use when the user asks to update documents, record this session's work, save progress, or sync discussion results into the project docs. Do not use to review documentation compliance, to write a Spec, or to mark work accepted or released.
---

# CoolFlow Docs Update

Bring the project's Step 1–5 documents up to date with the work just done, then say exactly what changed. This is an on-demand record keeper, not a lifecycle stage, a compliance review, or an acceptance decision.

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

Requirements and acceptance criteria belong to the unified Spec in Design Spec Loop (Step 6) and are outside this Skill. If the session produced them, say so and leave them for the Spec rather than writing them here.

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

Write only the sections the session actually supplies and leave the rest as `To decide`. Do not create a document merely because a template exists, and do not create `spec.md`, a PRD, prototypes or an objective that the work does not support.

## Updating the progress card

Apply the local standard's fields. In the default CoolFlow format:

- `status`: describe the work this document records. Use `in_progress` while work continues, `paused` when it stalls, and `complete` only when the recorded work reached its intended end. `complete` does not mean accepted or released.
- `related_steps`: keep the document's actual relation to Steps 1–5; add a step only when the document now records work for it.
- `progress_updated`: set to today's date in quotes.
- `current_progress`: one or two sentences on what is finished and what is under way, drawn from this session.
- `next_steps`: only concrete next actions the human or the work actually established.
- `open_questions`: unresolved items from this session, preferably phrased as questions.

Do not carry stale text forward into `next_steps` or `open_questions`; remove items this session resolved. Keep one authoritative status location: if the document has a frontmatter card, do not also write a `> Status:` line.

## Procedure

1. Read the local standard, `AGENTS.md`, and the in-scope documents. Read only what the session's content could plausibly touch; do not rewrite the whole tree.
2. Draft a short internal list: each item of content, its destination, and whether it is a confirmed decision, an observation with evidence, or an open question.
3. Write the confirmed items. Create a missing document only under the conditions above; otherwise extend the existing authoritative document.
4. Update each touched document's progress card, including `progress_updated`.
5. Ask about the smallest set of unresolved points. Prefer one grouped question over a long interrogation. If the user declines to answer, leave the item in `open_questions` and say so.
6. Verify: re-read the changed files, confirm the frontmatter still parses as intended, confirm no `> Status:` duplicate, and confirm no content was lost from sections you appended to.
7. Report the files actually changed, the fields updated, the questions left open, and anything the session could not record.

## Boundaries

- Do not mark work accepted, released or production-ready, and do not decide acceptance on the human's behalf. Report the state; let the human accept it in Documentation Sync terms.
- Do not edit `AGENTS.md` or the local documentation standard unless the user separately asks; if the standard itself is unclear or contradictory, report it.
- Do not stage, commit, push or archive work unless the user explicitly asks.
- Do not summarize the chat into a document. Record decisions, evidence and open questions.
- Do not overwrite sections that the session did not touch. Preserve existing content, structure and formatting.
- Do not infer progress from a document's existence elsewhere. If another workspace or Agent did work you cannot see, say that it is unrecorded.
