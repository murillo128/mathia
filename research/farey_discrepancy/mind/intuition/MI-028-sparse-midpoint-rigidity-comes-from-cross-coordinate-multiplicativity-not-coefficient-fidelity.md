# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, not near-extremal coefficient fidelity

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-178](../../findings/FD-178-variable-dyadic-blocks-hide-second-order-near-maximal-multiplicative-rank-fidelity.md).

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-178 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even an extremely deep coordinatewise approximation to the Möbius source.

For the dyadic ladder, FD-177 already constructs permanent deletion-only sources `a(n) in {0,mu(n)}` that agree with Möbius on every fixed subextremal fraction of the maximal squarefree-rank scale,

`omega(n) <= rho log n/loglog n`, `rho<1`,

while matching every sampled midpoint and modifying only `O(x^eta)` coefficients up to `x` for arbitrary `eta>0`.

FD-178 pushes the protected coordinate region through the leading extremal-rank scale. For every fixed `0<c<1`, one can still match every dyadic midpoint while preserving all sufficiently large squarefree coefficients satisfying

`omega(n) <= (log n/loglog n)(1 + c/loglog n)`,

with a deletion set of size `x^o(1)`. The construction uses variable-length dyadic repair blocks: increasing the block length makes the correction family grow slowly enough that only a vanishingly thin population of very high-rank composites is needed to absorb the rounding debt.

The reusable lesson is that **coordinate depth is not relational rigidity**. Even correctness through a second-order near-maximal multiplicative-rank window can leave enough rare high-rank coordinates to repair every sparse observation block. What the genuinely multiplicative source class supplies is a global product law tying those repair coordinates to prime data fixed earlier; separately correct coordinates do not reproduce that coupling.

This also changes how a prospective information lower bound should be formulated. Counting how many coefficients are fixed, how sparse the defect set is, or how close the protected rank is to the maximal scale does not measure the missing source information. The relevant resource is a cross-coordinate compatibility that prevents fresh-shell repair, or an observation family whose equations directly expose those compatible relations.

**Boundary.** FD-178 does not reach full squarefree-rank fidelity, prove a sharp second-order extremal endpoint, give pairwise sparse inversion, or improve the Franel--Landau destination estimate. The remaining coordinatewise escape is now pushed into an exceptionally thin near-extremal shell. The more structural target is to identify a compatibility weaker than full multiplicativity but strong enough to make block repair impossible, and then connect that source rigidity to the nonlocal RH-critical destination norm.