# CoolFlow Advisor — 精选推荐库 V1

**状态：场景级候选库；本版未记录任何条目完整的四项核查证据，因此目前没有可默认推荐的库内条目。A/B 是初评，不代表完成核查、统一对照实验或全部亲测。** 更新日期：2026-11-01。此处记录的是经过初步筛选的具体能力，而不是安装整个工程套件的建议。

## 使用方式

1. 用户明确指定当前开发阶段，或直接说明当前要解决的具体任务；**不做阶段感知**、不读取项目状态推断阶段。
2. 先根据下表找到**当前阶段**的文件，只读取对应文件；不要一次加载八份。
3. 先按下方核查门槛筛选，再考虑候选顺序、等级和用户约束；每个场景最多保留两个候选，默认推荐最多一个加一个备选。没有合格条目时明确说明，可建议现有 Agent 或简单人工方法；不得把未核查候选充作默认推荐。
4. 推荐的是**具体 Skill、方法或工具**，不是 Superpowers、gstack、PM Skills 之类的整个集合。若组件有依赖，明确说明。
5. 可轻量修改的 Skill **不因轻量修改自动降级**。例如 Superpowers brainstorming 仍是 A 级候选，保留核心思考方法，调整文档路径与强制下游交接即可。
6. 优先延用用户现有工具；不必为了使用推荐而安装。需要最新版本、价格或安装支持时再联网核实。
7. 来源信息以官方项目为准；未经实测与未核查是不同状态。对于未经实测或需要适配的条目，不声称“已实测”或“开箱即用”。
8. 推荐库的后续收录、删除和重排需要用户授权。此库不自动安装 Skill、修改应用或执行发布。

## 八阶段索引

| CoolFlow 阶段 | 推荐文件 | 具体任务场景数 |
| --- | --- | ---: |
| 1. Idea → Brainstorm | [01-idea-brainstorm.md](01-idea-brainstorm.md) | 5 |
| 2. Lightweight Strategic DDD | [02-strategic-ddd.md](02-strategic-ddd.md) | 4 |
| 3. Concept Prototype → Validation | [03-concept-prototype.md](03-concept-prototype.md) | 5 |
| 4. Roadmap | [04-roadmap.md](04-roadmap.md) | 4 |
| 5. UI Prototype | [05-ui-prototype.md](05-ui-prototype.md) | 7 |
| 6. Design Spec Loop | [06-design-spec.md](06-design-spec.md) | 5 |
| 7. Implementation Loop | [07-implementation.md](07-implementation.md) | 7 |
| 8. Human Acceptance → Documentation Sync → Release | [08-acceptance-release.md](08-acceptance-release.md) | 6 |

共 43 个细粒度任务场景、79 个候选位置（同一 Skill 可出现在多个任务中，**不是独立工具数量**）。

## 三个 Loops 不是额外阶段

- **Design Spec Loop：**对应 Stage 6 的 Spec 草稿、架构取舍、独立评审与计划拆分。
- **Implementation Loop：**对应 Stage 7 的编码、测试、代码审查、Spec Conformance 和 Fix。
- **Evolution Loop：**当任意阶段出现新证据时，重新评估问题、假设或路线图；可按任务返回 Stage 1、3、4 等，不自动改变流程状态。

## 默认推荐的核查门槛

每个具体条目在相关版本和使用场景下，须记录以下四项均已核查且适用，才可标为 **核查通过**，进入默认推荐筛选：

1. **来源：**官方来源、具体文件或组件与核查版本/日期可追溯。
2. **能力：**查阅上游内容，确认其实际能力与该场景相符，记录限制。
3. **依赖：**核查所需 Skill、脚本、服务、权限及运行条件，区分安装和运行。
4. **适配：**核查与 CoolFlow 文档、阶段交接、人类确认和发布授权的关系，记录必要修改及适用环境。

缺任何一项证据、存在未解决冲突或无法判断时，状态为 **候选（核查未完成）**，不进入默认推荐；此前的 A/B/C、L0–L3 和候选顺序均只是初评，不能代替核查。四项均通过也不意味着必须优先选用：仍需满足用户环境和任务约束；C 级原则上不默认推荐。核查通过与实机安装或受控对比测试是不同维度：未实测不自动等于未核查，须如实说明实际验证范围。

用户明确要求探索候选时，可列出未核查工具及缺失的核查项，清楚标为候选；若当次完成四项核查，可基于当次证据提出建议，并注明该结论尚未写入库。维护者更新状态时，应记录各项证据链接、版本或 Commit、日期、结论与测试情况；来源或依赖变化时重新核查。技术栈保持无关，按具体项目环境判断适用性。

## 推荐等级与适配等级（互相独立）

- **A：**高度匹配任务、优先推荐；**B：**明确有用、常规或备选推荐；**C：**实验候选；**待复核：**尚缺足够证据，不代表质量低。等级是初步选型而不是同模型同任务的基准测试名次。
- **L0：**可直接用；**L1：**改输出路径、流程交接或补少量文本依赖；**L2：**涉及子 Agent、脚本或复杂配置；**L3：**明显依赖原套件运行环境/权限；**待核实：**未验证原文件和依赖。
- **硬规则：L0 和 L1 一律不因适配成本降低推荐等级。** L2/L3 也不自动扣分，但必须解释依赖、成本和运行前提。
- 可单独安装 ≠ 可独立运行。必须区分具体 Skill 与套件脚本、其他 Skill、配置、第三方服务；不默认把单个 `SKILL.md` 当完整安装包。
- 保留上游核心方法；以 CoolFlow `docs/documentation.md` 为文档权威，路径、跨阶段交接等适合 L1 的地方轻量修改。需记录来源、原版本/Commit、适配差异及许可证，不自动覆盖已有修改。
- GitHub 热度或安装量不等于受控实验有效性。未核实的链接、依赖、运行环境应明确标为待核实，不编造“公认最佳”。

## 适配与收录判定

- **直接使用：**Skill 不要求改变 CoolFlow 已有的文档所有权、人类确认和发布授权。
- **轻量适配：**修改输出路径、移除强制跨阶段交接、补充很小的依赖说明；**不降低推荐优先级**。
- **依赖套件：**需要专门脚本、共享前置文件或整体运行环境。可借鉴方法，但不得把单个 SKILL.md 当成可独立运行。
- **结构冲突：**强制建立第二套 Spec、任务状态、文档树或自动发布路径；先决定谁是唯一事实来源，不默认安装。
- **暂无必要：**现有 Agent 指令或人工方法已足够时，明确建议不用新增工具。

每条应记录来源、使用场景、选择理由、风险/局限和 CoolFlow 适配建议。下一轮人工复核时再补充实际使用体验、兼容性测试与更新日期。

## 相关资料

- [CoolFlow 方法论](../../../methodology/flow.md) 与 [文档标准](../../../standards/documentation.md)
- [完整生态目录](../../../flowecosystem/catalog.md)：广义项目/方法备查，**不是**精选推荐的另一份副本
- [框架比较](../../../flowecosystem/framework-comparison.md)：用于判断整套框架是否会与 CoolFlow 冲突

**维护原则：**本目录是 Advisor 的本地离线推荐知识源。GitHub 维护版本；全局安装时需安装包含 `references/` 的完整 Skill 目录。只更新 GitHub 不会自动更新用户本地安装。

## 重点适配实例（2026-11-01）

| 工具 | 初评 | 核查到的依赖或适配 |
| --- | --- | --- |
| [grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) | A/L1 | 入口转调 `grilling`，补装或合并其追问方法即可。 |
| [grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) | A/L1 | 调用 `grilling` 与 `domain-modeling`；按 CoolFlow 文档规范输出。 |
| [Superpowers brainstorming](https://github.com/obra/superpowers/tree/main/skills/brainstorming) | A/L1 | 保留讨论与方案权衡；改路径、取消强制交接 `writing-plans`。 |
| [Superpowers writing-plans](https://github.com/obra/superpowers/tree/main/skills/writing-plans) | A/L1 | 改计划文档路径和后续执行交接，不创建第二套权威 Spec。 |
| [to-spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec) | A/L1 | 从 Issue Tracker 输出改为 `docs/work/<objective>/spec.md`。 |
| [code-review](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review) | A/L2 | 原版使用独立审查 Agent；需要宿主支持或明确适配。 |
| [subagent-driven-development](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development) | A/待核实 | 需要子 Agent 调度能力，不能仅复制 SKILL.md 声称可独立运行。 |
| [gstack design-shotgun](https://github.com/garrytan/gstack/tree/main/design-shotgun) | B/L3 | 依赖 gstack 共享脚本、会话机制；记录为有条件的候选，完成四项核查后再考虑推荐。 |
| [gstack ship](https://github.com/garrytan/gstack/tree/main/ship) | B/L3 | 需要共享运行环境，并涉及提交/推送/PR 等高权限动作；保持独立人类授权。 |

这些结论来自现有上游源码和文档初核，**不是所有候选的实机安装测试**。阶段文件保留完整具体场景与最多两个候选；上表仅记录部分初核发现，不代表四项核查均已完成。
