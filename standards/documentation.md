# Documentation standard (v0.1)

**Design rule:** durable, accepted project knowledge is separate from exploratory and in-progress work. Keep **one authoritative location per fact**; use links rather than duplicate paragraphs.

## Canonical application documentation tree

The following is the **default documentation tree for an application repository initialized with CoolFlow**. It describes the recommended homes and lifecycle of project documents; it is not a requirement to create every optional file.

```text
<app-repository>/
├── AGENTS.md                         # Required at initialization
├── README.md                         # Required at initialization
└── docs/
    ├── product.md                    # Required at initialization
    ├── roadmap.md                    # Required at initialization
    ├── domain.md                     # Required at initialization
    ├── features/                     # Directory required at initialization
    │   └── <feature>.md              # Accepted/current behavior; add after acceptance
    └── work/                         # Directory required at initialization
        ├── <objective>/              # Create only when real work begins
        │   ├── spec.md               # Default unified Spec
        │   ├── prd.md                # Optional: substantial product requirements
        │   ├── design.md             # Optional: deeper technical design
        │   ├── tasks.md              # Optional: persistent task progress
        │   ├── brainstorm.md         # Optional: useful discovery record
        │   └── prototypes/           # Optional: prototype artifacts
        └── archive/                  # Directory required at initialization
            └── <completed-work>/    # Selective completed-work evidence
    ├── architecture.md               # Optional: current system architecture
    ├── adr/                          # Optional: durable architecture decisions
    │   └── <decision>.md
    └── feature-map.md                # Optional: actual UI navigation and verification
```

### When each part is created

| Location | At initialization | When work begins | After acceptance |
|---|---|---|---|
| `AGENTS.md`, `README.md` | Create if missing | Maintain as needed | Keep current |
| `docs/product.md`, `roadmap.md`, `domain.md` | Create templates; unknown facts stay `Not started` | Update when decisions become durable | Sync accepted changes |
| `docs/features/` | Create directory | Usually leave unchanged | Add or update accepted feature descriptions |
| `docs/work/` | Create directory | Create one `<objective>/spec.md` for the actual objective | Archive selectively |
| `docs/work/archive/` | Create directory | No need to populate | Retain useful historical evidence |
| Optional documents | Do not create by default | Add only when complexity or a real need justifies them | Maintain or archive when relevant |

**Required at initialization** means create the missing files/directories in the template skeleton. It does not mean invent content, create empty feature documents, or start an implementation objective.

**Default when work starts** means one unified `spec.md` is the starting point. Optional artifacts are not mandatory steps or a fixed document checklist.

### What this tree deliberately does not prescribe

- No default `docs/solutions/`, `docs/knowledge/` or `docs/state.md` is required by CoolFlow v0.1.
- A project may add its own solution catalog, knowledge base, status note or other documentation if that project benefits from it. Such additions remain project-local choices, not CoolFlow initialization requirements.
- CoolFlow's own `flowsolutions/` directory belongs to the **CoolFlow methodology repository**. It is an external framework and method catalog, and is not copied into application repositories.
- Projects may customize document names and locations after initialization. Preserve one authoritative location per fact and keep the project-local `AGENTS.md` / README navigation accurate.

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
5. Use **Design Spec Loop (Step 6)** to review and revise material designs and **Implementation Loop (Step 7)** for tests, code review and Spec conformance. The **Evolution Loop** may be triggered by new evidence at **any step**, returning to any relevant step when product assumptions, scope or direction need reconsideration; routine quality fixes remain in their local Loops. After acceptance, sync durable docs as a **step**, not a separate Loop. Release and post-release feedback are possible events, not prerequisites for Evolution.
6. Keep structure lightweight; never add files solely to satisfy a checklist.
