---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

我想把下面的外部工作方式变成独立的 CoolFlow 原生 Skill，叫 coolflow-idea-clarify。仅输出草稿，不要联网或改文件。当前只拿到一段上游摘录：先逐步访谈需求，再比较两个方案；随后强制调用 external:planning，并在 docs/plans/ 创建计划。来源仅知 https://example.com/idea-tool，版本和许可证未知，其余上游文件不可用。请给出可用的 SKILL.md 草稿、保留和移除的内容，以及来源和验证状态。
