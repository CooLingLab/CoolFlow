---
name: coolflow-docs-review
description: Review project documentation against the project's local documentation standard and report violations; fix only mechanical issues, and only when explicitly asked to fix. Use when the user asks to review, audit, check, or fix documentation compliance, documentation structure, or whether new or changed docs follow the project's documentation rules. Do not use for code review, general prose editing, or creating documentation from scratch.
---

# CoolFlow Docs Review

Review project documentation against the project's **local** documentation standard. This is an on-demand quality check, not a lifecycle stage, a mandatory gate, or a documentation generator.

## Core rule

The target project's `AGENTS.md` and the local documentation standard it references are the source of truth. Resolve the standard's path from `AGENTS.md` or `README.md`; use `docs/documentation.md` only as the default when the project has not customized it. Do not impose the CoolFlow repository's current standard on a project that has customized its conventions.

Read the local rules first. Every finding must cite a local rule, an explicit user instruction, or an objectively broken mechanical reference.

If the local standard cannot be found at the resolved or default path, stop and report it. Distinguish **missing** from **located elsewhere**; ask for the correct path instead of assuming. Do not silently substitute CoolFlow defaults, and do not create or overwrite the standard. If `AGENTS.md` conflicts with the local standard, report the conflict and follow the more specific project instruction; do not silently choose one.

## Inputs and scope

1. Identify the exact target project root. Do not review the Skill installation directory, the Agent configuration directory, or the CoolFlow source repository unless the user explicitly asks.
2. Read `AGENTS.md` and the local documentation standard it references completely, plus any project instruction files they reference. If the standard path is unclear, ask.
3. Determine the mode:
   - **Default — `check`:** review and report, and make no edits. A bare request to review or 审查 does not authorize changes: the local standard's approval rule applies, and editing a document is a separate action that the user must request or approve. State that no edits will be made.
   - **`fix-safe`:** only when the user explicitly asks to fix, correct or 修正 the documents, or approves specific fixes you proposed. Then apply only the safe fixes in [Fix policy](#fix-policy) and report everything else.
   - If the wording does not clearly authorize changes, ask before editing rather than assuming either mode.
4. Determine the scope:
   - The paths the user named.
   - Otherwise, documentation files changed in the working tree or current task.
   - If neither is clear, ask for the paths. Do not scan the entire documentation tree by default.
   - A full-corpus review happens only when the user explicitly asks for all project documents.
   - If the user asks to fix only specific items or forbids certain changes, apply only those; do not apply other safe fixes.
5. Read the relevant documents and enough linked context to verify their claims. Check documentation claims against actual code, tests or configuration only when the local standard or the document makes a verifiable factual claim. Do not review code quality.

## Rule map

Before checking, build a small rule map from the local standard:

- The local standard's path and any custom document locations.
- Creation and lifecycle rules for each document type.
- Required content and purpose for each type.
- Status rules: planned versus accepted, `Not started` / `To decide`, draft versus final.
- Ownership, duplication and linking rules.
- Naming, language and navigation rules.
- Project-specific conventions in `AGENTS.md`.

The generic checks in [review-checks.md](references/review-checks.md) are prompts, not rules. Only the local standard or an explicit user instruction creates a violation. If a dimension is not specified locally, mark it **not specified** and do not enforce a preferred convention.

An objectively broken local reference is a **mechanical defect**, not a rule violation. A relative link whose target does not exist and an anchor that cannot match any heading are examples. A mechanical defect may be fixed under the safe-fix policy even when the local standard is silent, but the report must label it as a mechanical defect.

## Review dimensions

Use the applicable checks from [review-checks.md](references/review-checks.md):

1. Placement and lifecycle.
2. Structure and purpose.
3. Truth and status.
4. Single authoritative location and duplication.
5. Links and navigation.
6. Naming, format and safety.

For each finding, record:

- File and line, or the relevant section.
- Severity: `error`, `warning` or `info`.
- The local rule, explicit user instruction or mechanical defect it relates to.
- Evidence: a short quote or precise paraphrase.
- Action: `fixed`, `needs decision` or `report only`.

Do not report style preferences as violations. If the local standard is silent, say so instead of inventing a requirement.

## Fix policy

Safe to fix without asking, **only in an authorized `fix-safe` run**:

- A broken relative link or anchor when exactly one unambiguous target exists and the link is not inside a governance document.
- An obvious navigation reference in `README.md` when the target is unambiguous.
- Duplicate blank lines, trailing whitespace or similar formatting noise, only when the local standard requires it.

Never fix automatically:

- Status changes: planned to accepted, `Not started` to done, draft to final.
- Changing a document's placement or name, including moving or renaming within or between directories.
- Deleting content; merging, consolidating or splitting documents or substantive content; rewriting prose.
- Creating, filling or archiving documents.
- Editing `AGENTS.md` or the local documentation standard, including `docs/documentation.md`, as part of a review. These are governance documents; report issues and ask for a separate explicit task.
- Changing ownership or deciding which document is authoritative.
- Any change that requires guessing a product fact, decision, owner, date or acceptance status.
- Changes outside the target project or outside the reviewed scope.

The **Never fix** list overrides the safe-fix list. A broken link inside a governance document is reported, not fixed. The fixability table in [review-checks.md](references/review-checks.md) is authoritative if wording differs.

When a fix is ambiguous, leave the text unchanged and report it. Do not "fix" by inventing content.

## Procedure

1. Resolve the scope, mode and local rules. State the resolved mode, scope and intended safe fixes before editing. Edit only in `fix-safe` mode after explicit authorization; if the wording does not clearly authorize changes, ask.
2. Inventory the in-scope documents and classify each by type using the local paths. For a custom or unknown path, use the local standard's mapping; if it is still unclear, mark it `custom/unknown` and avoid type-specific assumptions.
3. Review each document. For cross-document checks, compare the in-scope documents plus directly referenced documents needed to verify a claim.
4. Apply only the authorized safe fixes, with minimal diffs. Preserve existing content, formatting and user changes. Do not reformat whole files.
5. Re-check each edited file for the specific issue and for new broken links. Use Git diff, file hashes or an equivalent check to confirm that no out-of-scope file changed.
6. Report:
   - Scope, mode and local standard source.
   - Summary counts: checked, passed, fixed, needs decision, report only.
   - Findings table with `file:line`, severity, rule, issue, evidence and action.
   - Fixes applied, with a short before/after.
   - Unresolved items and checks not performed, such as external links not fetched or acceptance status not verifiable.
7. Do not stage, commit or push. Leave changes in the working tree for human review.

## Result recording

This Skill's primary result is the review report. Report it in the conversation by default.

Before finishing, decide whether the review produced a durable finding worth retaining: a confirmed convention gap, an unresolved ownership or status question, or a user-requested record. Transient style findings and the normal report do not need a file.

If a record is warranted and the task authorizes documentation updates:

- Read the local documentation rules and existing records first.
- Prefer the current work objective's existing notes or Spec, or another existing authoritative record.
- If no suitable record exists, ask for the destination or, when the project has an established review/work location and the user authorized it, create the record there. Do not create a new tracker or a new review file for every invocation.
- Distinguish observed facts, user claims, decisions, unverified findings, assumptions and open questions. Link evidence.
- Update before finishing, not only when the user asks later, and report the actual files updated or why no write occurred. If no write is authorized or possible, say what remains unrecorded and, when known, where it could go.

If the review reveals a durable gap or ambiguity in the local documentation standard, report it and ask before changing the standard. If the human confirms a durable convention change, update the standard only within that separately authorized scope.

## Boundaries

- This Skill does not create product documentation, write a Spec, fill templates or decide product facts.
- It does not change document ownership, placement, status or acceptance claims.
- It does not review code quality, run tests or validate external URLs by default.
- It does not replace human acceptance or Documentation Sync.
- It does not enforce CoolFlow upstream rules that the project has not adopted.
- It does not modify files outside the target project.
- If the requested scope contains no documentation, report that instead of expanding the scope automatically.
