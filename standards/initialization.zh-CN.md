# 项目初始化契约

[English](initialization.md) | **简体中文**

**Skill 调用方式：**“使用 coolflow-init 初始化这个空项目。”

这是**初始化，不是产品发现或实现**。

## 范围与空目录前提

coolflow-init Skill 仅用于全新的空目标项目。

- 目标根目录必须不包含任何条目，或只包含一个名为 .git 的根级条目。
- .git 条目可以是目录（普通 Git 仓库）或普通文件（Git worktree）。
- 检查所有根目录条目，包括隐藏文件。任何其他文件、目录或符号链接都会使目标变为非空。
- 如果目标非空、有歧义、不可访问或无法可靠检查，Skill 必须**在写入任何内容之前**停止。它不得
  为了满足目录条件而删除、移动、重命名或覆盖文件。
- 不要把 Skill 自身的安装目录或 CoolFlow 源仓库误认为目标项目。

此限制适用于 coolflow-init。**不要对已有项目使用该 Skill。** 请遵循
[Getting Started 中的已有项目采用流程](../GETTING_STARTED.zh-CN.md)。

## 必需结果

- 遵循[标准应用文档树](documentation.zh-CN.md#标准应用文档树)；不要在该文档树之外发明额外的
  默认文件夹或文件。
- 空目录前提通过后，创建：
  - AGENTS.md
  - README.md
  - docs/documentation.md
  - docs/product.md（项目级 Product Brief，**不是 PRD**）
  - docs/roadmap.md
  - docs/domain.md
- 使用 .gitkeep 确保 docs/features/、docs/work/ 和 docs/work/archive/ 作为仅存在于 Git 的空
  目录而存在。
- 初始化期间**不要**创建 docs/solutions/ 或 docs/adr/；两者都是可选的，只有当已验证的可复用
  发现或重要决策需要时才出现。
- 在 **AGENTS.md** 中填写简明的八阶段流程、三个 Loop 和 Agent 行为规则；文档规则引用
  docs/documentation.md。
- 将完整的 templates/project/docs/documentation.md 复制到 docs/documentation.md。初始化后它
  是项目的本地标准，可以独立演进，无需访问 CoolFlow。
- 用**模板**填写其他文档，而不是编造产品事实。如果用户提供实际事实，只填写其授权的部分；否则
  保持 Not started 或 To decide。
- **不要**创建 docs/work/001-mvp/、spec.md、PRD、原型、任务文件、应用代码、依赖项、CI 或架构
  决策。
- 对路径和必需标题运行一致性检查。报告创建的文件、任何验证限制以及下一个可选操作。停止，不
  开始 Brainstorm。

## 已有项目采用（与本 Skill 分开）

- 绝不要在非空项目中调用 coolflow-init。
- 对于已有项目，遵循 [Getting Started](../GETTING_STARTED.zh-CN.md)
  中的先检查流程。
- 先检查现有架构、指令、文档、约定和相关工作。总结实际状态，并提出最小、有用的选择性采用计划。
- 在用户批准具体计划之前，不要创建完整的 CoolFlow 文档树或修改任何文件。
- 批准后，只修改已商定的文件。保留现有内容、项目特定指令、代码和未提交工作。报告冲突，而不是
  悄悄替换任何内容。
- 采用 CoolFlow 不要求从 Idea 重新开始，也不要求采用每一个 CoolFlow 阶段。

## 模板来源与路径解析

标准模板位于 CoolFlow 源仓库的 `templates/project/`。当 coolflow-init 作为 Skill 全局安装时，
它必须在目标目录预检通过后，从权威 CoolFlow GitHub 仓库获取标准与模板。

- 不要从 Skill 安装路径、Agent 配置目录或目标项目目录推断 CoolFlow 仓库根目录。
- 不要期望 `standards/` 或 `templates/` 位于已安装 Skill 旁边或 Agent 配置目录内。
- 不要在目标应用中创建 CoolFlow `standards/` 或 `templates/` 的本地副本。只复制本契约列出的
  必需项目文件。
- 如果无法完整获取权威源文件，请在写入前停止并报告不可用的来源。

将必需文件复制到目标路径；只替换明确支持的占位符。文档模板实现[源标准](documentation.zh-CN.md)，
且不包含仅 CoolFlow 使用的文件链接；修改标准时保持两者一致。

## 验收检查

1. 六个必需文档存在，包括一份完整、无需访问 CoolFlow 即可使用的本地 docs/documentation.md。
2. 必需目录在 Git 中存在。
3. 没有创建意外的代码、依赖项、产品计划或初始工作目标。
4. Skill 接受空目录和仅包含根级 .git 元数据（目录或普通文件）的目录。
5. Skill 在任何来源查找、网络请求或写入之前，拒绝所有其他根级条目——包括隐藏文件；拒绝时保持
   目标不变，且不触发标准/模板路径搜索。
6. 已有项目采用流程先检查，在用户批准具体计划前不做任何修改。
7. 文件和报告不包含编造事实。

**翻译说明：** 本文是英文 [Project initialization contract](initialization.md) 的中文翻译。英文
是权威版本；如出现歧义，以英文为准。
