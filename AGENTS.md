# Instructions for Agents Developing CoolFlow

This repository publishes a **reference methodology and documentation standard**, not an orchestration engine.

## Goals and scope
- Preserve the **one Development Flow / three Adaptive Loops** model: Step 6 **Design Spec Loop**, Step 7 **Implementation Loop**, and a **cross-stage Evolution Loop** that may start at any step and revisit any relevant step as assumptions change. No fixed release/roadmap prerequisite. Documentation Sync is a post-acceptance step, not another Loop.
- Keep `standards/` the normative source of truth. Templates and optional Skills implement it; never invent conflicting requirements.
- Prefer short, explicit, Agent-readable Markdown. Avoid workflow-state machines, custom runtimes, agent-router protocols, and mandatory installations.
- A new project is initialized only when explicitly asked; initialization must never launch product discovery or start writing app code.
- The project-local `AGENTS.md` template must include a self-contained concise lifecycle overview and reference `docs/documentation.md` for documentation rules.

## Document lifecycle
- Durable truth: product, roadmap, domain, accepted feature specs.
- In-progress: discovery may use `docs/work/<objective>/` without a Spec; create unified `spec.md` in Design Spec Loop, with optional PRD, design, tasks and prototypes.
- Default to a **unified Spec**. A separate tasks file is not required when the coding Agent already tracks the plan in its session.
- Review the design before significant implementation; review code and Spec conformance afterward; update durable docs only after acceptance.

## External solution references
- `flowsolutions/` is a **non-normative, optional reference catalog**; `standards/` remains authoritative.
- Do not install, invoke, or combine external frameworks merely because they appear in the catalog.
- Prefer the smallest relevant component; treat a complete suite as an explicit workflow alternative when its artifacts, gates, or state model overlap with CoolFlow.
- Keep parent frameworks and their bundled Skills/playbooks distinct, and verify upstream compatibility before recommending installation.

## Validation
- During development, maintain internal cases under `reviews/scenarios/`; use an **independent reviewer Agent** with explicit evidence to check outcomes.
- Internal Scenario Review files must **not be included in the final release tree**.
- Never claim a test or Agent review passed unless it has actually run and evidence exists.

## Working on this repository
- Update the relevant standard first, then adjust templates, Skill instructions, and internal review cases.
- Preserve existing user files and project-local overrides in all examples.
- Keep docs and links coherent, and report limitations and untested cases clearly.
