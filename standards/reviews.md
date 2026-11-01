# Reviews during product development

The **Design Review** and **Code Review** below are part of the recommended development methodology. The separate **Scenario Review** directory in this CoolFlow repository is internal testing of CoolFlow itself and must be removed from final release artifacts.

## Within the Design Spec Loop: review before coding

Consider independent EGM-style Goldfish Review when a feature is novel, complex, risky or irreversible. Provide the reviewer with the approved unified Spec, optionally linked PRD/design, and relevant existing code/context. The independent reviewer should:

- Challenge missing user behavior, validation cases and failure modes.
- Check assumptions against existing code and constraints.
- Flag overengineering, alternative approaches and unclear trade-offs.
- Verify the implementation plan is detailed enough to guide a coding Agent.
- Report actionable issues and supporting evidence.

Revise and re-review material blockers before writing significant code. Small changes can use lightweight checks. The review of **existing code** for design feasibility is *not* a review of new implementation.

## Within the Implementation Loop: review implemented code

- Run relevant tests and check obvious regressions.
- Review the **new code diff** for correctness, security, readability and maintainability.
- Compare code behavior against Spec and acceptance criteria.
- Resolve discrepancies by changing code or explicitly revisiting requirements with a human.
- Seek human acceptance of the actual result; sync durable docs afterward.

**After human acceptance**, synchronize durable feature/domain/roadmap documentation and archive relevant work records. This is a step, not a separate Knowledge Loop. **After release**, usage and feedback inform the roadmap through the outer Evolution Loop.

CoolFlow does not require EGM, Spec Kit, OpenSpec or a particular agent runner. These are optional tools and sources of good practices.
