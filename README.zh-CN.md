# CoolFlow

[English](README.md) | **简体中文**

## AI 会写代码，但开发不只有写代码。

**一张面向 AI 独立开发者的轻量开发路线图。**

**让 AI 写代码，让你掌握开发方向。**

从一个模糊的想法，到一个真正能用的产品，CoolFlow 帮你理清下一步做什么、什么时候需要设计与验证，以及哪些重要信息值得保留下来。它是一套可以参考和调整的开发方法，而不是声称只有一种正确的软件开发流程。

> **当前状态：v0.1 开发草案。** 本分支仍在评审中，并非正式发布版本；真实项目和端到端场景验证尚未完成。

## 为什么需要 CoolFlow？

AI 让写代码变得前所未有的容易。你可以用自然语言生成界面、实现功能、修复 Bug，甚至独立完成过去需要多人协作的项目。

但随着项目逐渐复杂，新的问题也会出现：

- 想法很多，却不知道应该先做什么。
- AI 不断修改代码，产品方向却越来越模糊。
- 功能看起来完成了，却不知道有没有真正验证。
- 反复迭代之后，重要决策和开发经验逐渐丢失。

**会让 AI 写代码，不等于拥有一套清晰的产品开发方法。**

CoolFlow 希望填补这中间的空白：让第一次借助 AI 开发产品的人更容易上手，也为已经有自己工作流的独立开发者提供一份可灵活借鉴的参考。

## CoolFlow 是什么？

CoolFlow 是一套开放、轻量、可按需调整的 AI 辅助软件开发方法，提供三个核心部分：

| | 它能帮你做什么 |
| --- | --- |
| **一张开发路线图（Development Flow）** | 从想法探索、领域理解、原型验证与版本规划，逐步走向实现、人工验收和发布。 |
| **三个反馈循环（Adaptive Loops）** | 持续完善 Spec、验证实现，并在获得新信息时重新审视产品方向。 |
| **一套轻量文档规范（Documentation Standard）** | 保留产品目标、需求、决策与值得复用的工程经验，让你和 AI 都更容易接续工作。 |

<p align="center">
  <img src="docs/diagrams/coolflow-diagram.zh-CN.svg" alt="CoolFlow 开发流程与反馈循环">
</p>

**流程是一张地图，不是一张必须逐项打勾的清单。**

你可以跳过不需要的阶段，合并简单步骤，也可以在发现问题时回到任何相关环节。小型 Bug 修复不需要完整的产品规划；复杂的新产品则可能值得在编码前多做一些探索与验证。

**流程应该服务于开发，而不是让开发服务于流程。**

[查看开发流程](methodology/flow.md) · [了解三个反馈循环](methodology/loops.md)

## 如何开始使用？

不需要购买软件，也不需要更换熟悉的 Coding Agent、安装工作流引擎或部署 Dashboard。你可以直接用现有的工具和 GitHub 项目开始。

如果是**新项目**，可按照 [Getting Started 使用指南（英文）](GETTING_STARTED.md) 初始化必要文档、梳理想法，再确定第一个可验证的小目标；如果是**已有项目**，只采用对下一项功能或修复有帮助的部分，不必重新走一遍完整流程。

**可以先把这段话发给你的 Coding Agent：**

> 请阅读 [CoolFlow v0.1 开发草案](https://github.com/CooLingLab/CoolFlow/tree/feat/v0.1-standard-and-init)，重点了解开发方法、文档规范和 Getting Started 指南。先检查我当前项目的真实状态，帮我梳理目标和下一步最小、可验证的开发工作。开始写代码前先提出计划；保留已有文件和项目指令。如果无法读取参考资料，请明确告诉我，不要自行猜测规范。

可选的 [`coolflow-init` Skill](skills/coolflow-init/SKILL.md) 只负责初始化文档骨架，**不会自动开发 App**。方法论与规范文档才是权威依据。

## 四条 Golden Rules

CoolFlow 还整理了四条面向**人类开发者**的判断原则。即使不使用完整的开发流程，你也可以独立借鉴：

1. **Keep It Working → Ship Small → Improve** — 先保护已有正确行为，小步交付，再持续改进。
2. **Know the Actual State** — 分清计划、实际修改、已验证、人工验收和已发布。
3. **Keep a Way Back** — 保留可靠的版本检查点和真正可行的恢复方案。
4. **Prove It Works** — 用可复查的实际证据确认结果，而不是只听 AI 说“已经完成”。

它们是对人的提醒，**不是强制要求 AI 执行的四条命令**。具体的 Agent 规则应由目标项目的 `AGENTS.md` 承担。

[阅读 Golden Rules 中文版](methodology/golden-rules.zh-CN.md)

## 为什么由一位飞行员发起？

我是 Cooling，一名飞行员，也是一名 AI 独立开发爱好者。

航空领域长期使用标准操作程序（SOP）、态势感知、交叉检查和风险管理等方法，让复杂任务在变化与不确定性中保持有序。

在使用 AI 独立开发软件的过程中，我发现其中一些思想也值得借鉴：明确优先级、了解真实状态、保留恢复路径，以及用可验证的证据确认成果。

CoolFlow 的部分灵感来自航空 SOP 和**空客飞行员金科玉律（Airbus Golden Rules for Pilots）**，但它是独立形成的软件开发方法，**并非空客制定或认可的软件开发规范**。

我不打算重新发明软件工程。CoolFlow 只是尝试把有价值的实践整理得更清晰、更轻量，让更多人能理解、采用、修改并共同完善。

## 进一步了解

- [Getting Started（英文）](GETTING_STARTED.md)：新项目与已有项目的可复制提示词，以及人工验收节点。
- [开发流程](methodology/flow.md)与[反馈循环](methodology/loops.md)：完整方法说明。
- [文档规范](standards/documentation.md)与[初始化约定](standards/initialization.md)：何时生成什么文档。
- [文档模板](templates/)：Spec、Solutions、ADR 等可选模板与说明。
- [四条 Golden Rules](methodology/golden-rules.zh-CN.md)：面向开发者的判断原则。

这是一套轻量默认方法，不要求每个项目都生成全部文档，也不要求已有项目放弃原来的约定。CoolFlow **不是** Agent Harness、工作流引擎或强制安装的 Skills 集合。

### 参考与启发

CoolFlow 参考了 [EGM](https://github.com/google/elephant-goldfish-model)、[GitHub Spec Kit](https://github.com/github/spec-kit)、[OpenSpec](https://github.com/Fission-AI/OpenSpec) 和 [Agent Skills 规范](https://agentskills.io/specification) 的部分思想，但不强制依赖这些项目。

**版本说明：** 英文 [README](README.md) 与英文 [Golden Rules](methodology/golden-rules.md) 仍为规范的权威版本，中文用于方便理解与传播。若有分歧，以英文规范为准。

---

*CoolFlow by Cooling · 人类主导、AI 辅助、持续演进的独立开发方法。*
