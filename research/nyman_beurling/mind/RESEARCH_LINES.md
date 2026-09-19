# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Replace population-only Ford control below linear source width by genuinely joint zero information

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-059-generic-strip-analyticity-does-not-cancel-the-transported-carrier`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, reconstruction cost and the exact analytic carrier. NB-218 shows that the Mellin-primitive tariff disappears when the source and kernel are kept coupled; NB-219--NB-221 remove localization and transport artifacts and identify the same leading carrier, a smooth convolution of `-zeta'/zeta`, for every fixed primitive depth.

NB-222 proves that generic bounded strip analyticity is exhausted: the contour factor `e^(-X eta)` is sharp for the exact carrier over that ambient function class. NB-223 then retains the actual zeta singularity spectrum. Its weighted zero sum

`sum_rho m(rho) e^(-X(1-beta)) (1+|gamma-t|)^(-A)`

combined with Bellotti's near-one zero-density theorem gives an order-one positive Euler gap throughout every fixed logarithmic margin below Ford height. For a fixed-width logarithmic shell, the exact Ford scale remained blocked by the final near-one zero layer.

NB-224 shows that this endpoint obstruction is resolution-dependent. Widen the source shell to `H=theta X`, normalized by `1/H`. The total positive source mass remains order one, while the Fourier carrier narrows to vertical width `Theta(1/X)`. Bellotti's local disk count then sees only `O(K)` zeros in a horizontal layer `R(1-beta)<=K`, and for a sufficiently small fixed Ford constant the positive-return defect stays bounded below all the way to the exact Ford denominator. The price is physical: the source spans roughly `e^X <= n <= e^((1+theta)X)`.

NB-225 proves that this linear shell width is not merely a convenient sufficient choice for the **current population-only mechanism**. At exact Ford scale `R~X`, every genuinely sublinear width `H=o(R)` permits an abstract packet of near-one zeros that is compatible simultaneously with the Vinogradov--Korobov zero-free depth, Bellotti's fixed and growing near-one density estimates, Bellotti's local `O(K)` disk count and ordinary local zero counting. The packet can be placed at spacing `Theta(1/X)` so that the moving-shell phases align, while its depth is chosen so the horizontal damping makes the total signed residue contribution order one.

Thus

`H=o(X)`

cannot be closed at exact Ford scale from the present population bounds alone. This is a logical insufficiency statement, not a claim that the actual zeta zeros realize the packet. Combined with NB-224 it makes `H=Theta(X)` the sharp width transition, up to constants, for what the present zero-free and population inputs can force without additional phase information.

The live source-side question is now narrower. To retain exact-Ford reach with fixed or sublinear logarithmic source width, prove information that couples horizontal depth to the `1/H` vertical window strongly enough to rule out the NB-225 packet, or prove cancellation in the signed residue sum from actual zeta-zero phase/correlation structure. Repackaging the same global and local population counts cannot cross this boundary.

## Keep source width, carrier width, zero population, phase coherence and destination resolution separate

The relevant currencies now include source total variation, logarithmic shell width `H`, multiplicative span `e^H`, transported carrier width `1/H`, zero-free contour width, horizontal zero depth, local zero counts at scale `1/R`, carrier phase, and any cancellation norm placed on the residue sum.

NB-222--NB-225 give a sharp hierarchy. Generic strip analyticity cannot improve the carrier scale. Zeta-specific population improves it almost to Ford for fixed-width shells. Local disk counts plus a log-wide shell reach exact Ford because the source deliberately buys vertical localization. NB-225 shows that every sublinear shell leaves enough unresolved vertical capacity for an order-one phase-aligned packet under those same population theorems.

A future source-side improvement must therefore pay for a **joint depth-window or phase theorem**, not another absolute count. A theorem at Ford height is not automatically stronger if it achieves that height by widening the source beyond the multiplicative resolution consumed by the Nyman--Beurling destination. Conversely, the sublinear-width no-go is only a method boundary for the present population information, not an obstruction to actual zeta phase cancellation.

This remains source-side information. NB-224--NB-225 do not themselves give a quantitative Nyman--Beurling distance theorem or prove that every good approximant realizes the positive Euler-return observable. Any destination claim must preserve that bridge explicitly.
