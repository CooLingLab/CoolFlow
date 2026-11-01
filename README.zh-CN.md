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
  <img src="docs/diagrams/coolflow-diagram.zh-CN.svg" alt="CoolFlow 开发流程与反馈循环">
</p>

流程可以按需跳过、合并或回到之前的阶段，不必机械执行。

## 快速开始

使用你现有的 Coding Agent，根据项目情况选择入口：

**新项目——先初始化文档**

> 请阅读 https://github.com/CooLingLab/CoolFlow/blob/main/GETTING_STARTED.md 及其引用的规范。在我的新项目中，只创建缺失的 CoolFlow 文档和目录，保留已有文件。暂不进行产品探索、编写 Spec 或开发代码，并报告实际修改。

**已有项目——先检查现状**

> 请阅读 https://github.com/CooLingLab/CoolFlow/blob/main/GETTING_STARTED.md 并检查我的现有项目。针对 **[功能或修复]**，建议采用哪些 CoolFlow 步骤，以及下一项最小、可验证的工作。保留原有约定，先提出方案，不要直接修改。

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
