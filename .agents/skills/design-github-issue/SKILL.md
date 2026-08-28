---
name: design-github-issue
description: Define a self-contained execution-ready GitHub issue that resolves material decisions and gives a fresh executor the facts needed to implement safely, then explain the designed mechanism separately to the user in chat.
---

# Design a GitHub Execution Issue

## Responsibility

Use this skill before non-trivial implementation starts, or when execution returns because a material design or validation decision is unresolved.

The design authority owns:

- the observable outcome;
- material architectural and validation decisions required for that bounded task;
- the task-specific context needed to execute safely;
- scope, invariants, exclusions, failure semantics, and acceptance criteria;
- risk-based review checkpoints when useful;
- a separate concise explanation to the user of how the designed mechanism works when that helps them understand the project.

It does not implement code, operate branches, publish commits, perform independent review, or grant the executor merge authority.

## Assume a fresh executor

Design the issue for an executor that has no access to the design session's reasoning and should not need to reconstruct material facts from old chats or unrelated history.

The issue must contain every task-specific fact, decision, constraint, and acceptance rule required for correct implementation. Links are supporting references, not substitutes for material instructions.

## Keep user teaching outside the issue

The GitHub issue is an execution contract for Codex or another implementation agent. Do not add tutorial-style sections solely to teach the user.

After designing or publishing the issue, explain non-obvious mechanisms separately in chat. Focus on end-to-end behavior, define specialized terms when needed, and keep the explanation proportional.

## Design-session traceability

When a ChatGPT design session publishes a new issue:

- if the current private conversation URL is available, add `Design session: [ChatGPT](<private-conversation-url>)` to the initial issue body;
- never create or use a public/shared ChatGPT link for this provenance; if the private conversation URL is unavailable, omit the link rather than blocking issue publication;
- after GitHub assigns the issue number, if the environment exposes a supported conversation-title action, rename the current ChatGPT conversation to `#<issue-number> — <issue-title>`;
- do not add a repository prefix to the conversation title, and do not fail or block the workflow when conversation renaming is unavailable.

This traceability applies only to the design session. Do not add Codex implementation-session identifiers or general session bookkeeping to the issue.

## Load material design context

Start with:

1. `AGENTS.md` when present;
2. the user request or existing controlling issue.

Then inspect only what is needed to settle the task:

- relevant exploratory/specification documents;
- source seams, APIs, ownership boundaries, state, and tests;
- baseline behavior or prior experiment evidence that constrains the work;
- required models, datasets, mathematical sources, artifacts, dependencies, or environment inputs;
- overlapping current work when it materially constrains the design.

Do not promote exploratory hypotheses from `docs/CONCEPTUAL_MATH_DIRECTION.md` into requirements unless the current task explicitly chooses them.

## The issue is the executor's complete contract

Depending on the task, include:

- current limitation and observable goal;
- accepted baseline behavior and defaults that must remain unchanged;
- relevant model, dataset, source-material, dependency, or artifact inputs;
- inspected implementation seams and data shapes;
- resolved API/configuration semantics and invalid combinations;
- ordering, failure behavior, and resource constraints where relevant;
- permitted implementation scope and explicit exclusions;
- validation targets, fixtures, environments, datasets, and artifacts;
- objective acceptance criteria and material review risks;
- prior negative evidence when it prohibits repeating a known-invalid mechanism.

Do not copy generic Git, publication, review, merge, or reporting procedure already owned by skills. An issue may state observable post-merge completion conditions, but it must not authorize Codex/the executor to merge or enable auto-merge.

## Design method

### 1. Define the observable outcome

State what must become true, why it matters, the current limitation, and the boundary of the requested change.

### 2. Resolve only material unknowns

Resolve questions that can change behavior, compatibility, architecture, data handling, model behavior, mathematical validity, evaluation, licensing, or deployment strategy.

Do not invent project-wide plans, phases, schemas, or architectural commitments just because they might be useful later.

### 3. Bound implementation without under-specifying it

Define the smallest coherent outcome, permitted subsystem/files, explicit exclusions, and invariants. Include exact files or seams when an executor could otherwise modify the wrong layer.

### 4. Define validation that proves the outcome

Specify repository-native build, test, lint, evaluation, or benchmark targets as appropriate; relevant correctness/data/performance checks; required external inputs; and objective pass/fail criteria.

For AI-generated mathematical or conceptual data, define separately what is mechanically checkable, what is AI-judged, and what requires human or formal review.

### 5. Keep evidence proportional

Capture enough evidence to support the decision or comparison being made. Do not require elaborate provenance or immutable archives unless the task specifically needs them.

### 6. Add review checkpoints when they reduce risk

Use independent checkpoints only for distinct material risks such as architecture, data integrity, mathematical faithfulness, evaluation validity, numerical behavior, or broad refactoring.

A final-capable review is a technical gate to the ready-for-review handoff, not merge authorization.

### 7. Define restart semantics

Distinguish local implementation defects, design defects, evidence gaps, replaceable tool failures, and real blockers. Repeated failure of the same mechanism should trigger design review rather than endless compensating patches.

### 8. Check overlap

Inspect only plausibly overlapping issues, PRs, branches, and recent attempts. Avoid reconstructing unrelated history.

## Execution-ready check

Before declaring an issue ready for execution, confirm:

- a fresh executor can implement without hidden design-session reasoning;
- observable outcome and terminology are unambiguous;
- all material task-specific facts and decisions are present;
- scope, invariants, failure behavior, and acceptance are clear;
- required inputs and validation capabilities are identified;
- no exploratory project hypothesis was silently promoted to a settled requirement;
- no issue text grants executor merge or auto-merge authority.

## Suggested issue structure

```markdown
# <Outcome-oriented title>

## Goal and current limitation
<Observable outcome, why it matters, and current behavior.>

## Baseline and inputs
<Material baseline facts, sources, models, datasets, artifacts, and defaults.>

## Resolved technical contract
<Required data flow, semantics, failure behavior, and concrete seams.>

## Scope
### In scope
### Out of scope
### Invariants

## Validation and evidence
<Required targets, cases, environment, artifacts, and objective gates.>

## Checkpoints
<Only distinct material-risk checkpoints when useful.>

## Delivery
<PR shape, dependency/publication boundaries, ready-for-review handoff, and observable post-merge completion. Do not authorize executor merge.>
```
