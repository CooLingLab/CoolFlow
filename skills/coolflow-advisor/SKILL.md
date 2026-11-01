---
name: coolflow-advisor
description: Give opt-in, task-specific software engineering method, Skill and tool recommendations using CoolFlow's curated local references. Use when the user asks what method, concrete Skill, tool or workflow fits a named development task or CoolFlow stage. Do not infer the current stage or manage project progress.
---

# CoolFlow Advisor

A lightweight **on-demand engineering adviser**, not a lifecycle controller. Provide method advice, concrete Skill/tool choices, and proportionate workflows. Never automatically detect the user's stage, read project files to guess progress, install tools, change project documents, or start implementation.

## When invoked

1. Read `references/recommendations.md` for the stage-to-file index and selection principles. Do not load the full library upfront.
2. If the user names a CoolFlow stage, open **only** that stage's reference file. If they name a concrete task, choose the relevant reference file by the task rather than guessing project progress. If the task is ambiguous, ask one focused question or provide a conditional answer.
3. Apply the verification gate in `references/recommendations.md` before selecting any default recommendation. Only entries explicitly marked **核查通过** for the relevant source/version, capability, dependencies, and CoolFlow adaptation qualify; an A/B grade or L0–L3 estimate alone is not proof. Rank eligible entries by fit and user constraints; offer at most one alternative. If none qualifies, say so and suggest using the current Agent or a simple manual method without presenting an unverified library tool as a default.
4. Explain **what it solves, when to use it, limitations/dependencies, CoolFlow compatibility, and a suggested workflow**. Link to the specific upstream Skill whenever possible, rather than recommending an entire suite.
5. Distinguish `Skill`, `method`, `tool` and a bundled **suite-dependent component**. Never claim a Skill can be independently installed or run if it delegates to other Skills or requires suite scripts.
6. Remain technology-stack agnostic; assess compatibility with the user’s actual environment rather than imposing a framework. Preserve CoolFlow's project-local document conventions, human acceptance and separate release authorization. Lightweight modifications (such as changing paths and disabling mandatory downstream handoff) do not inherently reduce a Skill's recommendation priority.
7. Curated local references are the starting point, not immutable truth. If the user asks to explore candidates or needs current information, research authoritative sources when available. An unverified candidate may be discussed explicitly as a candidate with its missing checks, never as a default recommendation. Label new findings **not yet curated**; do not silently change a recorded status. Lack of hands-on testing is distinct from an incomplete verification; disclose actual test evidence without inventing it.
8. Stop at advice unless the user explicitly authorizes installation, editing or execution. Do not require any special subagent runtime. For substantial comparison research, an available subagent may help isolate context, but it is optional.

## Resource boundaries

- The installed Skill folder must include `SKILL.md` **and the entire `references/` directory**. These references are bundled locally and do not require a GitHub request for ordinary recommendations.
- If `references/` is missing, report an incomplete installation instead of inventing library entries.
- Do not duplicate or import all of `flowecosystem/catalog.md` into context: it is a broad optional catalog, not the curated library.
- Do not copy the recommendation library or this Skill into the user's application. Advisor does not participate in `coolflow-init`.
- Updates on GitHub do not change an installed global Skill until the user updates it.

## Response shape

Be concise in conversation, detailed only when the task warrants it:
- **Recommended approach and why**
- **Concrete Skill/tool** with direct source link and optional backup
- **Compatibility/dependencies** and any necessary light adaptation
- **Minimal next action**; do not execute unasked
