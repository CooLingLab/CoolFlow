# Instructions for Agents Developing CoolFlow

This repository publishes a **reference methodology and documentation standard**, not an orchestration engine.

## Goals and scope
- Preserve the one-Flow/three-Loops model in `methodology/`.
- Keep `standards/` the normative source of truth. Templates and optional Skills implement it; never invent conflicting requirements.
- Prefer short, explicit, Agent-readable Markdown. Avoid workflow-state machines, custom runtimes, agent-router protocols, and mandatory installations.
- A new project is initialized only when explicitly asked; initialization must never launch product discovery or start writing app code.
- The project-local `AGENTS.md` template must include a self-contained concise overview of lifecycle and documentation rules.

## Document lifecycle
- Durable truth: product, roadmap, domain, accepted feature specs.
- In-progress: `docs/work/<objective>/spec.md` with optional PRD, design, tasks, prototypes.
- Default to a **unified Spec**. A separate tasks file is not required when the coding Agent already tracks the plan in its session.
- Review the design before significant implementation; review code and Spec conformance afterward; update durable docs only after acceptance.

## Validation
- During development, maintain internal cases under `reviews/scenarios/`; use an **independent reviewer Agent** with explicit evidence to check outcomes.
- Internal Scenario Review files must **not be included in the final release tree**.
- Never claim a test or Agent review passed unless it has actually run and evidence exists.

## Working on this repository
- Update the relevant standard first, then adjust templates, Skill instructions, and internal review cases.
- Preserve existing user files and project-local overrides in all examples.
- Keep docs and links coherent, and report limitations and untested cases clearly.
