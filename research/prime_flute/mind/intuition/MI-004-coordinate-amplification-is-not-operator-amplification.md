# MI-004 — Coordinate amplification is not yet operator amplification

**Evidence level:** supported by exact geometric comparison results; operator conclusion remains open

## Core intuition

For the exact all-composite shift clone `p_n -> p_n+1`, different hyperbolic coordinates report very different summability classes. Raw additive cuff-length differences are only `ell^2`, not `ell^1`, yet several quantities more native to the thin geometry — collar widths, collar areas, canonical spine/seam data, and all-span separator ratios — have summable or uniformly vanishing defects. A large coordinate defect therefore cannot be interpreted as a spectral obstruction until it is propagated through a comparison adapted to the Laplacian.

## Strongest justified principle

PF-107--PF-110 isolate the issue sharply.

- PF-107 shows that endpoint `ell^1` control does **not** imply additive cuff-length `ell^1`: the shift-clone cuff defect has leading size `2/p_n`, hence belongs to `ell^2` but not `ell^1`.
- PF-108 shows that this amplification is coordinate dependent. Standard collar-width defects, collar-area defects, canonical seam/spine defects, and an explicit unweighted collar metric-log-distortion integral are absolutely summable.
- PF-109 proves a uniform multiplicative comparison for every canonical PF-004 separator in the tail. Even separators tending to zero cannot amplify the clone error into a persistent marked separator-length discrepancy.
- PF-110 closes the most convenient global-coordinate shortcut: the prime flute has zero systole, while a bounded ideal triangulation would force quasiconformal equivalence to a positive-systole modular-type surface. The Whitney--Šarić bounded-triangulation machinery therefore cannot supply the needed global comparison.

The evidence points to a distinction between **bad Fenchel--Nielsen coordinates** and a genuinely noncompact relative Laplacian effect. Neither implication is currently proved.

## What remains possible

A direct pants/collar gluing on a common marked topological surface can still succeed without a bounded ideal triangulation. If its metric defect tends to the identity strongly enough through collars and cusps, existing relative-Laplacian theory may imply equality of essential spectra or compact relative resolvent. Conversely, the collapsing thin geometry may amplify a summable collar/spine defect in precisely the weighted norm relevant to the Laplacian and destroy compactness.

The correct gate is therefore operator-native: the comparison must be tested in the metric/measure quantities entering the quadratic form, resolvent, heat kernel, or wave operators rather than inferred from one coordinate sequence.

## Status / novelty

The summability and pinching estimates and the triangulation obstruction are persisted findings. No compactness, Schatten, wave-operator, or isospectral conclusion is promoted here. The intuition only identifies the now-supported location of the missing theorem.

## Falsification criterion

Prove that the non-`ell^1` additive cuff defect alone forces noncompact relative resolvent for the shift clone despite the summable collar/spine controls, or prove a direct common-surface comparison satisfying a standard compactness/Schatten criterion. Either result would replace this synthesis by an operator theorem.

## Lean-formalizable core

- Series classifications for the endpoint, cuff, collar-width, and seam defects.
- Uniform conversion from log cross-ratio error to separator-length ratio error.
- Elementary implication from bounded ideal triangulation plus quasiconformal length distortion to positive systole.
