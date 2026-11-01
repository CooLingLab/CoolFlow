# Stage 1 — Idea → Brainstorm

[精选推荐索引](recommendations.md) · [CoolFlow 方法论](../../../methodology/flow.md)

**阶段目标：**澄清问题、用户、现有替代方案、机会和产品假设；不要提前创建正式 Spec。

**状态：已收录场景级初选；A/B 表示选型判断，非统一受控 A/B 测试结果。** L0/L1 不因轻量适配扣分；依赖未经核实时明确标记，不声称可独立运行。

## 1.1 问题澄清与深度追问

**适用场景：**只有一个模糊想法，希望用问答找到真正的问题与边界。

- **首选： [grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)**（Skill）。**用途：**逐题追问，暴露未经验证的假设。 **局限：**原版依赖同仓库 grilling；只装入口文件可能无法独立运行。 **CoolFlow 适配：**补装 grilling 或将其追问法内化为 CoolFlow 轻量适配版；不强制写额外文件。 **等级：**A / L1。

- **备选： [interview-me](https://github.com/addyosmani/agent-skills/tree/main/skills/interview-me)**（Skill）。**用途：**以结构化问题收集需求、成功标准和约束。 **局限：**偏需求访谈；不能替代真实用户访谈。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**待复核 / 待核实（接入前核查）。

**选择建议：**需要高强度反问选 grill-me；需要较有条理的需求澄清选 interview-me。

## 1.2 新产品创意发散

**适用场景：**希望从产品、设计、工程三个视角探索解决方案。

- **首选： [brainstorm-ideas-new](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/brainstorm-ideas-new)**（Skill）。**用途：**多视角生成候选功能并标出验证假设。 **局限：**容易过早形成大功能清单；先明确用户问题。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / 待核实（接入前核查）。

- **备选： [idea-refine](https://github.com/addyosmani/agent-skills/tree/main/skills/idea-refine)**（Skill）。**用途：**帮助澄清和收敛初步概念。 **局限：**不是完整竞品研究。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**待复核 / 待核实（接入前核查）。


## 1.3 设计方向共识与方案比较

**适用场景：**思路已初步明确，但需要讨论路线、权衡和获得人类确认。

- **首选： [brainstorming（Superpowers）](https://github.com/obra/superpowers/tree/main/skills/brainstorming)**（Skill）。**用途：**结构化探索需求、备选设计和设计确认，适合 CoolFlow Brainstorm。 **局限：**原版会要求设计文档确认后调用 writing-plans，且可能指定外部文档路径。 **CoolFlow 适配：****A 级候选：轻量适配而不降优先级**；保留高质量提问与方案权衡，移除强制 writing-plans 交接，将输出记入 CoolFlow 当前 work/ 下可选 brainstorm.md，正式 Spec 留在 Step 6。 **等级：**A / L1。

- **备选： [office-hours（gstack）](https://github.com/garrytan/gstack/tree/main/office-hours)**（Skill）。**用途：**从产品视角挑战想法，帮助识别不清晰的价值定位。 **局限：**依赖 gstack 环境，不能假设单独复制 SKILL.md 就能运行。 **CoolFlow 适配：**借鉴问答方法即可；不接管 CoolFlow 下游流程。 **等级：**B / L2。


## 1.4 竞品、替代方案和市场研究

**适用场景：**需要理解用户已经如何解决问题，区分直接竞品、间接方案和替代方法。

- **首选： [competitor-analysis](https://github.com/phuryn/pm-skills/tree/main/pm-market-research/skills/competitor-analysis)**（Skill）。**用途：**提供竞品比较的分析框架，便于形成有来源的比较矩阵。 **局限：**AI 分析不能替代核实官方信息、真实定价和用户反馈。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / 待核实（接入前核查）。

- **备选： [research](https://github.com/mattpocock/skills/tree/main/skills/engineering/research)**（Skill）。**用途：**针对开放问题开展来源导向的研究并提炼判断。 **局限：**比竞品专用 Skill 更通用，需要指定比较维度。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / 待核实（接入前核查）。


## 1.5 用户访谈问题设计

**适用场景：**需要向真实或潜在用户核实需求，不想把假设当事实。

- **首选： [interview-script](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/interview-script)**（Skill）。**用途：**设计以行为和过去经历为主的访谈提纲。 **局限：**访谈提纲不等于真实用户证据；避免引导式问题。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**B / L0。

- **备选： [interview-me](https://github.com/addyosmani/agent-skills/tree/main/skills/interview-me)**（Skill）。**用途：**让 Agent 向开发者系统询问未定义的需求。 **局限：**访谈对象是开发者而非市场用户时更合适。 **CoolFlow 适配：**直接使用；尊重项目现有文档规范 **等级：**待复核 / 待核实（接入前核查）。

**选择建议：**外部用户用 interview-script；澄清开发者需求用 interview-me。
