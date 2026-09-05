# VIS-042 — logarithmic pooling of Markov closures gives one panel-wide residual-orientation gauge

## Claim

Let `P^(1),...,P^(m)` be probability laws on the same fixed finite three-variable alphabet `(X,Y,Z)`. Assume each adjacent-pair-preserving Markov closure

`Q^(r)_(ijk) = P^(r)_(ij) P^(r)_(jk) / P^(r)_j`

is strictly positive on the common support. Write

`Q^(r)_(ijk) = q^(r)_j a^(r)_(i|j) b^(r)_(k|j)`.

Fix positive weights `lambda_r` with `sum_r lambda_r=1` **before** inspecting the residual-orientation comparison, and form the normalized weighted logarithmic pool

`H_(ijk) = Z^(-1) product_r (Q^(r)_(ijk))^(lambda_r)`.

Then `H` is itself a strictly positive first-order Markov law. More explicitly, put

`c_j = product_r (q^(r)_j)^(lambda_r)`,

`A_j = sum_i product_r (a^(r)_(i|j))^(lambda_r)`,

`B_j = sum_k product_r (b^(r)_(k|j))^(lambda_r)`.

The normalizer is

`Z = sum_j c_j A_j B_j`,

and

`H_(ijk) = h_j alpha_(i|j) beta_(k|j)`,

where

`h_j = c_j A_j B_j / Z`,

`alpha_(i|j) = [product_r (a^(r)_(i|j))^(lambda_r)] / A_j`,

`beta_(k|j) = [product_r (b^(r)_(k|j))^(lambda_r)] / B_j`.

Thus the panel's own lower-order Markov closures generate a **single common Markov reference** without choosing a different whitening law for each pair of processes.

Let

`Delta^(r) = P^(r) - Q^(r)`

be the irreducible adjacent-pair-preserving residuals. By `VIS-041`, all of them can now be compared in the same Fisher metric at `H`:

`G_rs = sum_(i,j,k) Delta^(r)_(ijk) Delta^(s)_(ijk) / H_(ijk)`.

The matrix `G=(G_rs)` is positive semidefinite. For every process with `G_rr>0`, the normalized coefficients

`K_rs = G_rs / sqrt(G_rr G_ss)`

form a positive-semidefinite correlation Gram matrix on the nonzero residuals, with entries in `[-1,1]`. They compare residual **orientation** after the lower-order `XY` and `YZ` marginals have been removed, rather than only residual magnitude.

With equal weights `lambda_r=1/m`, the pooled reference is invariant under permutation of the panel members. The construction is also invariant under a common relabeling of the fixed bins and, through `VIS-041`, under a common orthonormal change of interaction coordinates.

The improvement over an arbitrary `H` is procedural, not absolute: **the logarithmic pool fixes one gauge for one predeclared panel, but it does not produce a canonical gauge independent of the panel, weights, support, or partition**.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL LOGOP/MARKOV-PRESERVATION SPECIALIZATION + REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that the pooled metric is statistically optimal, that a particular panel or weighting is privileged, that zeta and finite CUE residual directions agree, that logarithmic pooling is new, or that this construction gives an RH criterion.

## 1. The weighted logarithmic pool stays inside the Markov family

The unnormalized pool factorizes directly:

`tilde H_(ijk)`
` = product_r [q^(r)_j a^(r)_(i|j) b^(r)_(k|j)]^(lambda_r)`
` = c_j [product_r a^(r)_(i|j)^(lambda_r)]`
`       [product_r b^(r)_(k|j)^(lambda_r)]`.

Summing over `i,k` therefore gives

`sum_(i,k) tilde H_(ijk) = c_j A_j B_j`,

and summing over `j` gives the stated `Z`. Dividing by `Z` and normalizing the two conditional factors separately yields

`H_(ijk)=h_j alpha_(i|j) beta_(k|j)`.

Hence `X` and `Z` are conditionally independent given `Y` under `H`.

Nothing specifically arithmetic enters this step. It is the elementary three-variable chain specialization of the classical fact that logarithmic opinion pooling preserves commonly held Markov independencies. David M. Pennock and Michael P. Wellman, **Graphical Representations of Consensus Belief**, UAI 1999, pp. 531–540, explicitly identify this preservation property for LogOP; their later **Graphical Models for Groups: Belief Aggregation and Risk Sharing**, *Decision Analysis* 2:3 (2005), 148–164, DOI `10.1287/deca.1050.0048`, develops the corresponding graphical-model representation. The factorization above is derived here directly so the exact normalization used by the Mathia residual comparison is explicit.

This prior art rules out treating Markov preservation under the geometric/logarithmic pool as a new general theorem.

## 2. One pooled reference gives one simultaneous residual space

For every `r`, the own-closure residual satisfies exactly

`sum_k Delta^(r)_(ijk)=0`,

`sum_i Delta^(r)_(ijk)=0`.

Because the pooled `H` is Markov, write its conditionals as `alpha_(i|j)` and `beta_(k|j)` and define

`u_j=(sqrt(alpha_(i|j)))_i`,

`v_j=(sqrt(beta_(k|j)))_k`.

Whitening every residual by the **same** `H`,

`W^(r)_(ijk)=Delta^(r)_(ijk)/sqrt(H_(ijk))`,

gives for every process and every middle state

`W^(r)_j v_j=0`,

`u_j^T W^(r)_j=0`.

Choose common orthonormal contrast bases `U_j` for `u_j^perp` and `V_j` for `v_j^perp`. Then

`C^(r)_j = U_j^T W^(r)_j V_j`

is a lossless coordinate representation of the residual interaction, and

`G_rs = sum_j tr((C^(r)_j)^T C^(s)_j)`.

For any real coefficients `x_1,...,x_m`,

`sum_(r,s) x_r G_rs x_s`
` = sum_j ||sum_r x_r C^(r)_j||_F^2`
` >= 0`.

So `G` is exactly a Gram matrix. Restricting to nonzero residuals and dividing each vector by its norm gives the normalized positive-semidefinite matrix `K`.

The signed fiber contributions

`g_j^(r,s)=tr((C^(r)_j)^T C^(s)_j)`

remain available when a global angle could hide cancellation between middle-state fibers. This is the same localization control as `VIS-041`, now placed in one common metric for an entire panel rather than just one pair.

## 3. What the pool fixes, and what it does not

`VIS-041` deliberately left the common positive Markov reference `H` external. That is mathematically clean, but an empirical panel could still drift into pair-specific gauges: one reference for zeta window A versus `CUE_8`, another for window B versus `CUE_12`, and so on. Angles computed in those different metrics are not directly one common orientation geometry.

The logarithmic-pool rule removes that **pairwise gauge drift** once the panel and weights are frozen. The panel's own Markov closures contain only its admitted lower-order `XY` and `YZ` structure; their logarithmic pool stays Markov and supplies one metric in which all residual vectors can be placed simultaneously. Every pairwise entry of `K` is then an angle in the same Hilbert space.

This does not make the metric intrinsic to the underlying mathematical process. Adding or removing a panel member changes `H`; changing the weights changes `H`; changing the common partition or support changes `H`. Equal weighting removes dependence on the *ordering* of panel members, not dependence on *which* members were admitted.

Accordingly, the panel and weights are part of the representation contract and must be fixed before looking for alignment. Choosing a subset or weights after observing which choice makes zeta and CUE look closest would be the same kind of parameter fishing that the Visual Researcher is required to reject elsewhere.

A fixed external `H` remains preferable when the scientific question genuinely supplies one. The pooled construction is useful precisely when the desired control is: use the compared processes' lower-order Markov structure, but do so through one symmetric predeclared rule rather than separately optimized pairwise references.

## 4. The pooled gauge has the correct local Fisher limit

The construction is also compatible with the local information geometry of `VIS-040`.

Suppose a panel of Markov closures approaches the same strictly positive Markov base `H_0` smoothly:

`Q_epsilon^(r) = H_0 + epsilon T_r + O(epsilon^2)`,

with `sum T_r=0`, and suppose the own-closure residuals satisfy

`Delta_epsilon^(r)=epsilon B_r+O(epsilon^2)`.

Take fixed weights `lambda_r`. Entrywise,

`log Q_epsilon^(r)`
` = log H_0 + epsilon T_r/H_0 + O(epsilon^2)`.

Therefore the unnormalized logarithmic pool is

`H_0 + epsilon sum_r lambda_r T_r + O(epsilon^2)`.

Its total mass has no first-order correction because each `T_r` is a probability tangent vector. Hence normalization does not change the first-order term, and

`H_epsilon`
` = H_0 + epsilon sum_r lambda_r T_r + O(epsilon^2)`.

Consequently

`G_rs(epsilon)`
` = epsilon^2 sum B_r B_s/H_0 + O(epsilon^3)`
` = epsilon^2 <B_r,B_s>_(H_0) + O(epsilon^3)`.

Whenever `B_r` and `B_s` are nonzero,

`K_rs(epsilon)`
` -> <B_r,B_s>_(H_0) / (||B_r||_(H_0) ||B_s||_(H_0))`.

Thus the pooled-reference angle converges to the Fisher-normal angle already identified by `VIS-040` and `VIS-041`. The panel pooling changes the finite comparison gauge, but it does not invent a different leading local interaction geometry when the processes genuinely share a Markov limit.

This local statement is conditional on the displayed smooth common-base regime. It is not evidence that finite CUE and finite-height zeta satisfy that regime.

## 5. Prior-art and novelty boundary

The main ingredients are classical. Logarithmic opinion pooling is a standard weighted geometric aggregation of probability laws. Pennock and Wellman establish preservation of common Markov independencies under LogOP and bound any novelty claim for the first part of this construction. Fisher inner products, conditional-independence models, and local divergence geometry are standard information geometry, as already recorded for `VIS-040`; common whitened residual coordinates and their normalized overlap were made explicit for the Mathia three-gap problem in `VIS-041`.

The present result does **not** claim a new opinion-pooling theorem or a new general similarity coefficient. Its durable Mathia-specific content is the composition of those classical pieces under the active representation constraint:

- residualize each process against its **own** adjacent-pair-preserving Markov closure so lower-order differences are removed;
- logarithmically pool those closures under one predeclared panel/weight rule;
- use the resulting Markov law as the **single** whitening metric for every residual in the panel;
- retain the complete Gram/orientation matrix rather than collapsing back to one scalar dependence energy.

That composition closes a concrete ambiguity left by `VIS-041`: how to obtain one shared Markov gauge for several comparisons without choosing an independently favorable metric for each pair.

## 6. Boundary conditions and falsification

Strict positivity on one common support is required. If one process has structural zeros or finite-sample zeros, the panel needs a predeclared common reduced support or a justified common regularization before logarithmic pooling. Dropping different cells for different processes destroys the shared geometry.

The Markov closures must be formed **before** pooling. Pooling the raw `P^(r)` would generally preserve some common graphical structure but would mix the irreducible conditional residual back into the reference itself and would no longer implement the lower-order-quotient control used here.

The same empirical data may be used algebraically to estimate a process's closure and residual, but that makes the pooled metric statistically dependent on the residual estimates. This finding supplies an exact representation, not a sampling distribution. A significance test must preserve that dependence through process-aware resampling, sample splitting/cross-fitting, or another predeclared calibration appropriate to the data source.

If a residual has `G_rr=0`, its normalized orientation is undefined and should be reported as a zero interaction rather than assigned an arbitrary angle. Rare cells can make `1/H` weights unstable even when positivity formally holds; minimum-mass and partition robustness are empirical controls, not reasons to tune `H` after seeing the result.

The algebra is falsified if the normalized pool fails the displayed Markov factorization, if an own-closure residual fails its exact zero `XY`/`YZ` marginal identities, if the whitened residual leaves the common interaction subspace, if `G` is not positive semidefinite up to numerical tolerance in a faithful implementation, or if a common relabeling/common contrast rotation changes `G` or `K`.

A stable `K` is still not arithmetic evidence by itself. Similar residual orientations can arise from a shared universal finite-size mechanism, estimator bias, or another admitted control. Conversely, disagreement in orientation can refute a strong process-transfer interpretation while leaving a scalar CMI crossing intact.

## Research consequence

The accepted `CLUE-zeta-three-gap-cmi-equivalent-size-eight` asks whether the descriptive finite-CUE CMI bracket transfers to independent higher zeta windows and explicitly requires a direction-sensitive residual comparison frozen before inspecting those windows. `VIS-041` supplied the exact pairwise orientation statistic; this finding supplies a natural **panel-wide gauge rule** when no external reference law is privileged.

A future empirical test may predeclare the complete comparison panel — for example the selected independent zeta windows together with the declared finite-CUE sizes/controls — and equal weights, construct every process's own Markov closure under the already frozen common partition, logarithmically pool those closures once, and report the resulting residual Gram/correlation matrix alongside scalar CMI and the signed fiber overlaps.

If the scalar CMI-equivalent bracket moves with height while the orientation entries are unstable, near zero, or opposed in the same frozen panel metric, the evidence remains a norm-level finite-size calibration. If both magnitude and direction move coherently, that is a stronger process-level observation but still must survive independent windows, finite-size CUE controls, arithmetic corrections, and process-aware uncertainty before any arithmetic interpretation.

No new visualization or new clue is required for this exact representation result. It narrows the already accepted empirical clue without resolving it.