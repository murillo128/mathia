# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Declare quotient, source complexity, localization, observation algebra, and bandwidth together

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-188 show that exact sufficiency and stable inversion are different questions. Adaptive positive source clusters can remain exactly separated while derivative-limited observations become super-algebraically close, yet the same controls become visible once the Euler harmonic ladder is resolved. The logarithmic Rayleigh window carries a continuum of algebraic fidelity exponents rather than a binary visible/invisible transition.

AF-189--AF-194 sharpen that scale dependence into an overlap/saddle hierarchy. The finite-overlap theta regime and the growing-overlap saddle agree logarithmically across a wider window than they agree multiplicatively, and AF-193 isolates the first correction parameter `q^4/m^3`: leading theta asymptotics become multiplicatively valid only beyond the sharper `m >> q^(4/3)` scale.

AF-200 adds an independent source-side gate. Even at fixed positive `W_1`, fixed quartic cancellation order, minimal five-node support, and a fixed finite Euler band, a mirror-symmetric source can send almost all of its Peano carrier to `+infinity` and make the observation discrepancy tend to zero. The exact carrier barycenter and `W_1(B,delta_x)` expose the missing resource directly: **equicoercive Peano-carrier localization** is not implied by source transport distance.

The live problem is therefore a source-class lower recovery theorem or kernel-specific converse that states the quotient, source-complexity growth, carrier tightness/localization, bandwidth, and approximation strength together. Exact infinite-bandwidth sufficiency, a derivative envelope, `W_1` separation, or one leading asymptotic profile does not determine the inverse scale by itself.

## Solve the Peano B-spline knot extremal only inside a declared localization class

AF-195 removes coefficient freedom on `m+1` distinct nodes: the unique minimal-support signed control annihilating degrees below `m` is the divided-difference functional. AF-196--AF-197 then show that equispaced parity geometry is not extremal at fixed `W_1`, and AF-198 closes the cheapest quartic escape: the mirror-symmetric five-node optimizer is a strict local minimum even under unrestricted asymmetric perturbations modulo scale. Any better five-node control must lie in a genuinely separate basin.

AF-199 identifies the general object behind those order-by-order rational optimizations. The normalized minimal-support control is the `m`th distributional derivative of one nonnegative Peano B-spline `B_u`, and its scale-free leading response is exactly `Q_m = (m!/2^(m-1)) ||D^m B_u||_TV^(m-1) / ||B_u^(m-1)||_1^m`.

AF-200 shows why this homogeneous extremal is not automatically the full Euler extremal: the Peano carrier itself can escape to a region where the fixed-band kernel is exponentially insensitive. Determine the sharp variable-knot spline constant and extremizing shapes **together with** the weakest localization/equicoercivity condition that lets the homogeneous asymptotic control the actual observation. A sharp `Q_m` constant without that gate is not a source-class recovery theorem.

## Keep provenance and endpoint sufficiency separate from conditioning

A representation can be exactly sufficient yet lose source identity after quotienting, or preserve provenance while becoming badly conditioned on an expanding source class. Recovery claims should state separately what is reconstructible, which equivalences are harmless, and at what quantitative cost the inverse remains stable.
