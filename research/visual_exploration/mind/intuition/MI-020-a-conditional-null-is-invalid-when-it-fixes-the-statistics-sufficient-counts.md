# MI-020 — A conditional null must vary inside representation support; nuisance phase can be quotiented exactly

**Evidence level:** exact finite counting and representation-support obstruction from [VIS-232](../../findings/VIS-232-transition-conditioned-collision-controls-are-occupancy-degenerate.md) through [VIS-236](../../findings/VIS-236-ordered-prime-coordinate-cells-make-first-order-type-degenerate.md), sharpened by the exact origin-averaged pair-functional identity [VIS-237](../../findings/VIS-237-random-origin-cell-collisions-are-triangular-pair-functional.md).

For cell labels, the same-cell collision statistic is determined by occupancies, so any conditional surrogate preserving those occupancies has conditioned the statistic away. Exact first-order transition preservation is even more restrictive, and for actual ordered prime-coordinate cells the label sequence is nondecreasing, so the apparent lag-two Markov escape is also an occupancy functional. A null that introduces revisits/backtracking creates configurations outside the representation support.

VIS-237 shows how to remove a genuine representation nuisance without violating that support. For ordered points and cell width `ell`, average the same-cell collision count over a uniform grid origin. The result is exactly

`sum_(a<b) (1-|x_b-x_a|/ell)_+`.

Thus grid-origin randomization is not a new categorical or Markov null. It is an exact quotient of origin phase into a triangular two-point gap kernel. The statistic remains entirely determined by the ordered point configuration.

This sharpens the admission rule. First quotient representation nuisances when an exact invariant formulation exists. Then choose a stochastic/control law on the remaining **realizable geometric object**. Finally verify that the tested statistic is nondegenerate under that law and that any residual is not fixed by the conditioned sufficient statistics.

For the critical prime-coordinate cells, origin robustness should therefore be interpreted as evidence that the observable is really a local pair-gap functional, not as evidence of arithmetic significance. A prime-specific claim requires an independently specified ordered-point/gap baseline and a residual of the triangular statistic that cannot be explained by that baseline.

The reusable distinction is: **representation quotienting removes nuisance degrees of freedom; it does not manufacture source information.** A statistic may become cleaner and more stable after quotienting while remaining completely generic for ordered point sets.

**Boundary.** VIS-237 is an exact geometric identity, not a stochastic model of primes. It establishes no anomalous prime residual and no RH consequence. Different justified representations may admit other nondegenerate nulls, but any such null must stay inside their actual structural support rather than create artificial variability.