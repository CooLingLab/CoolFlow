# Stage 7 — Implementation Loop

[精选推荐索引](recommendations.md) · [CoolFlow 文档规范](../../../standards/documentation.md)

**目标：**Coding → Testing → Review → Spec Conformance → Fix；以证据验证实现。

**收录依据：**仅保留本对话已讨论的具体工具；每个任务最多两个选择。核查通过=阅读官方源码及关联依赖、确定 CoolFlow 适配方案，不等于已安装或做过受控对照测试。运行时仍需校验环境及权限。

## 7.1 按计划执行编码

**何时使用：**按已确认 Spec/计划小步实现并验证。

- **首选：[executing-plans](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**按实现计划逐任务执行、检查与交付。**依赖/限制：**当前版明确为同一会话内执行，依赖可用的代码与测试工具；部分下游审查需适配。**CoolFlow 适配：**以 CoolFlow Spec 为准，不强制引入额外任务控制器。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md)，Git blob `ac77129d7c695734105004b6da10169de8d13df3`（2026-11-01）。

- **备选：[implement](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement/SKILL.md)**（具体 Skill；B / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**按 Spec 或 ticket 实现并运行测试。**依赖/限制：**Ticket 模式依赖 tracker；还会调用 `tdd` Skill。**CoolFlow 适配：**无 ticket 时基于本地 Spec；按需补装或内化 TDD 方法。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement/SKILL.md)，Git blob `bd49e472984c7b99aac40286fdae749bb955a842`（2026-11-01）。

## 7.2 测试驱动开发

**何时使用：**需要 Red-Green-Refactor、行为测试边界。

- **首选：[tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)**（具体 Skill；A / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**围绕行为和质量约束执行 Red-Green-Refactor。**依赖/限制：**需项目有实际可运行的测试环境。**CoolFlow 适配：**按项目测试框架执行，不固定技术栈。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)，Git blob `01eadaa34e7c9a63a67d6dc3cce1cc81b0e49985`（2026-11-01）。

- **备选：[test-driven-development](https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md)**（具体 Skill；A / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**强调先看测试失败，再实现最小可通过代码。**依赖/限制：**需项目测试工具，原版倾向强制对所有代码修改使用 TDD。**CoolFlow 适配：**只在适合的代码变更中调用，避免对探索性原型机械应用。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md)，Git blob `46838cc9e893c06259e3bdad0fc2425b36242f15`（2026-11-01）。

## 7.3 Bug 根因分析

**何时使用：**先复现、定位因果，再修复和回归。

- **首选：[systematic-debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md)**（具体 Skill；A / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**先定位根因、获取证据后修复。**依赖/限制：**需要真实代码、日志或运行环境才能验证猜想。**CoolFlow 适配：**真实复现及测试结果作为结论证据。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md)，Git blob `62fc752aaef59a8bbed5d305f4cadc60f8ae07ed`（2026-11-01）。

- **备选：[diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md)**（具体 Skill；A / L1）。**核查通过（源码与依赖检查，未实机验证）** **能力：**将复杂 bug 诊断分阶段为假设、实验、定位和修复。**依赖/限制：**需真实运行证据；部分约定会读取 GLOSSARY 与 ADR。**CoolFlow 适配：**优先读 `docs/domain.md` 与相关 ADR/solutions，不强制创建 glossary。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md)，Git blob `d039541ddd1c46e6ddbd662fe99d49b686fc5e12`（2026-11-01）。

## 7.4 代码审查

**何时使用：**围绕 Diff、Spec 与编码标准检查风险。

- **首选：[code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md)**（具体 Skill；A / L2）。**核查通过（源码与依赖检查，未实机验证）** **能力：**按 Standards 与 Spec 两个视角复核代码变更。**依赖/限制：**原版并行调用两个审查子 Agent；需真实 Diff 和 Spec。**CoolFlow 适配：**需宿主有子 Agent，或明确改成顺序审查而非声称原版运行。**核查依据：**[上游文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md)，Git blob `83183e0ad36fd0eef25d37c7e483284b7e34c1f0`（2026-11-01）。

- **备选：[review](https://github.com/garrytan/gstack/blob/main/review/SKILL.md)**（具体 Skill；B / L3）。**核查通过（源码与依赖检查，未实机验证）** **能力：**面向 PR 的多角度代码审查。**依赖/限制：**依赖 gstack 共享 preamble、命令和完整 repo 环境。**CoolFlow 适配：**具备 gstack 支持时使用；不自动修改或发布。**核查依据：**[上游文件](https://github.com/garrytan/gstack/blob/main/review/SKILL.md)，Git blob `8ae90451443897b3e68c796ab0c75960d5f48553`（2026-11-01）。

## 7.5 实施结果验证

**何时使用：**在声称完成前核查测试、输出与 Spec。

- **首选：[verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md)**（具体 Skill；A / L0）。**核查通过（源码与依赖检查，未实机验证）** **能力：**完成声明前要求实际测试结果而非猜测。**依赖/限制：**需可执行验证命令/可见工具输出。**CoolFlow 适配：**映射到当前 CoolFlow Spec 验收标准；不取代人工验收。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md)，Git blob `7d45333cc4a49c57a80df6c1fe2fa777a207afbc`（2026-11-01）。

## 7.6 多任务子 Agent 协作

**何时使用：**任务独立且具备真实子 Agent 调度环境。

- **首选：[subagent-driven-development](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md)**（具体 Skill；A / L2）。**核查通过（源码与依赖检查，未实机验证）** **能力：**将独立任务交给新上下文子 Agent 并逐步复核。**依赖/限制：**必须有实际子 Agent 调度与隔离能力，且要管理并行成本。**CoolFlow 适配：**宿主不支持时不推荐运行原版；不内置多 Agent 引擎。**核查依据：**[上游文件](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md)，Git blob `ea170ed101d61a52fdee0ade8368ec0723980a5c`（2026-11-01）。

