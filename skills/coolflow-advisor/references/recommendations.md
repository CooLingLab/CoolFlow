# CoolFlow Advisor — 精选推荐库（初版草稿）

**状态：待复核初选，不代表已全部亲测或已批准收录。** 整理日期：2026-11-01。此处记录的是经过初步筛选的具体能力，而不是安装整个工程套件的建议。

## 使用方式

1. 用户明确指定当前开发阶段，或直接说明当前要解决的具体任务；**不做阶段感知**、不读取项目状态推断阶段。
2. 先根据下表找到**当前阶段**的文件，只读取对应文件；不要一次加载八份。
3. 在对应场景中优先考虑首选，备选只作为不同约束下的选择；通常每个场景不超过两个推荐。
4. 推荐的是**具体 Skill、方法或工具**，不是 Superpowers、gstack、PM Skills 之类的整个集合。若组件有依赖，明确说明。
5. 可轻量修改的 Skill **不因轻量修改自动降级**。例如 Superpowers brainstorming 仍是 A 级候选，保留核心思考方法，调整文档路径与强制下游交接即可。
6. 优先延用用户现有工具；不必为了使用推荐而安装。需要最新版本、价格或安装支持时再联网核实。
7. 来源信息以官方项目为准；对于未经本地测试或需要适配的条目，不能声称“开箱即用”。
8. 候选调整和正式收录修改必须由用户明确批准。此库不自动安装 Skill、修改应用或执行发布。

## 八阶段索引

| CoolFlow 阶段 | 推荐文件 | 具体任务场景数 |
| --- | --- | ---: |
| 1. Idea → Brainstorm | [01-idea-brainstorm.md](01-idea-brainstorm.md) | 5 |
| 2. Lightweight Strategic DDD | [02-strategic-ddd.md](02-strategic-ddd.md) | 4 |
| 3. Concept Prototype → Validation | [03-concept-prototype.md](03-concept-prototype.md) | 5 |
| 4. Roadmap | [04-roadmap.md](04-roadmap.md) | 4 |
| 5. UI Prototype | [05-ui-prototype.md](05-ui-prototype.md) | 5 |
| 6. Design Spec Loop | [06-design-spec.md](06-design-spec.md) | 5 |
| 7. Implementation Loop | [07-implementation.md](07-implementation.md) | 7 |
| 8. Human Acceptance → Documentation Sync → Release | [08-acceptance-release.md](08-acceptance-release.md) | 6 |

共 41 个细粒度任务场景、77 个首选/备选位置（同一 Skill 可出现在多个任务中，**不是独立工具数量**）。

## 三个 Loops 不是额外阶段

- **Design Spec Loop：**对应 Stage 6 的 Spec 草稿、架构取舍、独立评审与计划拆分。
- **Implementation Loop：**对应 Stage 7 的编码、测试、代码审查、Spec Conformance 和 Fix。
- **Evolution Loop：**当任意阶段出现新证据时，重新评估问题、假设或路线图；可按任务返回 Stage 1、3、4 等，不自动改变流程状态。

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
