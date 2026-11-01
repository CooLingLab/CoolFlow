# CoolFlow Ecosystem

This directory is a **reference catalog**, not a bundled toolchain or a mandatory dependency list.

It maps mature external frameworks, Skills, methods and tools to the stages and Loops in CoolFlow. The goal is to help a developer choose the smallest useful solution for the current problem without confusing a complete workflow suite with one of its components.

## Browse

- [Framework Comparison](framework-comparison.md) — compare lifecycle coverage, engineering practices, state management and knowledge capture across major AI development frameworks.
- [Solution Catalog](catalog.md) — broad research catalog of external methods, frameworks and Skills.
- [CoolFlow Advisor curated recommendations](../skills/coolflow-advisor/references/recommendations.md) — task-by-task **selected concrete Skills/tools**, bundled locally with the optional Advisor Skill.

## Selection principles

1. **Use the smallest sufficient solution.** Do not install a framework when a focused Skill, method or direct Agent instruction is enough.
2. **Separate suites from components.** A Skill inside a framework is not an independent framework; its parent and installation requirements must remain visible.
3. **Do not stack competing workflows blindly.** A complete suite may own its own artifacts, commands, gates and state model. Choose it as an alternative or selectively adopt compatible components.
4. **Prefer official sources.** Links point to the upstream project or its maintained documentation.
5. **Treat popularity as a signal, not a quality score.** Star counts are point-in-time context only.
6. **Re-check before adoption.** Projects, commands, compatibility and maintenance status change.

## Relationship to CoolFlow

CoolFlow defines the human-led development methodology and documentation conventions. The solutions listed here are optional ways to perform particular activities. They do not change the normative requirements in `methodology/` or `standards/`, and they are not automatically installed or invoked.

The catalog is intentionally maintained separately from the core methodology so that recommendations can evolve without turning CoolFlow into a mandatory Skills bundle.
