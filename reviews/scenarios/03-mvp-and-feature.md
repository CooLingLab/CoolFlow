# S03 — Work objective and feature lifecycle

Environment: initialized nature-catalog app; user explicitly starts product Brainstorm then later adds AI bird identification.

Expected:
1. Initialization itself did not create the MVP work objective.
2. Discovery may open `docs/work/001-mvp/` for notes/prototypes, but must **not** require `spec.md` merely because discovery started; open questions are not fabricated.
3. Prototypes and optional PRD/design belong to the relevant work objective when useful. A unified `spec.md` is drafted when the selected objective enters **Design Spec Loop**.
4. When AI bird identification is proposed, it belongs in discovery/roadmap or a new work objective; write its Spec when entering **Design Spec Loop**, **not** accepted `features/`.
5. `tasks.md` is absent unless explicit persistence need is established.
6. The **Design Spec Loop** reviews the current draft, resolves material issues and confirms readiness before substantial implementation; the **Implementation Loop** reviews new code and verifies Spec conformance after coding.

Check actual tree, document links and recorded decisions.
