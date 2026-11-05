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
| 3. Concept Prototype → Validation | Not started |
| 4. Roadmap | Not started |
| 5. UI Prototype | Not started |
| 6. Design Spec Loop | Not started |
| 7. Implementation Loop | Not started |
| 8. Human Acceptance → Documentation Sync → Release | Not started |
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

Status: `Not started`

## 4. Roadmap

Status: `Not started`

## 5. UI Prototype

Status: `Not started`

## 6. Design Spec Loop

Status: `Not started`

## 7. Implementation Loop

Status: `Not started`

## 8. Human Acceptance → Documentation Sync → Release

Status: `Not started`

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
