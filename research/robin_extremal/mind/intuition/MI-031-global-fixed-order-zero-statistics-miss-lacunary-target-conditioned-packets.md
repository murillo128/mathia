# MI-031 — Global fixed-order zero statistics can miss lacunary target-conditioned packets

**Evidence level:** exact matched-control blindness theorem from [RE-152](../../findings/RE-152-global-gue-statistics-are-blind-to-lacunary-one-sided-vertical-escape.md), built on the corrected one-sided packet of RE-151.

Start from any critical-line background with Riemann--von Mangoldt main counting and standard local `O(log T)` occupancy. RE-152 inserts a lacunary sequence of off-critical packet stages whose cumulative population is only `O(log T)`, so the classical counting scale and local unit-interval occupancy remain intact.

For every fixed order `k` and compactly supported test function, the inserted stage affects a random-translation correlation average only when the translation center falls in a window of width `O(1/log T)` around that stage. Its `O(log T)` local multiplicity then contributes only

`O((log T)^(k-1)/T)=o(1)`.

Thus all fixed-order globally averaged local-correlation limits, bounded local observables and fixed local-count moments can be inherited unchanged from the background, while the exceptional stages still realize RE-151's one-sided scale-maximal Robin hiding mechanism.

The quantifier mismatch is the key point. Global GUE-type statistics describe typical translation centers; the Robin obstruction selects a deliberately exceptional target stage. Even an entire hierarchy of fixed-order averaged laws does not become a uniform statement around every sufficiently high target. Closing this channel needs a stronger source theorem: a local law uniform at all relevant targets, a large-deviation estimate strong enough to eliminate every exceptional center, or an explicit-formula/Euler-product relation that prices the packet phase geometry directly.

**Boundary.** The construction is a matched control and inherits only the corrected one-sided Robin obstruction. It does not show that actual zeta zeros contain such lacunary packets, and it does not close the symmetric observation window. The result is blindness of global fixed-order averaging to a permitted exceptional geometry, not evidence against GUE behavior of zeta zeros.