# 阶段活动与 Skill 边界

[English](activities.md) | **简体中文**

**状态：讨论稿。** 本文是[开发流程](flow.zh-CN.md)的非规范性配套文档。它识别每个阶段中可能出现的不同活动，以及在边界达成一致后，哪些位置可能适合使用 Skill。

本文不新增阶段，不要求每个项目执行所有活动，也不替代[文档规范](../standards/documentation.zh-CN.md)。八个阶段和三个 Adaptive Loops 仍以 [flow.zh-CN.md](flow.zh-CN.md) 的定义为准。

## 本文档的推进方式

活动逐个阶段与开发者确认。阶段经过讨论并确认前，其内容标记为 `讨论中` 或 `尚未开始`。已确认的活动清单是双方对工作的共同理解，不是强制检查表。

每个已确认阶段使用同一张表：

- **活动：** 阶段内一项独立的工作。
- **回答的问题：** 该活动要解决的问题。
- **核心产出：** 该活动产生的结果或证据。
- **边界：** 哪些属于本活动，哪些属于相邻活动。

在所有阶段边界达成一致前，刻意不分配 Skill。

## 阶段状态

| 阶段 | 状态 |
| --- | --- |
| 1. Idea → Brainstorm | 已确认（2026-11-05） |
| 2. Lightweight Strategic DDD | 已确认（2026-11-05） |
| 3. Concept Prototype → Validation | 尚未开始 |
| 4. Roadmap | 尚未开始 |
| 5. UI Prototype | 尚未开始 |
| 6. Design Spec Loop | 尚未开始 |
| 7. Implementation Loop | 尚未开始 |
| 8. Human Acceptance → Documentation Sync → Release | 尚未开始 |
| Evolution Loop（跨阶段） | 尚未开始 |

## 1. Idea → Brainstorm

状态：`已确认`（2026-11-05）

| ID | 活动 | 回答的问题 | 核心产出 | 边界 |
| --- | --- | --- | --- | --- |
| 1.1 | 理解用户与问题（含与决策相称的用户研究） | 谁在什么情境下遇到什么困难？ | 用户、场景、问题、已知证据，以及收集证据时的方法、来源和日期 | 不研究竞品，不提出方案 |
| 1.2 | 研究竞品与替代方案 | 这个问题目前是如何被解决的？ | 直接竞品、间接替代方案、变通做法、来源与研究日期 | 不决定我们要做什么，也不把竞品功能当作需求 |
| 1.3 | 定义问题边界 | 我们要解决哪个问题，不解决哪些问题？ | 问题陈述、目标用户边界、非目标与关键约束 | 不判断机会是否值得，也不设计方案 |
| 1.4 | 评估机会 | 现有方案的哪些缺口值得考虑，依据是什么？ | 机会假设、支持证据、反证与未知项 | 不承诺开发，也不展开功能 |
| 1.5 | 发散产品方向 | 有哪些不同思路可以解决该问题？ | 多个候选方向及其价值与代价比较 | 不收敛为最终范围，不编写 Spec |
| 1.6 | 形成产品假设 | 我们目前相信什么，最应先验证什么？ | 目标用户、价值主张、差异化假设与关键风险 | 不是已成立的结论，也不是 Roadmap |

### 理由与边界

- 1.1 与 1.2 收集不同证据：用户/问题证据与外部解决方案证据。将两者分开，可以避免把竞品功能当作
  用户需求。
- 当现有证据不足时，1.1 包含与决策相称的用户研究，例如访谈、观察或分析现有数据。研究深度与
  决策相称；发现需区分观察事实、用户陈述、解释和假设。用户研究是发现阶段的一项活动，不是
  独立阶段或强制关卡。
- 1.3 在判断机会之前先框定问题。它是本文提出的细化；当前 `flow.zh-CN.md` 将这一框定视为发现和
  机会判断工作的一部分，而不是一个单独命名的步骤。
- 1.4 使用 1.1–1.3 判断机会。它不选择功能，也不承诺范围。
- 1.5 发散多个方向；1.6 将选定的方向转成一个可验证的假设。设计与执行验证实验属于第 3 阶段，
  不属于本阶段。
- 研究深度与决策相称。一个范围较小的功能可能只需要快速扫描，或明确决定无需更深入的研究。
- 本阶段不创建正式 Spec。发现笔记与证据在有帮助时可以放在当前工作目录中。

### 参考来源

本文的拆分对照了以下公开实践。它们为边界选择提供参考，但不是 CoolFlow 的规范：

- Teresa Torres，[Product Discovery Basics](https://www.producttalk.org/2021/11/product-discovery/)：
  成果 → 机会 → 解决方案；将机会空间与解决方案空间分开。
- Design Council，[The Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/)：
  在开发与交付方案之前，先发现并定义问题。
- Nielsen Norman Group，[Design Thinking 101](https://www.nngroup.com/articles/design-thinking/)：
  共情、定义、构思、原型和测试是不同的活动。
- Marty Cagan，[The Four Big Risks](https://svpg.com/four-big-risks/)：价值、可用性、可行性和
  商业可行性作为评估维度。
- Strategyn，[Jobs-to-be-Done](https://strategyn.com/jobs-to-be-done/)：从尚未满足的成果出发，
  而不是从产品功能出发。
- Strategyzer，[Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas)：
  分别描述客户问题与拟提供的价值，再验证两者的匹配。

## 2. Lightweight Strategic DDD

状态：`已确认`（2026-11-05）

**范围：** 初始战略领域发现。本阶段产生一个暂定的领域模型。战术领域设计——聚合、实体、值对象、
仓储、领域事件和事务边界——推迟到 Design Spec Loop（第 6 步）。

| ID | 活动 | 回答的问题 | 核心产出 | 边界 |
| --- | --- | --- | --- | --- |
| 2.1 | 界定领域范围与参与者 | 这个产品涉及哪一部分业务、哪些角色和工作对象？ | 领域范围、参与者/角色、核心工作对象、核心与辅助部分 | 不重新定义第 1 阶段的产品问题或目标用户；不设计技术模块 |
| 2.2 | 建立统一语言与核心概念 | 每个核心术语在这个领域里是什么意思？ | 术语表、定义、同义词与歧义、核心概念及关系 | 不收录所有 UI 标签或代码命名；跨上下文冲突留给 2.3 |
| 2.3 | 划分限界上下文 | 哪些概念共享一致含义？同一个术语在哪里含义不同？ | 上下文列表、每个上下文的语言与职责、上下文之间的关系 | 不是微服务、代码模块或部署边界；不决定接口 |
| 2.4 | 定义核心业务规则与不变量 | 哪些条件必须始终成立，状态如何变化？ | 不变量、业务规则、状态转换、例外与失败条件 | 不规定实现算法或数据库约束；不替代验收条件 |
| 2.5 | 用业务场景检验并确认模型 | 模型能否解释真实流程和边界情况，哪些仍未解决？ | 关键场景走查、修正后的模型、已确认理解、开放问题 | 不是用户验收或原型测试；不验证产品假设；不编写 Spec |

### 理由与边界

- 2.1 与 2.2 分开：2.1 确定观察范围；2.2 定义术语含义。合并这两项容易把产品名称、UI 标签和
  技术标识混入领域语言。
- 2.3 识别的是**语义**边界。限界上下文之后可能影响模块或服务边界，但在这里不决定部署或接口。
- 2.4 记录业务规则与不变量，而不是实现约束。数据库约束和代码级强制属于后续设计与实现。
- 2.5 使用业务叙述和纸上走查，暴露缺失的概念与规则。它不是原型、用户测试或验收决定。
- `docs/domain.md` 中记录的模型是暂定且持续演进的。战术设计和代码级模型细化发生在第 6、7 步；
  新的领域理解可以通过 Evolution Loop 回到本阶段。
- 本阶段与项目复杂度相称。小型或熟悉的领域可能只需要核心术语、关键规则和一个上下文。不要为了
  执行 DDD 而虚构多个上下文。EventStorming、Domain Storytelling 和上下文映射都是可选方法。

### 参考来源

本文的拆分对照了以下公开实践。它们为边界选择提供参考，但不是 CoolFlow 的规范：

- Eric Evans，[Whirlpool Process of Model Exploration](https://www.domainlanguage.com/ddd/whirlpool/)：
  模型探索不是开发流程，应嵌入迭代式设计。
- Martin Fowler，[Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html)：
  共享的严格语言随领域理解不断演进。
- Martin Fowler，[Bounded Context](https://martinfowler.com/bliki/BoundedContext.html)：
  大模型被划分为语义上下文；上下文不是代码模块。
- DDD Crew，[DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process)：
  领域发现、分解、战略和战术设计是迭代过程，不是线性序列。
- Domain Storytelling，[DDD with Domain Storytelling](https://domainstorytelling.org/domain-driven-design)：
  故事支持战略设计、统一语言以及后续的战术设计。
- EventStorming，[EventStorming](https://www.eventstorming.com/)：协作式领域探索可以发现事件、
  边界和开放问题。

## 3. Concept Prototype → Validation

状态：`尚未开始`

## 4. Roadmap

状态：`尚未开始`

## 5. UI Prototype

状态：`尚未开始`

## 6. Design Spec Loop

状态：`尚未开始`

## 7. Implementation Loop

状态：`尚未开始`

## 8. Human Acceptance → Documentation Sync → Release

状态：`尚未开始`

## Evolution Loop（跨阶段）

Evolution Loop 是跨阶段的。其活动边界将在八个阶段之后讨论，但不会把它当作第九个阶段，也不会
把它限定为发布后的步骤。

## 变更记录

| 日期 | 变更 |
| --- | --- |
| 2026-11-03 | 创建文档骨架与写作约定。 |
| 2026-11-05 | 确认第 1 阶段的活动边界，并补充支撑理由。 |
| 2026-11-05 | 确认第 2 阶段的初始领域发现边界；战术设计推迟到第 6 步。 |
| 2026-11-05 | 明确第 1 阶段的用户/问题发现包含与决策相称的用户研究。 |

**翻译说明：** 本文是英文 [Stage activities and Skill boundaries](activities.md) 的中文翻译。
英文是权威版本；如出现歧义，以英文为准。
