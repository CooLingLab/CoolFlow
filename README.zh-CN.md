# CoolFlow

[English](README.md) | **简体中文**

**by Cooling · 面向 AI 辅助软件开发的 SOP**

**一位飞行员的 AI 软件开发方法。**

> 一位飞行员，将航空 SOP 中的金科玉律、态势感知与安全理念引入 AI 软件开发，探索如何让个人开发者在充分利用 AI 的同时，始终掌握项目的优先级、实际状态、恢复能力与验证结果。

CoolFlow 由 **Cooling** 创建，灵感来自 **空客飞行员金科玉律（Airbus Golden Rules for Pilots）** 与航空标准操作程序（SOP）。这些思想被独立改编为**人类主导、AI 辅助的软件开发方法**；它不是空客官方的软件开发规范，也不代表空客认可本项目。

CoolFlow 以**一个 Development Flow、三个自适应 Loop，以及轻量文档规范**，帮助开发者在产品全生命周期中明确目标、制定设计、验证成果、保存重要知识。

CoolFlow **不是** Agent Harness、工作流引擎或强制安装的 Skills 集合。

> **当前状态：v0.1 开发草案。** 仍在评审和完善中，并非正式发布版本。

## CoolFlow Golden Rules

**[AI 辅助软件开发的四条金科玉律](methodology/golden-rules.zh-CN.md)**  
*By Cooling · Creator of CoolFlow*

这是面向**人类开发者**的判断原则；即使不使用完整的 CoolFlow 方法论，也可以独立采用：

1. **Keep It Working → Ship Small → Improve** — 保护已有正确行为、小步交付、持续改进。
2. **Know the Actual State** — 区分计划、实际变更、已验证、人工验收和已发布状态。
3. **Keep a Way Back** — 保留可靠的版本检查点及真正可行的恢复方案。
4. **Prove It Works** — 以实际运行与可复查证据验证成果，不依赖 AI 自述。

Golden Rules 是对人的提醒，**不是新的 AI 强制命令或开发阶段**。Agent 的具体执行约束应由目标项目的 `AGENTS.md` 承担。

## 开发模型

**一个 Development Flow（灵活、按需采用）**

1. Idea → Brainstorm：厘清用户、问题与核心价值。
2. 轻量战略 DDD：统一领域语言、核心概念与边界。
3. Concept Prototype → Validation：快速验证关键体验与假设。
4. Roadmap：明确 MVP 与后续版本。
5. UI Prototype：制作当前版本的交互原型。
6. Design Spec Loop：编写统一 Spec，按需审查、修订。
7. Implementation Loop：编码、测试、代码审查、核对 Spec、修复。
8. Human Acceptance → Documentation Sync → Release：人工验收、同步文档、发布。

**三个自适应 Loop**

- **Design Spec Loop（第 6 步）：** 编写统一 Spec → 按需独立评审 → 修订与复审。
- **Implementation Loop（第 7 步）：** 实现 → 测试 → 代码审查 → 核对 Spec → 修复并重复。
- **Evolution Loop（跨阶段）：** **任意一步**获得新证据或发现原有假设不成立 → 重新审视相关决策 → 回到**任意需要重新处理的步骤**；不要求先发布、不强制更新 Roadmap，也没有固定起点。

普通设计修订或代码修复属于对应的质量 Loop；当新的认知需要改变产品方向、范围或关键假设时，才使用 Evolution Loop。**Documentation Sync 是人工验收后的步骤，并非第四个 Loop。** 小型修复不必机械走完八个阶段。

## Getting Started · 如何使用

**从 [Getting Started 英文完整指南](GETTING_STARTED.md) 开始。** 指南提供可以直接复制给 Coding Agent 的提示词，覆盖新项目初始化、启动实际需求、Spec、实施与验证、人工验收，也包括已有项目的使用方法。

不要求安装任何 Skill、特定 Agent 或 Dashboard。只需让 AI 在**目标应用仓库**中读取 [Flow](methodology/flow.md)、[Loops](methodology/loops.md)、[文档规范](standards/documentation.md) 和 [初始化约定](standards/initialization.md)。

首次使用可以这样说：

> 请阅读 CoolFlow 开发规范，检查当前目标仓库并补齐缺失的 `AGENTS.md`、`README.md`、`docs/product.md`、`docs/roadmap.md`、`docs/domain.md` 及相关目录。保留所有已有文件，**只初始化，不写 App 代码、不安装依赖、不决定 MVP、不创建 `docs/work/001-mvp/`**。报告实际创建、已存在及无法验证的内容。如果读不到规范，请停止并说明。

初始化后，**另行明确要求**进行 Idea/Brainstorm 或某项开发。只有正式开始探索首个开发目标时，才按需建立 `docs/work/001-mvp/`。

[`coolflow-init` 可选 Skill](skills/coolflow-init/SKILL.md) 只用于方便地初始化文档骨架，权威依据仍是标准文档。

## Reusable document templates · 项目文档模板

当你在一个 App 项目中使用 CoolFlow，最终得到的是下面这套**属于你自己的项目文档结构**。这里展示的是使用者的 App，而不是 CoolFlow GitHub 仓库自身的目录。可选文件只有在确实需要时才创建。

```text
<your-app>/
├── AGENTS.md                         # 项目级 Agent 指令
├── README.md                         # 面向人类的项目入口
└── docs/
    ├── product.md                    # Product Brief：产品定义，不是 PRD
    ├── roadmap.md                    # MVP 与后续版本规划
    ├── domain.md                     # 领域语言、边界与规则
    ├── features/                     # 已实现、已验收的功能
    │   └── <feature>.md              # 功能验收后添加
    ├── work/
    │   ├── <objective>/              # 真正开始一项开发工作时创建
    │   │   ├── spec.md               # 默认统一 Spec
    │   │   ├── prd.md                # 可选：复杂的产品需求
    │   │   ├── design.md             # 可选：深入的技术设计
    │   │   ├── tasks.md              # 可选：需要持久化的任务进度
    │   │   └── prototypes/           # 可选：交互原型
    │   └── archive/                  # 已完成工作的精选历史证据
    ├── solutions/                    # 可选：经过验证、可复用的工程经验
    │   └── <solution>.md
    ├── architecture.md               # 可选：当前系统架构
    ├── adr/                          # 可选：重要架构决策记录
    │   └── <number>-<decision>.md
    └── feature-map.md                # 可选：UI 导航与验证指南
```

### 哪些文件什么时候创建？

| 时机 | 文件与目录 |
|---|---|
| **项目初始化** | `AGENTS.md`、`README.md`、`docs/product.md`、`roadmap.md`、`domain.md`，以及空的 `features/`、`work/`、`work/archive/` 目录 |
| **真正开始开发时** | 默认创建一个 `docs/work/<objective>/spec.md` |
| **确实需要时** | `prd.md`、`design.md`、`tasks.md`、`prototypes/`、`architecture.md`、`solutions/`、`adr/`、`feature-map.md` |
| **出现经过验证、值得复用的工程经验时** | 再创建可选的 `docs/solutions/`，不为了拥有知识目录而创建 |
| **做出重要架构或技术决策时** | 再创建可选的 `docs/adr/`，每项决策单独记录 |

**Product Brief 不等于 PRD。** `docs/product.md` 是整个产品长期维护的简洁定义，回答产品为什么存在、服务谁、提供什么价值以及边界在哪里。可选的 `prd.md` 属于某一项具体开发工作，描述这一轮的用户需求、范围和产品层面的成功标准。统一 Spec 则进一步定义精确行为、实现方式和验证标准。

**经验存储在哪里？** `docs/solutions/` 是可选的工程经验库，保存经过验证、非显而易见、长期有用且值得复用的工程知识，设计思路参考 Compound Engineering。已完成工作的历史证据保存在 `docs/work/archive/`；重要架构决策的原因保存在 `docs/adr/`；只有 Agent 必须长期遵守的高优先级稳定规则才进入 `AGENTS.md`。Solutions 和 ADR 不同：前者沉淀可复用的工程发现，后者记录项目为什么做出重要技术选择。两者都不在初始化时创建，也不要求每次功能开发或 Bug 修复后都创建。

对应的可复用源模板按用途组织：

- [Project skeleton](templates/project/)：初始化所需的 `AGENTS.md`、`README.md` 和核心文档。
- [Work templates](templates/work/)：统一 Spec，以及可选的 PRD、Design、Tasks。
- [Optional templates](templates/optional/)：[Feature Map](templates/optional/feature-map.md)、[Feature 文档模板](templates/project/docs/features/feature-template.md)、[Solutions 经验规范与模板](templates/optional/solutions/README.md)、[ADR 模板与示例](templates/optional/adr/README.md)。

这是一套轻量默认结构，不是必须逐项打勾的清单。已有项目可以保留自己的结构，只采用真正有帮助的部分。

## 开发与发布

当前仍是 **v0.1 开发草案**。内部场景验证和真实项目测试尚未完成，不能宣称已通过。测试文件将在实际验证完成、准备正式发布时移除；正式发布尚未进行。

## 参考项目

- [EGM（Elephant-Goldfish Model）](https://github.com/google/elephant-goldfish-model)：独立技术设计审查。
- [GitHub Spec Kit](https://github.com/github/spec-kit)：规格驱动的软件开发。
- [OpenSpec](https://github.com/Fission-AI/OpenSpec)：开发中的变更与已接受规范。
- [Agent Skills](https://agentskills.io/specification)：通用 Skill 格式。

CoolFlow 参考这些思想，但不强制依赖它们。

**翻译说明：** [英文 README](README.md) 及英文 [Golden Rules](methodology/golden-rules.md) 为权威版本；中文用于方便理解与传播。如有不一致，以英文标准为准。
