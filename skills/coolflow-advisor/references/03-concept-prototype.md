# Stage 3 — Concept Prototype → Validation

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**围绕一个具体产品假设快速制作可丢弃原型，并通过真实证据判断结论。

**状态：已收录场景级初选；A/B 表示选型判断，非统一受控 A/B 测试结果。** L0/L1 不因轻量适配扣分；依赖未经核实时明确标记，不声称可独立运行。

## 3.1 识别最危险的产品假设

**适用场景：**不确定需求、可行性、可用性或商业价值，需决定先验证什么。

- **首选： [identify-assumptions-new](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/identify-assumptions-new)**（Skill）。**用途：**把产品假设按风险维度展开，避免只验证容易的部分。 **局限：**输出是假设清单，不是市场事实。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / 待核实（接入前核查）。

- **备选： [prioritize-assumptions](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/prioritize-assumptions)**（Skill）。**用途：**按风险和验证价值聚焦先做哪个实验。 **局限：**先有足够明确的假设清单才有意义。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / 待核实（接入前核查）。


## 3.2 状态、逻辑和交互机制原型

**适用场景：**想知道某个状态机或业务规则在操作中是否合理。

- **首选： [prototype — logic branch](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype)**（Skill）。**用途：**专门生成可操作的临时逻辑展示，快速测试边界行为。 **局限：**原版按自身目录习惯存放丢弃原型。 **CoolFlow 适配：**优先放在 CoolFlow 当前 work/<objective>/prototypes/ 或临时分支；明确可丢弃。 **等级：**A / L0。



## 3.3 快速可视化概念界面

**适用场景：**需要对比几种根本不同的交互方向，而不是先实现正式 App。

- **首选： [prototype — UI branch](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype)**（Skill）。**用途：**同一个具体 Skill 的 UI 分支，可快速比较视觉/交互候选。 **局限：**不是正式设计系统，也不应与 Step 5 UI 原型混淆。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**A / L0。

- **备选： [design-html（gstack）](https://github.com/garrytan/gstack/tree/main/design-html)**（Skill）。**用途：**用于把明确的设计方向变成可查看 HTML。 **局限：**依赖 gstack 专有脚本/共享说明，不能按独立 Skill 直接复制。 **CoolFlow 适配：**仅在已经采用 gstack 环境时优先；普通原型可直接让 Agent 写 HTML。 **等级：**待复核 / L2。


## 3.4 设计低成本验证实验

**适用场景：**需要检验是否真的有人愿意完成关键行为。

- **首选： [brainstorm-experiments-new](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/brainstorm-experiments-new)**（Skill）。**用途：**将假设转成可观察的低成本实验，例如落地页或原型任务。 **局限：**实验方案必须定义实际可测行为，不等于执行或得到结论。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / 待核实（接入前核查）。



## 3.5 验证浏览器原型的实际交互

**适用场景：**已经有 HTML 原型，需要运行、点击、记录失败场景。

- **首选： [browser-testing-with-devtools](https://github.com/addyosmani/agent-skills/tree/main/skills/browser-testing-with-devtools)**（Skill）。**用途：**使用浏览器开发者工具检查页面交互和行为证据。 **局限：**需要可用浏览器和对应权限；截图漂亮不等于体验验证。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**待复核 / 待核实（接入前核查）。

- **备选： [qa（gstack）](https://github.com/garrytan/gstack/tree/main/qa)**（Skill）。**用途：**可用于已有运行应用的交互 QA。 **局限：**依赖 gstack 运行环境；可能重于临时原型。 **CoolFlow 适配：**原版运行需核查 gstack 共享脚本与宿主能力；缺少依赖时只能借鉴方法并改造，不视为原版独立使用。 **等级：**待复核 / L2。

