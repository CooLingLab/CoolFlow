# CoolFlow 入门指南

[English](GETTING_STARTED.md) | **简体中文**

**CoolFlow by Cooling · AI 软件开发 SOP**

[首页](README.zh-CN.md) · [English](README.md) · [Golden Rules](methodology/golden-rules.zh-CN.md)

CoolFlow 是一套轻量的**开发方法论和文档规范**，不是 Agent runner。它与现有的 Coding Agent
配合使用。可选的 coolflow-init Skill 遵循开放的
[Agent Skills 规范](https://agentskills.io/specification)；不要求特定 Agent 厂商或安装工具。

> **v0.1 草稿：** 以下说明描述预期工作流。端到端场景执行和真实项目验证**尚未完成**。

## 前提条件

你需要一个 Coding Agent 可以检查的**目标应用仓库**。它与 CoolFlow 参考仓库是分开的。

在下面选择正确的起点。coolflow-init Skill 仅用于全新的空项目目录。已有项目使用单独的“先检查
再采用”流程。

## 选择起点

### A. 新项目——初始化空目录

可选的 coolflow-init Skill 提供了一个简短、可复用的入口，用于创建 CoolFlow 文档结构。

#### 目标目录要求

目标项目根目录必须是：

- 完全为空；或
- 只包含一个根级 .git 条目，可以是目录或普通文件（Git worktree 元数据）。

Claude Code 会在它打开的每个目录中创建自己的根级 `.claude/` 目录。该目录是 Agent 元数据而非
项目内容，只要它包含的每个条目都是以下之一，就不会使目标不合格：

- `.cc-writes/`：Claude Code 的原子写入暂存目录；
- `settings.local.json`：本地权限文件。

`.claude` 文件或符号链接、`.claude/` 中的任何其他条目（例如 `settings.json`、`commands/`、
`agents/` 或 `skills/`），以及所有其他根级条目都会使目录变为非空——包括 README.md、
.gitignore、.DS_Store、CLAUDE.md、.mcp.json、其他隐藏文件、目录和符号链接。Skill 必须在不修改
任何内容的情况下拒绝运行。不要为了满足目录条件而删除文件；请选择一个新的空目录。

#### 安装 Skill——让你的 Agent 执行

打开你正在使用的 Coding Agent，并发送：

```text
请按照当前 Agent 支持的标准安装方式，将这个 Skill 安装到全局：
https://github.com/CooLingLab/CoolFlow/tree/main/skills/coolflow-init
```

Agent 应选择它支持的方法。如果无法全局安装 Skill，它应告知你，而不是猜测。

#### 其他安装方式（备用）

如果你希望自行安装：

- **Agent 原生安装：** 按照 Agent 文档安装用户级或全局 Skill。Agent Skills 规范定义格式，
  但不规定统一的安装路径。
- **手动安装：** 下载或克隆此仓库，然后将完整的 `skills/coolflow-init/` 文件夹复制到 Agent
  文档指定的全局 Skills 目录。保留文件夹名称。
- **可选的第三方安装器：** [Vercel Skills CLI](https://github.com/vercel-labs/skills) 支持多个
  Agent：

  ```bash
  npx skills add CooLingLab/CoolFlow --skill coolflow-init -g
  ```

  这是可选项，不是 CoolFlow 的依赖。该 CLI 需要 Node.js 22.20 或更高版本；此要求仅适用于
  安装器。

并非每个 Coding Agent 都支持 Agent Skills 或全局安装。如果你的 Agent 不支持，请使用其文档
指定的指令机制，或下面的手动初始化备用方案。

#### 使用 Skill

1. 在 Coding Agent 中打开一个**全新的空目标项目目录**。
2. 询问：**“使用 `coolflow-init` 初始化这个空项目。”**
3. Agent 在做任何修改前检查目标根目录——包括隐藏条目。它只忽略文档中定义的 Claude Code
   `.claude/` harness 元数据，并保持其不变。
4. 如果符合条件，它读取权威 CoolFlow 标准与模板，创建必需的项目文件，验证结果，报告结果并
   停止。它不会自动开始 Brainstorm 或编写应用代码。

如果你的 Agent 无法安装或调用 Skill，请使用以下手动初始化备用方案：

> 阅读 https://github.com/CooLingLab/CoolFlow 的 CoolFlow 仓库。先检查当前目标项目根目录，
> 包括隐藏条目。只有在忽略 Claude Code 自身的 `.claude/` harness 元数据（仅限 `.cc-writes/`
> 和/或 `settings.local.json`）后，目录为空或只包含一个根级 .git 目录/普通文件时才继续；
> 否则停止，不修改任何内容。阅读 standards/initialization.md、standards/documentation.md、
> methodology/flow.md、methodology/loops.md，以及 templates/project/ 下的必需模板。严格遵循
> 初始化契约，创建必需的文档结构，验证结果，报告结果并停止。不要开始 Brainstorm 或实现。

**空项目**中的预期骨架：

    AGENTS.md
    README.md
    docs/
      documentation.md  # 完整的项目本地文档规范
      product.md        # 简明项目级 Product Brief，不是 PRD
      roadmap.md
      domain.md
      features/
      work/
        archive/

空目录使用 .gitkeep 以便 Git 跟踪。Skill 本身**不会复制**到目标应用。

初始化后，项目遵循自己的 docs/documentation.md；后续文档工作不需要访问 CoolFlow。项目可以独立
调整该本地标准。

### B. 已有项目——先检查现状再采用

**不要在已有或非空项目中运行 coolflow-init。** Skill 会在那里拒绝运行。

相反，请让 Coding Agent 检查现有项目，并提出选择性采用计划：

> 阅读 https://github.com/CooLingLab/CoolFlow 的 CoolFlow 指南，并检查我的现有仓库，包括
> AGENTS.md、代码、架构和相关文档。总结实际项目约定，说明 CoolFlow 的哪些部分有助于
> **[具体修复、功能或开发需求]**。提出最小、有用的采用计划。保留所有现有文件、指令、代码和
> 未提交修改。**在我批准计划之前，不要修改任何内容。**

批准后，只应用已商定的变更。不要重建整个文档树、覆盖项目约定，或默认从 Idea 重新开始。继续
从当前工作相关的 CoolFlow 阶段开始。

## 继续新项目——发现阶段

**新项目初始化**后，在准备好时明确开始发现。例如：

> 让我们开始第 1 步 — Idea → Brainstorm，针对 **[产品想法]**。遵循项目本地 CoolFlow 指令，
> 引导我完成问题与用户发现、竞争格局分析、机会识别和产品假设。与我讨论重要决策。不要在
> brainstorm 期间开始实现或创建正式 Spec。

Agent 可以更新 docs/product.md（项目级 Product Brief）、docs/domain.md、docs/roadmap.md 以及
发现笔记。竞品发现通常属于 brainstorm.md；只有当研究规模大到值得独立记录时，才创建单独的
competitive-landscape.md。**在特定目标进入 Design Spec Loop（第 6 步）之前，工作目录可以没有
Spec。** 较大的目标可以使用自己的可选 docs/work/<objective>/prd.md；不要将其与项目简报混淆。
已验证、非显而易见、持久且有实质意义的工程经验，之后可以提炼到可选的 docs/solutions/；原始
工作历史留在工作项或归档中。只有当重要架构或技术决策需要保留理由时，才在可选的 docs/adr/
中记录单独的 ADR。当阶段不增加价值时，可以**跳过或合并**。

## 设计与实现选定的增量

在编写相关工作规格之前，如果可选的 docs/solutions/ 目录存在，只查阅其中相关的现有记录。默认
不要阅读整个知识库。只有当发现经过验证，并且非显而易见、持久且有实质意义时，才记录新的
Solution。

当具体增量被选定进入 **Design Spec Loop（第 6 步）** 时，询问：

> 针对 **[选定功能/增量]**，编写一份统一的 docs/work/<objective>/spec.md，包含目标与非目标、
> 可观察的验收条件、主要设计选择、实施策略和验证计划。当复杂性或风险需要时，独立评审**当前
> Spec 草稿和相关背景**；解决重要发现，并确认设计已准备好实施。然后实现**最小、完整、有价值的
> 增量**。运行相关测试，评审实际变更的代码，检查与已批准 Spec 的一致性，并处理失败。如果发现
> Spec 有误，明确重新审视设计，而不是悄悄改变需求。展示哪些内容确实可用的直接证据，并指出仍
> 未验证的内容。**请我验收结果；不要自行标记为已验收。**

**Design Spec Loop** 评估计划；**Implementation Loop** 验证代码和行为。单独的 tasks.md 是可选
的。编译成功本身并不证明功能可用。

## 人类验收、文档同步与发布

检查实际行为和证据。如果满意，明确验收增量：

> 我已检查 **[具体功能/证据]**，并 **[接受 / 请求修改]**。如果接受，只更新相关的持久文档
> （docs/features/ 用于已验收、已实现的行为），并选择性归档重要决策与验证证据。**区分已验收与
> 已发布。** 没有单独的明确指令，不要部署或发布。

只有适当时才发布。**Evolution Loop 可以在任何步骤**使用，而不仅是在发布后：反馈、新想法或
变化的需求只要值得重新考虑产品假设、范围或方向，就可以让项目回到任何相关步骤（例如，失败的
原型回到 Brainstorm）。普通的 Spec 修订或代码/测试修复仍留在本地 Design Spec 或 Implementation
Loop 中。只重新审视需要重新考虑的内容。

## 人类检查点

| 时机 | 需要确认什么 |
| --- | --- |
| 初始化 | 目标满足空目录要求；只创建了预期文件 |
| 编码前 | 目标、约束和可观察的验收条件已理解 |
| 编码后 | 实际变更和验证证据支持所声称的结果 |
| 验收前 | 局限性、数据风险和恢复选项已理解 |
| 发布前 | 已验收行为已记录；发布已单独授权 |

面向人的原则参见 [CoolFlow Golden Rules](methodology/golden-rules.zh-CN.md)。**本指南不引入任何
强制全局状态文件或 Agent 编排系统。**

**翻译说明：** 本文是英文 [Getting Started with CoolFlow](GETTING_STARTED.md) 的中文翻译。英文
是权威版本；如出现歧义，以英文为准。
