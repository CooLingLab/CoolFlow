# CoolFlow lifecycle (recommended Flow)

The human developer's overarching priorities are described by the [Golden Rules](golden-rules.md). The rules guide decisions across every stage but do not create additional phases or mandatory artifacts.

CoolFlow describes **one flexible Development Flow and three adaptive Loops**, not a rigid stage scheduler. The **Evolution Loop can be triggered from any stage**, whenever feedback, new ideas, or changing needs call for reconsidering a product decision; it may return to any relevant stage. Each stage suggests outputs and questions; the developer and Agent decide what adds value. No engine, transition state, or gate file is required.

| Stage | Purpose | Typical result |
| --- | --- | --- |
| 1. Idea → Brainstorm | Clarify the problem, users and value; analyze the competitive landscape; identify an opportunity and testable product hypotheses | Evolving `product.md`; proportionate market/competitor findings and exploration notes in current work |
| 2. Lightweight strategic DDD | Ubiquitous language, bounded contexts, core invariants | `domain.md` |
| 3. Concept Prototype → Validation | Test critical experience / feasibility assumptions quickly | Interactive HTML or other prototype under `work/<objective>/prototypes/` |
| 4. Roadmap | Define MVP/current version and later possibilities | `roadmap.md`; optional PRD for substantial product scope |
| 5. UI Prototype | Design the current version's interactions | Prototype and notes in the relevant work directory |
| 6. Design Spec Loop | Capture requirements, solution, acceptance criteria and implementation strategy; review the design and revise when useful | `work/<objective>/spec.md`; optional `design.md` |
| 7. Implementation Loop | Implement, test, review changed code, verify Spec conformance, fix and repeat (often Agent-assisted) | Tested code and review evidence; tasks live in Agent session unless persistent tracking is needed |
| 8. Human Acceptance → Documentation Sync → Release | Human accepts actual behavior; sync durable docs; archive meaningful history; release and learn | Updated `features/`, domain/roadmap/feature-map as relevant; `work/archive/` |

## Step 1 — Idea → Brainstorm

The goal is not to turn every idea into a build plan immediately. First understand the problem and user, then examine how the need is already being served, identify a credible opportunity, and formulate a product hypothesis.

A useful sequence is:

1. **Problem & User Discovery** — clarify who experiences the problem, in what context, how important it is, and what outcome they need. Avoid defining the solution too early.
2. **Competitive Landscape Analysis** — research existing ways of solving the same or adjacent problem:
   - **Direct competitors:** products serving similar users with a similar core job.
   - **Indirect alternatives:** products that solve the need in a different way.
   - **Substitutes and workarounds:** offline methods, general-purpose tools, spreadsheets, communities, or combinations users currently rely on.
   - Compare only decision-relevant dimensions: target users, core value, main experience, key capabilities, pricing/business model, user feedback, limitations and unmet needs.
3. **Opportunity Identification** — synthesize what existing solutions do well, where users encounter friction, which audiences or use cases are underserved, and whether a meaningful opportunity exists. Existing competitors can validate demand; their presence alone does not invalidate an idea. A lack of visible competitors does not by itself prove demand.
4. **Product Hypothesis** — state what you propose to build, for whom, which problem it will solve, why the proposed approach may be better or meaningfully different, and what assumptions still need validation.

Keep the research proportionate to the decision. A small idea or narrow feature may need only a quick scan or no separate research; a new product or unfamiliar market may justify deeper analysis. Use credible, preferably primary sources; record links and research dates, and distinguish observed facts from interpretation, assumptions and unknowns. Do not present a feature checklist as market validation or invent competitor details.

Record concise findings and links in the current work's `brainstorm.md` when useful. Create a separate `competitive-landscape.md` only when the research is substantial enough to maintain independently. Neither document is mandatory for every idea. This is an exploration activity, not a new stage or a rigid gate.

**Stage 6 is not a requirement to run EGM.** For complex, risky or unfamiliar work, use an independent design-review Agent; for small fixes, a concise Spec/checklist may be adequate.

**Human Acceptance is distinct from Release.** After acceptance, Documentation Sync updates the current project truth and selectively archives work; it is **not an independent top-level Loop**. Accepted but not yet shipped behavior must be described accurately, including release status when relevant.

For a new app, the first work objective can be `work/001-mvp/`, **opened during discovery when useful** (not during folder initialization). Discovery notes and prototypes may live there without a Spec; write the unified `spec.md` when the selected objective reaches **Design Spec Loop (Step 6)**. The directory label does not presume MVP scope is already final.

**Evolution Loop (cross-stage):** New Input → Reassess → Adapt. At **any step**, feedback, new ideas, or changing needs may prompt reconsideration of product direction, scope, or key decisions and a return to **any relevant step**. For example, a failed concept prototype (Step 3) might return to Brainstorm (Step 1), or an invalid product assumption uncovered during implementation (Step 7) might require revisiting Roadmap (Step 4). Post-release feedback is one trigger, **not a prerequisite**. Ordinary design or code corrections remain in the corresponding local quality Loop. Never require a fixed start/end, automatic roadmap revision, or mechanical repetition of all eight stages.

See [quality loops](loops.md) and [documentation rules](../standards/documentation.md).
