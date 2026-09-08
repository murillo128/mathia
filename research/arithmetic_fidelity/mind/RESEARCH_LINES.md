# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Declare quotient, source complexity, observation algebra, and bandwidth together

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-188 show that exact sufficiency and stable inversion are different questions. Adaptive positive source clusters can remain exactly separated while derivative-limited observations become super-algebraically close, yet the same controls become visible once the Euler harmonic ladder is resolved. The logarithmic Rayleigh window carries a continuum of algebraic fidelity exponents rather than a binary visible/invisible transition.

AF-189--AF-194 sharpen that scale dependence into an overlap/saddle hierarchy. The finite-overlap theta regime and the growing-overlap saddle agree logarithmically across a wider window than they agree multiplicatively, and AF-193 isolates the first correction parameter `q^4/m^3`: leading theta asymptotics become multiplicatively valid only beyond the sharper `m >> q^(4/3)` scale. A recovery theorem must therefore state not only a nominal resolution scale but the accuracy notion in which adjacent asymptotic descriptions are being identified.

The live problem is a source-class lower recovery theorem or kernel-specific converse that matches these exact controls. Neither exact infinite-bandwidth sufficiency, a derivative envelope, nor one leading asymptotic profile determines the inverse scale by itself.

## Solve the Peano B-spline knot extremal before calling a moment-flat stencil sharp

AF-195 removes coefficient freedom on `m+1` distinct nodes: the unique minimal-support signed control annihilating degrees below `m` is the divided-difference functional. AF-196--AF-197 then show that equispaced parity geometry is not extremal at fixed `W_1`, and AF-198 closes the cheapest quartic escape: the mirror-symmetric five-node optimizer is a strict local minimum even under unrestricted asymmetric perturbations modulo scale. Any better five-node control must lie in a genuinely separate basin.

AF-199 identifies the general object behind those order-by-order rational optimizations. The normalized minimal-support control is the `m`th distributional derivative of one nonnegative Peano B-spline `B_u`, and its scale-free leading response is exactly

`Q_m = (m!/2^(m-1)) ||D^m B_u||_TV^(m-1) / ||B_u^(m-1)||_1^m`.

Thus the free-node source problem is a sharp variable-knot spline derivative-norm inequality. The equispaced/cardinal spline gives the baseline constant, but AF-196--AF-197 already prove that it is not the knot extremizer for `m=3,4`.

The live theorem is to determine the sharp Peano-spline constant and its extremizing knot shapes, or to exhibit a nonlocal asymmetric competitor below the AF-198 quartic basin. A regularity-only recovery lower bound should not treat one convenient stencil as extremal until this restricted spline optimization has been solved or explicitly bounded.

## Keep provenance and endpoint sufficiency separate from conditioning

A representation can be exactly sufficient yet lose source identity after quotienting, or preserve provenance while becoming badly conditioned on an expanding source class. Recovery claims should state separately what is reconstructible, which equivalences are harmless, and at what quantitative cost the inverse remains stable.
