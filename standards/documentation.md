# Documentation standard (v0.1)

**Design rule:** durable, accepted project knowledge is separate from exploratory and in-progress work. Keep **one authoritative location per fact**; use links rather than duplicate paragraphs.

## Core project docs (created on initialization)

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Self-contained concise lifecycle, docs rules, working boundaries, project-local index |
| `README.md` | Human-readable project entry; no invented features |
| `docs/product.md` | Problem, audience, product vision and current positioning; *not* the brainstorm transcript |
| `docs/roadmap.md` | MVP, future versions and priority; explicitly distinguishes planned from accepted |
| `docs/domain.md` | Ubiquitous language, domain boundaries, core rules; may remain unfilled initially |

Create `docs/features/`, `docs/work/` and `docs/work/archive/` as part of the skeleton; use `.gitkeep` if the Git directory is otherwise empty.

## Work artifacts (created only after development begins)

Default: **one unified** `docs/work/<objective>/spec.md`. `<objective>` is a descriptive slug or number; may represent one feature, an MVP, a fix, or a release objective. For an initial product journey, use `001-mvp` when discovery starts, without claiming its scope is settled.

A complete Spec should be comprehensible by a new Agent and provide:
- Context, goal and non-goals.
- User requirements and concrete acceptance criteria.
- Design/architecture decisions and major alternative trade-offs.
- Implementation strategy, dependencies and meaningful validation method.
- Open questions / assumptions clearly distinguished from decisions.

Optional artifacts, created for actual need:
- `prd.md`: substantial product scope, user journeys and product-level success criteria; reference from Spec.
- `design.md`: complex technical design too detailed for unified Spec; reference from Spec.
- `tasks.md`: **only** when independent, persistent task progress is needed across sessions, agents, or time. Do not duplicate existing session, Issue or other task trackers.
- `brainstorm.md`, `prototypes/`: candidate concepts and working prototypes, in the applicable work directory.
- `docs/architecture.md`, `docs/adr/`: current system architecture and durable decision rationale, only if complexity merits them.
- `docs/feature-map.md`: actual navigation paths, actions, stable test identifiers and verification procedures for operating the shipped/accepted UI, when useful. It is **not** a duplicate of `features/`.

## Accepted knowledge and archiving

- `docs/features/<feature>.md` describes behavior **actually implemented and accepted**, not planned behavior. Future ideas stay in `roadmap.md` or open work Specs.
- Acceptance triggers updates of relevant current docs; it does **not** imply production release.
- First sync the accepted truth. Then move a completed work directory to `docs/work/archive/`, selectively retaining important Specs, design/decision rationale and verification evidence; prune temporary drafts only when safe and appropriate.
- Keep the provenance of important choices. An ADR may be superseded, not erased.
- Never assume an empty template means the stage is completed; `Not started` means not decided or not filled.
- Projects own their documents and may customize paths and conventions. No forced upstream version pinning or automatic migration.

## Document ownership

- `product.md`: *why this product*; `roadmap.md`: *when/which scope*.
- Optional `prd.md`: *what user-facing outcome this increment needs*.
- Unified `spec.md`: *precise expected behavior + implementable solution*.
- Optional `design.md`: *deeper technical details referenced by Spec*.
- Optional `tasks.md`: *mutable execution progress*, not another source of requirements.
- `features/`: *what is accepted and true now*.
- `feature-map.md`: *where and how to operate/verify implemented features*.

## AI rules

1. Read relevant files, not the entire documentation tree by default.
2. Preserve user data; don't overwrite existing README, AGENTS, code or docs without approval.
3. When information is unknown, mark it as `Not started` / `To decide`; don't invent product requirements.
4. Ask a human for product-critical decisions; automate verifiable documentation/implementation tasks.
5. Use the **Design Spec Loop** to review and revise material designs before coding; use the **Implementation Loop** for tests, code review and Spec conformance. After acceptance, sync durable docs as a **step**, not a separate Loop. After release, use the outer **Evolution Loop** to incorporate feedback into the roadmap.
6. Keep structure lightweight; never add files solely to satisfy a checklist.
