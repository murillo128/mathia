# MI-006 — Screening can hide in one marginal while mirror symmetry forces lower-band leakage; extraction is the real gate

**Evidence level:** supported by WI-115--WI-124 and Fujii/form-factor input in the stated regimes

## Core intuition

Matched controls and source constraints act on different observables. A screening configuration can be perfectly compensated in a counting or moving-edge marginal while necessarily leaking into a conjugate spectral harmonic. The actual zeta same-ordinate mirror symmetry makes that leakage stronger: an off-line finite-period compensator cannot postpone every deterministic alias to the support-one edge. Conversely, the existence of a leaked harmonic is not yet useful unless the final representation extracts enough of it without cancellation from the complement.

Thus the durable distinction is **which information channel compensation can erase, where symmetry forces it to reappear, and whether the final observable has a quantitative localization/coercivity theorem for that channel**.

## Strongest justified principle

WI-115--WI-118 make the support-one screening obstruction structural. Universal termwise positivity forces endpoint taper, and Fejér averaging makes the canonical critical-lattice mirror-pair/double-zero statistic asymptotically blind. WI-120 restores a moving-edge response but leaves open cancellation by a surrounding screening background.

WI-121 adds independent source rigidity: Fujii short-interval moments rule out the canonical long exact double-density critical-lattice island as a positive-density model for the actual zeta zeros. This narrows one extremizer but does not repair the representation alias.

WI-122 shows why count rigidity alone is insufficient. A compensated finite motif can contain a positive density of off-line mirror pairs while keeping cumulative zero counts within bounded discrepancy of the critical control and cancelling the moving-edge quadratic signal down to lower order.

WI-123 proves complementary finite-period rigidity: nonzero horizontal displacement plus aggregate functional-equation balance forces at least one nonzero subcritical reciprocal harmonic. Periodic repetition then gives coherent Bragg-scale mass there.

WI-124 uses the full same-ordinate mirror symmetry `b -> -b`. In reciprocal-cell variables the root multiset is self-inversive. If the first `floor(P/2)` power sums vanished, Newton--Girard plus reciprocal coefficient symmetry would kill every interior coefficient, forcing all roots onto the unit circle and hence every horizontal displacement to vanish. Therefore every genuinely off-line mirror-symmetric `P`-periodic cell has a nonzero alias at some `0<alpha<=1/2`. The finite-period escape of pushing all leakage into `alpha -> 1` is closed exactly.

## Evidence synthesis and boundaries

The lower-half alias theorem is qualitative in growing period: it does not provide a period-uniform lower bound on the leaked amplitude. Nor does a selected block's coherent mass automatically survive addition of the complementary zeta amplitude before the complete positive square is formed. Irregular, aperiodic, sparse, or growing-period compensators can therefore evade the fixed-cell conclusion quantitatively without contradicting it.

The supported program is two-stage. First convert horizontal defect into a quantitative aggregate of lower-half power-sum mass, or prove that every source-admissible compensator must leak such mass. Then prove an **extraction/localization inequality** preventing the surrounding zero configuration from cancelling that mass at the scale used by the unconditional form factor. Without both steps, leakage is diagnostic rather than coercive.

## Status / novelty

Fujii moments, Fejér analysis, self-inversive polynomials, Newton identities, and Bragg harmonics are classical. The persisted synthesis is the channel-transfer view sharpened by exact zeta mirror symmetry: finite-period compensation cannot hide solely at the support edge, but arithmetic use still depends on quantitative amplitude and extraction.

## Falsification criterion

Construct an exactly mirror-symmetric finite-period off-line motif whose reciprocal harmonics all vanish through `alpha=1/2`, contradicting WI-124; or construct a source-admissible growing-period/aperiodic family with quantitatively vanishing lower-half leakage that still performs the required screening. Conversely, a period-uniform defect-to-alias lower bound plus a coercive extraction inequality would materially strengthen the intuition.

## Lean-formalizable core

- Exact support-one screening identity.
- Endpoint taper from universal termwise positivity.
- Finite-motif bounded-discrepancy compensation.
- Self-inversive coefficient symmetry from `b <-> -b` pairing.
- Newton--Girard half-range extinction implication.
- Periodic repetition and Bragg-harmonic amplification.
