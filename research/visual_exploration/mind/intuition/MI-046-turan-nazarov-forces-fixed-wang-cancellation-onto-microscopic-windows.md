# MI-046 — Turán--Nazarov forces fixed Wang cancellation onto microscopic windows

**Evidence level:** exact harmonic-analysis synthesis from [VIS-346](../../findings/VIS-346-turan-nazarov-short-window-obstruction.md), extending the fixed-bank moment obstructions of VIS-343--VIS-345 with classical Turán--Nazarov propagation. This is a fixed-bank multiplier obstruction, not a source-specific estimate for the theta remainder.

For a fixed translated Wang bank with `B` active phase fibers, short-window cancellation cannot be treated as a free escape from the fiberwise moment equations. After lower moments vanish, each next asymptotic order is a fixed exponential polynomial in the translation phases. A phase-resolving reference interval gives a coefficient-scale lower bound, and Turán--Nazarov propagates that nontriviality into any shorter subwindow.

If the bank satisfies `sup_(J_X)|M|=O(X^-r)` on windows of length `ell_X`, then a nonzero `k`-th moment vector with `B_k` active phase fibers requires

`X*min(ell_X,1)^(B_k-1)=O(1)`.

Consequently, the coarse fixed-bank condition `X*min(ell_X,1)^(B-1)->infinity` forces the same fiber moments through order `r-1` to vanish. For power-law windows `ell_X=X^-alpha`, escaping this obstruction requires at least `alpha>=1/(B-1)` at the coarse level.

This turns “use a shorter moving window” into a quantitative resource claim. **A fixed bank can avoid the asymptotic moment cost only by concentrating its cancellation on windows microscopic enough relative to its active phase count.** That scale is merely where the present obstruction stops; it is not evidence that useful cancellation exists there.

The surviving mechanisms must therefore change something substantive: let phase count or spacing vary with scale, use growing/coalescing banks, permit adaptive or frequency-dependent coefficients, or exploit signed arithmetic structure of the normalized theta remainder `G` rather than uniform scalar-multiplier smallness. Every such route still has to expose coefficient conditioning, finite-frequency leakage and the downstream derivative repayment.

**Boundary.** The Turán--Nazarov threshold is a necessary escape condition for the stated fixed finite bank, not a sharp construction theorem. VIS-346 does not rule out ultra-shrinking windows at or below that scale, scale-dependent phase geometry, adaptive coefficients, infinite expansions or direct source cancellation. No PNT or RH improvement follows from the localization bound.