# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Separate exact-Ford reach from fixed-width multiplicative resolution

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-059-generic-strip-analyticity-does-not-cancel-the-transported-carrier`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, reconstruction cost and the exact analytic carrier. NB-218 shows that the Mellin-primitive tariff disappears when the source and kernel are kept coupled; NB-219--NB-221 remove localization and transport artifacts and identify the same leading carrier, a smooth convolution of `-zeta'/zeta`, for every fixed primitive depth.

NB-222 proves that generic bounded strip analyticity is exhausted: the contour factor `e^(-X eta)` is sharp for the exact carrier over that ambient function class. NB-223 then retains the actual zeta singularity spectrum. Its weighted zero sum

`sum_rho m(rho) e^(-X(1-beta)) (1+|gamma-t|)^(-A)`

combined with Bellotti's near-one zero-density theorem gives an order-one positive Euler gap throughout every fixed logarithmic margin below Ford height. For a fixed-width logarithmic shell, the exact Ford scale remained blocked by the final near-one zero layer.

NB-224 shows that this endpoint obstruction is **resolution-dependent**. Widen the source shell from fixed logarithmic width to `H=theta X`, normalized by `1/H`. The total positive source mass remains order one, while the Fourier carrier narrows vertically from width `Theta(1)` to `Theta(1/X)`. Bellotti's local disk count then sees only `O(K)` zeros in a horizontal layer `R(1-beta)<=K`, rather than paying the generic `Theta(log |t|)` population of a unit vertical window.

At the exact Ford regime `X/R=Theta(1)`, this narrower carrier is enough: for sufficiently small fixed Ford constant `kappa_0`, the positive-return defect stays bounded below uniformly for

`1 <= |t| <= exp(kappa_0 X^(3/2)/(log X)^(1/2))`.

Thus the Ford denominator itself is no longer the source-side barrier once proportional logarithmic width is allowed. The price is physical resolution. The source now spans roughly

`e^X <= n <= e^((1+theta)X)`,

so NB-224 does not solve the fixed-width endpoint left by NB-223.

The live question is therefore sharper than “reach Ford scale.” It is to determine the **width-versus-height tradeoff** and whether the fixed-width or sublinear-width source can recover the same local-zero-count gain without losing multiplicative resolution. A useful theorem should quantify how the carrier width `1/H` interacts with local zero counts at `X/R=Theta(1)`, identify the smallest admissible growth of `H`, or show that fixed width requires genuinely new zero-phase cancellation rather than population bounds.

## Keep source width, carrier width, zero population and destination resolution separate

The relevant currencies now include source total variation, logarithmic shell width `H`, multiplicative span `e^H`, transported carrier width `1/H`, zero-free contour width, the zero-residue weight `e^(-X(1-beta))`, local zero counts at scale `K/R`, and any phase-sensitive cancellation norm placed on the zero sum.

NB-222--NB-224 give a clean hierarchy. Generic strip analyticity cannot improve the carrier scale. Zeta-specific near-one population improves it almost to Ford for fixed-width shells. Local disk counts plus a log-wide shell reach exact Ford because the source deliberately buys much finer vertical localization. That gain is genuine, but it is not free: the physical source resolution degrades exponentially in the shell width.

A future source-side improvement should therefore be judged after both sides of this uncertainty trade are stated. A theorem at Ford height is not automatically stronger if it achieves that height by widening the source beyond the resolution consumed by the Nyman--Beurling destination. Conversely, a fixed-width obstruction is not a universal Ford obstruction if widening the source removes it.

This remains source-side information. NB-224 does not itself give a quantitative Nyman--Beurling distance theorem or prove that every good approximant must realize the positive Euler return observable. Any destination claim must preserve that bridge explicitly.