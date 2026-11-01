# Stage 5 — UI Prototype

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**围绕当前版本打磨导航、关键页面、交互和视觉一致性；根据验证目标选择保真度。

**状态：已收录场景级初选；A/B 表示选型判断，非统一受控 A/B 测试结果。** L0/L1 不因轻量适配扣分；依赖未经核实时明确标记，不声称可独立运行。

## 5.1 用户旅程和关键操作路径

**适用场景：**需要梳理导航、关键页面及任务流。

- **首选： [customer-journey-map](https://github.com/phuryn/pm-skills/tree/main/pm-market-research/skills/customer-journey-map)**（Skill）。**用途：**将用户目标、触点与摩擦整理成可讨论的旅程。 **局限：**用户旅程研究不等于可点击 UI 原型。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / 待核实（接入前核查）。



## 5.2 探索多种视觉方向和交互变体

**适用场景：**视觉方向还没定，希望以真实可切换的方案比较界面与交互。

- **首选： [prototype — UI branch](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype)**（Skill）。**用途：**低成本生成可切换的多个 UI 变体，比较根本不同的交互方向。 **局限：**产物是可丢弃原型，不等于正式设计系统。 **CoolFlow 适配：**放在当前 work 的 prototypes/；保留同目录 UI.md，不接管正式 UI/Spec 流程。 **等级：**A / L0。

- **备选： [design-shotgun（gstack）](https://github.com/garrytan/gstack/tree/main/design-shotgun)**（Skill）。**用途：**需要更系统的批量视觉探索时，生成多种设计方向。 **局限：**依赖 gstack 共享脚本与会话机制，不能只复制 SKILL.md。 **CoolFlow 适配：**具备原版环境才运行；否则只借鉴方法，不声称独立可用。 **等级：**B / L3。


## 5.3 生成高质量前端视觉实现

**适用场景：**方向已定，想快速实现高质量视觉或查阅系统化设计知识。

- **首选： [frontend-design（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/frontend-design)**（Skill）。**用途：**强调非模板化视觉风格、层级和细节。 **局限：**偏视觉实现，不替代产品交互研究。 **CoolFlow 适配：**直接使用；遵守项目现有文档规范。 **等级：**A / L0。

- **备选： [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/.claude/skills/ui-ux-pro-max)**（Skill）。**用途：**检索配色、字体、风格和 UX 规则，为设计提供系统化知识支持。 **局限：**依赖配套数据与脚本，单独复制 SKILL.md 不完整。 **CoolFlow 适配：**按需安装其资源；保持技术栈无关，不接管文档规范。 **等级：**A / L2。


## 5.4 精细编辑交互稿或高保真原型

**适用场景：**设计需要手动微调组件、动效和页面关系。

- **首选： [Figma](https://www.figma.com/)**（工具）。**用途：**适用于视觉精修、可点击原型和设计系统。 **局限：**需要人工编辑时更有价值；纯 HTML 原型不必强制使用。 **CoolFlow 适配：**可按需使用，不是 CoolFlow 依赖 **等级：**待复核 / L0。

- **备选： [prototype — UI branch](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype)**（Skill）。**用途：**低成本比较多个交互变体，不必先购买设计服务。 **局限：**产物通常为可丢弃原型，不是长期设计系统。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**A / L0。


## 5.5 视觉与操作验证

**适用场景：**已有 UI 原型，需要检查功能路径、状态反馈和浏览器表现。

- **首选： [browser-testing-with-devtools](https://github.com/addyosmani/agent-skills/tree/main/skills/browser-testing-with-devtools)**（Skill）。**用途：**通过实际点击、浏览器调试和错误检查验证 UI。 **局限：**需要实际运行环境；不能仅凭代码推断成功。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**待复核 / 待核实（接入前核查）。

- **备选： [design-review（gstack）](https://github.com/garrytan/gstack/tree/main/design-review)**（Skill）。**用途：**从布局和设计质量角度复查页面。 **局限：**可能需要 gstack 的浏览器工具链与配置。 **CoolFlow 适配：**原版运行需核查 gstack 共享脚本与宿主能力；缺少依赖时只能借鉴方法并改造，不视为原版独立使用。 **等级：**待复核 / L2。


## 5.6 设计访谈与风格定位

**适用场景：**用户尚未形成明确的视觉偏好，需要先澄清品牌风格与约束。

- **首选： [design-consultation（gstack）](https://github.com/garrytan/gstack/tree/main/design-consultation)**（Skill）。**用途：**通过设计访谈澄清风格和界面需求。 **局限：**原版依赖 gstack 共享脚本，不保证产出运行原型。 **CoolFlow 适配：**若抽取提问法可轻量改造；原版运行需具备依赖环境。 **等级：**B / L2。

## 5.7 前端 UI 工程质量检查

**适用场景：**交互已明确，需要检查组件语义、响应式和代码层面的 UI 质量。

- **首选： [frontend-ui-engineering](https://github.com/addyosmani/agent-skills/tree/main/skills/frontend-ui-engineering)**（Skill）。**用途：**检查 UI 组件结构、语义与响应式工程实践。 **局限：**偏实现质量，不代替视觉方向探索。 **CoolFlow 适配：**不引入框架专属默认规范，只采用与当前场景有关的原则。 **等级：**B / 待核实（接入前核查）。
