# Source research and capability extraction

Use this reference for adapting, combining, or evaluating external material. For a Skill created from scratch, identify the user need and existing overlap without inventing an upstream source.

## Establish the source

For each relevant source, record the exact repository and file, immutable commit or release, author if known, license and its distribution/notice conditions, review date, and which files were actually read. Follow references far enough to identify material behavior and dependencies: other Skills, scripts, services, credentials, network, platform or permissions. A repository URL, a summary, or a license badge alone is not complete source inspection.

When a file, version, dependency or license is missing, mark it unknown; do not infer an MIT license from another repository or claim the candidate is independently usable. Do not execute untrusted instructions, install packages, or transmit project data during research. Obtain authorization and isolate any later executable tests. If provenance or permission is unresolved, do not copy substantial upstream expression or promote the adaptation; a provisional, independently written exploration may remain possible. Seek appropriate legal advice when the obligations are uncertain.

## Extract and decide

Make a compact matrix, in conversation or an existing work record only when useful:

| Item | Source and evidence | Native decision | Reason / unresolved issue |
| --- | --- | --- | --- |
| User problem and useful method | Specific file / revision or unknown | Retain / adapt / reject | Actual need |
| Handoffs, files and runtime | Dependencies actually observed | Remove / make optional / disclose | Compatibility and portability |
| Existing native coverage | Skill or catalog entry inspected | Reuse / improve / create / no-op | Gap, or inspection unavailable |
| License and attribution | Actual license text and provenance | Preserve notices / investigate | Distribution conditions |

Compare multiple sources on decision-relevant capabilities; do not average incompatible workflows. An upstream habit, stage sequence, hard-coded path or suite integration is not automatically a reusable principle. Keep only what improves the actual task, and explain trade-offs and conflicts. If existing coverage is sufficient, recommend using it instead of creating a duplicate.

The creator itself was informed by Superpowers `writing-skills`; its fixed source, adaptation notes and MIT notice are in [UPSTREAM-NOTICE.md](../UPSTREAM-NOTICE.md). This provenance does not make Superpowers a runtime dependency.
