---
name: spec-driven-codex-loop
description: Execute an approved controlling issue through bounded implementation, repository-native validation, publication, independent review, and a ready-for-review handoff.
---

# Spec-Driven Codex Loop

## Responsibility

Use this skill for non-trivial **PR-backed implementation** under an approved controlling issue. The issue is the complete task-specific contract; repository documents define durable project constraints; branches and PRs preserve implementation; tests and technical evidence preserve observed behavior.

The executor owns implementation, validation, commits, progression through technical review, and handoff. Delegate GitHub mutations to `codex-github-operations` and checkpoint/final review to `codex-independent-review`. The executor may not review its own work independently.

The executor's terminal delivery state is a PR that is **ready for review**, not merged. It must not merge the PR, enable auto-merge, or treat a technical review verdict as merge authorization.

This generic executor does not override Mathia's explicit specialized no-PR workflows. If the controlling issue names `mathia-compute-executor`, `mathia-formalization-executor`, or another skill with an explicit publication contract, that named skill is the procedural authority instead of this PR-backed loop.

## Context and authority

Load once:

1. `AGENTS.md`;
2. the controlling issue;
3. only the exact source, test, data, model, prompt, artifact, mathematical source, dependency, or external input needed by the active outcome;
4. only the workflow or utility skill that owns the current action.

Exploratory documents such as `docs/CONCEPTUAL_MATH_DIRECTION.md` and `docs/WORKING_SYNTHESIS.md` provide motivation and hypotheses; they are not implementation contracts unless the controlling issue explicitly adopts a bounded part of them.

Do not weaken the issue, reconstruct its intent from broad history, or choose between materially different implementations when the issue is silent. Return to design instead. Do not silently promote exploratory notes, hypotheses, brainstorming, or provisional chat conclusions into requirements.

On resume, verify branch, `HEAD`, worktree, the controlling issue's single authoritative state label, and new material issue or PR discussion since the last handoff. Reuse unchanged inspected context rather than replaying history.

## Skillforge-compatible local-runner entry

When the session is launched through `.github/workflows/codex-execute-ready.yml`, the launcher has already established repository isolation before Codex starts. Treat the supplied persistent issue worktree/branch as an execution lease: the working directory must be the issue worktree, the branch must be `codex/issue-N`, repository identity must be Mathia, and a retry may contain unfinished state from an earlier attempt that must be inspected and deliberately adopted.

The launcher uses the Skillforge runner protocol and therefore the host may expose `SKILLFORGE_ISSUE_WORKTREE`, `SKILLFORGE_ISSUE_BRANCH`, and related `SKILLFORGE_*` variables. When those variables are present, fail closed if cwd, branch, repository identity, or controlling issue does not match them.

Do **not** create another worktree, switch to the durable coordination clone, switch to `main`, invent a second implementation branch, or discard pre-existing issue work merely because the session was launched by automation. For this PR-backed executor, the persistent issue worktree is the correct workspace.

The GitHub Actions job exits shortly after launching the interactive Codex turn. Actions success means only that the turn started, not that the issue succeeded. Do not depend on an ephemeral Actions token after launch, and never recover or persist one from runner state or logs. Git/GitHub operations must use the persistent transports described by `codex-github-operations`.

This launcher context changes only workspace/control-plane mechanics. Scope, validation, review, PR, and merge rules remain the normal executor rules below.

## Entry gate and workflow state

Before editing, confirm:

- exactly one state label exists;
- it is `execution-ready` or `in-progress`;
- branch and worktree are safe;
- scope, invariants, failure semantics, acceptance, and required inputs are clear;
- no competing branch or PR creates ambiguous ownership.

Before the first implementation edit, use `codex-github-operations` to replace `execution-ready` with `in-progress`. Do not post a comment solely for this transition.

Use label replacements for execution-time returns:

- missing material design decision: `design-required`;
- evidence needed before design: `investigation-required`;
- genuinely unavailable external capability: `blocked`.

`completed` is a post-merge state for this PR-backed workflow. The executor must not set `completed` or close the controlling issue as part of implementation delivery. After an explicit user-facing review accepts and merges the ready PR, the merge workflow may set `completed` and close the issue after observing the merge.

By default, add comments only when a material reason, technical finding, contract amendment, exact checkpoint target/verdict, blocker capability, or final handoff must be preserved.

## Execution loop

### 1. Establish the bounded outcome

Confirm intended behavior, permitted subsystem, invariants, required validation/evidence, and next checkpoint. Do not combine unrelated work or invent project-wide roadmaps, phases, schemas, frameworks, ontologies, or process machinery as a side effect of one issue.

### 2. Implement the smallest coherent delta

Follow the issue and accepted repository invariants, preserve baseline behavior outside scope, add tests/evaluation coverage when required, use repository-native integration, avoid unrelated cleanup/formatting, and stop when evidence invalidates the design or acceptance strategy.

Commits should represent reviewable outcomes; mechanical substeps do not need separate commits.

### 3. Handle dependencies and external inputs deliberately

For external repositories, models, datasets, mathematical texts, generated corpora, or other inputs, preserve identities required by the issue, respect licensing and redistribution terms, publish exact external targets when another actor must inspect them, and never present unavailable or ambiguous dependency state as successful evidence.

### 4. Validate honestly

Prefer repository-native build, test, lint, type-check, evaluation, benchmark, corpus-audit, Lean, or other formal commands appropriate to the issue. Record material deviations, environment limits, and checks not run. Never claim an unrun check passed.

For mathematical or AI-generated outputs, keep distinct syntactic validity, AI-judge/heuristic quality, human review when required, formal verification where available, and downstream task performance. Do not report teacher similarity, prose quality, or a compiling formalization as mathematical truth.

### 5. Retain evidence proportionally

Keep enough evidence to support the claim being made. Large models, datasets, caches, binaries, traces, bulky logs, or transient experiment outputs belong outside Git unless the issue explicitly requires them.

### 6. Publish intentionally

Publish when remote preservation, collaboration, a checkpoint, or PR review requires it. Exact SHAs are useful for review targets, not routine prose. Update durable documents only when the durable knowledge they own changes; do not edit research/architecture documents merely to mirror workflow state.

## Comments and progress observability

By default, comment only when a checkpoint is ready, scope or acceptance materially changes, a blocker/design/investigation return needs its cause preserved, or final handoff is ready. Progress comments requested by an orchestrating workflow are operational observability only: they do not change the contract, trigger review, replace checkpoints, or become technical evidence.

## Review checkpoints

At a declared checkpoint:

1. publish the exact target;
2. provide scope, material risks, acceptance criteria, and relevant evidence;
3. invoke one fresh independent review;
4. continue only after `PASS` or non-blocking `PASS_WITH_NOTES`.

A checkpoint may serve as final technical review when it covers the complete final diff and all remaining acceptance criteria. Any later technical change invalidates that verdict. A final technical verdict never authorizes merge by itself.

Progression is bounded: `PASS`/non-blocking `PASS_WITH_NOTES` may continue; `FAIL` requires a bounded correction or return to design/investigation; `BLOCKED` means the required capability has no safe alternative. Do not mechanically implement every reviewer suggestion.

## Repeated-review circuit breaker

After two consecutive failures in substantially the same validation, attestation, parser, documentation-sync, or bookkeeping mechanism, stop compensating patches and return to design authority before a third cycle unless the defect is materially different. This never waives a continuing technical defect.

## Pull request discipline

Use one PR per controlling issue unless the issue explicitly decomposes delivery. Keep it draft while required implementation, validation, or independent technical review remains incomplete.

When the complete final diff has passed required validation and final-capable independent review, update the PR description with the final technical state, mark it **ready for review**, and stop execution.

The executor must never merge the PR, enable auto-merge, interpret technical success as merge authorization, close the issue, or set it to `completed` before a later explicit user-facing review accepts and merges the PR.

## Handoff

Include only what the next actor cannot derive cheaply: issue and bounded outcome; ready-for-review PR and exact reviewed target when useful; last accepted checkpoint; material evidence; unresolved non-blocking notes; and the immediate next action, which is user-facing review and merge decision.
