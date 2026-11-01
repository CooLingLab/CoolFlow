# Project Agent Instructions

## Development Flow

Use this recommended CoolFlow lifecycle; skip, merge or revisit stages as project complexity requires:

1. Idea → Brainstorm — clarify problem, users and value.
2. Lightweight strategic DDD — establish core concepts, boundaries and language.
3. Concept Prototype → Validation — test core assumptions cheaply.
4. Roadmap — define MVP and future versions.
5. UI Prototype — design interactions for the current version.
6. Design Spec Loop — write a unified, verifiable Spec → review when useful → revise.
7. Implementation Loop — code → test → code review → Spec conformance → fix (Agent-assisted as appropriate).
8. Human Acceptance → Docs Sync → Release — record accepted reality and learn.

## Three Adaptive Loops

- **Design Spec Loop (Step 6):** Draft → Review → Refine. Develop a unified Spec until it is ready for implementation.
- **Implementation Loop (Step 7):** Build → Test → Review → Fix. Check the implementation against the Spec and acceptance criteria until it is ready for human acceptance; return to Design Spec Loop if the design itself is wrong.
- **Evolution Loop (cross-stage):** New Input → Reassess → Adapt. At **any step**, reconsider important product decisions in response to feedback, new ideas, or changing needs, and revisit **any relevant step** as needed. A prior release or roadmap revision is **not** required. Routine design/code fixes belong to their local quality Loops.

**Documentation Sync is not a Loop:** after human acceptance, update accepted/current docs, verify consistency and selectively archive work. Acceptance and release may occur at different times.

## Documentation Map

- `docs/product.md`: concise project-level Product Brief (why, for whom, value and boundaries); it is **not a PRD**.
- `docs/roadmap.md`: planned releases, including not-yet-built items.
- `docs/domain.md`: domain terms, boundaries and core rules.
- `docs/features/`: accepted actual feature behavior; never speculative plans.
- `docs/work/<objective>/spec.md`: full active design for a development objective. Open `work/001-mvp/` when initial discovery begins, **not** on folder initialization.
- Optional within work: `prd.md` for substantial product requirements; `design.md` for complex technical design; `tasks.md` only for persistent progress tracking; `prototypes/` for explorations.
- `docs/work/archive/`: selective historical Specs, work-specific decisions and verification evidence.
- Optional `docs/solutions/`: verified, non-obvious, durable and material engineering knowledge; consult relevant entries before related work and capture only when the finding is worth reusing.
- Optional `docs/adr/`: one record per consequential architecture or technical decision; preserve history and supersede decisions rather than silently rewriting them.
- Optional `docs/feature-map.md`: where/how to navigate and verify actual UI.

## Working Rules

1. Read the files relevant to the current task; do not assume an empty template is complete.
2. Preserve existing project content, conventions and code. No destructive replacement without permission.
3. Do not invent requirements, user decisions or successful tests. Mark unknowns `Not started` / `To decide`.
4. For substantial changes: independently review the design before coding; review the new code and Spec conformance after coding.
5. AI may implement and verify routine work. Ask the human to decide major product trade-offs and to accept the result.
6. Update durable docs only to reflect accepted reality. Human acceptance and production release are distinct.
7. Manage ordinary task lists in the active Agent session; create `tasks.md` only when persistent state is needed.
8. The project may evolve these conventions independently; it does not need to track upstream CoolFlow releases.
9. Before related work, consult only relevant existing Solutions. Capture a new Solution only when a verified finding is non-obvious, durable and material; update an existing record instead of duplicating it.
10. Create an ADR only for a consequential architecture or technical decision. Record one decision per file and supersede old records rather than silently rewriting them.

## Project-specific Conventions

- Product / stack: To decide.
- Build and test commands: To decide.
- Other project constraints: To decide.
