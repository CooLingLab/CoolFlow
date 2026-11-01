# CoolFlow

**English** | [简体中文](README.zh-CN.md)

**AI can write code. Building software takes more than code.**

CoolFlow is a lightweight development roadmap for independent developers building with AI—from a rough idea to a working, verifiable product.

## Why CoolFlow?

AI makes writing code easier, but building a product still raises familiar questions:

- What should you build first?
- Is the AI changing code without a clear product direction?
- Does a feature actually work, or does it only look finished?

## What CoolFlow provides

- **One Development Flow:** From idea discovery, prototypes and roadmap to implementation, human acceptance and release.
- **Three Adaptive Loops:** Improve designs through review, validate implementations through testing and code review, and adapt product direction as new information emerges.
- **Lightweight documentation:** Keep goals, requirements, key decisions and reusable engineering knowledge.

<p align="center">
  <img src="methodology/flow-diagram.en.svg" alt="CoolFlow development flow and feedback loops">
</p>

Skip, combine or revisit stages as needed. The flow is a guide, not a rigid checklist.

## Get started

Use your current coding agent. Choose the right starting point:

**New project — initialize documentation**

> Read https://github.com/CooLingLab/CoolFlow/blob/main/GETTING_STARTED.md and its linked standards. In my new repository, create only missing CoolFlow documentation and folders. Preserve existing files; do not brainstorm, create a Spec or write code yet. Report what changed.

Initialization includes `docs/documentation.md`, a complete project-local standard for later documentation work without accessing CoolFlow. Existing files are preserved.

**Existing project — inspect before adopting**

> Read https://github.com/CooLingLab/CoolFlow/blob/main/GETTING_STARTED.md and inspect my existing repository. For **[feature or fix]**, suggest which CoolFlow steps would help and the smallest verifiable next action. Preserve existing conventions and propose a plan before changing anything.

[Complete Getting Started guide](GETTING_STARTED.md) · A work directory may be opened during discovery; the formal Spec is written when the chosen work enters Design Spec Loop.


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

## More documentation

- [Getting Started](GETTING_STARTED.md) — new and existing projects.
- [Development Flow](methodology/flow.md) · [Adaptive Loops](methodology/loops.md) — the method.
- [Documentation Standard](standards/documentation.md) · [Templates](templates/) — documentation conventions and reusable templates.

## Ecosystem & Tool Selection

CoolFlow defines a development methodology and documentation standard; it does not bundle or require a particular Agent toolchain. These references help you compare external approaches and choose the smallest useful complement:

- [Framework Comparison](flowecosystem/framework-comparison.md) — compare documented capabilities, workflow coverage, project state and knowledge capture across major AI development frameworks.
- [Solution Catalog](flowecosystem/catalog.md) — find external frameworks, Skills, methods and tools by CoolFlow stage and development need.
