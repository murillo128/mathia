# Visual-exploration research lines

This file records current mathematical questions for the visual-exploration line. It is a mutable synthesis, not a task queue or history.

## Renormalize maximally fragmented Wang branches before declaring cross-fragment aggregation unavoidable

**Linked intuition:** `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-317--VIS-323 identify the faithful unimodular Wang coordinates, reduce each frozen branch to center-gap fixed-gap runs and show that aggregate singular-series cost is neutral at the first diagonal decomposition. VIS-324 then closes every polynomially long first-level run by the classical two-linear-form Selberg upper-bound sieve: at the natural scale, `k<=M^(1-delta)` already gives the required `L/log^2 M` occupancy scale.

VIS-325 changes the interpretation of the fully fragmented range `k>L`. With `k=|u-v|`, the same branch is, up to only `O(1)` determinant indices, the rational mechanical path of lower denominator `k` and slope `d/k`, where `|dm-ck|=1`. Its exact period monodromy is the diagonal vector `(sigma,sigma)`. Thus the apparent singleton fragmentation is a failure of the **first diagonal period representation**, not a proof that the observed path has no deeper repeated structure.

The live question is now whether the continued-fraction/Christoffel hierarchy of `d/k` exposes a shorter primitive direction with enough repetition for the two-prime sieve, or whether the complementary nonrepetitive regime admits a direct discrepancy/energy estimate once the Wang taper is included. Cross-fragment aggregation remains a plausible destination, but it should be invoked after this exact lower-denominator renormalization rather than because `k>L` looks pointwise in the first coordinate system.

## Keep arithmetic dimension, center gap, representation denominator, run length, aggregation and taper together

The first-level center-gap decomposition and the denominator-`k` mechanical representation describe the same branch at different resolutions. When `k<=L`, complete periods are visible and fixed-gap runs are the natural unit. When `k>L`, VIS-325 proves that the branch still carries an exact lower-denominator rational word up to bounded error, but it does not prove that continued-fraction iteration creates a long sieveable block.

Future work must preserve the two-prime local factor and final destination taper while changing representation. A large partial quotient may create many repeats of a shorter Christoffel block; a bounded-type regime may instead favor an energy/discrepancy estimate. Either mechanism must ultimately be priced against the weighted Wang occupancy target. Mechanical renormalization is structural simplification, not arithmetic cancellation by itself.