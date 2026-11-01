# Getting Started with CoolFlow

**CoolFlow by Cooling · An AI Software Development SOP**

[Home](README.md) · [简体中文](README.zh-CN.md) · [Golden Rules](methodology/golden-rules.md)

CoolFlow is a lightweight **development methodology and documentation standard**, not an Agent runner. Use it with your existing coding Agent. The optional coolflow-init Skill follows the open [Agent Skills specification](https://agentskills.io/specification); no particular Agent vendor or installation tool is required.

> **v0.1 draft:** The instructions below describe the intended workflow. End-to-end scenario execution and real project validation are **not yet completed**.

## Prerequisites

You need a **target application repository** that your coding Agent can inspect. This is separate from the CoolFlow reference repository.

Choose the correct starting point below. The coolflow-init Skill is only for a new, empty project directory. Existing projects use the separate inspect-first adoption process.

## Choose your starting point

### A. New project — initialize an empty directory

The optional coolflow-init Skill provides a short, reusable entry point for creating the CoolFlow documentation structure.

#### Target directory requirement

The target project root must be either:
- completely empty; or
- contain exactly one root-level .git entry, which may be a directory or a regular file (Git worktree metadata).

Every other entry makes the directory non-empty, including README.md, .gitignore, .DS_Store, other hidden files, directories and symlinks. The Skill must refuse to run without changing anything. Do not delete files just to make a directory eligible; choose a new empty directory instead.

#### Install the Skill — ask your Agent

Open the coding Agent you already use and send:

```text
Please install this Skill globally using the standard installation method for your current Agent:
https://github.com/CooLingLab/CoolFlow/tree/main/skills/coolflow-init
```

The Agent should choose the installation method it supports. If it cannot install Skills globally, it should tell you rather than guessing.

#### Other installation methods (fallback)

If you prefer to install it yourself:

- **Agent-native installation:** Follow your Agent's documentation for installing a user-level or global Skill. The Agent Skills specification defines the format, not one universal installation path.
- **Manual installation:** Download or clone this repository, then copy the complete `skills/coolflow-init/` folder into the global Skills directory documented by your Agent. Preserve the folder name.
- **Optional third-party installer:** [Vercel Skills CLI](https://github.com/vercel-labs/skills) supports multiple Agents:

  ```bash
  npx skills add CooLingLab/CoolFlow --skill coolflow-init -g
  ```

  This is optional and not a CoolFlow dependency. The CLI requires Node.js 22.20 or later; this requirement applies only to the installer.

Not every coding Agent supports Agent Skills or global installation. If yours does not, use its documented instruction mechanism or the manual initialization fallback below.

#### Use the Skill

1. Open a **new, empty target project directory** in your coding Agent.
2. Ask: **“Use `coolflow-init` to initialize this empty project.”**
3. The Agent checks the target root—including hidden entries—before making any changes.
4. If eligible, it reads the canonical CoolFlow standards and templates, creates the required project files, verifies them, reports the result, and stops. It does not automatically begin Brainstorm or write application code.

If your Agent cannot install or invoke Skills, use this manual initialization fallback:

> Read the CoolFlow repository at https://github.com/CooLingLab/CoolFlow. First inspect the current target project root, including hidden entries. Proceed only if it is empty or contains exactly one root-level .git directory or regular file; otherwise stop without changing anything. Read standards/initialization.md, standards/documentation.md, methodology/flow.md, methodology/loops.md, and the required templates under templates/project/. Follow the initialization contract exactly, create the required documentation structure, verify it, report the result, and stop. Do not begin Brainstorm or implementation.

Expected skeleton in an **empty project**:

    AGENTS.md
    README.md
    docs/
      documentation.md  # complete project-local documentation standard
      product.md        # concise project-level Product Brief, not a PRD
      roadmap.md
      domain.md
      features/
      work/
        archive/

Empty directories use .gitkeep for Git tracking. The Skill itself is **not copied** into the target application.

After initialization, the project follows its own docs/documentation.md; future documentation work does not require access to CoolFlow. Projects may adapt that local standard independently.

### B. Existing project — inspect before adopting

**Do not run coolflow-init in an existing or non-empty project.** The Skill will refuse to run there.

Instead, ask your coding Agent to inspect the existing project and propose a selective adoption plan:

> Read the CoolFlow guide at https://github.com/CooLingLab/CoolFlow and inspect my existing repository, including its AGENTS.md, code, architecture and relevant documentation. Summarize the actual project conventions and explain which parts of CoolFlow would help with **[specific fix, feature or development need]**. Propose the smallest useful adoption plan. Preserve all existing files, instructions, code and uncommitted changes. **Do not modify anything until I approve the plan.**

After approval, apply only the agreed changes. Do not rebuild the entire documentation tree, overwrite project conventions, or restart from Idea by default. Continue at the relevant CoolFlow stage for the work at hand.

## Continue a new project — discovery

After **new-project initialization**, explicitly start discovery when you are ready. For example:

> Let's begin Step 1 — Idea → Brainstorm for **[product idea]**. Follow the project's local CoolFlow instructions and guide me through problem and user discovery, competitive landscape analysis, opportunity identification and a product hypothesis. Discuss important decisions with me. Do not start implementing or create a formal Spec during brainstorming.

The Agent can update docs/product.md (the project-level Product Brief), docs/domain.md, docs/roadmap.md, and discovery notes. Competitive findings normally belong in brainstorm.md; create a separate competitive-landscape.md only for substantial research that merits its own record. **A work directory may exist without a Spec until a specific objective enters Design Spec Loop (Step 6).** A substantial objective may use its own optional docs/work/<objective>/prd.md; do not confuse that with the project brief. Verified, non-obvious, durable and material engineering experience may later be distilled into optional docs/solutions/; raw work history stays with the work item or archive. Record a separate ADR in optional docs/adr/ only when a consequential architecture or technical decision needs its rationale preserved. Stages may be **skipped or merged** when they add no value.

## Design and implement a selected increment

Before specifying related work, consult only relevant existing records in docs/solutions/ if that optional directory exists. Do not read the entire knowledge store by default. Capture a new Solution only after a finding is verified and only when it is non-obvious, durable and material.

When a concrete increment has been selected for **Design Spec Loop (Step 6)**, ask:

> For **[selected feature/increment]**, write one unified docs/work/<objective>/spec.md with goals and non-goals, observable acceptance criteria, main design choices, implementation strategy, and verification plan. Review the **current Spec draft and relevant context** independently when warranted by complexity or risk; resolve material findings and confirm that the design is ready to implement. Then implement the **smallest complete valuable increment**. Run relevant tests, review the actual changed code, check conformance with the approved Spec, and address failures. If the Spec proves wrong, explicitly revisit the design instead of silently changing requirements. Show direct evidence of what works and identify what remains unverified. **Ask me to accept the result; don't mark it accepted yourself.**

The **Design Spec Loop** evaluates the plan; the **Implementation Loop** verifies the code and behavior. A separate tasks.md is optional. Compiling successfully is not, by itself, proof of a working feature.

## Human acceptance, documentation sync, and release

Inspect actual behavior and evidence. If satisfied, explicitly accept the increment:

> I have inspected **[specific functionality/evidence]** and **[accept / request changes]**. If accepted, update only the relevant durable documentation (docs/features/ for accepted, implemented behavior) and selectively archive important decision and verification evidence. **Distinguish accepted from released.** Do not deploy or publish without a separate explicit instruction.

Release happens only when appropriate. The **Evolution Loop** is available **at any step**, not only after release: feedback, new ideas, or changing needs that warrant reconsidering product assumptions, scope, or direction can send the project back to any relevant step (for example, a failed prototype back to Brainstorm). Ordinary Spec revisions or code/test fixes stay within the local Design Spec or Implementation Loop. Revisit only what needs reconsideration.

## Human checkpoints

| Moment | What to confirm |
| --- | --- |
| Initialization | The target met the empty-directory requirement; only intended files were created |
| Before coding | Goal, constraints, and observable acceptance criteria are understood |
| After coding | Real changes and verification evidence support the claimed result |
| Before acceptance | Limitations, data risks, and a recovery option are understood |
| Before release | Accepted behavior is documented; release is separately authorized |

See the [CoolFlow Golden Rules](methodology/golden-rules.md) for the human-facing principles. **No mandatory global status file or Agent orchestration system is introduced by this guide.**
