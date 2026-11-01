# CoolFlow Advisor — 精选推荐库（会话对齐版 V1）

**版本：2026-11-01。** 本版从现有候选库重新筛选，**仅保留本次对话中已研究、核查或明确讨论的具体场景和工具**。不采用后来扩充出的未经对齐条目。

## 使用规则

1. **按需读取：**用户明确给出阶段或具体任务后，先读本索引，再只读相关阶段文件。不得自动猜阶段或遍历整个仓库判断进度。
2. **推荐门槛：**阶段条目必须标为 **核查通过** 才能进入 Advisor 默认推荐。标为 **候选（未核查）** 的工具只能在用户要求探索候选时介绍，不能因为 A/B 等级较高就绕过核查。
3. **核查通过的定义：**已经核到上游具体文件/版本，阅读它的实际能力及限制，识别依赖/运行前提，并写明与 CoolFlow 文档及流程的适配方式；**不是**已实机安装、所有环境均可用，也不是经过 A/B 实验的效果证明。
4. **每场景最多两个：**优先推荐该场景首选；若环境不满足其必要依赖，选择已核查且实际可用的备选。若均不合适，建议直接使用现有 Agent，而不是强推外部工具。每次最多一个首选加一个备选。
5. **推荐等级与适配成本分开：**A 是优先考虑，B 是常规候选，C 为待进一步研究；L0 可直接使用、L1 修改文档路径/交接或补少量文本依赖、L2 需要子 Agent/脚本/服务、L3 深度依赖原框架。**L0 和 L1 不因轻量修改降低推荐级别**；L2/L3 也不自动扣分，但须先满足依赖条件。
6. **通用而非技术栈特定：**不收录 Expo、React Native 等特定解决方案作为 CoolFlow 默认方法。针对某次项目可另行查询专用工具，但不能悄悄加入本库。
7. **CoolFlow 始终拥有文档所有权：**遵守项目本地 `docs/documentation.md`，不强制新建第二套 Spec、Roadmap、Task Tracker；探索阶段可选笔记，第六阶段才创建正式 Spec。人类验收与发布授权必须分离。
8. **不自动安装和执行：**Advisor 只提供建议。原版 Skill 的路径/脚本/权限需在实际安装时复核。需要 Fork/修改时记录原始 Commit、许可及差异。

## 八阶段目录

| 阶段 | 参考文件 | 具体场景数 |
| --- | --- | ---: |
| 1. Idea → Brainstorm | [01-idea-brainstorm.md](01-idea-brainstorm.md) | 5 |
| 2. Lightweight Strategic DDD | [02-strategic-ddd.md](02-strategic-ddd.md) | 3 |
| 3. Concept Prototype → Validation | [03-concept-prototype.md](03-concept-prototype.md) | 4 |
| 4. Roadmap | [04-roadmap.md](04-roadmap.md) | 3 |
| 5. UI Prototype | [05-ui-prototype.md](05-ui-prototype.md) | 2 |
| 6. Design Spec Loop | [06-design-spec.md](06-design-spec.md) | 4 |
| 7. Implementation Loop | [07-implementation.md](07-implementation.md) | 6 |
| 8. Human Acceptance → Documentation Sync → Release | [08-acceptance-release.md](08-acceptance-release.md) | 5 |

**总计：32 个细分场景，47 个工具位置（含跨场景重复）。其中 46 个位置已完成源码与依赖核查、1 个位置保留为未核查候选。**同一 Skill 在不同场景可能重复出现，这些不是独立工具数量。**

## 核查与证据说明

- **来源：**条目直接链接原作者的具体 Skill 文件（不是整个套件首页），附核查时 Git Blob SHA；同名工具必须核对仓库。
- **能力：**说明它针对该任务解决什么问题，避免仅依据 Stars、安装量打分。
- **依赖：**明确它是否调用其他 Skills、Python/CLI、API Key、子 Agent 或 gstack 的共享脚本。可单独安装不等于可独立运行。
- **适配：**说明文档路径、执行衔接、必要权限和 CoolFlow 约定，不因轻量改动降低优先级。
- **受控效果与本机实测：**本次未进行。核查通过不代表跑通了用户的 Codex 或其他 Harness，也不意味着某个 Skill 有经实证证明的领先地位。
- **后续维护：**上游文件和依赖变化时重新核验；GitHub 推荐库更新不会自动同步已安装的 Advisor Skill。

## 边界

CoolFlow Advisor 是**按需推荐**的精选 Skill 索引，不是阶段感知引擎、强制安装器或 workflow orchestrator。三个 Loops 保持既有方法论定义，本库不另建流程状态文件。

- [CoolFlow 方法论](../../../methodology/flow.md)
- [CoolFlow 文档规范](../../../standards/documentation.md)
- [Advisor Skill 入口](../SKILL.md)
