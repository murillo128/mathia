# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Declare quotient, source complexity, observation algebra, and bandwidth together

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-188 show that exact sufficiency and stable inversion are different questions. Adaptive positive source clusters can remain exactly separated while derivative-limited observations become super-algebraically close, yet the same controls become visible once the Euler harmonic ladder is resolved. The logarithmic Rayleigh window carries a continuum of algebraic fidelity exponents rather than a binary visible/invisible transition.

AF-189--AF-194 sharpen that scale dependence into an overlap/saddle hierarchy. The finite-overlap theta regime and the growing-overlap saddle agree logarithmically across a wider window than they agree multiplicatively, and AF-193 isolates the first correction parameter `q^4/m^3`: leading theta asymptotics become multiplicatively valid only beyond the sharper `m >> q^(4/3)` scale. A recovery theorem must therefore state not only a nominal resolution scale but the accuracy notion in which adjacent asymptotic descriptions are being identified.

The live problem is a source-class lower recovery theorem or kernel-specific converse that matches these exact controls. Neither exact infinite-bandwidth sufficiency, a derivative envelope, nor one leading asymptotic profile determines the inverse scale by itself.

## Optimize the geometry of matched controls before treating one stencil as extremal

AF-195 identifies the unique minimal-support signed control annihilating all polynomials below a prescribed order through divided-difference weights. AF-196 and AF-197 then show that the familiar equispaced parity geometry is not extremal once node locations are allowed to vary at fixed Wasserstein separation: already in the first free-node cubic case, and again in the mirror-symmetric quartic family, nonequispaced controls reduce the first surviving moment response.

Thus moment cancellation order and support size do not determine the strongest recovery obstruction. The source geometry itself is an optimization variable. Future regularity-only lower bounds should either solve the relevant node/weight extremal problem on the admitted source class or state explicitly that the chosen stencil is only a witness, not a sharp barrier.

## Keep provenance and endpoint sufficiency separate from conditioning

A representation can be exactly sufficient yet lose source identity after quotienting, or preserve provenance while becoming badly conditioned on an expanding source class. Recovery claims should state separately what is reconstructible, which equivalences are harmless, and at what quantitative cost the inverse remains stable.
