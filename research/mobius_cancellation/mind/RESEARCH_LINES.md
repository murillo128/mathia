# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Treat broad Hamming-window regularization and every sub-log-log radial truncation as classified

**Linked intuitions:** `MI-011-source-forced-prime-deformation-is-a-polynomial-information-channel` and `MI-012-hamming-regularization-is-degree-two-damping-before-the-square-root-transition`.

MC-097--MC-103 show that low-bias amplitude regularization is governed by positive low shells and a positive diagonal floor, while generic exact recovery from shrinking intervals is Chebyshev-ill-conditioned. MC-104 extends the obstruction to moving windows: interval location does not create a broad low-amplitude escape, and a critical-scale uniform window would already need width about `(log N)^(-1/2)` or smaller.

MC-105--MC-106 then expose the source-specific shell geometry. Every fixed shell of degree at least two has a positive Landau main term, consecutive shells grow strongly, and the same positive cascade persists uniformly through every cutoff `K_N=o(log log N)`. The hard endpoint cancellation is therefore absent from every sub-log-log radial truncation. The first unresolved radial regime is `Theta(log log N)`, unless a genuinely non-radial source relation bypasses shell truncation.

## Derive the signed relation at the first scale capable of carrying the endpoint

A survivor should either resolve the `Theta(log log N)` shell transition with enough uniform signed information to explain the endpoint, or identify a non-radial/cross-shell relation whose proof does not reduce to generic polynomial reconstruction. Fixed-order recurrences and finite Taylor data are now excluded by the shell cascade itself, not merely by conditioning.

## Keep comparator turnover and scale coverage explicit

Pointwise or narrow windows may still be useful when tied to a source-specific relation, but a per-scale witness is not an iterable theorem unless its location, conditioning, degree reach, and signed coupling remain controlled across the whole scale range. Any gain must survive both Chebyshev transfer cost and the positive shell cascade before it is credited as Möbius cancellation.
