# CoolFlow

**English** | [简体中文](README.zh-CN.md)

**by Cooling · An AI Software Development SOP**

**A pilot's approach to AI-assisted software development.**

Created by **Cooling**, a pilot, CoolFlow is **inspired by the Airbus Golden Rules for Pilots** and aviation **Standard Operating Procedures (SOPs)**—especially their focus on priorities, situational awareness, and safety. These are Cooling's independent adaptations for **human-led, AI-assisted software development**, not Airbus-authored or Airbus-endorsed software guidance.

**One Development Flow · Three Adaptive Loops · A lightweight documentation standard.**

CoolFlow is an AI-oriented software development methodology for individual developers. It tells you **what to clarify, document, validate, and retain** across the product lifecycle. It is **not** an Agent harness, workflow engine, or mandatory skill collection.

> **Status: v0.1 development draft.** The `feat/v0.1-standard-and-init` branch is for review; it is not a release.

## CoolFlow Golden Rules

**The Four Golden Rules for AI-Assisted Software Development**  
*By Cooling · Creator of CoolFlow*

CoolFlow's four [Golden Rules](methodology/golden-rules.md) are **human-facing principles for AI-assisted software development**, not rules limited to people who adopt the CoolFlow framework. They help the developer retain engineering priorities, situational awareness, recoverability and independent judgment throughout the product lifecycle:

1. **Keep It Working → Ship Small → Improve** — protect verified behavior, deliver small valuable increments, then improve.
2. **Know the Actual State** — distinguish what is planned, executed, verified, accepted and released.
3. **Keep a Way Back** — maintain useful version checkpoints and realistic recovery options.
4. **Prove It Works** — confirm results with direct, reproducible evidence rather than an Agent's assertion.

These are **human-facing decision principles**, not four new mandatory Agent commands or workflow stages. Specific Agent execution instructions belong in the target project's `AGENTS.md`.

## The model

**Flow (recommended, adaptable)**

1. Idea → Brainstorm
2. Lightweight strategic DDD
3. Concept Prototype → Validation
4. Roadmap (MVP and later versions)
5. UI Prototype (for the current release)
6. Design Spec Loop (write a unified Spec, review when useful, revise)
7. Implementation Loop (code, test, code review, Spec conformance, fix)
8. Human Acceptance → Documentation Sync → Release

**Three Adaptive Loops**

- **Design Spec Loop (Step 6):** draft/clarify a unified Spec → review when useful → revise → re-review until implementation-ready. EGM is *optional*.
- **Implementation Loop (Step 7):** code → test → code review → Spec conformance → fix until acceptance criteria are met.
- **Evolution Loop (cross-stage):** new evidence or changed assumptions **at any step** → reconsider relevant decisions → re-enter **any step that needs revisiting**. It does **not** require a release, roadmap update, fixed starting point, or full restart.

A routine design revision or code/test fix belongs to its local quality Loop; use the Evolution Loop when new learning warrants reconsidering scope, assumptions, or product direction. **Documentation Sync follows Human Acceptance; it is a step, not a fourth Loop.**

Stages may be skipped, merged, reordered, or revisited. For a tiny fix, do not invent a PRD, diagram, or elaborate review merely to complete a template.

## Getting started

**Start here:** [Getting Started — from an idea to your first accepted increment](GETTING_STARTED.md). The guide provides copyable prompts for a **new project** and an **existing app**, plus the boundary between initialization, implementation, acceptance, and release.

CoolFlow requires **no installation, dashboard, orchestration engine, or specific AI agent**. Have your coding agent read the [Flow](methodology/flow.md), [Loops](methodology/loops.md), [documentation standard](standards/documentation.md), and [initialization contract](standards/initialization.md) before working in your **target application repository**.

The [`coolflow-init` Skill](skills/coolflow-init/SKILL.md) is optional and initializes documentation **only**. The Standard remains the authoritative source.

## Reusable document templates

When you apply CoolFlow to an App, this is the **project documentation structure you get**. It shows the target App's files—not the internal folders of the CoolFlow repository. Optional files are not created unless the project needs them.

\`\`\`text
<your-app>/
├── AGENTS.md                         # Project-local Agent instructions
├── README.md                         # Human-readable project entry
└── docs/
    ├── product.md                    # Product Brief: why, for whom and value; NOT a PRD
    ├── roadmap.md                    # MVP and future priorities
    ├── domain.md                     # Domain language, boundaries and rules
    ├── features/                     # Accepted, implemented behavior
    │   └── <feature>.md              # Added after acceptance
    ├── work/
    │   ├── <objective>/              # Created when actual work begins
    │   │   ├── spec.md               # Default unified Spec
    │   │   ├── prd.md                # Optional: substantial product requirements
    │   │   ├── design.md             # Optional: deeper technical design
    │   │   ├── tasks.md              # Optional: persistent task progress
    │   │   └── prototypes/           # Optional: working prototypes
    │   └── archive/                  # Selective evidence from completed work
    ├── lessons/                      # Optional: verified, reusable project lessons
    │   ├── README.md
    │   └── <lesson>.md
    ├── architecture.md               # Optional: current system architecture
    ├── adr/                          # Optional: durable architecture decisions
    └── feature-map.md                # Optional: UI navigation and verification
\`\`\`

### What gets created, and when?

| When | Files and folders |
|---|---|
| **Project initialization** | \`AGENTS.md\`, \`README.md\`, \`docs/product.md\`, \`roadmap.md\`, \`domain.md\`, plus empty \`features/\`, \`work/\` and \`work/archive/\` directories |
| **When development begins** | One \`docs/work/<objective>/spec.md\` as the default starting point |
| **Only when needed** | \`prd.md\`, \`design.md\`, \`tasks.md\`, \`prototypes/\`, \`architecture.md\`, \`adr/\`, \`feature-map.md\` |
| **When a verified reusable lesson emerges** | Optional \`docs/lessons/\`; do not create it just to have a knowledge folder |

**Product Brief is not PRD.** \`docs/product.md\` is the concise, long-lived definition of the whole product—problem, audience, vision, value and boundaries. An optional \`prd.md\` belongs to one substantial development objective and describes that increment's user needs, scope and product-level success criteria. The unified \`spec.md\` then defines precise behavior, implementation and verification.

**Where does experience go?** \`docs/lessons/\` stores evidence-backed lessons that should change future decisions or actions. Completed work and its evidence stay in \`docs/work/archive/\`; important architecture rationale belongs in \`docs/adr/\`; only stable, high-priority rules that Agents must always follow belong in \`AGENTS.md\`. A project may independently add a \`solutions/\` directory for reusable solution recipes, but CoolFlow does not require it. It is not the same as the optional \`lessons/\` directory.

The reusable source templates are organized by purpose:

- [Project skeleton](templates/project/) — initial \`AGENTS.md\`, \`README.md\` and core docs.
- [Work templates](templates/work/) — unified Spec, optional PRD, design and tasks.
- [Optional templates](templates/optional/) — feature map and reusable lesson templates.

The tree is a lightweight default, not a mandatory checklist. Existing projects can preserve their own structure and adopt only the parts that help.

## Repository structure

The tree below shows the document and template layout currently maintained by CoolFlow. The separate **application documentation tree** created in a target App repository is defined in the [documentation standard](standards/documentation.md#canonical-application-documentation-tree).

```text
CoolFlow/
├── README.md / README.zh-CN.md
├── GETTING_STARTED.md
├── AGENTS.md
│
├── methodology/                     # Development method
│   ├── flow.md
│   ├── loops.md
│   ├── golden-rules.md
│   └── golden-rules.zh-CN.md
│
├── standards/                       # Normative standards
│   ├── documentation.md
│   ├── initialization.md
│   └── reviews.md
│
├── templates/                       # Reusable document templates
│   ├── project/
│   │   ├── AGENTS.md
│   │   ├── README.md
│   │   └── docs/
│   │       ├── product.md
│   │       ├── roadmap.md
│   │       ├── domain.md
│   │       ├── features/.gitkeep
│   │       └── work/
│   │           ├── .gitkeep
│   │           └── archive/.gitkeep
│   ├── work/
│   │   ├── spec.md
│   │   ├── prd.md
│   │   ├── design.md
│   │   └── tasks.md
│   └── optional/
│       └── feature-map.md
│
├── skills/
│   └── coolflow-init/SKILL.md       # Optional initialization Skill
│
├── flowsolutions/                   # Optional external solution catalog
│   ├── README.md
│   ├── framework-comparison.md
│   └── catalog.md
│
└── reviews/
    └── scenarios/                  # Development-only review fixtures
```

- [methodology/](methodology/) defines the Flow, Loops and Golden Rules.
- [standards/](standards/) defines normative documentation, initialization and review conventions.
- [templates/](templates/) provides the starting files copied into an App repository or an active work objective.
- [flowsolutions/](flowsolutions/) is an optional catalog of external frameworks and methods. It is not copied into App projects.
- [reviews/scenarios/](reviews/scenarios/) contains **development-only** review fixtures and must be excluded from the final release tree.

The separate CoolFlow Dashboard may visualize stages and project documents; the dashboard does not schedule or execute Agents.

## Development vs release

`reviews/scenarios/` contains **internal development validation cases**. Keep it while designing and testing CoolFlow, but **exclude it from the final published release tree**. Removing files from a future commit does not remove them from Git history.

See [internal review guidelines](reviews/scenarios/README.md). No release has been made.

## References

- [EGM (Elephant-Goldfish Model)](https://github.com/google/elephant-goldfish-model) — independent review of technical design.
- [GitHub Spec Kit](https://github.com/github/spec-kit) — specification and implementation convergence.
- [OpenSpec](https://github.com/Fission-AI/OpenSpec) — working changes and accepted/current specs.
- [Agent Skills](https://agentskills.io/specification) — portable `SKILL.md` format.

CoolFlow draws on these ideas but does not require or bundle them.
