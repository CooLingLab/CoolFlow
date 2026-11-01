# Getting Started with CoolFlow

**CoolFlow by Cooling · An AI Software Development SOP**

[Home](README.md) · [简体中文](README.zh-CN.md) · [Golden Rules](methodology/golden-rules.md)

CoolFlow is a lightweight **development methodology and documentation standard**, not an Agent runner. Use it with your existing coding Agent. You don't have to install a Skill, use a Dashboard, or learn a new command-line tool.

> **v0.1 draft:** The instructions below describe the intended workflow. End-to-end scenario execution and real project validation are **not yet completed**.

## Prerequisites

You need a **target application repository** (new or existing) that your coding Agent can inspect. This is separate from the CoolFlow reference repository.

The Agent should read the [Development Flow](methodology/flow.md), [Loops](methodology/loops.md), [documentation standard](standards/documentation.md), and [initialization contract](standards/initialization.md) as relevant. Templates are in [templates/project/](templates/project/). If it cannot read the canonical sources, provide a local copy or paste them; **do not let it guess the rules**.

## Choose your starting point

### A. New project — initialize documentation first

In your **new target repository**, paste this into the coding Agent:

> Read CoolFlow from https://github.com/CooLingLab/CoolFlow/tree/main, especially `standards/initialization.md`, `standards/documentation.md`, `methodology/flow.md`, `methodology/loops.md` and `templates/project/`. Inspect my **target repository** and initialize only the missing documentation and folders. Preserve existing files and instructions. **Do not** brainstorm product requirements, write app code, install dependencies, define MVP scope, or create `docs/work/001-mvp/` or `spec.md`. Report what was created, what already existed and what remains unverified. If the reference files are inaccessible, stop and tell me.

Expected skeleton in an **empty project**:

```text
AGENTS.md
README.md
docs/
  product.md  # concise project-level Product Brief, not a PRD
  roadmap.md
  domain.md
  features/
  work/
    archive/
```

Empty directories may use `.gitkeep` for Git tracking. Initialization must preserve existing content and be idempotent. The optional [`coolflow-init` Skill](skills/coolflow-init/SKILL.md) supports **only** this documentation setup.

### B. Existing project — inspect before adopting

Do **not** automatically reinitialize a mature app or overwrite its conventions. Start by pasting:

> Read https://github.com/CooLingLab/CoolFlow/tree/main and inspect my existing repository, including its `AGENTS.md`, code and relevant documentation. Explain its actual state and which parts of CoolFlow would help with **[specific fix or feature]**. Propose the smallest useful, verifiable next step and any non-destructive documentation changes. **Do not** overwrite files or implement the change until we agree on the plan. Skip unrelated stages and tell me if you cannot read the references.

After reviewing the plan, continue at the **relevant stage** below. Adopting CoolFlow does not require rebuilding the project's documentation tree or restarting from Idea.

## Continue a new project — discovery

After **new-project initialization**, explicitly start discovery when you are ready:

> I want to build **[product idea]** for **[users]** to solve **[problem]**. Using CoolFlow, help me clarify the goal, important domain concepts, critical assumptions, and a tentative MVP roadmap. Open `docs/work/001-mvp/` **if it helps record discovery**, but do not assume the MVP scope is settled or create a formal `spec.md` just for brainstorming. Record unknown decisions honestly and use a concept prototype only if it helps validate a risky assumption. **Do not start implementing yet**.

The Agent can update `docs/product.md` (the project-level Product Brief), `docs/domain.md`, `docs/roadmap.md`, and discovery notes. **A work directory may exist without a Spec until a specific objective enters Design Spec Loop (Step 6).** A substantial objective may use its own optional `docs/work/<objective>/prd.md`; do not confuse that with the project brief. Verified, non-obvious, durable and material engineering experience may later be distilled into optional `docs/solutions/`; raw work history stays with the work item or archive. Record a separate ADR in optional `docs/adr/` only when a consequential architecture or technical decision needs its rationale preserved. Stages may be **skipped or merged** when they add no value.

## Design and implement a selected increment

Before specifying related work, consult only relevant existing records in `docs/solutions/` if that optional directory exists. Do not read the entire knowledge store by default. Capture a new Solution only after a finding is verified and only when it is non-obvious, durable and material.

When a concrete increment has been selected for **Design Spec Loop (Step 6)**, paste:

> For **[selected feature/increment]**, write one unified `docs/work/<objective>/spec.md` with goals and non-goals, observable acceptance criteria, main design choices, implementation strategy, and verification plan. Review the **current Spec draft and relevant context** independently when warranted by complexity or risk; resolve material findings and confirm that the design is ready to implement. Then implement the **smallest complete valuable increment**. Run relevant tests, review the actual changed code, check conformance with the approved Spec, and address failures. If the Spec proves wrong, explicitly revisit the design instead of silently changing requirements. Show direct evidence of what works and identify what remains unverified. **Ask me to accept the result; don't mark it accepted yourself.**

The **Design Spec Loop** evaluates the plan; the **Implementation Loop** verifies the code and behavior. A separate `tasks.md` is optional. Compiling successfully is not, by itself, proof of a working feature.

## Human acceptance, documentation sync, and release

Inspect actual behavior and evidence. If satisfied, explicitly accept the increment:

> I have inspected **[specific functionality/evidence]** and **[accept / request changes]**. If accepted, update only the relevant durable documentation (`docs/features/` for accepted, implemented behavior) and selectively archive important decision and verification evidence. **Distinguish accepted from released.** Do not deploy or publish without a separate explicit instruction.

Release happens only when appropriate. The **Evolution Loop** is available **at any step**, not only after release: feedback, new ideas, or changing needs that warrant reconsidering product assumptions, scope, or direction can send the project back to any relevant step (for example, a failed prototype back to Brainstorm). Ordinary Spec revisions or code/test fixes stay within the local Design Spec or Implementation Loop. Revisit only what needs reconsideration.

## Human checkpoints

| Moment | What to confirm |
| --- | --- |
| Initialization | Only missing docs were added; existing material is intact |
| Before coding | Goal, constraints, and observable acceptance criteria are understood |
| After coding | Real changes and verification evidence support the claimed result |
| Before acceptance | Limitations, data risks, and a recovery option are understood |
| Before release | Accepted behavior is documented; release is separately authorized |

See the [CoolFlow Golden Rules](methodology/golden-rules.md) for the human-facing principles. **No mandatory global status file, Skill suite, or Agent orchestration system is introduced by this guide.**
