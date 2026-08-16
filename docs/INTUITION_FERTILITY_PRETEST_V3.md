# Intuition-fertility pre-test v3

## Status

**Current revised scientific contract for Mathia issue #30.** It responds to the fresh-context independent `REVISE` verdict on `INTUITION_FERTILITY_PRETEST_V2.md` + `INTUITION_FERTILITY_PANEL_V1.md` at reviewed head `818793ba4ec2d7d0a7db718c0c8deacf366ea83b`.

The exact revised panel is `INTUITION_FERTILITY_PANEL_V2.md`. Canonical target identities are separated from artifact metadata in `INTUITION_FERTILITY_TARGET_IDENTITY_AUDIT_V1.md`.

V2/PANEL_V1 remain review provenance. No Mathia post-training, qwen-lean inference, GPU run, RL, or #31 implementation is authorized by this revision itself.

The scientific question is deliberately narrower than the original conceptual story:

> Can compact theorem-specific strategic mathematical guidance causally increase the yield of Lean-verified whole proofs from a separate formal specialist beyond factual restatement, generic structural priming, and strategy-shaped but mechanism-distant context; and does the exact Qwen base leave useful headroom relative to a strong frontier reference?

## What #30 does and does not validate

The working training hypothesis remains exploratory:

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

This pre-test validates or rejects the **fertility measurement channel** and the usefulness of the compact-intuition interface. It does **not** establish that the proposed concept families or conceptual moves are a correct, minimal, separable latent ontology.

### Provisional concept-family scaffolding

Retain as descriptive research scaffolding only:

- maps, composition, and information flow;
- reversibility and inverse structure;
- equivalence, fibers/kernels, and quotients;
- decomposition, products, and partitions;
- symmetry, actions, orbits, stabilizers, and invariants;
- representation, factorization, and bridges.

### Provisional conceptual-move scaffolding

Retain as descriptive annotations only:

- `transfer`;
- `decompose`;
- `synthesize`;
- `abstract/compress`;
- `reframe/bridge`;
- `generalize/weaken`;
- `stress-test`;
- `select`.

Current examples make these labels plausible and useful for analysis, but #30 has no behavioral intervention that can show they are distinct capacities. Do not report target coverage or fertility uplift as evidence that the eight labels are behaviorally separated.

## Intuition unit

One intuition is one compact strategic proposal: a mechanism, representation, intermediate object, small number of useful subgoals, relevant assumption, or obstruction.

The generator receives a name-free generic theorem presentation and only the structural background needed to understand it. It does not receive theorem/declaration name, source proof, neighboring lemmas/comments, audit mechanism note, qwen-lean output, or private formal metadata.

Frozen semantic request:

> Propose one compact mathematical strategy for why the result should hold and how a proof might be organized. Identify the main mechanism or representation and a small number of useful intermediate mathematical goals if needed. Mention an obstruction or essential assumption only if it materially guides the route. Do not write the proof.

Disallow Lean code, tactic names, library identifiers, source names, line-by-line derivations, and near-complete informal proofs.

The phrase “why the result should hold” may elicit elegant exposition; that is not itself evidence. The dependent variable remains verified downstream whole-proof yield.

## Leakage firewall

Before qwen-lean outcomes exist, classify each generated candidate under the exact leakage-only rubric frozen in `INTUITION_FERTILITY_PANEL_V2.md`:

- `strategic`;
- `borderline`;
- `proof_like`.

The classifier is blind to generator identity, source/private proof material, audit notes, and formal-worker outcomes. It judges only how much proof/implementation has been transmitted, not whether the intuition is correct, elegant, teacher-like, or likely to succeed. Uncertain/disputed samples default to `borderline`. Only `strategic` enters primary fertility scoring.

This prevents an AI judge from becoming a hidden mathematical truth oracle or a teacher-style selector.

## Target identity and formal-worker exposure

The original five train-exposed candidates remain excluded. The six revised primaries and G calibration retain their previously observed Phase-2 heldout status.

The independent review found canonical-name defects for D/E. `INTUITION_FERTILITY_TARGET_IDENTITY_AUDIT_V1.md` now freezes canonical pinned-mathlib names separately from the previously reported artifact/shortlist strings:

- D canonical: `SimpleGraph.nonempty_hom_of_forall_finite_subgraph_hom`;
- E canonical: `Relation.church_rosser`.

Their record IDs, pinned source files, and pre-outcome heldout evidence remain unchanged. Future code must bind by the corrected canonical identity plus retained record/source provenance and must not treat the invalid long strings as canonical Lean names.

Qwen-base pretraining familiarity remains allowed and reported. Direct qwen-lean SFT/model-selection exposure to an exact target remains an exclusion.

## Revised primary panel

| Id | Canonical private formal target | Main discriminating structure |
|---|---|---|
| A | `AnalyticOnNhd.eqOn_zero_of_preconnected_of_eventuallyEq_zero_aux` | local analytic agreement → global agreement over a preconnected region |
| B | `Module.End.disjoint_genEigenspace` | incompatible generalized spectral behavior for distinct scalars |
| C | `linearIndependent_sum` | split a global relation; cross-cancellation controlled by span intersection |
| D | `SimpleGraph.nonempty_hom_of_forall_finite_subgraph_hom` | finite satisfiability/coherence → global graph homomorphism |
| E | `Relation.church_rosser` | direct-fork joinability → global finite-path confluence |
| F | `MeasureTheory.MeasurableSet.eq_preimage_restrict_countable` | measurable-set generation preserves countable coordinate support |

Calibration G remains `MulAction.card_orbit_mul_card_stabilizer_eq_card_group`, clean heldout but short/wrapper-like.

Primary A now states that `E` and `F` are normed over the same nontrivially normed field and that `F` is complete. Primary B now states explicitly that depths live in `ℕ∞`, including the unbounded case. Exact model-visible wording lives in PANEL_V2.

Primary C remains intentionally usable but is downgraded interpretively: because the theorem statement itself foregrounds span disjointness, it is evidence for **proof-organization fertility**, not strong evidence that the intuition generator discovered a hidden mechanism.

## Formal worker and measured signal

The intended #32 worker remains the validation-selected Phase-5 qwen-lean adapter after Phase 5 completes. Do not substitute the Phase-5 midpoint or Phase 4 merely to make the experiment runnable.

Current qwen-lean generates a full Lean continuation after `by`; Lean verifies the reconstructed proof. Therefore v3 measures **verified whole-proof generation fertility**, not tactic-level proof search.

Primary outcomes per theorem/condition under a frozen candidate budget:

- Lean-verified candidate count/rate;
- pass@k / at least one verified proof;
- matched uplift among the frozen conditions.

Candidate rank, tokens-to-first-verified candidate, and runtime are secondary whole-proof sampling-cost proxies only.

## Guidance intervention and OOD control

Guided qwen-lean differs from baseline only by a bounded natural-language Lean comment before the exact declaration/proof continuation. All non-intervention bytes, theorem, checkpoint, tokenizer, sampling, candidate budget, and verifier remain matched.

A natural-language Lean comment can itself be an OOD/prompting intervention. V3 therefore no longer relies on factual + generic controls alone. It adds a **same-generator distant mismatched strategy** under the same comment wrapper and token envelope.

All generated strategy-bearing guidance has a common maximum of 96 qwen-lean-tokenizer tokens before delimiters. Actual guidance lengths are recorded. Relevant-vs-distant comparisons support a content-specific claim only when their lengths differ by at most 20% of the longer text. No post-generation semantic padding/truncation is allowed.

This does not make token count perfectly causal, but it removes “there was simply a strategy-shaped natural-language comment / much more context” as an uncontrolled free explanation for the main theorem-specific comparison.

## Required conditions

For each primary theorem:

- `no_guidance`;
- theorem-specific `factual_control`;
- theorem-independent `generic_strategy_control`;
- adjacent `cross_theorem_strategy` retained as a **transfer probe**, not a negative control;
- new `distant_mismatched_strategy` as the strategy-shaped negative control;
- `qwen_base_intuition`;
- `codex_reference_intuition`;
- future `mathia_intuition` without redesign.

Exact adjacent and distant donor mappings are frozen in PANEL_V2 before any protected qwen-lean comparative outcome.

## Why two kinds of cross guidance

The original A↔E, B↔C, D↔F pairs are intentionally adjacent in abstraction. They answer:

> Can a useful strategy transfer across theorem/domain boundaries?

They cannot simultaneously function as clean negative controls because genuine transfer is expected to be possible.

The distant mismatched mapping answers a different question:

> Does strategy-shaped text from the same generator help even when its mathematical mechanism was selected to be irrelevant to this target?

Keeping these roles separate lets the experiment distinguish theorem-specific utility from transferable abstraction and from generic/contextual prompting.

## Interpretation matrix

The protocol is designed to separate, where the data permit:

- **specific useful intuition:** relevant strategic guidance > distant mismatch, generic, factual, and no-guidance;
- **transferable abstraction:** relevant and adjacent-cross both > distant mismatch;
- **generic structural priming:** generic ≈ relevant and both > factual/no-guidance;
- **strategy-shaped context/OOD:** distant mismatch ≈ relevant;
- **proof leakage:** only `borderline`/`proof_like` guidance helps;
- **simple token/context effect:** uplift appears only in length-imbalanced cells or tracks guidance length rather than relevance.

No single small panel guarantees identification in every observed pattern. Ambiguous patterns are explicitly non-positive results, not license for post-hoc reinterpretation.

## Candidate budget

Do not inherit qwen-lean's small heldout candidate count mechanically. #32 must freeze a bounded candidate budget large enough to estimate within-theorem yield differences before comparative outcomes, and must not selectively increase it for ambiguous cells.

## Channel-validity gate

A positive theorem-specific channel signal requires at least some non-ceiling primary targets where `strategic` relevant guidance increases verified yield beyond:

- unguided baseline;
- factual control;
- generic strategy control;
- same-generator distant mismatched strategy satisfying the length criterion.

There must also be learnable headroom: Qwen-base guidance is weaker/inconsistent relative to frontier reference, or strategic samples have materially different downstream yields.

Return to design rather than train Mathia if:

- strong reference guidance does not change non-ceiling primary yield;
- factual/generic/distant controls reproduce the relevant effect;
- all strategy-shaped comments help equally;
- only borderline/proof-like hints help;
- only length-imbalanced cells show uplift;
- all primary targets are ceiling/floor;
- Lean-comment serialization/OOD effects dominate;
- the chosen formal worker cannot exploit natural-language strategic information;
- Qwen-base and frontier guidance leave no useful headroom.

If all six proof-bearing primaries are floor while G responds, conclude that the current formal-worker/panel instrument is inadequate or inconclusive; do not infer that mathematical intuition is useless. G success alone never supports the substantive claim.

## Genericity and representation robustness

Each primary and G retains an exact name-free notation/paraphrase variant in PANEL_V2. These test alpha-renaming and incidental presentation dependence only. Failure under trivial renaming is evidence against the task/model; success is not by itself evidence of conceptual understanding or transfer.

## Arithmetic/concrete-instance boundary

No primary Mathia-facing item requires evaluation of concrete numerical instances. “zero”, finite/countable, finite path, depth, and cardinality in G are structural roles, not hidden arithmetic-execution tasks. G is calibration only.

## Falsifiability

V3 preserves clear results that would revise or abandon the current fertility hypothesis/channel:

- strong reference guidance cannot beat controls on any informative primary;
- distant/generic/factual controls explain the uplift;
- only near-proofs help;
- the comment channel rather than mathematical relevance explains yield;
- there is no base/reference headroom;
- the selected worker/panel is uniformly floor/ceiling.

The first five directly damage the proposed intuition-fertility interpretation. Uniform floor/ceiling primarily falsifies the chosen instrument rather than mathematical truth and requires redesign before training.

## Remaining #30 gate

The material findings from the independent `REVISE` have been addressed in this revised contract:

1. D/E canonical identities are corrected and all seven targets are explicitly mapped in the identity audit;
2. adjacent cross guidance is reclassified as a transfer probe, while a distant same-generator strategy negative and length guard are added;
3. leakage classification is operationalized as outcome/model/source-blind proof-transmission screening, not quality/truth judging;
4. concepts/moves are downgraded to unvalidated descriptive scaffolding;
5. A/B model-visible assumptions are made faithful at the semantic level.

A same-context author check cannot substitute for the requested fresh independent gate. Before #31 begins, the exact **PRETEST_V3 + PANEL_V2 + TARGET_IDENTITY_AUDIT_V1** target must receive a fresh independent `PASS` or genuinely non-material `PASS_WITH_NOTES`.
