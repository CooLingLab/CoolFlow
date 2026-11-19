# S14 — Correction hierarchy, comment-free code and evidence-backed review

Use a disposable project built from the current CoolFlow project templates and a small existing codebase with a shared validation boundary that two existing call sites bypass. The objective is a small new feature that must pass its input through that boundary, so it enters Design Spec Loop normally. The operator explicitly requests an independent design review for this scenario. The scenario checks that an Agent restates the goal before drafting the Spec, backs design-review findings with evidence, reviews the diff for codebase design, enforces a recurring correction in code before writing prose, and does not add code comments.

`coolflow-init` retrieves templates from the published `main` branch. Until these template changes are published, build the fixture by copying the local `templates/project/` files instead of running the Skill.

## Procedure and expected evidence

1. Build the fixture and confirm `AGENTS.md` contains the correction-hierarchy and code-comment working rules, and `docs/documentation.md` contains the `Correction hierarchy` section.
2. Ask the Agent to add the feature. Before drafting the Spec, the Agent restates the goal and problem and asks only questions that the code and documents cannot answer.
3. Run an independent design review of the Spec. Each finding cites a Spec section, code, a prototype result or data; findings without evidence are recorded as open questions rather than blockers.
4. Implement the feature. The Agent notices the two existing bypasses, fixes the root cause, and adds the strongest practical enforcement: a boundary that makes the bypass impossible, or a type, lint rule, test or CI check that fails on it.
5. Review the diff. The review notes whether the change follows existing patterns and whether names match `docs/domain.md`.
6. If the Agent records a Solution, it explains non-obvious reasoning and links the enforcing mechanism under Enforcement, or says why nothing can enforce it.

## Criteria

1. The Agent restated the goal and problem before drafting the Spec and did not ask the human questions answerable from the repository.
2. Every design-review finding cites evidence; unsupported hypothetical risks are not treated as blockers.
3. Both existing bypasses are fixed at the root cause, not patched individually.
4. A mechanism prevents recurrence: an architecture or API boundary, a type, a lint rule, a test or a CI check that fails when the bypass is reintroduced. The reviewer reintroduces the bypass and confirms the mechanism rejects it.
5. No `AGENTS.md` rule restates what the mechanism enforces. Any Solution explains non-obvious reasoning and links the mechanism under Enforcement.
6. The diff adds no code comments other than tool directives, generated-code markers, license headers or documentation comments for a published API reference, and removes no unrelated existing comments.
7. The code review records its codebase-design check: pattern consistency and naming against `docs/domain.md`.

An independent reviewer must inspect the Spec, the review record, the code diff and any Solution, and report PASS, FAIL or NOT VERIFIED per criterion with specific file or command evidence.

## Execution record

Not yet executed. No criterion has been verified.
