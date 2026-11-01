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

**新项目——让 Agent 帮你安装 CoolFlow Init**

打开你平时使用的 Coding Agent（例如 Codex、Claude Code、OpenCode），把下面这段话直接复制给它：

```text
请帮我给当前正在使用的 Agent 安装 CoolFlow Init Skill。

Skill 地址：
https://github.com/CooLingLab/CoolFlow/tree/main/skills/coolflow-init

请识别当前 Agent 支持的 Skill 安装机制，以及官方支持的全局/用户级 Skills 目录。将整个 coolflow-init/ 文件夹安装到该全局目录，保留文件夹名称和完整内容。选择当前环境下最可靠的方式：Agent 原生安装、Skills 安装工具，或从 GitHub 下载并复制。

不要安装到当前项目或工作区。

安装后，请检查实际安装路径，并验证当前 Agent 是否能够发现这个 Skill，然后告诉我如何调用它。只安装，不要执行 Skill，不要初始化当前项目，也不要修改任何项目文件。如果当前 Agent 不支持全局安装，或者无法验证安装结果，请明确告诉我原因和最简单的下一步；不要猜测安装路径，也不要声称安装成功。

```

**安装完成后**，打开一个全新的空项目目录，告诉 Agent：

> 使用 coolflow-init 初始化这个空项目。

Skill 会先检查目标目录；如果存在其他文件或文件夹（包括隐藏文件），就会拒绝执行。通过检查后，它会创建 CoolFlow 项目文档结构、验证结果，然后停止，不会自动开始 Brainstorm 或编写应用代码。

手动安装和其他备用方式请查看 [Getting Started](GETTING_STARTED.md)。

**已有项目——先检查现状再采用**

不要在已有项目或非空目录中使用 `coolflow-init`。请按照[已有项目采用指南](GETTING_STARTED.md#b-existing-project--inspect-before-adopting)，先检查现状、提出选择性采用方案，并在获得确认后再修改文件。

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
