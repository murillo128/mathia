# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Replace population and fixed-power phase control below linear source width by genuinely joint depth-phase information

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-060-fixed-power-phase-cancellation-is-not-enough-at-the-ford-boundary`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, reconstruction cost and the exact analytic carrier. NB-218 shows that the Mellin-primitive tariff disappears when the source and kernel are kept coupled; NB-219--NB-221 remove localization and transport artifacts and identify the same leading carrier, a smooth convolution of `-zeta'/zeta`, for every fixed primitive depth.

NB-222 proves that generic bounded strip analyticity is exhausted: the contour factor `e^(-X eta)` is sharp for the exact carrier over that ambient function class. NB-223 then retains the actual zeta singularity spectrum. Its weighted zero sum combined with Bellotti's near-one zero-density theorem gives an order-one positive Euler gap throughout every fixed logarithmic margin below Ford height.

NB-224 shows that the endpoint obstruction is resolution-dependent. Widen the source shell to `H=theta X`, normalized by `1/H`; the Fourier carrier narrows to vertical width `Theta(1/X)`, and Bellotti's local disk count then reaches the exact Ford denominator. The price is physical: the source spans roughly `e^X <= n <= e^((1+theta)X)`.

NB-225 proves that this linear shell width is the sharp transition for the **current population-only mechanism**. At exact Ford scale `R~X`, every genuinely sublinear width `H=o(R)` permits an abstract near-one zero packet compatible with the Vinogradov--Korobov zero-free depth, Bellotti's fixed and growing density estimates, Bellotti's local disk count and ordinary local zero counting. Its moving-shell phases can be aligned while its horizontal depth is tuned so the signed residue remains order one.

NB-226 shows that replacing alignment by a generic phase-cancellation hypothesis still does not cross the boundary. For every fixed `0<vartheta<1`, the matched packet can be arranged so that **every consecutive vertical subpacket** of `m` zeros satisfies a deterministic bound `O(m^vartheta)` while the weighted signed residue remains order one. Square-root cancellation is therefore insufficient. The packet simply moves horizontally until its damping `e^(-YD)` compensates the allowed `M^vartheta` phase bias.

The live source-side question is now precise: prove a theorem that couples horizontal depth to vertical phase strongly enough that

`e^(-YD) |sum e^(iX(gamma-t))| = o(1)`

uniformly on the packets admitted by the population bounds, or control the actual residue-weighted sum directly. Equivalent useful inputs include a joint depth-window density theorem or a depth-sensitive phase estimate whose saving strengthens as zeros move left. Another absolute count, or a fixed-power bound for raw phases independent of depth, cannot close a sublinear Ford shell.

## Keep source width, carrier width, zero population, phase coherence and horizontal depth separate

The relevant currencies now include source total variation, logarithmic shell width `H`, multiplicative span `e^H`, transported carrier width `1/H`, zero-free contour width, horizontal zero depth, local zero counts at scale `1/R`, raw carrier phase, depth-sensitive phase cancellation, residue weights, and any cancellation norm placed on the zero sum.

NB-222--NB-226 give a sharp hierarchy. Generic strip analyticity cannot improve the carrier scale. Zeta-specific population improves it almost to Ford for fixed-width shells. Local disk counts plus a log-wide shell reach exact Ford because the source buys vertical localization. Every sublinear shell leaves enough vertical capacity for an order-one matched packet, and NB-226 shows that the same packet can satisfy any fixed positive power cancellation law by trading the remaining phase bias against horizontal damping.

A future source-side improvement must therefore pay for a **joint depth-window/phase theorem**, not another absolute count and not an unweighted random-phase heuristic. A theorem at Ford height is not automatically stronger if it achieves that height by widening the source beyond the multiplicative resolution consumed by the Nyman--Beurling destination. Conversely, the sublinear-width no-go remains a method boundary for the audited information, not an obstruction to actual zeta phase-depth correlations.

This remains source-side information. NB-224--NB-226 do not themselves give a quantitative Nyman--Beurling distance theorem or prove that every good approximant realizes the positive Euler-return observable. Any destination claim must preserve that bridge explicitly.
