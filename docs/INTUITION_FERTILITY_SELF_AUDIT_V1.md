# Intuition-fertility exact-panel self-audit v1

## Status

Non-independent pre-review of `INTUITION_FERTILITY_PRETEST_V2.md` + `INTUITION_FERTILITY_PANEL_V1.md` after the heldout replacement shortlist was resolved. This is not the required fresh-context review.

Verdict: **PASS_TO_INDEPENDENT_REVIEW**. No known material design defect remains from the current-context audit, but the independent reviewer must still be allowed to return `REVISE` or `BLOCKED`.

## Checks and findings

### Target exposure

PASS. Six primary targets and the calibration target are Phase-2 heldout. The retired five original primary targets were actually present in Phase-5 optimizer training and remain excluded.

### Formal-worker semantics

PASS. The contract consistently measures verified whole-proof generation yield, not tactic-level search. Candidate rank/tokens are secondary sampling-cost proxies only.

### Target selection leakage

PASS. The twenty-target shortlist was created without Qwen/qwen-lean inference. Primary selection used source/proof metadata and private mathematical inspection only.

### Concrete arithmetic boundary

PASS WITH NOTE. Primary Mathia-visible statements do not use concrete numerical instances as evidence or require arithmetic execution. Structural notions such as finite, countable, depth, zero function, or finite path remain mathematical roles rather than instance calculations. The retired/rejected quantitative shortlist candidates were not needed for v1.

### Statement fidelity

PASS WITH NOTE. The natural-language statements preserve the mathematical proposition at the intended semantic level. The analytic target still summarizes the ambient normed analytic setting rather than spelling every Lean typeclass assumption. This is intentional to avoid testing Lean/typeclass literacy; independent review should verify that no material hypothesis has been omitted or strengthened.

### Statement-to-strategy leakage

PASS WITH NOTE. Some targets necessarily reveal structural vocabulary because it is part of the theorem: generalized eigenspaces, disjoint spans, finite subgraphs, finite reduction paths, and product coordinates. The prompts do not state the audit-only mechanism that turns these ingredients into a proof. Primary C is the closest case: the theorem itself already names span disjointness. It should be interpreted as testing organization of a proof rather than discovery of the condition.

### Proof leakage policy

PASS. Audit references stop at mechanism/subgoal level. They deliberately do not name exact mathlib lemmas, Lean tactics, or full source derivations. Generated samples are classified before their formal-worker outcomes and leaky samples are not sanitized.

### Factual control

PASS. Each factual control restates theorem facts/conclusion without introducing an extra representation, construction, or proof route. Exact token equality is not claimed; final generation budget and prompt bytes freeze in #32.

### Generic strategy control

PASS WITH NOTE. The original wording was too aligned with quotient/reversibility concepts and was narrowed. The current control mentions only broad representation/decomposition/invariant/intermediate-object advice. It may still help some theorems; that is precisely the confound it is designed to measure.

### Cross-theorem strategy control

PASS WITH NOTE. Pairings are intentionally adjacent:

- analytic identity ↔ confluence: local-to-global;
- generalized eigenspaces ↔ disjoint-sum independence: linear-algebraic separation;
- finite graph consistency ↔ countable coordinate dependence: global structure from restricted information.

This makes the control hard rather than irrelevant by vocabulary. A cross hint may legitimately help. If cross guidance performs as well as relevant guidance, the experiment supports transfer/general abstraction more than theorem-specific strategy and should be interpreted that way.

### Genericity variants

PASS. Each primary item now has exact alternate model-visible text rather than an instruction for #31 to invent a paraphrase. Variants rename symbols or re-express the same structure without changing the private formal target.

### Calibration target

PASS. Orbit–stabilizer has an exact Mathia-visible statement, factual control, audit reference, leakage boundary, and variant. It remains explicitly excluded from primary substantive evidence because its proof is short/wrapper-like.

### Panel diversity

PASS. The six primaries cover analytic continuation, generalized spectral separation, linear-independence decomposition, graph compactness/coherence, relational confluence, and measurable-coordinate support. No single candidate concept such as quotienting or induction plausibly explains the full panel.

### Falsifiability

PASS. Material negative outcomes are possible and pre-specified: no strong-reference uplift, generic/factual controls matching relevant guidance, proof-like hints being required, all cells ceiling/floor, comment serialization effects, or no base/reference headroom.

## Independent-review focus

The independent reviewer should especially attack:

1. whether Primary A's ambient analytic assumptions are faithfully represented;
2. whether Primary C is too self-revealing to be informative;
3. whether A/E, B/C, or D/F are too close for a useful cross-control interpretation;
4. whether the generic strategy control is too strong/weak or uneven across domains;
5. whether a natural-language hint injected as a Lean comment creates an OOD/prompt effect not controlled by factual/generic comments;
6. whether all proof-bearing items may be too difficult for the eventual Phase-5 worker, making the calibration item insufficient to diagnose a floor;
7. whether any selected theorem should be replaced by one of the pre-registered heldout reserves before model outcomes exist.
