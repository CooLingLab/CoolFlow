# CoolFlow Loops: three adaptive feedback cycles

CoolFlow has **one Development Flow** and **three Adaptive Loops**:

- **Design Spec Loop (Step 6):** improve design quality through Spec, review, and revision.
- **Implementation Loop (Step 7):** improve implementation quality through code, tests, reviews, and fixes.
- **Evolution Loop (cross-stage):** reassess feedback, new ideas, or changing needs **from any step** and adapt **any relevant step** as needed. It has no mandatory entry point or end point.

The first two Loops are primarily associated with their named stages; the third is **cross-stage**, not a mandatory post-release cycle. These are feedback mechanisms, **not** Agent orchestration, fixed stage gates, or a requirement to iterate indefinitely. **Documentation Sync is a post-acceptance step, not a fourth Loop.**

## 1. Design Spec Loop — design quality

`Draft → Review → Refine ↻`

**Goal:** make the *design*, expressed through the Spec, clear, correct, and implementable.

- When a selected objective enters this Loop, draft its unified `spec.md`; earlier discovery may have used the work directory without a Spec. The Spec carries context, goals/non-goals, behavior and acceptance criteria, technical decisions, trade-offs, implementation strategy, and verification. Optional PRD or detailed design can be linked without duplicating content.
- Independent review is preferably fresh-context. The reviewer reads the **current Spec draft**, linked references and relevant **existing code**, rather than inheriting the drafter's assumptions.
- Seek missing cases, risky assumptions, overengineering, incompatibilities, feasibility issues, and unclear implementation steps.
- Refine the Spec and verify that important blockers are resolved. The human decides product-critical trade-offs.
- EGM Goldfish is a **recommended optional** review method, not a dependency.
- Reading existing code to check design feasibility **is not the same as reviewing code newly produced for this task**.
- `tasks.md` is optional and only needed for persistent progress tracking beyond the Agent's session or existing task system.

**Exit:** design is sufficiently reviewed, coherent, and ready to implement for the task's risk level.

## 2. Implementation Loop — code quality

`Build → Test → Review → Fix ↻`

**Goal:** implement the approved behavior and obtain evidence that it works.

- The coding Agent normally manages its own tasks in-session; CoolFlow does not require a persistent task file.
- Run relevant tests and review the changed code for correctness, security, maintainability and regressions.
- Check implementation against the **approved Spec and acceptance criteria**, not just the test suite.
- When code and Spec diverge, identify whether the implementation is wrong or the requirement needs human reconsideration.
- If the Spec is incomplete or flawed, **return to the Design Spec Loop**. Never silently rewrite requirements to rationalize broken code.
- Repeat until evidence supports human acceptance, or report unresolved blockers.

**Exit:** tested, reviewed implementation is ready for a human acceptance decision.

## Post-acceptance step — Documentation Sync and archive (not a Loop)

`Human Acceptance → Update accepted/current docs → Verify consistency → Selectively archive → Release`

- `docs/features/` describes accepted actual behavior, not a speculative design.
- Update `product.md`, `domain.md`, `roadmap.md`, `architecture.md`, `feature-map.md` only if affected.
- Preserve important past Specs, decisions, and verification evidence; remove redundant temporary drafts when appropriate.
- Acceptance may precede production release, so document release status accurately.
- The project's documentation standard can evolve independently after initialization.

## 3. Evolution Loop — cross-stage adaptation

`New Input → Reassess → Adapt ↻`

**Goal:** reassess and, when warranted, adapt the product direction, scope, or important decisions in response to feedback, new ideas, or changing needs, **whether before, during, or after implementation and release**.

- The Evolution Loop can **start from any of the eight steps** and re-enter **any step that is relevant**. It does not require a prior release, a roadmap update, or a fixed sequence.
- Examples: a concept prototype at Step 3 disproves the target user's assumption, so revisit Step 1; UI design at Step 5 reveals a domain misunderstanding, so revisit Step 2; implementation at Step 7 reveals a product-scope problem, so revisit Step 4; user feedback after Step 8 can lead to any relevant earlier step.
- New input can include an issue, a feature request, a new idea, or a feature becoming outdated. Reassessment may lead to action, further observation, or a decision not to adopt the input.
- Revisit only the decisions and artifacts affected by the input. Do not restart all eight stages mechanically.
- **Distinguish local quality iteration from product evolution:** fixing tests or revising a design within agreed requirements stays in the Implementation or Design Spec Loop. Use the Evolution Loop when the learning warrants rethinking assumptions, scope, or direction.
- Human judgment remains responsible for product-critical changes. There is no mandated endpoint; stop, continue, or pivot according to what is learned.

## Review terminology

| Review | Object | Timing |
| --- | --- | --- |
| Design Spec Review (EGM-style) | Design expressed in the Spec, assumptions, feasibility and implementation strategy | Before substantial coding |
| Code Review | Newly changed code and tests | After coding, within Implementation Loop |
| Spec Conformance | Expected behavior versus actual implementation | Within Implementation Loop and acceptance |
| Scenario Review | **CoolFlow itself**: do agents follow the Standard correctly? | Internal CoolFlow development only; remove from final release tree |

Do not mistake internal CoolFlow **Scenario Review** for a fourth product-development Loop.
