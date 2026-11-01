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
| Post-acceptance documentation / release workflow | ● | ◐ | ◐ | ● | ◐ | ● | ◐ | ◐ |
| Reusable project-learning capture | ◐* | ● | ◐ | ● | ◐ | ◐ | ◐ | ● |
| Persistent cross-session state / handoff | ◐* | ◐ | ◐ | ● | ◐ | ◐ | ● | ● |
| Explicit cross-stage evolution / learn-and-adjust loop | ● | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ◐ |

* **CoolFlow's knowledge-capture and state mechanisms are under design discussion, not yet normative v0.1 features.** The current Golden Rule “Know the Actual State” expresses a human-facing principle, but CoolFlow does not yet define a canonical project status artifact or an Agent retrieval protocol. Knowledge capture has been discussed as cross-stage, but its trigger, storage and retrieval rules are not yet part of the published standard.

### What the comparison reveals

1. **CoolFlow's strongest distinction is its product-lifecycle framing.** It explicitly includes lightweight strategic DDD, concept validation, roadmap and UI prototyping before the implementation-heavy loops. BMAD also covers much of this territory, so CoolFlow should not claim to be the only full-lifecycle method.
2. **Implementation quality is a mature, crowded area.** Superpowers, Compound Engineering, GStack, PStack, Addy Skills, BMAD and GSD Core all provide substantial implementation, testing or review workflows. CoolFlow should reference proven solutions rather than reimplement every engineering practice.
3. **Knowledge capture and state continuity are different capabilities.** Compound Engineering, GStack and GSD Core provide concrete learning or memory mechanisms. PStack focuses more on turning repeated corrections into better Skills and structural enforcement. These should not be treated as interchangeable.
4. **A complete suite may overlap with CoolFlow's artifacts and lifecycle.** Spec Kit, OpenSpec, BMAD, GSD Core and Compound Engineering can each introduce their own planning files, lifecycle commands or state conventions. Adopting one wholesale requires an explicit integration decision.

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
