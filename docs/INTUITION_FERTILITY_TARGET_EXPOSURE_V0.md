# Intuition-fertility target exposure audit v0

## Status

This document records the CPU-only qwen-lean Phase-2 lookup required by Mathia issue #30. It is observed evidence supplied from the qwen-lean project context, not a hypothesis.

The lookup used the actual local `artifacts/phase2/mathlib-whole-proof-v1` JSONL artifacts rather than inferring split membership from source paths. The intended downstream formal worker is the future validation-selected Phase-5 adapter, so any exact target proof present in Phase-5 optimizer training is excluded from the primary intuition-fertility panel.

## Result

Five of the six original candidate targets are in Phase-2 `train`, are eligible under the Phase-5 `mathlib-sft-v1 <= 1024` rule, and are present in `phase5-train-full-v1`. They are therefore excluded for the Phase-5 fertility experiment.

| Original candidate | Phase-2 split | serialized tokens | Phase-5 optimizer exposure | Mathia status |
|---|---|---:|---|---|
| `Subgroup.card_subgroup_dvd_card` | train | 78 | yes | `EXCLUDE` |
| `LinearMap.rank_range_add_rank_ker` | train | 123 | yes | `EXCLUDE` |
| `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` | heldout | 131 | no | `CLEAN_HELDOUT` |
| `Function.Embedding.schroeder_bernstein_of_rel` | train | 713 | yes | `EXCLUDE` |
| `HallMarriageTheorem.hall_hard_inductive` | train | 396 | yes | `EXCLUDE` |
| `IsCompact.image_of_continuousOn` | train | 257 | yes | `EXCLUDE` |

There are no `validation` targets in the original panel, so no `MODEL_SELECTION_EXPOSURE` case occurs.

## Exact record evidence

### Lagrange / subgroup cardinality

- requested mathematical target: `Subgroup.card_subgroup_dvd_card`
- stored Phase-2 `declaration_name`: `QuotientGroup.Subgroup.card_subgroup_dvd_card`
- record id: `781e6f6a1d651774fd2cdd150bbb65d7f53a4b4f3ab403b1d1065f215f785161`
- component id: `07f9ac4ffc3e837a117b0301eb4b6c61f0b5646ea0726a78c0718cab062b2ce9`
- file: `Mathlib/GroupTheory/Coset/Card.lean`
- split: `train`
- serialized length: 78 tokens
- Phase-5 training: included

The qwen-lean lookup found a metadata bug: the stored fully qualified declaration name is invalid, while the retained source span/proof corresponds to the real `Subgroup.card_subgroup_dvd_card`. This must not be misclassified as a missing target; its proof is demonstrably train-exposed.

### Rank-nullity

- declaration: `LinearMap.rank_range_add_rank_ker`
- record id: `7cf74a2646795b4334e50b8fb3c3271e532bb20ce978e58d3ef2397cd8cb60fe`
- component id: `84c326f780eeb1d73284b19600a4223635174998db0267d42fb350dd4afdf56e`
- file: `Mathlib/LinearAlgebra/Dimension/RankNullity.lean`
- split: `train`
- serialized length: 123 tokens
- Phase-5 training: included

### Orbit-stabilizer

- declaration: `MulAction.card_orbit_mul_card_stabilizer_eq_card_group`
- record id: `60b1a7986f6f4b88449378e1d397c3e717b2e9d2e29d21efe11d73ff443a7c41`
- component id: `391447f14bcfa2bacddd4f60d14bfd52e25ff7431644ff799cbd02899d11d9f9`
- file: `Mathlib/GroupTheory/GroupAction/Quotient.lean`
- split: `heldout`
- serialized length: 131 tokens
- Phase-5 optimizer exposure: none
- status: `CLEAN_HELDOUT`

This target remains useful mainly as channel calibration: the underlying mathlib proof is short/wrapper-like, so it may have a high ceiling and should not carry the main claim about strategic fertility.

### Schröder-Bernstein

- declaration: `Function.Embedding.schroeder_bernstein_of_rel`
- record id: `1b16456979f0207b2842c1f6296dcb40a188bc50492a48b48a1ae685ec83acec`
- component id: `34643c1b2eb945e6ff2aaa826afb99305ce242c9962b438ee0c64aed220d325b`
- file: `Mathlib/SetTheory/Cardinal/SchroederBernstein.lean`
- split: `train`
- serialized length: 713 tokens
- Phase-5 training: included

### Hall matching

- declaration: `HallMarriageTheorem.hall_hard_inductive`
- record id: `f64d67128b047cece377c92520837311695d16d4fdb07d49c33476a536a4d184`
- component id: `69b82bdf9b52b8196e7c626b148fa42ba9e0831a62208e3284e37d69d5c1d6b6`
- file: `Mathlib/Combinatorics/Hall/Finite.lean`
- split: `train`
- serialized length: 396 tokens
- Phase-5 training: included

### Continuous image of compact set

- declaration: `IsCompact.image_of_continuousOn`
- record id: `cdb6799427790bf41b3a0ffbb8b6a5cc94d1eaff5818b4b945baed8b1b3059c8`
- component id: `90b2986e394f1189ccbd7f193e7f0a45621aed5f374a4ee7a70087cadd8a5aef`
- file: `Mathlib/Topology/Compactness/Compact.lean`
- split: `train`
- serialized length: 257 tokens
- Phase-5 training: included

## qwen-lean checkpoint state at lookup

Phase 5 was not complete at the time of this audit:

- state: `stopped_at_mandatory_resume_boundary`
- optimizer step: 4981 / 9962
- examples consumed: 39,848 / 79,696
- Q1 and Q2 exist; Q3/Q4 absent
- `checkpoint_selection: null`
- no selected Phase-5 adapter yet

A physical checkpoint exists at `artifacts/phase5/training/trainer-state/checkpoint-4981` with validation CE about `1.1711516944`, but it is not a contract-selected/fully validated adapter and must not be adopted merely to make the Mathia experiment runnable sooner.

The most recent fully selected and validated formal-worker checkpoint is Phase 4:

- adapter id: `phase4-train4096-v1-lora`
- PEFT LoRA, unmerged, rank 16
- selected optimizer step: 512
- selected validation CE: about `1.4309009798` versus step-0 `1.8658065785`
- training artifact SHA-256: `039492178af14c0a6188165ea60f1e8b554cea257179e79709eaf94fb90290b8`
- local adapter weights SHA-256: `3d92d8bbca246da6adc21e53d9fb9403e4b9a00649c53f7f0d2f093e638da05f`
- reviewed source head: `49c8c2f5db3ca249d149e7b32fa4634096a5739f`
- merged via qwen-lean PR #18
- independent verdict: `PASS_WITH_NOTES`, no material findings

None of the six original Mathia targets was in the Phase-4 selected train/validation/heldout workloads. Nevertheless, Mathia v0 should not switch to the Phase-4 worker simply to preserve the old panel. The intended primary experiment should use the selected Phase-5 worker after Phase 5 completes and should therefore rebuild its target panel from Phase-2 heldout.

## Design consequence

The original six-target panel is scientifically superseded as a primary Phase-5 panel:

- retain orbit-stabilizer as a clean channel-calibration item;
- retire the other five from primary fertility scoring;
- retain their conceptual analyses as examples for concept/dimension scoping only;
- choose replacement primary targets from the actual Phase-2 `heldout` split before inspecting qwen-lean model outputs on them;
- select replacements using theorem/proof/source metadata and conceptual diversity, never qwen-lean success/failure.

This preserves the causal question: the formal worker may know the surrounding mathematical library and general proof patterns, but it has not been optimized directly on the exact target proof.