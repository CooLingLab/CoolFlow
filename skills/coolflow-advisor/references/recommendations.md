# CoolFlow Advisor — 精选推荐库 V1

**状态：场景级初选，A/B 等级并不代表已通过统一对照实验或全部亲测。** 更新日期：2026-11-01。此处记录的是经过初步筛选的具体能力，而不是安装整个工程套件的建议。

## 使用方式

1. 用户明确指定当前开发阶段，或直接说明当前要解决的具体任务；**不做阶段感知**、不读取项目状态推断阶段。
2. 先根据下表找到**当前阶段**的文件，只读取对应文件；不要一次加载八份。
3. 在对应场景中优先考虑首选，备选只作为不同约束下的选择；通常每个场景不超过两个推荐。
4. 推荐的是**具体 Skill、方法或工具**，不是 Superpowers、gstack、PM Skills 之类的整个集合。若组件有依赖，明确说明。
5. 可轻量修改的 Skill **不因轻量修改自动降级**。例如 Superpowers brainstorming 仍是 A 级候选，保留核心思考方法，调整文档路径与强制下游交接即可。
6. 优先延用用户现有工具；不必为了使用推荐而安装。需要最新版本、价格或安装支持时再联网核实。
7. 来源信息以官方项目为准；对于未经本地测试或需要适配的条目，不能声称“开箱即用”。
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

共 43 个细粒度任务场景、79 个首选/备选位置（同一 Skill 可出现在多个任务中，**不是独立工具数量**）。

## 三个 Loops 不是额外阶段

- **Design Spec Loop：**对应 Stage 6 的 Spec 草稿、架构取舍、独立评审与计划拆分。
- **Implementation Loop：**对应 Stage 7 的编码、测试、代码审查、Spec Conformance 和 Fix。
- **Evolution Loop：**当任意阶段出现新证据时，重新评估问题、假设或路线图；可按任务返回 Stage 1、3、4 等，不自动改变流程状态。

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
| [subagent-driven-development](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development) | A/L2 | 需要子 Agent 调度能力，不能仅复制 SKILL.md 声称可独立运行。 |
| [gstack design-shotgun](https://github.com/garrytan/gstack/tree/main/design-shotgun) | B/L3 | 依赖 gstack 共享脚本、会话机制；建议保留为条件备选。 |
| [gstack ship](https://github.com/garrytan/gstack/tree/main/ship) | B/L3 | 需要共享运行环境，并涉及提交/推送/PR 等高权限动作；保持独立人类授权。 |

这些结论来自现有上游源码和文档初核，**不是所有候选的实机安装测试**。阶段文件保留完整具体场景与最多两个工具推荐。
