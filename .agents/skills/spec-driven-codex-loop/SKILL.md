---
name: spec-driven-codex-loop
description: Execute an approved controlling issue through bounded implementation, repository-native validation, publication, independent review, and a ready-for-review handoff.
---

# Spec-Driven Codex Loop

## Responsibility

Use this skill for non-trivial implementation under an approved controlling issue. The issue is the complete task-specific contract; repository documents define broader context only to the extent they are explicitly authoritative.

The executor owns implementation, validation, commits, technical review progression, and handoff. Delegate GitHub mutations to `codex-github-operations` and independent checkpoint/final review to `codex-independent-review` when required.

The executor's terminal delivery state is a PR that is **ready for review**, not merged. It must not merge the PR, enable auto-merge, or treat a technical review verdict as merge authorization.

## Context and authority

Load once:

1. `AGENTS.md`;
2. the controlling issue;
3. only the exact source, test, data, model, prompt, artifact, mathematical source, or external input needed by the active outcome.

Exploratory documents such as `docs/CONCEPTUAL_MATH_DIRECTION.md` provide motivation and hypotheses; they are not implementation contracts unless the issue explicitly adopts a bounded part of them.

Do not weaken the issue or choose between materially different implementations when the issue is silent. Return to design instead.

Do not silently promote exploratory notes, hypotheses, brainstorming, or provisional chat conclusions into requirements. Use them only when the controlling issue or an authoritative repository source explicitly adopts them.

On resume, verify branch, `HEAD`, worktree, the controlling issue's single authoritative state label, and new material issue or PR discussion since the last handoff. Reuse unchanged inspected context rather than replaying history.

## Entry gate and workflow state

Before editing, confirm:

- exactly one state label exists;
- it is `execution-ready` or `in-progress`;
- branch/worktree are safe;
- scope, invariants, failure semantics, acceptance, and required inputs are clear;
- no competing branch or PR creates ambiguous ownership;
- the task does not depend on a project-wide plan or phase structure that does not exist.

Before the first implementation edit, use `codex-github-operations` to replace `execution-ready` with `in-progress`. Do not post a comment solely for this transition.

Use label replacements for execution-time returns:

- missing material design decision: `design-required`;
- evidence needed before design: `investigation-required`;
- genuinely unavailable external capability: `blocked`.

`completed` is a post-merge state. The Codex executor must not set `completed` or close the controlling issue as part of implementation delivery. After an explicit user-facing review accepts and merges the ready PR, the merge workflow may set `completed` and close the issue after observing the merge.

## Execution loop

### 1. Establish the bounded outcome

Confirm intended behavior, permitted subsystem, invariants, required validation/evidence, and next review boundary.

### 2. Implement the smallest coherent delta

- follow the issue and repository invariants;
- preserve behavior outside scope;
- add tests/evaluation coverage when required;
- use repository-native integration;
- avoid unrelated cleanup and formatting;
- stop when evidence invalidates the design or acceptance strategy.

### 3. Handle dependencies and external inputs deliberately

For external repositories, models, datasets, mathematical texts, generated corpora, or other inputs:

- preserve identities required by the issue;
- respect licensing and redistribution terms;
- do not treat unavailable dependency state as successful evidence;
- do not publish data or artifacts without rights to do so.

### 4. Validate honestly

Prefer repository-native build, test, lint, type-check, evaluation, benchmark, or corpus-audit commands. Record material deviations and checks not run. Never claim an unrun check passed.

For mathematical/AI-generated outputs, keep distinct:

- syntactic/schema validity;
- AI-judge or heuristic quality;
- human review where required;
- formal verification where available;
- downstream task performance.

### 5. Retain evidence proportionally

Keep enough technical evidence to support the claim being made. Large models, datasets, caches, and bulky logs belong outside Git.

### 6. Publish intentionally

Publish when remote preservation, collaboration, checkpoint review, or PR review requires it. Exact SHAs are useful for review targets, not routine prose.

## Review checkpoints

At a declared checkpoint:

1. publish the exact target;
2. provide scope, material risks, acceptance criteria, and relevant evidence;
3. invoke a fresh independent review when the issue requires one;
4. continue only after a technically safe verdict.

A final technical verdict never authorizes merge by itself.

## Repeated-review circuit breaker

After two consecutive failures in substantially the same validation, attestation, parser, documentation-sync, or bookkeeping mechanism, stop compensating patches and return to design authority before a third cycle unless the defect is materially different. This never waives a continuing technical defect.

## Pull request discipline

Use one PR per controlling issue unless the issue explicitly decomposes delivery. Keep it draft while required implementation, validation, or independent technical review remains incomplete.

When the complete final diff has passed required validation/review, mark the PR **ready for review** and stop execution.

The executor must never:

- merge the PR;
- enable auto-merge;
- interpret technical success as user merge authorization;
- create unrelated roadmap/phases/epics/decision logs merely as workflow bookkeeping;
- close the controlling issue or set it to `completed` before an explicit user-facing review accepts and merges the PR.

## Handoff

Include only what the next actor cannot derive cheaply:

- issue and bounded outcome;
- ready-for-review PR and exact reviewed target when useful;
- material evidence;
- unresolved non-blocking notes;
- immediate next action: user/ChatGPT review and merge decision.
