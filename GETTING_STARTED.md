# Getting Started with CoolFlow

**CoolFlow by Cooling · An AI Software Development SOP**

[Home](README.md) · [简体中文](README.zh-CN.md) · [Golden Rules](methodology/golden-rules.md)

CoolFlow is a lightweight **development methodology and documentation standard**, not an Agent runner. Use it with your existing coding Agent. You don't have to install a Skill, use a Dashboard, or learn a new command-line tool.

> **v0.1 draft:** The instructions below describe the intended workflow. End-to-end scenario execution and real project validation are **not yet completed**.

## Prerequisites

You need a **target application repository** (empty or existing) that your coding Agent can inspect and edit. This is separate from the CoolFlow reference repository.

Before beginning, have the Agent read the [Development Flow](methodology/flow.md), [Loops](methodology/loops.md), [documentation standard](standards/documentation.md), and [initialization contract](standards/initialization.md). Templates are in [templates/project/](templates/project/). If it cannot access the canonical sources, provide a local copy or paste them; **do not let it guess the rules**.

## 1. Initialize the project (documentation only)

In the **target project's** coding-agent conversation, paste:

> Read the CoolFlow v0.1 draft at https://github.com/CooLingLab/CoolFlow/tree/feat/v0.1-standard-and-init, especially `standards/initialization.md`, `standards/documentation.md`, `methodology/flow.md`, `methodology/loops.md`, and `templates/project/`. Inspect my **current target repository**. Create only missing CoolFlow documentation and folders; preserve all existing files and project-specific instructions. **Do not** write application code, install dependencies, define MVP scope, or create `docs/work/001-mvp/`. Report what was created, what already existed, and any unverified results. If you cannot read the reference files, stop and tell me.

Expected skeleton in an **empty project**:

```text
AGENTS.md
README.md
docs/
  product.md
  roadmap.md
  domain.md
  features/
  work/
    archive/
```

Empty directories may use `.gitkeep` for Git tracking. For existing repositories, the Agent must **not** overwrite files; it should report incompatibilities and only add missing pieces. Repeating initialization should leave existing content unchanged.

The optional [`coolflow-init` Skill](skills/coolflow-init/SKILL.md) supports this step, but is not required.

## 2. Start actual discovery (separate instruction)

After initialization, describe the product you want and explicitly start work:

> I want to build **[product idea]** for **[users]** to solve **[problem]**. Using CoolFlow, help me clarify the goal, important domain concepts, critical assumptions, and a tentative MVP roadmap. Open `docs/work/001-mvp/` **only now that discovery has started**. Do not assume the MVP scope is settled. Record unknown decisions honestly and use a concept prototype only if it helps validate a risky assumption. **Do not start implementing yet**.

The Agent can update `docs/product.md`, `docs/domain.md`, `docs/roadmap.md`, and working notes. Stages may be **skipped or merged** when they add no value.

## 3. Specify and implement one small increment

When the next increment is chosen, paste:

> For **[selected feature/increment]**, write one unified `docs/work/<objective>/spec.md` with goals and non-goals, observable acceptance criteria, main design choices, implementation strategy, and verification plan. Obtain independent design review when warranted by complexity or risk. Implement the **smallest complete valuable increment**. Run relevant tests, review the actual changed code, check conformance with the approved Spec, and address failures. If the Spec proves wrong, explicitly revisit the design instead of silently changing requirements. Show direct evidence of what works and identify what remains unverified. **Ask me to accept the result; don't mark it accepted yourself.**

The **Design Spec Loop** evaluates the plan; the **Implementation Loop** verifies the code and behavior. A separate `tasks.md` is optional. Compiling successfully is not, by itself, proof of a working feature.

## 4. Human acceptance, documentation sync, and release

Inspect actual behavior and evidence. If satisfied, explicitly accept the increment:

> I have inspected **[specific functionality/evidence]** and **[accept / request changes]**. If accepted, update only the relevant durable documentation (`docs/features/` for accepted, implemented behavior) and selectively archive important decision and verification evidence. **Distinguish accepted from released.** Do not deploy or publish without a separate explicit instruction.

Release happens only when appropriate. The **Evolution Loop** is available **at any step**, not only after release: new evidence that changes product assumptions, scope, or direction can send the project back to any relevant step (for example, a failed prototype back to Brainstorm). Ordinary Spec revisions or code/test fixes stay within the local Design Spec or Implementation Loop. Revisit only what needs reconsideration.

## Have an existing app instead?

Don't restart a mature project from Idea or overwrite its conventions. Use:

> Inspect my current repository, its `AGENTS.md`, code, and relevant docs. Apply only the parts of CoolFlow useful for **[specific fix or new feature]**. Preserve existing project structure and data. Define the smallest work objective and verifiable success criteria; implement, test, review, and ask for acceptance. Skip unrelated brainstorming, DDD, and prototypes.

## Human checkpoints

| Moment | What to confirm |
| --- | --- |
| Initialization | Only missing docs were added; existing material is intact |
| Before coding | Goal, constraints, and observable acceptance criteria are understood |
| After coding | Real changes and verification evidence support the claimed result |
| Before acceptance | Limitations, data risks, and a recovery option are understood |
| Before release | Accepted behavior is documented; release is separately authorized |

See the [CoolFlow Golden Rules](methodology/golden-rules.md) for the human-facing principles. **No mandatory global status file, Skill suite, or Agent orchestration system is introduced by this guide.**
