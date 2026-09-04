# MI-004 — Complete scalar control is a diffraction-realizability problem, and finite real diffraction no longer supplies the Montgomery--Taylor ceiling

**Evidence level:** supported through ANF-033 by exact finite-configuration duality, sharp-energy rigidity, and convex-closure separation

## Core intuition

For the universal scalar pair-correlation carrier, matching the right small-frequency slope is far weaker than satisfying the full Montgomery--Taylor domination on the support-one band. The honest control problem is a convex realizability question for complete diffraction measures, not a local hyperuniformity test.

The newest evidence changes the frontier materially. Natural stochastic real-line controls fail, but the entire finite-real diffraction closure also fails to impose the sharp Montgomery--Taylor ceiling: ANF-033 proves that the order interval below the sharp budget is disjoint from the finite-real diffraction body, and by duality there exists a nonnegative support-one scalar test that beats the Montgomery--Taylor constant on every finite real configuration. The scalar route therefore cannot be rejected at the finite-real stability stage.

## Strongest justified principle

ANF-018--ANF-020 identify the exact finite-real scalar boundary and dualize it to a convex diffraction-realizability problem. ANF-021--ANF-029 eliminate favorable local slopes, lattice mixtures, iid displacement, renewals, fractional-Brownian displacement, the zero-Hurst boundary, and fixed-intensity log-Gaussian mixtures as ways of realizing the sharp budget.

ANF-030--ANF-032 then expose the sharp face itself. The Montgomery--Taylor extremizer has a nonnegative spatial transform whose positive zero set is sum-free; near-sharp finite configurations become locally two-point sparse after deleting a small exceptional set. ANF-033 closes the remaining compactness loopholes and proves

`K ∩ {mu : 0 <= mu <= nu_MT} = emptyset`.

Equivalently, finite real configurations admit a support-one test with stability ratio strictly better than the Montgomery--Taylor constant. This is an existential separation, not yet an explicit optimal kernel and not yet a zeta theorem.

## What remains possible

The next obstruction is genuinely zero-side: complex conjugation-invariant configurations, the full affine zeta inequality, multiplicity, and any additional source constraints. A decisive scalar advance should either construct an explicit useful separating test and pass those complex controls, or prove that complex/source-admissible configurations restore the ceiling that finite real diffraction does not.

## Status / novelty

Diffraction, Palm theory, convex duality, Fejer-kernel estimates, and packing arguments are classical ingredients. The durable synthesis is the boundary shift: **complete finite-real diffraction is not the universal scalar obstruction; the remaining difficulty lies in the complex/source-admissible zero geometry**.

## Falsification criterion

Show that the ANF-033 separation cannot be transferred to the actual complex/conjugation-invariant zero-side affine problem, or produce a valid scalar test whose full zeta-side inequality yields a strictly stronger unconditional conclusion.

## Lean-formalizable core

- Finite diffraction convex closure and domination duality.
- Sharp-energy nonnegativity and local packing.
- Disjointness of the sharp order interval from the finite-real closure.
- Logical separation between finite-real stability and complex zero-side admissibility.
