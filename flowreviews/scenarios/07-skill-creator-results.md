# S07 — Skill Creator validation record

This is an internal, point-in-time review record, not proof of universal compatibility. See [the scenario](07-skill-creator.md) and its linked reusable prompts for the expected behavior.

## Setup

- Date: 2026-11-02. CoolFlow base commit: `182399187b09bd11d3eefa4996c9c39cd28207be`; the new Skill was uncommitted.
- Initial `SKILL.md` SHA-256: `02e4d55c5e8c03ab64715ad1f422b282505d9a9654db73b37b9abdd8ab75b114`. First revision: `08e14fa6b7ae3fc176a5a475a0437a4f3c4214f97655a316852bc32b45f3527c`. Second revision: `e612b7c51aad578990cace901615c719061c6d4ecfc87d71340c1bbae7b08a65`. The entry and `references/validation.md` were then revised to add a default evaluation budget and a user-approval gate before larger testing; those latest changes have not yet been behavior-tested.
- Host: OpenCode on macOS, fresh general-Agent sessions. Each initial prompt ran once without the creator and once with the initial Skill read directly. The captured final responses and independent grading were saved in a local temporary workspace, not committed. Model timing, token counts and tool-call traces were not retained.
- Direct reading tests instruction following, not host automatic discovery. The runs used the same user prompts, but the working tree changed as the Skill was added. One with-Skill executor reported inadvertently listing some evaluation filenames; it said it did not open them, but no trace exists to verify that claim. These limitations make the comparison exploratory.

## Initial response-level comparisons

An independent grader assessed the saved answers against temporary criterion files. Those scoring files are no longer kept; the reusable expected outcomes now live in each case's `case.yaml`. These are single observations, not statistical estimates:

| Scenario | Without Skill | With initial Skill | Evidence and limits |
| --- | ---: | ---: | --- |
| External overlap | 3/3 | 3/3 | Both decided not to copy unverified upstream text or claim it was tested. The baseline already met the stated checks. |
| Offline Standard | 3/3 | 3/3 | Both declined to invent missing rules or claim latest-version compatibility. The baseline already met the stated checks. |
| From scratch | 3/4 | 4/4 | Both supplied a draft and a test plan. The baseline draft said “不运行命令、测试或查询”; the with-Skill draft allowed “用户允许且环境规则许可时” read-only checks. The fourth criterion was **added after seeing the baseline** and is exploratory, not preregistered evidence. |
| Adapt upstream | 2/3 | 3/3 | The baseline acknowledged untested behavior but did not propose a concrete Skill-validation plan. The with-Skill response proposed ordinary, insufficient-information and non-trigger scenarios before promotion. |

The grader evaluated response text, not actual tool behavior or whether the candidate Skills ran. The initial evidence cannot establish automatic triggering, real file-safety behavior, actual promotion, or cross-host independence. The generated temporary review page includes these limitations and the full captured answers.

## Initial independent review and revision

An independent reviewer inspected the source files and recorded S07 criteria 1, 2, 5 and 7 as static passes; criterion 3 as a static failure; and criteria 4, 6 and 8 as not verified with the evidence then available. The actionable failure was an ambiguity between “test without rewriting” and “stop at advice.” The reviewer also requested explicit existing-target collision handling and noted the absence of trace, automatic-discovery and repository-license evidence.

The first revision distinguishes authorized test execution from plan-only requests, adds target-collision and symlink checks, and distinguishes a self-contained design from verified independent execution. In an isolated-copy draft exercise, the response nevertheless included “无需 CoolFlow 源码或网络即可使用” inside the candidate while elsewhere admitting offline use was untested. The second revision explicitly requires the candidate itself, as well as the report, to distinguish design intent from tested runtime behavior.

Static checks parsed the Skill metadata and four test cases, verified local Markdown links and checked whitespace. `git diff --check` was also clean, but by itself does not include untracked files. The independent reviewer fetched the pinned upstream license and confirmed that the bundled MIT notice matches it; this does **not** establish a license for the CoolFlow repository or the new Skill as a whole.

## Revised behavior and final review

- Two original scenarios were re-run with the first revision and independently graded from their saved response text: creation 4/4, adaptation 3/3. The original baselines were **not rerun**, and the creation case's fourth criterion remains post hoc. These results do not automatically cover later revisions or tool behavior.
- With the final entry and the preceding version of `validation.md`, an offline-copy draft said “设计上不要求联网 … 实际离线和宿主兼容性尚待验证”; a separate missing-reference response reported an incomplete installation and stopped. Earlier offline-copy runs loaded a general authoring Skill due to host instructions, and no complete trace was retained, so strict isolation and runtime independence remain **NOT VERIFIED**.
- In a disposable sandbox after the final validation-reference clarification, the test-only Agent reported running the authorized Ruby checker. The resulting `results/report.txt` contained `PASS name=coolflow-sample sha256=6e96d2ceaa1d0dcbb76448ee403e69020839d1ad5080a18fd501518a5b425333`; an independent filesystem check found the sample Skill and its local override unchanged. The override's before/after SHA-256 was `f5dec47937353ac52fd8d0837e404715cae1cc44f32cebd3f3a4323808810eca`. This artifact and final state do not prove every intermediate action without a tool trace.
- With the final entry and the preceding validation reference, the collision exercise reported the existing target and asked whether to update or rename. Independent hashes of the sample Skill and override matched their original values, and the target contained no additional files. Symlink behavior and actions outside the observed target remain **NOT VERIFIED**.
- The plan-only exercise was repeated after the validation-reference clarification. Its response provided a plan; an independent filesystem check found the sample and override hashes unchanged and no result artifact. Without a retained trace, absence of test execution remains **NOT VERIFIED**.

The independent reviewer confirmed that the earlier S07 criterion 3 **static** failure was resolved, including the distinction between authorized sandbox output and protected files. The earlier static review found criteria 1, 2, 5 and 7 consistent with the source files. Full behavioral verification for criteria 3, 6 and 8 remains **NOT VERIFIED** without adequate traces; criterion 4 remains **NOT VERIFIED** for complete upstream dependencies and CoolFlow's own distribution rights, even though the upstream MIT text was independently compared. Automatic discovery, strict offline isolation, symlink handling and cross-host behavior also remain **NOT VERIFIED** at acceptance.

The Skill was **human-accepted on 2026-11-02** for use as an optional CoolFlow Meta Skill. Acceptance means the user reviewed the design, the available evidence and the remaining limitations, and chose to adopt it. It does not mean the unverified items below have passed, nor does it authorize installing, publishing, distributing or releasing the Skill.

Remaining **NOT VERIFIED** at acceptance: automatic triggering and host discovery; strict offline isolation without another authoring Skill loaded; full tool-call traces for the safety exercises; symlink handling; cross-host compatibility; and the distribution terms for the CoolFlow repository and its Skill content. The bundled CoolFlow summary is a compact aid maintained with the Skill, not a separate normative source or complete Standard; installed copies update when the Skill is updated.

The latest evaluation-budget changes were checked statically but not behavior-tested; future use and feedback should be recorded here rather than inferred as passed.
