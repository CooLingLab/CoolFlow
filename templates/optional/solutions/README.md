# Project Solutions

This optional directory stores **verified engineering knowledge that should help solve future work**. It is inspired by the capture-and-reuse approach in [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin), adapted as a lightweight CoolFlow convention.

Create docs/solutions/ only when the project has a useful finding to preserve. It is not an initialization requirement and does not need to exist as an empty folder.

## What is worth recording?

A separate Solution is worthwhile when the finding is:

1. **Non-obvious:** a future developer is unlikely to recover the important reasoning from the final code, tests or ordinary documentation.
2. **Durable:** it is likely to remain useful beyond the exact change that revealed it.
3. **Material:** forgetting it could cause a repeated failure, meaningful risk or substantial rediscovery.

If the code, test, type, assertion or a short code comment already makes the knowledge obvious, do not create a separate document.

## What belongs here?

- A verified root cause and the fix for a non-obvious recurring failure.
- A technical constraint or integration behavior that future work must account for.
- A reusable engineering practice, pattern or workflow improvement backed by experience.
- Important failed approaches when knowing what did not work prevents repeated investigation.

## What belongs elsewhere?

- Change-specific history and raw implementation evidence: the work item, commit or docs/work/archive/.
- A consequential project architecture choice and why it was made: docs/adr/.
- Machine-enforceable behavior: tests, types, assertions or CI checks.
- A local explanation needed beside one code path: a code comment.
- Stable instructions that every Agent must follow: the project AGENTS.md, but only after the rule is sufficiently important and general.

## Capture and retrieval

- Before related work, search and read only the existing Solutions relevant to the task.
- Capture after the finding has been verified, while its reasoning and evidence are still available.
- Search for overlap first. Update an existing canonical Solution instead of creating a near-duplicate.
- Keep one focused finding per document. Link to the source Spec, work item, tests, commit or other evidence.
- Record failed approaches only when they teach something reusable.
- Revisit a Solution when code, dependencies or external conditions make it stale. Correct or remove misleading guidance.

Do not turn experience capture into a mandatory ceremony after every feature or bug fix. The Evolution Loop can produce useful experience at any stage; Solutions are a storage option, not an extra development stage.

## Suggested layout

Start simple:

- docs/solutions/README.md
- docs/solutions/<descriptive-solution-name>.md

If the collection grows, add a small number of category folders that match the project's actual knowledge. Do not create a taxonomy before it is needed.

## Templates and examples

- [Solution template](solution-template.md)
- [Example: bug-fix knowledge](examples/bug-fix.md)
- [Example: reusable engineering practice](examples/engineering-practice.md)

Examples are illustrative; adapt them to the project's real evidence and vocabulary.
