---
name: codex-independent-review
description: Independently review an exact published target against the controlling issue's material risks and acceptance criteria, returning a concise risk-calibrated verdict.
---

# Codex Independent Review

## Responsibility

Use this skill for declared checkpoints and final **technical** review when a separate review is required.

The reviewer owns independent exact-target inspection, proportional validation, materiality, and the technical verdict. It does not implement fixes, redesign the issue, mutate workflow state, continue execution, authorize/perform merge, or perform open-ended research discovery.

For a completed Mathia Lean formalization, the reviewer also owns an independent **formal-to-human correspondence review**: reconstruct the Lean theorem in ordinary mathematical language, explain the proof as mathematics rather than tactics, and state exactly what surrounding mathematics remains outside the formal theorem.

The formal-to-human reconstruction may expose a correctness-relevant mathematical mismatch. Report such a mismatch as part of the technical verdict. **Do not turn this final technical review into a clue-generation or fertility-search stage.** `mathia-formalization-executor` launches a separate fresh post-approval fertility subagent only after this review has returned `PASS` or `PASS_WITH_NOTES`.

A `PASS` or `PASS_WITH_NOTES` means the reviewed target is technically safe to progress according to the controlling workflow. It is not merge authorization and does not mean that a later independent fertility audit will find no mathematical subproducts.

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

For Mathia Lean formalizations, also load the authoritative informal claim/finding and the exact Lean source being reviewed.

Do not preload neighboring findings merely to search for possible research leads. That belongs to the separate post-approval fertility stage.

## Independence

The reviewer must:

- use a fresh context that does not inherit executor hidden reasoning;
- inspect exactly the requested target;
- remain read-only over the reviewed implementation, research state, and workflow state;
- judge evidence rather than intent;
- not implement corrections or advance later work;
- not create/update clues, canonical findings, or adversarial sidecars.

There is **no research-tree write exception** in this technical-review role.

## Materiality

Return `FAIL` only when a finding:

- violates an explicit invariant or acceptance criterion;
- exposes a plausible normal-path defect;
- makes required evidence materially false, incomplete, or misleading;
- introduces unapproved scope, architecture, dependency, data handling, or behavior;
- makes progression unsafe.

For Lean formalization, a material mismatch between the mathematical claim and the theorem actually stated in Lean is a correctness defect even when the Lean proof itself checks.

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

### 3. Reconstruct completed Lean formalizations as mathematics

When the exact target contains a completed Mathia Lean proof, do not stop at compilation and theorem-signature inspection.

Independently perform all of the following:

1. **Human theorem reconstruction.** Read the Lean definitions, quantifiers, hypotheses, domains, conventions, and conclusion and restate the theorem in ordinary mathematical notation and prose without relying on the surrounding informal claim.
2. **Correspondence check.** Compare that reconstructed theorem with the authoritative Mathia claim. Identify whether they are equivalent, one is stronger/weaker, or a bridge is being assumed outside Lean. Pay special attention to indexing, normalization, gauge, singularities, boundary cases, coercions, and encoded side conditions.
3. **Human proof reconstruction.** Convert the formal proof into a concise mathematical proof or proof sketch that exposes the actual mathematical steps. Compress tactic noise and library plumbing; preserve the substantive lemmas, reductions, inequalities, invariants, case splits, and representation changes that make the theorem true.
4. **Explanation/correctness comparison.** Compare the reconstructed proof with any persisted informal proof. If a difference changes theorem meaning, hides a required bridge, weakens/strengthens the formal claim, or otherwise affects correctness, report it. A merely different valid proof representation is not a technical defect by itself.
5. **Evidence boundary.** State precisely what the Lean theorem does not prove: upstream identities accepted as definitions/inputs, analytic or asymptotic bridges, geometric interpretations, novelty claims, or surrounding consequences.

The purpose is to make the chain

```text
informal claim <-> Lean statement <-> human mathematical proof <-> checked Lean proof
```

auditable.

A human proof need not mimic the tactic sequence. A better mathematical compression is preferred when it is faithful to the same formal argument.

### 4. Do not perform the post-approval fertility audit here

For Mathia formalization, stop once technical correspondence, proof integrity, boundaries, and acceptance criteria are decided.

Do **not** use the technical review to decide whether a quotient, kernel, normal form, factorization, alternate representation, hypothesis relaxation, or other formal subproduct deserves a clue merely because you noticed it while reconstructing the proof.

You may mention a representation change when it is necessary to explain the proof or a technical mismatch, but do not investigate its downstream research fertility and do not create a clue.

After `PASS` or `PASS_WITH_NOTES`, `mathia-formalization-executor` must spawn a different fresh subagent under:

```text
.agents/skills/mathia-formalization-fertility-review/SKILL.md
```

That later role owns the deliberate Lean-vs-finding/subproduct audit and any narrow proposed-clue write exception.

### 5. Test proportionally

Run issue-defined validation when supported. Prefer checks capable of falsifying the claimed outcome. Distinguish commands personally run from committed/external evidence inspected.

### 6. Determine whether review is final

A checkpoint can serve as final technical review when it covers the complete final diff and all remaining acceptance criteria. Later technical changes invalidate that verdict for the changed target.

For a completed Mathia Lean formalization, final technical review is complete when the formal-to-human correspondence and evidence boundary above have been reconstructed. **Fertility review is deliberately not part of this verdict.**

Final technical review completion allows the controlling executor to enter its post-approval fertility stage. It does not authorize merge or publication by itself.

### 7. Report briefly

Record exact target, verdict, material findings, validation/evidence inspected, and the smallest required delta or non-blocking notes.

For completed Mathia Lean formalizations, also record:

- the human mathematical statement corresponding to the principal Lean theorem(s);
- the concise human proof/proof structure;
- correspondence verdict against the authoritative claim;
- explicit unformalized boundary.

Do not report a fertility outcome or proposed clue path from this technical-review invocation.

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