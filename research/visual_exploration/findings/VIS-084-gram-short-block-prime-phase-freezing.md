# VIS-084 — sublogarithmic Gram blocks freeze every fixed finite prime-phase field

## Claim

Let `g_n` be the Gram points, defined for all sufficiently large `n` by

`theta(g_n) = pi n`,

up to the harmless conventional integer shift in the Gram indexing. Fix distinct primes `p_1,...,p_r`, and write

`z_n = (exp(-i g_n log p_1), ..., exp(-i g_n log p_r)) in T^r`.

Let `H_n` be a nonnegative integer sequence with

`H_n = o(log g_n)`.

Then

`max_(0<=h<=H_n) max_(1<=j<=r) |exp(-i g_(n+h) log p_j) - exp(-i g_n log p_j)| -> 0`.

More quantitatively, for fixed prime support,

`max_(0<=h<=H) max_j |exp(-i g_(n+h) log p_j) - exp(-i g_n log p_j)|`
` <= (pi H/theta'(g_n)) max_j log p_j`
` = O(H/log g_n)`

uniformly whenever `H=O(log g_n)`.

Hence, with the torus metric

`d_infty(z,w)=max_j |z_j-w_j|`

and the empirical block measure

`mu_(n,H) = (1/(H+1)) sum_(h=0)^H delta_(z_(n+h))`,

one has

`W_1(mu_(n,H_n), delta_(z_n)) = O(H_n/log g_n) -> 0`.

Thus a consecutive Gram block of sublogarithmic length is asymptotically **frozen** on every fixed finite prime torus. A tight visual cluster in that regime is forced by Gram spacing and is not evidence of a new arithmetic information channel.

There is also a deterministic transition-scale description. Uniformly for `0<=h<=H=O(log g_n)`,

`g_(n+h)-g_n = [pi h/theta'(g_n)](1+o(1))`
`               = [2 pi h/log(g_n/(2 pi))](1+o(1))`.

Therefore the whole fixed-prime block is asymptotic to the one-parameter torus arc

`z_(n+h,j) = z_(n,j) exp(-2 pi i h log p_j/log(g_n/(2 pi)) + o(1))`,

uniformly over the block. The Gram-count scale `H=Theta(log g_n)` is the first scale on which order-one phase motion for fixed primes can occur; this statement does **not** assert Haar mixing at that scale.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GRAM-SPACING COROLLARY + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No short-block equidistribution theorem, growing-prime-support result, prime/zero independence statement, or RH consequence is claimed.

## 1. Consecutive Gram spacing gives a deterministic block diameter

For sufficiently large `t`, the Riemann-Siegel theta function satisfies the standard asymptotics

`theta'(t) = (1/2) log(t/(2 pi)) + O(t^(-2))`

and

`theta''(t) = 1/(2t) + O(t^(-3))`.

In particular, `theta'` is eventually positive and increasing. For `h>=0`, the mean-value theorem applied between `g_n` and `g_(n+h)` gives a point `xi_(n,h)` in that interval such that

`pi h = theta(g_(n+h))-theta(g_n)`
`     = theta'(xi_(n,h)) (g_(n+h)-g_n)`.

Since `theta'` is increasing,

`0 <= g_(n+h)-g_n <= pi h/theta'(g_n)`.

For a fixed prime `p`, the elementary chord bound

`|e^(-i a)-e^(-i b)| <= |a-b|`

therefore yields

`|exp(-i g_(n+h) log p)-exp(-i g_n log p)|`
` <= (pi h log p)/theta'(g_n)`.

Taking the maximum over `h<=H` and the fixed prime set proves the displayed `O(H/log g_n)` diameter bound. If `H_n=o(log g_n)`, that diameter tends to zero.

The Wasserstein statement is then immediate: couple every atom of `mu_(n,H)` to `z_n`. The transport cost is bounded by the block diameter, so

`W_1(mu_(n,H),delta_(z_n)) <= max_(h<=H) d_infty(z_(n+h),z_n)`.

The same estimate bounds the change of every `1`-Lipschitz visual statistic on this fixed torus.

## 2. The logarithmic Gram-count scale produces a local torus arc, not an automatic null escape

Suppose now that `H=O(log g_n)`. The previous bound gives

`g_(n+H)-g_n = O(1)`.

Across an `O(1)` height interval,

`theta'(xi_(n,h))-theta'(g_n) = O(1/g_n)`

uniformly in `h<=H`, because `theta''(t)=O(1/t)`. Since `theta'(g_n)~(1/2)log(g_n/(2 pi))`, this perturbation is negligible relative to `theta'(g_n)`. Returning to the mean-value identity gives uniformly

`g_(n+h)-g_n = [pi h/theta'(g_n)](1+o(1))`
`             = [2 pi h/log(g_n/(2 pi))](1+o(1))`.

Multiplying by each fixed `log p_j` shows that the phase cloud over `H=O(log g_n)` is governed, to first order, by a deterministic local flow whose velocity vector is

`-(2 pi/log(g_n/(2 pi))) (log p_1,...,log p_r)`.

Consequently the visual transition from a near-point cloud to an order-one arc occurs because the sampling mesh itself has spacing about `2 pi/log g_n`. It is not evidence that the Gram anchor has introduced a new prime-phase law.

This complements `VIS-083`. Globally, every fixed finite prime-phase field sampled over all Gram points is Haar-equidistributed. Locally, sufficiently short consecutive Gram blocks do the opposite: they collapse to their starting phase, and logarithmic-size blocks first trace a deterministic local arc. Global Haar behavior and local freezing are therefore compatible parts of the same sampling geometry.

## Prior art and novelty assessment

The Riemann-Siegel theta asymptotics and the resulting average Gram spacing are classical. The derivation above is only the mean-value-theorem consequence needed to expose the correct local visual null.

The global fixed-prime Gram-phase law is also established prior art. Antanas Laurinčikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`, works directly with Gram-point prime-phase coordinates and the weak-convergence input used in discrete universality; `VIS-083` records the corresponding fixed-finite-prime population obstruction.

A bounded targeted literature check did not identify a need to treat the sublogarithmic block-diameter estimate as a separate novelty claim. It is an elementary local-spacing corollary, and no novelty is claimed for it. The durable Mathia contribution is the **control boundary**: short-block visual clustering at Gram points must first be quotiented by this deterministic sampling geometry.

## Boundary and falsification

The result fixes the prime set before `n->infinity`. If the largest admitted prime grows with `n`, the factor `max_j log p_j` can offset the shrinking Gram spacing and a separate uniform analysis is required.

The collapse theorem concerns consecutive Gram points in **Gram-count blocks** with `H=o(log g_n)`. It does not classify blocks much longer than `log g_n`, nor does it prove equidistribution, mixing, discrepancy rates, or independence on any growing scale.

The local-arc expansion for `H=O(log g_n)` describes only the fixed-prime phase coordinates. It does not remove additional information carried by Gram occupancy, `Z(g_n)`, derivatives, nearby-zero geometry, or another independently supplied coordinate.

Falsify the result by breaking the standard eventual theta derivative asymptotics, the mean-value identity for Gram spacing, or the elementary phase chord bound. A proposed visual separator that uses this regime must additionally show that its effect survives subtraction or matching of the deterministic local arc rather than merely displaying the arc itself.

## Visual consequence

No canonical PNG is retained. In the sublogarithmic regime the exact diameter bound is stronger than a finite-height scatter plot, and at the logarithmic transition scale the first-order arc formula already predicts the visually salient geometry. Retaining a plot here would risk promoting deterministic sampling geometry into apparent evidence.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should be narrowed again. `VIS-083` closes Gram points as a positive external anchor for fixed-finite-prime **population** statistics; this result additionally closes **sublogarithmic consecutive Gram blocks** as a positive visual separator, because their prime-phase clouds are forced to freeze.

A surviving Gram-based short-window route must therefore operate outside this collapsed regime or use a statistic that explicitly removes the deterministic local arc and then demonstrates a residual not implied by the same fixed-prime sampling geometry. Growing prime support or genuinely additional Gram/zero coordinates remain different questions and require their own controls.