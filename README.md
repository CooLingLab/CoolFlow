# CoolFlow

**English** | [简体中文](README.zh-CN.md)

## AI can write code. Building software takes more than code.

**A lightweight development roadmap for people building with AI.**

**Build with AI. Stay in control.**

From a rough idea to something people can actually use, CoolFlow helps you understand what to do next, when to design or validate, and which decisions are worth keeping. It is a practical reference for individual developers—not a claim to define the one correct way to build software.

> **Status: v0.1 development draft.** This branch is under review, not an official release. Real-project and end-to-end validation are still pending.

## Why CoolFlow?

AI has made writing code dramatically more accessible. You can describe a screen, build a feature, or fix a bug with a coding agent. But as projects grow, it's easy to run into a different kind of difficulty:

- You have plenty of ideas, but you're not sure what to build first.
- AI keeps changing the code while the product direction becomes less clear.
- A feature looks finished, but you can't tell whether it has actually been verified.
- After several iterations, important decisions and lessons become hard to recover.

**Knowing how to ask AI to write code is not the same as having a clear process for building a product.**

CoolFlow is an attempt to bridge that gap—especially for people starting with AI-assisted development, without getting in the way of developers who already have their own workflow.

## What does CoolFlow provide?

| | What it helps with |
| --- | --- |
| **One Development Flow** | Navigate from idea, domain understanding and prototypes to planning, implementation, human acceptance and release. |
| **Three Adaptive Loops** | Refine a Spec, verify implementation, and revisit product decisions whenever new evidence calls for it. |
| **Lightweight documentation** | Keep product goals, requirements, decisions and reusable engineering knowledge understandable to both you and your AI agent. |

<p align="center">
  <img src="docs/diagrams/coolflow-diagram.en.svg" alt="CoolFlow development flow and feedback loops">
</p>

**The flow is a map, not a checklist.** Skip, combine, reorder or revisit stages when that makes sense. A small bug fix doesn't need a PRD or a prototype; a complex new product may benefit from both discovery and validation before implementation.

[Explore the Development Flow](methodology/flow.md) · [Understand the three Loops](methodology/loops.md)

## Start using it

You don't need to install a new app, switch coding agents, adopt an orchestration engine, or use a dashboard. Start with the tool and repository you already have.

For a **new project**, use the [Getting Started guide](GETTING_STARTED.md) to initialize only the necessary documents, clarify the idea, and choose a first small, verifiable increment. For an **existing project**, apply only the parts that help with the next feature or fix—there is no need to start over.

**A first prompt to try:**

> Read the [CoolFlow v0.1 draft](https://github.com/CooLingLab/CoolFlow/tree/feat/v0.1-standard-and-init), especially its methodology, documentation standard, and Getting Started guide. Inspect my current project and help me clarify its actual state, goals, and next smallest verifiable step. Propose the plan before writing code. Preserve existing files and instructions; tell me if you cannot access the reference material.

The optional [`coolflow-init` Skill](skills/coolflow-init/SKILL.md) can create the documentation skeleton; **it does not implement an app**. The methodology and standards, not the Skill, are the source of truth.

## Four Golden Rules

CoolFlow also offers four memorable principles for the **human developer**. You can use them even without adopting the whole flow:

1. **Keep It Working → Ship Small → Improve** — protect what already works, deliver small increments, then improve.
2. **Know the Actual State** — distinguish planned, changed, tested, accepted and released.
3. **Keep a Way Back** — keep practical version checkpoints and recovery options.
4. **Prove It Works** — trust direct, reproducible evidence, not just an AI agent's claim.

These are decision principles, **not mandatory commands for AI agents**. Put concrete agent instructions in the target project's `AGENTS.md`.

[Read the Golden Rules](methodology/golden-rules.md)

## Why was this started by a pilot?

I'm Cooling, a pilot who enjoys building software with AI.

Aviation uses standard operating procedures, situational awareness, cross-checks and risk management to bring structure to complex work. While experimenting with AI-assisted development, I saw some useful parallels: know your priorities, understand the real state, keep a way back, and verify outcomes.

CoolFlow is **an independent adaptation of ideas inspired in part by aviation SOPs and the Airbus Golden Rules for Pilots**. It is **not** Airbus-authored or Airbus-endorsed software guidance, and it doesn't claim that aviation and software engineering work the same way.

The goal isn't to reinvent software engineering. It's to make useful practices easier to understand, apply, adapt and improve together.

## Dig deeper

- [Getting Started](GETTING_STARTED.md) — copyable prompts for new and existing projects, including human checkpoints.
- [Development Flow](methodology/flow.md) and [Adaptive Loops](methodology/loops.md) — the full method.
- [Documentation Standard](standards/documentation.md) and [Initialization Contract](standards/initialization.md) — what to document and when.
- [Project and work templates](templates/) — reusable, optional templates, including Spec, Solutions and ADR guidance.
- [Golden Rules](methodology/golden-rules.md) — the four human-facing principles.

Documentation is a lightweight default, not an obligation to produce every file. An existing repository can retain its own conventions. This project is **not** an agent harness, a workflow engine, or a mandatory Skills collection.

### Related ideas

CoolFlow has learned from [EGM](https://github.com/google/elephant-goldfish-model), [GitHub Spec Kit](https://github.com/github/spec-kit), [OpenSpec](https://github.com/Fission-AI/OpenSpec), and the [Agent Skills specification](https://agentskills.io/specification). None is required to use CoolFlow.

---

*CoolFlow by Cooling · An independent, evolving approach to human-led, AI-assisted software development.*
