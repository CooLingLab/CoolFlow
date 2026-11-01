# CoolFlow Golden Rules

**The Four Golden Rules for AI-Assisted Software Development**  
*By Cooling · Creator of CoolFlow*

Inspired by a **pilot's approach** to aviation SOP principles, these Golden Rules help human developers keep priorities clear, maintain situational awareness, retain a way back, and verify real outcomes. They are adapted for software engineering, not copied from aircraft procedures, and are **applicable beyond the CoolFlow methodology**.

> **Audience: human developers.** These rules help a person maintain practical control of the **whole AI-assisted software development lifecycle**, even when an Agent performs most of the actual work.
>
> These are enduring *judgment principles*, not new Flow stages, automated gates, compulsory Skills, or a substitute for the detailed execution constraints in `AGENTS.md`.

## 1. Keep It Working → Ship Small → Improve

**保持正确运行 → 小步交付 → 持续改进**

When engineering priorities compete:

1. **Keep It Working:** protect the known-good behavior, user data, safety and essential operation of the product. Correct a critical regression or serious risk before accumulating new changes.
2. **Ship Small:** prefer the smallest **complete, valuable, verifiable** increment over speculative scope or big-bang implementations. `Ship` means a genuinely usable delivery appropriate to the context, not skipping review, testing, or an agreed release gate.
3. **Improve:** refine performance, architecture, maintainability, user experience or breadth after the necessary behavior and delivery path are sound.

**This is a default conflict-resolution priority, not three compulsory sequential phases.** On a new product with no existing code, start by establishing a thin working baseline; do not manufacture bugs to fix. An urgent performance or security issue can itself be the highest-priority work. `Ship Small` is **not** `Ship More`: value and correctness matter more than raw output volume.

**Human checkpoint:** Are we protecting what already works, delivering the smallest meaningful next increment, and avoiding unnecessary expansion?

## 2. Know the Actual State

**始终知晓项目与 Agent 的实际状态**

Know the difference between what the developer **intended**, what the Agent **attempted**, what changed **in the repo or environment**, what is **verified**, what the human **accepted**, and what is **actually released**. A planned step or confident completion message is not evidence of completion.

For substantial work, a short Agent end-of-task report can help: current objective/Flow or Loop, observed changes, verification evidence, known blockers, and next action. Such a report is only a **signal**, not a separate source of truth. Cross-check the relevant Spec, Git history/diff, actual tests and acceptance decision. Several work objectives may occupy different stages at the same time; do not invent a single global phase.

A persistent project-status document or Dashboard can be useful later, but **neither is required by this Golden Rule**. If used, show its evidence and last verification point to avoid misleading stale status.

**Human checkpoint:** Do I know what has *actually happened*, what remains unverified, and what happens next?

## 3. Keep a Way Back

**始终保留可恢复的退路**

Before a significant change, understand its scope and preserve a practical route back to a known-good state. Use appropriate Git commits/branches or other checkpoints, isolated environments, backups and tested recovery methods **proportionate to the risk**.

**Git can restore code history, but not necessarily database state, user data, deleted secrets, external side effects, or an already-applied production migration.** Irreversible operations require a separate risk assessment and recovery or mitigation plan. A rollback that nobody has verified may not be a real fallback.

**Human checkpoint:** What could this change break, what is our known-good reference, and can we actually recover if it goes wrong?

## 4. Prove It Works

**以真实结果证明有效**

Never treat an Agent's self-report, the presence of generated files, or a successful compilation as sufficient proof that the desired outcome has been achieved.

Require **appropriate direct evidence** for the claim being made: exercised user-visible paths, relevant automated tests, logs, screenshots or simulator/device behavior, observable side effects, and comparison with acceptance criteria. When useful, retain commands, inputs and results so that a different reviewer can reproduce the verification. Distinguish **not tested**, **test passed**, **human accepted**, and **released**.

This echoes PStack's [Prove It Works](https://github.com/cursor/plugins/tree/main/pstack/skills/principle-prove-it-works) principle; CoolFlow uses it as a human acceptance standard across its Flow and Loops, not as a required external dependency.

**Human checkpoint:** What observable evidence proves this specific outcome, and what remains untested?

---

## How the four rules fit together

| Human concern | Golden Rule | Question |
| --- | --- | --- |
| Engineering priority | Keep It Working → Ship Small → Improve | What must come first when priorities conflict? |
| Situational awareness | Know the Actual State | What is actually happening, not merely planned? |
| Recoverability | Keep a Way Back | Can we return to safety if this fails? |
| Evidence and acceptance | Prove It Works | What proves the result really works? |

These rules guide **human judgment** at every point in the [Development Flow](flow.md), including the [Design Spec, Implementation and Evolution Loops](loops.md). They do not imply that the human must write every line of code or manually manage every Agent task.

## Relationship to AGENTS.md

- **Golden Rules:** short, durable principles for the **human developer**.
- **Flow and Loops:** the recommended process for developing and reviewing software.
- **AGENTS.md:** explicit instructions and constraints for **AI Agents**, including approval boundaries, code changes, validation and reporting.
- **Skills and tools:** optional mechanisms for executing or automating repeatable work.

Keep this separation: do not mechanically turn Golden Rules into additional mandatory documents, status files, Skills, or per-turn Agent output. Concrete Agent instructions can be specified separately when the developer chooses to adopt them.
