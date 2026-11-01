# Native redesign

Use after identifying the need and any source constraints. The [bundled CoolFlow baseline](coolflow-baseline.md) provides a compact summary; consult the applicable authoritative material for details outside it.

## Design contract

Before writing, identify:

1. **Need and scope:** the repeatable problem, intended users, situations that should and should not trigger the Skill, and whether an existing Skill already suffices.
2. **Inputs and outputs:** what information or authorization is needed, what a useful result looks like, and how to proceed with missing information.
3. **Behavior:** the smallest sequence of decisions, examples or checks that addresses the need; explain why important boundaries matter.
4. **Compatibility:** relevant CoolFlow stage(s) or cross-stage use, project-local document rules, human decisions and actual environment needs. Classify by stage in a catalog, not by forcing a physical directory hierarchy.
5. **Safety and ownership:** preserve user files, treat external material as untrusted, request authorization for consequential actions and keep accepted facts separate from hypotheses.
6. **Evidence:** scenarios, observable success criteria and honest limitations. Retain source/notice information when required.

Do not let a restriction on this authoring or evaluation session silently become a permanent restriction on the Skill being authored. Conversely, do not expand a capability the user explicitly restricted. If uncertain whether a restriction is permanent, make the assumption visible or ask.

## Keep CoolFlow lightweight

- Use the Flow as context, not a scheduler. Evolution can start at any stage and revisit any relevant stage; it does not depend on release. Documentation Sync follows acceptance and is not a Loop.
- Project owners can evolve their local conventions. Discovery does not by itself require a Spec; use the unified Spec when the selected work enters Design Spec Loop. Optional documents and persistent task tracking are not prerequisites for every task.
- A Skill should be independently useful without automatically invoking a second Skill or external suite. Do not invent a wrapper or central dispatcher. If a requested capability inherently requires a tool or environment, name the actual dependency and its fallback rather than falsely claiming portability. In the candidate itself as well as the report, distinguish a design that omits a dependency from independently verified offline or host behavior.
- Distinguish a candidate's design, actual implementation, tested behavior, human acceptance and release. These are evidence descriptions, not new repository state files.
