# Stage activities and Skill boundaries

**English** | [简体中文](activities.zh-CN.md)

**Status: draft for discussion.** This document is a non-normative companion to the
[Development Flow](flow.md). It identifies the distinct activities that can appear
within each stage and, once agreed, the boundaries at which a Skill may be useful.

It does not add stages, require every activity in every project, or replace the
[documentation standard](../standards/documentation.md). The eight stages and the
three Adaptive Loops remain as defined in [flow.md](flow.md).

## How this document is being developed

The activities are confirmed one stage at a time with the developer. Until a stage
has been discussed and confirmed, its content is marked `In discussion` or
`Not started`. A confirmed activity list is a shared understanding of the work, not
a mandatory checklist.

Each confirmed stage uses the same table:

- **Activity:** a distinct piece of work within the stage.
- **Answers:** the question this activity resolves.
- **Core output:** the useful result or evidence it produces.
- **Boundary:** what belongs here, and what belongs to a neighboring activity.

Skill allocation is deliberately deferred until all stage boundaries are agreed.

## Stage status

| Stage | Status |
| --- | --- |
| 1. Idea → Brainstorm | Agreed (2026-11-05) |
| 2. Lightweight Strategic DDD | Agreed (2026-11-05) |
| 3. Concept Prototype → Validation | Agreed (2026-11-06) |
| 4. Roadmap | Agreed (2026-11-06) |
| 5. UI Prototype | Agreed (2026-11-06) |
| 6. Design Spec Loop | Agreed (2026-11-06) |
| 7. Implementation Loop | Agreed (2026-11-06) |
| 8. Human Acceptance → Documentation Sync → Release | Agreed (2026-11-06) |
| Evolution Loop (cross-stage) | Not started |

## 1. Idea → Brainstorm

Status: `Agreed` (2026-11-05)

| ID | Activity | Answers | Core output | Boundary |
| --- | --- | --- | --- | --- |
| 1.1 | Understand users and the problem, including proportionate user research | Who encounters what difficulty, in which situation? | Users, contexts, problems, known evidence, and research methods/sources/dates when evidence is gathered | Does not research competitors or propose solutions |
| 1.2 | Research competitors and alternatives | How is this problem currently addressed? | Direct competitors, indirect alternatives, workarounds, sources and research dates | Does not decide what we should build, and does not treat competitor features as requirements |
| 1.3 | Define the problem boundary | Which problem are we solving, and which are we not? | Problem statement, target-user boundary, non-goals and key constraints | Does not judge whether the opportunity is worthwhile, or design a solution |
| 1.4 | Assess the opportunity | Which gaps in current solutions are worth considering, and on what evidence? | Opportunity hypotheses, supporting evidence, counter-evidence and unknowns | Does not commit to development or expand into features |
| 1.5 | Explore product directions | What different approaches could address the problem? | Multiple candidate directions with value and cost comparison | Does not converge on final scope or write a Spec |
| 1.6 | Form a product hypothesis | What do we currently believe, and what should be validated first? | Target users, value proposition, differentiation hypothesis and key risks | Not an established conclusion, and not a Roadmap |

### Rationale and boundaries

- 1.1 and 1.2 gather different evidence: user/problem evidence versus external
  solution evidence. Keeping them separate prevents competitor features from being
  treated as user requirements.
- 1.1 includes proportionate user research when existing evidence is insufficient—for
  example interviews, observation or analysis of existing data. Research depth matches
  the decision; findings distinguish observations, user claims, interpretation and
  assumptions. User research is an activity within discovery, not a separate stage or
  mandatory gate.
- 1.3 frames the problem before judging opportunity. It is a proposed refinement;
  the current `flow.md` treats this framing as part of discovery and opportunity
  work rather than as a separately named step.
- 1.4 judges opportunity using 1.1–1.3. It does not select a feature or promise scope.
- 1.5 explores multiple directions; 1.6 turns a selected direction into a testable
  hypothesis. Designing and running validation experiments belongs to
  Stage 3, not to this stage.
- Research depth is proportionate to the decision. A narrow feature may need only a
  quick scan or an explicit decision that deeper research adds little.
- No formal Spec is created in this stage. Discovery notes and evidence may live in
  the current work directory when useful.

### Sources consulted

The decomposition was checked against the following public practices. They informed
the boundary choices but are not normative for CoolFlow:

- Teresa Torres, [Product Discovery Basics](https://www.producttalk.org/2021/11/product-discovery/):
  outcome → opportunities → solutions; separate the opportunity and solution spaces.
- Design Council, [The Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/):
  discover and define the problem before developing and delivering solutions.
- Nielsen Norman Group, [Design Thinking 101](https://www.nngroup.com/articles/design-thinking/):
  empathize, define, ideate, prototype and test as distinct activities.
- Marty Cagan, [The Four Big Risks](https://svpg.com/four-big-risks/): value,
  usability, feasibility and business viability as assessment dimensions.
- Strategyn, [Jobs-to-be-Done](https://strategyn.com/jobs-to-be-done/): identify
  unmet outcomes rather than starting from product features.
- Strategyzer, [Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas):
  describe the customer problem and the proposed value separately, then test fit.

## 2. Lightweight Strategic DDD

Status: `Agreed` (2026-11-05)

**Scope:** initial strategic domain discovery. This stage produces a provisional domain
model. Tactical domain design—aggregates, entities, value objects, repositories, domain
events and transaction boundaries—is deferred to Design Spec Loop (Step 6).

| ID | Activity | Answers | Core output | Boundary |
| --- | --- | --- | --- | --- |
| 2.1 | Define domain scope and participants | Which part of the business, which roles and which work objects are involved? | Domain scope, participants/roles, core work objects, core and supporting parts | Does not redefine the Stage 1 product problem or target users; does not design technical modules |
| 2.2 | Establish the ubiquitous language and core concepts | What does each core term mean within this domain? | Glossary, definitions, synonyms and ambiguities, core concepts and relationships | Does not collect every UI label or code name; cross-context conflicts belong to 2.3 |
| 2.3 | Identify bounded contexts | Which concepts share one consistent meaning, and where does the same term mean something different? | Context list, language and responsibilities per context, relationships between contexts | Not a microservice, code-module or deployment boundary; does not decide interfaces |
| 2.4 | Define core business rules and invariants | Which conditions must always hold, and how does state change? | Invariants, business rules, state transitions, exceptions and failure conditions | Does not specify implementation algorithms or database constraints; does not replace acceptance criteria |
| 2.5 | Validate and confirm the model through business scenarios | Can the model explain real workflows and edge cases, and what remains unresolved? | Key scenario walkthroughs, revised model, confirmed understanding, open questions | Not user acceptance or prototype testing; does not validate product assumptions; does not write a Spec |

### Rationale and boundaries

- 2.1 and 2.2 are separate: 2.1 establishes what is in view; 2.2 defines what the terms
  mean. Combining them tends to mix product names, UI labels and technical identifiers
  into the domain language.
- 2.3 identifies **semantic** boundaries. A bounded context may later influence module
  or service boundaries, but it does not decide deployment or interfaces here.
- 2.4 records business rules and invariants, not implementation constraints. Database
  constraints and code-level enforcement belong to later design and implementation.
- 2.5 uses business narratives and paper walkthroughs to expose missing concepts and
  rules. It is not a prototype, user test or acceptance decision.
- The model recorded in `docs/domain.md` is provisional and evolves. Tactical design
  and code-level model refinement happen in Steps 6 and 7; new domain insight can
  return here through the Evolution Loop.
- The stage is proportionate. A small or familiar domain may need only core terms, key
  rules and one context. Do not invent multiple contexts merely to perform DDD.
  EventStorming, Domain Storytelling and context mapping are optional methods.

### Sources consulted

The decomposition was checked against the following public practices. They informed
the boundary choices but are not normative for CoolFlow:

- Eric Evans, [Whirlpool Process of Model Exploration](https://www.domainlanguage.com/ddd/whirlpool/):
  model exploration is not a development process and fits within iterative design.
- Martin Fowler, [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html):
  a shared rigorous language evolves as domain understanding grows.
- Martin Fowler, [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html):
  large models are divided into semantic contexts; a context is not a code module.
- DDD Crew, [DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process):
  domain discovery, decomposition, strategy and tactical design are iterative, not a
  linear sequence.
- Domain Storytelling, [DDD with Domain Storytelling](https://domainstorytelling.org/domain-driven-design):
  stories support strategic design, ubiquitous language and later tactical design.
- EventStorming, [EventStorming](https://www.eventstorming.com/): collaborative domain
  exploration can reveal events, boundaries and open questions.

## 3. Concept Prototype → Validation

Status: `Agreed` (2026-11-06)

**Scope:** time-boxed validation of the riskiest assumptions before committing to MVP
scope. A prototype is one possible test vehicle, not a requirement. A thin MVP may be
used as an experiment when it is the cheapest reliable way to observe behavior; it does
not replace the Roadmap decision or automatically become production code.

| ID | Activity | Answers | Core output | Boundary |
| --- | --- | --- | --- | --- |
| 3.1 | Identify and prioritize key assumptions | Which beliefs could most likely invalidate the direction, and which should be tested first? | One or two key assumptions ranked by importance and weakness of existing evidence | Does not enumerate every assumption; does not test low-risk items |
| 3.2 | Design the minimum validation and timebox | Which method, participants, result and deadline are sufficient to decide? | Validation plan: method, participants/sample, tasks or experiment steps, success criteria and timebox | Does not build a prototype before defining the question; does not create open-ended research |
| 3.3 | Create the minimum test vehicle | What is the cheapest artifact that can produce relevant evidence? | Clickable HTML, Figma or paper prototype, logic prototype, technical spike, survey, landing page or data-analysis material | Does not pursue production quality or build the complete product; spike code does not enter production |
| 3.4 | Run the validation and collect evidence | What actually happened, and how strong is the evidence? | Target-user behavior, technical results, data, failure cases and evidence strength | Does not substitute internal opinions for user evidence; does not treat a working spike as a completed feature |
| 3.5 | Interpret the result and decide the next step | Continue to MVP, adjust, return to an earlier stage, or stop? | Decision, known risks, open questions and next action | Does not treat one test as universal proof; does not extend validation indefinitely |

### Rationale and boundaries

- 3.1 combines identification and prioritization to avoid a separate ceremony. Select
  one or two assumptions that are both important and weakly evidenced; do not attempt
  to validate everything.
- 3.2 chooses the method according to the risk. User understanding and interaction
  risks favour concept or clickable prototypes; feasibility risks favour technical
  spikes; demand risks may require a landing page, waitlist or real behavioral data.
- 3.3 uses the cheapest sufficient test vehicle. AI-generated clickable HTML is a common
  lightweight option for concept and basic-interaction validation, but it cannot prove
  technical feasibility or commercial viability. Technical spike code is disposable.
- 3.4 collects direct evidence rather than opinions. User-facing assumptions should be
  tested with target users where possible; technical assumptions should be tested in a
  representative environment. Record what was simulated and what was real.
- 3.5 labels evidence strength and makes an explicit decision. If the test design was
  flawed, fix the test before concluding that the product failed. If the evidence
  invalidates product direction or scope, use the Evolution Loop.
- A thin MVP may be used as an experiment when it is cheaper or more reliable than a
  prototype. It remains an experiment: it does not replace the Roadmap decision and
  does not automatically become production code.
- When risk is low or existing evidence is sufficient, skip this stage and record why.
  Exit when the evidence is sufficient to choose MVP scope, not when every assumption
  is certain. Remaining uncertainty must be recorded as a known risk.

### Sources consulted

The decomposition was checked against the following public practices. They informed
the boundary choices but are not normative for CoolFlow:

- Teresa Torres, [Assumption Testing](https://www.producttalk.org/assumption-testing/):
  prioritize assumptions by importance and evidence, test one assumption at a time,
  define success before testing and track evidence.
- Strategyzer, [Testing Business Ideas](https://www.strategyzer.com/library/testing-business-ideas-book):
  use assumption mapping and choose experiments by cost, time and strength of evidence.
- GV, [The Design Sprint](https://www.gv.com/sprint/): answer critical questions with a
  realistic prototype tested with real users within a timebox.
- Eric Ries, [The Lean Startup principles](https://theleanstartup.com/principles):
  treat an MVP as an experiment and use validated learning rather than output volume.
- Nielsen Norman Group, [Paper Prototyping](https://www.nngroup.com/articles/paper-prototyping/):
  low-cost prototypes can reveal important usability problems before code is written.

## 4. Roadmap

Status: `Agreed` (2026-11-06)

**Scope:** product-level roadmap. It defines the product direction, the current
version, and later direction. It is not a feature-level release plan or task list.
Feature behavior and acceptance criteria belong in a PRD or Spec; implementation
tasks belong to the Agent session and, only when necessary, `tasks.md`.

| ID | Activity | Answers | Core output | Boundary |
| --- | --- | --- | --- | --- |
| 4.1 | Define product direction and the current-version goal | Where is the product going, and what user or business result should this version achieve? | Product direction, current-version goal and success measures | Does not write a feature list; does not replace the product brief in `product.md` |
| 4.2 | Define the current-version scope | Which product capabilities form the smallest complete, valuable and verifiable version? | MVP/current-version scope, priority rationale, non-goals, dependencies and risks | Does not write detailed acceptance criteria; does not break work into implementation tasks |
| 4.3 | Plan later versions | What may come next, and how much confidence do we have? | Later version themes or directions, confidence and key assumptions | Does not promise future features or dates |

### Rationale and boundaries

- Roadmap is product-level. A single roadmap version may contain several work
  objectives; a single feature normally belongs in a PRD or Spec, not in the Roadmap.
- 4.1 defines the outcome and success measures before scope. Roadmap is not a list of
  features looking for a justification.
- 4.2 selects the smallest **complete, valuable and verifiable** product increment, not
  the smallest number of features. It records explicit non-goals, dependencies, risks
  and necessary enabling work such as security, operations or data migration.
- 4.3 uses confidence rather than false precision. Dates appear only when they are real
  external constraints. Now–Next–Later is an optional confidence view, not a required
  format.
- Recording `roadmap.md` is a shared output of 4.1–4.3, not a separate activity. Human
  confirmation of the current-version scope is an exit condition, not a fourth step.
- When the product is small or the scope is already obvious, use a short Roadmap note
  or a single version. Do not create later versions merely to fill a template.
- Update the Roadmap when product direction, version scope or priorities change. Routine
  feature-level changes belong in the relevant Spec and do not require a Roadmap rewrite.
- Planned content is not proof of implementation. `features/` remains the authority for
  accepted, implemented behavior.

### Sources consulted

The decomposition was checked against the following public practices. They informed
the boundary choices but are not normative for CoolFlow:

- ProdPad, [Now–Next–Later Roadmap](https://www.prodpad.com/blog/now-next-later-roadmap/):
  organize by confidence rather than dates; avoid treating future items as commitments.
- Teresa Torres, [Product Roadmaps](https://www.producttalk.org/product-roadmaps/):
  the Roadmap should reflect current knowledge, with solutions now, opportunities next
  and outcomes later.
- ProductPlan, [The Ultimate Guide to Product Roadmaps](https://www.productplan.com/learn/what-is-a-product-roadmap/):
  a Roadmap communicates product direction and strategy, not a finished product; include
  necessary technical and operational work.
- Impact Mapping, [Impact Mapping](https://www.impactmapping.org/): connect goals,
  actors, impacts and deliverables so that scope remains tied to outcomes.

## 5. UI Prototype

Status: `Agreed` (2026-11-06)

**Scope:** design the current product version's key flows, visual direction, key screens
and states, and a clickable prototype. This stage is not a full design system,
production UI or Spec. Visual direction is a distinct activity, not an implicit part of
drawing screens.

| ID | Activity | Answers | Core output | Boundary |
| --- | --- | --- | --- | --- |
| 5.1 | Define design goals and constraints | Which user tasks must this version support, and what platform, brand, technical and accessibility constraints apply? | Design goals, key tasks, platform and constraints, design principles | Does not redefine Roadmap scope; does not design technical architecture |
| 5.2 | Design user flows and information architecture | How do users complete key tasks, and how are screens and navigation organized? | User flows, information architecture and key-screen inventory | Does not start with visual detail; does not write implementation code |
| 5.3 | Explore visual direction | What should the product look and feel like, and which direction best fits the users and brand? | Two or three visual directions using style tiles, mood boards or representative screens; selected direction and rationale | Not a complete design system; not every final screen |
| 5.4 | Create interfaces and an interactive prototype | How does the chosen direction apply to key screens, states and interactions? | Key screens, empty/loading/error/success states, clickable prototype and notes | Not production code; no real backend; does not replace the Spec |
| 5.5 | Review and usability validation | Can users understand and complete key tasks, and does the visual direction support the goals? | Design review record, task-based usability findings, revised prototype and open questions | Not final acceptance; does not treat internal opinion as user evidence |

### Rationale and boundaries

- 5.1 consumes the current-version scope from the Roadmap. It records target users,
  key tasks, platform, existing brand or design system, accessibility needs and material
  technical constraints.
- 5.2 designs flows and structure before visual detail. Wireflows or equivalent artifacts
  can show tasks, navigation, screen changes and system feedback when static wireframes
  are insufficient.
- 5.3 makes visual direction explicit. Explore two or three directions when the choice
  materially affects the product; use style tiles, mood boards or representative screens
  to compare colour, typography, spacing, iconography, illustration and motion. Reuse an
  existing brand or design system where one exists. A full design system is usually not a
  good investment for a prototype.
- 5.4 applies the selected direction to key screens and states, then connects them into a
  clickable prototype. Simulated data and interactions must be identified as such.
- 5.5 combines design review with task-based usability testing. Use target users where
  possible; a small qualitative sample can reveal major issues, but it is not statistical
  proof. If visual direction is itself a key risk, test comprehension and brand perception
  rather than only asking whether users like it.
- Routine changes may reuse existing patterns and skip formal visual exploration. Record
  why. Do not create a full design system or every edge-case screen merely to fill a
  template.
- Outputs belong in `docs/work/<objective>/prototypes/`. Complex design decisions may be
  recorded in optional `design.md`; no new mandatory UI document is introduced.

### Sources consulted

The decomposition was checked against the following public practices. They informed
the boundary choices but are not normative for CoolFlow:

- A List Apart, [Style Tiles and How They Work](https://alistapart.com/article/style-tiles-and-how-they-work/):
  style tiles explore visual language between a mood board and a full mock-up.
- Nielsen Norman Group, [5 Principles of Visual Design in UX](https://www.nngroup.com/articles/principles-visual-design/):
  scale, hierarchy, balance, contrast and Gestalt affect usability, emotion and brand.
- Nielsen Norman Group, [Design Systems 101](https://www.nngroup.com/articles/design-systems-101/):
  design systems combine style guides, component libraries and pattern libraries; a full
  system is usually not a short-term prototype investment.
- Nielsen Norman Group, [Wireflows](https://www.nngroup.com/articles/wireflows/):
  combine screen designs with task flows for dynamic interfaces.
- Nielsen Norman Group, [Prototype Fidelity](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/):
  choose prototype fidelity according to the question being tested.
- Nielsen Norman Group, [Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/):
  observe target users completing realistic tasks; small qualitative studies reveal major
  problems but are not statistical proof.

## 6. Design Spec Loop

Status: `Agreed` (2026-11-06)

**Scope:** create one implementable, verifiable and reviewable Spec for the selected
increment. The Spec carries requirements, observable acceptance criteria, technical
solution, optional tactical domain design, implementation strategy and verification.
This stage is not a PRD, implementation, task checklist or final acceptance. Code review
and acceptance belong to later stages.

| ID | Activity | Answers | Core output | Boundary |
| --- | --- | --- | --- | --- |
| 6.1 | Clarify requirements and acceptance criteria | What observable behavior is required, and which rules, examples and failure cases must hold? | Goals/non-goals, user behavior, acceptance criteria, key examples and open questions | Does not prescribe the technical solution; does not mix implementation detail into acceptance |
| 6.2 | Investigate the existing system and constraints | What existing code, data, interfaces, architecture and decisions constrain the solution? | Relevant code/data, interfaces, constraints, reusable patterns and risks | Does not rewrite the entire system; is not a review of newly written code |
| 6.3 | Design the solution and draft the unified Spec | How will it be implemented, what alternatives and trade-offs exist, and how will it be verified? | Unified `spec.md`: technical design, optional tactical domain design, implementation strategy, verification plan, trade-offs and assumptions; optional `design.md` | Does not write implementation code; does not require a task list; does not duplicate a PRD |
| 6.4 | Review and revise the design | Is the design complete, feasible, testable and not overengineered? | Review record, revised Spec, resolved or explicitly retained blockers | Not code review; not final acceptance |

### Rationale and boundaries

- 6.1 clarifies behavior with rules, concrete examples and questions. Acceptance criteria
  should be observable and testable. Open questions remain explicit rather than being
  silently converted into assumptions.
- 6.2 reads the existing system for design feasibility. This is not the same as reviewing
  code newly produced for the current task; code review belongs to the Implementation
  Loop.
- 6.3 designs the solution and drafts the unified Spec. It records meaningful alternatives,
  trade-offs, failure cases, implementation strategy and verification. A separate
  `design.md` is optional when the technical detail is too large for the Spec.
- Tactical domain design is an optional checkpoint inside 6.3, not a separate activity.
  Use it when the domain has non-trivial invariants, state transitions, cross-object
  consistency or multiple bounded contexts. Record aggregates, entities and value objects,
  where invariants are enforced, domain events, repository/service responsibilities and
  transaction boundaries. Update `docs/domain.md` only when durable domain understanding
  changes; record consequential architecture decisions as ADRs.
- `tasks.md` is optional. The coding Agent normally manages tasks in its session; create a
  persistent task file only when work must survive across sessions, agents or time.
- 6.4 reviews the design before significant implementation. Use an independent reviewer
  for novel, complex, risky or irreversible work; use a lightweight checklist for small
  changes. Resolve material blockers; product-critical trade-offs remain human decisions.
- Maintain one authoritative Spec. Optional PRD, design and task documents must be linked,
  not duplicated. A small fix may use a concise Spec or checklist rather than every
  section of the template.

### Sources consulted

The decomposition was checked against the following public practices. They informed
the boundary choices but are not normative for CoolFlow:

- GitHub, [Spec Kit](https://github.com/github/spec-kit): spec-driven development connects
  a specification to planning, tasks and implementation while keeping review points.
- OpenSpec, [OpenSpec](https://github.com/Fission-AI/OpenSpec): a change can carry proposal,
  specs, design and tasks; the workflow is iterative rather than a rigid phase gate.
- Cucumber, [Introducing Example Mapping](https://cucumber.io/blog/bdd/example-mapping-introduction/):
  rules, examples and questions clarify acceptance criteria before development.
- ADR GitHub organization, [Architectural Decision Records](https://adr.github.io/):
  capture consequential decisions with their context, rationale, trade-offs and consequences.

## 7. Implementation Loop

Status: `Agreed` (2026-11-06)

**Scope:** implement the approved Spec in small verifiable increments; test the behavior,
review the changed code and Spec conformance, fix defects and record evidence. This stage
does not perform final human acceptance or release, and it does not redesign the Spec
silently.

| ID | Activity | Answers | Core output | Boundary |
| --- | --- | --- | --- | --- |
| 7.1 | Implement the smallest verifiable increment | How can the Spec be implemented in small steps while keeping the code runnable? | Working code changes, necessary tests and version checkpoints | Does not expand the approved Spec; does not refactor unrelated code |
| 7.2 | Test and verify behavior | Does the code satisfy the acceptance criteria, including normal, boundary and failure paths? | Automated test results, build/lint/type-check results and necessary manual evidence | Does not treat compilation as behavior verification; does not skip failing tests |
| 7.3 | Review the code and Spec conformance | Is the change correct, secure and maintainable, and does it match the approved Spec? | Code review findings, Spec-conformance check and identified issues | Not a repeat of design review; not final acceptance |
| 7.4 | Fix, re-verify and record evidence | Are the issues actually resolved, and what remains unverified? | Fixed code, re-verification results, evidence and unresolved issues | Does not apply surface patches; does not silently rewrite requirements to fit the code |

### Rationale and boundaries

- 7.1 works in small increments that keep the system runnable and testable. Avoid
  accumulating a large unverified change. Use version-control checkpoints when they
  reduce risk; do not mix unrelated refactoring into the task.
- 7.2 runs the relevant automated tests and, where available, build, lint and type checks.
  Cover normal, boundary and failure paths. Use manual verification where automation
  cannot establish the observable behavior.
- 7.3 reviews the new diff, not the entire codebase. Review both code quality and Spec
  conformance: correctness, security, readability, maintainability, regressions, tests
  and documentation, plus the approved acceptance criteria. An independent reviewer or
  subagent is optional when the change is large or risky.
- 7.4 finds the root cause before fixing. If the implementation is wrong, fix it and
  re-run the relevant checks. If the Spec is wrong, return to the Design Spec Loop instead
  of silently changing requirements. If two fixes fail against the same check, verify the
  underlying assumption rather than continuing to patch.
- TDD is optional. Use Red–Green–Refactor when it suits the change; do not force it onto
  exploratory or trivial edits. Use the project's existing test, build and CI commands.
- Tasks normally live in the Agent session. Create `tasks.md` only when progress must
  persist across sessions, agents or time.
- Record direct evidence: commands, key output, test results, screenshots or logs. Keep
  **tested**, **human accepted** and **released** distinct.

### Sources consulted

The decomposition was checked against the following public practices. They informed
the boundary choices but are not normative for CoolFlow:

- Google, [Code Review](https://google.github.io/eng-practices/review/): reviewers examine
  design, functionality, complexity, tests, naming, comments, style and documentation.
- Martin Fowler, [Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html):
  Red–Green–Refactor is a way to build self-testing code and think about interfaces before
  implementation.
- Martin Fowler, [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html):
  integrate frequently, automate the build and tests, and fix broken builds immediately.
- CoolFlow, [Prove It Works](golden-rules.md): require direct, reproducible evidence rather
  than an Agent's completion claim.

## 8. Human Acceptance → Documentation Sync → Release

Status: `Agreed` (2026-11-06)

**Scope:** a human decides whether to accept the actual result; accepted behavior is
recorded in durable project documentation; a release is separately prepared, authorized,
executed and verified when applicable. Acceptance does not imply release, and release
is never inferred from implementation or documentation sync.

| ID | Activity | Answers | Core output | Boundary |
| --- | --- | --- | --- | --- |
| 8.1 | Inspect the result and make the human acceptance decision | Does the actual behavior and evidence meet the agreed goals and acceptance criteria? Does the human accept it? | Human decision: accept, request changes, or revisit design; known limitations | An Agent cannot accept its own work on the human's behalf; acceptance does not authorize release |
| 8.2 | Sync accepted facts and selectively archive work | After acceptance, which current project facts and work records need updating or preservation? | Updated `features/` and affected project docs; selected work evidence in the archive | Record only actual accepted behavior; sync does not wait for release |
| 8.3 | Prepare the release and obtain authorization | What will be released, are the required safeguards ready, and has release been authorized? | Release scope/version, notes, deployment/data-change checks, monitoring and recovery plan, explicit authorization | Readiness checks are not release execution; acceptance and release authorization are separate |
| 8.4 | Execute the release and verify its operation | Was the authorized release published/deployed, and is it operating as expected? | Actual release status, smoke-check/monitoring evidence, continue/stop/rollback decision | Use canary or staged rollout when risk warrants; post-release feedback enters the Evolution Loop |

### Rationale and boundaries

- 8.1 is a human decision based on observed behavior and evidence against the Spec, not
  an Agent completion statement. In a small project, the human requester or product owner
  may make the decision after inspecting the result. Complex or business-critical work may
  involve representative users in acceptance testing, but a formal UAT ceremony is not
  required for every change.
- If the human requests a code change, return to Step 7. If the requirements or design
  themselves need reconsideration, return to Step 6. Do not record unaccepted behavior in
  `features/` as current truth.
- 8.2 follows acceptance and does not wait for production release. Update `features/` with
  accepted implemented behavior; update product, domain, roadmap, architecture and
  feature-map records only when affected. Preserve important Specs, decisions and
  verification evidence; do not archive every temporary file.
- 8.3 distinguishes release readiness from permission to release. Preparation may include
  the exact scope/artifact, release notes, migrations and data handling, security or
  operational checks, monitoring, recovery and rollback. Explicit human authorization is
  required before an authorized release is executed. If release is not applicable or is
  deferred, record that state accurately.
- 8.4 executes only the authorized release and checks the resulting system. Use smoke tests,
  monitoring and a risk-proportionate staged/canary rollout where available. Record the
  actual version, time, status and unresolved issues. If checks fail, stop or roll back
  according to the prepared recovery plan; do not claim a successful release without
  evidence.
- Post-release feedback is an input to the cross-stage Evolution Loop, not another
  mandatory activity in every release.

### Sources consulted

The decomposition was checked against the following public practices. They informed
the boundary choices but are not normative for CoolFlow:

- Scrum.org, [Definition of Done](https://www.scrum.org/resources/what-definition-done):
  shared quality criteria describe when an increment is complete; CoolFlow keeps that
  distinct from a human's acceptance decision and release authorization.
- Google SRE Workbook, [Canarying Releases](https://sre.google/workbook/canarying-releases/):
  a canary is a partial, time-limited rollout evaluated before deciding whether to proceed.
- GitHub Docs, [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
  and [Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository):
  releases package a tagged iteration with notes and optional downloadable artifacts.
- Martin Fowler, [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html):
  production release is a business decision, separate from code integration.
- TestMonitor, [The Complete Guide to User Acceptance Testing](https://www.testmonitor.com/blog/the-complete-guide-to-user-acceptance-testing-uat):
  acceptance activities compare realistic user workflows against requirements, capture
  findings and record stakeholder approval; this is a commercial guide, not a CoolFlow
  requirement.

## Evolution Loop

The Evolution Loop is cross-stage. Its activity boundaries will be discussed after
the eight stages, without treating it as a ninth stage or a post-release-only step.

## Change log

| Date | Change |
| --- | --- |
| 2026-11-03 | Created the document skeleton and writing conventions. |
| 2026-11-05 | Agreed the Stage 1 activity boundaries and added supporting rationale. |
| 2026-11-05 | Agreed the Stage 2 initial-domain-discovery boundaries; deferred tactical design to Step 6. |
| 2026-11-05 | Clarified that Stage 1 user/problem discovery includes proportionate user research. |
| 2026-11-06 | Agreed the Stage 3 time-boxed validation boundaries. |
| 2026-11-06 | Agreed the Stage 4 product-level Roadmap boundaries. |
| 2026-11-06 | Agreed the Stage 5 UI Prototype boundaries, including explicit visual direction. |
| 2026-11-06 | Agreed the Stage 6 unified-Spec boundaries, with tactical domain design as an optional checkpoint. |
| 2026-11-06 | Agreed the Stage 7 implementation, verification, review and evidence boundaries. |
| 2026-11-06 | Agreed the Stage 8 acceptance, documentation sync, release authorization and verification boundaries. |
