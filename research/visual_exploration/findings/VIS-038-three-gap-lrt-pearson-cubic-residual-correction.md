# VIS-038 — the first Pearson/LRT separation is the cubic fitted-residual moment

## Claim

Use the empirical three-gap Markov-closure table and notation of `VIS-037`. On every fitted-positive cell let

`r_ijk = (n_ijk-e_ijk)/e_ijk`,

`eta = max |r_ijk|`,

`X_P^2 = sum e_ijk r_ijk^2`,

and define the weighted cubic residual moment

`C_3 = sum e_ijk r_ijk^3`.

The likelihood-ratio statistic is

`G^2 = sum e_ijk h(r_ijk)`,

with

`h(r)=2[(1+r)log(1+r)-r]`.

If `eta<1`, then

`|G^2 - X_P^2 + C_3/3| <= [eta^2/(6(1-eta)^3)] X_P^2`.

Therefore the first deterministic separation between likelihood-ratio/CMI energy and Pearson/CA energy is not another quadratic dependence channel. It is the signed cubic moment of the same fitted cell residuals, up to an explicitly controlled fourth-order remainder.

Equivalently, whenever `X_P^2>0`, put

`S_3 = C_3/X_P^2`.

Then `|S_3|<=eta` and

`G^2/X_P^2 - 1 = -S_3/3 + R`,

with

`|R| <= eta^2/[6(1-eta)^3]`.

Thus a small-residual table with excess positive residual skew (`C_3>0`) has `G^2<X_P^2` to leading cubic order, while negative residual skew reverses the sign. Agreement of the two totals can also occur because positive and negative cubic cell contributions cancel; it does not imply that every cell is close to quadratic symmetry.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL POWER-DIVERGENCE TAYLOR STRUCTURE + FINITE-TABLE REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No zeta-specific three-gap signal, random-matrix discrepancy, arithmetic effect, asymptotic zero statistic, or RH implication is claimed.

## 1. Cubic expansion with an explicit finite-table remainder

From `VIS-037`,

`h(r)=2[(1+r)log(1+r)-r]`.

Direct differentiation gives

`h(0)=h'(0)=0`,

`h''(0)=2`,

`h'''(0)=-2`,

and

`h''''(r)=4/(1+r)^3`.

Hence the third-order Taylor polynomial at zero is

`h(r)=r^2-r^3/3+q(r)`.

For `|r|<=eta<1`, Taylor's theorem gives

`|q(r)|`
` <= [sup_(|u|<=eta) |h''''(u)|] |r|^4/24`
` <= |r|^4/[6(1-eta)^3]`.

Multiplying cellwise by `e_ijk` and summing yields

`G^2 = X_P^2 - C_3/3 + sum e_ijk q(r_ijk)`.

Since `|r|^4 <= eta^2 r^2`,

`|sum e q(r)|`
` <= [1/(6(1-eta)^3)] sum e |r|^4`
` <= [eta^2/(6(1-eta)^3)] X_P^2`,

which proves the stated bound.

The normalization `S_3=C_3/X_P^2` satisfies

`|C_3| <= sum e |r|^3 <= eta sum e r^2 = eta X_P^2`,

so `|S_3|<=eta`.

## 2. What this adds to `VIS-037`

`VIS-037` proved the coarser deterministic statement that `G^2` and `X_P^2` coincide to first relative order when `eta` is small. The present expansion identifies the first term that can make them differ.

The quadratic part is exactly the total Pearson/CA principal-inertia energy. The cubic correction retains the **sign orientation** of fitted cell residuals: a positive and a negative residual of the same magnitude contribute equally to `X_P^2` but oppositely to `C_3`. Consequently the scalar discrepancy `G^2-X_P^2`, when the local expansion is valid, is primarily a residual-asymmetry coordinate rather than a second measurement of quadratic dependence strength.

This does not make `C_3` an independent information source. It is a deterministic functional of the same empirical three-gap table, and it can change under partitioning, support rules, unfolding, or occupancy just as the other fitted-table statistics do.

## 3. Representation consequence for the active three-gap visual program

The accepted three-gap clue currently compares CMI/LRT, total Pearson energy, and the conditional CA spectrum. `VIS-037` prevents counting the first two totals as independent confirmation in the local regime. `VIS-038` sharpens the diagnostic further.

For any pre-registered partition/window with `eta<1`, report `C_3` or `S_3` when interpreting a visible `G^2-X_P^2` separation. First verify the displayed remainder inequality. If the bound fails, the counts, fitted closure, support convention, or normalization are inconsistent. If it holds and the cubic term explains the separation, the difference between the two scalar totals should not be described as a new channel; it is the expected next power-divergence coordinate of the same residual table.

A zeta-versus-control difference in `S_3` could still be tested as a **matched residual-shape statistic**, because Pearson energy alone does not determine signed cellwise skew. But it must use the identical partition, support rule, unfolding, occupancy treatment, and finite-size process control on both sides. A large `S_3` in zeta alone is not evidence of arithmetic structure.

## 4. Prior art and novelty assessment

Pearson's statistic and the log-likelihood-ratio statistic are classical members of the Cressie–Read power-divergence family. Noel Cressie and Timothy R. C. Read, **Multinomial Goodness-Of-Fit Tests**, *Journal of the Royal Statistical Society: Series B (Methodological)* 46:3 (1984), 440–464, DOI `10.1111/j.2517-6161.1984.tb01318.x`, is already the canonical prior-art anchor used by `VIS-037`.

Higher-order Taylor comparison of power-divergence statistics is also established prior art. F. C. Drost, W. C. M. Kallenberg, D. S. Moore, and J. Oosterhoff, **Power Approximations to Multinomial Tests of Fit**, *Journal of the American Statistical Association* 84:405 (1989), 130–141, DOI `10.1080/01621459.1989.10478748`, explicitly develops Taylor expansions of the Cressie–Read statistics with Pearson `X^2` as the dominant term.

No novelty is claimed for the existence of a cubic correction, power-divergence asymptotics, or goodness-of-fit theory. The Mathia-specific value is the elementary **uniform finite-table remainder bound** written in the exact fitted three-gap Markov-closure coordinates already used by the visual program, together with the resulting interpretation of `G^2-X_P^2` as a residual-sign/skew diagnostic under the same local gate.

## 5. Boundary conditions and falsification

The bound requires `eta<1`. A fitted-positive cell with zero observed count has `r=-1` and lies outside the expansion gate. Near that boundary the fourth derivative grows rapidly and the local cubic interpretation is intentionally not trusted.

The cubic term can be small by cancellation even when individual residuals are not especially symmetric. Conversely, a nonzero `C_3` does not imply a zeta-specific effect; generic finite samples and matched determinantal controls can have signed residual skew.

The expansion concerns scalar power-divergence totals. It does not determine the full CA singular vectors or mode allocation. Two tables can share `X_P^2` and `C_3` while arranging residual geometry differently across middle-gap fibers and singular modes.

Falsify the implementation if a verified table with `eta<1` violates

`|G^2 - X_P^2 + C_3/3| <= [eta^2/(6(1-eta)^3)] X_P^2`.

Such a violation is a bookkeeping or implementation error, not an empirical anomaly.

## Research consequence

The current three-gap program should treat `eta`, `X_P^2`, `G^2`, and `C_3` as a nested local diagnostic: quadratic energy first, signed cubic correction second, and only then the fourth-and-higher residual remainder. This sharpens the information accounting before any high-zero versus matched-control experiment and supplies a direct consistency check without requiring a new visualization. The next substantive question remains empirical: whether any pre-registered scalar or CA-mode residual, including the signed cubic shape coordinate, separates zeta from the finite-size matched process after identical occupancy and support treatment.