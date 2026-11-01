# Skill validation and promotion

Validation is evidence about actual behavior, not a claim that a well-written Markdown file must work. Choose depth appropriate to risk, scope and available tools.

## Before and after

1. Define a realistic ordinary task, observable result and relevant constraints. A small first evaluation may need only this scenario plus static checks; add boundary, refusal, non-trigger or source/license cases when the risk or the user's request warrants them.
2. Where practical, **before drafting**, run the task in a fresh context **without** the new Skill, or with the previous version before editing. Record the actual outcome and notable omissions. If the baseline already meets expectations, report that; do not fabricate a failure or a performance improvement. For a pure reference Skill, test retrieval instead of forcing a behavioral baseline.
3. Draft or change the Skill, then run the same authorized scenario and conditions with it available. Inspect the output and any permitted tool actions, not just the Agent's self-report. Record exact inputs, versions, environment, observations and limitations. In simulations, avoid production or user data and real releases; write only to authorized disposable fixtures or separate test-output areas, preserving the protected Skill.
4. Address material failures and re-run the affected case when useful. An optional wording micro-test with repeated fresh contexts can help when a specific instruction remains unreliable; a single passing run does not establish consistency. Before a further iteration, show the user the actual result, material failures and the proposed next change.

Use an independent context or Agent when available, authorized and proportionate. If only an author self-check or human walkthrough is possible, label it accordingly. A host without subagents can still draft and run available checks, but cannot claim an independent Agent review or controlled comparison that did not happen. A repository may require independent review of the Skill being developed; follow that rule for that repository, but do not turn it into repeated multi-Agent evaluation for every candidate elsewhere.

## Default budget and expansion

Start with **one ordinary scenario** plus static checks. Keep the total at one with-Skill run and, where practical, one baseline run before asking the user whether to expand. State proposed extra cases, repetitions, multiple independent reviewers or report tooling—and their expected cost—before starting them. Expansion is justified by a specific unresolved risk, not by the desire for a more impressive benchmark. If larger testing is declined or unavailable, label the remaining risk instead of implying that the minimal check covers everything.

For a discipline-oriented Skill, the Superpowers approach of multiple pressure scenarios and repetition can be appropriate. Treat it as an **optional deeper evaluation selected with the user**, not the baseline cost of every Skill.

An authorized **test-only** request can run checks and record their results without modifying the Skill under test; a **plan-only** request must not execute those checks. For filesystem behavior, use disposable fixtures, preserve user files, record the target tree and hashes before and after, and inspect available action traces. Test existing target collisions and local overrides before claiming they are protected; missing traces or untested symlink cases remain limitations.

## Checks and reporting

- **Static:** parse frontmatter, check name/directory compatibility, local references and required resources. Review source provenance, license conditions, copied text and dependencies. These checks do not prove runtime behavior.
- **Behavior:** exercise the task under realistic constraints; check both useful output and boundaries such as no duplicate adoption, no invented standard, no unwanted upstream handoff, and no unapproved changes.
- **Discovery:** where the host supports it, test realistic should-trigger and should-not-trigger requests. Merely reading the Skill directly does not prove automatic discovery.
- **Report:** distinguish pass, fail and not verified per criterion; cite actual output, command or reviewer evidence. State when sample size is too small to support a comparative claim. Give concrete next tests for anything unverified.

## Promotion

Keep a candidate clearly labeled as a draft until relevant tests and applicable source, license and dependency checks have been completed. A human then decides whether to accept it into the native Skill Pool. Only after explicit authorization update a catalog, copy or install the Skill, or publish it; acceptance alone does not authorize unrelated Git, release or application changes. Preserve necessary upstream notices and record the tested version and evidence without asserting universal compatibility.
