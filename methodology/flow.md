# CoolFlow lifecycle (recommended Flow)

The human developer's overarching priorities are described by the [Golden Rules](golden-rules.md). The rules guide decisions across every stage but do not create additional phases or mandatory artifacts.

CoolFlow describes **one flexible Development Flow and three adaptive Loops**, not a rigid stage scheduler. The **Evolution Loop can be triggered from any stage**, whenever new evidence or changed assumptions call for reconsidering a product decision; it may return to any relevant stage. Each stage suggests outputs and questions; the developer and Agent decide what adds value. No engine, transition state, or gate file is required.

| Stage | Purpose | Typical result |
| --- | --- | --- |
| 1. Idea → Brainstorm | Define the problem, users, value and hypotheses | Evolving `product.md`; exploration notes in current work |
| 2. Lightweight strategic DDD | Ubiquitous language, bounded contexts, core invariants | `domain.md` |
| 3. Concept Prototype → Validation | Test critical experience / feasibility assumptions quickly | Interactive HTML or other prototype under `work/<objective>/prototypes/` |
| 4. Roadmap | Define MVP/current version and later possibilities | `roadmap.md`; optional PRD for substantial product scope |
| 5. UI Prototype | Design the current version's interactions | Prototype and notes in the relevant work directory |
| 6. Design Spec Loop | Capture requirements, solution, acceptance criteria and implementation strategy; review the design and revise when useful | `work/<objective>/spec.md`; optional `design.md` |
| 7. Implementation Loop | Implement, test, review changed code, verify Spec conformance, fix and repeat (often Agent-assisted) | Tested code and review evidence; tasks live in Agent session unless persistent tracking is needed |
| 8. Human Acceptance → Documentation Sync → Release | Human accepts actual behavior; sync durable docs; archive meaningful history; release and learn | Updated `features/`, domain/roadmap/feature-map as relevant; `work/archive/` |

**Stage 6 is not a requirement to run EGM.** For complex, risky or unfamiliar work, use an independent design-review Agent; for small fixes, a concise Spec/checklist may be adequate.

**Human Acceptance is distinct from Release.** After acceptance, Documentation Sync updates the current project truth and selectively archives work; it is **not an independent top-level Loop**. Accepted but not yet shipped behavior must be described accurately, including release status when relevant.

For a new app, the first work objective can be `work/001-mvp/`, **opened when discovery actually starts** (not during folder initialization). The label does not presume MVP scope is already final.

**Evolution Loop (cross-stage):** New evidence or changed assumptions **at any step** → reassess product direction, scope, or key decisions → return to **any relevant step**. For example, a failed concept prototype (Step 3) might return to Brainstorm (Step 1), or an invalid product assumption uncovered during implementation (Step 7) might require revisiting Roadmap (Step 4). Post-release feedback is one trigger, **not a prerequisite**. Ordinary design or code corrections remain in the corresponding local quality Loop. Never require a fixed start/end, automatic roadmap revision, or mechanical repetition of all eight stages.

See [quality loops](loops.md) and [documentation rules](../standards/documentation.md).
