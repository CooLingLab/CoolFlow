# CoolFlow Loops: two internal, one outer

CoolFlow has **one Development Flow** and **three Loops at two levels**:

- **Design Spec Loop:** design quality before substantial coding (internal).
- **Implementation Loop:** implementation quality during coding (internal).
- **Evolution Loop:** ongoing product direction across releases (outer; wraps the Flow).

The Loops describe useful feedback cycles, **not** an Agent orchestration system. Stages and review depth remain adaptable. **Documentation Sync is a post-acceptance step, not a fourth Loop.**

## 1. Design Spec Loop — design quality

`Draft Unified Spec → Independent Design Review → Revise → Re-review ↻`

**Goal:** make the *design*, expressed through the Spec, clear, correct, and implementable.

- The unified `spec.md` carries context, goals/non-goals, behavior and acceptance criteria, technical decisions, trade-offs, implementation strategy, and verification. Optional PRD or detailed design can be linked without duplicating content.
- Independent review is preferably fresh-context. The reviewer reads the Spec, linked references and relevant **existing code**, rather than inheriting the drafter's assumptions.
- Seek missing cases, risky assumptions, overengineering, incompatibilities, feasibility issues, and unclear implementation steps.
- Revise and re-review until important blockers are resolved. The human decides product-critical trade-offs.
- EGM Goldfish is a **recommended optional** review method, not a dependency.
- Reading existing code to check design feasibility **is not the same as reviewing code newly produced for this task**.
- `tasks.md` is optional and only needed for persistent progress tracking beyond the Agent's session or existing task system.

**Exit:** design is sufficiently reviewed, coherent, and ready to implement for the task's risk level.

## 2. Implementation Loop — code quality

`Code → Test → Code Review → Spec Conformance → Fix ↻`

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

## 3. Evolution Loop — product iteration (outer)

`Release → Observe usage / Feedback → Reprioritize Roadmap → Next relevant Flow stages ↻`

**Goal:** decide what to build or change next based on product use, learning, or new requirements.

- This Loop **wraps** the Development Flow; it is not simply another stage after Implementation.
- Feedback may change product scope, domain assumptions, prototypes, or the roadmap.
- For future releases, repeat only relevant stages. A minor fix need not restart Brainstorm or strategic DDD.
- The loop has no mandatory fixed endpoint; stop or pivot based on actual product goals and context.

## Review terminology

| Review | Object | Timing |
| --- | --- | --- |
| Design Spec Review (EGM-style) | Design expressed in the Spec, assumptions, feasibility and implementation strategy | Before substantial coding |
| Code Review | Newly changed code and tests | After coding, within Implementation Loop |
| Spec Conformance | Expected behavior versus actual implementation | Within Implementation Loop and acceptance |
| Scenario Review | **CoolFlow itself**: do agents follow the Standard correctly? | Internal CoolFlow development only; remove from final release tree |

Do not mistake internal CoolFlow **Scenario Review** for a fourth product-development Loop.
