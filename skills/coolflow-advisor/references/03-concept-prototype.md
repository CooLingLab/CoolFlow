# Stage 3 — Concept Prototype → Validation

[精选推荐索引](recommendations.md) · [CoolFlow 文档规范](../../../standards/documentation.md)

**目标：**用可丢弃原型或低成本实验回答最关键的产品问题。

**收录依据：**仅保留本对话已讨论的具体工具；每个任务最多两个选择。核查通过=阅读官方源码及关联依赖、确定 CoolFlow 适配方案，不等于已安装或做过受控对照测试。运行时仍需校验环境及权限。

## 3.1 业务逻辑交互原型

**何时使用：**验证状态机、业务规则和操作中的边界行为。

- **首选：[prototype（Logic）](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**生成用于回答单一问题的可丢弃原型（逻辑或 UI 两分支）。**依赖/限制：****必须连同 `LOGIC.md` 和 `UI.md`** 保存；逻辑分支可用独立 HTML，UI 分支需要可显示的路由/页面环境。**CoolFlow 适配：**放 `docs/work/<objective>/prototypes/`，完成验证后记录结论，不强制进入正式实现。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)，Git blob `a0044501fe0d385b4d8575b610188ede9b236ccf`（2026-11-01）。

## 3.2 核心体验概念原型

**何时使用：**生成并比较尚未进入正式实现的交互视觉方案。

- **首选：[prototype（UI）](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**生成用于回答单一问题的可丢弃原型（逻辑或 UI 两分支）。**依赖/限制：****必须连同 `LOGIC.md` 和 `UI.md`** 保存；逻辑分支可用独立 HTML，UI 分支需要可显示的路由/页面环境。**CoolFlow 适配：**放 `docs/work/<objective>/prototypes/`，完成验证后记录结论，不强制进入正式实现。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)，Git blob `a0044501fe0d385b4d8575b610188ede9b236ccf`（2026-11-01）。

## 3.3 识别产品关键假设

**何时使用：**寻找用户价值、可行性和市场风险中最危险的假设。

- **首选：[identify-assumptions-new](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/identify-assumptions-new/SKILL.md)**（具体 Skill；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**识别新产品的高风险假设。**依赖/限制：**纯文本方法；输出是待证实假设，不是市场证据。**CoolFlow 适配：**在探索资料中记录，避免虚构验证结果。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/identify-assumptions-new/SKILL.md)，Git blob `3ddc8bc514b2a05cf5f0914635f144940797f5ac`（2026-11-01）。

## 3.4 设计低成本验证实验

**何时使用：**把假设变成可以观察、衡量的实验。

- **首选：[brainstorm-experiments-new](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/brainstorm-experiments-new/SKILL.md)**（具体 Skill；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**针对假设设计低成本产品实验。**依赖/限制：**输出实验设计而非用户结果；真正执行仍需条件和资源。**CoolFlow 适配：**对每个实验写清可观察行为与通过标准。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/brainstorm-experiments-new/SKILL.md)，Git blob `8c946a51839c85b7ffb666c268ca4b06513166ed`（2026-11-01）。

