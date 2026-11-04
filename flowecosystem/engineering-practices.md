# Engineering Practices for AI-Assisted Development

**Research snapshot: 2026-11-02**

This is a **non-normative reference**, not a checklist. It collects engineering practices that work well when Agents write, review or deploy code, and explains where each one fits CoolFlow. None of them is required by the methodology. Adopt only what the project's risk, scale and tooling justify.

Nothing here changes the normative requirements in `methodology/` or `standards/`. A practice is a mechanism, not a guarantee: a review rule that the environment cannot enforce is only an intention.

**How to read each entry:** the problem it addresses, when it is worth using, its main cost, and its relationship to CoolFlow.

## Parallel development and integration

### 1. One worktree per task

- **Problem:** parallel Agents sharing one working directory overwrite each other's files, lose stashes and produce diffs nobody can attribute.
- **Worth using when:** tasks are independent (isolated bugs, tests, docs, separate modules) or when comparing alternative implementations of the same problem.
- **Main cost:** separate ports, environment files and databases; merge conflicts can still occur; stale worktrees need cleanup.
- **Relationship to CoolFlow:** supports running several Implementation Loops in parallel while keeping each change reviewable against its own Spec. It is unnecessary for sequential work and does not replace review or integration testing.

### 2. Small batches and short-lived branches

- **Problem:** long-lived branches drift from the mainline, large changes hide defects, and review degrades into a rubber stamp.
- **Worth using when:** almost always. Smaller changes are easier to review, verify and revert, and they keep the mainline close to a releasable state.
- **Main cost:** the work must be sliced into independently verifiable pieces; incomplete behavior may need a feature flag or stacked changes.
- **Relationship to CoolFlow:** the practical form of **Ship Small** (Golden Rule 1). It shortens the distance between implementation and human acceptance.

### 3. Branch protection and required checks

- **Problem:** "review passed" and "tests passed" are social facts until the repository enforces them. An Agent or a hurried human can merge a red change.
- **Worth using when:** any shared mainline, and especially when Agents have write access.
- **Main cost:** configuration and maintenance; slow or flaky checks block everyone and must be fixed rather than bypassed.
- **Relationship to CoolFlow:** turns **Prove It Works** (Golden Rule 4) into a mechanical gate. It supports human acceptance; it does not replace it.

## Review and merge

### 4. Independent reviewer

- **Problem:** the author shares their own assumptions and blind spots. Self-review is weak, and an Agent reviewing its own work tends to defend its choices.
- **Worth using when:** material changes, novel or risky work, and most Agent-written code.
- **Main cost:** another session or Agent, extra tokens and latency; a reviewer without context may raise noise or miss intent.
- **Relationship to CoolFlow:** maps to the fresh-context **Design Spec Review** and **Code Review**. The reviewer should read the Spec, the diff and the relevant code, not the author's explanation of why the change is correct. Reviewing with a different model family is optional, not a guarantee of independence.

### 5. Read-only reviewer

- **Problem:** a reviewer that can edit files, reach the network or read secrets expands the blast radius. It may "fix" instead of report, fetch untrusted content, or expose credentials.
- **Worth using when:** review is automated, or an Agent reviews without close supervision.
- **Main cost:** the boundary must be enforced by the environment (separate checkout, container, filesystem and network policy, scoped credentials), not by prompt instructions.
- **Relationship to CoolFlow:** makes the Code Review role distinct from implementation. If the environment cannot enforce read-only access, state that limitation instead of claiming the practice.

### 6. Bounded review

- **Problem:** review can loop indefinitely. Agents can generate endless "improvements", and style nits crowd out defects that actually matter.
- **Worth using when:** every review loop, especially automated review.
- **Main cost:** a cap can miss a real issue, so unresolved blockers must be escalated with evidence rather than silently accepted. The severity threshold needs calibration per project.
- **Relationship to CoolFlow:** gives the Design Spec and Implementation Loops a stopping rule. Report only defects that would cause incorrect behavior, security or privacy exposure, data loss, or unmet acceptance criteria; when the cap is reached, hand the residual risk and the decision to the human. A small fixed cap (for example, three rounds) is a common practitioner convention, not a universal standard.

### 7. Separate merge and release authority

- **Problem:** the entity that writes code also approves and deploys it. A single over-eager or compromised Agent can reach production.
- **Worth using when:** Agents have repository write access, or a release changes production.
- **Main cost:** more roles and credentials to manage, and additional steps for small teams.
- **Relationship to CoolFlow:** aligns with Step 8, where human acceptance and release are distinct decisions. Authority may be delegated for execution, but accountability for accepting and releasing remains human.

## Build, release and verification

### 8. Agent stops at the pull request

- **Problem:** an Agent that merges and deploys directly bypasses review and verification, and failures become hard to attribute.
- **Worth using when:** autonomous coding Agents change a shared branch, or production deployment is automated.
- **Main cost:** requires a pipeline that can review, test, merge, deploy and report status back; without one, the pull request becomes a manual bottleneck.
- **Relationship to CoolFlow:** draws the boundary between Step 7 (implementation and its evidence) and the post-acceptance release step. CI/CD may execute the mechanical path according to project policy; it does not replace a human acceptance decision where CoolFlow requires one.

### 9. Disposable clean environment per task

- **Problem:** Agent-written code runs on a developer machine or a shared runner, polluting state and exposing credentials. "Works on my machine" becomes the only evidence.
- **Worth using when:** running automated tests or builds, executing generated code, or working on several tasks in parallel.
- **Main cost:** image and startup time, compute resources, and harder debugging inside an isolated environment.
- **Relationship to CoolFlow:** supports reproducible **Prove It Works** evidence. Build isolation is not the same as an execution sandbox (practice 14); a project may need one, the other, or both.

### 10. Committed lockfiles and locked CI installs

- **Problem:** version ranges in a manifest can resolve to different dependency versions on different machines or at different times. Local and CI results diverge, and an unreviewed transitive update can change behavior or introduce supply-chain risk.
- **Worth using when:** the project uses a package manager that produces a lockfile, especially for applications and deployed services. Generate and commit the lockfile, and make CI install in the ecosystem's frozen/locked mode so it fails rather than silently resolving a different dependency set. The exact command is tool-specific (for example `npm ci`, `pnpm install --frozen-lockfile`, `yarn install --immutable`, `uv sync --locked`, `cargo build --locked`); the principle matters more than the command. Library projects that deliberately publish a dependency range may omit the lockfile; state that choice and make CI test the supported range instead.
- **Main cost:** lockfile merge conflicts and review noise; platform-specific or optional dependencies may need separate handling; dependency updates become an explicit reviewed change.
- **Relationship to CoolFlow:** supports **Prove It Works** (Golden Rule 4) by making CI evidence reproducible and **Keep It Working** (Golden Rule 1) by limiting unreviewed dependency drift. It is a build/reproducibility practice, not a new stage or a CoolFlow-wide requirement.

### 11. Post-deployment verification

- **Problem:** "the deploy job succeeded" is not "the change is running". Caches, partial rollouts, the wrong artifact and environment drift all produce false success.
- **Worth using when:** any production release, especially an automated one.
- **Main cost:** requires a version or health endpoint and a safe smoke path; tests should use synthetic accounts, not real user data.
- **Relationship to CoolFlow:** closes the gap between "released" and "verified running". Record the evidence, and treat failures as new input; the human decides whether they warrant the Evolution Loop.

## Data and irreversible changes

### 12. Expand–contract migrations

- **Problem:** a destructive schema change breaks old code during a rolling deploy, and rollback may no longer be possible.
- **Worth using when:** changing live data with more than one application instance, or whenever a rollback must remain practical.
- **Main cost:** multiple releases, dual writes or backfills, and discipline in removing the old structure only after verification. It is overkill for disposable or local data.
- **Relationship to CoolFlow:** supports **Keep It Working** and **Keep a Way Back** (Golden Rules 1 and 3), and splits a risky change into steps that fit **Ship Small**.

## Permissions, security and knowledge

### 13. Least privilege and secret isolation

- **Problem:** long-lived production credentials in an Agent environment turn a mistake, a malicious dependency or prompt injection into a breach.
- **Worth using when:** an Agent has tool access, or any environment contains real credentials.
- **Main cost:** short-lived tokens, credential brokers or proxies, and per-task scopes add setup and new failure modes.
- **Relationship to CoolFlow:** a concrete form of **Keep a Way Back** (Golden Rule 3). It limits the impact of a failure; it does not replace a human decision before an irreversible action.

### 14. Sandboxed agent execution

- **Problem:** model-generated commands run with the developer's full privileges. One bad command can delete files, reach internal services, or install something unwanted.
- **Worth using when:** Agents run unattended, execute generated code, or have network access.
- **Main cost:** isolation technology (container, microVM or OS sandbox), egress policy and secret handling; debugging is less convenient.
- **Relationship to CoolFlow:** makes "the Agent may implement and verify routine work" safer. State the boundary explicitly; an unstated sandbox is not a control.

### 15. Decision ledger

- **Problem:** Agents re-ask settled questions, rejected ideas resurface, and the rationale behind a choice disappears with the session.
- **Worth using when:** working repeatedly with Agents, or making product decisions with lasting consequences.
- **Main cost:** the human must record decisions in their own words, with dates, and keep the ledger current without turning it into a second Spec.
- **Relationship to CoolFlow:** complements **ADRs** (why a consequential architecture decision was made) and **accepted feature docs** (what is true now). Record accepted decisions and explicit rejections, link them to the relevant work item, and keep speculative ideas out.

## Out of scope

Event intake and routing, webhook dispatch, queueing and deduplication, model selection, self-hosted CI runners and chat-based approval cards are **runtime and orchestration concerns**. They can be valuable, but CoolFlow deliberately does not prescribe them, and this document does not either. See the [Framework Comparison](framework-comparison.md) for how complete workflow suites handle these areas.

## Sources

Links were checked during a quick research pass on 2026-11-02. They are further reading, not endorsements or verified implementation guides.

- Practitioner account: 数字生命卡兹克, *"折腾了整整 1 年，毫无保留地分享一下我这套 Agent 自动化系统"* (2026). Source for the pull-request handoff, read-only reviewer, review-round cap, disposable environments, decision ledger and post-release verification described above.
- Git worktrees for parallel Agents: [Google Cloud Community](https://medium.com/google-cloud/run-multiple-coding-agents-safely-with-git-worktrees-c2d237dbd6b2), [vensas](https://vensas.de/en/blog/git-worktrees-ai-workflows), [Superset](https://superset.sh/parallel-coding-agents).
- Trunk-based development and small batches: [DORA](https://dora.dev/capabilities/trunk-based-development), [Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development).
- Branch protection and required checks: [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- Agents propose, CI/CD owns the release path: [Qovery](https://www.qovery.com/solutions/ai-cicd).
- Post-deployment smoke and canary checks: [QASkills](https://qaskills.sh/blog/smoke-testing-post-deploy-canary), [Unleash](https://www.getunleash.io/blog/rolling-deployment-vs-smoke-test).
- Expand–contract / Parallel Change: [Martin Fowler](https://martinfowler.com/bliki/ParallelChange.html).
- Ephemeral environments and sandboxing: [Qovery](https://www.qovery.com/blog/best-ephemeral-code-execution-environments-ai-agents), [LangChain](https://www.langchain.com/resources/best-agent-sandboxes), [SpecStory](https://specstory.com/learning/environments/ai-sandbox).
