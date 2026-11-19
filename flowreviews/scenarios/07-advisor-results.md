# S07 — Project Advisor validation record

This is a point-in-time record for [the scenario](07-advisor.md), not a claim of general reliability.

## Setup

- Date: 2026-11-17. Four fresh Agent contexts followed Skill instructions directly: one old-Skill baseline and three revised-Skill runs. Each received the same request, “这个项目接下来最值得做什么？”, plus the relevant fixture path. The baseline was the unmodified working tree at commit `208b2ae90807d809060f613c15d840facecc68ea`.
- Each executor was explicitly told not to modify files, run tests, use the network, or use other Skills or subagents. Thus unchanged fixtures show what happened under that restriction; they do not independently prove that an unrestricted host enforces the Skill's read-only default.
- The baseline read the old `coolflow-advisor/SKILL.md` and `coolflow-progress/SKILL.md` before this change. The three candidate runs read the working-tree Advisor entry directly, SHA-256 `14c4408c031c74688052b9443b40c98bbaef976f0ae7a7c25906f324b86f10cf`. None of the candidate runs loaded the curated recommendation library; its links and index were adjusted afterward.
- After the runs, the entry was tightened to distinguish missing release evidence from proof of non-release, avoid unsupported cost or uniqueness claims, and require all five entries whenever it gives a Step 1–5 overview. The final entry's SHA-256 is `6d292745fa7a6d293f7f8c194731bdf38bb3e79a882ac9a13acaef8b119e3b84`. These changes received static checks, not a behavioral rerun.
- The fixtures are synthetic files in an isolated temporary directory, without Git repositories. The scenario describes their decision-relevant contents. No real projects or production data were used.
- A complete file list and SHA-256 hashes were captured before all runs and after all runs. The two lists compared equal; 16 file hashes are retained below. The check covers files and names, not empty directories or unrecorded tool actions.

## Observed outputs

The excerpts below are the executors' actual words; descriptions of their other output are summaries, not complete transcripts.

### Ordinary project — old-Skill baseline

The executor chose the old Progress Skill. Its answer began:

> 结论：从现有记录看，先完成 Step 3 的外部验证——观察两位独立 facilitator 各自完成一次周会 recap——再考虑路线图里的导出格式选择器。依据是文档自身的记录：validation 的下一步就是这两场观察；product 的唯一未决问题是独立 facilitator 是否觉得该工作流有用；roadmap 正文明确当前目标是先验证真实 facilitator 能否完成有用的 recap，并注明导出选择器只是提议的增强、不是已确认需求。因此它不应排在验证之前。

It also listed all five steps, labeled missing records, distinguished the prototype description from validation evidence, and stated that other workspaces and sessions were not visible. The old Skills already produced a reasonable project-specific suggestion in this sample; this comparison does not establish improved recommendation quality.

### Ordinary project — revised Advisor

The executor recommended the same broad action:

> 结论：接下来最值得做的是尽快完成两位独立引导者的观察验证，暂缓增加导出格式选择器。

It cited the README, product, roadmap, pilot validation and prototype note; distinguished proposed work from observed results; and stated that it could not inspect actual source, prototype behavior or Git history. Its explanation also asserted:

> 两位参与者已经同意，边际成本最低。

The fixture does not compare the costs of available actions, so “边际成本最低” is an unsupported comparative claim. The run is useful evidence for the main recommendation but does not establish reliable cost comparisons.

### Concurrent objectives — revised Advisor

The executor's recommendation was:

> 建议：先完成 CSV 导出缺陷的根因定位、修复和可重复复验，确认可靠后再邀请 pilot。

It cited the pilot goal and export defect, distinguished the separate visual-design exploration, noted the absence of code and current verification, and did not assign a single global stage. It described the fix as consistent with the recorded roadmap, while labeling its proposed regression samples as its own addition. It also said “修好并验证导出，是当前唯一能推进已承诺目标的动作”; the fixture supports the export as a blocker but does not establish that it is literally the only possible useful action.

### Conflicting records in a non-CoolFlow project — revised Advisor

The executor recommended:

> 先核实 "v1.1 是否已发布、Markdown 导出是否真的可用"，把状态基线定下来；这是当前最值得做的一步。之后再决定继续完善导出还是做纯文本导入。

It described the conflicting README and work note, stated there was no evidence establishing which was current, and did not require CoolFlow adoption. Its suggested verification included:

> 若已有产物，实际做一次 Markdown 导出……；若没有产物，按"未发布"处理。

This conditional needs care: absence of an artifact in an incomplete search does not itself prove no release. The executor did not claim a current release status, but the wording does not establish the completeness of a future search.

## Static checks

- The candidate entry's YAML frontmatter parsed, its `name` matched `coolflow-advisor`, and its description was 293 characters.
- `git diff --check` found no whitespace errors in tracked changes. The new scenario and record were separately checked for trailing whitespace.
- A copy containing only the Advisor entry and its Markdown reference files initially had 13 relative links outside the installed folder. After replacing those links with upstream URLs, a static scan found no unresolved relative file links in the standalone copy. The remote URLs and automatic Skill installation were not tested; project-local conventions remain authoritative.
- The old `coolflow-progress` source entry was removed; historical scenario references describe prior executions and were preserved. Existing global installations were not changed during these original runs; the obsolete global Advisor was later removed at the user's request.

## Not verified at the initial review

- Automatic natural-language Skill discovery, an installed version in a new host session, and cross-host behavior.
- The unrestricted read-only default, explicit recording, a standalone method/tool question, and a requested complete Step 1–5 overview.
- A real Git repository, dirty working tree, code-level or test-evidence inspection, remote systems, and concurrent work in a different workspace.
- Repeatability across models and runs, the relative cost of suggestions, improvement over the baseline, or a new recommendation that is absent from all recorded next actions. Each fixture was run once per version shown.
- Behavior after any later edit to the Skill entry; compare the SHA-256 above with the final entry before relying on these observations.

## Fixture hashes before and after

The path prefix is the temporary fixture root. The lists were identical before and after all runs.

```text
b501f35c627e3f49b3178863726257831933d1a788eb359886b7431b6852655e  concurrent/AGENTS.md
691b39c080551c3b5c03bca446e61ca673db5f2d2f07d5bb86eaa890aee7ac08  concurrent/README.md
d94aad0977fffe70feaab730e4bc8be911f15cb1bba399bb808ec00cfccfd9e5  concurrent/docs/documentation.md
680403d114c381bb1fd4350fc9c909fc5e0e2aed7a41ebf98a6626b9018d80e3  concurrent/docs/roadmap.md
b5e7a24f741da3b0fc446def0cc061d04cabd76fa4d5ff10c4bd4ef947e9d89f  concurrent/docs/work/export/spec.md
fa9f55eb73fd55d00f70b98ff10186564c9621dcb9c837c4fa6c56076bd9e93e  concurrent/docs/work/layout/brainstorm.md
50899806824afb3fc7bff973bf7f2574cb13b9cd34cf35672e3c2f5dfd4dd7c6  ordinary/AGENTS.md
69f1792e8c876de600837fcad910c653ad419a684437923481c2f61e79d44d03  ordinary/README.md
e8ef1fe096a511f95d2d79fd7f311ffb28bc3f838fffe8b1b619b46d78dda30d  ordinary/docs/documentation.md
64bafbd2aa4979b4b6fd496f5dde0f0d3ff162ab56e724e8839a0e37a534f8a2  ordinary/docs/product.md
6dc5502a6b4a962f2d0da9f751307bf6bc146149afe2f84c6b1b348f9c883b7d  ordinary/docs/roadmap.md
9a6696df44a27773666e90f0056b347313a849be58d1bea7fba4f6f7f42b06fa  ordinary/docs/work/pilot/prototypes/README.md
22a8c7f2430d9d3d3f524cf0d384ab1e6e6b4b26a60c8c0cb6c254ce9e723625  ordinary/docs/work/pilot/validation.md
4d3ca6ac13c79691561e4002ba3191674ec74aded0642730d7c6813169f9ffaa  uncertain/NOTES.md
c4838d10b3420528033a3326a6062c8772b911e5577d60b84580a33b30594c58  uncertain/PLAN.md
bad18cf384b1fea9f311352bf7cb1c34142eea8f9b7473ab76125b9709f9ca20  uncertain/README.md
```

## Independent review

The first independent review was stopped by the author after a prolonged wait; it returned no findings, and there was no evidence that it had stalled. A second independent Agent reviewed the Skill, this scenario and record, and the applicable progress-metadata rules. It did not run new behavior tests or inspect the README and recommendation index in detail.

| Criterion | Reviewer result | Scope and limitation |
| --- | --- | --- |
| 1. Ordinary recommendation | PASS for the tested entry | Grounded in recorded goals; the cost comparison quoted above lacked evidence. |
| 2. Concurrent objectives | PASS for the tested entry | Considered the pilot blocker and separate UI work; its “only action” assertion was too strong. |
| 3. Missing/conflicting records | PASS for the tested entry | Preserved the present conflict and did not require CoolFlow; the proposed future conclusion from a missing artifact was ambiguous. |
| 4. Fixture preservation | PASS for the constrained runs | The 16 file hashes matched; executors had been explicitly instructed not to write, and empty directories were not covered. |
| 5. Standalone method/tool advice | NOT VERIFIED | No such request or curated-library use was run. |
| 6. Complete Step 1–5 overview | NOT VERIFIED | Only the old baseline reported the five steps; the revised entry was not exercised on that request. |
| 7. Entry, index and README consistency | NOT VERIFIED by reviewer | The reviewer did not inspect the bilingual README, index semantics or an actual installed copy. |
| 8. Local conventions and default boundaries | NOT VERIFIED | No local-rule conflict or unrestricted default-read-only scenario was exercised. |

The reviewer identified the apparent tension between advice-only behavior and the Standard's result-recording rule. The author checked that the Standard requires recording **within the authorized scope** and expressly preserves discussion-only requests; this Skill's user-agreed default is advice-only, and it records when explicitly authorized. The reviewer also noted that the deleted Progress entry made the baseline instructions hard to repeat. The scenario now names the baseline commit and explains how to read its historical files; that clarification was not independently re-reviewed or rerun.

## User-requested follow-up cases

The following runs were performed after the review above; its NOT VERIFIED entries describe what was known at the time. Both executors directly read the final Advisor entry with SHA-256 `6d292745fa7a6d293f7f8c194731bdf38bb3e79a882ac9a13acaef8b119e3b84`. They were instructed not to write files, use the network or invoke other Skills, so these cases do not prove automatic discovery or an unrestricted read-only default.

### Standalone method and Skill — PARTIAL

Request: “我已经讨论了功能需求和架构设计，项目没有 Issue Tracker，使用本地 Markdown 保存。请推荐一种把这些讨论整理成功能 Spec 的方法，以及一个适合的具体 Skill。”

The executor read the fixture's README, the Advisor entry, `references/recommendations.md` and `references/06-design-spec.md`. It did not assess a global project stage. It recommended using the current Agent for a local unified Spec, and explained that the `to-spec` Skill would need adaptation because its original workflow expects an issue tracker. It disclosed that the upstream entries had not been run locally and did not install or execute a tool. Its complete response also stated: “备选 `spec`（garrytan/gstack，B / L2，核查通过）：也偏向 issue 流程，且依赖 gstack 共享 preamble 和相关脚本；当前项目没有证据表明已具备 gstack 环境，因此不作为默认。” This dependency detail was omitted from the first version of this record, so the independent reviewer could not verify it from that version.

The answer named `to-spec` and `spec` but gave **no direct upstream links**, although the Advisor entry asks for links where possible and the reference it read contains them. The useful advice is therefore not a complete pass for this response requirement.

### Complete Step 1–5 overview — PASS for one constrained run

Request: “请给我这个项目完整的 CoolFlow Step 1–5 进度概览，说明每一步目前记录了什么。”

The executor listed all five steps. It reported `domain.md` as `not_started` because that status was explicitly recorded; listed the Step 3 brainstorm as `in_progress` and the validation record as `paused` without combining them into a step-level status; and said the Step 5 UI note had no card and an unknown status. It identified the paper prototype as an artifact, and distinguished the roadmap card's `complete` from human acceptance and release. The executor read the project-local documentation rules and reported its limited visibility.

The 11 fixture-file paths and SHA-256 hashes were identical before and after both follow-up runs. Both scans used `--hidden --no-ignore` and found no additional hidden files. This is evidence of preservation under the explicit no-write test restriction, not proof of the unrestricted default. Empty directories and unrecorded tool actions were not covered.

### Natural-language discovery — PASS for one restricted host run

The first isolated attempt used a fixture containing the final Advisor. Claude Code's initialization event listed `coolflow-advisor`, but the model request failed with `API Error: Unable to connect to API (EPERM)`; there was no model tool call and that attempt cannot establish automatic discovery.

After the user authorized removal of the obsolete global Advisor, a second attempt ran Claude Code `2.1.326` with model `auto/claude-opus-5-5` in an isolated project. The project-local Advisor entry had SHA-256 `6d292745fa7a6d293f7f8c194731bdf38bb3e79a882ac9a13acaef8b119e3b84`. The natural-language user prompt did not name a Skill: “这个项目接下来最值得做什么？目前有内部原型，尚未开展外部用户验证，计划加入导出格式。请说明依据。” The prompt is retained from the command invocation; this stream did not replay the initial user message, so the prompt itself is not independently present in the captured trace.

The host's initialization event listed `coolflow-advisor`; an `assistant` event contained a `Skill` tool call with `skill: coolflow-advisor`; its tool result had no error; and a subsequent user event exposed the Skill base directory inside the isolated project. The complete loaded Skill body exactly matched the fixture's entry body after excluding YAML frontmatter. The final host result reported success, and the command exited 0. This provides direct evidence of one automatic invocation and of the version actually loaded.

The retry ran outside the OS sandbox after the connection failure, with `--setting-sources project`, `--strict-mcp-config`, no Chrome, no session persistence, noninteractive permission handling, and **only the `Skill` tool enabled**. Its prompt provided a brief project summary, so it did not test reading project files or the behavior of a normal full-tool session. The existing global `coolflow-progress` was excluded by the project-only settings. One successful run does not establish reliable triggering across prompts, models or hosts, nor does it test an installed global Advisor.

## Remaining limits

- The standalone method/Skill answer omitted direct source links; no Skill instruction was modified in response to this test-only request.
- The current entry's additional guards on unsupported cost and release claims have not been exercised with targeted behavioral cases. A single Step 1–5 overview and a single automatic invocation cannot demonstrate repeatability.
- The unrestricted advice-only default, explicit result recording, automatic discovery in a normal full-tool session, an installed global Advisor, and the remote references' live availability were not tested.
- The previous independent review predates these follow-up runs; its NOT VERIFIED judgments above are historical, not a review of the new evidence.

## Independent follow-up review

The independent reviewer inspected the follow-up scenario and record, the current Skill and documentation standard, the two fixture hash lists and the automatic-discovery trace. It reported:

- **Standalone method/Skill — PARTIAL:** The local, tracker-free advice was relevant, but the answer omitted available upstream links. The first version of this record did not preserve the answer's explicit `spec` dependency caveat; the quotation above was added afterward from the executor's actual response and was not independently re-reviewed.
- **Step 1–5 overview — PASS for one constrained run:** The five-step output and document-level distinctions matched the fixture. Stale cards and a step with no records were not exercised by this follow-up case.
- **Natural-language discovery — PASS for one restricted host run:** The trace showed the Skill call, successful tool result, fixture base directory, matching loaded body and successful host result. The initial user prompt is recorded from the command rather than replayed in the trace; the restricted tool set and incomplete inventory of competing Skills limit generalization.

The reviewer also requested clarification of the hidden-file check. The two scans did include hidden files, but none were found; the preservation paragraph above now states that explicitly. These record-only clarifications were not a new behavioral test.

## Later scope clarification

The project progress overview is not limited to Step 1–5. The Advisor entry now directs a general status report to use relevant design, implementation, acceptance and release evidence, while progress cards retain their existing Step 1–5 scope. A specifically requested Step 1–5 overview retains its five-step format.

This clarification was made after the behavioral runs above. It has not been behavior-tested; the new whole-project overview case in the scenario remains unexecuted.

## Follow-up fixture hashes

These 11 SHA-256 hashes were identical before and after the method and overview runs. Paths are relative to the temporary fixture root. The specific request asked for a Step 1–5 overview; it does not establish behavior for a general whole-project overview that includes design, implementation, acceptance and release.

```text
fa49d7723310ad5b497e53b571fde9e88d29cd5040b780b19405ec64137ab1eb  method/README.md
d10c7832f89d5eae60af308cf17d4366f9b545e9c091ecf3839d897de343e1e3  overview/AGENTS.md
e5120e3400a4d85d961bf20400eaefb24d50e121c0746f82f125a45279b74322  overview/README.md
aa5667120963eb0bb1f07eca8cfc562293a3196c1dceebbcbaeee51bcfc9483e  overview/docs/documentation.md
e22f4a806eff9523802962c58432ed7d7e8641a3eeb0d6b877ffb2672dcd546e  overview/docs/domain.md
826b69644d1e5f3e7d29e742df35a0ba4751e673b994ed9f58e64278b5b61812  overview/docs/product.md
191003a4952f46c573a8169d46b8dfe43eb929d4b6ef123047ea93f1a95e408b  overview/docs/roadmap.md
5a5b66eb3ace5b3e184ff1165308e8b8d58c5a982e413ff363ecb8d456c432c9  overview/docs/work/board/brainstorm.md
d328dfd7b6927451efc5337114bf1961dd5b7ba3f81c0f8b71929d4ce2e84bd3  overview/docs/work/board/prototypes/README.md
0d5140f23a8edf388e7603014f0682bfa3930d938b62bbcc64ebd61e53fcb918  overview/docs/work/board/ui-prototype.md
ec921c0d75960695647e7547bbfcc469b78f470cd12d06f83fb47731c5be49f9  overview/docs/work/board/validation.md
```
