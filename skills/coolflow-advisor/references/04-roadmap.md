# Stage 4 — Roadmap

[精选推荐索引](recommendations.md) · [CoolFlow 文档规范](../../../standards/documentation.md)

**目标：**确定 MVP/当前版本与后续版本的取舍，不把 Roadmap 混同实施任务表。

**收录依据：**仅保留本对话已讨论的具体工具；每个任务最多两个选择。核查通过=阅读官方源码及关联依赖、确定 CoolFlow 适配方案，不等于已安装或做过受控对照测试。运行时仍需校验环境及权限。

## 4.1 功能优先级排序

**何时使用：**明确做什么、不做什么、为什么。

- **首选：[prioritize-features](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/prioritize-features/SKILL.md)**（具体 Skill；B / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**结合影响、投入和风险对功能进行取舍。**依赖/限制：**文档引用 `prioritization-frameworks` 作为方法说明。**CoolFlow 适配：**按需补充轻量文本依赖，不制造虚假分数；更新 `docs/roadmap.md`。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/prioritize-features/SKILL.md)，Git blob `e58190d88a63f2f429ad04743dc6427751476ba7`（2026-11-01）。

- **备选：[pm-prioritization](https://github.com/Uxcel-Lab/product-skills/blob/main/pm/processes/prioritization/SKILL.md)**（具体 Skill；B / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**根据战略选择 ICE/RICE/MoSCoW 等合适的排序方式。**依赖/限制：**引用同库其他 PM Skills 作为可选交接，但文件声明不存在时可独立继续。**CoolFlow 适配：**不强制继承其它 PM 流程，取舍写回 CoolFlow Roadmap。**核查依据：**[上游文件](https://github.com/Uxcel-Lab/product-skills/blob/main/pm/processes/prioritization/SKILL.md)，Git blob `37d15b643711c4af79e1cf6e3f2d58d3280c26ed`（2026-11-01）。

## 4.2 制订成果导向 Roadmap

**何时使用：**将 MVP 和未来版本映射为可验证用户结果。

- **首选：[outcome-roadmap](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/outcome-roadmap/SKILL.md)**（具体 Skill；B / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**将功能导向 Roadmap 转为可验证成果导向。**依赖/限制：**文本 Skill；原版输出通常采用时间盒/季度风格。**CoolFlow 适配：**以 MVP/未来版本表达，不强制季度计划。**核查依据：**[上游文件](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/outcome-roadmap/SKILL.md)，Git blob `c51cfa226a50ab9f14367adc4c54af14b2562da9`（2026-11-01）。

## 4.3 挑战版本范围与过度开发

**何时使用：**发现 MVP 膨胀或价值定位不足。

- **首选：[plan-ceo-review](https://github.com/garrytan/gstack/blob/main/plan-ceo-review/SKILL.md)**（具体 Skill；B / L2）。**核查通过（源码与依赖检查，未实机验证）** **能力：**以创始人视角挑战 MVP 范围和价值假设。**依赖/限制：**gstack 的 preamble、hooks 和脚本/状态文件需原版环境。**CoolFlow 适配：**仅在原版环境满足时调用；否则用经适配的提问方法，用户决定取舍。**核查依据：**[上游文件](https://github.com/garrytan/gstack/blob/main/plan-ceo-review/SKILL.md)，Git blob `c804a37a5b35b94eb43b834d7325b5ba46eda859`（2026-11-01）。

