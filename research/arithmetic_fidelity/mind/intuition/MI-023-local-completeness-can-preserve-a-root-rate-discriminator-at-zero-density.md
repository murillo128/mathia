# MI-023 — Sparse root-rate observability is a quantitative phase-avoidance problem

**Evidence level:** exact finite-mode classifications, transcendental counterexamples, and Haar-generic faithfulness through AF-250

## Core intuition

Sparse output sampling preserves a finite-exponential root-rate discriminator according to the exponential rate at which the sampled phase orbit approaches the zero geometry of the relevant trigonometric polynomial. Natural density, local thickness, and periodic completeness are only special proxies in restricted arithmetic classes.

The decisive distinction is between ordinary recurrence and exponentially accurate destructive recurrence. A sampling set may visit every residue class and still fail root-rate fidelity if a transcendental phase approaches a cancelling configuration superexponentially.

## Strongest justified principle

AF-244 proves that zero-density sets with arbitrarily long consecutive blocks can preserve the exact finite-exponential root-rate discriminator. AF-245--AF-246 recast the general finite-mode question on the compact phase-orbit closure and identify the shrinking-target exponent to the polynomial zero set as the intrinsic fidelity currency.

AF-247 shows that algebraic modes are rigid enough for Subspace-Theorem recurrence machinery to reduce universal finite-mode observability to periodic completeness. AF-248 proves that this collapse is genuinely algebraic: a Li-symmetric two-mode transcendental phase can satisfy periodic completeness while half-integer approximation is so fast that the restricted root rate collapses. AF-249 makes the two-mode threshold exact through the exponential approximation exponent, and AF-250 supplies the matched generic control: for any fixed unbounded sampling set, Haar-almost every finite phase vector is root-faithful for every nonzero finite trigonometric polynomial.

## Program consequence

Treat the actual zeta/Li phases as a source-specific Diophantine problem. Identify their phase-orbit closures and prove that sampled visits to every relevant destructive zero set are only subexponentially accurate, with enough uniformity as the finite mode family grows. Do not replace that obligation by density, periodic completeness, or a generic-Haar heuristic.

Keep source cost separate: a sparse faithful output set does not make the retained Li coefficients cheaper to construct.

## Counterevidence / boundary

The exact classifications are finite-mode statements. Haar genericity says exceptional phase vectors have measure zero, not that the arithmetic phases avoid them. Algebraic periodic completeness remains valid in its own subclass, while transcendental families can be much worse. Uniformity as the number of modes grows is still a separate obstruction.

## Epistemic status

**Exact finite-mode classification by exponential phase avoidance, with algebraic periodic completeness and Haar-generic faithfulness as special controls; source-specific shrinking-target bounds for the zeta/Li phases remain open.**

## Falsification criterion

Exhibit an actual finite zeta/Li phase family whose sampled orbit approaches its destructive zero set at positive exponential rate, or prove that periodic completeness alone controls all transcendental finite-mode families contrary to AF-248--AF-249.
