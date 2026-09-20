# Visual-exploration research lines

This file records current mathematical questions for the visual-exploration line. It is a mutable synthesis, not a task queue or history.

## Move the Wang frontier out of the maximally fragmented regime

**Linked intuition:** `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-317--VIS-324 identify faithful unimodular Wang coordinates, reduce frozen branches to fixed-gap affine runs and close every polynomially long first-level run with the classical two-linear-form Selberg upper-bound sieve. VIS-325--VIS-327 then show that the fragmented range `k>L` has a lower-denominator mechanical-word description and that a short nondegenerate Christoffel parent simultaneously buys visible repetition and a small resultant/conductor.

VIS-328 removes the remaining dependence on a short first parent. For any denominator-`k` slope, the determinant-`k` approximation lattice contains a nonzero vector `(s,e)` with `s,|e|=O(sqrt(k))` by Minkowski. An `s`-step has one constant Wang displacement except at at most `|e|` edges, so the observed branch splits into at most `s+|e|` affine runs. The same vector controls both the primitive two-prime step and the resultant, and the only axis-degenerate vectors lie on an explicit long ray that the Minkowski vector misses at the natural same-shell scale.

At `L asymp M/log log M` with `k>L`, this gives `s+|e|=O(sqrt(M))=o(L)`, a polynomial-size conductor and a dimension-two Selberg bound with excess only `O((log log M)^2)`. That is inside the final taper budget. **The entire maximally fragmented range `k>L` is therefore closed as a Wang occupancy obstruction**, including the previous `J=1` axis-parent case.

The live branchwise frontier has moved to the near-maximal but non-fragmented transition

`k<=L`, `k=M^(1-o(1))`,

where phases can repeat and the denominator-`k` bounded-error replacement used by VIS-328 no longer applies in the same form. The next exact question is whether an analogous short nondegenerate packet survives once `L` reaches/exceeds `k`, or whether the repeated-phase geometry should instead be treated by discrepancy/energy aggregation.

## Keep finite-window repetition, arithmetic dimension, conductor and the taper destination coupled

VIS-328 strengthens the renormalization lesson. A useful packet need not be a canonical continued-fraction parent; it is enough that one short Diophantine vector simultaneously bounds exceptional edges, preserves two prime coordinates, controls the affine step/resultant and repeats often enough inside the actual observation window. Minkowski supplies such a packet throughout `k>L`.

Future work should not keep descending the Christoffel hierarchy in a regime that is already closed. It should target only `k<=L` with near-maximal `k`, carrying phase repetition, packet length, arithmetic dimension, local factors and final taper through the same finite-window estimate.