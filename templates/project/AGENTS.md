# Project Agent Instructions

## Development Flow

Use this recommended CoolFlow lifecycle; skip, merge or revisit stages as project complexity requires:

1. Idea → Brainstorm — clarify problem, users and value.
2. Lightweight strategic DDD — establish core concepts, boundaries and language.
3. Concept Prototype → Validation — test core assumptions cheaply.
4. Roadmap — define MVP and future versions.
5. UI Prototype — design interactions for the current version.
6. Unified Spec → optional independent design review — write an implementable, verifiable design.
7. Harness + Agent Loop — code → test → code review → Spec conformance → fix.
8. Human Acceptance → Docs Sync → Release — record accepted reality and learn.

## Three Loops at two levels

- **Design Spec Loop (internal):** draft unified Spec → independent design review (EGM-style when useful) → revise / re-review until ready.
- **Implementation Loop (internal):** code → test → code review → Spec conformance → fix, returning to Design Spec Loop if the design itself is wrong.
- **Evolution Loop (outer):** release → feedback → roadmap → revisit only the necessary Development Flow stages.

**Documentation Sync is not a Loop:** after human acceptance, update accepted/current docs, verify consistency and selectively archive work. Acceptance and release may occur at different times.

## Documentation Map

- `docs/product.md`: long-term product purpose and positioning.
- `docs/roadmap.md`: planned releases, including not-yet-built items.
- `docs/domain.md`: domain terms, boundaries and core rules.
- `docs/features/`: accepted actual feature behavior; never speculative plans.
- `docs/work/<objective>/spec.md`: full active design for a development objective. Open `work/001-mvp/` when initial discovery begins, **not** on folder initialization.
- Optional within work: `prd.md` for substantial product requirements; `design.md` for complex technical design; `tasks.md` only for persistent progress tracking; `prototypes/` for explorations.
- `docs/work/archive/`: selective historical specs, key decisions, and verification evidence.
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

## Project-specific Conventions

- Product / stack: To decide.
- Build and test commands: To decide.
- Other project constraints: To decide.
