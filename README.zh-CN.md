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

## 文档约定

首次初始化应具备 `AGENTS.md`、`README.md`、`docs/product.md`、`docs/roadmap.md`、`docs/domain.md`，以及 `docs/features/`、`docs/work/`、`docs/work/archive/` 目录（必要时用 `.gitkeep` 占位）。

- `docs/features/`：真实实现且**已经人工验收**的功能。
- `docs/work/<objective>/spec.md`：具体开发工作开始后建立的统一 Spec；`prd.md`、`design.md`、`tasks.md` 按需可选。
- `docs/work/archive/`：按需保存完成工作的关键决策、设计与验证证据。
- `docs/feature-map.md`（可选）：方便 Agent 操作和验证实际 UI，不是重复的功能需求文档。

初始化后的项目可以独立演进，不要求绑定 CoolFlow 的上游版本。

## 仓库导航

| 路径 | 作用 |
| --- | --- |
| [Getting Started](GETTING_STARTED.md) | 英文完整入门指南与可复制提示词 |
| [methodology/](methodology/) | Flow、Loops 与 Golden Rules |
| [standards/](standards/) | 文档、初始化与审查规范 |
| [templates/](templates/) | 项目和工作文档模板 |
| [skills/coolflow-init/](skills/coolflow-init/) | 可选初始化 Skill |
| [reviews/scenarios/](reviews/scenarios/) | **仅限开发阶段**的内部场景测试，正式发布前需清理 |

独立的 CoolFlow Dashboard 未来可以可视化阶段与文档，但不负责 Agent 编排或任务执行。

## 开发与发布

当前仍是 **v0.1 开发草案**。内部场景验证和真实项目测试尚未完成，不能宣称已通过。测试文件将在实际验证完成、准备正式发布时移除；正式发布尚未进行。

## 参考项目

- [EGM（Elephant-Goldfish Model）](https://github.com/google/elephant-goldfish-model)：独立技术设计审查。
- [GitHub Spec Kit](https://github.com/github/spec-kit)：规格驱动的软件开发。
- [OpenSpec](https://github.com/Fission-AI/OpenSpec)：开发中的变更与已接受规范。
- [Agent Skills](https://agentskills.io/specification)：通用 Skill 格式。

CoolFlow 参考这些思想，但不强制依赖它们。

**翻译说明：** [英文 README](README.md) 及英文 [Golden Rules](methodology/golden-rules.md) 为权威版本；中文用于方便理解与传播。如有不一致，以英文标准为准。
