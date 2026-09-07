# VIS-085 — linear Gram-arc subtraction freezes broad growing prime supports

## Claim

Let `g_n` be the Gram points, defined for all sufficiently large `n` by

`theta(g_n) = pi n`,

up to the harmless conventional integer shift, and put

`a_n = theta'(g_n)`.

Let `H_n=O(log g_n)` and let `P_n>=2`. For each prime `p<=P_n` and `0<=h<=H_n`, define the phase after removing the exact first-order Gram arc at the block origin by

`R_(n,h)(p)`
` = exp(-i log p [g_(n+h)-g_n-pi h/a_n])`.

Then uniformly over the whole block and all admitted primes,

`max_(h<=H_n) max_(p<=P_n) |R_(n,h)(p)-1|`
` << H_n^2 log P_n / [g_n (log g_n)^3]`.

Consequently, whenever

`H_n^2 log P_n = o(g_n (log g_n)^3)`,

the arc-removed prime-phase field collapses uniformly to the identity. In the transition regime `H_n=O(log g_n)`, this reduces to the very broad condition

`log P_n = o(g_n log g_n)`.

Thus allowing the prime support to grow does not by itself create a Gram-specific local residual after the deterministic first-order sampling arc has been matched. In particular, every polynomial support `P_n<=g_n^A` with fixed `A` lies far inside the collapsing regime.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GRAM-SPACING COROLLARY + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No short-block equidistribution theorem, zeta-approximation theorem, prime/zero independence statement, or RH consequence is claimed.

## 1. The inverse-theta curvature controls the arc error

Write

`Delta_(n,h) = g_(n+h)-g_n`.

For `H_n=O(log g_n)`, `VIS-084` gives uniformly

`Delta_(n,h)=O(H_n/log g_n)=O(1)`.

The standard Riemann-Siegel theta asymptotics are

`theta'(t) = (1/2) log(t/(2 pi)) + O(t^(-2))`

and

`theta''(t) = 1/(2t) + O(t^(-3))`.

Taylor's theorem in integral form gives

`pi h`
` = theta(g_n+Delta_(n,h))-theta(g_n)`
` = a_n Delta_(n,h)`
`   + integral_0^Delta_(n,h) [Delta_(n,h)-u] theta''(g_n+u) du`.

Because `Delta_(n,h)=O(1)`, uniformly over the block

`sup_(0<=u<=Delta_(n,h)) |theta''(g_n+u)| = O(1/g_n)`.

Therefore

`|Delta_(n,h)-pi h/a_n|`
` <= [1/a_n] O(Delta_(n,h)^2/g_n)`
` = O(h^2/[g_n a_n^3])`
` = O(h^2/[g_n (log g_n)^3])`.

This is the curvature correction left after subtracting the local linear inverse-theta model. For `h=O(log g_n)` its size is `O(1/[g_n log g_n])`.

The estimate is deliberately stated as a uniform bound rather than as a new Gram-spacing asymptotic. It needs only the classical first two theta derivatives and the already established logarithmic-block diameter.

## 2. Growing prime support only multiplies the curvature error by `log P_n`

For any real `x`,

`|e^(-ix)-1| <= |x|`.

Hence for every `p<=P_n`,

`|R_(n,h)(p)-1|`
` <= log p |Delta_(n,h)-pi h/a_n|`
` << h^2 log P_n/[g_n (log g_n)^3]`.

Taking the maxima over `h<=H_n` and the prime support proves the claim.

Equivalently, let the arc-corrected block vector be

`r_(n,h) = (R_(n,h)(p))_(p<=P_n)`

on the growing prime torus, equipped with the sup chord metric. Then

`max_(h<=H_n) d_infty(r_(n,h),1)`
` << H_n^2 log P_n/[g_n (log g_n)^3]`.

Thus the empirical distribution of the corrected vectors converges to a point mass whenever the displayed ratio tends to zero. This conclusion is dimension-free in the sup metric: the number of prime coordinates may grow, and only the largest logarithmic frequency enters the deterministic sampling-error bound.

## 3. What this closes in the visual search space

`VIS-084` left growing prime support as a separate local question because its raw phase-diameter estimate contains `max log p`. That caveat is real for the **unsubtracted** cloud: larger primes move faster along the deterministic Gram arc.

But once the correct local null is the first-order arc itself, the relevant quantity is not the raw motion `Delta log p`; it is the inverse-theta curvature error

`[Delta-pi h/a_n] log p`.

That error is much smaller. At `H=O(log g_n)`, any support with `log P_n=o(g_n log g_n)` has vanishing arc-removed residual. Ordinary polynomial, polylogarithmic, and much larger subexponential-in-`g_n log g_n` supports therefore cannot produce a persistent local residual merely from nonuniform Gram spacing.

This does not say that a growing prime field is statistically equivalent to a fixed-dimensional Haar field. It says something narrower and local: **after matching the deterministic Gram sampling arc, the residual sampling geometry itself vanishes uniformly across an enormous growing-frequency range**. Any surviving effect must come from the observable/source law, a larger block scale, or an additional coordinate, not from the first curvature correction of the Gram clock.

## Prior art and novelty assessment

The Riemann-Siegel theta asymptotics, Gram-point definition, and average Gram spacing are classical. `VIS-083` records the discrete-universality literature in which Gram-point prime phases are studied globally, including A. Laurinčikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`, and the earlier M. Korolev–A. Laurinčikas Gram-point work.

A targeted search around Gram-point short blocks and inverse-theta spacing did not identify a reason to present the uniform arc-remainder estimate as a new theorem. It is an elementary Taylor consequence of the classical theta derivatives. No novelty is claimed for that estimate.

The durable Mathia contribution is the resulting **control boundary** for the visual search: the growing-support caveat left by `VIS-084` does not rescue logarithmic Gram blocks merely through sampling-clock curvature across any support satisfying the explicit uniform bound.

## Boundary and falsification

The result assumes `H_n=O(log g_n)` so that the whole Gram block remains in an `O(1)` height interval and the theta-curvature bound is uniform in the simple form used above. Longer blocks require a separate analysis rather than extrapolating this estimate.

The support bound controls only the Gram-clock residual. It does not prove global Haar equidistribution uniformly over growing prime dimension, and it does not remove arithmetic information carried by the prime coefficients themselves, `Z(g_n)`, Gram occupancy, derivatives, nearby-zero geometry, or another independently supplied coordinate.

The sup metric is intentional because it gives a coordinatewise visual-control statement independent of the number of admitted primes. Statistics whose Lipschitz constants grow rapidly with dimension need their own normalization before this coordinatewise collapse can be converted into a scalar error bound.

Falsify the claim by breaking the classical theta derivative asymptotics, the logarithmic-block `Delta=O(1)` estimate, Taylor's remainder bound, or the elementary phase chord inequality. A proposed positive Gram residual must show either that its scale lies outside the displayed corridor or that its signal remains after this arc-removal error is accounted for.

## Visual consequence

No canonical PNG is retained. The exact uniform remainder bound is stronger than a finite-height plot of the corrected phase cloud, and a scatter could visually magnify a residual that the theorem forces to zero after the proper scaling.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should be narrowed again. For `H=O(log g_n)`, **controlled growing prime support is not a local Gram-anchor escape merely because the prime dimension grows**: after subtracting the deterministic first-order Gram arc, the entire coordinatewise residual vanishes whenever `log P_n=o(g_n log g_n)`.

A surviving Gram-based route must therefore move to genuinely longer blocks, use an observable/source law with information not explained by the matched prime-torus arc, or add an independently informative Gram/zero coordinate. Merely increasing the number of prime phases inside a logarithmic Gram block no longer qualifies as an uncovered local mechanism.