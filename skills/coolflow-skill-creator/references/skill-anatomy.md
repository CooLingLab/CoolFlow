# Skill anatomy and discovery

Use this reference when writing or modifying a Skill. The [Agent Skills specification](https://agentskills.io/specification) describes the portable format; check a particular host separately when its requirements matter.

## Minimal structure

```text
skills/<skill-name>/
  SKILL.md                 # required entry point
  references/              # only when supporting detail is useful
  scripts/                 # only for real, reusable automation
  assets/ or templates/    # only when output resources are useful
```

Use a flat `skills/<skill-name>/` namespace; stage mapping is a catalog concern. A `SKILL.md` begins with YAML frontmatter containing `name` and `description`. The name matches its directory, is 1–64 lowercase letters, digits or hyphens, with no leading/trailing or consecutive hyphens. The nonempty description is at most 1024 characters and helps an Agent recognize concrete use and non-use cases. Prefer describing the trigger rather than putting a condensed workflow in the description.

Write a short main entry that can actually direct the task. Link supporting files with relative paths and say when they are needed; do not assume files elsewhere in the source checkout travel with an installed Skill. Add scripts only for useful repeatable work, document actual runtime requirements, and never run downloaded scripts without permission. If a resource is required, specify what to do when it is missing.

## Choose the instruction shape

Match the guidance to the observed problem: use explicit boundaries for a safety or ownership violation, a positive output structure for a malformed deliverable, a required field for a missing datum, and an observable condition for conditional behavior. Avoid turning every hypothetical edge case into a new rule. An example should demonstrate a real decision or useful result, not replace the procedure.

Separate the restrictions of the present authoring session from the future Skill's requested behavior. Do not promise that a Skill can perform actions its target environment cannot perform, and do not describe a user-provided fact as verified. Keep sensitive or destructive actions within the user's authorization and the host's actual permissions.
