# Stage 8 — Human Acceptance → Documentation Sync → Release

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**人类检查实际行为并接受；同步已验收事实；发布是单独授权的动作。

**状态：初版候选（研究推荐），不声称已经个人实测。** 每个场景通常最多两个推荐。原项目中的单个 Skill 未必能脱离其依赖直接运行。

## 8.1 设计人工验收测试情境

**适用场景：**需要一组覆盖真实用户行为、边界和失败路径的测试脚本。

- **首选： [test-scenarios](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/test-scenarios)**（Skill）。**用途：**把需求转成可以由人执行的测试场景。 **局限：**测试用例通过不自动等于用户接受；要确认对应目标版本。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

- **备选： [qa（gstack）](https://github.com/garrytan/gstack/tree/main/qa)**（Skill）。**用途：**对运行中的产品做端到端操作检查。 **局限：**依赖浏览器与 gstack 运行环境；人工验收仍需人类亲自判断。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 8.2 验收后的文档同步

**适用场景：**已验收代码与文档存在差异，需更新真实现状而不是复制计划。

- **首选： [document-release（gstack）](https://github.com/garrytan/gstack/tree/main/document-release)**（Skill）。**用途：**检查已有实现、发布和文档是否一致。 **局限：**有自带文档分类和发布前提，不可覆盖 CoolFlow 本地规范。 **CoolFlow 适配：**对齐 docs/features/、product.md、domain.md、roadmap.md 等；仅记录已验收事实。

- **备选： [documentation-and-adrs](https://github.com/addyosmani/agent-skills/tree/main/skills/documentation-and-adrs)**（Skill）。**用途：**提供维护文档与 ADR 的方法。 **局限：**不应将临时草稿全部升级为长期文档。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 8.3 发布前证据与风险复核

**适用场景：**验收已完成，希望再次核对部署前的状态和关键约束。

- **首选： [verification-before-completion（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/verification-before-completion)**（Skill）。**用途：**用实际证据检查准备情况，避免过早声称完成。 **局限：**不能替代部署权限、用户批准或渠道审核。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

- **备选： [shipping-and-launch](https://github.com/addyosmani/agent-skills/tree/main/skills/shipping-and-launch)**（Skill）。**用途：**整理上线与交付检查重点。 **局限：**需按平台具体发布约束另外核实。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范


## 8.4 完成开发分支、合并和交付

**适用场景：**工作已被接受，需要按仓库规则结束分支或交付变更。

- **首选： [finishing-a-development-branch（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch)**（Skill）。**用途：**有序处理分支完成、验证与合并选择。 **局限：**不能绕过人工批准，不能未经授权直接发布。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

- **备选： [ship（gstack）](https://github.com/garrytan/gstack/tree/main/ship)**（Skill）。**用途：**集成从验证到交付的一揽子操作。 **局限：**执行权限较大、依赖 gstack；不适合默认自动调用。 **CoolFlow 适配：**只能在用户明确授权对应交付动作时使用。


## 8.5 生成版本说明和发布记录

**适用场景：**已经决定发布某个版本，需要准确概括用户可见变化。

- **首选： [release-notes](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/release-notes)**（Skill）。**用途：**帮助把变更转成面向用户的说明。 **局限：**必须区分已发布与尚未发布的功能，基于真实 Diff/发布内容。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范



## 8.6 发布后的反馈与下一轮迭代

**适用场景：**已有真实用户反馈，希望判断继续、调整还是回到前一阶段。

- **首选： [interview-script](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/interview-script)**（Skill）。**用途：**帮助开展真实用户反馈访谈。 **局限：**不把少量主观评价当成统计显著需求。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

- **备选： [retro（gstack）](https://github.com/garrytan/gstack/tree/main/retro)**（Skill）。**用途：**复盘流程和质量问题，发现值得沉淀的经验。 **局限：**复盘不等于自动修改产品方向。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范

