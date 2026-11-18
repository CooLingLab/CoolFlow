# S10 — Project context mode in YAML

Exercise a candidate project instruction that delegates context loading to `docs/coolflow.yml`. The experiment uses identical project instructions for both modes and changes only the YAML value. Each request runs in a fresh Agent context.

## Build the fixtures

Run this block from the CoolFlow checkout. It prints the two fixture paths. Use a fresh temporary directory for each repetition.

```sh
set -eu
fixture_root=$(mktemp -d "${TMPDIR%/}/coolflow-context.XXXXXX")
mkdir -p "$fixture_root/alpha/docs/methodology" "$fixture_root/alpha/docs/work/csv-export"
cat > "$fixture_root/alpha/AGENTS.md" <<'EOF'
# Project instructions

For project planning, changes in product direction, or requests to resume work, read `docs/coolflow.yml` first.

- `context_mode: auto`: for project planning or changes in direction, read `docs/methodology/flow.md` and `docs/methodology/loops.md`. For a resume request, look in `docs/work/` for the relevant ongoing objective and read its records. If multiple objectives fit, ask which one. If a single objective fits, use its recorded next step.
- `context_mode: manual`: for planning, use the scope and context the user provides. For an ambiguous resume request, ask the user which objective to continue before searching work records. Read explicitly requested references and records for objectives the user identifies.

For a concrete maintenance task, read the relevant project files and follow the requested scope in either mode.
EOF
printf 'context_mode: auto\n' > "$fixture_root/alpha/docs/coolflow.yml"
cp methodology/flow.md methodology/loops.md "$fixture_root/alpha/docs/methodology/"
cat > "$fixture_root/alpha/docs/work/csv-export/spec.md" <<'EOF'
# CSV export

The export patch exists. Its behavior has yet to pass the remaining regression check.

Next step: verify that a contact label of `North, Dock` round-trips as one CSV field. Human acceptance is pending.
EOF
cp -R "$fixture_root/alpha" "$fixture_root/bravo"
printf 'context_mode: manual\n' > "$fixture_root/bravo/docs/coolflow.yml"
diff -ru -x coolflow.yml "$fixture_root/alpha" "$fixture_root/bravo"
printf '%s\n' "$fixture_root/alpha" "$fixture_root/bravo"
```

## Run and judge

Give each executor the fixture path, one request from the table, and read-only access. Run each row once per mode with a fresh context. Keep the mode and expected behavior out of the executor prompt. For an instruction-following test, tell the executor to read the fixture's `AGENTS.md` first. For a host-discovery test, start the host in the fixture and rely on its documented project-instruction mechanism. Record which method you used.

| Request | `auto` | `manual` |
| --- | --- | --- |
| 我们接着上次的工作。先告诉我下一步是什么。 | Reads the YAML, discovers the CSV Spec and identifies the `North, Dock` regression check. Leaves acceptance pending. | Reads the YAML and asks which work to continue before looking for work records. |
| 我想规划一个帮助独立教师整理课堂笔记的新项目。先给我一个推进建议。 | Reads the YAML and both methodology files, then uses them to recommend a proportionate first step. | Reads the YAML and gives scoped advice or asks a planning question using the context provided. Leaves both methodology files unread. |

Record the exact request, the answer or its decision-relevant excerpt, and the observed file accesses for each run. Count actual tool-call paths or a host trace as direct access evidence. If only the executor's account is available, label it as self-reported and mark access requirements that depend on it NOT VERIFIED. Compare the complete fixture file lists and SHA-256 hashes before and after. Have an independent reviewer report PASS, FAIL or NOT VERIFIED by criterion from the available evidence.

See [the validation record](10-yaml-context-mode-results.md) for the sampled runs.

## Retest the initialization templates

Assemble the required files from the working-tree `templates/project/` according to the initialization contract, or initialize from the candidate source using the host's supported entry point. Record which path was used. Create isolated copies for `auto`, `manual`, absent YAML, and a present file with `context_mode: typo`. Add the CSV Spec from the recipe to each copy. Supply a small CSV formatter file for the maintenance check.

Start a fresh read-only host session in each fixture, without telling the Agent to read `AGENTS.md` or naming either mode. Check the tool trace and answer against these expectations:

| Case | Expected behavior |
| --- | --- |
| Unnamed resume in `auto` | Reads the YAML and discovers the one active CSV objective. Reports the pending regression check. |
| Unnamed resume in `manual` | Reads the YAML and asks which objective to continue before searching work records. |
| Unnamed resume with missing or invalid configuration | Uses `manual` behavior. Reports the issue for the present invalid configuration. |
| New project planning in `auto` and `manual` | `auto` reads `docs/development-flow.md`. `manual` uses the supplied context. Neither opens the unrelated CSV Spec. |
| Concrete maintenance in either mode | Reads the relevant code. Skips the YAML, Flow reference, and unrelated work records. |

Record any inherited instructions or configured hooks and whether the host reaches its first model turn. A startup or authentication failure leaves host discovery and behavior NOT VERIFIED. Verify file integrity for read-only runs.
