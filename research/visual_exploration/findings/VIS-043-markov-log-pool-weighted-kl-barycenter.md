# VIS-043 — the pooled Markov gauge is the unique weighted-KL barycenter of the panel closures

## Claim

Let `Q^(1),...,Q^(m)` be the strictly positive adjacent-pair-preserving Markov closures from `VIS-042`, on one fixed finite support, and let positive weights `lambda_r` satisfy `sum_r lambda_r=1`. Define

`H(x) = Z^(-1) product_r Q^(r)(x)^(lambda_r)`,

where `x=(i,j,k)` and

`Z = sum_x product_r Q^(r)(x)^(lambda_r)`.

Then for every probability law `R` on the same support,

`sum_r lambda_r D_KL(R || Q^(r)) = D_KL(R || H) - log Z`.

Consequently `H` is the **unique** minimizer of the weighted aggregate-to-panel divergence

`R -> sum_r lambda_r D_KL(R || Q^(r))`

over the full probability simplex. Since `VIS-042` proves that `H` is itself Markov, the same `H` is also the unique minimizer when `R` is restricted to the positive first-order Markov family.

At the minimum,

`D_pool := sum_r lambda_r D_KL(H || Q^(r)) = -log Z >= 0`,

with equality if and only if all panel closures `Q^(r)` are identical.

Thus the logarithmic-pool gauge from `VIS-042` is not merely a symmetric convenient choice: **for the already fixed panel, weights, support, and KL direction, it is the unique distribution simultaneously closest to the panel closures in weighted `D_KL(gauge || closure)` loss**. This does not make the gauge canonical independently of those choices.

If

`H_(ijk)=h_j alpha_(i|j) beta_(k|j)`

and

`Q^(r)_(ijk)=q^(r)_j a^(r)_(i|j) b^(r)_(k|j)`,

then the panel dispersion has the exact Markov-chain decomposition

`D_pool`
` = sum_r lambda_r D_KL(h || q^(r))`
` + sum_j h_j sum_r lambda_r D_KL(alpha_(.|j) || a^(r)_(.|j))`
` + sum_j h_j sum_r lambda_r D_KL(beta_(.|j) || b^(r)_(.|j))`.

The scalar `D_pool` therefore measures only disagreement in the admitted lower-order Markov structure used to define the common gauge. It does **not** measure the irreducible three-gap residuals `Delta^(r)=P^(r)-Q^(r)`, their common-reference energies, or their orientation Gram matrix from `VIS-041`/`VIS-042`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL LOGOP/KL-BARYCENTER SPECIALIZATION + REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that this KL direction is statistically optimal for the zeta/CUE comparison, that the panel or weights are privileged, that small `D_pool` forces stable residual angles, or that the variational characterization is a new general opinion-pooling theorem.

## 1. Exact variational identity

By definition of the normalized geometric pool,

`product_r Q^(r)(x)^(lambda_r) = Z H(x)`.

For any probability law `R`,

`sum_r lambda_r D_KL(R || Q^(r))`
` = sum_x R(x) [log R(x) - sum_r lambda_r log Q^(r)(x)]`
` = sum_x R(x) log [R(x)/(Z H(x))]`
` = D_KL(R || H) - log Z`.

Since all `Q^(r)` and therefore `H` are strictly positive, the right-hand side is finite on the fixed support. Gibbs' inequality gives

`D_KL(R || H) >= 0`,

with equality exactly at `R=H`. Hence `H` is the unique global minimizer, and evaluating the identity at `R=H` gives

`D_pool=-log Z`.

Because `VIS-042` independently establishes that the logarithmic pool of these Markov closures remains in the same first-order Markov family, restricting the minimization to that family does not move the optimum.

The equality criterion follows immediately. If `D_pool=0`, every nonnegative term `lambda_r D_KL(H||Q^(r))` vanishes because every `lambda_r>0`; hence `Q^(r)=H` for all `r`. Conversely identical panel closures give `Z=1`, `H=Q^(r)`, and `D_pool=0`.

## 2. The dispersion localizes entirely to lower-order Markov channels

For two positive Markov laws

`H_(ijk)=h_j alpha_(i|j) beta_(k|j)`

and

`Q^(r)_(ijk)=q^(r)_j a^(r)_(i|j) b^(r)_(k|j)`,

the log likelihood ratio splits additively:

`log[H_(ijk)/Q^(r)_(ijk)]`
` = log[h_j/q^(r)_j]`
` + log[alpha_(i|j)/a^(r)_(i|j)]`
` + log[beta_(k|j)/b^(r)_(k|j)]`.

Averaging under `H` and summing out the normalized conditional factors gives the ordinary KL chain-rule decomposition

`D_KL(H||Q^(r))`
` = D_KL(h||q^(r))`
` + sum_j h_j D_KL(alpha_(.|j)||a^(r)_(.|j))`
` + sum_j h_j D_KL(beta_(.|j)||b^(r)_(.|j))`.

Weighting by `lambda_r` yields the displayed formula for `D_pool`.

This gives a useful representation diagnostic before any residual-angle interpretation. A large `D_pool` can be localized to disagreement in the middle-state marginal, the left conditional channel, or the right conditional channel. Such disagreement means the common Fisher gauge is spanning materially different lower-order closures and should be subjected to the partition/support/gauge robustness controls already required by `VIS-041` and `VIS-042`.

But the converse must not be overstated. `D_pool=0` only says that all lower-order Markov closures coincide. Their irreducible residuals may still have different magnitudes or directions. Likewise a nonzero `D_pool` does not imply that the orientation matrix `K` is unstable; that is a separate residual-level question.

## 3. Prior art and novelty boundary

The variational characterization of logarithmic pooling by weighted KL divergence is classical. Ali E. Abbas, **A Kullback-Leibler View of Linear and Log-Linear Pools**, *Decision Analysis* 6:1 (2009), 25–37, DOI `10.1287/deca.1080.0133`, explicitly frames linear and log-linear opinion pools as optimal assignments under KL-based scoring. The identity above is derived directly because the exact KL direction and normalizing constant matter for the Mathia gauge interpretation.

`VIS-042` already records David M. Pennock and Michael P. Wellman's graphical-model prior art showing that logarithmic pooling preserves commonly held Markov independencies. Combining that preservation fact with the KL variational identity explains why the same pooled law is simultaneously (i) inside the admitted Markov reference family and (ii) the unique weighted-KL center of the declared panel closures.

No novelty is claimed for logarithmic opinion pooling, KL barycenters, Gibbs' inequality, the KL chain rule, or Markov-family preservation. The Mathia-specific durable content is the **interpretation boundary for the active residual-orientation control**: the pooled gauge has a precise predeclared optimization meaning, while its dispersion can be separated cleanly from the higher-order residual geometry that the experiment is actually trying to compare.

## 4. Boundary conditions and falsification

Strict positivity and one common support are essential for the finite formulas as stated. Structural zeros require the same predeclared reduced-support or regularization discipline already imposed by `VIS-042`; otherwise the KL objective may be infinite and different support choices can manufacture an apparent optimum.

The KL direction is part of the result. Reversing it to `sum_r lambda_r D_KL(Q^(r)||R)` generally gives a different barycenter and must not be described as the same variational principle. Likewise changing the panel, weights, partition, or support changes both `H` and `D_pool`.

The exact identity is falsified by any positive finite example for which

`sum_r lambda_r D_KL(R||Q^(r)) - D_KL(R||H)`

depends on `R` or differs from `-log Z`. The channel decomposition is falsified if its three nonnegative components fail to sum to `D_KL(H||Q^(r))` for any panel member.

`D_pool` must not be optimized after inspecting the residual Gram matrix. It is a diagnostic of the already chosen gauge construction, not another statistic to tune for zeta/CUE agreement.

## Research consequence

The panel-wide rule in `VIS-042` now has an exact variational interpretation. For a predeclared zeta/CUE comparison panel, one may report `D_pool=-log Z` and its three lower-order Markov-channel contributions alongside the residual orientation Gram matrix. This separates two questions that were previously easy to conflate: **how heterogeneous the lower-order closures are under the chosen common gauge, and how the irreducible residuals align once that gauge has been fixed**.

A robust process-transfer claim should not rely on a favorable pooled angle while hiding extreme lower-order gauge dispersion. Conversely, low `D_pool` does not count as residual agreement and supplies no arithmetic evidence by itself. The accepted `CLUE-zeta-three-gap-cmi-equivalent-size-eight` therefore remains unresolved: its empirical higher-window test still has to determine whether scalar magnitude and residual direction transfer together under a predeclared panel, with process-aware uncertainty and the finite-CUE/arithmetic controls already specified.

No new visualization or new clue is required for this exact representation result. It completes one coherent interpretation step after `VIS-042` and leaves the empirical transfer question for a later invocation.