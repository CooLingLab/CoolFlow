---
name: coolflow-docs-review
description: Assess a software project's documentation against the CoolFlow documentation standard and recommend practical improvements, including for an existing project considering adoption. Use for CoolFlow documentation structure or conformance checks. Review is read-only by default. Fix only explicitly authorized mechanical defects.
---

# CoolFlow Docs Review

Assess documentation against the [bundled CoolFlow standard](references/documentation-standard.md). Use [review-checks.md](references/review-checks.md) as a checklist. The source of truth for the bundled snapshot is CoolFlow's `standards/documentation.md`.

## Baseline and local context

1. Identify the target root and applicable project instructions; do not treat the Skill installation folder, an Agent configuration folder, or the CoolFlow source repository as the target unless asked. Read `AGENTS.md` or its equivalent, the README, and any local documentation standard they reference. Check `docs/documentation.md` as the default if no path is given. Distinguish **no local standard** from **a referenced path that cannot be found**; if neither prevents reading the target project, note it and continue the CoolFlow comparison, leaving local-rule compliance unverified where local rules are unavailable.
2. Read the bundled snapshot and report its version and source blob identifier. If the snapshot is missing or unreadable, report the incomplete installation and stop the CoolFlow comparison instead of reconstructing the standard. Links inside the snapshot refer to the source repository; the Skill is designed not to require network access to resolve them.
3. Map each document by its real purpose and the project's local conventions. Credit equivalent paths, names, and arrangements permitted by the baseline. Apply required content and metadata checks only to the roles and lifecycle stages they cover. Apply initialization requirements only to projects initialized with CoolFlow. Treat missing optional artifacts and unused lifecycle stages as normal.
4. Classify each finding as a **CoolFlow difference**, **adopted-rule violation**, **mechanical defect** (such as an objectively broken local link or anchor), or **unverified** item. For a project considering adoption, a CoolFlow difference is an adoption opportunity, not a defect. If local rules explicitly differ, explain the difference and respect the local rules for project work.

## Scope and execution

- Use the paths or work objective the user named. For a project-level assessment, inventory documentation entry points, then sample relevant documents across the roles that exist and relevant gaps. For a change-oriented request without paths, use the changed documentation; if scope is still unclear, ask rather than scanning everything. Review the full corpus only when requested. Report scope and limits.
- **`check` (default):** inspect and report with no edits. For adoption, identify what can be kept, which existing documents already serve CoolFlow roles, and the smallest useful improvements as input to the user's adoption decision; adoption changes require separate approval.
- **`fix-safe`:** only when the user explicitly authorizes fixes (or approves specific proposed fixes), and restricted to any subset or exclusions the user specified. Fix only unambiguous mechanical defects outside governance documents (`AGENTS.md`, `docs/documentation.md`, or equivalent): a broken relative link or anchor with one evident local target, or mechanical whitespace required by an applicable project rule. Report governance defects for a separate task. Re-check edited files, verify no out-of-scope file changed, leave changes unstaged, and never commit or push.
- Preserve meaning, status, ownership, and placement. Never automatically change status or acceptance claims, fill `not_started` / `To decide`, rename or move files, delete, merge, consolidate, split, or archive content, or create product docs/Specs. Limit code or test inspection to evidence for a documentation claim; do not fetch external URLs by default.

## Report and record

Report the scope, mode, snapshot identifier, and local context; summarize existing matches; and list findings with `file:line` (or section), severity (`error` / `warning` / `info`), category, applicable rule or mechanical defect, evidence, and action (`fix-safe` / `fixed` / `needs decision` / `report only`), plus any authorized fixes applied and checks not performed.

Return the report in the conversation by default; routine reports and transient findings need no file. When the review produces durable outcomes worth retaining (such as confirmed convention decisions, adoption choices, or unresolved ownership/status questions) and the task authorizes documentation updates:

1. Read the project's local instructions, documentation rules, and relevant existing records first; follow project conventions and prefer an existing authoritative document, or create a record at the project's established location only when warranted and authorized (never create a Spec merely for discovery or a new review tracker per run).
2. Choose the destination by context (CoolFlow defaults when local conventions do not specify otherwise): discovery-stage convention notes in the objective's discovery notes (such as `brainstorm.md`), design-stage documentation decisions for a selected objective in its `spec.md`, human-confirmed durable project-level plans/decisions in `product.md`, `roadmap.md` (future scope labeled planned/proposed), or `domain.md` with actual status, and accepted-behavior facts synced only after human acceptance.
3. Update at useful checkpoints or before finishing rather than waiting for chat end. Preserve existing content; separate observed facts, user claims (noting when unverified), human-confirmed decisions, unverified findings, assumptions, and open questions; avoid duplicate authorities; and report the files actually updated.
4. Respect discussion-only or no-write requests, missing write access, or an unclear project/destination: do not invent a location or permission; state what remains unrecorded and its intended home when known, asking only if needed. Changing a local standard requires separate explicit confirmation.
