# Stage 5 — UI Prototype

[精选推荐索引](recommendations.md) · [CoolFlow 文档规范](../../../standards/documentation.md)

**目标：**为选定版本探索视觉方向和高保真交互，不预设平台或框架。

**收录依据：**仅保留本对话已讨论的具体工具；每个任务最多两个选择。核查通过=阅读官方源码及关联依赖、确定 CoolFlow 适配方案，不等于已安装或做过受控对照测试。运行时仍需校验环境及权限。

## 5.1 视觉方向探索

**何时使用：**探索清晰、有辨识度的设计方向，兼顾设计系统知识。

- **首选：[frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)**（具体 Skill；A / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**生成有辨识度的视觉风格和排版选择。**依赖/限制：**纯文本设计指导；具体界面实现仍需要 Agent 的 UI 编码能力。**CoolFlow 适配：**不限定技术栈；UI 原型不等于正式产品 UI。**核查依据：**[上游文件](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)，Git blob `a5333457c414d20d625f307df945842c0952ecc3`（2026-11-01）。

- **备选：[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md)**（具体 Skill；A / L2）。**核查通过（源码与依赖检查，未实机验证）** **能力：**检索风格、配色、字体、UX 规则和设计系统建议。**依赖/限制：**需同目录查询脚本及数据、Python 3；单复制 SKILL.md 不完整。**CoolFlow 适配：**安装整个 Skill 资源目录，不把框架示例变为 CoolFlow 默认技术栈。**核查依据：**[上游文件](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md)，Git blob `41f8e2fd7f8c568228d0b55186ebe3f7b4007377`（2026-11-01）。

## 5.2 生成多个 UI 版本比较

**何时使用：**快速生成可切换的多个交互和视觉版本。

- **首选：[prototype（UI）](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**生成用于回答单一问题的可丢弃原型（逻辑或 UI 两分支）。**依赖/限制：****必须连同 `LOGIC.md` 和 `UI.md`** 保存；逻辑分支可用独立 HTML，UI 分支需要可显示的路由/页面环境。**CoolFlow 适配：**放 `docs/work/<objective>/prototypes/`，完成验证后记录结论，不强制进入正式实现。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)，Git blob `a0044501fe0d385b4d8575b610188ede9b236ccf`（2026-11-01）。

- **备选：[design-shotgun](https://github.com/garrytan/gstack/blob/main/design-shotgun/SKILL.md)**（具体 Skill；B / L3）。**核查通过（源码与依赖检查，未实机验证）** **能力：**批量生成多种界面设计并在比较界面评审。**依赖/限制：**依赖 gstack 共享脚本、会话文件和运行环境。**CoolFlow 适配：**仅环境满足时原版运行；否则改用轻量 `prototype` UI 分支。**核查依据：**[上游文件](https://github.com/garrytan/gstack/blob/main/design-shotgun/SKILL.md)，Git blob `59f595100fbfe12788b70eeffbf346400b200c3c`（2026-11-01）。

