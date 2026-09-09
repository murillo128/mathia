# VIS-114 — centered macroscopic third-order averages have an exact independent-null scale

## Claim

Let `X_1,...,X_N` be independent identically distributed real random variables with

`E[X_i]=0`, `E[X_i^2]=v<infinity`.

For integers `0<a<b<N`, put `M=N-b` and define the admissible-start third-order average

`T_(a,b) = (1/M) sum_(i=1)^M X_i X_(i+a) X_(i+b)`.

Then exactly

`E[T_(a,b)] = 0`

and

`Var(T_(a,b)) = v^3/M`.

Moreover, if `(a,b)!=(c,d)` are two distinct ordered lag pairs with `0<a<b<N` and `0<c<d<N`, then

`Cov(T_(a,b), T_(c,d)) = 0`.

Hence for any finite predeclared set of distinct lag pairs and deterministic weights `w_j`,

`Var(sum_j w_j T_(a_j,b_j)) = v^3 sum_j w_j^2/(N-b_j)`.

The natural independent-null scale of a centered third-order lag average is therefore `M^(-1/2)`, not `M^(-1)`.

The constant-amplitude homometric family of `VIS-113` survives centering as well. Its two binary words `x_r,y_r` have common global mean

`p=7/29`.

Define the centered empirical third-order average at the same macroscopic lags

`B_z(2r,8r) = (1/(21r)) sum_(i=1)^(21r) (z_i-p)(z_(i+2r)-p)(z_(i+8r)-p)`.

Then for every `r>=1`,

`B_(x_r)(2r,8r)-B_(y_r)(2r,8r)`
` = (1-p^2)/21`
` = 264/5887`.

Thus the synthetic `VIS-113` separation remains exactly nonzero after mean centering, while a population-centered independent null has standard deviation of order `N^(-1/2)` at the same macroscopic lag fractions.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL WHITE-NOISE/HIGHER-ORDER-STATISTICS BASELINE + SYNTHETIC AMPLITUDE CALIBRATION + NO-SOURCE-SPECIFICITY + NO-NOVELTY-CLAIM`.

No finite-size CUE variance, conditioned Markov-type variance, zeta/CUE difference, asymptotic normality, or RH implication is established.

## 1. One lag pair has exact variance `v^3/M`

Write

`Y_i = X_i X_(i+a) X_(i+b)`,

so `T_(a,b)=M^(-1) sum_i Y_i`.

The three indices in each `Y_i` are distinct because `0<a<b`. Independence and centering give

`E[Y_i]=E[X_i]E[X_(i+a)]E[X_(i+b)]=0`.

Also

`E[Y_i^2]=E[X_i^2]E[X_(i+a)^2]E[X_(i+b)^2]=v^3`.

For `i!=j`, consider the two three-point index sets

`S_i={i,i+a,i+b}`,
`S_j={j,j+a,j+b}`.

They cannot be equal: their minima are respectively `i` and `j`. Therefore their symmetric difference is nonempty. Any index in that symmetric difference occurs to the first power in the product `Y_i Y_j`. By independence its centered first moment factors out, so

`E[Y_i Y_j]=0`.

Consequently the summands are pairwise uncorrelated even when their index triples overlap, and

`Var(T_(a,b))`
` = M^(-2) sum_(i=1)^M Var(Y_i)`
` = M^(-2) M v^3`
` = v^3/M`.

No Gaussian approximation or large-`N` limit is used.

## 2. Distinct lag pairs are exactly orthogonal under the independent null

Let

`T_(a,b)=(N-b)^(-1) sum_i X_i X_(i+a) X_(i+b)`

and define `T_(c,d)` analogously.

A cross term can have nonzero expectation only if the two three-point index sets are identical, because otherwise some independent centered variable occurs exactly once.

Suppose

`{i,i+a,i+b}={j,j+c,j+d}`.

Both sets have their starting index as their unique minimum, so equality forces `i=j`. Subtracting that common minimum then gives

`{0,a,b}={0,c,d}`.

With ordered positive lags this forces `(a,b)=(c,d)`.

Therefore distinct lag-pair averages have zero covariance exactly. The weighted-panel variance formula follows by bilinearity.

This does **not** make the lag-pair statistics independent. It supplies only an exact second-moment normalization for the independent centered baseline.

## 3. The `VIS-113` witness retains constant amplitude after centering

For the lifted words of `VIS-113`, each word contains exactly `7r` ones among `29r` positions, so the common global mean is

`p=7/29`.

At lags `2r` and `8r`, there are `21r` admissible starts. The direct macro-block count used in `VIS-113` gives the following exact differences between `x_r` and `y_r` over those starts.

For the raw triple sum,

`Delta sum z_i z_(i+2r) z_(i+8r) = r`.

For all three pair sums appearing after centering,

`Delta sum z_i z_(i+2r) = 0`,
`Delta sum z_i z_(i+8r) = 0`,
`Delta sum z_(i+2r) z_(i+8r) = 0`.

For the three single-coordinate sums,

`Delta sum z_i = -r`,
`Delta sum z_(i+2r) = 0`,
`Delta sum z_(i+8r) = 0`.

These counts are the `r`-fold lift of the fixed macro words: for `r=1` the corresponding raw counts are respectively

`(triple; pairs; singles)_x = (1; 2,2,2; 4,5,6)`,
`(triple; pairs; singles)_y = (0; 2,2,2; 5,5,6)`,

and every active macro offset is repeated exactly `r` times.

Expanding the centered product therefore yields the raw centered-sum difference

`r - p(0) + p^2(-r) = r(1-p^2)`.

Dividing by `21r` gives

`Delta B = (1-p^2)/21`
` = (1-49/841)/21`
` = 264/5887`.

The constant `1/21` raw-binary contrast from `VIS-113` is therefore not an artifact of failing to remove the mean.

## 4. What this says about amplitude calibration

For a population-centered independent baseline with variance `v`, the one-statistic standard deviation is exactly

`v^(3/2)/sqrt(M)`.

Thus a fixed nonzero centered contrast at macroscopic lags is extensive relative to that baseline: measured in units of one-sequence independent-null standard deviation, it grows like `sqrt(M)`.

This sharpens the amplitude gate in the accepted multiscale clue. A raw normalized effect should not be classified as large or small solely by whether it tends to a constant. The relevant comparison is the fluctuation scale of the **declared matched null**. `M^(-1/2)` is an exact sanity-check scale for independent centered data, not a substitute for the finite-size CUE or conditioned source null required by the zeta experiment.

The same distinction prevents the opposite mistake. An `O(M^(-1/2))` effect can be order-one after variance stabilization, while an `O(1)` effect can still be generic if the matched non-arithmetic source produces the same structure.

## 5. Prior art and novelty assessment

Third-order moments, cumulants, bispectra, and their sampling theory are classical. `VIS-109` already records C. L. Nikias and M. R. Raghuveer, **Bispectrum estimation: A digital signal processing framework**, *Proceedings of the IEEE* 75:7 (1987), 869–891, DOI `10.1109/PROC.1987.13824`, and Jerry M. Mendel, **Tutorial on higher-order statistics (spectra) in signal processing and system theory: theoretical results and some applications**, *Proceedings of the IEEE* 79:3 (1991), 278–305, DOI `10.1109/5.75086`, as standard higher-order-statistics references.

A targeted check also recovers David R. Brillinger, **An Introduction to Polyspectra**, *The Annals of Mathematical Statistics* 36:5 (1965), 1351–1374, DOI `10.1214/aoms/1177699896`, as foundational prior art for polyspectra and statistical properties of their estimators.

The variance and cross-covariance identities above are elementary finite-sample consequences of independence and centering, specialized to the exact admissible-start lag statistic used by the current Mathia branch. The centered `VIS-113` calculation is likewise a direct finite count on the already-persisted block lift. **No new general theorem in time-series analysis, bispectral estimation, or white-noise theory is claimed.**

## Boundary and falsification

The independent-null theorem requires an externally defined or population-centered sequence with independent coordinates and zero mean. If centering is performed with the same sample mean being tested, the coordinates become dependent and the displayed variance identity need not hold exactly.

Likewise, fixed symbol counts, exact Markov-type conditioning, CUE eigenangle dependence, unfolded zero-gap constraints, overlapping-window construction, or any other source-preserving conditioning can introduce covariance absent from the independent baseline. Those cases require their own calibration.

The theorem would be falsified by an independent centered distribution and distinct positive lag pair for which a cross term with unequal three-point index sets has nonzero expectation, or by a `VIS-113` lift for which one of the displayed finite counts fails. Independence plus the singleton-index factorization proves the former, and direct block counting proves the latter.

## Visual consequence

No canonical PNG is retained. A lag-plane variance heatmap for the independent null would be visually flat after multiplying each coefficient by `sqrt(N-b)/v^(3/2)`, but the exact diagonal covariance calculation already establishes that normalization without dependence on rendering, binning, or color scale.

A later source visualization should therefore show variance-stabilized third-order residuals relative to the **actual matched source null**, not raw coefficient magnitude alone.

## Research consequence

`VIS-113` established that fixed-block escape, complete two-point homometry, and constant raw empirical third-order amplitude can coexist. `VIS-114` adds the first exact fluctuation-scale calibration for this branch and shows that the same synthetic witness keeps constant amplitude after centering.

The representational and elementary amplitude-normalization gates are now cleanly separated from the remaining source question. A zeta-zero continuation must still predeclare its lag law and centering/normalization, then estimate or derive the finite-size CUE or otherwise appropriate conditioned-null covariance before inspecting confirmation residuals. The independent `M^(-1/2)` law is a baseline sanity check, not evidence of arithmetic specificity.