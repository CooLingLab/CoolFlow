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
- **Three Adaptive Loops:** Refine a Spec, verify code, and revisit decisions when new evidence emerges.
- **Lightweight documentation:** Keep goals, requirements, key decisions and reusable engineering knowledge.

<p align="center">
  <img src="docs/diagrams/coolflow-diagram.en.svg" alt="CoolFlow development flow and feedback loops">
</p>

Skip, combine or revisit stages as needed. The flow is a guide, not a rigid checklist.

## Get started

Keep your current coding agent. Paste this into your AI coding tool:

> Read https://github.com/CooLingLab/CoolFlow/blob/main/GETTING_STARTED.md and the CoolFlow methodology and documentation standards it references. Inspect the actual state of my project, clarify the goal and smallest verifiable next step, and propose a plan first. Do not overwrite existing files or start coding yet. Tell me if you cannot access the documentation.

The [Getting Started guide](GETTING_STARTED.md) covers both new and existing projects.

## Four Golden Rules

CoolFlow also offers four memorable principles for the **human developer**. You can use them even without adopting the whole flow:

1. **Keep It Working → Ship Small → Improve** — protect what already works, deliver small increments, then improve.
2. **Know the Actual State** — distinguish planned, changed, tested, accepted and released.
3. **Keep a Way Back** — keep practical version checkpoints and recovery options.
4. **Prove It Works** — trust direct, reproducible evidence, not just an AI agent's claim.

These are decision principles, **not mandatory commands for AI agents**. Put concrete agent instructions in the target project's `AGENTS.md`.

[Read the Golden Rules](methodology/golden-rules.md)

## Why a pilot?

CoolFlow was started by Cooling, a pilot exploring AI-assisted software development. Aviation SOPs, situational awareness and cross-checks inspired its emphasis on priorities, actual state, recoverability and verification. The approach draws in part on the Airbus Golden Rules for Pilots, but it is **independent and neither authored nor endorsed by Airbus**.

## More documentation

- [Getting Started](GETTING_STARTED.md) — new and existing projects.
- [Development Flow](methodology/flow.md) · [Adaptive Loops](methodology/loops.md) — the method.
- [Documentation Standard](standards/documentation.md) · [Templates](templates/) — documentation conventions and reusable templates.
