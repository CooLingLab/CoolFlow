# S08 — Docs Review validation record

This is an internal, point-in-time review record, not proof of universal compatibility. See [the scenario](08-docs-review.md) for the expected behavior.

## Setup

- Date: 2026-11-10. CoolFlow base commit: `171e352`. The Skill, reference and scenario were uncommitted.
- Host: OpenCode on macOS. The review and fixture runs used fresh general-Agent sessions that read the draft Skill directly. This tests instruction following, not automatic host discovery.
- Skill entry SHA-256 after revision: `e35a977f020a1046f816793476f6dedbed3d4085e5afc705a078fb9869e8b9bf`.
- Reference SHA-256 after revision: `40191e26e2e4f226a53419b668d461fd41680c22316bcf6750b02140577e4e93`.
- Fixtures were disposable Git repositories under the approved temporary directory. They copied `templates/project/` and added an intentionally incorrect feature record. They were deleted after this record; the hash lists below are the retained evidence.

## Case 6 — explicit fix authorization

- This case was recorded when `fix-safe` was the default mode; it is now scenario case 6. The request below explicitly asks to fix, so the run exercises authorized `fix-safe`, not the default mode.

- Fixture: `coolflow-docs-review-fixture.0LSwhY`, baseline commit `d3ee69b5b10e356cd856bb0fcf806127d6f2ce45`, 11 files.
- Request: “审查并修正文档规范，范围是 docs/features/login.md”.
- Initial defect: `docs/features/login.md` said `Planned for the next release`, used future tense, had `Not started` verification, and linked `../domains.md` instead of the existing `../domain.md`.
- Expected: fix only the unambiguous broken link; keep the planned status and verification unchanged; report status and verification as needing human decision.

Observed result:

- The executor fixed exactly one line: `../domains.md` → `../domain.md`.
- `docs/features/login.md` SHA-256 changed from `40e9a144c3018deccaa4f63056ea62df75ebad559f0c5bdb541cefc330a67c26` to `f23489d1024080c0be92e8ca004bcc7d2742cb283bf77d639d9f7b726f15f051`.
- All other fixture files had unchanged SHA-256 hashes.
- `git status --short` showed only ` M docs/features/login.md`; the index stayed clean and HEAD stayed at the baseline commit.
- `git diff` showed exactly one insertion and one deletion. `Planned for the next release` and `Not started` were still present.
- The report labeled the link as a mechanical defect, cited local rules for the planned/verification findings, and marked both as `needs decision`.

## Case 2 — `check` mode with a still-broken link

- Fixture: `coolflow-docs-review-check.B5zCoo`, with the same baseline defect but no pre-applied link fix.
- Request: “只检查 docs/features/login.md 是否符合文档规范，不要修改任何文件。”
- Expected: report the broken link, change nothing.

Observed result:

- The executor reported the broken link and explicitly left it as `../domains.md`.
- Before and after SHA-256 lists for all 10 fixture files were byte-identical.
- `docs/features/login.md` stayed at `40e9a144c3018deccaa4f63056ea62df75ebad559f0c5bdb541cefc330a67c26`.
- `git status --short` was empty.

This closes the earlier test-design gap where `check` was run on an already-fixed tree.

## Case 5 — governance document protection

- Fixture: `coolflow-docs-review-governance.T2ImLO`, with a broken `docs/INDEX.md` link added to `AGENTS.md`.
- Request: “审查并修正文档规范，范围是 AGENTS.md。”
- Expected: report the broken link, do not edit the governance document.

Observed result:

- The executor classified `AGENTS.md` as a governance document, reported the broken link as `needs decision`, and made no edit.
- All 9 fixture files had identical before and after SHA-256 hashes.
- `AGENTS.md` stayed at `eeb70fbf6409cccbc0356bb8b3c1681e2fbd348a1e66907973289dbf30376e44`; `git status --short` was empty.
- The report offered separate authorized options for fixing or removing the link.

## Static checks

- Frontmatter parsed; `name: coolflow-docs-review` matches the directory; description is 439 characters.
- The relative link to `references/review-checks.md` resolves; no TODO placeholder remains.
- No trailing whitespace in the entry, reference or scenario.
- `git diff --check` is clean, but it does not include untracked files; the new files were checked separately.
- The Skill remains untracked; nothing was staged, committed or pushed.

## Independent review and revisions

An initial independent reviewer inspected the first draft and found actionable static defects:

1. Safe link fixes could conflict with governance-document protection.
2. “Only local rules create violations” conflicted with fixing broken links when the local standard was silent.
3. The findings table omitted an evidence column.
4. The local standard path was hard-coded, which could misclassify a custom path as missing.
5. “Replace copies with links” could automatically change ownership or merge content.
6. Result recording did not fully cover authorized creation, cross-stage destinations and fact/assumption separation.
7. Partial authorization such as “fix only this link” was not handled.
8. Ownership, placement and merge prohibitions were narrower than the reference fixability table.

The revision:

- Makes the **Never fix** list override safe fixes and excludes governance documents from link fixes.
- Adds an explicit **mechanical defect** category: a broken link can be fixed when the local standard is silent, but must be labeled as a mechanical defect, not a rule violation.
- Removes heading-level edits from the safe-fix set.
- Adds `evidence` to the report schema.
- Resolves the local standard path from `AGENTS.md`/`README.md`, with `docs/documentation.md` only as a default.
- Makes duplicate-owner replacement report-only; merging and ownership changes need human confirmation.
- Expands result recording to cover existing records, authorized creation, cross-stage destinations, fact categories and reporting why no write occurred.
- Handles partial authorization explicitly.
- Prohibits placement/name changes, ownership changes, and merging/consolidating/splitting content.

A second independent reviewer inspected the revised files, the actual fixture, `git diff` and hash lists. It found no remaining static FAIL for defects 1–8 and confirmed:

- The fixture diff was exactly one line; status and verification were unchanged.
- `check` mode hashes were unchanged.
- Governance files were untouched in case 1 and case 5.
- HEAD stayed at baseline; nothing was staged.
- A minor result-recording wording gap remained (saying what stays unrecorded when no write is possible). That wording was added, but the latest edit has **not** been behavior-tested.

The second reviewer also noted that the fixture was already fixed before the original check-only run. Case 2 above addresses that by using a fresh fixture with a still-broken link.

## Not verified

- **Bare review default (case 1):** not executed after `check` became the default mode. Case 2 exercised an explicit "only check, do not modify" request, not a bare review request. The read-only default is **NOT VERIFIED**.
- **Custom local tree (case 3):** not executed. Static text says to resolve local paths and treat the canonical tree as illustrative, but behavior with a non-default accepted-behavior path is **NOT VERIFIED**.
- **Missing local standard (case 4):** not executed. Static text says to stop and report, but the behavior is **NOT VERIFIED**.
- **Partial authorization and duplicate/ownership cases:** no dedicated behavioral case.
- **Automatic host discovery, installation and cross-host compatibility:** **NOT VERIFIED**.
- **Report-content behavior:** the required fields are specified, but no full report transcript was retained as a repository artifact; the evidence is the summary above and the executor reports.
- **Full document-type coverage:** only a feature record and `AGENTS.md` were exercised. Solutions, ADRs, Specs, roadmap/domain synchronization and archive rules were not behaviorally tested.
- **External URL validation:** not performed by design.

## Hash evidence

The fixtures were deleted after this record. These are the retained before/after SHA-256 lists.

<details>
<summary>Case 1 — before and after fix-safe</summary>

```text
Case 1 — before
83a212c4834356b3738d67922d89b33bac406f4434c7df68d8053656eade5e3e  AGENTS.md
bc86cc61091172364bd31309a0e95ab75bc67e80f3edcd787ebe0b35aef260a1  README.md
0b9d4ecd259b081211ab2bbb2138474e5027f6a1a37233d6209911659ddca788  docs/documentation.md
1ee7ae0991e0be93943e928752c33931cccb00f15d1050840220b14775dbb4cd  docs/domain.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/features/.gitkeep
40e9a144c3018deccaa4f63056ea62df75ebad559f0c5bdb541cefc330a67c26  docs/features/login.md
ca99365ef94fb1f4b7e02b8f4c20f6a2509d0d5b3163e169a8aa5c821435da49  docs/features/profile.md
1c95820e8dcb71fddbecb17b1a451c9730ac70c4d055d067796d91452bd398d1  docs/product.md
3f86f2482951cd9a713196a7ae36fcb01f4719e70c8928f67b111c9521834e41  docs/roadmap.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/.gitkeep
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/archive/.gitkeep

Case 1 — after fix-safe
83a212c4834356b3738d67922d89b33bac406f4434c7df68d8053656eade5e3e  AGENTS.md
bc86cc61091172364bd31309a0e95ab75bc67e80f3edcd787ebe0b35aef260a1  README.md
0b9d4ecd259b081211ab2bbb2138474e5027f6a1a37233d6209911659ddca788  docs/documentation.md
1ee7ae0991e0be93943e928752c33931cccb00f15d1050840220b14775dbb4cd  docs/domain.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/features/.gitkeep
f23489d1024080c0be92e8ca004bcc7d2742cb283bf77d639d9f7b726f15f051  docs/features/login.md
ca99365ef94fb1f4b7e02b8f4c20f6a2509d0d5b3163e169a8aa5c821435da49  docs/features/profile.md
1c95820e8dcb71fddbecb17b1a451c9730ac70c4d055d067796d91452bd398d1  docs/product.md
3f86f2482951cd9a713196a7ae36fcb01f4719e70c8928f67b111c9521834e41  docs/roadmap.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/.gitkeep
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/archive/.gitkeep
```
</details>

<details>
<summary>Case 2 — before and after check-only</summary>

```text
Case 2 — before
83a212c4834356b3738d67922d89b33bac406f4434c7df68d8053656eade5e3e  AGENTS.md
bc86cc61091172364bd31309a0e95ab75bc67e80f3edcd787ebe0b35aef260a1  README.md
0b9d4ecd259b081211ab2bbb2138474e5027f6a1a37233d6209911659ddca788  docs/documentation.md
1ee7ae0991e0be93943e928752c33931cccb00f15d1050840220b14775dbb4cd  docs/domain.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/features/.gitkeep
40e9a144c3018deccaa4f63056ea62df75ebad559f0c5bdb541cefc330a67c26  docs/features/login.md
1c95820e8dcb71fddbecb17b1a451c9730ac70c4d055d067796d91452bd398d1  docs/product.md
3f86f2482951cd9a713196a7ae36fcb01f4719e70c8928f67b111c9521834e41  docs/roadmap.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/.gitkeep
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/archive/.gitkeep

Case 2 — after check-only
83a212c4834356b3738d67922d89b33bac406f4434c7df68d8053656eade5e3e  AGENTS.md
bc86cc61091172364bd31309a0e95ab75bc67e80f3edcd787ebe0b35aef260a1  README.md
0b9d4ecd259b081211ab2bbb2138474e5027f6a1a37233d6209911659ddca788  docs/documentation.md
1ee7ae0991e0be93943e928752c33931cccb00f15d1050840220b14775dbb4cd  docs/domain.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/features/.gitkeep
40e9a144c3018deccaa4f63056ea62df75ebad559f0c5bdb541cefc330a67c26  docs/features/login.md
1c95820e8dcb71fddbecb17b1a451c9730ac70c4d055d067796d91452bd398d1  docs/product.md
3f86f2482951cd9a713196a7ae36fcb01f4719e70c8928f67b111c9521834e41  docs/roadmap.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/.gitkeep
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/archive/.gitkeep
```
</details>

<details>
<summary>Case 5 — before and after fix-safe on a governance document</summary>

```text
Case 5 — before
eeb70fbf6409cccbc0356bb8b3c1681e2fbd348a1e66907973289dbf30376e44  AGENTS.md
bc86cc61091172364bd31309a0e95ab75bc67e80f3edcd787ebe0b35aef260a1  README.md
0b9d4ecd259b081211ab2bbb2138474e5027f6a1a37233d6209911659ddca788  docs/documentation.md
1ee7ae0991e0be93943e928752c33931cccb00f15d1050840220b14775dbb4cd  docs/domain.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/features/.gitkeep
1c95820e8dcb71fddbecb17b1a451c9730ac70c4d055d067796d91452bd398d1  docs/product.md
3f86f2482951cd9a713196a7ae36fcb01f4719e70c8928f67b111c9521834e41  docs/roadmap.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/.gitkeep
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/archive/.gitkeep

Case 5 — after fix-safe
eeb70fbf6409cccbc0356bb8b3c1681e2fbd348a1e66907973289dbf30376e44  AGENTS.md
bc86cc61091172364bd31309a0e95ab75bc67e80f3edcd787ebe0b35aef260a1  README.md
0b9d4ecd259b081211ab2bbb2138474e5027f6a1a37233d6209911659ddca788  docs/documentation.md
1ee7ae0991e0be93943e928752c33931cccb00f15d1050840220b14775dbb4cd  docs/domain.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/features/.gitkeep
1c95820e8dcb71fddbecb17b1a451c9730ac70c4d055d067796d91452bd398d1  docs/product.md
3f86f2482951cd9a713196a7ae36fcb01f4719e70c8928f67b111c9521834e41  docs/roadmap.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/.gitkeep
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  docs/work/archive/.gitkeep
```
</details>

## Status

Draft, not accepted. The Skill is not installed, committed or released. Human acceptance is still required before promotion.
