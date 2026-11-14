# CoolFlow

**English** | [简体中文](README.zh-CN.md)

**AI can write code. Building software takes more than code.**

CoolFlow is a lightweight engineering method for independent developers building with AI—from a rough idea to a working, verifiable product.

## Why CoolFlow?

AI makes writing code easier. It does not give us a framework for running a project. What actually gets in the way is rarely code:

- What should a project do first, and what can wait?
- How do product, domain, architecture and features connect?
- When is something good enough, what needs review, and what counts as accepted?
- What should this project leave behind for the next one?

CoolFlow does not hand you ready-made experience. It builds these questions into a flow and a set of documents, so you have a structure before you have the experience—and a place to keep the experience you gain.

## What CoolFlow provides

- **One Development Flow:** From idea discovery, prototypes and roadmap to implementation, human acceptance and release—with the questions each stage should answer and the output it should leave behind.
- **Three Adaptive Loops:** Improve designs through review, validate implementations through testing and code review, and adapt product direction as new information emerges.
- **Lightweight documentation:** Give goals, domain, architecture, key decisions and reusable engineering knowledge a stable home.

<p align="center">
  <img src="methodology/flow-diagram.en.svg" alt="CoolFlow development flow and feedback loops">
</p>

Skip, combine or revisit stages as needed. The flow is a guide, not a rigid checklist.

## Get started

Use CoolFlow with your preferred coding Agent; no specific Agent vendor or installation tool is required.

**New project — install CoolFlow Init**

Open your coding Agent and send:

```text
Please install this Skill globally using the standard installation method for your current Agent:
https://github.com/CooLingLab/CoolFlow/tree/main/skills/coolflow-init
```

After installation, open a **new, empty project directory** and ask:

> Use `coolflow-init` to initialize this empty project.

The Skill checks the target directory before writing and refuses any other files or folders, including hidden entries. It creates the CoolFlow project documentation, verifies the result, and stops without starting Brainstorm or writing application code.

If your Agent cannot install Skills, see the manual installation and optional installer methods in the [Getting Started guide](GETTING_STARTED.md).

**Existing project — inspect before adopting**

Do not use `coolflow-init` for an existing or non-empty project. Follow the inspect-first [Existing Project Adoption guide](GETTING_STARTED.md#b-existing-project--inspect-before-adopting): review the current project, propose a selective adoption plan, and wait for approval before changing files.

[Complete Getting Started guide](GETTING_STARTED.md) · A work directory may be opened during discovery; the formal Spec is written when the chosen work enters Design Spec Loop.

## CoolFlow Skills

CoolFlow includes four optional Agent Skills:

| Skill | Purpose | Why it matters | Use when |
| --- | --- | --- | --- |
| [`coolflow-init`](skills/coolflow-init/SKILL.md) | Create the CoolFlow documentation skeleton | Gives every new project the same CoolFlow starting point, not a one-off setup | Starting a new, empty project |
| [`coolflow-advisor`](skills/coolflow-advisor/SKILL.md) | Recommend methods, Skills and tools for a specific task | Keeps method and tool choices small, relevant and grounded in the current task | Choosing an approach for a development task |
| [`coolflow-docs-review`](skills/coolflow-docs-review/SKILL.md) | Check documentation against the project's local documentation standard | Finds structural drift and broken references without imposing CoolFlow's own conventions | Auditing or repairing documentation compliance |
| [`coolflow-skill-creator`](skills/coolflow-skill-creator/SKILL.md) | Create, adapt, test and maintain native CoolFlow Skills | Turns external ideas and repeated practice into a maintained personal Skill library—an asset that improves through real use and validation | Building or reviewing a Skill |

`coolflow-init` is the project setup entry point. The others are optional on-demand Skills. Install a Skill with your Agent's standard installation method; `coolflow-init` has an example above.

**What mature CoolFlow looks like:** Every project starts from the same clear, flexible flow; each iteration leaves durable documentation and evidence; and your Skill library becomes a personal arsenal of adapted, validated capabilities that make the next project faster and more reliable.

## Four Golden Rules

CoolFlow also offers four memorable principles for the **human developer**, inspired in part by the Airbus Golden Rules for Pilots. You can use them even without adopting the whole flow:

1. **Keep It Working → Ship Small → Improve** — protect what already works, deliver small increments, then improve.
2. **Know the Actual State** — distinguish planned, changed, tested, accepted and released.
3. **Keep a Way Back** — keep practical version checkpoints and recovery options.
4. **Prove It Works** — trust direct, reproducible evidence, not just an AI agent's claim.

These are decision principles, **not mandatory commands for AI agents**. Put concrete agent instructions in the target project's `AGENTS.md`.

[Read the Golden Rules](methodology/golden-rules.md)

## Why a pilot?

CoolFlow was started by Cooling, a pilot exploring AI-assisted software development. Aviation SOPs, situational awareness and cross-checks inspired its emphasis on priorities, actual state, recoverability and verification.

## Documentation guide

Every CoolFlow document is short and can be read on its own. Jump to what you need now:

| Document | What it covers |
| --- | --- |
| [Getting Started](GETTING_STARTED.md) | Initializing a new project, adopting CoolFlow in an existing one, and taking the first increment from discovery to release. |
| [Development Flow](methodology/flow.md) | The eight stages, the question each stage answers, and the result it should leave behind. |
| [Adaptive Loops](methodology/loops.md) | The three feedback cycles—design, implementation and evolution—and when each applies. |
| [Stage Activities](methodology/activities.md) | The concrete activities within each stage and the boundaries between them. |
| [Golden Rules](methodology/golden-rules.md) | Four human decision principles you can use even without the full flow. |
| [Documentation Standard](standards/documentation.md) | Where each project document lives, when it is created, and how it evolves. |
| [Initialization Contract](standards/initialization.md) | Exactly what `coolflow-init` checks, creates, and must leave alone. |
| [Review Practices](standards/reviews.md) | What design review and code review check—and what they do not replace. |
| [Templates](templates/) | The project documentation skeleton, work-document templates, and optional ADR/Solution examples. |

**Repository maintenance:** [AGENTS.md](AGENTS.md) explains how to develop this repository; [internal Scenario Reviews](flowreviews/scenarios/README.md) record how CoolFlow validates its own standards, templates and Skills. They are not application tests and are never copied into target projects.

## Ecosystem & Tool Selection

CoolFlow defines a development methodology and documentation standard; it does not bundle or require a particular Agent toolchain. The [ecosystem catalog](flowecosystem/README.md) helps you compare external approaches and choose the smallest useful complement:

- [Framework Comparison](flowecosystem/framework-comparison.md) — compare documented capabilities, workflow coverage, project state and knowledge capture across major AI development frameworks.
- [Solution Catalog](flowecosystem/catalog.md) — broad ecosystem research by development stage.
- [Engineering Practices](flowecosystem/engineering-practices.md) — optional practices for parallel work, review, release verification, permissions and decision records in AI-assisted development.
