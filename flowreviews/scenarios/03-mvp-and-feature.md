# S03 — Work objective and feature lifecycle

Environment: initialized nature-catalog app; user explicitly starts product Brainstorm then later adds AI bird identification.

Expected:
1. Initialization itself did not create the MVP work objective.
2. Step 1 Brainstorm clarifies the problem and target users, then performs proportionate competitive landscape research across direct competitors, indirect alternatives, substitutes and existing workarounds. Findings include source links/dates, distinguish evidence from assumptions, and inform an opportunity/product hypothesis; exhaustive research is not required for a small project.
3. Discovery may open `docs/work/001-mvp/` for notes/prototypes, but must **not** require `spec.md` merely because discovery started; open questions are not fabricated.
4. Prototypes and optional PRD/design belong to the relevant work objective when useful. A unified `spec.md` is drafted when the selected objective enters **Design Spec Loop**.
5. When AI bird identification is proposed, it belongs in discovery/roadmap or a new work objective; write its Spec when entering **Design Spec Loop**, **not** accepted `features/`.
6. `tasks.md` is absent unless explicit persistence need is established.
7. The **Design Spec Loop** reviews the current draft, resolves material issues and confirms readiness before substantial implementation; the **Implementation Loop** reviews new code and verifies Spec conformance after coding.

Check actual tree, document links and recorded decisions.
