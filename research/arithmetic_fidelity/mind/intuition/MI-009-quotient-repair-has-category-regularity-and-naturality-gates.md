# MI-009 — Finite exactness, bounded accessibility, morphism category, and original-range assembly are distinct gates

**Evidence level:** supported through AF-104; exact in the stated Banach-space models

## Core intuition

Finite observational reproducibility is cheap unless a uniform budget and an admissible morphism category are fixed. Even after finite costs are calibrated, there are two further questions: whether the second-leg map is accessible in the chosen category, and whether the resulting bidual construction lands in the original target range.

The newest results make the category boundary exact. A map can be reproduced on every finite subsystem, even by genuine preadjoints, while every globally coherent approximation requires norms tending to infinity. Thus finite provenance tests, bounded accessibility, and original-range recovery must not be conflated.

## Strongest justified principle

AF-097--AF-101 show that unbudgeted finite interpolation is universal, a declared norm budget makes finite polar witnesses complete, and bidual accessibility can still be weaker than original-range assembly. The latter distinction is encoded by the exact `alpha` versus `pi` tensor-norm gap.

AF-102 identifies the precise second-leg category. For `C:L^*->K^*`, the canonical bidual lift `C^*J_K:K->L^{**}` has accessibility cost

`beta(C)=a_L(C^*J_K)`.

This is the exact optimal second-leg mapping norm over all sources and is already sharp at the self-source `X=K`. The maps with finite `beta` form the maximal bounded second-leg category for the AF-101 construction; reflexive targets collapse the distinction, while general Banach targets need not.

AF-103 gives the provenance analogue. Genuine preadjoints are strongly dense on every finite-dimensional test family, so finite SOT observations cannot certify whether an operator actually comes from a preadjoint. The exact invariant is the uniform strong-recovery budget: bounded SOT closure has a finite polar certificate, while unbudgeted pointwise approximation does not.

AF-104 shows that the infinite-cost regime is real rather than a formal possibility. Reinov's approximation-property example supplies an operator for which every finite observation can be matched while every coherent preadjoint/accessibility approximation has norm tending to infinity. Finite exactness therefore does not imply bounded accessibility even in a classical Banach-space setting.

## What remains possible

Nonlinear repair categories can still differ from linear accessibility, and a concrete arithmetic source may force reflexivity, complementability, positivity, locality, equivariance, or another structure that collapses some gates. Those hypotheses must be derived from the source rather than chosen after the target is known.

## Status / novelty

Approximation properties, bidual embeddings, preadjoints, strong-operator closure, tensor norms, and Reinov-type counterexamples are classical. The synthesis is the hierarchy: **finite exactness < uniformly bounded accessibility < correct morphism category < original-range global assembly**.

## Falsification criterion

Show that a concrete source category forces these gates to coincide, or construct a bounded second-leg/original-range repair contradicting the persisted accessibility or tensor-norm obstructions. An arithmetic application must identify the source-forced budget and category before finite success is interpreted as global fidelity.

## Lean-formalizable core

- Finite polar interpolation duality.
- Exact second-leg accessibility cost `beta`.
- Bounded SOT-closure gauge for preadjoints.
- Separation of finite exactness from bounded accessibility.
