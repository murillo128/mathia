# Intuition-fertility pre-test v2

## Status

**Current #30 contract.** This v2 supersedes v1 after resolving the original panel's qwen-lean Phase-2 exposure. V0/v1 and the self-audit remain provenance.

The main scientific change is that target selection is now constrained by the formal worker's actual training lineage rather than by the fame or explanatory quality of a theorem. Five of six original targets were directly exposed in Phase-5 optimizer training and are therefore retired from primary fertility scoring. The primary panel will be rebuilt from Phase-2 `heldout` before qwen-lean outcomes are inspected.

The experiment still asks whether compact strategic mathematical guidance can causally increase the yield of Lean-verified whole proofs from a separate formal specialist, and whether Qwen base leaves useful headroom relative to a strong frontier reference.

## Working decomposition

The training hypothesis remains exploratory:

```text
mathematical concepts
        |
reusable conceptual moves
        |
candidate intuitions emerge
        |
frontier-teacher bootstrap when useful
        |
formal-worker fertility signal
        |
possible later optimization
```

#30 validates the objects and measurement channel only. It does not authorize Mathia training.

## Provisional concept families

Use these as a small experimental substrate, not a permanent ontology:

- maps, composition, and information flow;
- reversibility and inverse structure;
- equivalence, fibers/kernels, and quotients;
- decomposition, products, and partitions;
- symmetry, actions, orbits, stabilizers, and invariants;
- representation, factorization, and bridges.

## Provisional conceptual moves

Retain eight moves provisionally because current examples distinguish them behaviorally:

- **transfer** — port a mechanism to another realization;
- **decompose** — split a problem/object into structurally meaningful parts;
- **synthesize** — combine separately understood constructions/viewpoints;
- **abstract/compress** — remove accidental presentation and identify a smaller common mechanism;
- **reframe/bridge** — change representation or introduce an intermediate translator;
- **generalize/weaken** — broaden a statement or remove assumptions according to the mechanism;
- **stress-test** — perturb/falsify a mechanism to identify its first obstruction;
- **select** — choose among valid viewpoints by expected downstream usefulness.

Do not treat simplification, multiple perspectives, naturalness/canonicality, prediction, bridge construction, or fertility as independent v2 moves. They are respectively outcomes/criteria, repeated reframing, selection criteria, consequences, a subtype of reframing, and an evaluation signal.

## Intuition unit

One intuition is one compact strategic proposal: a mechanism, representation, intermediate object, small number of useful subgoals, relevant assumption, or obstruction.

The generator receives a name-free generic theorem presentation and the minimum structural background needed to understand it. It does not receive theorem/declaration name, source proof, neighboring lemmas/comments, documented/reference intuition, qwen-lean output, or private formal metadata.

The semantic request is:

> Propose one compact mathematical strategy for why the result should hold and how a proof might be organized. Identify the main mechanism or representation and a small number of useful intermediate goals if needed. Mention an obstruction or essential assumption only if it materially guides the route. Do not write the proof.

Disallow Lean code, tactic names, library identifiers, line-by-line derivations, and near-complete informal proofs.

## Leakage classification

Before qwen-lean outcomes exist, classify each generated intuition as:

- `strategic` — substantial proof work remains;
- `borderline` — too much local derivation for clean causal interpretation;
- `proof_like` — effectively supplies the proof/implementation route.

Only `strategic` samples enter primary fertility scoring. Do not rewrite leaky outputs after observing formal-worker results.

## Target-selection policy

### Formal-worker exposure rule

Primary targets must be Phase-2 `heldout` for the qwen-lean Phase-5 lineage. Validation targets are unnecessary for v2 and should not be used while enough heldout material exists. Train targets are excluded because Phase 5 fits all eligible train records.

The observed audit is recorded in `INTUITION_FERTILITY_TARGET_EXPOSURE_V0.md`.

### Original panel disposition

- `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` is `CLEAN_HELDOUT` and may remain as a **channel calibration** target.
- Lagrange/subgroup-cardinality, rank-nullity, Schröder-Bernstein, Hall, and compact-image targets are Phase-5 train-exposed and are retired from primary fertility scoring.
- Their conceptual analyses remain useful examples for scoping concepts/moves; they are not deleted from provenance.

### Replacement selection must precede model outcomes

Select replacement targets from the full Phase-2 heldout corpus using only source/theorem/proof metadata and mathematical inspection. Do not use base/adaptor/Codex proof-generation success, pass@k, logits, or qwen-lean outputs to choose them.

A heldout candidate should normally satisfy:

- exact retained record/source identity and reconstructable Lean verification;
- qwen-lean whole-proof prompt fits the frozen inference context/budget;
- not an obvious one-line wrapper around an immediately preceding theorem;
- enough proof-bearing structure that a strategy could plausibly change generation;
- compact enough statement that a name-free mathematical presentation is faithful;
- no dependence on concrete arithmetic execution for Mathia's conceptual input;
- useful conceptual mechanism that can be described without giving most of the proof;
- panel-level diversity across domains/moves.

Proof length is a diagnostic proxy, not a truth criterion. Prefer a spread of moderate and harder completion lengths rather than selecting purely by token count.

### Desired panel shape

Keep the panel small. A reasonable target is roughly six primary theorems plus the orbit-stabilizer calibration item, but exact cardinality may change during audit.

Seek diversity such as:

- representation/quotient/information mechanism;
- decomposition plus later synthesis;
- symmetry/invariance/action;
- transfer/preservation in topology/analysis or another non-algebraic domain;
- a combinatorial or order-theoretic construction;
- at least one proof-bearing target where the key move is not a standard wrapper lemma.

Do not force one item per label if the heldout corpus does not support a clean example.

## Formal worker

The primary #32 formal worker should be the **validation-selected Phase-5 qwen-lean adapter after Phase 5 completes**. Do not adopt the physical midpoint checkpoint at step 4981 or switch to the Phase-4 adapter merely to preserve an old theorem panel.

Phase 4 remains a fully validated fallback/provenance reference, but choosing it would change the intended experimental question because Phase 5 is the actual future formal specialist being developed.

At #32 freeze, record exact Phase-5 adapter checkpoint, training artifact hash, source revision, tokenizer, Lean/mathlib environment, prompt format, generation settings, and verifier.

## Formal-worker semantics

Current qwen-lean generates a full Lean continuation after `by`; Lean verifies the raw reconstructed proof. V2 therefore measures **verified whole-proof generation fertility**, not tactic-level proof-search complexity.

Primary outcomes per theorem/condition under a frozen candidate budget:

- Lean-verified candidate count/rate;
- pass@k / at least one verified proof;
- matched uplift versus control conditions.

Candidate rank, tokens-to-first-verified candidate, and runtime are secondary sampling-cost proxies only.

## Guidance intervention

For theorem `T`, freeze guidance `I` before its guided qwen-lean outcomes. Guided prompt differs from baseline only by a bounded natural-language Lean comment placed before the exact declaration/proof continuation.

Conceptually:

```text
/- existing whole-proof instruction -/
/- Strategic hint: <frozen I> -/
<exact declaration> := by
  <generated continuation>
```

Theorem declaration, formal-worker checkpoint, tokenizer, candidate budget, sampling, verifier, and every non-intervention prompt byte remain matched and inspectable.

## Required controls

- `no_guidance` — current whole-proof request;
- `factual_control` — theorem-specific, strategy-free restatement of facts already in the declaration;
- `generic_strategy_control` — theorem-independent structural reasoning advice in the same comment channel;
- `cross_theorem_strategy` — frozen strategy from another conceptually adjacent target;
- `qwen_base_intuition` — exact common base under the same intuition task;
- `codex_reference_intuition` — recorded frontier reference under the same bounded task;
- future `mathia_intuition` without changing the protocol.

Cross-theorem guidance may genuinely help through transfer. Preserve that result rather than defining the control to require failure.

## Channel-validity gate

A positive channel signal requires some non-ceiling heldout targets where relevant strategic guidance increases verified proof yield beyond unguided, factual, and generic-strategy controls without becoming proof-like.

There must also be learnable headroom: Qwen-base guidance is weaker/inconsistent relative to the frontier reference, or different strategic samples have materially different downstream yields.

Return to design rather than train Mathia if strong reference guidance does not change non-ceiling yield, generic/factual controls reproduce the effect, only proof-like hints help, all targets are ceiling/floor, or the result is dominated by comment serialization/prompt artifacts.

Formal-worker failure never means the theorem or intuition is mathematically false.

## Remaining #30 gates

### Gate A — heldout replacement shortlist

From the actual qwen-lean Phase-2 `heldout.jsonl`, produce a metadata/source-based shortlist of candidate replacement theorems **without running qwen-lean inference on them**. Preserve declaration, record id, component, file, statement, completion length, relevant source/doc context, and a private conceptual-scoping note.

### Gate B — Mathia panel selection

Inspect the shortlist mathematically and choose the smallest diverse primary panel. For each retained target freeze:

- private formal identity;
- exact name-free Mathia-visible statement;
- factual control;
- audit-only reference strategy;
- leakage risk;
- genericity/notation variant;
- cross-theorem pairing;
- human-readable documentation where available.

### Gate C — fresh-context adversarial review

Attack concept/dimension redundancy, exposition-vs-strategy behavior, statement leakage, proof-like hints, weak controls, generic-strategy priming, comment/OOD effects, cross-control triviality, target exposure, whole-proof-vs-search semantics, teacher similarity as pseudo-truth, solver-specific prompt hacking, theorem-name/arithmetic shortcuts, genericity fragility, and inability to falsify the hypothesis.

Iterate fix/re-review until `PASS`, genuinely non-material `PASS_WITH_NOTES`, or `BLOCKED`.

## Exit condition

#30 closes only when the heldout panel is fully selected/frozen and a fresh independent review passes. #31 then implements mechanics; it must not invent target replacements, scientific controls, or reward semantics.