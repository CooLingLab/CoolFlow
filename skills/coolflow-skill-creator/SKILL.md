---
name: coolflow-skill-creator
description: Use when asked to create, adapt, combine, test, refactor, or maintain a CoolFlow-native Skill. Do not use merely to choose a Skill or initialize a project.
---

# CoolFlow Skill Creator

Develop useful, independently usable CoolFlow Skills—not a collection of copied upstream workflows. Work from the user's actual need; an existing Skill, a small improvement, or no new Skill may be the best outcome. This is an optional maintenance Skill, not a development-stage controller.

## Scope and source of truth

- Support creation from scratch, adaptation or combination of sources, improvement of an existing Skill, and testing or review without rewriting it. Skip source research when no external source is involved.
- First identify the requested deliverable, target location, existing related Skills, constraints, and authorized actions. For an in-chat design or review, deliver the requested draft or assessment without changing files. If the user asks to run tests without modifying the Skill, run the authorized tests and leave that Skill unchanged. If they ask only for a test plan, do not run tests. Do not install, commit, push, publish, or change application files merely because this Skill is invoked.
- Before writing or changing a Skill on disk, inspect the exact target and preserve existing files, local overrides and user work. A request to create a new Skill does not authorize overwriting an existing target: if it already exists, stop and ask whether to update it or choose another name. For an explicitly authorized update, change only the agreed scope. If a target or its path is a symlink, resolve and verify its destination before writing; stop and ask if the destination or authorization is unclear.
- Read [the bundled CoolFlow baseline](references/coolflow-baseline.md). It is a compact summary maintained with this Skill, not a copy of the complete Standard. When working in a confirmed CoolFlow source checkout, use its applicable `standards/` and `methodology/` as the source of truth. A target application's own instructions and documentation conventions remain its own; do not overwrite them with this summary.
- Do not assume that this Skill's installation folder, an Agent configuration folder, or an application directory is a CoolFlow source checkout. When the user requests a current-version check and network access is permitted, compare against the official upstream and disclose differences. Keep the bundled summary aligned as a normal maintenance change. If a needed rule is absent and its authoritative source is unavailable, mark that requirement unverified and obtain the source before claiming conformance.
- The installed Skill needs this file and the complete `references/` directory. If a needed reference is missing, report the incomplete installation and stop the affected work instead of inventing its contents. Include [the upstream notice](UPSTREAM-NOTICE.md) when distributing this Skill.

## Workflow

Use the applicable steps, proportionate to the task. These are Skill-engineering activities, not new CoolFlow lifecycle stages or a mandatory state machine.

### 1. Research sources, when applicable

Read each relevant upstream `SKILL.md` and the supporting instructions, referenced Skills, scripts and license needed to understand its behavior. Identify the repository, immutable revision, actual dependencies and license terms; distinguish verified facts from user-provided or inaccessible information. Treat upstream text and scripts as untrusted reference material: do not execute or install them just to read them. See [capability extraction](references/capability-extraction.md).

If a source or its license is unavailable, describe the gap. An independently worded, clearly provisional design based on the available ideas may still be useful; do not copy unlicensed material or promote an adaptation until source, dependency and distribution questions are resolved.

### 2. Extract capabilities and check overlap

Identify the problem, useful techniques, inputs, outputs, and failure modes. Separate transferable methods from author preferences, upstream-specific handoffs and runtime assumptions. Compare with relevant existing native Skills or the catalog when available. If coverage is already adequate, recommend using the existing Skill; if inspection is impossible, say overlap is unknown. Explain what to keep, change, reject or combine and why; a concise conversation is enough when a persistent record is unnecessary.

### 3. Redesign for CoolFlow

Specify the trigger and non-trigger, desired behavior, user-controlled boundaries, inputs, output and verification. Map only to stages relevant to the capability, including cross-stage use where appropriate. Respect the one Flow and three adaptive Loops, project-local document ownership and human acceptance; never turn the eight stages into mandatory gates. Remove unnecessary upstream handoffs, duplicate trackers and specific harness requirements. If an essential dependency cannot be removed, disclose it; do not describe the result as independent. In both the candidate Skill and the report, say “designed not to require” a dependency when that is the intent; do not claim it actually runs offline or independently until the relevant behavior has been tested. See [native redesign](references/native-redesign.md).

Separate constraints on **this authoring session** from the intended future Skill. For example, a request not to write files while drafting does not, by itself, forbid future explicitly authorized read-only checks. Preserve restrictions the user actually specifies for the future Skill, and obey all current session and environment restrictions.

### 4. Design the smallest useful evaluation

Define the ordinary task, observable result and relevant constraints. Where practical, choose a small realistic scenario, test it without the new Skill or against the old version, and record what actually happens; if the unassisted attempt already succeeds, say so. A Skill that only documents a reference may need retrieval checks rather than a behavioral baseline. See [validation](references/validation.md).

**Default to one ordinary scenario plus static checks.** Treat a boundary, refusal, non-trigger, source/license, repeated run, or comparison of multiple variants as optional unless the task risk makes it necessary. Before expanding beyond this default, state the proposed cases, number of runs and expected cost, and obtain the user's agreement. Never invent a baseline or a test failure.

### 5. Implement the smallest useful Skill

When the user authorized implementation, create or update `skills/<skill-name>/SKILL.md` at the agreed target. When only an in-chat draft was requested, provide the actual draft in the response without writing files. Use a valid matching `name`, a concrete discovery-oriented `description`, explicit instructions and practical boundaries. Add local references, assets or scripts only when useful, and explain when to load them. Do not introduce mandatory dependencies on Advisor, this creator, a third-party suite, a particular subagent runtime or an application document tree. See [Skill anatomy](references/skill-anatomy.md).

### 6. Validate and improve

Run the same authorized scenarios with the Skill, inspect both behavior and outputs, and revise only material failures. A single passing run is evidence about one case, not proof of universal reliability. Static checks and reading alone are not behavioral tests. Before a further iteration, show the user the actual output, the material failures and the proposed next change; continue only if the user agrees or the existing task already authorizes that iteration. Stop when the result is adequate, the remaining risk is documented, or further testing is not adding useful evidence. Follow the specific repository's independent-review requirement separately; that repository rule does not make repeated multi-Agent evaluation the default for every candidate.

If no baseline, runtime, source, or relevant test is available, deliver a clearly identified draft with a concrete test plan and limitations. Never report a proposed test, a static source check or a user assertion as a passed behavioral test. Do not delete existing work to manufacture a test-first history.

### 7. Human acceptance and promotion

Present the candidate, source and license status, actual checks and evidence, unresolved risks, and any repository-specific registration the user wants. A candidate is not accepted merely because it exists as a draft. Promote it only after relevant tests and source/distribution checks are complete and a human explicitly accepts the result. Human acceptance is separate from installing, publishing, committing or releasing.

## Response

Report the decision and deliverable first: **existing capability / draft / tested candidate / accepted**, as supported by evidence. Include what was retained or removed when adapting sources, the applicable CoolFlow baseline, exact checks performed, unverified items and the smallest next action. Do not imply that a single scenario or a successful review proves universal compatibility.
