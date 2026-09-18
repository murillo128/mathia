# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Match reverse discrimination to the actual endpoint channel, conductor scale and bias amplitude

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-066-quadratic-boundary-carries-macroscopic-inverse-root-rank-bias`.

MC-366--MC-369 show that endpoint discrimination depends jointly on provenance and physical resolution. Coordinate queries and parity sketches have exact source-revealment tariffs; an exact-real shell bias can nevertheless encode the whole sign vector through subset sums; and a nearest-Hamming-shell quotient removes those address bits under the sharp `l1` condition `||d-R^(-1)1||_1<1/R`.

MC-370 adds a genuinely softer stability regime. Writing `d_i=1/R+epsilon_i`, average Hamming-shell dephasing remains asymptotically complete under an `l2` defect bound of order `1/(R^2 log R)`, even when worst-case `l1` shell decoding is unavailable. Pointwise finite-resolution recovery and average energy stability are therefore different endpoint resources.

MC-371--MC-375 move the bottleneck from coefficient balance to primitive source conductor. The quartic common-source floor survives without equal defect cells and forces source-incidence balance in the saturated regime. MC-372 shows that central Hamming modes already demand quadratic conductor on average. MC-373 makes the Burgess input effective with a moving order close to that quadratic boundary, and MC-374 upgrades the scalar bias argument to a frame-rank theorem: only `O(R/Delta)` modes can have primitive conductor below the near-quadratic threshold `y^(2-Delta)`. Under quartic saturation, almost every central mode has minimum primitive conductor exponent tending to two.

MC-375 extends that saturation from the middle layer to almost the entire Fourier cube. The exact Walsh variance identity for package conductors forces source log mass to delocalize across an increasing number of incidence signatures, while the earlier half-loading theorem keeps that mass concentrated near central Hamming weight. A quartic-efficient endpoint is therefore simultaneously **Hamming-central and incidence-delocalized**.

MC-376 adds the missing amplitude statement at this conductor boundary. The endpoint coefficients obey exact second and fourth moment laws; a Paley--Zygmund argument then forces at least a fixed positive fraction of modes to have bias of size at least `sqrt(S_2/2)`, hence at least `1/sqrt(2R)`. Combining this with MC-375 shows that asymptotically a positive fraction of the entire Fourier cube simultaneously has minimum primitive conductor `y^(2+o(1))` and macroscopic inverse-root-rank endpoint bias. The expensive boundary is therefore populated by many quantitatively visible modes, not by a negligible exceptional set.

This closes the hoped-for escape in which most central endpoint modes secretly admit cheap primitive representatives or become negligible at the quadratic boundary. The live arithmetic question is now sharper: identify a source theorem or endpoint observable that controls a macroscopic family at near-quadratic conductor with bias at least inverse-root-rank, or find a different invariant that does not require resolving those modes one by one. A theorem about one exceptional mode, a fixed positive bias threshold, or generic information below quadratic conductor will not address the current obstruction.

## Keep resolution, average stability, source incidence, conductor and bias scale distinct

The current resource ledger separates exact-real subset-sum conditioning, finite-resolution Hamming quotienting, `l1` worst-case shell displacement, `l2` average dephasing stability, source-incidence balance, incidence-signature delocalization, package conductor, minimum primitive conductor and endpoint bias amplitude. These are not interchangeable.

In particular, near-uniform cell masses do not by themselves remove exact-real address information, while conductor saturation does not by itself prove Möbius cancellation. MC-376 prevents a different shortcut: one cannot dismiss the quadratic-conductor population as quantitatively invisible. The endpoint argument must state which quotient is physically observed, which family of modes is needed by the destination, and whether the acquisition mechanism can access their near-quadratic source conductors with the required sign and inverse-root-rank amplitude.

## Repair probabilistic comparators only after exact-stratum and algebraic-collapse gates

Probabilistic proxies remain secondary until their conditioning is arithmetically consistent and their observables survive exact multiplicative simplification. A model that becomes degenerate after conditioning on an exact arithmetic stratum, or whose auxiliary statistic collapses algebraically to `M(x)`, has not created an independent cancellation mechanism. The conductor-and-amplitude results sharpen that gate: a plausible comparator must reproduce the central/delocalized source-incidence geometry and the macroscopic inverse-root-rank population at quadratic primitive conductor rather than hiding the endpoint cost in cheap or vanishing representatives.
