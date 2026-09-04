# MI-004 — Complete scalar control is a diffraction-realizability problem, not a local hyperuniformity test

**Evidence level:** supported through ANF-027 by exact finite-configuration duality and candidate-class exclusions

## Core intuition

For the universal scalar pair-correlation carrier, matching the right small-frequency slope is far weaker than satisfying the full Montgomery--Taylor domination on the support-one band. After finite binding is included, the honest problem is a convex realizability question for complete diffraction measures of finite real configurations.

The stochastic boundary is now substantially sharper. Scale mixtures, iid positional disorder, stationary iid renewals, and the full fractional-Brownian displaced-lattice family all fail. Even the singular zero-Hurst/dilution escape does not approach the target: bounded scales recrystallize to an iid-shuffled lattice, while uniform dilution tends to white diffraction, and arbitrary moving mixtures cannot interpolate between those limits while staying below the Montgomery--Taylor budget.

## Strongest justified principle

ANF-018--ANF-020 identify the exact scalar boundary. Free-density finite-particle stability survives dilute replication, and the whole support-one certificate dualizes to whether the convex diffraction body of finite configurations can fit under the Montgomery--Taylor measure.

ANF-021 shows that a candidate may have the correct local hyperuniform slope and still violate the full-band budget. ANF-022 rules out every probability mixture of arithmetic lattice diffractions by an exact Möbius dilation certificate. ANF-023 closes iid random displacement through incompatible Bragg and diffuse constraints, and ANF-024 closes stationary iid renewals because the zero-frequency diffuse floor forces deterministic gaps.

ANF-025--ANF-027 close a genuinely correlated Gaussian displacement escape. For fixed Hurst exponent `H>0`, fractional-Brownian lattice displacement erases the nonzero Bragg comb but produces the wrong low-frequency power law. The `H->0` boundary does not repair this: at bounded scale it recrystallizes to the iid Gaussian-shuffled lattice, while `rho->0` produces a uniform white-diffraction limit. ANF-027 combines these regimes to exclude arbitrary moving mixtures with `H->0` in probability from the target domination closure.

## What remains possible

The complete finite-configuration diffraction body is still not classified. A surviving stochastic witness must use correlated structure outside the excluded renewal, iid-displacement, and fractional-Brownian displacement closures, while simultaneously producing the linear low-frequency cusp, avoiding open-band Bragg atoms, and avoiding the white/recrystallized boundary models. A direct finite-configuration separating witness also remains possible.

## Status / novelty

Diffraction formulas, renewal theory, Gaussian stationary-increment processes, lattice perturbation spectra, Möbius inversion, and convex duality are classical or literature-backed. The durable synthesis is the increasingly complete control hierarchy: **local hyperuniformity and several natural randomizations, including singular fractional-Brownian limits, fail before the complete scalar diffraction ceiling is broken**.

## Falsification criterion

Produce a realizable finite-configuration diffraction measure below the Montgomery--Taylor budget, or a correlated process outside the excluded closures whose complete diffraction lies below it. Conversely, a proof that the full finite diffraction body misses the budget would close the universal scalar route.

## Lean-formalizable core

- Finite binding/dilute-replication monotonicity.
- Lattice scale-mixture dilation inequalities.
- Perturbed-lattice atom/diffuse incompatibility.
- Renewal zero-frequency rigidity.
- Fractional-Brownian fixed-`H` cusp exponent and zero-Hurst/white-diffraction boundary dichotomy.
