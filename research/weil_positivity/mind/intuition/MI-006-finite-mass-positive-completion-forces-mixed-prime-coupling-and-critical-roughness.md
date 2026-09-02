# MI-006 — Finite-mass positive completion forces mixed-prime coupling and critical roughness

**Evidence level:** proved for the exact-cover prime-torus completion class and its standard product-coordinate regularity tests

## Core intuition

The critical one-prime Weil rays can live inside a finite positive all-prime carrier, but not as an isolated sparse positive sector. Positivity must be paid for with mixed-prime correlations, and the most natural positive operations cannot later erase those correlations while preserving the prime coordinates. Even when correlations are engineered strongly enough to restore equivalence with product Haar measure, the exact critical rays force the resulting state below standard first-order product-coordinate regularity.

The durable lesson is not that positivity fails. It is that **positive completion changes both the interaction support and the regularity category**. A global Weil mechanism must explain those changes geometrically rather than treat the mixed modes as disposable bookkeeping.

## Strongest justified principle

WP-096 gives the sparse obstruction. Exact cover covariance turns a finite positive scalar form into a positive measure on the infinite prime torus. If only the exact one-prime Weil rays are retained and every mixed-prime Fourier coefficient is set to zero, positivity forces diagonal mass

`C >= 2 sum_{p in P} (log p)/(sqrt(p)-1)`

on every finite prime set, hence no all-prime finite-mass sparse positive carrier exists.

WP-097 shows that this is not an obstruction to positivity itself. Allowing mixed-prime Fourier coefficients gives an explicit positive product completion with the exact one-prime rays and a sharp finite mass `C_*`; the mixed terms are precisely what pays for positivity.

WP-098--WP-099 close two canonical ways of deleting that completion afterwards. A unital positive map on the same prime-torus algebra that keeps every coordinate unitary lies in the multiplicative domain and therefore keeps all their products; the exact first-order Fourier projector that kills mixed modes is not positivity-preserving. Enlarging by an arbitrary positive auxiliary sector and passively eliminating it through a Schur complement/shorting also fails: the reduced form is dominated by the original finite-mass form, whereas a positive sparse output requires an ever larger diagonal budget. If the diagonal is preserved exactly, the passive reduction is rigid and cannot change any coefficient.

WP-100--WP-101 classify the first regularity escape. The independent product completion is Kakutani-singular to product Haar exactly at and below the critical exponent `sigma=1/2`. But this singularity is not correlation-invariant: a correlated countable block mixture at the sharp mass can be equivalent to Haar while preserving every exact one-prime ray. The cost is endpoint roughness: every absolutely continuous critical completion lies outside `L(log L)^(1/2)`, hence outside every `L^(1+epsilon)`.

WP-102 supplies a correlation-robust boundary. For **any** finite positive completion with first coordinate moments `-(log p)p^(-sigma)`, every finite marginal has cylindrical Fisher energy at least

`C^(-2) sum_{p in P} (log p)^2 p^(-2 sigma)`.

Therefore the all-prime cylindrical Fisher energy is infinite for `sigma<=1/2`, independent of all mixed-prime correlations, measure class, or factorization. The threshold is sharp: the supercritical product completion has finite cylindrical Fisher energy for `sigma>1/2`.

## What remains possible

A surviving positive route must form the finite--archimedean object **before** a same-algebra positive quotient or passive reduction is asked to recover the sparse rays. It may use a non-passive/off-diagonal coupling, a changing domain, a singular or endpoint-rough state, higher cohomology, or a geometry not based on the standard product-coordinate Fisher/Dirichlet metric.

Such a mechanism must derive three things independently: why the mixed-prime correlations have the form they do, how the archimedean/polar sector couples to them, and why the final sign survives despite the critical roughness. Merely choosing correlations to match the desired moments or deleting them after positivity is established does not qualify.

## Status / novelty

Multiplicative-domain rigidity, conditional expectations, Schur complements/shorting, Kakutani product-measure theory, Zygmund endpoint estimates, and Fisher-information inequalities are classical. The persisted Mathia synthesis is their exact interaction with the cover-covariant Weil rays: **finite positivity is attainable, but only in an interaction/regularity category that the final selector must genuinely understand**.

## Falsification criterion

Construct a canonical finite-mass positive completion with the exact critical rays and finite standard cylindrical Fisher energy, contradicting WP-102; or give a positivity-preserving same-algebra/passive map that removes the mixed modes while retaining the exact one-prime coordinates and finite diagonal, contradicting WP-098--WP-099. A positive escape must explicitly change one of those hypotheses and derive the replacement geometry from the Weil construction.

## Lean-formalizable core

- Multiplicative-domain retention of prime-coordinate products.
- Order obstruction for passive positive elimination.
- Prime-torus sparse diagonal lower bound.
- Coordinate-moment lower bound for cylindrical Fisher energy.
- Divergence threshold of `sum_p (log p)^2 p^(-2 sigma)` at `sigma=1/2`.
