# MI-025 — Uniformly transport-stable single-level geometry collapses before the polygon mesh scale

**Evidence level:** exact geometric/transport obstruction from [PC-309](../../findings/PC-309-transport-stable-prime-source-geometry-collapses-before-mesh-scale.md), extending the translated-source stability boundary in [PC-306](../../findings/PC-306-prime-polygon-centroid-is-algebraically-lossless-but-topologically-unstable.md)--[PC-308](../../findings/PC-308-ordinary-oriented-fourier-packets-have-a-linear-stability-threshold.md).

The canonical prime source and its one-step rotation are combinatorially maximally different—their discrete supports are disjoint—but the physical rotation moves every atom by only one polygon step. For every physical Wasserstein metric,

`W_p(nu_q,nu_q^+) <= 2 sin(pi/q) ~ 2 pi/q`.

Therefore any single-level observable with transport Lipschitz constant `L_q` separates this matched pair by at most `O(L_q/q)`. A fixed output margin forces `L_q=Omega(q)`. This is not a finite-Fourier-coordinate artifact: every uniformly transport-continuous geometry with `L_q=o(q)` collapses on the same source/control pair.

The full normalized logarithmic-potential field has an even more explicit boundary. Rotation covariance and the angular derivative of the logarithmic kernel give

`sup_(|z|<=r) |V_(nu_q^+)(z)-V_(nu_q)(z)| <= (2 pi/q) r/(1-r)`.

Hence the **entire two-dimensional interior field** becomes indistinguishable on every moving disk with `q(1-r_q)->infinity`. Retaining all interior values rather than finitely many Fourier modes does not restore stable source information before the boundary layer reaches the polygon mesh thickness `1/q`.

This places PC-308's linear-frequency major arcs at exactly the expected conditioning scale: characters with `k=Theta(q)` have physical Lipschitz norm `Theta(q)`. They can resolve one-step transport because they already spend mesh-scale angular sensitivity, after which the first stable witnesses are classical congruence resonances.

The remaining single-level escape is therefore necessarily singular. A proposed geometric carrier must enter a mesh-scale boundary layer, pay an explicitly diverging condition number of at least linear order, or use a topology discontinuous enough to resolve one-step transport. That cost is not automatically bad, but it must be **canonical and zero-sensitive rather than merely a decoder for the discrete source**. Genuinely cross-level/mixed-conductor constructions remain outside this obstruction because they are not functions of one source measure alone.

The reusable local audit is now simple: before treating a source geometry as a stable carrier, state its modulus with respect to physical transport and the smallest boundary layer it resolves. If its order-one discrimination requires `Omega(q)` sensitivity or `1/q` resolution, explain what arithmetic information appears there beyond the classical mesh/congruence data already classified by PC-308.

**Boundary.** PC-309 does not rule out singular boundary evaluation, mesh-scale operators with controlled diverging norm, nonlinear operations whose transport modulus is intentionally large, or mixed-conductor data. It proves only that uniformly transport-stable single-level geometry—including the complete normalized logarithmic potential away from the mesh layer—cannot retain a fixed margin against the matched one-step source rotation.