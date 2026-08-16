# Intuition-fertility pre-test v2

## Status

**Current #30 contract.** The formal-worker exposure gate and heldout replacement selection are complete. The exact six-primary-plus-calibration panel is frozen in `INTUITION_FERTILITY_PANEL_V1.md` pending only fresh-context independent adversarial review and any fixes that review requires.

V0/v1, the original panel, and the self-audit remain provenance. The scientific question is unchanged:

> Can compact strategic mathematical guidance causally increase the yield of Lean-verified whole proofs from a separate formal specialist, and does the exact Qwen base leave useful headroom relative to a strong frontier reference?

No Mathia post-training is authorized by this document.

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

#30 validates the conceptual objects and the proposed measurement channel only.

## Provisional concept families

Use these as experimental scaffolding, not a permanent ontology:

- maps, composition, and information flow;
- reversibility and inverse structure;
- equivalence, fibers/kernels, and quotients;
- decomposition, products, and partitions;
- symmetry, actions, orbits, stabilizers, and invariants;
- representation, factorization, and bridges.

## Provisional conceptual moves

Retain eight moves provisionally because the current examples separate them behaviorally:

- **transfer** — port a mechanism to another realization;
- **decompose** — split a problem/object into structurally meaningful parts;
- **synthesize** — combine separately understood constructions/viewpoints;
- **abstract/compress** — remove accidental presentation and identify a smaller common mechanism;
- **reframe/bridge** — change representation or introduce an intermediate translator;
- **generalize/weaken** — broaden a statement or remove assumptions according to the mechanism;
- **stress-test** — perturb/falsify a mechanism to identify its first obstruction;
- **select** — choose among valid viewpoints by expected downstream usefulness.

Do not treat simplification, multiple perspectives, naturalness/canonicality, prediction, bridge construction, or fertility as independent v2 moves. They are respectively outcomes/criteria, repeated reframing, selection criteria, consequences, a subtype of reframing, and an evaluation signal.

These names may change after training/evaluation evidence.

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

## Formal-worker exposure evidence

The original six candidate targets were resolved against the actual local qwen-lean Phase-2 artifact.

Five are in Phase-5 optimizer training and are excluded from primary fertility scoring:

- `Subgroup.card_subgroup_dvd_card`;
- `LinearMap.rank_range_add_rank_ker`;
- `Function.Embedding.schroeder_bernstein_of_rel`;
- `HallMarriageTheorem.hall_hard_inductive`;
- `IsCompact.image_of_continuousOn`.

`MulAction.card_orbit_mul_card_stabilizer_eq_card_group` is `CLEAN_HELDOUT`, but its retained proof is short/wrapper-like. It survives only as a channel calibration item.

Observed record IDs, splits, components, token lengths, the Lagrange metadata-name defect, and qwen-lean checkpoint evidence are preserved in `INTUITION_FERTILITY_TARGET_EXPOSURE_V0.md`.

Base-model pretraining familiarity is allowed for this calibration and reported as a limitation. Direct qwen-lean post-training proof exposure is an exclusion because it can saturate the proposed reward instrument.

## Heldout replacement selection

Replacement candidates were selected from the actual Phase-2 `heldout.jsonl` before any qwen-lean inference on those candidates.

The twenty-candidate CPU-only shortlist and reported validation facts are preserved in `INTUITION_FERTILITY_HELDOUT_SHORTLIST_V0.md`. Selection used retained source/proof metadata and private mathematical inspection, not model performance, pass@k, logits, or generated proofs.

All twenty shortlist records were reported as source-identity valid, reconstructable, Lean-accepted with their retained proof, compatible with the whole-proof context budget, and non-wrapper-like.

## Frozen primary panel

The exact statements, factual controls, audit-only strategies, leakage boundaries, genericity variants, and record identities are in `INTUITION_FERTILITY_PANEL_V1.md`.

Primary targets:

| Id | Private formal target | Main discriminating structure |
|---|---|---|
| A | `AnalyticOnNhd.eqOn_zero_of_preconnected_of_eventuallyEq_zero_aux` | local analytic agreement -> global agreement over preconnected region |
| B | `Module.End.disjoint_genEigenspace` | incompatible generalized spectral behavior for distinct scalars |
| C | `linearIndependent_sum` | split a global linear relation; cross-cancellation controlled by span intersection |
| D | `SimpleGraph.Finsubgraph.nonempty_hom_of_forall_finite_subgraph_hom` | finite satisfiability/coherence -> global graph homomorphism |
| E | `Relation.ReflGen.SymmGen.ReflTransGen.TransGen.EqvGen.church_rosser` | direct-fork joinability -> global finite-path confluence |
| F | `MeasureTheory.MeasurableSet.eq_preimage_restrict_countable` | measurable-set generation preserves countable coordinate support |

All six are Phase-2 heldout and were privately classified `proof_bearing` during CPU scoping.

Calibration target:

- `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` — clean heldout, short/wrapper-like, used only to test whether the natural-language guidance channel can affect an easier formal target.

Primary claims must not be based on calibration success alone.

## Why this panel

The primary set was chosen for mechanism diversity rather than proof length or theorem fame. It creates three intentionally hard cross-controls:

- **A ↔ E:** local-to-global propagation in analysis versus rewriting/confluence;
- **B ↔ C:** two linear-algebraic separation problems with different mechanisms;
- **D ↔ F:** global structure assembled from restricted information via different compactness/closure ideas.

A cross-theorem strategy may genuinely help because the abstraction transfers. Preserve that as evidence rather than redefining the control after seeing outcomes.

Reserves and experimental reasons for non-selection are recorded in the shortlist/panel docs. Any replacement required by independent review must occur before protected qwen-lean comparative inference.

## Formal worker

The intended #32 formal worker is the **validation-selected Phase-5 qwen-lean adapter after Phase 5 completes**.

At the exposure lookup, Phase 5 was stopped at its mandatory midpoint (`step 4981 / 9962`) and had no selected adapter. The physical midpoint checkpoint is not a valid substitute. Phase 4 is fully validated but should not be adopted merely to preserve an old panel.

At #32 freeze, resolve the real completed Phase-5 identity and record exact adapter checkpoint, training artifact hash, source revision, tokenizer, Lean/mathlib environment, prompt format, generation settings, and verifier.

If Phase 5 ultimately fails to produce a valid selected adapter, return to design rather than silently changing formal worker lineage.

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

Guidance is outside the generated continuation. No private source proof, reference lemma list, or audit-only mechanism may enter the formal-worker prompt except through the independently generated frozen intuition itself.

## Required controls

### `no_guidance`

The unchanged whole-proof request.

### `factual_control`

The theorem-specific strategy-free text frozen for each primary item in `INTUITION_FERTILITY_PANEL_V1.md`. It restates only facts already visible in the proposition.

### `generic_strategy_control`

Use the same theorem-independent semantic content for all targets:

> Look for a structural representation that makes the conclusion direct. Check whether a decomposition, invariant, reversible or quotient-like map, or equivalent formulation removes irrelevant detail. Prefer one mechanism and a small number of subgoals; do not write the proof.

This controls generic strategy-shaped priming. #31/#32 may deterministically escape it for Lean comments and normalize the token budget, but must not change its mathematical content after results.

### `cross_theorem_strategy`

Use the exact frozen intuition generated for the paired target:

- A ↔ E;
- B ↔ C;
- D ↔ F.

### `qwen_base_intuition`

Strategic samples from the exact common Qwen base under the same name-free intuition task.

### `codex_reference_intuition`

Strategic samples from the explicitly recorded frontier/Codex configuration under the same bounded task. This is a strong reference/channel probe, not an independent truth oracle.

### future `mathia_intuition`

The same scientific intervention must accept future Mathia checkpoints without redesign.

## Candidate budget

Do not inherit qwen-lean's small heldout candidate count mechanically. This experiment has only a few theorem/condition cells and is trying to estimate intuition-level yield changes.

#32 must freeze a candidate budget large enough to estimate within-theorem differences while remaining bounded by available compute. Choose the budget before comparative outcomes and do not selectively increase it for ambiguous cells.

## Channel-validity gate

A positive channel signal requires some non-ceiling primary targets where relevant strategic guidance increases verified proof yield beyond unguided, factual, and generic-strategy controls without becoming proof-like.

There must also be learnable headroom: Qwen-base guidance is weaker/inconsistent relative to the frontier reference, or different strategic samples have materially different downstream yields.

Return to design rather than train Mathia if:

- strong reference guidance does not change non-ceiling yield;
- factual/generic controls reproduce the effect;
- all strategy-shaped comments help equally;
- only near-proofs help;
- all primary targets are ceiling/floor;
- comment serialization/OOD effects dominate;
- the chosen formal worker cannot exploit natural-language strategic information.

Formal-worker failure never means the theorem or intuition is mathematically false.

## Genericity and representation robustness

Each primary item has at least one small name-free notation/paraphrase variant in `INTUITION_FERTILITY_PANEL_V1.md`.

These variants test dependence on theorem names and incidental symbols. They do not change the private formal target consumed by qwen-lean.

Failure under trivial renaming is evidence against the conceptual task/model; robustness is not by itself proof of understanding.

## Remaining #30 gate: fresh-context independent review

Gate A (exposure) and Gate B (heldout panel selection/freeze) are complete.

A fresh reviewer must now attack at least:

- whether the concept/move distinctions are still redundant;
- whether the task rewards exposition rather than strategic mathematics;
- whether any name-free statement leaks its audit-only strategy;
- whether paraphrases are faithful to the exact formal target;
- whether strategic references are actually near-proofs;
- whether factual controls contain strategy;
- whether the generic strategy control is unfairly aligned with some targets;
- whether A/E, B/C, or D/F cross pairings are so similar that the control is effectively relevant guidance;
- comment/OOD/extra-token artifacts;
- formal-worker training exposure and Phase-5 lineage;
- whole-proof generation being mislabeled as tactic search;
- Codex/reference similarity becoming pseudo-truth;
- solver-specific prompt hacking;
- theorem-name/pretraining/arithmetic shortcuts;
- genericity/notation fragility;
- inability of the protocol to produce evidence against the hypothesis.

Verdict must be one of `PASS`, genuinely non-material `PASS_WITH_NOTES`, `REVISE`, or `BLOCKED`. Material findings require fix and fresh re-review.

## Exit condition

#30 closes only when the exact v2 + panel-v1 target receives independent `PASS` or genuinely non-material `PASS_WITH_NOTES`.

Then #31 may implement deterministic mechanics. #31 must not invent theorem replacements, change the conceptual prompt, redefine leakage, add/remove scientific controls, alter cross pairing, or reinterpret the reward signal.