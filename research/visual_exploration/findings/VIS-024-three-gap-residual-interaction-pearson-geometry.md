# VIS-024 — three-gap residual has exact interaction dimension and Pearson-weighted local geometry

## Claim

Let `P(i,j,k)` be a fully supported distribution on three consecutive `s`-state bins, and let

`Q(i,j,k) = P_12(i,j) P_23(j,k) / P_2(j)`

be its adjacent-pair-preserving Markov closure from `VIS-020`. Write `Delta = P-Q`.

For every fixed middle state `j`,

`sum_k Delta(i,j,k) = 0` for every `i`, and
`sum_i Delta(i,j,k) = 0` for every `k`.

Hence the `s x s` residual slice `Delta_j` lies in the row-and-column-zero interaction subspace, whose dimension is exactly `(s-1)^2`. With all `s` middle states present, the complete pair-marginal-preserving three-gap residual therefore has

`dim = s(s-1)^2`

independent directions. This is exactly the Wilks degrees of freedom in `VIS-023` for first-order versus second-order Markov dependence.

Moreover, on a fixed adjacent-pair-marginal fiber, put `P=Q+Delta` and let `max |Delta_ijk|/Q_ijk -> 0`. Then

`I_P(X;Z|Y) = D(P||Q)`
`             = (1/2) sum_ijk Delta_ijk^2 / Q_ijk`
`               + O(sum_ijk |Delta_ijk|^3 / Q_ijk^2)`.

Thus the local likelihood geometry is not Euclidean geometry of the raw tensor `Delta`. Its natural quadratic coordinates are the Pearson-weighted residuals

`W_ijk = Delta_ijk / sqrt(Q_ijk)`,

for which

`2 I_P(X;Z|Y) = ||W||_2^2 + higher-order terms`.

**Evidence/status:** `CLASSICAL-CONTINGENCY-GEOMETRY + EXACT-DERIVED SPECIALIZATION`.

The result is an information-accounting and visualization control. It does not establish any zeta-specific higher-order signal.

## Exact residual constraints and dimension

Because `P` and `Q` have the same `12` and `23` marginals,

`sum_k P(i,j,k) = sum_k Q(i,j,k)`

and

`sum_i P(i,j,k) = sum_i Q(i,j,k)`.

Subtracting gives the displayed zero-row and zero-column constraints on each fixed-`j` slice.

An `s x s` real matrix has `s^2` coordinates. Requiring all `s` row sums and all `s` column sums to vanish gives `2s` linear equations, but one is redundant because the total row sum equals the total column sum. Their rank is therefore `2s-1`, leaving

`s^2-(2s-1) = (s-1)^2`

degrees of freedom. The slices for distinct positive-mass middle states are independent under these linear constraints, giving `s(s-1)^2` dimensions in the fully supported equal-alphabet case.

This recovers the dimension difference in `VIS-023` from the geometry of the residual tensor itself rather than by separately counting Markov transition parameters.

## Local KL/Pearson geometry

On a fixed pair-marginal fiber the closure `Q` is fixed. For one cell write `u=Delta/Q`. The scalar expansion

`(Q+Delta) log((Q+Delta)/Q) = Q(1+u) log(1+u)`

gives

`Delta + Delta^2/(2Q) - Delta^3/(6Q^2) + O(Delta^4/Q^3)`.

Summing over cells removes the linear term because `sum Delta=0`. Therefore

`D(Q+Delta||Q) = (1/2) sum Delta^2/Q + O(sum |Delta|^3/Q^2)`

as the relative perturbation tends uniformly to zero.

For empirical triple frequencies with `m` overlapping triples, the corresponding local Pearson form is

`X_P^2 = m sum_ijk (P_hat_ijk-Q_hat_ijk)^2 / Q_hat_ijk`.

Together with `VIS-023`, this explains the classical asymptotic equivalence between the likelihood-ratio statistic

`G^2 = 2m D(P_hat||Q_hat)`

and the Pearson quadratic form. Both see the same `s(s-1)^2` interaction directions asymptotically.

## Visual consequence

The paired artifact

`research/visual_exploration/visualizations/three-gap-residual-whitening-geometry.md`

shows one fixed middle-state slice with a nonuniform Markov closure. A small `2 x 2` checkerboard perturbation preserves every row and column sum, so all four nonzero raw residual cells have exactly the same magnitude. In the Pearson-weighted view the same perturbation is much larger in cells where `Q` is small.

This is not a discovery from the synthetic picture. It illustrates an exact consequence of the KL expansion: a raw residual heatmap and a likelihood-sensitive residual heatmap answer different questions. Raw `Delta` localizes displaced probability mass; `Delta/sqrt(Q)` localizes contribution to the local information metric.

## Prior art and novelty assessment

The maximum-entropy closure and identity `D(P||Q)=I(X;Z|Y)` are standard information theory, already anchored to Cover and Thomas in `SOURCES.md` and specialized in `VIS-020`.

Pearson chi-square residual geometry, likelihood-ratio `G^2`, their common contingency-table degrees of freedom, and asymptotic equivalence are classical categorical-data theory. Besag and Mondal, **Exact Goodness-of-Fit Tests for Markov Chains**, *Biometrics* 69:2 (2013), 488–496, DOI `10.1111/biom.12009`, already used by `VIS-023`, give the first-order-versus-second-order Markov likelihood-ratio statistic and its `s(s-1)^2` asymptotic chi-square calibration. The present dimension calculation and Taylor expansion are elementary specializations to the exact adjacent-pair-preserving residual used by this visual line.

No novelty is claimed for Pearson weighting, the KL quadratic expansion, or the dimension formula. The useful Mathia result is the **representation control**: the active zeta three-gap experiment has an exact residual subspace and a canonical local weighting, so visual salience in raw probability mass must not be confused with salience in likelihood/information geometry.

## Boundary conditions

The expansion is local and requires positive `Q` with small relative perturbations. Rare or zero expected cells make `Delta/sqrt(Q)` unstable or undefined and are evidence that the partition is too sparse for this asymptotic geometry. They must not be rescued by silently deleting bins after inspecting the data.

The entries of `W=Delta/sqrt(Q)` are **not independent z-scores**. They satisfy transformed linear constraints, and with empirical `Q_hat` they also inherit covariance from estimating the pair marginals from the same sequence. Cellwise thresholds therefore require the appropriate fitted-model covariance or process-level resampling; the heatmap alone supplies no significance test.

The same warning applies across zeta and CUE. Because each process is projected against its own adjacent-pair closure, their `Q` tensors need not match exactly. A fair comparison must keep the partition and estimation rule fixed and propagate each process's finite-sample covariance rather than comparing color intensity by eye.

## Research consequence

`CLUE-zeta-three-gap-conditional-residual` remains live. Its next empirical visualization should retain both the raw residual `Delta` and the Pearson-weighted residual `Delta/sqrt(Q)` (or an equivalent covariance-aware projection), with occupancy diagnostics and the same fixed partition on zeta and matched finite-size CUE/arithmetic controls.

The scalar `I=D(P||Q)` remains the exact nonlinear information distance. The weighted residual adds localization in the metric that generates that scalar to second order. A candidate zeta-minus-control pattern should survive both representation choices or have a precise reason for appearing in only one, and any cellwise claim must be calibrated with the fitted residual covariance or matched process-level resampling.
