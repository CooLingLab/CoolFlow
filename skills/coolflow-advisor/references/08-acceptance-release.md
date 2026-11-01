# Stage 8 — Human Acceptance → Documentation Sync → Release

[精选推荐索引](recommendations.md) · [CoolFlow 文档规范](../../../standards/documentation.md)

**目标：**人工接受实际行为、同步已验收事实；交付/发布需单独授权。

**收录依据：**仅保留本对话已讨论的具体工具；每个任务最多两个选择。核查通过=阅读官方源码及关联依赖、确定 CoolFlow 适配方案，不等于已安装或做过受控对照测试。运行时仍需校验环境及权限。

## 8.1 设计人工验收测试情境

**何时使用：**把实际用户行为、失败路径变成手工验收脚本。

- **首选：[test-scenarios](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/test-scenarios/SKILL.md)**（具体 Skill；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**把用户故事转换成可执行的人工测试情境。**依赖/限制：**纯文本方法，测试设计不等于真实运行与人工接受。**CoolFlow 适配：**用 CoolFlow Spec 验收条件定义行为，人工决定是否通过。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/test-scenarios/SKILL.md)，Git blob `d5a25a7185d1681f97c1506d2ff1ccc083a7ce95`（2026-11-01）。

## 8.2 发布前验证

**何时使用：**证据充分后再宣布可交付，不替代人工验收。

- **首选：[verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md)**（具体 Skill；A / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**完成声明前要求实际测试结果而非猜测。**依赖/限制：**需可执行验证命令/可见工具输出。**CoolFlow 适配：**映射到当前 CoolFlow Spec 验收标准；不取代人工验收。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md)，Git blob `7d45333cc4a49c57a80df6c1fe2fa777a207afbc`（2026-11-01）。

## 8.3 完成开发分支与交付

**何时使用：**按仓库规则处理已验收变更、分支或 PR。

- **首选：[finishing-a-development-branch](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md)**（具体 Skill；A / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**通过测试后提供分支合并、保留或清理等选项。**依赖/限制：**需要 Git 环境；原版可执行合并/分支清理。**CoolFlow 适配：**执行每个有影响的 Git 操作前遵守人类授权，不等同于上线。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md)，Git blob `fa8aecaf8813f1b19d19996f7957d1b0121f2d9c`（2026-11-01）。

- **备选：[ship](https://github.com/garrytan/gstack/blob/main/ship/SKILL.md)**（具体 Skill；B / L3）。**核查通过（源码与依赖检查，未实机验证）** **能力：**串联测试、变更记录、推送与 PR 流程。**依赖/限制：**gstack 共享运行环境与脚本、Git/PR 权限，具有写入与推送副作用。**CoolFlow 适配：**仅相关授权明确且环境具备时调用；禁止默认自动发布。**核查依据：**[上游文件](https://github.com/garrytan/gstack/blob/main/ship/SKILL.md)，Git blob `32de83e7db47b9e1828110bb5c481949b5461412`（2026-11-01）。

## 8.4 编写版本更新说明

**何时使用：**根据真实变更写面向用户的发布说明。

- **首选：[release-notes](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/release-notes/SKILL.md)**（具体 Skill；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**从变更记录生成用户可读的更新说明。**依赖/限制：**纯文本方法；需实际发布内容，不能凭规划猜测已发布。**CoolFlow 适配：**注明已发布/未发布，审阅实际 Diff 与验收事实。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/release-notes/SKILL.md)，Git blob `148bf1cb176851d13531a54facc207824b22f493`（2026-11-01）。

## 8.5 发布后用户反馈访谈

**何时使用：**以真实反馈支持下一轮 Evolution Loop。

- **首选：[interview-script](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/interview-script/SKILL.md)**（具体 Skill；B / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**用非引导式问题设计真实用户访谈。**依赖/限制：**文本 Skill；访谈提纲不等于已经收集到用户证据。**CoolFlow 适配：**只在需访谈时使用；结果分清事实与假设。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/interview-script/SKILL.md)，Git blob `7ec574e0d107507cb6c1926d2620e2ac822c00b6`（2026-11-01）。

