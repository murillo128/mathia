# VIS-041 — common Markov whitening gives an exact orientation-sensitive three-gap residual comparison

## Claim

Let `P^(A)` and `P^(B)` be two probability laws on the same fixed finite three-variable alphabet `(X,Y,Z)`, with positive middle marginals, and let

`Q^(r)_(ijk) = P^(r)_(ij) P^(r)_(jk) / P^(r)_j`,  `r in {A,B}`,

be their own adjacent-pair-preserving Markov closures. Put

`Delta^(r) = P^(r) - Q^(r)`.

Each residual has exactly zero `XY` and `YZ` marginals:

`sum_k Delta^(r)_(ijk)=0`,  `sum_i Delta^(r)_(ijk)=0`.

Now choose one **common**, strictly positive Markov reference law

`H_(ijk)=h_j a_(i|j) b_(k|j)`

on the same support and define the common-reference whitened residuals

`W^(r)_(ijk)=Delta^(r)_(ijk)/sqrt(H_(ijk))`.

For each middle state `j`, let

`u_j=(sqrt(a_(i|j)))_i`,  `v_j=(sqrt(b_(k|j)))_k`.

Then both processes lie in the same interaction space:

`W^(r)_j v_j = 0`,  `u_j^T W^(r)_j = 0`.

Consequently, after choosing any **common** orthonormal contrast bases `U_j` for `u_j^perp` and `V_j` for `v_j^perp`, both residuals admit lossless coordinates

`C^(r)_j = U_j^T W^(r)_j V_j`,
`W^(r)_j = U_j C^(r)_j V_j^T`.

The common-reference Fisher inner product is exactly

`G_H(A,B)`
` = sum_(i,j,k) Delta^(A)_(ijk) Delta^(B)_(ijk) / H_(ijk)`
` = sum_j tr((C^(A)_j)^T C^(B)_j)`.

Writing `E_H(r)=G_H(r,r)`, the normalized orientation coefficient

`kappa_H(A,B) = G_H(A,B) / sqrt(E_H(A) E_H(B))`

is defined whenever both residuals are nonzero, lies in `[-1,1]`, and is invariant under every common orthonormal change of contrast bases and every common relabeling of the fixed bins. It therefore compares **where the irreducible conditional-dependence residual points** after lower-order marginals have been removed, rather than only how large its Pearson/CMI energy is.

This comparison is deliberately reference-dependent: changing `H` changes the metric and can change `kappa_H`. The exact representation control is therefore **common gauge, not canonical gauge**. The reference law, support, partition, and whitening rule must be fixed before inspecting the process difference.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION CONTROL + CLASSICAL FISHER/CORRESPONDENCE-ANALYSIS GEOMETRY + NO-NOVELTY-CLAIM`.

No claim is made that a particular reference `H` is mathematically privileged, that zeta and finite CUE have matching residual directions, that `kappa_H` is an RH criterion, or that it is a new general matrix-similarity coefficient.

## 1. The two residuals share one exact interaction subspace

Because each `Q^(r)` preserves the two adjacent-pair marginals of its own `P^(r)`, the residual identities

`sum_k Delta^(r)_(ijk)=0`,
`sum_i Delta^(r)_(ijk)=0`

hold without requiring the two processes to share the same marginals.

Fix `j`. Since

`sqrt(H_(ijk)) = sqrt(h_j) sqrt(a_(i|j)) sqrt(b_(k|j))`,

we have

`(W^(r)_j v_j)_i`
` = sum_k Delta^(r)_(ijk) sqrt(b_(k|j)) / sqrt(H_(ijk))`
` = [1/(sqrt(h_j) sqrt(a_(i|j)))] sum_k Delta^(r)_(ijk)`
` = 0`.

Likewise

`u_j^T W^(r)_j = 0`.

Thus the two whitened residual matrices belong to the same linear space

`u_j^perp tensor v_j^perp`.

If the outer alphabet sizes are `I` and `K`, this space has dimension `(I-1)(K-1)` per middle state. This is the same classical conditional-interaction dimension already exposed by `VIS-025`; the new point is that a **single externally fixed Markov whitening** puts two different processes into one shared metric and one shared contrast space.

Let `U_j` and `V_j` have orthonormal columns spanning those complements. The projector identities

`U_j U_j^T = I-u_j u_j^T`,
`V_j V_j^T = I-v_j v_j^T`

and the two annihilation relations give

`W^(r)_j = U_j U_j^T W^(r)_j V_j V_j^T`.

Hence

`C^(r)_j = U_j^T W^(r)_j V_j`

is lossless once the common reference and contrast gauges are fixed.

## 2. Fisher overlap is exactly Frobenius overlap in common coordinates

At a positive discrete law `H`, the Fisher inner product of two simplex tangent vectors `R` and `S` is

`<R,S>_H = sum R_(ijk) S_(ijk) / H_(ijk)`.

Applying this to the two conditional residuals gives

`G_H(A,B)=sum_j <W^(A)_j,W^(B)_j>_F`.

Because `U_j` and `V_j` are isometries on the interaction subspace,

`<W^(A)_j,W^(B)_j>_F`
` = tr((C^(A)_j)^T C^(B)_j)`.

The same calculation with `A=B` gives

`E_H(A)=sum_j ||C^(A)_j||_F^2`,
`E_H(B)=sum_j ||C^(B)_j||_F^2`.

Cauchy-Schwarz therefore yields `|kappa_H|<=1`.

If the common contrast bases are changed by

`U'_j=U_j R_j`,  `V'_j=V_j S_j`

with orthogonal `R_j,S_j`, then

`C'^(r)_j = R_j^T C^(r)_j S_j`.

Both Frobenius norms and the cross inner product are unchanged. A common permutation of the fixed bins similarly conjugates all three objects — `H`, `Delta^(A)`, and `Delta^(B)` — by the same permutation matrices and leaves `G_H`, `E_H`, and `kappa_H` unchanged.

The signed per-fiber contributions

`g_j = tr((C^(A)_j)^T C^(B)_j)`

also provide an exact localization of agreement or opposition across the middle-state fibers. Their sum is `G_H`; they should be inspected when cancellation across fibers could hide a mixed comparison.

## 3. Singular spectra do not determine residual orientation

`VIS-025` and `VIS-035` show why correspondence-analysis singular values are useful invariant summaries, but they also show that singular vectors/orientation are quotiented out. The common-reference construction makes that information loss explicit.

Take one middle state with outer alphabet sizes at least three, so the interaction-coordinate matrix is at least `2 x 2`. In one common contrast basis let

`C^(A)=diag(1,0)`.

Three possible second residual directions are

`C^(B_1)=diag(1,0)`,
`C^(B_2)=diag(0,1)`,
`C^(B_3)=-diag(1,0)`.

All four matrices have the same singular spectrum `(1,0)` and the same Frobenius norm. Nevertheless their common-reference orientation coefficients relative to `A` are respectively

`kappa_H(A,B_1)=1`,
`kappa_H(A,B_2)=0`,
`kappa_H(A,B_3)=-1`.

Mapping the `C` matrices back through `U C V^T` and multiplying by `sqrt(H)` gives valid zero-row/zero-column residual directions; after sufficiently small scaling they are valid probability perturbations about `H`. Thus the loss of orientation is not a coordinate pathology. Identical CA singular spectra can represent aligned, orthogonal, or opposed conditional-interaction directions.

This also explains why separately whitening each process by its own closure and then separately choosing its SVD basis is inadequate for a direction claim. The resulting coordinates use different metrics and independently rotating gauges. Their norms or singular values remain meaningful within each process, but there is no single Fisher inner product in which a signed cross-orientation has been fixed.

## 4. Relation to the CMI finite-size transfer question

`VIS-040` gives the local Markov-limit expansion. If two smooth process families share the same positive Markov base `H`,

`P_epsilon^(r)=H+epsilon A_r+O(epsilon^2)`,

and `B_r=A_r-Pi_H A_r` is the Fisher-normal component from `VIS-040`, then their own Markov residuals satisfy

`Delta_epsilon^(r)=epsilon B_r+O(epsilon^2)`.

Therefore

`kappa_H(P_epsilon^(A),P_epsilon^(B))`
` -> <B_A,B_B>_H / (||B_A||_H ||B_B||_H)`

whenever both normal components are nonzero. At the same time,

`I(P_epsilon^(r)) = (epsilon^2/2)||B_r||_H^2 + O(epsilon^3)`.

So in the exact local regime the scalar CMI records only the two normal magnitudes, while `kappa_H` records their relative Fisher-normal direction. A scalar CMI crossing can therefore coexist with `kappa_H` near zero or negative; such an outcome would falsify a stronger claim that the two processes have transferred the same irreducible three-gap geometry even if their scalar interaction energies match.

For finite empirical laws not known to be small perturbations of one common Markov base, `kappa_H` remains an exact common-reference comparison of their residual tensors, but the local Fisher/CMI interpretation above must not be imported automatically. In that regime it is a pre-registered representation statistic, not a geodesic distance, likelihood-ratio theorem, or process-identification result.

## 5. Prior art and novelty assessment

The ingredients are classical. `VIS-025` already identifies each fixed-middle-state Pearson-whitened residual with ordinary correspondence-analysis interaction geometry, using the standard CA references recorded in `SOURCES.md`. `VIS-040` already identifies the Fisher metric as the quadratic local metric for the positive probability simplex and cites Amari and Nagaoka's *Methods of Information Geometry* as the standard information-geometric anchor.

A targeted novelty check also finds a broad classical literature on metric-aware matrix/configuration similarity, including P. Robert and Y. Escoufier, **A Unifying Tool for Linear Multivariate Statistical Methods: The RV-Coefficient**, *Applied Statistics* 25:3 (1976), 257–265, DOI `10.2307/2347233`. That coefficient is not the signed statistic defined here — it is designed to quotient orientation more aggressively — but it reinforces that matrix similarity under chosen metrics is standard multivariate geometry.

No novelty is claimed for the Fisher metric, Frobenius inner product, normalized cosine, orthogonal contrast changes, correspondence analysis, or matrix-similarity methodology. The Mathia-specific durable content is the exact **common-gauge control** for the already active three-gap experiment: residualize each process against its own lower-order Markov closure, then compare the surviving residuals in one pre-fixed positive Markov metric. This pins down precisely what “direction-sensitive comparison” must preserve and why matching scalar CMI or singular spectra alone cannot do it.

## 6. Boundary conditions and falsification

The common reference `H` must be strictly positive on the fixed support. Structural or sampling zeros require a predeclared common reduced support or another justified regularization; deleting cells differently for the two processes destroys the shared space.

`H` is part of the representation. Selecting it after seeing which choice maximizes zeta/CUE agreement or separation is parameter fishing. A serious empirical test should pre-register a process-independent construction — for example a fixed external control/reference law or another rule frozen before the comparison — and treat reasonable alternative references as robustness checks rather than optimization variables.

The two residuals must be formed from their own adjacent-pair-preserving Markov closures before common whitening. Whitening raw `P^(A)-P^(B)` would mix lower-order marginal differences back into the object and would not test the same conditional-interaction channel.

If either `E_H(A)` or `E_H(B)` is zero, `kappa_H` is undefined. Report the zero residual rather than assigning an arbitrary angle. A global `kappa_H` can also conceal cancellation between positive and negative `g_j`, so per-fiber signed overlaps should accompany the aggregate when the middle-state allocation matters.

Falsify the algebra if a claimed residual fails the exact zero `XY`/`YZ` marginal identities, if a common-reference whitened residual fails `W_j v_j=0` or `u_j^T W_j=0`, if the coordinate/Fisher inner products disagree, or if a common orthogonal basis change alters `kappa_H`. Those failures indicate inconsistent residualization, support, weighting, or normalization rather than a new data effect.

Statistical significance is a separate layer. Overlapping zeta triples are dependent, fitted residuals have finite-sample floors, and the finite-CUE/arithmetic baseline remains essential. This finding supplies a representation-preserving direction statistic; it does not calibrate its sampling distribution.

## Research consequence

The accepted `CLUE-zeta-three-gap-cmi-equivalent-size-eight` now has an exact direction-sensitive companion to its scalar CMI bracket without requiring an independently optimized SVD basis. For each predeclared higher zeta window and matched finite-CUE control, freeze one common positive Markov reference `H`, compute both processes' own Markov residuals, and report `kappa_H` together with the signed per-fiber overlaps and the already specified scalar CMI comparison.

A stronger finite-circle transfer interpretation should require the scalar bracket and residual orientation to move coherently under the same frozen partition/reference rule. If the scalar CMI-equivalent size moves as predicted while `kappa_H` is unstable, near zero, or opposed, retain the result only as a norm-level scalar calibration. Conversely, stable orientation does not by itself establish arithmetic structure; it still must survive independent windows, finite-size CUE, arithmetic corrections, and process-aware uncertainty.

This closes the representation ambiguity in the clue's pre-registered “direction-sensitive comparison” requirement. The remaining work is empirical/process-level rather than another choice of visual coordinate. No new visualization is required for this exact control.