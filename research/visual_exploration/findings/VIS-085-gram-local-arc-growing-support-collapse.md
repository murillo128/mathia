# VIS-085 — linear Gram-arc subtraction freezes broad growing prime supports

## Claim

Let `g_n` be the Gram points, defined for all sufficiently large `n` by

`theta(g_n) = pi n`,

up to the harmless conventional integer shift, and put

`a_n = theta'(g_n)`.

Let `H_n>=0` be any integer sequence and let `P_n>=2`. For each prime `p<=P_n` and `0<=h<=H_n`, define the phase after removing the exact first-order Gram arc at the block origin by

`R_(n,h)(p)`
` = exp(-i log p [g_(n+h)-g_n-pi h/a_n])`.

Then, for all sufficiently large `n`, uniformly over the whole block and all admitted primes,

`max_(h<=H_n) max_(p<=P_n) |R_(n,h)(p)-1|`
` << H_n^2 log P_n / [g_n (log g_n)^3]`.

Consequently, whenever

`H_n^2 log P_n = o(g_n (log g_n)^3)`,

the arc-removed prime-phase field collapses uniformly to the identity.

This is substantially stronger than the original logarithmic-block formulation. For fixed prime support it covers every

`H_n = o(sqrt(g_n) (log g_n)^(3/2))`,

while for polynomial support `P_n<=g_n^A` with fixed `A` it covers every

`H_n = o(sqrt(g_n) log g_n)`.

Thus increasing the Gram-block length well beyond `log g_n`, or allowing the prime support to grow polynomially, still does not create a Gram-specific residual after the deterministic first-order sampling arc has been matched throughout this corridor.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GRAM-SPACING COROLLARY + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No long-block equidistribution theorem, zeta-approximation theorem, prime/zero independence statement, or RH consequence is claimed.

## 1. Monotonicity of the Gram clock removes the logarithmic-block restriction

Write

`Delta_(n,h) = g_(n+h)-g_n`.

The standard Riemann-Siegel theta asymptotics are

`theta'(t) = (1/2) log(t/(2 pi)) + O(t^(-2))`

and

`theta''(t) = 1/(2t) + O(t^(-3))`.

Hence, for all sufficiently large `t`, `theta'(t)>0` and `theta''(t)>0`. In particular `theta'` is increasing on every interval beginning at a sufficiently large Gram point.

For every `h>=0`, the mean-value identity and monotonicity give

`pi h = theta(g_n+Delta_(n,h))-theta(g_n)`
`     >= a_n Delta_(n,h)`,

so

`0 <= Delta_(n,h) <= pi h/a_n`.

Unlike the earlier proof, this estimate does not require `Delta_(n,h)=O(1)` or `H_n=O(log g_n)`.

Taylor's theorem in integral form gives

`pi h`
` = a_n Delta_(n,h)`
`   + integral_0^Delta_(n,h) [Delta_(n,h)-u] theta''(g_n+u) du`.

Because every point in the integration interval is at least `g_n`, the theta asymptotic yields the uniform bound

`sup_(u>=0) |theta''(g_n+u)| << 1/g_n`.

Therefore the Taylor remainder is nonnegative and

`0 <= pi h/a_n - Delta_(n,h)`
` << Delta_(n,h)^2/(g_n a_n)`
` << h^2/(g_n a_n^3)`
` << h^2/[g_n (log g_n)^3]`.

The key point is that the same inverse-theta curvature bound is valid for arbitrary block length; it merely becomes too weak to force collapse once `H_n` leaves the displayed square-root-scale corridor.

## 2. Growing prime support multiplies only the clock remainder

For any real `x`,

`|e^(-ix)-1| <= |x|`.

Hence for every `p<=P_n`,

`|R_(n,h)(p)-1|`
` <= log p |Delta_(n,h)-pi h/a_n|`
` << h^2 log P_n/[g_n (log g_n)^3]`.

Taking the maxima over `h<=H_n` and the prime support proves the claim.

Equivalently, let

`r_(n,h) = (R_(n,h)(p))_(p<=P_n)`

be the arc-corrected block vector on the growing prime torus with the sup chord metric. Then

`max_(h<=H_n) d_infty(r_(n,h),1)`
` << H_n^2 log P_n/[g_n (log g_n)^3]`.

Thus the empirical distribution of corrected vectors converges to a point mass whenever the displayed ratio tends to zero. This coordinatewise statement is dimension-free: only the largest admitted logarithmic frequency enters the deterministic sampling-error bound.

## 3. What the stronger corridor closes

`VIS-084` identifies `H=Theta(log g_n)` as the first fixed-prime scale on which the raw Gram phase cloud can move an order-one distance. The original version of this finding showed that, at that transition scale, subtracting the first-order inverse-theta arc kills its curvature residual even across enormous growing prime supports.

The monotonicity argument above shows that the control is not confined to that local transition. For polynomial prime cutoff, the same first-order arc remains coordinatewise complete throughout every block with

`H_n=o(sqrt(g_n) log g_n)`.

For fixed prime support the corridor is larger by a factor `sqrt(log g_n)`. These blocks contain vastly more than logarithmically many consecutive Gram points, yet the only Gram-clock effect left after linear arc subtraction still vanishes uniformly.

This does not say that the prime field is statistically Haar on those growing blocks, nor that every scalar statistic built from many coordinates vanishes. It says something narrower and stronger as a visual null: **the nonlinearity of the Gram sampling clock itself cannot supply a persistent coordinatewise residual anywhere inside the condition `H_n^2 log P_n=o(g_n(log g_n)^3)`**.

A positive route inside this corridor must therefore use information in the observable/source law or an additional Gram/zero coordinate, not merely the curvature of the sampling schedule. A route based only on prime-phase motion must leave the corridor or replace the first-order arc by a different claim whose information content is independently justified.

## Prior art and novelty assessment

The Riemann-Siegel theta asymptotics, Gram-point definition, average Gram spacing, and inversion of the Gram clock are classical. `VIS-083` records the discrete-universality literature in which Gram-point prime phases are studied globally, including A. Laurinčikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`, and the earlier M. Korolev–A. Laurinčikas Gram-point work.

A targeted literature check around Gram-point spacing and inverse-theta descriptions did not identify a reason to present the displayed remainder estimate as a new theorem. The strengthened range is an elementary consequence of eventual monotonicity of `theta'`, the classical derivative asymptotics, Taylor's formula, and the phase chord inequality. No novelty is claimed for that analytic estimate.

The durable Mathia contribution is the **control boundary** for visual search: the first-order Gram arc remains a sufficient sampling-clock null on a much longer block corridor than the original logarithmic formulation recorded.

## Boundary and falsification

The collapse conclusion requires

`H_n^2 log P_n=o(g_n(log g_n)^3)`.

Outside this corridor the bound ceases to force a vanishing residual; that is an absence of control, not evidence of a positive mechanism. A higher-order inverse-theta subtraction may extend the null further, but that is a separate mathematical question and is not assumed here.

The support bound controls only the Gram-clock residual. It does not prove Haar equidistribution uniformly over growing prime dimension, approximate zeta by the admitted prime support, or remove arithmetic information carried by the prime coefficients themselves, `Z(g_n)`, Gram occupancy, derivatives, nearby-zero geometry, or another independently supplied coordinate.

The sup metric is intentional because it gives a coordinatewise visual-control statement independent of the number of admitted primes. Statistics whose Lipschitz constants grow rapidly with dimension need their own normalization before this coordinatewise collapse can be converted into a scalar error bound.

Falsify the claim by breaking the classical eventual theta derivative asymptotics, monotonicity of `theta'`, Taylor's remainder bound, or the elementary phase chord inequality. A proposed positive Gram residual inside the stated corridor must show that its signal uses information not accounted for by this arc-removal null.

## Visual consequence

No canonical PNG is retained. The exact uniform remainder bound is stronger than a finite-height plot of the corrected phase cloud, and a scatter could visually magnify a residual that the theorem forces to zero after the proper scaling.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should be narrowed again. **Genuinely longer Gram blocks are not by themselves an escape from the deterministic sampling null.** For polynomial prime support, linear Gram-arc subtraction forces coordinatewise collapse all the way through `H_n=o(sqrt(g_n) log g_n)`; for fixed support the proved corridor is larger still.

A surviving Gram-based route must therefore operate beyond the explicit `H_n^2 log P_n=o(g_n(log g_n)^3)` corridor, use an observable/source law with information not explained by the matched prime-torus arc, or add an independently informative Gram/zero coordinate. Whether higher-order inverse-theta correction closes still longer blocks is left as a separate follow-up rather than being folded into this finding.