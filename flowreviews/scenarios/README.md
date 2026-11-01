# CoolFlow internal scenario reviews

This directory contains internal validation scenarios for **CoolFlow itself**. They check whether CoolFlow's Standards, templates, Skills and initialization guidance produce the expected results. They are not unit or integration tests for applications built with CoolFlow.

Keep these files in the CoolFlow source repository, including its public `main` branch and published source releases. They are repository-maintenance materials, not application templates. **Never copy `flowreviews/` into a target application** when initializing or adopting CoolFlow.

An independent Agent (using a different context from the implementer when practical) should inspect the scenario, applicable Standard, resulting files / diff, and any runnable evidence. It should report PASS, FAIL or NOT VERIFIED **for each criterion, with specific evidence**.

Suggested result format:
- Case ID and execution environment
- Expected vs actual changed files
- Per-criterion judgment plus file/diff evidence
- Critical failures and proposed corrections
- Explicitly state what could not be tested

Do not mark unexecuted cases as PASS. These scenarios remain in the CoolFlow source repository; they are not copied into application repositories.
