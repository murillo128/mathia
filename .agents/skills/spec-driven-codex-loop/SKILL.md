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

## Entry gate

Before editing, confirm:

- branch/worktree are safe;
- scope, invariants, failure semantics, acceptance, and required inputs are clear;
- no competing branch or PR creates ambiguous ownership;
- the task does not depend on a project-wide plan or phase structure that does not exist.

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

## Pull request discipline

Use one PR per controlling issue unless the issue explicitly decomposes delivery. Keep it draft while required implementation, validation, or independent technical review remains incomplete.

When the complete final diff has passed required validation/review, mark the PR **ready for review** and stop execution.

The executor must never:

- merge the PR;
- enable auto-merge;
- interpret technical success as user merge authorization;
- create unrelated roadmap/phases/epics/decision logs merely as workflow bookkeeping.

## Handoff

Include only what the next actor cannot derive cheaply:

- issue and bounded outcome;
- ready-for-review PR and exact reviewed target when useful;
- material evidence;
- unresolved non-blocking notes;
- immediate next action: user/ChatGPT review and merge decision.
