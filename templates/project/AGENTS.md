# Project Agent Instructions

## Development Flow

Use this recommended CoolFlow lifecycle; skip, merge or revisit stages as project complexity requires:

1. Idea → Brainstorm — clarify problem, users and value; analyze relevant competitors, alternatives and workarounds; identify an opportunity and product hypothesis.
2. Lightweight strategic DDD — establish an initial domain model: core concepts, semantic boundaries, language and business rules. Tactical domain design belongs to Design Spec Loop; keep `docs/domain.md` provisional and evolving.
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

## Documentation

Follow `docs/documentation.md` when creating, updating or archiving project documents.

## Working Rules

1. Read the files relevant to the current task; do not assume an empty template is complete.
2. Preserve existing project content, conventions and code. No destructive replacement without permission.
3. Do not invent requirements, user decisions or successful tests. Mark unknowns `Not started` / `To decide`.
4. For substantial changes: review the current Spec draft and related context before coding, resolve important findings and confirm design readiness; review new code and Spec conformance after coding.
5. AI may implement and verify routine work. Ask the human to decide major product trade-offs and to accept the result.
6. Record human-confirmed plans with their actual status; sync durable docs describing accepted/current behavior after human acceptance. Acceptance and production release are distinct.
7. Manage ordinary task lists in the active Agent session.
8. Before related work, consult relevant existing Solutions when available.
9. If the project uses a package manager, generate and commit its lockfile; CI must install from the lockfile using the package manager's frozen/locked mode.

## Project-specific Conventions

- Product / stack: To decide.
- Build and test commands: To decide.
- Other project constraints: To decide.
