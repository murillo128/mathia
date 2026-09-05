# VIS-037 — Pearson/CA and likelihood-ratio three-gap statistics coincide in the local residual regime

## Claim

Use the empirical three-gap Markov-closure setup of `VIS-023` and `VIS-036`. On every cell `(i,j,k)` with fitted expected count

`e_ijk = n_ij n_jk / n_j > 0`,

define the relative fitted residual

`r_ijk = (n_ijk-e_ijk)/e_ijk`,

and let

`eta = max_(e_ijk>0) |r_ijk|`.

Because the fitted table and observed table have the same total mass,

`sum_(e_ijk>0) e_ijk r_ijk = 0`.

The Pearson/CA statistic from `VIS-036` is

`X_P^2 = sum e_ijk r_ijk^2`,

while the likelihood-ratio/CMI statistic from `VIS-023` can be written exactly as

`G^2 = sum e_ijk h(r_ijk)`,

with

`h(r)=2[(1+r)log(1+r)-r]`.

If `eta<1`, so every fitted-positive cell is also observed-positive, then

`|G^2-X_P^2| <= [eta/(3(1-eta)^2)] X_P^2`.

Thus whenever all cellwise relative residuals are uniformly small, the likelihood-ratio/CMI energy and the Pearson/correspondence-analysis energy are deterministically forced to agree to first relative order. They are not two independent empirical channels in that regime; they are two members of the classical power-divergence family applied to the same fitted Markov-closure defect.

Without any small-residual assumption, the exact divergence inequality already used in `VIS-035` gives the global one-sided envelope

`G^2 <= 2m log(1+X_P^2/m) <= 2 X_P^2`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL POWER-DIVERGENCE RELATION + FINITE-TABLE REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No zeta-specific three-gap dependence, CUE discrepancy, arithmetic signal, asymptotic zero statistic, or RH implication is claimed.

## 1. Exact residual parameterization

Write one positive fitted-support cell as `n=e(1+r)`. Structural fitted zeros cause no problem: if `e_ijk=0`, then at least one required adjacent count is zero and hence `n_ijk=0`, so those cells contribute nothing after restricting to the fitted-positive support.

The Pearson statistic is immediately

`X_P^2`
` = sum (n-e)^2/e`
` = sum e r^2`.

For the likelihood ratio,

`G^2 = 2 sum n log(n/e)`
`    = 2 sum e(1+r)log(1+r)`.

Since observed and fitted totals both equal `m`,

`sum e r = sum(n-e)=0`.

Therefore subtracting the vanishing linear term gives the exact representation

`G^2 = sum e * 2[(1+r)log(1+r)-r]`
`    = sum e h(r)`.

This puts the two statistics on the same cellwise residual coordinate system rather than comparing only their common asymptotic chi-square limit.

## 2. Deterministic local-equivalence bound

Let

`f(r)=h(r)-r^2`.

A direct differentiation gives

`f(0)=f'(0)=f''(0)=0`,

and

`f'''(r) = -2/(1+r)^2`.

Assume `|r|<=eta<1`. Taylor's theorem with remainder around zero gives

`|f(r)|`
` <= [sup_(|u|<=eta) |f'''(u)|] |r|^3 / 6`
` <= |r|^3/[3(1-eta)^2]`.

Hence

`|G^2-X_P^2|`
` = |sum e f(r)|`
` <= sum e |f(r)|`
` <= [1/(3(1-eta)^2)] sum e |r|^3`
` <= [eta/(3(1-eta)^2)] sum e r^2`
` = [eta/(3(1-eta)^2)] X_P^2`.

The constant is deliberately elementary rather than optimized. The useful content is the explicit deterministic gate: if the maximum relative fitted residual is small, a substantial disagreement between `G^2` and `X_P^2` is mathematically impossible when both are computed from the same fitted table and support rule.

In particular, along any sequence of fixed-alphabet empirical tables for which `eta=o(1)`,

`G^2/X_P^2 -> 1`

whenever `X_P^2>0`. This is a finite-table route to the familiar local quadratic equivalence rather than a new asymptotic testing theorem.

## 3. Global one-sided envelope

`VIS-035` records the standard inequality

`D(P||Q) <= log(1+chi^2(P||Q))`.

For the empirical three-gap table,

`G^2=2m D(P_hat||Q_hat)`

and

`X_P^2=m chi_P^2(P_hat||Q_hat)`.

Therefore

`G^2 <= 2m log(1+X_P^2/m)`.

Using `log(1+x)<=x` for `x>=0` gives

`G^2 <= 2X_P^2`.

This bound remains valid when the local `eta<1` gate fails. It is one-sided and can be loose in sparse or strongly nonlocal tables; it does not replace process-level calibration.

## 4. Meaning for the active visual experiment

`VIS-023` and `VIS-036` currently give two scalar summaries of the same three-gap residual: `G^2` is the likelihood-ratio/CMI geometry and `X_P^2` is the total Pearson/CA principal-inertia energy. The present control separates two regimes.

When `eta` is small, the two totals are forced to be nearly equal. Reporting both remains useful as an implementation and support-rule consistency check, but agreement is not independent replication of a zeta-specific effect. The full CA spectrum can still localize *where* the Pearson energy lies across fibers and modes; the scalar total itself is locally the same quadratic residual measured by `G^2`.

When `eta` is not small, especially with sparse or nearly empty fitted cells, the local equivalence guarantee disappears. A numerical separation between `G^2` and `X_P^2` then says primarily that the fitted table is outside the quadratic local-residual regime. It must not be promoted as an additional arithmetic feature without the matched finite-size CUE/arithmetic comparison and process-level uncertainty required by the accepted clue.

This suggests a compact diagnostic for every partition/window:

`eta = max_(e_ijk>0) |n_ijk/e_ijk - 1|`,

reported alongside occupancy, `G^2`, `X_P^2`, and the CA spectrum. The same support convention must be used for zeta and every matched control.

## 5. Prior art and novelty assessment

The relationship between Pearson and likelihood-ratio goodness-of-fit statistics is classical. Noel Cressie and Timothy R. C. Read, **Multinomial Goodness-Of-Fit Tests**, *Journal of the Royal Statistical Society: Series B (Methodological)* 46:3 (1984), 440–464, DOI `10.1111/j.2517-6161.1984.tb01318.x`, place Pearson's `X^2` (`lambda=1`) and the log-likelihood-ratio statistic (`lambda=0`) in one power-divergence family and analyze asymptotic differences between members.

The Markov-order interpretation of the two statistics is already classicalized in `VIS-023` and `VIS-036`. No novelty is claimed for power-divergence statistics, local Pearson/LRT equivalence, chi-square limits, or goodness-of-fit asymptotics.

The Mathia-specific contribution is only the explicit deterministic **cellwise residual gate** specialized to the active three-gap Markov closure and its visual correspondence-analysis representation. It turns the vague statement that `G^2` and `X_P^2` are asymptotically similar into a directly checkable finite-table control for deciding whether two plotted/scalar summaries are genuinely providing different information in a particular visualization window.

## 6. Boundary conditions and falsification

The local bound requires `eta<1`. In particular, a fitted-positive cell with observed count zero has `r=-1` and lies outside the stated gate. This is intentional: zero or near-zero occupancy is exactly where the log and quadratic divergences can behave differently and ordinary chi-square approximations become fragile.

The condition is sufficient, not necessary. `G^2` and `X_P^2` may agree well even when one cell makes `eta` large, so failure of the gate is not evidence that the statistics must differ. The displayed constant is also not a sharp best constant.

Changing the partition, support trimming, pooling rare bins, or changing the unfolding changes the empirical table and therefore changes `eta`, `G^2`, and `X_P^2`. A post-hoc support edit that makes the local-equivalence diagnostic look better is not a valid robustness test.

The global envelope and the local bound concern the two scalar totals. They do not collapse the full CA spectrum to CMI: different singular-mode allocations can share the same `X_P^2`, and the matched zeta-versus-control spectral comparison remains a distinct visual question.

Falsify the implementation if a table with verified `eta<1` violates the deterministic inequality when `G^2` and `X_P^2` are computed from the same fitted closure. Do not interpret such a violation as mathematics; it signals inconsistent counts, support, normalization, or code.

## Research consequence

Sharpen `CLUE-zeta-three-gap-conditional-residual` by requiring the maximum fitted-relative-residual diagnostic `eta` for each pre-registered partition/window. In the local regime, treat `G^2` and total `X_P^2` as two coordinates of the same quadratic interaction channel rather than as independent confirmations. Outside that regime, use their disagreement only as a sparsity/nonlocality warning until matched-process Monte Carlo or another process-aware uncertainty analysis shows that it carries reproducible zeta-versus-control information.

The next substantive step remains the accepted clue's matched high-zero experiment. No new visualization is required to establish this control, so no PNG artifact is added or changed in this finding.