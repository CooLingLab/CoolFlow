# Solution Catalog

**Research snapshot: 2026-11-01**

This catalog maps external solutions to CoolFlow's Development Flow and Loops. It includes complete workflow suites, individual Skills, methods and specialist tools. It is a discovery guide, not a list of mandatory dependencies.

For a side-by-side capability comparison, see [Framework Comparison](framework-comparison.md).

## How to choose

### Integration modes

| Label | Meaning | Recommended use |
|---|---|---|
| **Direct use** | A focused Skill or method can be used without adopting another full workflow | Use it for one activity inside CoolFlow |
| **Selective adoption** | Borrow a component from a larger suite | Use the component, but keep CoolFlow's document ownership and human checkpoints |
| **Workflow alternative** | The project provides its own end-to-end or phase-based workflow | Choose it deliberately instead of running two competing workflows in parallel |
| **Stack-specific** | The solution depends on a particular language, framework or platform | Show it only when the target project's stack matches |

**Do not install everything.** If a direct Agent instruction or existing tool is sufficient, no extra Skill or framework is required.

### Project families

- **Full workflow suites:** Compound Engineering, Superpowers, GStack, PStack, BMAD Method and GSD Core.
- **Lifecycle Skills collection:** Addy Osmani Agent Skills.
- **Specification / change-management systems:** GitHub Spec Kit and OpenSpec.
- **Focused methods and Skills:** EGM, DDD Crew methods and Matt Pocock's Skills.

A Skill inside a suite is a component of that suite. The catalog names both the parent and the component so users do not mistake a bundled Skill for a separate framework.

## Recommendations by CoolFlow stage

### 1. Idea → Brainstorm

| Solution | Type | What it is useful for | Integration |
|---|---|---|---|
| [Grill Me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) — from [Matt Pocock's Skills](https://github.com/mattpocock/skills) | Focused Skill | One-question-at-a-time interrogation to expose assumptions and sharpen a plan or design. The `grill-me` entry delegates to the underlying `grilling` Skill. | Direct use |
| [Superpowers: brainstorming](https://github.com/obra/superpowers/tree/main/skills/brainstorming) | Skill in a full methodology | Socratic exploration, design alternatives and an agreed design before implementation planning. | Selective adoption / workflow alternative |
| [Compound Engineering: ce-brainstorm](https://github.com/EveryInc/compound-engineering-plugin) | Skill in a full suite | Produces a requirements-focused brainstorm artifact that can be enriched by `ce-plan`. | Selective adoption |
| [GStack: office-hours](https://github.com/garrytan/gstack) | Skill in a full suite | Challenges product framing and creates a design document consumed by downstream reviews. | Selective adoption |
| [Addy Agent Skills: interview-me](https://github.com/addyosmani/agent-skills) | Skill in a lifecycle pack | Structured requirements interview; useful when the problem is underspecified. | Direct use / selective adoption |
| [BMAD: brainstorming and product brief](https://github.com/bmad-code-org/BMAD-METHOD) | Workflow suite | Facilitated ideation and product framing with specialized product workflows. | Workflow alternative / selective adoption |
| [PStack: in-your-own-words / sharpen](https://github.com/cursor/plugins/tree/main/pstack) | Focused Skills in a plugin | Clarifies the user's goal or deepens a prompt; useful before a larger engineering task, but not a substitute for product discovery. | Direct use |

**Selection guidance:** use Grill Me for a focused interview; use Superpowers or Compound when you want a more structured design/requirements artifact; use GStack or BMAD when you want a broader product perspective.

### 2. Lightweight Strategic DDD

| Solution | Type | What it is useful for | Integration |
|---|---|---|---|
| [DDD Crew: Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process) | Modeling method | A guided path into domain discovery, ubiquitous language and strategic modeling. | Direct use / conditional |
| [DDD Crew: Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas) | Modeling template | Describes the purpose, responsibilities, relationships and boundaries of a Bounded Context. | Direct use / conditional |
| [DDD Crew: Context Mapping](https://github.com/ddd-crew/context-mapping) | Modeling method | Makes relationships and integration patterns between bounded contexts explicit. | Conditional |
| [PStack: principle-model-the-domain](https://github.com/cursor/plugins/tree/main/pstack) | Engineering principle Skill | Reminds the Agent to model the domain rather than prematurely shape code around implementation details. | Selective adoption |
| [BMAD: domain research](https://github.com/bmad-code-org/BMAD-METHOD) | Workflow component | Researches a domain and helps establish useful project context. | Selective adoption |

**Selection guidance:** do not force full DDD onto a small CRUD application. Start with shared vocabulary, important entities, invariants and boundaries. Add EventStorming, Context Mapping or canvases only when domain complexity justifies them.

### 3. Concept Prototype → Validation

| Solution | Type | What it is useful for | Integration |
|---|---|---|---|
| [Compound Engineering: ce-prototype](https://github.com/EveryInc/compound-engineering-plugin) | Skill in a full suite | Creates a low-cost prototype to answer a product, interaction or feasibility question. | Selective adoption |
| [PStack: prototype playbook](https://github.com/cursor/plugins/tree/main/pstack) | Playbook in a plugin | Builds a throwaway sketch to settle a design or behavioral decision empirically. | Direct use / selective adoption |
| [BMAD prototyping guidance and UX](https://github.com/bmad-code-org/BMAD-METHOD) | Workflow guidance / Skill | Encourages prototypes as a learning tool; UX workflows can create HTML mocks and wireframes. | Selective adoption |
| [GStack: design-shotgun / design-html](https://github.com/garrytan/gstack) | Design Skills in a full suite | Generates and iterates visual alternatives, then turns an approved direction into a working HTML artifact. | Selective adoption |

**Selection guidance:** state the hypothesis first. A prototype is successful when it answers the question, including when it disproves the idea. Decide explicitly whether to discard it or promote it into the real product.

### 4. Roadmap

| Solution | Type | What it is useful for | Integration |
|---|---|---|---|
| [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) | Full workflow suite | Product briefs, requirements and planning from prototype through larger initiatives. | Workflow alternative / selective adoption |
| [GSD Core](https://github.com/open-gsd/gsd-core) | Full workflow suite | Milestone and phase planning with explicit progress tracking and execution plans. | Workflow alternative |
| [GStack: plan-ceo-review / plan-eng-review](https://github.com/garrytan/gstack) | Review Skills in a full suite | Challenges product scope and engineering sequencing before a plan is executed. | Selective adoption |
| [Compound Engineering: ce-strategy / ce-plan](https://github.com/EveryInc/compound-engineering-plugin) | Skills in a full suite | Captures product direction and turns a selected increment into implementation guardrails. `ce-strategy` is not itself a dated roadmap. | Selective adoption |

**Selection guidance:** distinguish strategy (why and where to go), roadmap (which increments and when), and a task-level implementation plan. They are related but not interchangeable.

### 5. UI Prototype

| Solution | Type | What it is useful for | Integration |
|---|---|---|---|
| [GStack: design-consultation / design-shotgun / design-html](https://github.com/garrytan/gstack) | Design Skills in a full suite | Explores visual directions, creates a design system and produces working HTML prototypes. | Selective adoption |
| [BMAD: bmad-ux](https://github.com/bmad-code-org/BMAD-METHOD) | UX workflow | Produces UX direction, key-screen concepts, wireframes and HTML mocks. | Selective adoption |
| [PStack: prototype playbook](https://github.com/cursor/plugins/tree/main/pstack) | Playbook | Quickly tests a visual or behavioral idea; not a complete design-system workflow. | Direct use |
| [Compound Engineering: ce-prototype](https://github.com/EveryInc/compound-engineering-plugin) | Skill | Prototypes a specific interaction or concept to reduce uncertainty. | Direct use / selective adoption |

**Selection guidance:** use a UI-specific workflow when interaction, visual hierarchy or navigation is central. A low-fidelity HTML prototype is often enough; high fidelity should be justified by the question being tested.

### 6. Design Spec Loop

| Solution | Type | What it is useful for | Integration |
|---|---|---|---|
| [Google EGM](https://github.com/google/elephant-goldfish-model) | Design-review method / Skills | Independent adversarial review of a technical design before significant implementation. | Direct use |
| [Compound Engineering: ce-plan / ce-doc-review](https://github.com/EveryInc/compound-engineering-plugin) | Planning and review Skills | Enriches a requirements artifact into implementation guardrails and challenges plan quality. | Selective adoption |
| [Superpowers: writing-plans / subagent-driven-development](https://github.com/obra/superpowers) | Skills in a full methodology | Produces executable plans and uses fresh subagents plus review loops for implementation units. | Selective adoption / workflow alternative |
| [GStack: spec / plan-eng-review / autoplan](https://github.com/garrytan/gstack) | Skills in a full suite | Creates a precise spec and runs product/design/engineering plan reviews. | Selective adoption |
| [PStack: architect / interrogate / arena](https://github.com/cursor/plugins/tree/main/pstack) | Skills in a plugin | Settles module boundaries, challenges assumptions and explores parallel design options. | Selective adoption |
| [Addy Agent Skills: spec / plan / doubt-driven-development](https://github.com/addyosmani/agent-skills) | Lifecycle Skills | Writes a PRD/spec, creates atomic implementation plans and applies adversarial review to important decisions. | Direct use / selective adoption |
| [BMAD: PRD / architecture / review workflows](https://github.com/bmad-code-org/BMAD-METHOD) | Full workflow suite | Structured product requirements, architecture and specialist review. | Workflow alternative / selective adoption |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Spec-driven toolkit | Constitution, specify, plan, tasks and customizable workflows. | Workflow alternative / selective adoption |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | Change-oriented spec workflow | Proposal, requirements, design, tasks, verification and archive for individual changes. | Workflow alternative / selective adoption |

**Selection guidance:** EGM reviews the design expressed in the Spec; code review belongs in Step 7. Spec Kit and OpenSpec can overlap with CoolFlow's document structure, so decide which system owns the canonical Spec and change lifecycle before combining them.

### 7. Implementation Loop

| Solution | Type | What it is useful for | Integration |
|---|---|---|---|
| [Superpowers: test-driven-development / systematic-debugging / subagent-driven-development](https://github.com/obra/superpowers) | Skills in a full methodology | Red-Green-Refactor, evidence-led debugging and task-scoped implementation/review. | Selective adoption / workflow alternative |
| [Compound Engineering: ce-work / ce-simplify-code / ce-code-review](https://github.com/EveryInc/compound-engineering-plugin) | Skills in a full suite | Executes a plan, simplifies the result and reviews the implementation against the plan. | Selective adoption |
| [GStack: verify / review / qa / cso / ship](https://github.com/garrytan/gstack) | Engineering-team Skills | Runs repo checks, reviews code, exercises the app, performs security checks and ships verified changes. | Selective adoption / workflow alternative |
| [PStack: poteto-mode playbooks and tdd](https://github.com/cursor/plugins/tree/main/pstack) | Playbook router and Skills | Routes feature, bug-fix, refactor, performance and verification work through rigorous playbooks and model delegation. | Selective adoption / workflow alternative |
| [Addy Agent Skills: test-driven-development / code-review-and-quality](https://github.com/addyosmani/agent-skills) | Lifecycle Skills | Applies TDD, verification and structured code review. | Direct use / selective adoption |
| [BMAD: build / test / review](https://github.com/bmad-code-org/BMAD-METHOD) | Workflow suite | Executes planned work with specialized development and testing workflows. | Workflow alternative |
| [GSD Core: execute-phase / verify-work](https://github.com/open-gsd/gsd-core) | Workflow suite | Executes plans in context-isolated waves and verifies phase outcomes. | Workflow alternative |

**Selection guidance:** keep CoolFlow's Implementation Loop as the quality model. Adopt a proven TDD, debugging or code-review Skill rather than copying another framework's entire task orchestration unless you intentionally choose that framework.

### 8. Human Acceptance → Documentation Sync → Release

| Solution | Type | What it is useful for | Integration |
|---|---|---|---|
| [GStack: document-release / document-generate / land-and-deploy / canary](https://github.com/garrytan/gstack) | Release and documentation Skills | Audits documentation against shipped behavior, generates missing docs, deploys and checks production health. | Selective adoption |
| [Addy Agent Skills: review / ship](https://github.com/addyosmani/agent-skills) | Lifecycle Skills | Quality gates and a structured path to production release. | Direct use / selective adoption |
| [BMAD: retrospective and UAT workflows](https://github.com/bmad-code-org/BMAD-METHOD) | Workflow components | Evidence-based acceptance and review of completed work, with follow-up action items. | Selective adoption |
| [GSD Core: verify-work / complete-phase / complete-milestone](https://github.com/open-gsd/gsd-core) | Workflow suite | Verifies phase outcomes, reconciles completion artifacts and closes milestones. | Workflow alternative |

**Selection guidance:** a passing test suite is not human acceptance. The developer should inspect actual behavior and decide whether the increment is accepted. Release should remain a separate decision where appropriate.

## Cross-cutting capabilities

These capabilities are not owned by one CoolFlow stage.

### Knowledge capture and reuse

| Solution | Mechanism | What is actually captured |
|---|---|---|
| [Compound Engineering: ce-compound](https://github.com/EveryInc/compound-engineering-plugin/blob/main/docs/guides/ce-compound.md) | Writes structured learnings to `docs/solutions/`; planning Skills search them later | Symptoms, root cause, failed approaches, working solution and prevention; only when knowledge is non-obvious, durable and material |
| [GStack: /learn and GBrain](https://github.com/garrytan/gstack) | Searchable persistent knowledge, optionally shared across machines | Project patterns, pitfalls, preferences, learned context and code knowledge |
| [GSD Core: extract-learnings](https://github.com/open-gsd/gsd-core/blob/next/docs/features/extract-learnings.md) | Extracts decisions, lessons, patterns and surprises from completed phase artifacts | Source-attributed learnings; optional global store and planner injection |
| [PStack: /reflect /correct /recall](https://github.com/cursor/plugins/tree/main/pstack) | Mines session history, routes repeated mistakes to structural fixes, or turns durable recipes into Skill edits | Agent behavior improvements and reusable playbooks, rather than a general project solution-document corpus |
| [BMAD: retrospective](https://github.com/bmad-code-org/BMAD-METHOD) | Evidence-based epic retrospective | Aggregate defects, lessons and owned process-improvement actions |

**Important distinction:** a solution document, a persistent Agent memory, a project decision record and a reusable Skill are different artifacts. See [Framework Comparison](framework-comparison.md) and the CoolFlow design discussion before choosing a canonical knowledge model.

### Project-state awareness

Project-state awareness means the Agent can recover the project's current position, progress and likely next action from durable, explicit project artifacts. It is not the same as remembering a conversation or saving a solution.

| Solution | Mechanism | What to understand |
|---|---|---|
| [GSD Core: STATE.md and state.json](https://github.com/open-gsd/gsd-core/blob/next/docs/reference/state-md.md) | Reads STATE.md at workflow start; updates it after significant actions; validates/syncs against project artifacts; publishes versioned state.json for external readers | The clearest explicit project-state implementation in this comparison. The JSON is a derived read contract for dashboards, not a second source of truth. |
| [GStack](https://github.com/garrytan/gstack/blob/main/docs/state-root.md) | Persistent per-project buckets for checkpoints, learnings and timeline; structured on-disk state for unattended autoplan runs | More than chat memory, but state is distributed across project/run artifacts rather than one compact lifecycle digest equivalent to GSD STATE.md. |
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | Plans, work-unit execution state and dedicated handoff workflow | Useful scoped work state; does not prescribe one universal project-wide status digest. |
| [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) | Durable product, architecture and workflow artifacts | Supports artifact-based continuity, but the reviewed sources do not show a single canonical project-state digest with GSD's read/update/validate contract. |
| [Superpowers](https://github.com/obra/superpowers) | Design documents, implementation plans and task checklists | Useful task-level progress context, not a dedicated project-wide state model. |

GSD's implementation is worth studying even if CoolFlow never adopts it: [STATE.md schema](https://github.com/open-gsd/gsd-core/blob/next/docs/reference/state-md.md), [consistency gates](https://github.com/open-gsd/gsd-core/blob/next/docs/features/statemd-consistency-gates.md), and [machine-readable state contract](https://github.com/open-gsd/gsd-core/blob/next/docs/features/machine-readable-state-contract-planningstatejson.md).

### Session handoff and resume

| Solution | Mechanism | Main trade-off |
|---|---|---|
| [Compound Engineering: ce-handoff](https://github.com/EveryInc/compound-engineering-plugin/blob/main/docs/guides/ce-handoff.md) | Dedicated create/resume Skill for handing work between sessions | Explicit handoff contract, scoped to continuing a unit of work rather than defining all project state |
| [GStack](https://github.com/garrytan/gstack) | Project checkpoints, CEO/design handoffs and context-restore workflows | Persistent cross-session context with a separate local state store |
| [PStack: pause safely](https://github.com/cursor/plugins/blob/main/harness/pstack/claude-code/skills/poteto-mode/playbooks/pause-safely.md) | Writes a cold-start resume note with intent, progress, verification, current state, next steps and key files | Strong explicit pause discipline; not a project-wide lifecycle state file |
| [GSD Core: pause-work / resume-work](https://github.com/open-gsd/gsd-core/blob/next/gsd-core/workflows/pause-work.md) | Separate HANDOFF.json and .continue-here.md alongside STATE.md | Separates the project's current state from the details of an interrupted session |
| [BMAD: brainstorming resume](https://github.com/bmad-code-org/BMAD-METHOD/tree/main/skills/bmad-brainstorming/references) | Workflow-specific resume guidance | Useful within that workflow; not a universal project handoff contract |

**Do not conflate the three:** project-state awareness answers “where is the project now?”; session handoff answers “where did this work stop, and how can it safely continue?”; knowledge capture answers “what reusable lesson should future work retrieve?”

### Skill quality and routing

| Solution | Mechanism | Value |
|---|---|---|
| [Addy Agent Skills](https://github.com/addyosmani/agent-skills) | Meta-skill routing plus trigger, routing and behavioral evaluations | Tests whether Skills are discoverable and behave as intended |
| [Superpowers](https://github.com/obra/superpowers) | Skill-writing workflow and pressure testing | Treats Skills as executable workflows that should be tested, not just prompt prose |
| [PStack](https://github.com/cursor/plugins/tree/main/pstack) | Poteto Mode playbook routing and an eval playbook | Routes tasks to focused procedures and tests changes to agent behavior |

## Compatibility cautions

1. **Do not run multiple full orchestration suites by default.** They may disagree on plan files, task state, review gates, worktree usage or completion semantics.
2. **Keep one source of truth for each artifact.** If Spec Kit or OpenSpec owns a change's spec, CoolFlow should link to it rather than create a competing second spec.
3. **Keep product decisions human-owned.** A framework's CEO, product-owner or reviewer persona can recommend; it does not replace the developer's decision.
4. **Use stack-specific Skills only when the project stack matches.** For example, Expo-specific Skills belong in a technology-specific extension, not in the universal catalog.
5. **Verify current compatibility before installation.** Host support, commands, versions and installation instructions can change.

This catalog is maintained as an optional companion to CoolFlow. It does not change the core Flow, Loops or documentation standard.
