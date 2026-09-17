# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-derived sign theorem outside scalar shadows and universal enriched lifts

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation` through `MI-044-fixed-positive-scalarization-cannot-rescue-stationary-operator-valued-transport`.

WP-293--WP-330 close broad scalar, semigroup and operator-valued routes whose positivity is universal before the source-selective readout. WP-331--WP-332 give the opposite exact rigidity: a faithful UCP readout preserving the first two moments of the same self-adjoint source observable has zero Kadison defect and places that observable in the multiplicative domain.

WP-333--WP-338 expose and classify the moving-tail loophole. Strong convergence on bounded observables can coexist with order-one variance on a growing logarithmic coordinate. Rowwise `W_2^2` is exactly Kadison defect plus squared barycentric bias; every `W_p`, `p<2`, misses rare long jumps, while every `p>=2` controls them.

WP-339 extends that threshold to every scalar displacement penalty: uniform defect control under channel convergence is possible exactly when the tail cost eventually dominates the quadratic displacement. Any asymptotically subquadratic scalar cost admits an exact-barycentric rare-long-jump counterexample.

WP-340 classifies the stationary Hilbertian escape on one prime-power ray. A translation-invariant negative-type cost has quadratic growth only through an invariant Euclidean drift; the pure spectral/jump part is subquadratic.

WP-341 closes the direct **cross-prime stationary scalar** extension. On the full prime-exponent group `Gamma=direct_sum_p Z e_p`, let `L(alpha)=sum_p alpha_p log p` and let `psi` be a translation-invariant squared-Hilbert/CND cost. Its abelian Levy--Khinchin decomposition is a quadratic part `q` plus a positive spectral/jump part. Eventual control

`psi(alpha) >= a L(alpha)^2`

holds if and only if

`q(alpha) >= a L(alpha)^2`

for every `alpha`. Equivalently the arithmetic logarithm is already a bounded Hilbert covector of the quadratic sector; on each finite prime window the Gram matrix contains the rank-one PSD direction `a ell ell^T` with `ell_p=log p`. Cross-prime spectral coupling cannot synthesize the missing log-square from a softer stationary geometry.

WP-342 closes the immediate **stationary operator-valued plus fixed positive readout** escape. If `Psi:Gamma->A_sa` is stationary order-CND and `phi:A->C` is any fixed positive linear functional, then `psi_phi=phi circ Psi` is scalar CND. Therefore any eventual scalarized domination `psi_phi(alpha)>=aL(alpha)^2` is already subject to WP-341: the scalarized Levy--Khinchin quadratic sector must contain the arithmetic log-square, equivalently `L` must factor as a bounded Hilbert covector through that quadratic sector. States, traces and density-matrix expectations do not let operator-valued stationary transport synthesize the missing quadratic control after scalarization.

The remaining UCP route is therefore not to search for another scalar metric, a richer stationary Hilbert embedding, or an operator-valued stationary CND kernel whose Weil-facing observable is only a fixed positive linear scalarization. It must derive decay of the **quadratic logarithmic displacement energy** from genuinely source-specific arithmetic structure, exploit nonseparable operator positivity before scalarization, use a genuinely nonlinear/state-dependent readout with its own sign theorem, or leave the stationary commutative domain for a global/noncommutative coupling. Matched free-abelian controls reproduce WP-341--WP-342 for arbitrary weights, so operator notation and prime labels alone are not selective.

## Separate source fingerprint from source-selective sign

Shifted-lattice support, Mangoldt coefficients, prime-power gaps, exact scalar laws, dyadic realizations and the prime-exponent logarithm are source-specific fingerprints. WP-333--WP-342 show that the moving-tail variance obstruction, its sharp transport thresholds, and the fixed-positive-scalarization reduction remain generic probability/Hilbert/operator geometry even on intrinsic arithmetic coordinates. A valid sign mechanism must fail on an appropriate matched control, not merely carry the arithmetic log vector explicitly or hide it inside an operator-valued kernel.

## Match the topology to the moving observable without restating the target

The useful ledger remains channel error, barycentric bias, propagation geometry, scalarization/readout and the destination's moving quadratic scale. WP-339 says every scalar cost that universally closes the defect must already pay that quadratic scale; WP-340--WP-341 say stationary Hilbert geometry supplies it only through a genuine quadratic drift sector containing the relevant logarithmic direction; WP-342 says fixed positive scalarization of a stationary operator-valued CND cost inherits the same requirement. Future weighted graph, energy, operator-valued or noncommutative norms are useful only if an independent source theorem proves their control without merely inserting the desired log-square before the final readout.