# Stage 6 — Design Spec Loop

[精选推荐索引](recommendations.md) · [CoolFlow 文档规范](../../../standards/documentation.md)

**目标：**形成统一 Spec、必要架构决策与实施计划，按重要性评审。

**收录依据：**仅保留本对话已讨论的具体工具；每个任务最多两个选择。核查通过=阅读官方源码及关联依赖、确定 CoolFlow 适配方案，不等于已安装或做过受控对照测试。运行时仍需校验环境及权限。

## 6.1 编写功能 Spec

**何时使用：**把已确认的需求与实现策略落实为统一规范。

- **首选：[to-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**把已有讨论综合成可实施 Spec。**依赖/限制：**原版要求预先配置 Issue Tracker 和标签；不是纯粹输出本地文件。**CoolFlow 适配：**改为 `docs/work/<objective>/spec.md`，不建第二套 Spec。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md)，Git blob `3f52599ae2a4347aee5a07432c2707518e691a7f`（2026-11-01）。

- **备选：[spec](https://github.com/garrytan/gstack/blob/main/spec/SKILL.md)**（具体 Skill；B / L2）。**核查通过（源码与依赖检查，未实机验证）** **能力：**系统化梳理需求并形成具体工程 Spec。**依赖/限制：**需 gstack 共享 preamble 和相关脚本，原版还偏向 issue 流程。**CoolFlow 适配：**只在运行环境满足时使用；最终 Spec 以 CoolFlow 工作目录为权威。**核查依据：**[上游文件](https://github.com/garrytan/gstack/blob/main/spec/SKILL.md)，Git blob `8d94a32c83368e44b0d2d863b96c8b15ff2742f9`（2026-11-01）。

## 6.2 架构与技术方案审查

**何时使用：**检视模块职责、接口和工程交付风险。

- **首选：[plan-eng-review](https://github.com/garrytan/gstack/blob/main/plan-eng-review/SKILL.md)**（具体 Skill；B / L2）。**核查通过（源码与依赖检查，未实机验证）** **能力：**按工程可行性、风险和模块职责审查设计。**依赖/限制：**gstack 共享前置内容、会话机制与命令工具。**CoolFlow 适配：**按实际宿主条件运行，不覆盖 CoolFlow Spec/ADR 决策。**核查依据：**[上游文件](https://github.com/garrytan/gstack/blob/main/plan-eng-review/SKILL.md)，Git blob `46dc6e36b9688dd05e52bf2d6e804274bb20d68f`（2026-11-01）。

- **备选：[codebase-design](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md)**（具体 Skill；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**讨论深模块、接口边界与可维护性。**依赖/限制：**文本方法；不保证单独产生独立架构评审。**CoolFlow 适配：**遵守轻量设计，避免为抽象而抽象。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md)，Git blob `3f63c8146dd2604b419c929e9876b90c30d410e9`（2026-11-01）。

## 6.3 领域与架构决策记录

**何时使用：**需要记录重要、难撤销的设计/技术取舍。

- **首选：[domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**挑战领域术语、业务规则、边界案例和重大领域决策。**依赖/限制：**原版默认根目录 `GLOSSARY.md` 与自己的 ADR 习惯。**CoolFlow 适配：**映射到 `docs/domain.md`；仅重大决策使用可选 `docs/adr/`。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)，Git blob `a4438c6879c517d1a08e2b5fbca049b632688dfe`（2026-11-01）。

- **备选：[CoolFlow ADR template](https://github.com/CooLingLab/CoolFlow/tree/main/templates/optional/adr)**（CoolFlow 内置模板；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**为重要、难撤销的架构决策保留理由和替代方案。**依赖/限制：**CoolFlow 自带模板，无第三方依赖。**CoolFlow 适配：**仅在真正需要 ADR 时创建，使用 `docs/adr/`。**核查依据：**[上游文件](https://github.com/CooLingLab/CoolFlow/tree/main/templates/optional/adr)，Git blob `f64fa2648bb56c6f3a36b9ad4454c4bb17e02b8d`（2026-11-01）。

## 6.4 拆解实施计划

**何时使用：**将确认的 Spec 变成小型、可验证的任务。

- **首选：[writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**从确认 Spec 形成可执行的小任务和验证步骤。**依赖/限制：**原版内置 Superpowers 计划路径和执行交接。**CoolFlow 适配：**写入现有 Agent 会话，只有跨会话需要时才使用 `tasks.md`。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md)，Git blob `4cf0275d88d67aa4ef09f4bbca9970ed6ff74a00`（2026-11-01）。

- **备选：[to-tickets](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md)**（具体 Skill；B / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**以可交付纵向切片拆解任务及其依赖。**依赖/限制：**原版要 Issue Tracker/local tracker 配置。**CoolFlow 适配：**仅必要时适配成 `tasks.md` 或现有 issue，避免重复事实来源。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md)，Git blob `9b77a01db9460c99c22d03c910c349f890f12c0e`（2026-11-01）。

