# Stage 5 — UI Prototype

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**围绕当前版本打磨导航、关键页面、交互和视觉一致性；根据验证目标选择保真度。

**状态：初版候选（研究推荐），不声称已经个人实测。** 每个场景通常最多两个推荐。原项目中的单个 Skill 未必能脱离其依赖直接运行。

## 5.1 用户旅程和关键操作路径

**适用场景：**需要梳理导航、关键页面及任务流。

- **首选： [customer-journey-map](https://github.com/phuryn/pm-skills/tree/main/pm-market-research/skills/customer-journey-map)**（Skill）。**用途：**将用户目标、触点与摩擦整理成可讨论的旅程。 **局限：**用户旅程研究不等于可点击 UI 原型。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范



## 5.2 探索多种视觉方向

**适用场景：**还没决定视觉气质、版式和关键界面。

- **首选： [design-shotgun（gstack）](https://github.com/garrytan/gstack/tree/main/design-shotgun)**（Skill）。**用途：**批量探索视觉方向，避免直接锁定第一稿。 **局限：**依赖 gstack 共享脚本/运行环境；直接拆出可能不能运行。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

- **备选： [design-consultation（gstack）](https://github.com/garrytan/gstack/tree/main/design-consultation)**（Skill）。**用途：**用设计访谈澄清品牌风格与界面需求。 **局限：**不保证产出可运行 HTML。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 5.3 生成高质量前端视觉实现

**适用场景：**设计方向已确定，想快速产出精致的界面或代码原型。

- **首选： [frontend-design（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/frontend-design)**（Skill）。**用途：**强调非模板化视觉风格、层级和细节。 **局限：**偏 UI 视觉实现，不替代产品交互研究。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

- **备选： [frontend-ui-engineering](https://github.com/addyosmani/agent-skills/tree/main/skills/frontend-ui-engineering)**（Skill）。**用途：**兼顾组件结构、语义、响应式与 UI 工程质量。 **局限：**可能偏工程实现；原型阶段避免过度抽象。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 5.4 精细编辑交互稿或高保真原型

**适用场景：**设计需要手动微调组件、动效和页面关系。

- **首选： [Figma](https://www.figma.com/)**（工具）。**用途：**适用于视觉精修、可点击原型和设计系统。 **局限：**需要人工编辑时更有价值；纯 HTML 原型不必强制使用。 **CoolFlow 适配：**可按需使用，不是 CoolFlow 依赖

- **备选： [prototype — UI branch](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype)**（Skill）。**用途：**低成本比较多个交互变体，不必先购买设计服务。 **局限：**产物通常为可丢弃原型，不是长期设计系统。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 5.5 视觉与操作验证

**适用场景：**已有 UI 原型，需要检查功能路径、状态反馈和浏览器表现。

- **首选： [browser-testing-with-devtools](https://github.com/addyosmani/agent-skills/tree/main/skills/browser-testing-with-devtools)**（Skill）。**用途：**通过实际点击、浏览器调试和错误检查验证 UI。 **局限：**需要实际运行环境；不能仅凭代码推断成功。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

- **备选： [design-review（gstack）](https://github.com/garrytan/gstack/tree/main/design-review)**（Skill）。**用途：**从布局和设计质量角度复查页面。 **局限：**可能需要 gstack 的浏览器工具链与配置。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

