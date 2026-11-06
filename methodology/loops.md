# CoolFlow Loops: three adaptive feedback cycles

**English** | [简体中文](loops.zh-CN.md)

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
- Work autonomously within the approved behavior and constraints. Pause for human judgment when proceeding would change product intent, materially expand scope, or commit to a significant unresolved trade-off; present the evidence and decision needed rather than silently deciding.
- Repeat until evidence supports human acceptance, or report unresolved blockers.

**Exit:** tested, reviewed implementation is ready for a human acceptance decision.

## Post-acceptance step — Documentation Sync and archive (not a Loop)

`Human Acceptance → Sync accepted truth → Verify doc consistency → Selectively archive → (separate release authorization) → Execute and verify release, if applicable`

- `docs/features/` describes accepted actual behavior, not a speculative design.
- Update `product.md`, `domain.md`, `roadmap.md`, `architecture.md`, `feature-map.md` only if affected.
- Preserve important past Specs, decisions, and verification evidence; remove redundant temporary drafts when appropriate.
- Acceptance may precede production release, so document release status accurately.
- The project's documentation standard can evolve independently after initialization.

## 3. Evolution Loop — cross-stage adaptation

`New Input → Reassess → Adapt ↻`

**Goal:** reassess and, when warranted, adapt the product direction, scope, or important decisions in response to feedback, new ideas, or changing needs, **whether before, during, or after implementation and release**.

- **Capture and describe new input:** record its source, context and evidence, distinguishing observed facts, user claims, interpretation and assumptions. Input may include user research, prototype findings, technical constraints, a feature request, a new idea, post-release feedback, or a market/environment change. A request is not itself a decision.
- **Reassess affected decisions:** identify which assumptions, goals, domain understanding or scope may have changed and whether further investigation is needed. Reassess only relevant decisions; distinguish a product change from a local quality defect.
- **Decide the response and adapt relevant work:** act, investigate or validate further, observe, defer, or decline the input; identify the relevant stage or local Loop. Update only affected records with their correct lifecycle status. Exploration findings stay in work notes, human-confirmed durable plans update the relevant project docs, and accepted behavior is synced after human acceptance.
- The Evolution Loop can **start from any of the eight steps** and re-enter **any step that is relevant**. It does not require a prior release, a roadmap update, or a fixed sequence.
- Examples: a concept prototype at Step 3 disproves the target user's assumption, so revisit Step 1; UI design at Step 5 reveals a domain misunderstanding, so revisit Step 2; implementation at Step 7 reveals a product-scope problem, so revisit Step 4; user feedback after Step 8 can lead to any relevant earlier step.
- **Distinguish local quality iteration from product evolution:** fixing tests or correcting code within agreed requirements stays in the Implementation Loop; revising the solution within agreed product intent stays in the Design Spec Loop. Use the Evolution Loop when learning warrants rethinking product assumptions, direction, scope or a consequential decision.
- Product-critical changes remain human decisions. A response may be to take no action. There is no mandated endpoint; stop, continue, defer or pivot according to what is learned. Do not restart all eight stages mechanically.

## Review terminology

| Review | Object | Timing |
| --- | --- | --- |
| Design Spec Review (EGM-style) | Design expressed in the Spec, assumptions, feasibility and implementation strategy | Before substantial coding |
| Code Review | Newly changed code and tests | After coding, within Implementation Loop |
| Spec Conformance | Expected behavior versus actual implementation | Within Implementation Loop and acceptance |
| Scenario Review | **CoolFlow itself**: do Agents follow the Standard correctly? | Internal CoolFlow validation in `flowreviews/scenarios/`; retained in the source repository, not copied to target applications |

Do not mistake internal CoolFlow **Scenario Review** for a fourth product-development Loop.
