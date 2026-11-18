# Documentation standard (v0.1)

**English** | [简体中文](documentation.zh-CN.md)

**Design rule:** durable, accepted project knowledge is separate from exploratory and in-progress work. Keep **one authoritative location per fact**; use links rather than duplicate paragraphs.

## Canonical application documentation tree

The following is the **default documentation tree for an application repository initialized with CoolFlow**. It describes the recommended homes and lifecycle of project documents; it is not a requirement to create every optional file.

```text
<app-repository>/
├── AGENTS.md                         # Required at initialization
├── README.md                         # Required at initialization
└── docs/
    ├── documentation.md              # Required at initialization; local documentation standard
    ├── coolflow.yml                  # Required at initialization; context preference
    ├── development-flow.md           # Required at initialization; on-demand reference
    ├── product.md                    # Required at initialization
    ├── roadmap.md                    # Required at initialization
    ├── domain.md                     # Required at initialization
    ├── features/                     # Directory required at initialization
    │   └── <feature>.md              # Accepted/current behavior; add after acceptance
    ├── work/                         # Directory required at initialization
    │   ├── <objective>/              # Create only when real work begins
    │   │   ├── spec.md               # Draft when objective enters Design Spec Loop
    │   │   ├── prd.md                # Optional: substantial product requirements
    │   │   ├── design.md             # Optional: deeper technical design
    │   │   ├── tasks.md              # Optional: persistent task progress
    │   │   ├── brainstorm.md         # Optional: discovery notes and product hypotheses
    │   │   ├── validation.md         # Optional: validation evidence and its decision
    │   │   ├── competitive-landscape.md # Optional: substantial competitor / market research
    │   │   └── prototypes/           # Optional: prototype artifacts
    │   └── archive/                  # Directory required at initialization
    │       └── <completed-work>/    # Selective completed-work evidence
    ├── solutions/                    # Optional: verified, reusable engineering knowledge
    │   └── <solution>.md              # One focused finding per file
    ├── architecture.md               # Optional: current system architecture
    ├── adr/                          # Optional: consequential architecture decisions
    │   └── <number>-<decision>.md     # One decision per file
    └── feature-map.md                # Optional: actual UI navigation and verification
```

### When each part is created

| Location | At initialization | During discovery / development | After acceptance |
|---|---|---|---|
| `AGENTS.md`, `README.md` | Create if missing | Maintain as needed | Keep current |
| `docs/documentation.md` | Copy the complete local standard if missing | Follow and adapt it to project needs | Keep project conventions current |
| `docs/coolflow.yml`, `docs/development-flow.md` | Copy default preference and offline reference | Update preference as needed | Keep reference discoverable |
| `docs/product.md`, `roadmap.md`, `domain.md` | Create templates with `status: not_started`; unknown body facts stay `To decide` | Update when decisions become durable, including the progress card | Sync accepted changes |
| `docs/features/` | Create directory | Usually leave unchanged | Add or update accepted feature descriptions |
| `docs/work/` | Create directory | Open an objective directory during discovery if useful; create its `spec.md` when entering Design Spec Loop | Archive selectively |
| `docs/work/archive/` | Create directory | No need to populate | Retain useful historical evidence |
| `docs/solutions/` | Do not create by default | Create when a non-obvious, durable and material engineering finding is verified | Keep useful findings current; remove misleading or obsolete guidance |
| `docs/adr/` | Do not create by default | Create one record when a consequential architecture or technical decision needs a durable rationale | Preserve history; supersede old decisions with new ADRs rather than rewriting them |
| Optional documents | Do not create by default | Add only when complexity or a real need justifies them | Maintain or archive when relevant |

**Required at initialization** means create the missing files/directories in the template skeleton. It does not mean invent content, create empty feature documents, or start an implementation objective.

**During discovery**, an objective directory can hold notes or prototypes without a Spec. **When a selected objective enters Design Spec Loop**, write its unified `spec.md` to define the implementable design and verification criteria. A Spec is not required merely to brainstorm; optional artifacts are not a fixed checklist.

### What this tree deliberately does not prescribe

- No default `docs/solutions/`, `docs/adr/`, `docs/knowledge/` or `docs/state.md` is required by CoolFlow v0.1.
- `docs/solutions/` is the recommended optional home for verified, reusable engineering knowledge. it is not created during initialization.
- `docs/adr/` is the optional home for Architecture Decision Records: one consequential decision per file. It is not created during initialization.
- CoolFlow's own `flowecosystem/` directory belongs to the **CoolFlow methodology repository**. It catalogs external frameworks and methods and is not copied into application repositories. An App's `docs/solutions/` is its own engineering knowledge store; the names are related but serve different purposes.
- Projects may customize document names and locations after initialization. Preserve one authoritative location per fact and keep the project-local `AGENTS.md` / README navigation accurate.
- Progress metadata lives in each document's frontmatter (see [Step 1–5 progress metadata](#step-15-progress-metadata)); it does not require a separate state file, engine or task list.

## CoolFlow context preference

`docs/coolflow.yml` stores the project-wide preference `context_mode`. New projects start in `auto`. Switch modes by editing this value. Work progress remains in its existing records.

| Request | `auto` | `manual` |
| --- | --- | --- |
| Plan a new project or reassess product direction | Read `docs/development-flow.md` and limit any further record reads to the requested direction. | Use the supplied context. Read the Flow reference only on explicit request. |
| Resume work without a named objective | Look for relevant active work in project records, including progress cards and Specs. Use a unique match or ask when there is no clear match. | Ask the user which objective to resume before searching work records, even if the project has only one active objective. |
| Named objective, Spec or concrete maintenance request | Read the task-relevant project files directly. | Read the task-relevant project files directly. |

Resolve the mode before searching for work records on an unnamed resume request. An absent file means `manual`. If the file is present but unreadable, malformed, or lacks a valid `context_mode` value (`auto` or `manual`), use `manual` and report the issue when consulting it. Apply project working rules in either mode. Honor explicit requests to review the methodology or report project progress. For an unnamed resume request, asking for the next step follows the resume row above.

## Step 1–5 progress metadata

Steps 1–5 (Idea → Brainstorm through UI Prototype) produce evolving documents rather than accepted behavior, so each document that records this work carries a short **progress card** at the top. It lets a person or an Agent judge where the work stands before reading the body.

Applies to `docs/product.md`, `docs/roadmap.md`, `docs/domain.md`, and work documents under `docs/work/<objective>/` that record Step 1–5 progress, such as `brainstorm.md` or `competitive-landscape.md`. It does not apply to `AGENTS.md`, `README.md`, `docs/documentation.md`, `docs/features/`, `docs/solutions/`, `docs/adr/`, or the objective-scoped `prd.md`, `spec.md`, `design.md` and `tasks.md`, which keep their own document status and track progress through their content, code and acceptance evidence.

```yaml
---
status: in_progress
related_steps: [1]
progress_updated: "2026-11-16"
current_progress: "Target users are roughly identified; use scenarios are under discussion."
next_steps:
  - "Identify the most common user problems."
open_questions:
  - "Whether team users are also in scope."
---
```

| Field | Required | Value |
|---|---|---|
| `status` | Yes | `not_started`, `in_progress`, `paused` or `complete`. |
| `related_steps` | Yes | Flow steps 1–5 the document relates to, for example `[1]` or `[1, 4]`. |
| `progress_updated` | No | Quoted `"YYYY-MM-DD"` date of the last progress update. |
| `current_progress` | No | One or two sentences: what is finished and what is under way. |
| `next_steps` | No | Short list of the next intended actions. |
| `open_questions` | No | Short list of unresolved questions or decisions. |

Rules:

- The block must be the first content in the file, before the top-level heading, and stay short — a card, not a second document. Quote values YAML could misread — `progress_updated` dates must be quoted — keep short enum values such as `status` unquoted, use block lists for multi-item text, and put no comments inside the block.
- `status` describes **the work this document records**, not the whole project and not a unique current stage. Several documents may relate to one step, and one document may relate to several steps with a single status; `related_steps` means related, not that every listed step has that status.
- An absent document or missing block is **not** evidence of `not_started`. Absence of progress metadata stays "no record found" until someone confirms otherwise.
- The card is a **snapshot** of human-confirmed work, not proof that requirements are accepted, code exists or validation happened. `complete` means the recorded work reached its intended end; acceptance and release are separate.
- Keep one authoritative location for status. A document that uses the block does not also carry a `> Status:` line.
- Fill optional fields only from actual work. Fresh core templates carry `status: not_started` and `related_steps`; new work documents carry `status: in_progress` because their creation means the work has begun. Leave the remaining fields out until real progress exists instead of writing placeholder text into them.
- A work document is created from real content: include only the sections the work actually covers and omit the rest, rather than copying unfilled template headings or leaving `To decide` under them. Copying a full template is appropriate only when an explicit empty starting structure is wanted.
- Update the card whenever the document's progress changes materially. Readers treat `progress_updated` as a hint about recency, not as proof that the body is current.
- To see where Step 1–5 work stands, read the cards first and open bodies only as needed. A requested Step 1–5 overview lists all five steps and distinguishes `not_started` from "no record found"; it does not infer a step's status from a related document alone. A general project overview is not limited to these cards: it may use relevant Specs, code and acceptance evidence to cover the applicable lifecycle without forcing a complete eight-step report.
- Default mappings for the core documents are `product.md` → `[1]`, `domain.md` → `[2]` and `roadmap.md` → `[4]`. Refine them when the project's actual organization differs, and record that choice in the project-local standard.

## Delivery progress (Steps 6–8)

Record delivery progress for a specific work objective in a `Delivery progress` section of its existing unified Spec, or in an existing authoritative acceptance or delivery record when local conventions assign it there. Consult and update one authoritative record for each fact. Use links for evidence maintained elsewhere. Keep the Spec's document status separate from delivery progress. Step 1–5 progress cards retain their existing scope.

| Field | Values | Evidence |
| --- | --- | --- |
| Implementation | `not_started`, `in_progress`, `implemented` | Observed changes and their scope or revision. `implemented` requires evidence that the agreed behavior is implemented. |
| Verification | `not_verified`, `partially_verified`, `verified` | Actual checks, results, and gaps for the relevant revision or scope. Use `partially_verified` when only part of the required verification is supported. |
| Acceptance | `pending`, `accepted`, `changes_requested` | Record an explicit human decision for the applicable scope. Use `pending` when awaiting a decision is established. |
| Release | `not_released`, `released` | Record explicit release authorization separately from the outcome. Use `released` when actual release evidence identifies what was released and where. Record available post-release checks. |

Record only supported fields and note material unknowns. Use `not_started`, `not_verified`, and `not_released` only when evidence establishes those states for the stated scope. Authorization, acceptance, and release are separate facts. After a material change, keep earlier verification, acceptance and release evidence scoped to the version it describes. Record the current gaps and seek fresh evidence or a human decision when needed.

During authorized work, record meaningful implementation and verification results when they are available, and record explicit human decisions when given. After acceptance, sync affected durable documents per the usual Documentation Sync rules. Release execution requires separate authorization. If an authoritative objective record is missing or ambiguous, report what remains unrecorded and resolve the destination before writing. No separate state file or retrospective migration is required.

## Recording results from Agent Skills

When a Skill produces project-specific decisions, findings or open questions worth retaining, identify the appropriate project document and record the useful result within the authorized scope. Read the project-local documentation rules and relevant existing work first. Update a meaningful checkpoint during longer discussions when useful, and complete the record before finishing the task; do not rely on the chat ending to trigger a later write. Preserve existing content and report which documents were actually updated.

Choose the destination by the content and current work, following project-local conventions before these defaults:

- During discovery, use the current work objective's existing notes or, when useful, `docs/work/<objective>/brainstorm.md`. Discovery alone does not require a Spec.
- For a selected objective in Design Spec Loop, capture relevant requirements, design decisions, trade-offs and open questions in its unified `docs/work/<objective>/spec.md` or the project's equivalent.
- Record human-confirmed, durable project-level plans and decisions in the relevant product, roadmap or domain document with their actual status. A roadmap may summarize future feature scope labeled as planned or proposed; keep detailed unaccepted behavior and unresolved designs in work records or a Spec. After human acceptance, sync affected accepted/current facts to product, roadmap, domain and feature documents as relevant; acceptance does not require release.

Distinguish observed facts, user claims, decisions, unverified findings, assumptions and unresolved questions from one another; user claims may not be independently verified. Update an existing authoritative record where possible rather than duplicating it; do not create an extra document for every Skill invocation. If the user requests a discussion-only result, writes are unavailable, or the project or appropriate destination cannot be determined, leave the documents unchanged and say what remains unrecorded and, when known, where it could go. Ask for the missing target when it is necessary to proceed.

## Core project docs (created on initialization)

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Stable working rules and links to the local documentation standard and context preference |
| `README.md` | Human-readable project entry; no invented features |
| `docs/documentation.md` | Complete project-local documentation standard; independently maintained after initialization |
| `docs/coolflow.yml` | Project context preference |
| `docs/development-flow.md` | Offline reference for the eight stages and three Loops |
| `docs/product.md` | A concise project-level Product Brief: problem, audience, vision, value, boundaries and current positioning; **not a PRD** |
| `docs/roadmap.md` | Product-level MVP/current version, later direction and priority; explicitly distinguishes planned from accepted |
| `docs/domain.md` | Ubiquitous language, domain boundaries, core rules; provisional and may remain unfilled initially |

Create `docs/features/`, `docs/work/` and `docs/work/archive/` as part of the skeleton; use `.gitkeep` if the Git directory is otherwise empty.

## Work artifacts (created during discovery or development)

## Idea → Brainstorm: competitive landscape

During Step 1, clarify the problem, target users and use context before researching existing solutions. Then conduct a competitive landscape analysis proportionate to the decision:

- Include direct competitors, indirect alternatives, substitutes and current user workarounds.
- Compare relevant target users, core value, user experience, key capabilities, pricing/business model, user feedback, limitations and unmet needs.
- Use credible sources; retain links and research dates, and distinguish observed facts from interpretation, assumptions and unknowns.
- Synthesize whether a meaningful opportunity or differentiation exists. Existing competitors may validate demand; their presence alone does not invalidate an idea. No visible competitor does not prove demand.

For a small idea or narrow feature, a brief scan or an explicit decision that deeper research adds little may be enough. For a new product or unfamiliar market, deeper research may be warranted. This is an exploration activity, not a new stage or a mandatory gate.

Record concise findings in the current work's `brainstorm.md` when useful. Create a separate `competitive-landscape.md` only when the research is substantial enough to maintain independently. Neither document is required for every idea, and neither is created during project initialization.


During discovery, **you may open** `docs/work/<objective>/` for exploration notes and prototypes; no Spec is required yet. When an objective is selected for **Design Spec Loop (Step 6)**, create the default unified `docs/work/<objective>/spec.md`. `<objective>` is a descriptive slug or number for a feature, MVP, fix or release. An initial product journey may use `001-mvp` once discovery begins, without claiming the MVP scope is settled.

A complete Spec should be comprehensible by a new Agent and provide:
- Context, goal and non-goals.
- User requirements and concrete acceptance criteria.
- Design/architecture decisions and major alternative trade-offs.
- Implementation strategy, dependencies and meaningful validation method.
- Open questions / assumptions clearly distinguished from decisions.

### When to use the work templates

CoolFlow maintains starter templates for these work artifacts:

| Artifact | When to use it | Template |
| --- | --- | --- |
| `spec.md` | The default unified Spec; create it when a selected objective enters Design Spec Loop (Step 6), not during brainstorming alone. | [Spec template](../templates/work/spec.md) |
| `prd.md` | Optional: when one objective has substantial product requirements, user journeys or scope that deserve a separate product-focused document. | [PRD template](../templates/work/prd.md) |
| `design.md` | Optional: when technical design is too detailed for the unified Spec; link to it from the Spec. | [Detailed design template](../templates/work/design.md) |
| `brainstorm.md` | Optional: default Step 1 home for problem, user, competitor, opportunity and hypothesis notes once real discovery begins. | [Discovery notes template](../templates/work/brainstorm.md) |
| `validation.md` | Optional: when Step 3 or Step 5 produces actual validation evidence and a decision. | [Validation template](../templates/work/validation.md) |
| `tasks.md` | Optional: only when task progress must persist across Agent sessions, agents or time and no existing tracker is sufficient. | [Persistent tasks template](../templates/work/tasks.md) |

These templates are starting points, not a checklist. Do not create optional artifacts merely because a template exists. During discovery, use notes and prototypes as needed; write the unified Spec only when the selected objective enters Design Spec Loop.

Optional artifacts, created for actual need:
- `prd.md`: optional, substantial product requirements for **one development objective**—user problem, journeys, scope and product-level success criteria; reference from Spec. It is not the project-wide Product Brief.
- `design.md`: complex technical design too detailed for unified Spec; reference from Spec.
- `tasks.md`: **only** when independent, persistent task progress is needed across sessions, agents, or time. Do not duplicate existing session, Issue or other task trackers.
- `brainstorm.md`: discovery notes, competitor findings, opportunity analysis and product hypotheses.
- `competitive-landscape.md`: optional, substantial competitor/market research that merits its own maintained record; do not create it by default.
- `prototypes/`: candidate concepts and working prototypes, in the applicable work directory.
- `docs/architecture.md`: current system architecture; `docs/adr/`: rationale for consequential architecture decisions. Both are optional and should be created only when complexity merits them.
- `docs/feature-map.md`: actual navigation paths, actions, stable test identifiers and verification procedures for operating the shipped/accepted UI, when useful. It is **not** a duplicate of `features/`.

## Accepted knowledge and archiving

- `docs/features/<feature>.md` describes behavior **actually implemented and accepted**, not planned behavior. Future ideas stay in `roadmap.md` or open work Specs. Use the [Feature record template](../templates/project/docs/features/feature-template.md) as a starting point.
- Acceptance triggers updates of relevant current docs; it does **not** imply production release.
- First sync the accepted truth. Then move a completed work directory to `docs/work/archive/`, selectively retaining important Specs, design/decision rationale and verification evidence; prune temporary drafts only when safe and appropriate.
- Keep the provenance of important choices. An ADR may be superseded, not erased.
- Never assume an empty template means the stage is completed; `status: not_started` and `To decide` mean not decided or not filled.
- Projects own their documents and may customize paths and conventions. No forced upstream version pinning or automatic migration.

## Reusable project Solutions (optional)

`docs/solutions/` is the optional home for **verified engineering knowledge that should help solve future work**. Create it only when the project has a finding worth preserving; it is not part of the initialization skeleton. See the [Solutions guidance and template](../templates/optional/solutions/README.md).

A separate Solution is worth recording when the finding is:

1. **Non-obvious:** a future developer is unlikely to recover the important reasoning from the final code, tests or ordinary documentation.
2. **Durable:** it should remain useful beyond the exact change that revealed it.
3. **Material:** forgetting it could cause a repeated failure, meaningful risk or substantial rediscovery.

A Solution may capture a verified root cause and fix, a technical constraint, a reusable engineering practice, or a failed approach that would otherwise be repeated. Keep one focused finding per file and link to its source work, tests, commit or other evidence. Search for overlap first; update an existing canonical record rather than creating a near-duplicate.

Do not store raw brainstorming, every debugging transcript, unverified guesses or information already obvious from code and tests. Capture only after the finding is verified, while its reasoning and evidence are available. Before related work, consult only the Solutions relevant to the task. Revisit records when code, dependencies or external conditions make them stale.

Keep knowledge in its narrowest durable home:
- `docs/work/archive/`: historical evidence of what happened in a completed work item.
- `docs/solutions/`: reusable engineering findings extracted from experience.
- `docs/adr/`: why a consequential architecture or technical decision was made.
- Tests, types and assertions: behavior that can be enforced mechanically.
- Code comments: local rationale needed beside one code path.
- `AGENTS.md`: only stable, high-priority instructions that future Agents must consistently follow.

Do not turn experience capture into a mandatory ceremony after every feature or bug fix. The Evolution Loop can produce useful experience at any stage; Solutions are a storage option, not an extra development stage.

These Solutions are **project-local**. If a finding is independently validated across multiple projects, it may be promoted to the developer's shared knowledge base. Only broadly validated development principles belong in CoolFlow's own `methodology/` or `standards/`.

## Architecture Decision Records (ADR, optional)

`docs/adr/` stores durable records of **why the project made consequential architecture or technical decisions**. It is not a general decision diary and is not required for every feature or implementation choice.

Create one ADR per decision when the choice affects architecture, data ownership, system boundaries, security, deployment, a foundational technology or a hard-to-reverse dependency. A useful ADR normally records context, decision drivers, options considered, the chosen decision and its consequences. See the [ADR template and example](../templates/optional/adr/README.md).

Use sequential, descriptive filenames such as `0001-use-expo-react-native.md`. Preserve accepted records. If a decision changes, create a new ADR and mark the earlier one as superseded instead of silently rewriting history. An optional README index may summarize the records when the collection grows.

An ADR records the **rationale** for a decision; the current system design belongs in `architecture.md` or the relevant Spec. Do not create ADRs for routine UI details, variable names, ordinary bug fixes or every feature.

## Document ownership

- `product.md` (**Product Brief**): *why this product exists, for whom and within what boundaries*; `roadmap.md`: *when/which scope*.
- Optional `prd.md`: *what user-facing outcome this particular increment needs*; it is not the project-level Product Brief.
- Unified `spec.md`: *precise expected behavior + implementable solution*.
- Optional `design.md`: *deeper technical details referenced by Spec*.
- Optional `tasks.md`: *mutable execution progress*, not another source of requirements.
- `features/`: *what is accepted and true now*.
- `feature-map.md`: *where and how to operate/verify implemented features*.
- Optional `solutions/`: *what verified engineering experience should change future work*.
- Optional `adr/`: *why a consequential architecture or technical decision was made*.

## Reviewing against CoolFlow

A CoolFlow conformance review uses this standard, or an identified offline snapshot of it, as its comparison baseline. Read project-local rules to understand the actual document roles, paths, and conventions. Equivalent arrangements allowed by this standard satisfy the baseline. Report differences from the baseline separately from violations of rules the project has adopted. Initialization-only requirements apply to projects initialized with CoolFlow. For an existing project considering adoption, recommend only the changes that would help its current work and leave adoption decisions to the user.

A distributed snapshot is a copy of this standard. When changing this standard, refresh the snapshot in the same change. Identify the reviewed snapshot in the report.

## AI rules

1. Read relevant files, not the entire documentation tree by default.
2. Preserve user data; don't overwrite existing README, AGENTS, code or docs without approval.
3. When information is unknown, use `status: not_started` in the progress card and `To decide` in the body; don't invent product requirements.
4. Ask a human for product-critical decisions; automate verifiable documentation/implementation tasks.
5. Create the unified `spec.md` when the chosen objective enters **Design Spec Loop (Step 6)**, not solely because discovery started; use that Loop to review and revise material designs and **Implementation Loop (Step 7)** for tests, code review and Spec conformance. The **Evolution Loop** may be triggered at **any step** by feedback, new ideas, or changing needs, returning to any relevant step when product assumptions, scope or direction need reconsideration; routine quality fixes remain in their local Loops. After acceptance, sync durable docs as a **step**, not a separate Loop. Release and post-release feedback are possible events, not prerequisites for Evolution.
6. When relevant, consult matching verified Solutions before work; capture only non-obvious, durable and material findings. Record an ADR only for a consequential architecture or technical decision, not every feature or fix.
7. Keep structure lightweight; never add files solely to satisfy a checklist.
