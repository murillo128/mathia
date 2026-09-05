---
name: mathia-formalization-fertility-review
description: Independently inspect a technically approved Mathia Lean formalization for mathematical deltas, information lost by formal abstraction, unused formal structure, and clue-worthy research subproducts.
---

# Mathia Formalization Fertility Review

## Responsibility

Use this skill only as the **last independent subagent stage** of `mathia-formalization-executor`, after the exact final Lean candidate has already passed repository-native validation and a separate fresh `codex-independent-review` subagent has returned `PASS` or `PASS_WITH_NOTES` with no unresolved material defect.

This role is not the technical approver. It does not decide whether the Lean artifact is correct enough to publish. Its purpose is different: treat the already-approved formalization as a mathematical observation surface and ask what useful structure the formal proof exposed, what source structure the chosen formal abstraction forgot, and whether either direction yields a distinct falsifiable research question beyond the canonical finding's own presentation.

The executor must spawn this role in a **fresh isolated context**. It must not inherit the executor's hidden reasoning, the Gate-0 reviewer's hidden reasoning, or the final technical reviewer's hidden reasoning.

A successful fertility review may find nothing. Do not manufacture novelty or clues. `NO_MATERIAL_FERTILITY_DELTA` is nevertheless a substantive conclusion: it is valid only after both mandatory discovery lenses and the bounded candidate-kill procedure below have actually been performed.

## Entry gate

Do not run this stage before technical approval.

The executor must provide or identify:

1. `AGENTS.md`;
2. this skill;
3. `.agents/skills/mathia-research-clues/SKILL.md`;
4. the controlling formalization issue;
5. the authoritative canonical finding(s) and current persisted review state;
6. the **exact technically approved Lean source/diff**;
7. the final technical-review verdict only as evidence that the target is frozen and safe to inspect, not as a fertility conclusion;
8. when available, the executor's compact **ephemeral fertility handoff** described below.

If the exact target changed after technical review, stop and require a new technical review before fertility analysis.

## Independence and the ephemeral fertility handoff

The fertility reviewer must:

- independently read and reconstruct the exact Lean definitions and proof structure relevant to fertility;
- remain read-only over Lean source, canonical findings, adversarial sidecars, issues, and workflow state;
- not implement stronger theorems, refactor Lean, or broaden the controlling issue;
- not treat a formal object as novel merely because Lean needed a representation for it;
- use `mathia-research-clues` only for the narrow proposed-clue write exception below.

The executor may pass a compact ephemeral handoff containing only **explicit audit surfaces**, not hidden chain-of-thought or conclusions to trust. Appropriate entries are:

- representations or reductions chosen to make the theorem formalizable;
- source bridges deliberately left outside Lean;
- hypotheses observed to be unused or used only in one direction;
- helper objects, normal forms, quotients, filtrations, factorizations, kernels/ranges, or degenerate branches that appeared during proof engineering;
- alternative exact representations encountered and then abandoned;
- concrete non-blocking mathematical observations that would otherwise disappear at the fresh-context boundary.

Treat every handoff item as an untrusted lead. Reconstruct it independently from the frozen artifact and authoritative mathematics before using it. The handoff preserves observation surfaces across context isolation; it does not weaken reviewer independence and is not a clue proposal by itself.

For `mathia-research-clues` purposes, **this role is the formalization-specific Independent Reviewer clue producer**. The generic `codex-independent-review` technical role is read-only and must not exercise that clue exception. Keep the existing `origin: independent-review` value for compatibility unless the clue skill later introduces a dedicated fertility-review origin.

If the review discovers a possible correctness problem in the approved theorem/finding correspondence, do **not** hide it in a clue. Return it as a material challenge to the executor, which must route it through the normal adversarial/re-review path before publication.

## Bounded mathematical context

This stage is allowed a slightly wider mathematical view than the technical reviewer because clue fertility may depend on how a formal subproduct interacts with nearby persisted mathematics.

Load only the bounded neighborhood needed to interpret the candidate:

- the canonical finding(s) formalized;
- findings, source documents, or formal artifacts explicitly cited as dependencies by the issue, finding, or Lean file;
- external/public formalization artifacts explicitly named by the controlling issue or canonical finding when they are needed to reconstruct the source-to-formal map;
- directly named immediate consequences or bridges;
- **one-hop downstream findings that explicitly cite the canonical finding or exact formal artifact**, when their interaction is needed to test whether an exposed structure is already consumed or still leaves a residual question;
- existing local/global clues needed for deduplication.

Do not preload the whole research line or roam the repository looking for arbitrary analogies. Reverse-reference inspection is one hop only unless a concrete surviving candidate requires one additional exact source to formulate or kill its decisive test. The goal is to notice information exposed by **this formalization and its abstraction boundary**, not to perform a general Research Watch run.

## Mandatory discovery lens A: formal-internal structure

The first pass is the ordinary formal-subproduct audit. Inventory the mathematically nontrivial objects that the accepted formalization had to define, expose, factor through, or make canonical.

Inspect especially:

- equivalences and conjugacies;
- quotient types and quotient groups;
- subgroups, submodules, spans, kernels, ranges, images, cokernels, orbit spaces, and stabilizers;
- normal forms, decompositions, factorizations, filtrations, flags, associated graded layers, and exact sequences;
- order structures, monotonicity, injective/surjective interfaces, and asymmetric branches;
- finite certificates or auxiliary invariants with more structure than the final scalar statement;
- helper theorems whose mathematical surface is cleaner or more general than the final issue target;
- concrete encodings such as nested sums/products, block indices, coordinates, or constructors that may be the formal shadow of a more canonical mathematical object.

For each serious candidate object, ask explicitly:

1. **What mathematical structure does this object carry?**
2. **Which part of that structure does the final theorem/finding actually consume?**
3. **What information is discarded when the proof compresses the object to a cardinality, dimension, rank, scalar, existence statement, diagonal target, or other endpoint?**
4. **Is the concrete Lean representation an instance of a more canonical construction such as a flag-depth operator, graded object, signed Gram form, quotient map, or universal finite certificate?**
5. **Does any unused structure, combined with the bounded neighboring mathematics, yield a genuinely different falsifiable question?**

A quotient used only through its cardinality, a kernel used only through its dimension, an equivalence used only to transfer a count, or a nested block encoding used only entrywise must not automatically be dismissed as proof engineering. Inspect the algebraic/geometric/combinatorial structure that survives before deciding it is semantically empty.

## Mandatory discovery lens B: source-to-formal information loss

Independently reconstruct the map

```text
source mathematics -> chosen formal abstraction -> Lean theorem -> final scalar/structural conclusion
```

Do not start only from the Lean theorem. Identify every mathematically material reduction that happened **before** Lean's principal theorem surface and ask what relations were forgotten.

Inspect especially whether formalization replaced a source object by:

- an arbitrary matrix/operator after forgetting how it was generated;
- coordinates after forgetting a subspace, flag, symmetry, or basis-construction relation;
- independent block entries after forgetting shared factors or common generators;
- a scalar, norm, trace, determinant, rank, dimension, or inertia count after forgetting the richer object producing it;
- an abstract hypothesis after forgetting a source-side sign, positivity, multiplicity, conjugacy, Gram, tensor, orbit, interpolation, or arithmetic constraint;
- a finite certificate after forgetting how certificates for different indices are coupled.

For every such abstraction ask:

1. **Which exact source relations are no longer expressible in the Lean theorem as stated?**
2. **Do those lost relations make quantities that Lean treats as independent actually share generators, factors, signs, kernels, ranges, or conservation laws?**
3. **If one restores just one lost relation while keeping the checked theorem, does a stronger compatibility identity, obstruction, generalization, or classification question appear?**
4. **Can that residual question be killed cheaply by an exact derivation, a small counterexample, a bounded computation, or a targeted prior-art check?**

This pass is mandatory even when the formal-internal pass found no candidate. A formalization can be mathematically fertile precisely because its smallest faithful theorem surface exposed what had to be discarded to become small.

## Lean-vs-finding delta audit

Across both discovery lenses also inspect the ordinary formalization deltas:

- hypotheses present in the issue/finding but not actually consumed;
- extra side conditions or bridges Lean genuinely needs;
- stronger, weaker, cleaner, or differently parameterized exact theorem boundaries suggested by the checked proof;
- one-sided use hidden behind an apparently symmetric informal condition;
- distinct formal objects that prose conflates, or a formal identification the prose fails to exploit;
- degenerate branches that expose the real boundary;
- an alternative representation or invariant that changes the mathematical explanation rather than merely shortening tactics.

The target-specific fertility questions named in the controlling issue are **minimum probes, not an exhaustive checklist**. Answering the expected question does not end this audit.

## Bounded candidate refinement loop

After **both** mandatory discovery lenses, synthesize concrete candidate research questions. Do not require the first pass to have found a clue before running the second pass.

For each candidate that is more than a wording observation, run a bounded kill/refinement loop:

1. **Round 1 is mandatory for every candidate.** Reconstruct it from authoritative objects, check the bounded neighboring findings and existing clues, and try to kill it by duplication, an immediate counterexample, a known theorem, a stronger already-persisted result, or by showing that the apparent extra structure has no unresolved consequence.
2. If the candidate survives and Round 1 exposes a **new mathematical object, relation, factorization, information-loss boundary, or exact residual** with a concrete unresolved consequence, perform **one additional refinement round**. Tighten the question and decisive test around that new structure and try to kill it again.
3. Stop after at most **two refinement rounds after discovery**. Do not continue merely because prose can be improved, more analogies can be listed, or the agent can invent another speculative layer.

Continue from one round to the next only when the previous round exposed genuinely new mathematical structure with a falsifiable residual. Stop immediately when a candidate is duplicated, classicalized with no residual, contradicted, subsumed by an existing finding/clue, or reduced to non-mathematical proof engineering.

Several raw candidates may be considered, but only genuinely distinct survivors should become clues. Prefer strengthening one precise survivor over proliferating nearby variants.

## Clue gate

A formalization delta becomes a clue only when it yields a **distinct, concrete, falsifiable research direction** that survives the bounded refinement loop.

Good examples include:

- unused quotient/subgroup/character structure suggesting a compatibility or classification theorem;
- a kernel normal form whose internal coordinates may constrain intersections with another persisted construction;
- a hypothesis relaxation with a decisive counterexample/proof test;
- two equivalent representations suggesting a new invariant whose necessity can be tested;
- a finite/local certificate suggesting an exact boundary for a wider class;
- a source-generated matrix/operator abstraction that forgot shared Gram/tensor factors, leading to a concrete coupling identity or inequality to prove;
- a concrete multi-block Lean encoding that is really a canonical flag/graded construction and suggests an exact wider theorem.

Not clue-worthy by itself:

- a shorter tactic script;
- a convenient mathlib lemma;
- import or coercion plumbing;
- a renaming or notation improvement;
- merely restating the accepted theorem in different syntax;
- a formal object whose unused structure produces no concrete unresolved consequence;
- a candidate that survived only because no bounded attempt was made to falsify or deduplicate it.

When the clue gate passes:

1. load and obey `.agents/skills/mathia-research-clues/SKILL.md`;
2. deduplicate against existing local and global clues;
3. create or materially strengthen only a `status: proposed` clue;
4. use `origin: independent-review` unless the clue skill later defines a more specific formalization-fertility origin;
5. cite the canonical finding plus the exact Lean artifact in `based_on`, and include any bounded neighboring finding required to motivate the question;
6. make the `Decisive test` capable of killing the proposed direction cheaply when possible;
7. state explicitly in `Evidence boundary` what Lean did **not** prove and, for source-loss clues, which restored source relation is still unproved or unused.

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

For `PROPOSED_CLUE`, report every created/strengthened clue path, which discovery lens exposed it, and the formal/source structure that survived refinement.

For `NO_MATERIAL_FERTILITY_DELTA`, briefly state:

- which serious formal subproducts were inspected;
- which source-to-formal abstraction losses were inspected;
- which candidate questions, if any, were killed and why.

Do not merely say that Lean proves the intended theorem.

For `MATERIAL_CHALLENGE`, state the exact mismatch and evidence; do not issue a technical `PASS`/`FAIL` verdict because that belongs to `codex-independent-review`.

## Publication handoff

The fertility reviewer does not publish Lean or close the issue. It hands its outcome back to `mathia-formalization-executor`.

When the outcome is `NO_MATERIAL_FERTILITY_DELTA` or `PROPOSED_CLUE`, the executor may proceed to its direct-main publication gate. Any proposed clue may be included in the same focused direct-main publication as the already-approved Lean artifact, subject to the clue/path/concurrency gates.

A `MATERIAL_CHALLENGE` blocks publication.