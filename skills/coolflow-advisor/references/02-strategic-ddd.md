# Stage 2 — Lightweight Strategic DDD

[精选推荐索引](recommendations.md) · [CoolFlow 文档规范](../../../standards/documentation.md)

**目标：**统一领域语言、业务规则和边界；避免过度 DDD。

**收录依据：**仅保留本对话已讨论的具体工具；每个任务最多两个选择。核查通过=阅读官方源码及关联依赖、确定 CoolFlow 适配方案，不等于已安装或做过受控对照测试。运行时仍需校验环境及权限。

## 2.1 领域概念建模

**何时使用：**厘清核心术语、领域规则及边界。

- **首选：[domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**挑战领域术语、业务规则、边界案例和重大领域决策。**依赖/限制：**原版默认根目录 `GLOSSARY.md` 与自己的 ADR 习惯。**CoolFlow 适配：**映射到 `docs/domain.md`；仅重大决策使用可选 `docs/adr/`。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)，Git blob `a4438c6879c517d1a08e2b5fbca049b632688dfe`（2026-11-01）。

## 2.2 访谈并沉淀领域模型

**何时使用：**在追问同时更新领域概念与规则。

- **首选：[grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**追问业务规则并同步沉淀术语和决策。**依赖/限制：**本身仅调用 `grilling` 与 `domain-modeling` 两个 Skill。**CoolFlow 适配：**补齐这两个文本依赖并遵守 CoolFlow 的 domain/ADR 所有权。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)，Git blob `62b9efb6f991d1b229adee7506962f13ced0c499`（2026-11-01）。

## 2.3 统一语言与概念歧义

**何时使用：**存在同义词、歧义词或不同业务方定义冲突。

- **首选：[domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**挑战领域术语、业务规则、边界案例和重大领域决策。**依赖/限制：**原版默认根目录 `GLOSSARY.md` 与自己的 ADR 习惯。**CoolFlow 适配：**映射到 `docs/domain.md`；仅重大决策使用可选 `docs/adr/`。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)，Git blob `a4438c6879c517d1a08e2b5fbca049b632688dfe`（2026-11-01）。

- **备选：[ubiquitous-language](https://www.skills.sh/mattpocock/skills/ubiquitous-language)**（具体 Skill；C / 待核实）。**候选（上游当前来源/依赖尚未核查，不进入默认推荐）** **能力：**统一领域语言与术语（历史研究候选）。**依赖/限制：**无法确认当前上游独立 SKILL.md 的路径及依赖。**CoolFlow 适配：**仅供检索候选，核查通过前不作为默认推荐。**缺失证据：**当前上游的具体 SKILL.md 及依赖未确认。

