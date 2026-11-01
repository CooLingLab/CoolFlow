# Stage 4 — Roadmap

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**决定 MVP/当前版本范围与后续优先级，分清产品路线图和实现任务计划。

**条目状态：本文件所有条目均为候选（核查未完成），不进入 Advisor 默认推荐。** 现有记录不足以证明每项均完成来源、能力、依赖与适配四项核查；候选顺序、A/B/C 与 L0–L3 为初评，不是核查通过。未实测与未核查不同；L0/L1 轻量适配不降优先级。核查规则见[索引](recommendations.md#默认推荐的核查门槛)。

## 4.1 筛选 MVP 功能

**适用场景：**已有许多功能想法，需要决定首个可验证的产品范围。

- **候选 1： [prioritize-features](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/prioritize-features)**（Skill）。**用途：**基于影响、成本、风险和战略一致性取舍功能。 **局限：**不要把打分当成客观真理；保留明确的暂不做事项。 **CoolFlow 适配：**按需补齐其引用的 prioritization-frameworks，或内化必要规则；输出仍遵守 CoolFlow roadmap 规范。 **等级：**B / L1。

- **候选 2： [prioritization-frameworks](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/prioritization-frameworks)**（Skill）。**用途：**帮助选择 RICE/ICE 等适当的取舍方法。 **局限：**数值缺乏证据时不要制造虚假的精度。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / L0。


## 4.2 规划结果导向的版本路线

**适用场景：**希望 MVP、后续迭代围绕用户结果而不是功能堆砌。

- **候选 1： [outcome-roadmap](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/outcome-roadmap)**（Skill）。**用途：**把功能清单映射到预期用户结果和可验证指标。 **局限：**其默认季度式展示不适合所有独立开发项目。 **CoolFlow 适配：**在 CoolFlow docs/roadmap.md 记录 MVP / Later；不强求日期。 **等级：**B / L1。

- **候选 2： [GitHub Projects](https://github.com/features/issues)**（工具）。**用途：**跟踪实际版本事项与 Issue，不必另建工作流引擎。 **局限：**不是产品决策方法，单人短项目不一定需要。 **CoolFlow 适配：**可按需使用，不是 CoolFlow 依赖 **等级：**待复核 / L0。


## 4.3 挑战版本边界和商业假设

**适用场景：**担心 MVP 范围过大、用户价值不聚焦。

- **候选 1： [plan-ceo-review（gstack）](https://github.com/garrytan/gstack/tree/main/plan-ceo-review)**（Skill）。**用途：**从价值和优先级角度挑战计划。 **局限：**gstack 整套角色与命令偏重；不能替代用户决策。 **CoolFlow 适配：**只借鉴 CEO 评审问题，不让 gstack 改写 CoolFlow roadmap 结构。 **等级：**B / L2。

- **候选 2： [strategy-red-team](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/strategy-red-team)**（Skill）。**用途：**用反证视角识别目标、市场和计划中的盲点。 **局限：**结果是风险提示而不是自动否决。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**待复核 / 待核实（接入前核查）。


## 4.4 分解短期版本交付节奏

**适用场景：**当前增量已确认，需要安排近期的少数可交付单元。

- **候选 1： [sprint-plan](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/sprint-plan)**（Skill）。**用途：**建立迭代节奏与优先顺序。 **局限：**偏团队 Scrum；个人开发不应引入无意义的仪式。 **CoolFlow 适配：**输出可回写 roadmap 或当前 work，正式 tasks.md 只在需要持久跟踪时创建。 **等级：**待复核 / 待核实（接入前核查）。


