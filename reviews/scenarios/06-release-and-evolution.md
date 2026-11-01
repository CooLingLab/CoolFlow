# S06 — Cross-stage Evolution and release feedback

Environment: an application with a partially completed development objective, documented new evidence that challenges an earlier assumption (before release), and a separate accepted/released increment with later user feedback.

Expected:
1. Human acceptance triggers Documentation Sync and selective archiving, **not** a fictional independent Knowledge Loop.
2. Release status is distinguishable from accepted-but-not-yet-shipped features.
3. **Before release**, new evidence during any step can trigger the **Evolution Loop**, returning to any relevant earlier or later Development Flow step without requiring a release or mandatory roadmap change.
4. **After release**, actual feedback may also trigger Evolution and a relevant roadmap or product change. Neither an enforced starting step nor a mandatory return to Roadmap is assumed.
5. Only affected steps are revisited; the Agent must not restart all eight steps by default.
6. Routine implementation defects and local Spec corrections are treated as **Implementation Loop** or **Design Spec Loop** iterations, not automatically as product Evolution.
7. New proposed functionality remains in roadmap or `docs/work/` until accepted; do not confuse it with existing `docs/features/`.
8. A material flaw in the Spec can return work from Implementation Loop to Design Spec Loop; reconsider the broader product direction only when new evidence warrants it.

Review against actual documentation updates and evidence of product decisions; do not rely solely on the executor's summary.
