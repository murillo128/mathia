# Intuition-fertility target identity audit v1

## Status

Current canonical-identity audit for Mathia issue #30 after the independent review of `818793ba4ec2d7d0a7db718c0c8deacf366ea83b` returned `REVISE`.

This document fixes a distinction that v1 blurred:

- **canonical Lean declaration** means the declaration name resolved from pinned mathlib source `81a5d257c8e410db227a6665ed08f64fea08e997`;
- **reported artifact/shortlist name** is the name previously recorded from the Phase-2 heldout scoping evidence;
- **record identity/split** is the observed CPU-only Phase-2 evidence already frozen before any protected qwen-lean inference.

The full Phase-2 JSONL remains outside Git, so this audit does not pretend to re-read unavailable artifact bytes. It re-verifies canonical source names against pinned mathlib and explicitly composes them with the already observed record IDs, source files, and heldout status. If the local artifact is re-opened later, its raw `declaration_name` must be preserved separately rather than silently substituted for the canonical source name.

No model inference, GPU work, pass@k, logits, generated proofs, or target replacement was used.

## Seven-target mapping

| Id | Canonical Lean declaration | Previously reported artifact/shortlist name | Record id | Pinned source | Observed Phase-2 status | Identity note |
|---|---|---|---|---|---|---|
| A | `AnalyticOnNhd.eqOn_zero_of_preconnected_of_eventuallyEq_zero_aux` | same | `b02d73078afb5b4319abc67810e0ae8efa2ce6960dea2d4a8445f6f422d9437b` | `Mathlib/Analysis/Analytic/Uniqueness.lean` | `heldout` | canonical name verified |
| B | `Module.End.disjoint_genEigenspace` | same | `9db61d80db52314e83addee2d556253ee17ad710d1a597725a0a6390d2009073` | `Mathlib/LinearAlgebra/Eigenspace/Basic.lean` | `heldout` | canonical name verified |
| C | `linearIndependent_sum` | same | `5751f369a1e80a5ebcf31574d28dd7a3b9b20c65d841fce0294f780562bd73e6` | `Mathlib/LinearAlgebra/LinearIndependent/Basic.lean` | `heldout` | canonical name verified |
| D | `SimpleGraph.nonempty_hom_of_forall_finite_subgraph_hom` | `SimpleGraph.Finsubgraph.nonempty_hom_of_forall_finite_subgraph_hom` | `9a0191efa6271a14b1aa05a9b3d422d207d1193899daf8ef955cbe9a2e0440ae` | `Mathlib/Combinatorics/SimpleGraph/Finsubgraph.lean` | `heldout` | **reported-name defect**: source closes `namespace Finsubgraph` before the theorem |
| E | `Relation.church_rosser` | `Relation.ReflGen.SymmGen.ReflTransGen.TransGen.EqvGen.church_rosser` | `92d6b286e0d3754888b472b5b8b3f488715970a8f1dca537c3f5bb10ed9934cc` | `Mathlib/Logic/Relation.lean` | `heldout` | **reported-name defect**: closure namespaces are closed before `church_rosser`; source references `Relation.church_rosser` |
| F | `MeasureTheory.MeasurableSet.eq_preimage_restrict_countable` | same | `7ee0d231a646406fb0e6adea92cbca454ed339175fcd0d2c83bda918064cc795` | `Mathlib/MeasureTheory/Constructions/Cylinders.lean` | `heldout` | canonical name verified |
| G | `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` | same | `60b1a7986f6f4b88449378e1d397c3e717b2e9d2e29d21efe11d73ff443a7c41` | `Mathlib/GroupTheory/GroupAction/Quotient.lean` | `CLEAN_HELDOUT` | calibration only; canonical name verified |

## Interpretation of D/E

The D/E defects are naming defects in the reviewed Mathia documents, not evidence that a different theorem was selected. The pre-existing CPU shortlist reported for each record:

- exact `heldout` split from the retained row;
- pinned source-span/identity matching;
- retained-proof reconstruction and Lean acceptance;
- whole-proof budget compatibility;
- no qwen-lean inference during selection.

Therefore the corrected contract binds D/E by **record id + pinned source + canonical source declaration**, while retaining the old long names only as provenance of the reviewed artifact. Future code must not use the invalid long names as canonical Lean identifiers.

## Remaining contamination boundary

This audit closes the known canonical-name ambiguity. It does not claim that lexical source identity detects every possible semantically equivalent theorem elsewhere in mathlib or base-model pretraining. The Phase-2 split evidence remains the relevant formal-worker post-training guard; Qwen-base pretraining familiarity remains a reported limitation rather than a hidden exclusion criterion.
