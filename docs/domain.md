# CoolFlow domain

Maintainer reference for developing this repository: its layers, who acts in each, and the words that mean different things in different layers. It is not a target-project document and is never copied into one.

When a word could belong to more than one layer, name the layer.

## Domain scope and participants

CoolFlow work spans three layers (see [Domain boundaries](#domain-boundaries)). Each has its own people and Agents:

| Participant | 中文 | Layer | Role |
| --- | --- | --- | --- |
| Maintainer | 框架维护者 | CoolFlow source | The human who develops CoolFlow and decides what it recommends. |
| Maintainer Agent | 维护 Agent | CoolFlow source | The Agent working in this repository, governed by the root [AGENTS.md](../AGENTS.md). |
| Project owner | 项目负责人 | Target project | The human who runs a project with CoolFlow: makes its product decisions, accepts its changes and owns its acceptance policy. |
| Project Agent | 项目 Agent | Target project | The coding Agent in a target project, governed by that project's `AGENTS.md`. |
| Operator | 操作者 | Validation | Runs a scenario: builds fixtures, sends the requests and plays the project owner. |
| Executor | 执行 Agent | Validation | Plays the project Agent inside a fixture, without CoolFlow source, the scenario or the maintainer's instructions in its context. |
| Scenario reviewer | 场景评审 Agent | Validation | Judges each scenario criterion as PASS, FAIL or NOT VERIFIED from evidence, independently of the executor and operator. |

## Domain boundaries

1. **CoolFlow source (框架源):** this repository. [`methodology/`](../methodology/), [`standards/`](../standards/) (the normative source), [`templates/`](../templates/), [`skills/`](../skills/), [`flowecosystem/`](../flowecosystem/), [`scripts/`](../scripts/) and the root `AGENTS.md`. Its product is guidance that people and Agents apply to target projects.
2. **Target project (目标项目):** an application repository that uses CoolFlow. `coolflow-init` creates one from an empty directory; an existing repository adopts CoolFlow through the inspect-first process in [Getting Started](../GETTING_STARTED.md#b-existing-project--inspect-before-adopting). It holds its own copies, such as `AGENTS.md`, `docs/documentation.md`, `docs/coolflow.yml` and `docs/development-flow.md`, plus its own product, domain, roadmap, features and `docs/work/` records. After initialization it does not need the CoolFlow repository.
3. **Validation (验证层):** [`flowreviews/`](../flowreviews/) in this repository. A fixture is a disposable target project built from the current templates in a temporary directory. Nothing in this layer is copied into a real target project.

Direction: CoolFlow source reaches a target project only through initialization, adoption and installed CoolFlow Skills. Validation builds fixtures from the source and observes how project Agents behave in them.

## Ubiquitous language

Terms that change meaning across layers:

- **`AGENTS.md`:** in the source, the root file binds the maintainer Agent, and [`templates/project/AGENTS.md`](../templates/project/AGENTS.md) is template text. In a target project, its copy binds the project Agent; "rule 5" means a numbered rule in that copy.
- **Documentation standard (文档标准):** in the source, [`standards/documentation.md`](../standards/documentation.md) is normative; [`templates/project/docs/documentation.md`](../templates/project/docs/documentation.md) must match it, and the docs-review Skill carries a snapshot. In a target project, `docs/documentation.md` is the project's local standard and may diverge.
- **`standards/` and the `standard` tier:** the directory of normative documents versus the middle acceptance tier in a target project. Write "the standard" or "`standards/`" for the first and "`standard` tier" for the second.
- **Tests and checks (测试与检查):** in the source, [`scripts/check_docs.py`](../scripts/check_docs.py) and its CI check CoolFlow's own files. In a target project, tests and CI are the project's own. In validation, `flowreviews/checks/` and the scenario reviewer judge scenarios.
- **Acceptance (验收):** exists only in a target project: the project owner accepts a change (`accepted`), or the project's declared policy does (`accepted_by_policy`). A scenario PASS is evidence about CoolFlow, not acceptance of a fixture's change.
- **Review (评审):** design review and code review are activities inside a target project's Loops, defined by [`standards/reviews.md`](../standards/reviews.md). A scenario review is the validation layer's judgment of a run.
- **Spec and work record:** exist only in a target project, under `docs/work/<objective>/`. [`templates/work/`](../templates/work/) in the source holds examples; it is not copied by initialization.
- **`domain.md`:** this file describes CoolFlow's own domain. A target project's `docs/domain.md` describes that project's domain.
- **Skill:** source lives under `skills/`; an installed Skill runs in an Agent host and acts on a target project.

## Core concepts, rules and invariants

- A rule binds whoever reads the file it lives in: root `AGENTS.md` binds the maintainer Agent, text under `templates/` binds project Agents once copied, and scenario files bind operators and reviewers. Decide a rule's layer before deciding its wording.
- CoolFlow defines contracts; target projects implement them. CoolFlow ships guidance, templates and optional Skills, not runtimes or code a project must install or run. Enforcement that depends on a project's language, tests or hosting, such as CI checks or branch protection, belongs to the target project.
- Decisions inside a target project belong to its project owner. The maintainer decides only what CoolFlow recommends; for example, CoolFlow defines the acceptance tiers, and each project owner decides whether to declare a policy and what it contains.
- `flowreviews/`, the root `AGENTS.md` and this file never reach a target project.
- In validation, the executor sees only its fixture and the operator's requests; the operator speaks for the project owner.

## Open questions

None recorded. The `low` acceptance check is a command the target project declares and owns (`acceptance.low_check`); CoolFlow defines what it should cover.
