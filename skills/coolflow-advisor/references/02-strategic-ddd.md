# Stage 2 — Lightweight Strategic DDD

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**梳理通用语言、领域边界、核心规则；不强制完整 DDD 或额外目录。

**条目状态：本文件所有条目均为候选（核查未完成），不进入 Advisor 默认推荐。** 现有记录不足以证明每项均完成来源、能力、依赖与适配四项核查；候选顺序、A/B/C 与 L0–L3 为初评，不是核查通过。未实测与未核查不同；L0/L1 轻量适配不降优先级。核查规则见[索引](recommendations.md#默认推荐的核查门槛)。

## 2.1 术语澄清和统一语言

**适用场景：**同一个词被不同角色用作不同含义，或者业务概念含糊。

- **候选 1： [domain-modeling](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)**（Skill）。**用途：**主动质疑术语、边界和场景，使领域语言具体。 **局限：**原版默认 GLOSSARY.md / GLOSSARY-MAP.md。 **CoolFlow 适配：**轻量映射到 CoolFlow docs/domain.md，不强制创建 GLOSSARY.md；重要决策才考虑 ADR。 **等级：**A / L1。

- **候选 2： [DDD Crew — Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process)**（方法）。**用途：**提供领域发现和战略建模的经典方法参考。 **局限：**它是方法资料，不是可直接调用的 Agent Skill。 **CoolFlow 适配：**作为方法参考，按项目规模裁剪 **等级：**待复核 / L0。


## 2.2 识别子域和限界上下文

**适用场景：**领域较复杂，需要决定哪些责任放在一起。

- **候选 1： [DDD Crew — Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas)**（方法）。**用途：**用职责、业务能力和交互来界定上下文。 **局限：**轻量小型产品可能只需在 domain.md 写数条边界。 **CoolFlow 适配：**作为方法参考，按项目规模裁剪 **等级：**待复核 / L0。

- **候选 2： [DDD Crew — Context Mapping](https://github.com/ddd-crew/context-mapping)**（方法）。**用途：**解释上下文之间的关系及协作模式。 **局限：**需要存在多个真实上下文，不为建模而拆分。 **CoolFlow 适配：**作为方法参考，按项目规模裁剪 **等级：**待复核 / L0。


## 2.3 对领域规则进行反例挑战

**适用场景：**已提出关键业务规则，希望用边界案例暴露冲突。

- **候选 1： [grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)**（Skill）。**用途：**针对已有文档和代码反复追问并推动术语一致。 **局限：****非独立 Skill**：原版仅调用 grilling 和 domain-modeling 两个 Skill；还会按其习惯写 glossary/ADR。 **CoolFlow 适配：**单独移植必须补齐依赖或内化核心方法；写入 CoolFlow domain.md，按需 ADR。 **等级：**A / L1。

- **候选 2： [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)**（Skill）。**用途：**只采用高强度追问逻辑，适合不需要自动写文档的场景。 **局限：**需要开发者明确记录最终被确认的领域规则。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / L0。


## 2.4 梳理系统之间的协作边界

**适用场景：**存在多个上下文或外部系统，担心耦合和职责交叉。

- **候选 1： [DDD Crew — Context Mapping](https://github.com/ddd-crew/context-mapping)**（方法）。**用途：**帮助描述上下文关系、上游下游和集成策略。 **局限：**不要把细粒度部署组件误当成业务上下文。 **CoolFlow 适配：**作为方法参考，按项目规模裁剪 **等级：**待复核 / L0。

- **候选 2： [codebase-design](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)**（Skill）。**用途：**从实际代码和接口形状出发检视模块边界。 **局限：**更偏技术模块设计；不能替代战略 DDD 的业务发现。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / L0。

