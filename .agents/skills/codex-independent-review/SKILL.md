---
name: codex-independent-review
description: Independently review an exact published target against the controlling issue's material risks and acceptance criteria, returning a concise risk-calibrated verdict.
---

# Codex Independent Review

## Responsibility

Use this skill for declared checkpoints and final technical review when a separate review is required.

The reviewer owns independent exact-target inspection, proportional validation, materiality, and the technical verdict. It does not implement fixes, redesign the issue, mutate workflow state, publish commits, continue execution, or authorize/perform merge.

A `PASS` or `PASS_WITH_NOTES` means the reviewed target is technically safe to progress according to the controlling workflow. It is not merge authorization.

## Trust the issue as the technical contract

Judge the implementation against the controlling issue's explicit contract. Do not replace settled task decisions with a new design merely because another approach is possible.

Exploratory repository notes provide context but are not acceptance criteria unless the issue explicitly adopts them.

## Minimal review packet

A fresh reviewer needs:

1. `AGENTS.md`;
2. this skill;
3. the controlling issue or exact checkpoint contract;
4. the exact published target/range;
5. the evidence required by that checkpoint.

Load prior history only when an unresolved material finding or repeated-review circuit breaker depends on it.

## Independence

The reviewer must:

- use a fresh context that does not inherit executor hidden reasoning;
- inspect exactly the requested target;
- remain read-only;
- judge evidence rather than intent;
- not implement corrections or advance later work.

## Materiality

Return `FAIL` only when a finding:

- violates an explicit invariant or acceptance criterion;
- exposes a plausible normal-path defect;
- makes required evidence materially false, incomplete, or misleading;
- introduces unapproved scope, architecture, dependency, data handling, or behavior;
- makes progression unsafe.

Use `PASS_WITH_NOTES` for editorial wording, bookkeeping, optional hardening, or robustness outside the declared boundary when the technical outcome remains trustworthy.

For every `FAIL`, state the exact criterion violated, material consequence, and smallest corrective delta or why design must reopen.

## Review procedure

### 1. Establish risk and authority

Identify outcome, scope, invariants, acceptance criteria, evidence, exact target, and failure boundary.

### 2. Inspect the exact target

Check diff/scope compliance, implementation/integration, credible evidence, plausible correctness/data/evaluation failures, unexpected dependencies or restricted artifacts, and safety to proceed.

For conceptual mathematical or AI-generated datasets, pay particular attention to:

- source faithfulness and unsupported claims;
- accidental leakage or contamination;
- whether AI-judge scores are being misrepresented as mathematical correctness;
- licensing/provenance claims required by the issue;
- evaluation that merely rewards style instead of the intended mathematical capability.

### 3. Test proportionally

Run issue-defined validation when supported. Prefer checks capable of falsifying the claimed outcome. Distinguish commands personally run from committed/external evidence inspected.

### 4. Determine whether review is final

A checkpoint can serve as final technical review when it covers the complete final diff and all remaining acceptance criteria. Later technical changes invalidate that verdict for the changed target.

Final technical review completion allows a ready-for-review handoff. It does not authorize merge.

### 5. Report briefly

Record exact target, verdict, material findings, validation/evidence inspected, and the smallest required delta or non-blocking notes.

## Repeated-review circuit breaker

When two consecutive reviews fail for substantially the same validation, attestation, parser, documentation-sync, or bookkeeping mechanism:

- stop open-ended searches for representational variants;
- use `PASS_WITH_NOTES` when progression is technically safe and the remaining concern is non-material;
- request design review when the validation strategy itself prevents a trustworthy decision;
- require explicit design-authority direction before a third corrective review of the same mechanism.

The circuit breaker never waives a continuing material defect.

## Verdicts

Return exactly one:

- `PASS`
- `PASS_WITH_NOTES`
- `FAIL`
- `BLOCKED`

Transport failure is an attempt result, not a verdict.
