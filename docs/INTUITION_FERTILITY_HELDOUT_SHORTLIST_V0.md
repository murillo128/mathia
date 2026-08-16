# Heldout replacement shortlist v0

## Status

This file records the CPU-only qwen-lean Phase-2 `heldout` shortlist used to choose `INTUITION_FERTILITY_PANEL_V1.md` under issue #30.

The shortlist was produced from the actual local `artifacts/phase2/mathlib-whole-proof-v1/heldout.jsonl`. All twenty records were reported as:

- split exactly `heldout` from the retained record;
- compatible with `whole-proof-v1` under `prompt_tokens + 1024 <= 2048`;
- source-span/identity matched against pinned mathlib `81a5d257c8e410db227a6665ed08f64fea08e997`;
- reconstructable with the retained original proof and Lean-accepted on CPU;
- not classified `wrapper_like`;
- selected without model inference, training, GPU work, pass@k, logits, or qwen-lean output.

Private proof/mechanism inspection was used only for scoping and must not enter Mathia-visible intuition prompts.

## Shortlist

| # | Declaration | Record id | Proof class | Prompt | Completion | SFT | Premises | Panel disposition |
|---|---|---|---|---:|---:|---:|---:|---|
| 1 | `Module.Relations.Solution.injective_fromQuotient_iff_ker_π_eq_span` | `5f02e6d28ac50ffa77d1d5ca5415705e9a3e07a40e2d365caeeda8cb369b77a6` | moderate | 77 | 171 | 249 | 15 | reserve |
| 2 | `existsUnique_zpow_near_of_one_lt` | `fd1395846bac45a375977bb3fa30edc065764be9433d362199ca032f4aced011` | proof_bearing | 84 | 278 | 363 | 13 | reserve |
| 3 | `Real.cauSeq_converges` | `f056617deb5f1254d186c5e77b2f8e58bf38f273dc5f5a32897c0d83a715746a` | proof_bearing | 58 | 320 | 379 | 26 | reserve |
| 4 | `Polynomial.exists_prod_multiset_X_sub_C_mul` | `c840cc8cf06a0e64b3803f6ef5ee384fd8a24f0c0bb70283741a8243d5ffcc68` | moderate | 97 | 162 | 260 | 16 | reserve |
| 5 | `AnalyticOnNhd.eqOn_zero_of_preconnected_of_eventuallyEq_zero_aux` | `b02d73078afb5b4319abc67810e0ae8efa2ce6960dea2d4a8445f6f422d9437b` | proof_bearing | 127 | 516 | 644 | 29 | **primary A** |
| 6 | `BoundedContinuousFunction.exists_norm_eq_restrict_eq` | `9c2381292e460692b44651eea9729b2338d1cb154014dfd72e60c9a311565093` | moderate | 72 | 271 | 344 | 12 | reserve |
| 7 | `ConvexOn.lipschitzOnWith_of_abs_le` | `4bd707ce5cd1ecd6257b2edf58494c4f455873215cecc095295b6bd59fbcc796` | proof_bearing | 117 | 706 | 824 | 30 | reserve |
| 8 | `Orthonormal.sum_inner_products_le` | `7874dae5a8c057a91ccd79dce0a38417ef5bcb575bbf72c7f88f884f0232b6f8` | proof_bearing | 86 | 309 | 396 | 20 | reserve |
| 9 | `LinearMap.image_closure_of_convex` | `76b8e72a11688578bf481d822e385cfabb71cda74ee8b1f3a4ec5a5051e59e5c` | moderate | 103 | 192 | 296 | 13 | reserve |
| 10 | `MulAction.Subgroup.normalCore_eq_ker` | `02bf0d2b51d7f716816d5777bc3a252d1a85fe4a95d15d3333d54279d2a4086e` | moderate | 57 | 178 | 236 | 12 | reserve |
| 11 | `Module.End.disjoint_genEigenspace` | `9db61d80db52314e83addee2d556253ee17ad710d1a597725a0a6390d2009073` | proof_bearing | 111 | 581 | 693 | 26 | **primary B** |
| 12 | `linearIndependent_sum` | `5751f369a1e80a5ebcf31574d28dd7a3b9b20c65d841fce0294f780562bd73e6` | proof_bearing | 118 | 462 | 581 | 29 | **primary C** |
| 13 | `BinaryTree.treesOfNumNodesEq_card_eq_catalan` | `d2788186eb3eaedb9ceb3be6019b369503c6ad06d7d5ed8ac98f9d679b846dbd` | moderate | 60 | 108 | 169 | 15 | reserve |
| 14 | `Finset.Colex.UV.erdos_ko_rado` | `74125800af541845d93880105ff8c85960a2ee725992406d5de98bdeca6341f1` | proof_bearing | 126 | 613 | 740 | 36 | reserve |
| 15 | `SimpleGraph.Finsubgraph.nonempty_hom_of_forall_finite_subgraph_hom` | `9a0191efa6271a14b1aa05a9b3d422d207d1193899daf8ef955cbe9a2e0440ae` | proof_bearing | 81 | 408 | 490 | 19 | **primary D** |
| 16 | `Relation.ReflGen.SymmGen.ReflTransGen.TransGen.EqvGen.church_rosser` | `92d6b286e0d3754888b472b5b8b3f488715970a8f1dca537c3f5bb10ed9934cc` | proof_bearing | 106 | 246 | 353 | 7 | **primary E** |
| 17 | `MeasureTheory.MeasurableSet.eq_preimage_restrict_countable` | `7ee0d231a646406fb0e6adea92cbca454ed339175fcd0d2c83bda918064cc795` | proof_bearing | 101 | 350 | 452 | 14 | **primary F** |
| 18 | `MeasureTheory.Measure.exists_sum_smul_dirac` | `5afeb91e34346dd9dd684eb7c1b11962cf64a4c4ea2a7e90ec791eb86afd97bf` | proof_bearing | 84 | 469 | 554 | 34 | reserve |
| 19 | `continuousSMul_iff_stabilizer_isOpen` | `e6d45e4263fd3966cb42188bc9b7169864d579b74b1b8109b788a34d91a8158a` | moderate | 74 | 183 | 258 | 10 | reserve |
| 20 | `Quiver.Path.exists_notMem_mem_hom_path_path_of_notMem_mem` | `c4c7b685776ae906b4c7b2679e76d696a508036f009b7439155cc7951a7b10b2` | moderate | 137 | 248 | 386 | 10 | reserve |

`SFT` is the reported complete `mathlib-sft-v1` serialized token length including EOS; `completion` excludes EOS.

## Selection rationale

The primary six are not the six longest proofs and are not selected by fame. They were chosen to make the causal channel hard to fake with one generic heuristic while preserving proof-bearing formal work:

- **A analytic identity:** local analytic information propagated through a preconnected region;
- **B generalized eigenspaces:** separation by incompatibility of two generalized spectral behaviors;
- **C linear independence over a disjoint sum:** decomposition of a global relation plus synthesis/separation across spans;
- **D finite graph consistency:** finite satisfiability/coherence producing a global homomorphism;
- **E Church–Rosser:** promotion of a direct-fork property to arbitrary finite reduction paths;
- **F countable coordinate dependence:** closure of a support property under measurable-set generation.

This gives three intentionally adjacent cross-control pairs:

- A ↔ E: local-to-global propagation;
- B ↔ C: linear-algebraic separation/decomposition;
- D ↔ F: global structure from restricted information.

The pairing deliberately allows real transfer. A cross-theorem hint that helps is an interpretable result, not an invalid control.

## Reserve logic

Important reserves remain available if independent review rejects a primary item:

- `Real.cauSeq_converges` for completeness/order representation;
- `BoundedContinuousFunction.exists_norm_eq_restrict_eq` for extension/construction;
- `Orthonormal.sum_inner_products_le` for orthogonal decomposition;
- `Finset.Colex.UV.erdos_ko_rado` for extremal combinatorial compression;
- `MeasureTheory.Measure.exists_sum_smul_dirac` for atomic decomposition;
- `continuousSMul_iff_stabilizer_isOpen` for symmetry/topology transfer.

Replacement after review must still occur before any protected qwen-lean comparative inference on the candidate. Do not substitute items after seeing model outcomes.
