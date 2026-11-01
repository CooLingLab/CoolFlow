# CoolFlow

[English](README.md) | **简体中文**

**AI 会写代码，但开发不只有写代码。**

CoolFlow 是面向 AI 独立开发者的轻量开发路线图，帮助你从想法走向可验证、可交付的产品。

## 为什么需要 CoolFlow？

AI 让写代码更容易，但做产品仍会遇到这些问题：

- 点子很多，不知道先做什么。
- AI 不断改代码，目标和决策却越来越模糊。
- 功能看似完成，却缺乏可靠的验证依据。

## CoolFlow 提供什么？

- **一个开发流程（Development Flow）：** 从想法探索、原型、Roadmap 到实现、验收和发布。
- **三个反馈循环（Adaptive Loops）：** 通过设计评审完善方案，通过测试与代码审查验证实现，并根据新信息持续调整产品方向。
- **轻量文档规范：** 保留目标、需求、关键决策和可复用经验。

<p align="center">
  <img src="methodology/flow-diagram.zh-CN.svg" alt="CoolFlow 开发流程与反馈循环">
</p>

流程可以按需跳过、合并或回到之前的阶段，不必机械执行。

## 快速开始

使用你现有的 Coding Agent。CoolFlow 不绑定特定 Agent 厂商或安装工具。

**新项目——初始化空目录**

CoolFlow 提供一个可选的 coolflow-init Skill，遵循开放的 [Agent Skills 规范](https://agentskills.io/specification)。按照你的 Agent 官方说明，将完整的 [skills/coolflow-init/](skills/coolflow-init/) 文件夹安装到用户级/全局 Skills 目录。不同 Agent 的安装位置和方式可能不同。

打开一个空项目目录（或仅包含根目录 .git 元数据的目录），然后告诉 Agent：

> 使用 coolflow-init 初始化这个空项目。

Skill 会在写入前检查目录；如果存在其他文件或文件夹（包括隐藏文件），就会拒绝执行。手动安装、可选的第三方安装工具和不支持 Skill 的 Agent 的手动初始化方式，请查看 [Getting Started](GETTING_STARTED.md)。

**已有项目——先检查现状再采用**

不要在已有项目或非空目录中使用 coolflow-init。请按照 [已有项目采用指南](GETTING_STARTED.md#b-existing-project--inspect-before-adopting)，先检查现状、提出选择性采用方案，并在获得确认后再修改文件。

[完整使用指南（英文）](GETTING_STARTED.md) · 探索阶段可建立工作目录；确定开发目标、进入 Design Spec Loop 时再编写正式 Spec。

## 四条 Golden Rules

CoolFlow 还整理了四条面向**人类开发者**的判断原则，部分灵感来自空客飞行员金科玉律。即使不使用完整的开发流程，你也可以独立借鉴：

1. **Keep It Working → Ship Small → Improve** — 先保护已有正确行为，小步交付，再持续改进。
2. **Know the Actual State** — 分清计划、实际修改、已验证、人工验收和已发布。
3. **Keep a Way Back** — 保留可靠的版本检查点和真正可行的恢复方案。
4. **Prove It Works** — 用可复查的实际证据确认结果，而不是只听 AI 说“已经完成”。

它们是对人的提醒，**不是强制要求 AI 执行的四条命令**。具体的 Agent 规则应由目标项目的 `AGENTS.md` 承担。

[阅读 Golden Rules 中文版](methodology/golden-rules.zh-CN.md)

## 项目缘起

CoolFlow 由飞行员 Cooling 发起。航空 SOP、态势感知和交叉检查启发我把明确优先级、掌握状态、保留退路与验证结果的思想带入 AI 辅助软件开发。

## 更多文档

- [Getting Started（英文）](GETTING_STARTED.md) — 新项目和已有项目入门。
- [开发流程](methodology/flow.md) · [反馈循环](methodology/loops.md) — 完整方法。
- [文档规范](standards/documentation.md) · [模板](templates/) — 文档约定与可复用模板。

## 生态与工具选型

CoolFlow 定义开发方法和文档规范，不绑定特定 Agent 工具链。你可以通过以下资料了解现有方案，并选择最小、合适的补充工具：

- [开发框架能力对比](flowecosystem/framework-comparison.md) — 比较主流 AI 开发框架的能力覆盖、工作流、项目状态管理与经验沉淀。
- [外部方案目录](flowecosystem/catalog.md) — 按照 CoolFlow 的开发阶段查找可借鉴的框架、Skills、方法和工具。
