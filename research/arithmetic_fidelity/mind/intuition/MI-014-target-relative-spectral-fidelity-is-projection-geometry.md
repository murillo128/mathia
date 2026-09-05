# MI-014 — Target-relative spectral fidelity is projection geometry until a source-canonical metric upgrades it to a generalized spectrum

**Evidence level:** supported through AF-138 by exact whitening, Moore--Penrose projection identities, complete fixed-target congruence invariants, commutant-gauge classification, and generalized Hermitian-definite spectral transport

## Core intuition

A raw source Gram matrix does not carry an intrinsic hierarchy of positive spectral magnitudes under arbitrary changes of generator coordinates. Without extra source geometry, target fidelity reduces to how target directions project onto the represented source subspace. Compact symmetry does not usually fix this: it leaves exactly the positive metric cone of the representation commutant, large enough to arbitrarily rescale active positive Gram channels.

A genuine source metric changes the category. If the source independently supplies a positive-definite coefficient metric `M`, then the invariant spectral object is the generalized pencil `(G,M)`, equivalently the whitened operator `M^{-1/2}GM^{-1/2}`. Spectral scale is meaningful relative to that metric, not relative to an arbitrary coordinate identity.

## Strongest justified principle

AF-135 gives the exact fixed-target residual `dist(k,ran A)^2=kappa-b^*G^dagger b`; after whitening it is ordinary projection geometry. AF-136 extends this to a target family: the projection Gram `Q=C^*G^dagger C` together with `rank G` is a complete invariant under the full invertible generator gauge, while positive Gram eigenvalue magnitudes can be changed by congruence.

AF-137 asks whether symmetry alone supplies the missing metric. For a compact-group representation, every invariant coefficient metric is a positive self-adjoint operator in the commutant. On each multiplicity space this freedom acts by positive congruence and can prescribe all active positive Gram eigenvalues. The metric is unique up to scale only for an irreducible coefficient representation, exactly where equivariance also forces the Gram spectrum to be flat. Symmetry therefore cannot simultaneously provide a nontrivial canonical positive spectral hierarchy and its own metric.

AF-138 gives the exact conditional repair. With a source-specified `M>0`, the generalized eigenvalues of `Gx=lambda Mx` are invariant under `A->AR`, `G->R^*GR`, `M->R^*MR`; after whitening the change is unitary. The target-relative generalized Picard measure is invariant as well, and the excess truncation error is exactly its discarded low-generalized-eigenvalue mass. If `M` is canonical only up to scale, eigenvalue ratios/order survive but an absolute cutoff still needs a normalization.

## What remains possible

A concrete spectral-fidelity theorem should derive `M` from source-natural measure, energy, probability, arithmetic weights, geometry, or another independently specified form, then prove the required generalized Picard-tail estimate. Choosing `M` from the target, desired cutoff, or Gram matrix itself merely moves the gauge choice into the metric.

For sources without such a metric, use projection/principal-angle geometry rather than raw spectral scale. For sources with only symmetry, classify the residual commutant gauge before attributing meaning to eigenvalue magnitudes.

## Status / novelty

Gram matrices, pseudoinverses, compact-group commutants, generalized eigenvalue pencils, whitening, singular values, and Picard regularization are classical. The persisted synthesis is the category boundary: **projection geometry is intrinsic under full generator gauge; symmetry alone generally leaves a commutant metric gauge; a source-canonical metric repairs that gauge and makes the generalized spectrum, not the raw Gram spectrum, the meaningful object**.

## Falsification criterion

Produce a nontrivial raw Gram spectral ordering invariant under the full admitted generator gauge without additional coefficient geometry, show that compact symmetry fixes a rich positive hierarchy despite the AF-137 commutant freedom, or find a simultaneously transported metric/source representation for which the generalized spectrum or generalized Picard tail changes.

## Lean-formalizable core

- Pseudoinverse projection identity and congruence invariance.
- Positive commutant classification of invariant metrics.
- Positive-congruence freedom on multiplicity blocks.
- Generalized pencil invariance under metric transport.
- Generalized Picard-tail identity for target truncation.
