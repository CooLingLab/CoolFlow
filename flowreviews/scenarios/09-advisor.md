# S09 — Project Advisor

Evaluate the optional `coolflow-advisor` Skill as a read-only, project-wide advisor. This internal CoolFlow scenario is not copied into target projects. Use disposable fixtures and a fresh Agent context per run. The ordinary case is run once with the previous Advisor and Progress Skills and once with the revised Advisor; the two additional cases run once each with the revised Advisor.

The historical baseline is repository commit `208b2ae90807d809060f613c15d840facecc68ea`. To repeat it after the old entry's removal, read `skills/coolflow-advisor/SKILL.md` and `skills/coolflow-progress/SKILL.md` from that commit with `git show <commit>:<path>`; use separate temporary copies if the host requires Skill files. Do not replace the current Skill. If the commit is unavailable, mark the baseline rerun NOT VERIFIED.

## Request

In a new session, ask: “这个项目接下来最值得做什么？” Supply the fixture root, make the relevant Skill instructions available, and leave the Agent to inspect the project and answer. Do not give the executor the expected answer. Directly reading `SKILL.md` exercises its instructions, not automatic Skill discovery.

## Fixtures and expected behavior

1. **Ordinary CoolFlow project:** A meeting-recap prototype has only internal walkthroughs. `product.md` records an unresolved question about independent facilitators; `roadmap.md` states the immediate goal is to learn whether facilitators can complete a useful recap, while its card proposes an export-format selector; a pilot validation record says two facilitators have agreed to participate but no sessions have occurred. Expect a project-specific recommendation grounded in the goal and evidence, with the recorded enhancement distinguished from the Agent's judgment. Do not claim the external sessions happened. A suggestion to run or prepare the user observation is reasonable but not the only possible answer if justified by the evidence.
2. **Concurrent objectives:** The product roadmap prioritizes a reliable CSV export for a pilot. An export work record reports a reproducible comma-handling defect and no recorded fix or re-verification; a separate UI work record explores two visual directions with no committed date. Expect the recommendation to weigh the pilot blocker against the redesign, without compressing both objectives into a single certain project stage or inventing acceptance.
3. **Missing and conflicting records:** A non-CoolFlow snippet tool has a README saying version 1.1 with Markdown export is released, a contemporaneous work note saying release is pending and export is unverified, and a plan prioritizing dependable export without deciding between two enhancements. No evidence settles the conflict. Expect the conflict and uncertainty to remain visible, with a useful conditional next action; no invented release state, progress card, initialization, or document requirement.

## Additional user-requested cases

4. **Standalone method/Skill advice:** Ask how to turn discussed requirements and architecture into a local Markdown Spec when no issue tracker is configured. Give the current Advisor entry directly to the executor. Expect a task-specific method and suitable Skill, with actual prerequisites and any necessary adaptation, without a project-wide stage assessment or implementation. This exercises instruction following, not automatic discovery.
5. **Complete Step 1–5 overview:** In a CoolFlow fixture, include a `not_started` domain document, multiple Step 3 records with different statuses, a multi-step record, a completed roadmap card, a cardless UI note and a prototype artifact. Ask for the complete Step 1–5 overview. Expect all five steps, document-level statuses, and clear distinctions among `not_started`, no record, missing cards, and acceptance or release. This exercises instruction following, not automatic discovery.
6. **Natural-language discovery:** In an isolated fresh host session where the current Advisor is available, ask “这个项目接下来最值得做什么？” without naming the Skill or instructing the Agent to load it. A reliable PASS requires actual host evidence of the current Advisor being invoked, not an executor's assertion or a sensible answer alone. Record the loaded Skill location, its entry hash, competing installed Skills, host/version, and any failure or inability to set up the isolated session.
7. **Whole-project overview:** In a CoolFlow fixture with an accepted feature and a separate objective with an in-progress implementation, ask for a general project progress overview without specifying Step 1–5. Include evidence of testing and human acceptance, and an explicit release status. Expect the overview to cover the relevant later work rather than stopping at Step 5, while preserving the distinction among implementation, acceptance and release. It need not print all eight steps. This case has not yet been run.

## Review criteria

An independent reviewer inspects the current Skill, applicable standard, changed files, fixture observations and available execution evidence. Report **PASS / FAIL / NOT VERIFIED**, with evidence, for each criterion:

1. The ordinary recommendation is grounded in project evidence, distinguishes recorded plans from advice, and does not claim unobserved validation.
2. Concurrent objectives are considered without inventing a unique global stage; the priority is justified against the recorded pilot goal.
3. Missing or conflicting records are not converted into an invented status, and a non-CoolFlow project is not forced to adopt CoolFlow.
4. Advice-only runs leave all fixture files unchanged; compare complete before/after file lists and hashes.
5. A standalone method/Skill question remains supported without requiring a project-wide assessment; only actually exercised behavior may be marked PASS.
6. A requested Step 1–5 overview preserves all five entries and the distinctions between missing, stale, document-level and accepted status; only actually exercised behavior may be marked PASS. A general project overview must not stop at Step 5 merely because progress cards end there.
7. The revised entry, recommendations index, bilingual README and old Progress entry are consistent with the agreed scope. The installed Skill does not require the removed entry.
8. Project-local instructions and document conventions take precedence; recommendations do not install tools, change project files, claim acceptance or release, or create a state tracker by default.

## Execution record

See [the validation record](09-advisor-results.md) for the actual outputs, Skill hash, fixture file checks, review evidence and untested limitations. Do not infer automatic host discovery or general reliability from direct instruction-following tests.
