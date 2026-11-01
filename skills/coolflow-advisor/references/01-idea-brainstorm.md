# Stage 1 — Idea → Brainstorm

[精选推荐索引](recommendations.md) · [CoolFlow 文档规范](../../../standards/documentation.md)

**目标：**明确问题、用户、替代方案与产品假设；不提前创建正式 Spec。

**收录依据：**仅保留本对话已讨论的具体工具；每个任务最多两个选择。核查通过=阅读官方源码及关联依赖、确定 CoolFlow 适配方案，不等于已安装或做过受控对照测试。运行时仍需校验环境及权限。

## 1.1 产品创意发散

**何时使用：**从产品、设计和工程视角提出新产品方向。

- **首选：[brainstorm-ideas-new](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/brainstorm-ideas-new/SKILL.md)**（具体 Skill；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**生成产品/设计/工程三视角产品创意。**依赖/限制：**纯文本流程；必须先明确问题，避免未经验证的功能堆砌。**CoolFlow 适配：**保持探索笔记可选，不提前创建正式 Spec。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/brainstorm-ideas-new/SKILL.md)，Git blob `449ef41b53a1218261fb192053c56b233a28e1db`（2026-11-01）。

## 1.2 深入追问、澄清需求

**何时使用：**想法模糊、希望厘清决策和约束。

- **首选：[grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**通过决策树式追问澄清模糊需求。**依赖/限制：**入口文件只转调同仓库 `grilling`；单装入口无法执行追问方法。**CoolFlow 适配：**连同 `grilling` 安装或合并指令，不强制新建文件。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)，Git blob `3947ff9c4ad980d14fc07fccbf659d47c114e81d`（2026-11-01）。

- **备选：[brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**对设计选择逐步提问、权衡备选并确认方向。**依赖/限制：**原版有 Superpowers 文档路径和后续 `writing-plans` 交接。**CoolFlow 适配：**轻量修改路径与强制交接；保留核心问答与方案比较。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md)，Git blob `7f5eef02f894c4f24cea313660c0465ce9c084ed`（2026-11-01）。

## 1.3 创业定位与价值判断

**何时使用：**判断产品价值、目标客户和切入点。

- **首选：[office-hours](https://github.com/garrytan/gstack/blob/main/office-hours/SKILL.md)**（具体 Skill；B / L2）。**核查通过（源码与依赖检查，未实机验证）** **能力：**从创业者角度检查产品价值、目标客户及可行切口。**依赖/限制：**依赖 gstack 共享前置内容、脚本与运行环境。**CoolFlow 适配：**具备 gstack 环境时可原版运行；否则只提取提问方法，不能称原版已可运行。**核查依据：**[上游文件](https://github.com/garrytan/gstack/blob/main/office-hours/SKILL.md)，Git blob `9bc0af744558834bab5d7c1218528250f8c9599b`（2026-11-01）。

## 1.4 竞品研究与横向比较

**何时使用：**比较直接竞品、间接替代品和现有解决办法。

- **首选：[competitive-research-snapshot](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/competitive-research-snapshot/SKILL.md)**（具体 Skill；B / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**基于证据生成竞品快照、比较矩阵与决策结论。**依赖/限制：**引用同仓库 `autonomous-investigation` 与 `intelligence-collection-disciplines` 研究协议；需要实际联网来源。**CoolFlow 适配：**按需补齐文本协议；大规模研究才创建 `competitive-landscape.md`。**核查依据：**[上游文件](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/competitive-research-snapshot/SKILL.md)，Git blob `80b082f69919143a29ed8440c156bf162fea9ebe`（2026-11-01）。

- **备选：[competitor-analysis](https://github.com/browserbase/skills/blob/main/skills/competitor-analysis/SKILL.md)**（具体 Skill；B / L2）。**核查通过（源码与依赖检查，未实机验证）** **能力：**用 Browserbase 搜索和浏览器研究生成竞品报告。**依赖/限制：**需 Browserbase API/CLI、密钥、联网及运行配置；不是纯文本 Skill。**CoolFlow 适配：**仅用户具备外部服务权限并接受依赖时使用，报告保留事实来源。**核查依据：**[上游文件](https://github.com/browserbase/skills/blob/main/skills/competitor-analysis/SKILL.md)，Git blob `2ebfdfaa3776fd264f9efc2ec2ef25f00d70200a`（2026-11-01）。

## 1.5 准备真实用户访谈

**何时使用：**准备非引导式访谈提纲。

- **首选：[interview-script](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/interview-script/SKILL.md)**（具体 Skill；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**用非引导式问题设计真实用户访谈。**依赖/限制：**文本 Skill；访谈提纲不等于已经收集到用户证据。**CoolFlow 适配：**只在需访谈时使用；结果分清事实与假设。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/interview-script/SKILL.md)，Git blob `7ec574e0d107507cb6c1926d2620e2ac822c00b6`（2026-11-01）。

