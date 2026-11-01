# CoolFlow lifecycle (recommended Flow)

CoolFlow describes **a flexible development paradigm**, not a rigid stage scheduler. Each stage suggests outputs and questions; the developer and Agent decide whether the stage adds value. No engine, transition state, or gate file is required.

| Stage | Purpose | Typical result |
| --- | --- | --- |
| 1. Idea → Brainstorm | Define the problem, users, value and hypotheses | Evolving `product.md`; exploration notes in current work |
| 2. Lightweight strategic DDD | Ubiquitous language, bounded contexts, core invariants | `domain.md` |
| 3. Concept Prototype → Validation | Test critical experience / feasibility assumptions quickly | Interactive HTML or other prototype under `work/<objective>/prototypes/` |
| 4. Roadmap | Define MVP/current version and later possibilities | `roadmap.md`; optional PRD for substantial product scope |
| 5. UI Prototype | Design the current version's interactions | Prototype and notes in the relevant work directory |
| 6. Unified Spec / Design Readiness | Capture requirement, behavior, solution, acceptance checks and implementation strategy; optionally run independent EGM-style review | `work/<objective>/spec.md`; optional `design.md` |
| 7. Harness + Agent Loop | Implement, run tests, review code, verify against Spec, fix | Tested code and review evidence; tasks live in Agent session unless persistent tracking is needed |
| 8. Human Acceptance → Documentation Sync → Release | Human accepts actual behavior; sync durable docs; archive meaningful history; release and learn | Updated `features/`, domain/roadmap/feature-map as relevant; `work/archive/` |

**Stage 6 is not a requirement to run EGM.** For complex, risky or unfamiliar work, use an independent design-review Agent; for small fixes, a concise Spec/checklist may be adequate.

**Human Acceptance is distinct from Release.** Accepted but not yet shipped behavior must be described accurately, including release status when relevant.

For a new app, the first work objective can be `work/001-mvp/`, **opened when discovery actually starts** (not during folder initialization). The label does not presume MVP scope is already final.

Subsequent releases revisit only relevant stages; never re-run every step mechanically.

See [quality loops](loops.md) and [documentation rules](../standards/documentation.md).
