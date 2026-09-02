# MI-006 — Finite-mass positive completion forces mixed-prime coupling and critical roughness

**Evidence level:** proved for the exact-cover prime-torus completion class and its standard Fisher, entropy, and Kronecker-flow regularity tests

## Core intuition

The critical one-prime Weil rays can live inside a finite positive all-prime carrier, but not as an isolated sparse positive sector. Positivity must be paid for with mixed-prime correlations, and the most natural positive operations cannot later erase those correlations while preserving the prime coordinates. More strongly, no choice of correlations can make the exact critical carrier regular for the ordinary information/Dirichlet geometries now tested: Fisher, cylindrical relative entropy, and the intrinsic log-prime Kronecker density energy all diverge at `sigma=1/2`.

The durable lesson is that **positive completion changes both interaction support and regularity category**. Nonlinear sparsification can recover the desired ray support algebraically, but positivity then becomes tautological or the natural global energy becomes infinite.

## Strongest justified principle

WP-096--WP-099 give the interaction-support boundary. A sparse exact one-prime positive carrier requires infinite diagonal mass; allowing mixed-prime coefficients restores finite positivity, while same-algebra positive quotients and passive Schur elimination cannot delete the mixed modes afterward.

WP-100--WP-102 show that correlations can change global measure class but not the first regularity obstruction. Product completion is Kakutani-singular at `sigma<=1/2`; correlated completions can be Haar-equivalent, yet every exact critical completion has infinite cylindrical Fisher energy.

WP-103 tests a nonlinear escape. Exponentiating the exact finite Weil score gives a positive Gibbs density whose **logarithm** has precisely the one-prime rays and no mixed-prime Fourier modes. The algebraic selector succeeds, but positivity of `e^V/Z` is automatic for every real potential and hence supplies no Weil sign theorem. Its all-prime relative entropy and Kronecker-flow score energy diverge at the critical exponent.

WP-107 makes the entropy obstruction correlation-robust. For any finite positive completion with the exact first one-prime moments, every finite cylinder has KL cost bounded below by the sum of `(log p)^2 p^(-2sigma)`; total correlation can only add nonnegative cost. Hence cylindrical KL is infinite for `sigma<=1/2`, with a sharp supercritical regime.

WP-108 does the same for the intrinsic multiplicative flow `X=sum_p (log p) partial_theta_p`. Parseval forces the exact rays to contribute at least the sum of `(log p)^4 p^(-2sigma)` to the ordinary density Dirichlet energy, again independently of mixed correlations and sharply divergent at the critical exponent.

## What remains possible

A surviving positive route must form the finite--archimedean object before a same-algebra quotient or passive reduction and must leave the ordinary product-coordinate information geometries. It may use a renormalized relative quantity, a globally coupled reference measure, a non-`L^2`/non-KL singular category, higher cohomology, or a nonseparable finite--archimedean form. Such an escape must derive its renormalization/sign independently; subtracting the divergent critical cost after seeing it is not enough.

## Status / novelty

Multiplicative-domain rigidity, Schur shorting, Kakutani theory, Pinsker/KL, Fisher information, Parseval, and Kronecker flows are classical. The persisted synthesis is their exact interaction with the Weil rays: **correlations can repair positivity and measure class, but not ordinary critical information energy**.

## Falsification criterion

Construct a finite-mass exact critical completion with finite cylindrical Fisher, KL, or Kronecker density energy, contradicting WP-102/WP-107/WP-108; or a positivity-preserving same-algebra/passive map that removes mixed modes while retaining the exact prime coordinates. A positive escape must explicitly change one of those hypotheses.

## Lean-formalizable core

- Prime-torus sparse diagonal lower bound.
- Multiplicative-domain and passive-order obstructions.
- Coordinate-moment Fisher and KL lower bounds.
- Kronecker-flow Parseval lower bound.
- Critical divergence thresholds of the corresponding prime sums.
