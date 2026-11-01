# Architecture Decision Records (ADR)

Use this optional template set when a project has an architectural or technical decision whose rationale should remain understandable after the original discussion and implementation have faded.

## What belongs in an ADR?

Create one ADR for a consequential decision about architecture, data ownership, system boundaries, security, deployment, a foundational technology, or a hard-to-reverse dependency.

Do not create an ADR for every feature, bug fix, UI detail, library import, or routine implementation choice.

## Recommended project layout

- docs/adr/README.md — optional index; useful when there are several ADRs
- docs/adr/0001-use-expo-react-native.md
- docs/adr/0002-use-local-first-storage.md
- docs/adr/0003-replace-provider-x.md

## Conventions

- One decision per file.
- Number records sequentially; use a short, descriptive filename.
- Keep the original record. If a decision changes, write a new ADR and mark the old one as Superseded; do not silently rewrite history.
- Suggested statuses: Proposed, Accepted, Rejected, Superseded, Deprecated.
- An ADR records why a decision was made and its consequences. The current implementation belongs in architecture documentation or the relevant Spec.
- A small project may omit the index file. The directory can contain only ADR records.

## When not to write one

Ask: would a future developer make a materially worse decision, or spend substantial time rediscovering the rationale, if this record did not exist? If not, skip it.

## Templates and example

- [ADR template](adr-template.md)
- [Example: choosing Expo + React Native](examples/0001-use-expo-react-native.md)

The example is illustrative, not a recommendation for every application.
