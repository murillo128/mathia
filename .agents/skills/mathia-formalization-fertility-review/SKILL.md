---
name: mathia-formalization-fertility-review
description: Independently inspect a technically approved Mathia Lean formalization for mathematical deltas, unused formal structure, and clue-worthy research subproducts.
---

# Mathia Formalization Fertility Review

## Responsibility

Use this skill only as the **last independent subagent stage** of `mathia-formalization-executor`, after the exact final Lean candidate has already passed repository-native validation and a separate fresh `codex-independent-review` subagent has returned `PASS` or `PASS_WITH_NOTES` with no unresolved material defect.

This role is not the technical approver. It does not decide whether the Lean artifact is correct enough to publish. Its purpose is different: treat the already-approved formalization as a mathematical observation surface and ask what useful structure the formal proof exposed beyond the canonical finding's own presentation.

The executor must spawn this role in a **fresh isolated context**. It must not inherit the executor's hidden reasoning, the Gate-0 reviewer's hidden reasoning, or the final technical reviewer's hidden reasoning.

A successful fertility review may find nothing. Do not manufacture novelty or clues.

## Entry gate

Do not run this stage before technical approval.

The executor must provide or identify:

1. `AGENTS.md`;
2. this skill;
3. `.agents/skills/mathia-research-clues/SKILL.md`;
4. the controlling formalization issue;
5. the authoritative canonical finding(s) and current persisted review state;
6. the **exact technically approved Lean source/diff**;
7. the final technical-review verdict only as evidence that the target is frozen and safe to inspect, not as a fertility conclusion.

If the exact target changed after technical review, stop and require a new technical review before fertility analysis.

## Independence and ownership

The fertility reviewer must:

- independently read and reconstruct the exact Lean definitions and proof structure relevant to fertility;
- remain read-only over Lean source, canonical findings, adversarial sidecars, issues, and workflow state;
- not implement stronger theorems, refactor Lean, or broaden the controlling issue;
- not treat a formal object as novel merely because Lean needed a representation for it;
- use `mathia-research-clues` only for the narrow proposed-clue write exception below.

If the review discovers a possible correctness problem in the approved theorem/finding correspondence, do **not** hide it in a clue. Return it as a material challenge to the executor, which must route it through the normal adversarial/re-review path before publication.

## Bounded mathematical context

This stage is allowed a slightly wider mathematical view than the technical reviewer because clue fertility may depend on how a formal subproduct interacts with nearby persisted mathematics.

Load only the bounded neighborhood needed to interpret the candidate:

- the canonical finding(s) formalized;
- findings or formal artifacts explicitly cited as dependencies by the issue, finding, or Lean file;
- directly named immediate consequences, bridges, or program-boundary results whose interaction with a newly exposed formal object is necessary to formulate a decisive research question;
- existing local/global clues needed for deduplication.

Do not preload the whole research line or roam the repository looking for arbitrary analogies. The goal is to notice information exposed by **this formalization**, not to perform a general Research Watch run.

## Formal-subproduct audit

The core audit is not just `Lean theorem versus finding theorem`. Inventory the mathematically nontrivial objects that the accepted formalization had to define, expose, factor through, or make canonical.

Inspect especially:

- equivalences and conjugacies;
- quotient types and quotient groups;
- subgroups, submodules, spans, kernels, ranges, images, cokernels, orbit spaces, and stabilizers;
- normal forms, decompositions, factorizations, filtrations, and exact sequences;
- order structures, monotonicity, injective/surjective interfaces, and asymmetric branches;
- finite certificates or auxiliary invariants with more structure than the final scalar statement;
- helper theorems whose mathematical surface is cleaner or more general than the final issue target.

For each serious candidate object, ask explicitly:

1. **What mathematical structure does this object carry?**
2. **Which part of that structure does the final theorem/finding actually consume?**
3. **What information is discarded when the proof compresses the object to a cardinality, dimension, rank, scalar, existence statement, or other endpoint?**
4. **Does that discarded structure, combined with the bounded neighboring mathematics, yield a genuinely different falsifiable question?**

This is the critical `unused formal structure` test. A quotient used only through its cardinality, a kernel used only through its dimension, or an equivalence used only to transfer a count must not automatically be dismissed as proof engineering; inspect the algebraic/geometric/combinatorial structure that survives before deciding it is semantically empty.

## Lean-vs-finding delta audit

Also inspect the ordinary formalization deltas:

- hypotheses present in the issue/finding but not actually consumed;
- extra side conditions or bridges Lean genuinely needs;
- stronger, weaker, cleaner, or differently parameterized exact theorem boundaries suggested by the checked proof;
- one-sided use hidden behind an apparently symmetric informal condition;
- distinct formal objects that prose conflates, or a formal identification the prose fails to exploit;
- degenerate branches that expose the real boundary;
- an alternative representation or invariant that changes the mathematical explanation rather than merely shortening tactics.

The target-specific fertility questions named in the controlling issue are **minimum probes, not an exhaustive checklist**. Answering the expected question does not end this audit. The point of this final independent stage is precisely to notice useful structure that the issue designer and proof executor did not anticipate.

## Clue gate

A formalization delta becomes a clue only when it yields a **distinct, concrete, falsifiable research direction**.

Good examples include:

- unused quotient/subgroup/character structure suggesting a compatibility or classification theorem;
- a kernel normal form whose internal coordinates may constrain intersections with another persisted construction;
- a hypothesis relaxation with a decisive counterexample/proof test;
- two equivalent representations suggesting a new invariant whose necessity can be tested;
- a finite/local certificate suggesting an exact boundary for a wider class.

Not clue-worthy by itself:

- a shorter tactic script;
- a convenient mathlib lemma;
- import or coercion plumbing;
- a renaming or notation improvement;
- merely restating the accepted theorem in different syntax;
- a formal object whose unused structure produces no concrete unresolved consequence.

When the clue gate passes:

1. load and obey `.agents/skills/mathia-research-clues/SKILL.md`;
2. deduplicate against existing local and global clues;
3. create or materially strengthen only a `status: proposed` clue;
4. use `origin: independent-review` unless the clue skill later defines a more specific formalization-fertility origin;
5. cite the canonical finding plus the exact Lean artifact in `based_on`, and include any bounded neighboring finding required to motivate the question;
6. make the `Decisive test` capable of killing the proposed direction cheaply when possible;
7. state explicitly in `Evidence boundary` what Lean did **not** prove.

This role never accepts, rejects, or resolves a clue and never creates a canonical finding.

## Material challenge discovered after approval

Technical approval does not make later mathematical inspection infallible. If this independent stage uncovers a plausible material theorem/finding mismatch:

- do not create a clue for the objection;
- return the exact challenge and evidence to `mathia-formalization-executor`;
- publication is blocked until the executor routes the challenge through the adversarial protocol and obtains any required repaired validation/final technical review;
- after a changed final target is technically approved again, rerun this fertility stage on the new exact target.

## Outcome

Return exactly one fertility outcome:

```text
NO_MATERIAL_FERTILITY_DELTA
PROPOSED_CLUE
MATERIAL_CHALLENGE
```

For `PROPOSED_CLUE`, report every created/strengthened clue path and the formal structure that motivated it.

For `NO_MATERIAL_FERTILITY_DELTA`, briefly state which serious formal subproducts were inspected and why their unused structure did not yield a distinct falsifiable direction. Do not merely say that Lean proves the intended theorem.

For `MATERIAL_CHALLENGE`, state the exact mismatch and evidence; do not issue a technical `PASS`/`FAIL` verdict because that belongs to `codex-independent-review`.

## Publication handoff

The fertility reviewer does not publish Lean or close the issue. It hands its outcome back to `mathia-formalization-executor`.

When the outcome is `NO_MATERIAL_FERTILITY_DELTA` or `PROPOSED_CLUE`, the executor may proceed to its direct-main publication gate. Any proposed clue may be included in the same focused direct-main publication as the already-approved Lean artifact, subject to the clue/path/concurrency gates.

A `MATERIAL_CHALLENGE` blocks publication.