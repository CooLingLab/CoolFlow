# CoolFlow baseline for Skill authors

This is a compact summary maintained with `coolflow-skill-creator`, not a copy of the complete Standard. The repository's `standards/` remain authoritative; update this summary alongside them when the applicable rules change.

## Authority and refresh

- In a confirmed CoolFlow source checkout, consult the relevant current working-tree files in `standards/` first, and `methodology/` for the Flow; disclose local modifications or version differences when relevant. Do not mistake an installed Skill or application for that checkout.
- Otherwise, use this summary only for the points it actually covers. An installed project owns its local `AGENTS.md` and `docs/documentation.md`; those conventions may evolve independently. Do not replace them from this summary.
- If the user requests a current comparison and network access is allowed, check the [official repository](https://github.com/CooLingLab/CoolFlow) and report the actual differences. Update the bundled summary as a normal authorized maintenance change rather than silently changing an installed copy. If a necessary detail is absent and the authoritative source cannot be obtained, leave it explicitly unverified.

Sources: [documentation standard](https://github.com/CooLingLab/CoolFlow/blob/main/standards/documentation.md), [review standard](https://github.com/CooLingLab/CoolFlow/blob/main/standards/reviews.md), [development flow](https://github.com/CooLingLab/CoolFlow/blob/main/methodology/flow.md), and [adaptive loops](https://github.com/CooLingLab/CoolFlow/blob/main/methodology/loops.md).

## Flow and document ownership

CoolFlow has one flexible Flow: (1) Idea → Brainstorm, (2) Lightweight Strategic DDD, (3) Concept Prototype → Validation, (4) Roadmap, (5) UI Prototype, (6) Design Spec Loop, (7) Implementation Loop, and (8) Human Acceptance → Documentation Sync → Release. Stages may be skipped, combined or revisited; do not force a Skill through all of them.

The three adaptive Loops are Design Spec at Step 6, Implementation at Step 7, and cross-stage Evolution. Evolution can start at **any** step and revisit **any relevant** step without waiting for release or a roadmap update. Documentation Sync is a post-acceptance step, not a fourth Loop. Human acceptance and release are distinct.

Exploration may use a work directory without a Spec. When a selected objective enters Design Spec Loop, the default is one unified Spec; persistent tasks, PRD, detailed design and prototypes are optional when needed. Accepted/current knowledge is separate from work in progress. Respect existing project conventions and one authoritative location per fact; do not add a second mandatory tracker or overwrite project files.

For meaningful project results from a Skill, the standard calls for choosing the appropriate project-local document and recording the result within the authorized task before finishing. Discovery notes and a selected objective's Spec have different homes; use an existing authoritative record when possible or create one at the established project location when needed and authorized. Distinguish observed facts, user claims, decisions, unverified findings, assumptions and open questions from one another; user claims may not be independently verified. Human-confirmed, durable project-level plans and decisions may be recorded with their actual status. A roadmap may summarize future feature scope labeled as planned or proposed; keep detailed unaccepted behavior and unresolved designs in work records or a Spec, and sync affected accepted/current facts after human acceptance without waiting for release. Honor local conventions. If writing is prohibited, unavailable or the destination is unclear, report what remains unrecorded instead of inventing a target. Do not create files for trivial results solely to satisfy a checklist.

Independent design review is proportionate to risk; review implementation and Spec conformance after changes. EGM, external suites, subagent runtimes and CoolFlow Skills are optional tools, not prerequisites for using CoolFlow. Internal CoolFlow Scenario Reviews stay in its source repository, not target applications.
