# MI-008 — Exact zero spectrality and positive Hilbertization still leave the arithmetic polarization theorem

**Evidence level:** supported by exact literature-backed spectral/trace constructions and persisted scalarization controls

## Core intuition

The prime-exponent program has now crossed two milestones that might otherwise be mistaken for RH mechanisms: exact global spectral realizations of the zeta divisor already exist, and canonical positive Hilbert norms built from completed zeta data already exist. Neither forces the zeros onto the critical line.

The missing theorem is more specific: a **canonical arithmetic polarization or metric identification** must tie the zero-sensitive global object to a positive/unitary structure. Spectrality, trace formulas, functional-equation centering, and positivity of an auxiliary norm are each weaker statements.

## Strongest justified principle

PL-118 records Deninger's prior-art template. Prime periods `log p`, repeated prime-power orbits, regularized cohomological determinants, and the half-axis mechanism are already part of the classical program. If a positive Hodge pairing exists and the flow acts with weight one on top degree, then `Theta-(1/2)I` is skew and the critical line follows. The load-bearing gap is the existence of the required global arithmetic cohomology/determinant/polarization package.

PL-119 removes the possibility that merely realizing zeros spectrally is enough. Meyer's adelic difference representation has an exact trace/character formula and realizes every zeta zero, with multiplicity, as spectrum. Hypothetical off-line zeros are represented just as faithfully. Positivity/unitarity is precisely what fails without RH.

PL-120 removes the complementary shortcut. Suzuki constructs a positive Hilbert norm canonically from the completed zeta screw data without RH. The RH-level theorem is the equality of that positive norm with the zero-sensitive Weil Hermitian form. Thus "there exists a positive zeta-derived Hilbert space" and "the Weil form is positive" are not the same achievement.

PL-121 shows that the de Bruijn--Newman deformation does not supply hidden multidimensional exponent geometry: its quadratic exponent coupling is rank one and factors through `log n`. PL-124 adds a strong trace-formula control: Poisson--Newton already transforms general Dirichlet frequency lattices into divisor trace formulas, and for zeta the logarithmic/Newton step collapses the full exponent cone to the prime-power rays `k e_p`. Centering at `1/2` is compatible with the functional equation but does not eliminate the real exponential factor of a hypothetical off-line zero.

PL-114--PL-117 supply the local-label counterpart. Fixed congruence, finite Galois, profinite class-function, and compatible `l`-adic Frobenius data either scalarize through characters/irreducibles or retain only conjugacy-local information; they do not canonically transport a cross-prime matrix frame that could substitute for the missing polarization.

## What remains possible

A surviving prime-lattice route should target the arithmetic identification theorem directly. It may construct a cohomological pairing, an indefinite-to-positive completion, a canonical model-space metric, or a finite--archimedean object whose positivity is forced before the zero divisor is read. The decisive property is that the positive structure must act on the same zero-sensitive object and exclude off-axis spectrum, not merely coexist beside it.

The 2026 absolute-twistor construction in PL-123 is relevant as a new source of canonical archimedean/sign geometry, and its odd Frobenius face still preserves the nontrivial zeta divisor. But until a determinant/zero-spectrum and positive polarization theorem connect that geometry to the divisor, it remains structural enrichment rather than localization.

## Status / novelty

Deninger, Meyer, Suzuki, Poisson--Newton, de Bruijn--Newman, representation theory, and adelic harmonic analysis are prior art. The Mathia synthesis is the sharpened gate: **exact arithmetic spectrality plus an auxiliary positive Hilbert space is still weaker than an arithmetic polarization of the zero-sensitive representation**.

## Falsification criterion

Produce an unconditional canonical positive/unitary structure on an exact zeta-zero spectral representation that directly forces `Theta-(1/2)I` to be skew-adjoint, or prove the Suzuki/Weil metric identity by an upstream arithmetic argument not equivalent to assuming RH. Conversely, an exact trace formula or positive norm that permits hypothetical off-line zeros does not falsify the principle.

## Lean-formalizable core

- Hodge-pairing identity implying `Theta-(1/2)I` skew.
- Logical separation of spectral realization from spectral localization.
- Rank-one exponent-lattice form of the de Bruijn--Newman weight.
- Prime-power-ray collapse under logarithmic/Newton coefficients.
- Character/class-function scalarization for fixed Galois labels.