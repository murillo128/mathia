# MI-004 — Complete scalar control is a diffraction-realizability problem, not a local hyperuniformity test

**Evidence level:** supported through ANF-024 by exact finite-configuration duality and candidate-class exclusions

## Core intuition

For the universal scalar pair-correlation carrier, matching the right small-frequency slope is far weaker than satisfying the full Montgomery--Taylor domination on the support-one band. After finite binding is included, the honest problem is a convex realizability question for complete diffraction measures of finite real configurations.

The newest controls substantially narrow the stochastic escape. Smearing lattice scale, adding iid positional noise, or replacing lattice spacings by an iid renewal law does not create enough freedom: the target's vanishing long-wavelength diffuse budget forces renewal randomness to collapse back to deterministic lattices before the band test is even reached.

## Strongest justified principle

ANF-018--ANF-020 identify the exact scalar boundary. Free-density finite-particle stability survives dilute replication, and the whole support-one certificate dualizes to whether the convex diffraction body of finite configurations can fit under the Montgomery--Taylor measure.

ANF-021 shows that a symplectic/Pfaffian candidate can have the correct local hyperuniform behavior and still violate the full-band budget. ANF-022 then rules out every probability mixture of arithmetic lattice diffractions at the Montgomery--Taylor constant by an exact Möbius dilation certificate.

ANF-023 closes the simplest disorder repair. An iid randomly displaced lattice retains a Bragg constraint and a diffuse floor that are incompatible with every contraction `a<1`; fixed-density mixtures of such displacement laws fail as well.

ANF-024 closes the classical renewal/random-tiling enlargement. For a stationary renewal process, the exact diffraction density has zero-frequency floor at least the squared coefficient of variation of the gap law. Domination by `a|h|` therefore forces the gap distribution to be deterministic. Convex mixtures consequently reduce to the lattice scale-mixture class already excluded by ANF-022. A surviving stochastic scalar witness must use genuine inter-gap correlations or leave the renewal framework.

## What remains possible

The complete diffraction body is not yet classified. Correlated non-renewal hyperuniform processes, joint density/displacement mixtures outside the proved classes, or a direct finite-configuration separating witness remain logically possible. Any such candidate must be tested on the full band and against finite binding, not credited from a structure-factor slope or thermodynamic limit alone.

## Status / novelty

Diffraction formulas, renewal theory, lattice perturbation spectra, Möbius inversion, and convex duality are classical or literature-backed. The durable synthesis is the control hierarchy: **local hyperuniformity, scale randomization, iid cloaking, and iid renewal randomness all fail before the complete scalar diffraction ceiling is broken**.

## Falsification criterion

Produce a realizable finite-configuration diffraction measure below the Montgomery--Taylor budget, or a correlated stochastic process whose complete diffraction lies below it and is not reduced by the persisted rigidity arguments. Conversely, a proof that the full finite diffraction body misses the budget would close the universal scalar route.

## Lean-formalizable core

- Finite binding/dilute-replication monotonicity.
- Lattice scale-mixture dilation inequalities.
- Perturbed-lattice atom/diffuse incompatibility.
- Renewal zero-frequency floor and deterministic-gap rigidity.
