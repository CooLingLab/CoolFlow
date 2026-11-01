# Three quality loops

CoolFlow is **one Flow with three Loops**. They can be iterated independently. None requires an Agent orchestrator.

## Loop A: Design (before coding)

`Unified Spec → Independent Design Review → Resolve → Revise / re-review`

- Spec defines problem, goals/non-goals, requirements, acceptance behavior, technical approach, trade-offs, implementation strategy, and verification.
- Review should be fresh-context where practical: the reviewer reads the Spec, cited context and relevant existing code; it must **not** rely only on the drafting Agent's summary.
- Reviewer seeks gaps, risky assumptions, overengineering, incompatibilities, and implementation-readiness issues.
- Human decides product-critical trade-offs. EGM Goldfish is a recommended optional implementation, not a dependency.
- A design review may read **existing code to verify the plan**, but it is **not the code review of newly implemented changes**.
- `tasks.md` is optional; there is no mandatory document boundary between spec, design and execution plan.

## Loop B: Implementation (after design)

`Code → Test → Independent Code Review → Spec Conformance → Fix → repeat`

- Coding Agent uses its own session tasks or native tools by default.
- Test behavior, regressions and errors. Review changed code for correctness, security, maintainability and scope.
- Check code against the **approved Spec and acceptance criteria**, not just whether tests happen to pass.
- Where code and Spec disagree, identify whether the code is wrong or the requirement needs explicit human reconsideration; do not silently rewrite the Spec to fit bugs.
- Repeat until evidence supports acceptance or unresolved blockers are reported.

## Loop C: Knowledge sync (after acceptance)

`Human Acceptance → Update current docs → Verify consistency → Selectively archive`

- `features/` contains **accepted actual behavior**, never speculative plans. Mark release status when necessary.
- Update `product.md`, `domain.md`, `roadmap.md`, `architecture.md`, and `feature-map.md` only when relevant.
- Archive useful past Specs, key alternatives/decisions and verification evidence. Avoid copying the whole conversational history.
- After initialization, a project may evolve its rules independently of upstream CoolFlow.

## Review distinction

| Review | Reviews | When |
| --- | --- | --- |
| Design Review (EGM-style) | Spec, design assumptions, feasibility, plan | Before code |
| Code Review | Newly changed code and tests | After code |
| Spec Conformance | Expected vs actual behavior | During implementation/acceptance |
| Scenario Review | **CoolFlow itself**: can agents use the standard correctly? | Internal CoolFlow development only; removed at final release |

Do not confuse Scenario Review of CoolFlow with app-level reviews prescribed by the methodology.
