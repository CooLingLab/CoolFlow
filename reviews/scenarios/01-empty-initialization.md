# S01 — Empty project initialization

Prompt: “参考 CoolFlow，帮我初始化当前项目文件夹和开发文档。只初始化。”

Environment: temporary empty Git repository.

Expected:
1. All six core documents are generated (plus three Git placeholders), including the complete local `docs/documentation.md`.
2. `AGENTS.md` contains Flow, Loops and behavior boundaries, and refers to the local documentation standard.
3. `product.md`, `roadmap.md` and `domain.md` retain explicit undecided placeholders.
4. No `work/001-mvp/`, Spec, PRD, design, tasks, code, dependencies or CI is generated.
5. Git-relevant directories exist, all generated links resolve, and the local standard is usable without CoolFlow access.
6. A second identical invocation preserves contents.

Review with actual file tree and diff evidence; don't accept the executor's narrative alone.
