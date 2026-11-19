# Reviews during product development

**English** | [简体中文](reviews.zh-CN.md)

The **Design Review** and **Code Review** below are part of the recommended development methodology. The separate `flowreviews/scenarios/` directory contains internal Scenario Reviews of CoolFlow itself, not tests for applications built with CoolFlow. Keep these cases in the public CoolFlow source repository; do not copy them into target application repositories.

## Within the Design Spec Loop: review before coding

Consider independent EGM-style Goldfish Review when a feature is novel, complex, risky or irreversible. Provide the reviewer with the **current Spec draft**, optionally linked PRD/design, and relevant existing code/context. The independent reviewer should:

- Challenge missing user behavior, validation cases and failure modes.
- Check assumptions against existing code and constraints.
- Flag overengineering, alternative approaches and unclear trade-offs.
- Verify the implementation plan is detailed enough to guide a coding Agent.
- When the project declares an acceptance policy, check the Spec's planned tier against the project's [acceptance tiers](documentation.md#acceptance-tiers).
- Report actionable issues, each with supporting evidence from the Spec, code, a prototype or data. Treat a hypothetical risk without evidence as an open question, not a blocker.

Resolve and verify material blockers, then confirm the design is ready to implement before writing significant code. Small changes can use lightweight checks. The review of **existing code** for design feasibility is *not* a review of new implementation.

## Within the Implementation Loop: review implemented code

- Run relevant tests and check obvious regressions.
- Review the **new code diff** for correctness, security, readability and maintainability.
- Check the diff's effect on codebase design: whether it follows existing patterns or introduces one later Agents will copy, whether module interfaces stay small relative to the behavior they hide, and whether names match the ubiquitous language in `docs/domain.md`.
- Compare code behavior against Spec and acceptance criteria.
- Before recording `accepted_by_policy`, check every `low` condition against the final diff; see [acceptance tiers](documentation.md#acceptance-tiers).
- Resolve discrepancies by changing code or explicitly revisiting requirements with a human.
- Seek human acceptance of the actual result, unless the change qualifies for `accepted_by_policy`; sync durable docs afterward.

**After acceptance** (human or `accepted_by_policy`), synchronize durable feature/domain/roadmap documentation and archive relevant work records. This is a step, not a separate Knowledge Loop. **At any Development Flow step**, feedback, new ideas, or changing needs that warrant reconsidering product direction, assumptions or scope can activate the cross-stage Evolution Loop, returning to any relevant step. Ordinary design and code corrections remain in their local quality Loops; post-release feedback is only one possible Evolution trigger.

CoolFlow does not require EGM, Spec Kit, OpenSpec or a particular agent runner. These are optional tools and sources of good practices.
