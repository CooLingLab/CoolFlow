---
name: coolflow-progress
description: Report where a CoolFlow project's Step 1–5 work currently stands by reading its document progress cards. Use when the user asks how the project is going, what stage the work is in, what is next, or what is still undecided. Do not use to update documents, review documentation compliance, or decide what to build.
---

# CoolFlow Progress

Answer "where does this project stand?" from the project's own records, quickly and honestly. This Skill reads and reports; it never writes.

## Core rule

Use the project's `AGENTS.md` and the documentation standard it references for document locations and field meanings. Use `docs/documentation.md` and the default locations only when the project has not customized them.

Read progress cards first — the frontmatter block at the top of each document. Open a document's body only when the card cannot answer what was asked, when two documents conflict, or when the user asks about a specific item's details.

## Procedure

1. Resolve the project root, the local standard, and the document locations. Stop and ask if the target is ambiguous.
2. Collect the Step 1–5 documents: `docs/product.md`, `docs/roadmap.md`, `docs/domain.md`, and the work documents under `docs/work/<objective>/` that carry progress metadata.
3. For each, read only the progress card. Note `status`, `related_steps`, `progress_updated`, `current_progress`, `next_steps` and `open_questions`.
4. Report all five steps in order, whether or not they have records. For each step list the related documents and their recorded progress; end with the next actions and open questions that affect it.
5. State separately: documents with no progress card, work directories that look abandoned, and anything in another workspace, Agent or branch that you cannot see.

## Reporting rules

- **Absence is not progress.** A step with no related document is "no record found", not `not_started`. A document that exists but lacks the card is "no progress card", not a guess.
- **A related document does not set the step's status.** `related_steps` expresses relevance. Several documents may relate to one step with different statuses, and one document may relate to several steps. Do not compress them into one step-level status, and do not report a percentage.
- **Cards are snapshots.** Mention `progress_updated` when it is old relative to the work being discussed, and say that the body may have moved on. If the user needs certainty, offer to open the body or run a documentation update, but do not change anything yourself.
- **`complete` is not accepted.** It means the recorded work reached its intended end. Acceptance and release are separate and cannot be inferred from a card.
- **Non-Markdown work still counts as a gap.** Prototypes, spikes and design files may show Step 3 or Step 5 activity without a card. Look for `prototypes/` and mention what you found, labeled as an artifact rather than a recorded status.
- **Do not invent next actions.** Only report `next_steps` and `open_questions` that the documents actually contain; when a card is empty, say so rather than proposing work.

## Output shape

Keep it compact and scannable:

```text
Step 1 — Idea → Brainstorm
  brainstorm.md (001-mvp) · in_progress · updated 2026-11-16
    Current: target users roughly identified; scenarios under discussion
    Next: identify the most common user problems
    Open: whether team users are in scope

Step 2 — Lightweight strategic DDD
  domain.md · not_started

Step 3 — Concept Prototype → Validation
  no record found
```

Then add a short section for unrecorded or unverifiable items. If the user asked one narrow question, answer that first and keep the full listing brief.

## Boundaries

- Never edit, create, move, archive or reformat documents.
- Never decide a stage is complete, nor recommend skipping a stage as though it were decided.
- Do not review documentation compliance; that belongs to a documentation review.
- Do not read the entire documentation tree when cards suffice.
- Do not report progress as fact when the evidence is a stale card, a missing file, or an agent's claim.
