# MI-004 — Complete scalar control is a diffraction-realizability problem, but the first genuinely complex obstruction begins only at five points

**Evidence level:** supported through ANF-036 by exact finite-configuration duality, explicit separator construction, and sharp complex-cardinality controls

## Core intuition

For the universal scalar pair-correlation carrier, matching the right small-frequency slope is far weaker than satisfying the full Montgomery--Taylor domination on the support-one band. The honest control problem is a convex realizability question for complete diffraction measures, not a local hyperuniformity test.

The finite-real barrier is now constructive rather than merely existential. ANF-034 gives an explicit nonnegative support-one central-notch ray that uniformly improves the Montgomery--Taylor stability ratio on every finite distinct real configuration. ANF-035--ANF-036 then locate the first genuinely new complex geometry: common vertical fibers collapse to real multiplicity tests, every conjugation-invariant configuration of at most four points is dominated by its real-part collapse, and five points are sharp for positivity-alone complex separation.

## Strongest justified principle

ANF-018--ANF-020 identify the exact finite-real scalar boundary and dualize it to a convex diffraction-realizability problem. ANF-021--ANF-029 eliminate favorable local slopes, lattice mixtures, iid displacement, renewals, fractional-Brownian displacement, the zero-Hurst boundary, and fixed-intensity log-Gaussian mixtures as ways of realizing the sharp budget.

ANF-030--ANF-033 then expose and separate the sharp finite-real face. The Montgomery--Taylor extremizer has a nonnegative spatial transform whose positive zero set is sum-free; near-sharp finite configurations become locally two-point sparse; and the order interval below the sharp budget is disjoint from the complete finite-real diffraction closure.

ANF-034 turns that separation into a stable explicit central-notch perturbation. ANF-035 shows that equal-height Cartesian complex lifts add no obstruction: their energy is bounded below by the corresponding real multiplicity configuration. ANF-036 proves a cardinality threshold from positivity alone: two-, three-, and four-point conjugation-invariant tests collapse to real controls, while a five-point configuration can lower the energy relative to real collapse. Thus the remaining scalar gate is not generic “complexity”; it is the first horizontal--vertical coupling that survives at five points and above.

## What remains possible

The explicit central-notch family has not yet been proved to satisfy the full zeta-side affine inequality. The decisive test is to evaluate its exact five-point complex deviation, multiplicity slack, and larger source-admissible configurations rather than return to richer finite-real controls. A failure there would identify the true complex obstruction; a surviving margin would move the burden to actual zeta-source constraints.

## Status / novelty

Diffraction, Palm theory, convex duality, Fejer-kernel estimates, packing, and elementary positive-kernel inequalities are classical ingredients. The durable synthesis is the boundary shift: **finite-real stability is explicitly beatable, and positivity alone postpones genuinely new conjugation-invariant geometry until five points**.

## Falsification criterion

Show that the ANF-034 separator fails already on a source-admissible five-point complex configuration with the required affine slack, or prove that it and a controlled neighborhood survive all complex configurations needed by the zero census and yield a stronger unconditional bound.

## Lean-formalizable core

- Finite diffraction convex closure and domination duality.
- Explicit central-notch separator inequalities.
- Common-vertical-fiber collapse.
- Four-point real-collapse theorem and five-point sharpness.
