# S10 — YAML context mode validation record

See the [scenario and fixture recipe](10-yaml-context-mode.md).

## Setup

On 2026-11-18, disposable `alpha` and `bravo` fixture trees used `auto` and `manual`, respectively. A recursive diff found one difference in `docs/coolflow.yml`, where `context_mode` had a different value. Both had the same candidate `AGENTS.md`, methodology references copied from this checkout, and a synthetic CSV export Spec.

Fresh executor subagents were given the fixture root and explicitly asked to read its `AGENTS.md`. Each received one Chinese request from the scenario, without the expected answer or the mode. Executors were instructed to use read-only fixture access and reported their access in order. Key file accesses were checked against local tool records from the child contexts. The host was Claude Code 2.1.326. The parent repository's instruction context was present in the executors, so the experiment measures which fixture documents were loaded in each mode.

## Results

Paths are relative to the corresponding fixture root. The sampled answers followed the intended branches.

- Resume — 我们接着上次的工作。先告诉我下一步是什么。
- Planning — 我想规划一个帮助独立教师整理课堂笔记的新项目。先给我一个推进建议。

The planning runs also show that the candidate instructions permit extra discovery. The `auto` executor brought up an unrelated work item, and the `manual` executor listed unrelated paths without opening their contents.

| Request | Mode | Observed answer | File access evidence after `AGENTS.md` |
| --- | --- | --- | --- |
| Resume | `auto` | “下一步是完成剩余的那项回归检查：验证联系人标签 `North, Dock` 在 CSV 往返后仍是一个完整字段（不会被逗号拆成两个字段）。” Kept human acceptance pending. | Read YAML, listed `docs/work/` and `docs/work/csv-export/`, read its Spec, then listed the fixture tree. The harness reported six tool calls. |
| Resume | `manual` | Asked “请告诉我要继续的目标（`docs/work/` 下的目标目录名，或一句话描述）”. | Read YAML. The harness reported two tool calls. |
| Planning | `auto` | Recommended Idea → Brainstorm, then concept validation before MVP scope. Also surfaced the unrelated CSV task. | Read YAML and both methodology files. The executor reported reading the CSV Spec too, and the answer cited its fixture-specific facts. |
| Planning | `manual` | Proposed a scoped plan beginning with interviews with two or three teachers, then outlined an MVP and asked for product decisions. | Read YAML. Two Bash calls listed paths using `ls` and `find`; neither opened methodology or Spec bodies. |

## File integrity

The initial snapshot and a fresh snapshot taken after all four runs listed ten files with identical paths and SHA-256 hashes. Both manifests had SHA-256 `4157674f9568a5bf9a25a8cc1ca9992447958fb8ed413bcc93d080eeb82c06f2`. The fixture creation block also ran successfully on a second temporary directory.

## Assessment

- **PASS — Resume response in both sampled modes.** `auto` grounded its next step in the fixture Spec. `manual` asked for the objective after reading the YAML and before searching work records.
- **PASS — Methodology file selection in the sampled planning runs.** The `auto` tool record shows both methodology reads. The `manual` run used file listings and gave planning advice without reading the methodology files.
- **PASS — File integrity.** All ten fixture files retained their names and contents.
- **NOT VERIFIED — Automatic discovery and repeatability.** The executors were pointed to `AGENTS.md` explicitly. Each combination ran once.

The unrelated CSV work in the `auto` planning reply is a scope issue. If the candidate is adopted, make the planning instruction specific to methodology and task-relevant project records, then retest that the reply leaves unrelated objectives out.

## Independent review

The independent reviewer reproduced the fixtures and confirmed the one-value difference and the recorded answer differences. The reviewer received the fixture snapshots and executor summaries, and rated per-path assertions NOT VERIFIED on the evidence provided. The coordinator separately inspected targeted local tool records. The observations below summarize those records without including private session metadata.

| Run | Direct trace excerpts |
| --- | --- |
| Resume, `auto` | The tool result returned the CSV Spec body containing the `North, Dock` check. |
| Resume, `manual` | The trace shows `Read` calls for `AGENTS.md` and `docs/coolflow.yml` followed by the request for an objective, with no intervening work search. |
| Planning, `auto` | The trace shows `Read` calls for `docs/coolflow.yml`, `docs/methodology/flow.md`, and `docs/methodology/loops.md`. The extra CSV Spec read is reported by the executor and corroborated by the fixture-specific details in its answer. |
| Planning, `manual` | The Bash calls used `ls` and `find -print` to list paths. The run had two `Read` calls reported for the instruction and YAML. |

The reviewer identified two wording gaps for a follow-up run. Define a resume request as unspecified when the user has named no objective, even if the fixture happens to contain only one. State directly whether manual planning should open the methodology files. Use an isolated host for the next run to test how the methodology affects the answer, and score unrelated work reads separately from the intended methodology reads.

## Working-tree template retest

The test projects were assembled from the eight required files in `templates/project/` and three Git placeholders, then seeded with the CSV objective and a small formatter for the maintenance cases. The run used Codex CLI 0.169.0-alpha.11.1 from the fixture directories in read-only mode with ephemeral sessions and JSON tool traces. The prompts did not mention `AGENTS.md`, YAML or either mode. The host still made its installed Superpowers guidance available in some sessions despite `--ignore-user-config`.

An initial run with missing YAML opened the CSV Spec before asking for the objective. After the project instructions were revised to determine the mode before searching records, a fresh set of eight sessions produced these results.

| Case | Result | Evidence from the final run |
| --- | --- | --- |
| Resume in `auto` | PASS | Read the YAML and context rules before the CSV Spec. Reported the `North, Dock` regression check and pending human acceptance. |
| Resume in `manual` | PASS | Read the YAML and context rules, then asked for the objective without searching work records. |
| Resume with an invalid mode | PASS | Read `context_mode: typo`, reported it, and asked which objective to resume without searching work records. |
| Resume with missing YAML | PASS | Checked for the YAML, read the context rules, and asked which objective to resume without searching work records. |
| Planning in `auto` | PASS | Read the local Flow reference and Product Brief. Listed documentation paths and did not open the unrelated CSV Spec. |
| Planning in `manual` | PASS | Read the configuration and context rules and gave planning advice without opening the Flow reference or CSV Spec. |
| Concrete maintenance in `auto` | PASS | Read `src/csv.js` and explained the CSV delimiter issue without consulting the mode, Flow, or work records. |
| Concrete maintenance in `manual` | PASS | Read `src/csv.js` and explained the same issue without consulting the mode, Flow, or work records. |

Before and after SHA-256 manifests matched all 49 fixture files. Static checks verified the default YAML, matching English context sections in the standard and template, eight stages, three Loops, the eight initialization template paths and local navigation. An independent reviewer checked the rollout before the last wording revision. The follow-up clarified unnamed resume precedence, direct-task routing, and the docs-review check, then exercised the resulting instructions in the sessions above.

The initial Codex launch hit host sandbox restrictions. The completed runs used the approved host launch with the Codex command sandbox set to read-only. This covers a host that discovers `AGENTS.md`, with one final run per case. The installed initialization Skill fetches public `main`, so this retest used the local candidate templates. A published-source initialization run, other hosts, malformed and unreadable YAML, and ambiguous `auto` resume with multiple objectives remain unverified for this rollout.

## Verification boundaries of the earlier prototype

These runs exercise Agent instruction following after explicit entry into the fixture instructions. Automatic host discovery, repeatability across models and hosts, ambiguous `auto` work with several objectives, concrete maintenance, and missing or malformed configuration are outside the executed cases. The fixture supplies both methodology files locally for direct reads. Their outbound links and deployment to initialized projects have yet to be exercised. The YAML value and project instructions together produced the observed differences. A host that discovers project instructions on its own and repeat runs per mode are needed to assess reliability in regular sessions.
