# MI-004 — Compatible all-level completion preserves labels, but its canonical radial geometry classicalizes to dilation half-density and flat log cylinders

**Evidence level:** supported by exact/classical completion, covariance, and local-metric obstructions through PC-166

## Core intuition

Passing from Prime-Circle shells to the compatible inverse limit preserves exact-order labels, divisor filtrations, and rational characters. But the canonical regular geometries on that completion still do not turn those labels into an RH-selecting spectrum. The newest results identify the radial sector almost completely: compatible power refinement is ordinary dilation in logarithmic radius, its unitary normalization forces the classical half-density exponent, and every regular power-homogeneous local metric is a flat log-cylinder metric with continuous radial spectrum.

Thus the half-weight can arise canonically here without selecting Riemann zeros. Label preservation, the critical half-density, proper spectral scale, and arithmetic polarization remain distinct gates.

## Strongest justified principle

PC-055--PC-074 establish the earlier boundary: the adelic solenoid preserves the rational label system, while broad commuting calculi and scalar dilation covariance fail compact resolvent; imposing a projective proper height recovers only a classical primitive-lattice zeta problem.

PC-165 makes the compatible radial action explicit. The completed punctured-plane power system splits as a logarithmic radial line times the solenoid. Haar `L^2` pullback is exactly the classical unitary dilation representation with exponent `-1/2+it`. A formal integer pullback sum can display `zeta(1/2-it)`, but the sum is unbounded/not strongly convergent and the radial generator has continuous spectrum. The half factor is representation theory, not a zero Hamiltonian.

PC-166 closes the most direct local-metric repair. Any continuous positive-definite local two-dimensional metric for which `z -> z^2` acts by homothety becomes a constant-coefficient metric in log-cylinder coordinates, including all radial-angular cross terms. Its Laplace-type spectrum retains the continuous radial channel and cannot produce a compact-resolvent Riemann zero divisor by local metric tuning.

## What remains possible

A surviving completion operator must be nonlocal, singular/domain-changing, non-homogeneous, one-sided, relative, or genuinely coupled across radial and arithmetic sectors in a way not reducible to the flat log cylinder. Its half-weight, normalization, and source selector must be forced independently rather than inherited from ordinary unitary dilation.

## Status / novelty

Solenoids, logarithmic polar coordinates, unitary dilation half-densities, and flat homogeneous metrics are classical. The synthesis is the separation: **the compatible completion can canonically generate the critical half-density while still lacking zero selection and coercive arithmetic spectrum**.

## Falsification criterion

Derive from the compatible geometry a source-forced nonlocal/singular operator with a discrete or relative zero-sensitive invariant that cannot be reduced to ordinary dilation, a chosen projective height, or a flat log-cylinder calculus.

## Lean-formalizable core

- Radial/solenoidal product decomposition.
- Half-density normalization of dilation.
- Flatness of power-homogeneous local metrics in log coordinates.
- Continuous radial-spectrum obstruction.
