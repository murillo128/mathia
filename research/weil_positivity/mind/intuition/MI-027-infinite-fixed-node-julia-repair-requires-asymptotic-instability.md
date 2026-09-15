# MI-027 — Infinite fixed-node Julia repair requires asymptotic instability

**Evidence level:** exact asymptotic-stability obstruction from [WP-313](../../findings/WP-313-asymptotically-stable-infinite-julia-chains-retain-mangoldt-gamma-sign-defect.md), extending the finite fixed-boundary obstruction of [WP-312](../../findings/WP-312-fixed-boundary-julia-nevanlinna-reduction-cannot-repair-gamma-asymptotic.md)

Passing from a finite to an infinite Julia--Nevanlinna chain does not by itself remove the Mangoldt--Gamma mismatch. The relevant question is whether the chain limit preserves the high-energy coefficient that detects the mismatch.

For a unit-log Pick function, remove the arbitrary real translation and measure first the `log(y)/y` defect `L`; when `L=0`, measure the `y^-2` curvature `C`. The reflected Mangoldt source begins with

`L(m_-)=0`, `C(m_-)=A_M>0`,

whereas the Riemann Gamma channel has

`L(Gamma_R)=0`, `C(Gamma_R)=-1/24`.

Every normalized regular fixed-real-node Julia reduction adds a positive amount to the first defect. Starting from the Mangoldt source,

`L(f_N)=pi sum_regular 1/d_j`.

Thus one regular reduction is enough: from its first occurrence onward every finite stage has a strictly positive `L`, with no cancellation channel inside reduction-only fixed-node dynamics.

If the chain contains no regular reduction and only strips Mangoldt poles, then `L` remains zero but

`C(f_N)=A_M + sum_{n in S_N} Lambda(n)log n/(n+1)`.

Every increment is positive. A sparse infinite removal can converge only to a curvature still at least `A_M`; exhaustive removal diverges to `+infinity`, already because the prime contribution grows like `(1/2)(log X)^2`.

Therefore an infinite fixed-node chain can reach the Gamma asymptotic only if the infinite-stage limit is **not stable at the discriminator scale**. Local uniform convergence on the upper half-plane is insufficient. The surviving scalar possibility requires a genuine noncommutation between chain depth and high energy: the defect must be pushed outward in `y` as the depth grows so that

`lim_N lim_y` and `lim_y lim_N`

do not agree for `L` or `C`.

This makes the remaining escape precise. A moving boundary layer, scale-dependent reference, or source-forced moving-node mechanism could in principle evade the theorem, but the nonuniformity must itself be derived rather than chosen to cancel the known Gamma defect. Merely proving convergence of an infinite Schur/Julia algorithm no longer addresses the obstruction.

**Boundary.** This is a reduction-only result for fixed real Julia nodes under convergence strong enough to transport the relevant high-energy invariant. It does not rule out moving nodes, augmentation with independently fixed source parameters, operator/matrix-valued boundary data, generalized resolvents, or another mechanism that changes the finite--archimedean geometry before scalar comparison.