# Stage 6 — Design Spec Loop

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**为选中的增量准备可实施的统一 Spec，必要时进行独立设计评审并修订。

**状态：初版候选（研究推荐），不声称已经个人实测。** 每个场景通常最多两个推荐。原项目中的单个 Skill 未必能脱离其依赖直接运行。

## 6.1 整理统一 Spec 草稿

**适用场景：**已经讨论清楚产品需求，需要沉淀范围、可观察验收标准、实现方案和验证方法。

- **首选： [to-spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec)**（Skill）。**用途：**把达成共识的需求和技术约束转成面向实现的 Spec。 **局限：**原版偏向向 Issue Tracker 发布并具有自身流程前提。 **CoolFlow 适配：**重定向输出到 CoolFlow docs/work/<objective>/spec.md，保留 CoolFlow 统一 Spec 规则；必要时先完成已有需求访谈。

- **备选： [spec（gstack）](https://github.com/garrytan/gstack/tree/main/spec)**（Skill）。**用途：**对复杂需求提供精细 Spec 表达。 **局限：**依赖 gstack 流程与工具；避免创建第二套权威 Spec。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 6.2 模块边界和技术方案

**适用场景：**需要确认接口、职责、耦合与非功能限制。

- **首选： [codebase-design](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)**（Skill）。**用途：**帮助识别可复用的深模块、接口边界和设计权衡。 **局限：**须结合项目规模，不为了架构而抽象。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

- **备选： [plan-eng-review（gstack）](https://github.com/garrytan/gstack/tree/main/plan-eng-review)**（Skill）。**用途：**从工程可行性和交付风险审查已有设计。 **局限：**依赖 gstack，适合重要方案而非每个小改动。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 6.3 独立设计评审与反证

**适用场景：**重大方案已成稿，需要一个独立视角找遗漏、风险和不一致。

- **首选： [Google Elephant Goldfish Model (EGM)](https://github.com/google/elephant-goldfish-model)**（方法）。**用途：**强调独立的设计质疑与修改闭环。 **局限：**只在高风险复杂方案中值得付出额外上下文与评审成本。 **CoolFlow 适配：**与 CoolFlow Design Spec Loop 互补；输出评审意见，不自动替代设计者决策。

- **备选： [doubt-driven-development](https://github.com/addyosmani/agent-skills/tree/main/skills/doubt-driven-development)**（Skill）。**用途：**用怀疑和反证方法检查假设与设计薄弱处。 **局限：**独立性需通过新上下文或另一 Agent 才能实现；单纯自问不等于独立评审。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 6.4 必要的架构决策记录 ADR

**适用场景：**有重要且难以逆转的技术选择，需要记录当时的取舍依据。

- **首选： [documentation-and-adrs](https://github.com/addyosmani/agent-skills/tree/main/skills/documentation-and-adrs)**（Skill）。**用途：**提供文档和架构决策记录的实践指南。 **局限：**不能强制为每项实现决定创建 ADR。 **CoolFlow 适配：**沿用 CoolFlow 可选 docs/adr/ 和已提供的模板。

- **备选： [CoolFlow ADR template](https://github.com/CooLingLab/CoolFlow/tree/main/templates/optional/adr)**（方法）。**用途：**使用仓库内部统一的 ADR 模板和示例。 **局限：**模板不代表每个功能都必须产生 ADR。 **CoolFlow 适配：**作为方法参考，按项目规模裁剪


## 6.5 拆分最小可交付任务

**适用场景：**Spec 已确认，实施跨度较大，需要把工作拆成可独立验证的增量。

- **首选： [writing-plans（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/writing-plans)**（Skill）。**用途：**将确认的设计转为细粒度可执行计划。 **局限：**原版有自己的计划文档路径和后续执行链。 **CoolFlow 适配：**轻量保留拆分方法；只在任务需要跨会话跟踪时创建 CoolFlow tasks.md。

- **备选： [to-tickets](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets)**（Skill）。**用途：**以纵向切片和依赖关系形成可执行工作项。 **局限：**原版依赖 Issue Tracker 或本地 tracker 配置，不能默认独立使用。 **CoolFlow 适配：**小任务直接在 Agent 会话拆解；复杂任务再决定是否用 Issue/本地 tracker。

