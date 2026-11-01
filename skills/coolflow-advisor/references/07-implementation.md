# Stage 7 — Implementation Loop

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**Coding → Testing → Review → Spec Conformance → Fix；在证据不足时继续迭代。

**条目状态：本文件所有条目均为候选（核查未完成），不进入 Advisor 默认推荐。** 现有记录不足以证明每项均完成来源、能力、依赖与适配四项核查；候选顺序、A/B/C 与 L0–L3 为初评，不是核查通过。未实测与未核查不同；L0/L1 轻量适配不降优先级。核查规则见[索引](recommendations.md#默认推荐的核查门槛)。

## 7.1 按确认的计划执行代码

**适用场景：**已有 Spec/计划，需要小步实现而不是重新设计需求。

- **候选 1： [executing-plans（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/executing-plans)**（Skill）。**用途：**按照计划执行、检查和汇报增量结果。 **局限：**可能引入其自有任务管理和执行约定。 **CoolFlow 适配：**仅采用执行纪律，仍以 CoolFlow Spec 与当前工具链为准。 **等级：**A / L1。

- **候选 2： [implement](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement)**（Skill）。**用途：**面向单个可实现任务的完成和验证流程。 **局限：**通常与 Matt Pocock 的 tickets 工作流衔接，单独使用需核对前提。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / L1。


## 7.2 测试驱动开发

**适用场景：**边开发边设计测试边界，避免只有实现没有可验证行为。

- **候选 1： [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)**（Skill）。**用途：**强调可观察的外部行为和明确的测试边界。 **局限：**不是所有原型、探索或配置改动都值得完整 TDD。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**A / L0。

- **候选 2： [test-driven-development（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)**（Skill）。**用途：**给出 Red-Green-Refactor 的可执行纪律。 **局限：**按项目实际测试环境裁剪，不强制所有工作完全同一循环。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**A / L0。


## 7.3 系统性 Bug 根因定位

**适用场景：**测试失败、行为异常、修复反复失败，需要先定位因果而非猜测。

- **候选 1： [systematic-debugging（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)**（Skill）。**用途：**基于证据区分症状与根因，避免盲目修改。 **局限：**调试过程可能较长；极简明确错误可以直接修复。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**A / L0。

- **候选 2： [diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)**（Skill）。**用途：**针对 Bug 进行可复现的排查和假设验证。 **局限：**必须查看实际运行/日志，不以主观猜测作结论。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**A / L0。


## 7.4 代码审查与风险识别

**适用场景：**实现完成，需要独立检查正确性、可维护性和实际变更范围。

- **候选 1： [code-review](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review)**（Skill）。**用途：**围绕实际变更找功能或设计风险，适合定向 Review。 **局限：**要阅读真实 Diff 和测试结果，避免泛泛而谈。 **CoolFlow 适配：**原版需要审查子 Agent；不支持时可改为单 Agent 分步骤审查，并明确属于适配版。 **等级：**A / L2。

- **候选 2： [review（gstack）](https://github.com/garrytan/gstack/tree/main/review)**（Skill）。**用途：**提供较完整的工程审查流程。 **局限：**gstack 运行环境较重；不要把该套件作为必要依赖。 **CoolFlow 适配：**原版运行需核查 gstack 共享脚本与宿主能力；缺少依赖时只能借鉴方法并改造，不视为原版独立使用。 **等级：**B / L3。


## 7.5 完成前证据核查和 Spec Conformance

**适用场景：**Agent 声称实现完成，需要核对测试结果、实际运行与已确认要求。

- **候选 1： [verification-before-completion（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/verification-before-completion)**（Skill）。**用途：**在宣布完成前要求直接验证证据。 **局限：**通过构建不等于人工验收，也不等于正式发布。 **CoolFlow 适配：**将验证结果对应 CoolFlow Spec 验收标准；用户仍负责最终验收。 **等级：**A / L0。

- **候选 2： [verify（gstack）](https://github.com/garrytan/gstack/tree/main/verify)**（Skill）。**用途：**聚焦实际验证证据与已完成工作的交付检查。 **局限：**依赖 gstack 环境，复杂程度因项目而异。 **CoolFlow 适配：**原版运行需核查 gstack 共享脚本与宿主能力；缺少依赖时只能借鉴方法并改造，不视为原版独立使用。 **等级：**待复核 / L2。


## 7.6 多任务并行和子 Agent 分工

**适用场景：**多个任务边界清晰，确实能减少等待并可独立集成。

- **候选 1： [subagent-driven-development（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development)**（Skill）。**用途：**为独立子任务配置专门执行和审查上下文。 **局限：**多 Agent 带来合并、成本和冲突开销；并非默认更快。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**A / 待核实（接入前核查）。

- **候选 2： [pair-agent（gstack）](https://github.com/garrytan/gstack/tree/main/pair-agent)**（Skill）。**用途：**面向协作式 Agent 执行。 **局限：**依赖运行环境，不应当作为 CoolFlow 通用规范。 **CoolFlow 适配：**原版运行需核查 gstack 共享脚本与宿主能力；缺少依赖时只能借鉴方法并改造，不视为原版独立使用。 **等级：**待复核 / L2。


## 7.7 安全性和上线风险检查

**适用场景：**项目涉及账户、支付、敏感数据或外部服务，需要专项检查。

- **候选 1： [security-and-hardening](https://github.com/addyosmani/agent-skills/tree/main/skills/security-and-hardening)**（Skill）。**用途：**从常见安全弱点和硬化措施检视实现。 **局限：**Skill 审查不能代替实际安全测试、供应链扫描和授权审批。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**待复核 / 待核实（接入前核查）。

- **候选 2： [cso（gstack）](https://github.com/garrytan/gstack/tree/main/cso)**（Skill）。**用途：**较系统的安全审查角色。 **局限：**需要适配 gstack；安全发现应以具体证据为准。 **CoolFlow 适配：**原版运行需核查 gstack 共享脚本与宿主能力；缺少依赖时只能借鉴方法并改造，不视为原版独立使用。 **等级：**待复核 / L2。

