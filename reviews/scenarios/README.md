# Development-only Scenario Review (NOT release content)

These cases validate **CoolFlow's usability and Skill output**, not an App's unit tests. Keep these files during early CoolFlow development, including on its development branch; **remove them from the final release tree**.

An independent Agent (different context from the implementer when practical) should inspect the scenario, applicable Standard, resulting files / diff, and any runnable evidence; it should output PASS, FAIL or NOT VERIFIED **per criterion with specific evidence**.

Suggested result format:
- Case ID and execution environment
- Expected vs actual changed files
- Per-criterion judgment plus file/diff evidence
- Critical failures and proposed corrections
- Explicitly state what could not be tested

Do not mark unexecuted cases as PASS. For a clean final-release tree, remove `reviews/scenarios/` before release; Git history may still contain old commits.
