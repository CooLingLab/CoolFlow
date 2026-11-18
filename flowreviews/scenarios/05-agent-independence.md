# S05 — No mandatory Skill or external runtime

Environment: temporary fresh repo with an AI Agent capable of reading CoolFlow Standard, but without installed CoolFlow Skills, EGM or a dashboard.

Expected:
1. Agent can initialize correctly from `standards/` and `templates/` alone.
2. The resulting `AGENTS.md` leads to the local documentation standard, YAML preference and offline Flow reference as appropriate for the task.
3. No workflow engine, dashboard, external EGM or task-file dependency is required.
4. The project can evolve its docs independently of CoolFlow upstream versions.

Record what source documents were read and inspect resulting project artifacts.
