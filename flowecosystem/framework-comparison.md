# Framework Comparison

**Research snapshot: 2026-11-01**

This comparison looks at complete AI-assisted software-development workflows and the most relevant adjacent systems. It is intended to show **what each project explicitly provides, where it is partial, and where CoolFlow may need a complementary solution**. It is not a ranking.

## How to read the matrix

- **● Explicit** — the project documents a first-class workflow, artifact or mechanism for this capability.
- **◐ Partial** — the capability exists through optional components, adjacent features or a less formal mechanism; it is not the main organizing principle.
- **— Not core** — no dedicated mechanism was identified in the reviewed official documentation.

A mark indicates documented coverage, not that every workflow was executed or independently tested. For CoolFlow, marks describe the current v0.1 draft; they do **not** imply that real-project validation is complete.

## Projects compared

GitHub stars are approximate snapshots retrieved on 2026-11-01. They indicate community attention, not quality, suitability or endorsement. Counts change over time.

| Project | Stars | What it is | Primary emphasis |
|---|---:|---|---|
| [CoolFlow](https://github.com/CooLingLab/CoolFlow) | 0 | Human-led methodology and documentation standard | Product lifecycle, three adaptive Loops, accepted/current documentation |
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | 25.8k | Cross-harness plugin with 36 Skills | Brainstorm → plan → work → simplify → review → compound learning |
| [Superpowers](https://github.com/obra/superpowers) | 310.2k | Agentic Skills framework and development methodology | Socratic brainstorming, executable plans, TDD, subagent execution, review and worktree isolation |
| [GStack](https://github.com/garrytan/gstack) | 138.5k | Opinionated virtual engineering-team toolkit | Product/CEO review, design, architecture, QA, security, documentation, release and persistent knowledge |
| [PStack](https://github.com/cursor/plugins/tree/main/pstack) | No separate count | Plugin distributed inside Cursor's plugins repository | Poteto Mode, 23 playbooks, multi-model delegation, rigorous verification and session handoff |
| [Addy Osmani Agent Skills](https://github.com/addyosmani/agent-skills) | 112.3k | Lifecycle-oriented Skills collection (25 Skills) | Define → Plan → Build → Verify → Review → Ship, with routing and Skill evaluations |
| [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) | 54.8k | Full AI-driven development method with specialized agents and workflows | Adaptive product discovery, requirements, architecture, UX, implementation, verification and retrospectives |
| [GSD Core](https://github.com/open-gsd/gsd-core) | 11.1k | Context-engineering and spec-driven development framework | Discuss → Plan → Execute → Verify → Ship, fresh-context subagents and durable project state |

**PStack counting note:** PStack is maintained as a plugin within [cursor/plugins](https://github.com/cursor/plugins), not as a separate repository with its own independently attributable Star count. The parent repository had approximately 14.9k stars at the snapshot date; that number must not be presented as PStack's own stars.

**GSD naming note:** the older `gsd-build/get-shit-done` repository is archived and points users to [GSD Core](https://github.com/open-gsd/gsd-core). This comparison uses the active successor, not the archived repository's historical star count.

**BMAD version note:** the repository distinguishes its stable v6 line from the v7 preview/alpha line. Check the upstream release guidance before adopting preview workflows in a production project.

## Lifecycle and capability matrix

| Capability | CoolFlow | Compound | Superpowers | GStack | PStack | Addy Skills | BMAD | GSD Core |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Idea clarification / brainstorming | ● | ● | ● | ● | ◐ | ● | ● | ● |
| Strategic DDD / domain modeling | ● | ◐ | — | ◐ | ● | ◐ | ◐ | ◐ |
| Concept prototype / assumption testing | ● | ● | ◐ | ◐ | ● | — | ◐ | ◐ |
| Product roadmap / version slicing | ● | ◐ | — | ◐ | ◐ | — | ● | ● |
| UI prototype / design exploration | ● | ◐ | ◐ | ● | ◐ | ◐ | ● | ● |
| Spec and technical design | ● | ● | ● | ● | ● | ● | ● | ● |
| Independent design / plan review | ● | ● | ◐ | ● | ● | ● | ● | ● |
| TDD / implementation discipline | ◐ | ● | ● | ● | ● | ● | ● | ● |
| Code review | ● | ● | ● | ● | ● | ● | ● | ● |
| Runtime / UI verification and QA | ◐ | ◐ | ◐ | ● | ● | ● | ● | ● |
| Explicit human acceptance checkpoint | ● | ◐ | ◐ | ◐ | ◐ | ● | ● | ◐ |
| Post-acceptance documentation / release workflow | ● | ◐ | ◐ | ● | ◐ | ◐ | ◐ | ◐ |
| Reusable project-learning capture | ◐* | ● | ◐ | ● | ◐ | ◐ | ◐ | ● |
| Project-state awareness (position, progress, next action) | —* | ◐ | ◐ | ◐ | — | — | ◐ | ● |
| Session handoff / resume context | — | ● | ◐ | ● | ● | — | ◐ | ● |
| Explicit cross-stage evolution / learn-and-adjust loop | ● | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ◐ |

* **CoolFlow's `—*` is deliberate.** “Know the Actual State” is a human-facing Golden Rule, not an Agent-readable project-state mechanism. CoolFlow v0.1 does not prescribe a STATE.md, status schema, automatic retrieval protocol or session-handoff format. Cross-stage knowledge capture is also not yet a normative feature.

### What the comparison reveals

1. **CoolFlow's strongest distinction is its product-lifecycle framing.** It explicitly includes lightweight strategic DDD, concept validation, roadmap and UI prototyping before the implementation-heavy loops. BMAD also covers much of this territory, so CoolFlow should not claim to be the only full-lifecycle method.
2. **Implementation quality is a mature, crowded area.** Superpowers, Compound Engineering, GStack, PStack, Addy Skills, BMAD and GSD Core all provide substantial implementation, testing or review workflows. CoolFlow should reference proven solutions rather than reimplement every engineering practice.
3. **State awareness, session handoff and knowledge capture are three different capabilities.** GSD Core has the clearest explicit project-state model; GStack has scoped persistent project/run state; Compound Engineering and PStack have useful handoff mechanisms. A solution corpus or Agent memory is not automatically a current project-state model.
4. **A complete suite may overlap with CoolFlow's artifacts and lifecycle.** Spec Kit, OpenSpec, BMAD, GSD Core and Compound Engineering can each introduce their own planning files, lifecycle commands or state conventions. Adopting one wholesale requires an explicit integration decision.

### What “state awareness” means in this comparison

**Project-state awareness** means a workflow can recover a durable view of the project's current position, progress and likely next action from explicit project artifacts or state records. A plan file, a general memory store, a status badge, or a session transcript alone does not qualify as a complete project-state model.

**Session handoff / resume** means preserving enough context about an interrupted unit of work for a later session or a cold-start Agent to continue safely. It is related to project state, but it answers a different question.

- **GSD Core — explicit project state.** `STATE.md` is read at the start of workflows and updated after significant actions; it combines machine-readable frontmatter with a compact human-readable digest. `state validate` and `state sync` check or repair drift against filesystem evidence. A versioned `.planning/state.json` is published for external readers such as dashboards. Session handoff is separate: GSD also has `HANDOFF.json` and `.continue-here.md`. See [STATE.md reference](https://github.com/open-gsd/gsd-core/blob/next/docs/reference/state-md.md), [state consistency gates](https://github.com/open-gsd/gsd-core/blob/next/docs/features/statemd-consistency-gates.md), [machine-readable state contract](https://github.com/open-gsd/gsd-core/blob/next/docs/features/machine-readable-state-contract-planningstatejson.md), and [pause-work workflow](https://github.com/open-gsd/gsd-core/blob/next/gsd-core/workflows/pause-work.md).
- **GStack — partial/scoped project state.** It keeps per-project checkpoints, learnings and timeline data under a persistent state root, and its unattended autoplan runner maintains structured run state. This is more than chat memory, but it is not one small, canonical lifecycle digest equivalent to GSD's STATE.md. See [GStack state root](https://github.com/garrytan/gstack/blob/main/docs/state-root.md) and [autoplan state implementation](https://github.com/garrytan/gstack/blob/main/lib/autoplan-state.ts).
- **Compound Engineering — partial/scoped state and explicit handoff.** Plans and work-unit state support execution continuity, while `ce-handoff` provides a dedicated create/resume workflow. It does not prescribe one universal project-wide status digest. See [ce-handoff](https://github.com/EveryInc/compound-engineering-plugin/blob/main/docs/guides/ce-handoff.md).
- **PStack — explicit session handoff, not project-wide state.** Its “Pause safely” playbook writes a resume note containing intent, progress, verified work, current state, next steps and key files. See [pause-safely](https://github.com/cursor/plugins/blob/main/harness/pstack/claude-code/skills/poteto-mode/playbooks/pause-safely.md).
- **BMAD and Superpowers — artifact-led continuity.** Their plans and workflow-specific resume guidance help continue work, but the reviewed sources do not establish a single canonical project-state digest with the same explicit read/update/validate contract as GSD.
- **CoolFlow — principle only.** The Golden Rule asks the human to know the actual state; v0.1 intentionally does not define an Agent state file or state engine.

GitHub Spec Kit and OpenSpec are primarily specification/change-management systems. Their per-change artifacts and lifecycle statuses should not be confused with a project-wide view of current position and next action.

## Adjacent specification-driven systems

These projects are important to CoolFlow, but they are better classified as **specification / change-management systems** than as full product-lifecycle methodologies.

| Project | Stars (2026-11-01) | Main contribution | Relationship to CoolFlow |
|---|---:|---|---|
| [GitHub Spec Kit](https://github.com/github/spec-kit) | 144.5k | Spec-driven development toolkit with constitution, specify, plan, tasks and customizable workflows | Strong overlap with Step 6 and parts of Step 7; can replace or complement the Design Spec Loop |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | 73.6k | Change-oriented specs with proposal, requirements, design, tasks, verification and archive | Strong reference for change-scoped documentation and syncing accepted specs |

Other important methods and component collections:

- [Google's Elephant-Goldfish Model (EGM)](https://github.com/google/elephant-goldfish-model) — a design-review method, not a complete development lifecycle.
- [DDD Crew Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process) — a domain-discovery and modeling process, not a general AI coding framework.
- [Matt Pocock's Skills](https://github.com/mattpocock/skills) — a collection of focused Skills, including Grill Me, not one mandatory end-to-end framework.

## Implications for CoolFlow

CoolFlow should not attempt to become a second implementation harness. Its durable value is to:

- define the human-facing lifecycle and decision boundaries;
- define the minimum documentation contract and the meaning of each artifact;
- make stage transitions and cross-stage evolution understandable;
- recommend compatible external solutions for concrete activities;
- preserve project-specific knowledge without requiring a particular Agent runtime.

A user should be able to adopt CoolFlow with a plain coding Agent, use a single external Skill where useful, or selectively adopt a larger suite. They should not be required to install all the projects in this comparison.

See the [Solution Catalog](catalog.md) for stage-by-stage recommendations.
