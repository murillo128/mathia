---
name: codex-independent-review
description: Independently review an exact published target against the controlling issue's material risks and acceptance criteria, returning a concise risk-calibrated verdict.
---

# Codex Independent Review

## Responsibility

Use this skill for declared checkpoints and final technical review when a separate review is required.

The reviewer owns independent exact-target inspection, proportional validation, materiality, and the technical verdict. It does not implement fixes, redesign the issue, mutate workflow state, continue execution, or authorize/perform merge.

For a completed Mathia Lean formalization, the reviewer also owns an independent **formal-to-human correspondence review**: reconstruct the Lean theorem in ordinary mathematical language, explain the proof as mathematics rather than tactics, and state exactly what surrounding mathematics remains outside the formal theorem.

For Mathia Lean, the reviewer additionally treats formalization as a possible **fertility instrument**. The target theorem may be prior art or otherwise non-novel; the review must still ask whether the exact formal proof exposed a mathematically meaningful object, asymmetry, hypothesis boundary, factorization, or representation that the informal source did not make explicit. This is an observation obligation, not a requirement to manufacture a clue.

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

For Mathia Lean formalizations, also load the authoritative informal claim/finding and the exact Lean source being reviewed.

## Independence

The reviewer must:

- use a fresh context that does not inherit executor hidden reasoning;
- inspect exactly the requested target;
- remain read-only over the reviewed implementation and workflow state;
- judge evidence rather than intent;
- not implement corrections or advance later work.

The only research-state write exception is the narrow Mathia formalization clue handoff defined below. It does not permit implementation edits, issue-state mutation, adversarial-review edits, canonical-finding edits, or clue disposition changes.

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
4. **Explanation comparison.** Compare the reconstructed proof with any persisted informal proof. If the formal proof gives a materially different explanation or representation of the same theorem, state that difference explicitly rather than treating it as mere proof-engineering trivia.
5. **Evidence boundary.** State precisely what the Lean theorem does not prove: upstream identities accepted as definitions/inputs, analytic or asymptotic bridges, geometric interpretations, novelty claims, or surrounding consequences.

The purpose is not to require a second formal proof. It is to make the chain

```text
informal claim <-> Lean statement <-> human mathematical proof <-> checked Lean proof
```

auditable.

A human proof need not mimic the tactic sequence. A better mathematical compression is preferred when it is faithful to the same formal argument.

### 3a. Formalization-fertility audit

For every completed Mathia Lean formalization, perform a short but active fertility audit after reconstructing the human proof. This audit is mandatory whether the target theorem is new, classical, or known prior art.

Ask explicitly:

> **What did Lean have to prove, factor, define, separate, or use that the finding or source did not treat as a first-class mathematical object?**

Inspect especially:

- hypotheses actually consumed versus hypotheses merely present in the informal statement;
- one-sided injectivity/surjectivity or monotonicity hidden behind an apparently symmetric informal condition;
- intermediate lemmas whose theorem surface is cleaner or more general than the final target;
- exact kernel/range/image descriptions, quotients, normal forms, factorizations, finite certificates, or invariant decompositions introduced because the formal proof needed them;
- case splits or degenerate branches that reveal the true theorem boundary;
- two distinct proof representations that become visibly equivalent only after formal reconstruction;
- proof dependencies that suggest the target belongs to a broader structural class than its original application.

Do not confuse library plumbing with mathematics. A helper is fertile only when its content changes how the theorem can be understood, generalized, classified, or falsified.

The audit must end with one of:

```text
no material fertility delta found
material fertility delta / clue candidate
material finding-or-statement divergence
```

`no material fertility delta found` is a fully successful outcome. A fertility-motivated formalization is an experiment in conceptual pressure, not a quota for discoveries.

A material finding-or-statement divergence is a correctness/research challenge and must follow the adversarial-review route owned by the Mathia formalization workflow; do not launder it into a clue.

### 4. Extract research clues from representation changes

For a Mathia Lean formalization review, the correspondence reconstruction and fertility audit are also observation surfaces.

If translating the Lean proof back into mathematics exposes a **distinct, falsifiable research direction** -- for example:

- an alternative proof that explains the theorem through a genuinely different representation;
- a finite/local certificate replacing apparently essential global structure;
- a new invariant, equivalence, normal form, or obstruction;
- a plausible generalization suggested by which hypotheses the Lean proof actually uses;
- two independent explanations of the same result whose coexistence suggests a deeper common mechanism;
- a classical/prior-art theorem whose formal proof reveals a new structural interface worth testing beyond the original application;

then load:

```text
.agents/skills/mathia-research-clues/SKILL.md
```

Deduplicate against existing clues and create or materially strengthen only a `status: proposed` clue under the owning research line (or the global clue inbox when genuinely cross-line).

A shorter tactic script, easier library lemma, import simplification, or merely shorter proof is **not** clue-worthy. The key test is whether the alternative proof changes the mathematical explanation/representation and yields a concrete research question with a decisive test.

The WP-014 pattern is canonical: a global Mittag--Leffler explanation and an independent finite Taylor/polynomial certificate of the same Schiffer obstruction can motivate questions about finite local certificates or deeper local invariants. The clue is the new research question, not the fact that one proof is shorter.

Likewise, prior-art status of the theorem does not prevent a clue when the **new research question** comes from a structural delta exposed by formalization. The clue must not imply that the prior-art theorem itself is novel.

The reviewer may not:

- set a clue to `accepted`, `rejected`, or `resolved`;
- create or rewrite a canonical finding;
- create/update an adversarial `.review.md` as part of this exception;
- modify the Lean target to make the clue easier to state.

Clue persistence is separate from the technical verdict. Report any created/strengthened clue path in the review handoff.

### 5. Test proportionally

Run issue-defined validation when supported. Prefer checks capable of falsifying the claimed outcome. Distinguish commands personally run from committed/external evidence inspected.

### 6. Determine whether review is final

A checkpoint can serve as final technical review when it covers the complete final diff and all remaining acceptance criteria. Later technical changes invalidate that verdict for the changed target.

For a completed Mathia Lean formalization, final review is not complete until the formal-to-human correspondence, fertility audit, and evidence boundary above have been reconstructed.

Final technical review completion allows a ready-for-review handoff. It does not authorize merge.

### 7. Report briefly

Record exact target, verdict, material findings, validation/evidence inspected, and the smallest required delta or non-blocking notes.

For completed Mathia Lean formalizations, also record:

- the human mathematical statement corresponding to the principal Lean theorem(s);
- the concise human proof/proof structure;
- correspondence verdict against the authoritative claim;
- explicit unformalized boundary;
- fertility-audit outcome;
- any proposed clue path created from a material representation change.

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
