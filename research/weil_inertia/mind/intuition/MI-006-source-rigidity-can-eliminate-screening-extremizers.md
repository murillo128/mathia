# MI-006 — Screening can hide in one marginal while leaking into another; extraction is the real gate

**Evidence level:** supported by WI-115--WI-123 and Fujii/form-factor input in the stated regimes

## Core intuition

Matched controls and source constraints act on different observables. A screening configuration can be perfectly compensated in a counting or moving-edge marginal while necessarily leaking into a conjugate spectral harmonic. Conversely, the existence of that leakage is not yet useful unless the chosen representation can extract it without cancellation from the complement.

Thus the durable distinction is not simply “controls are or are not source-admissible.” It is **which information channel the compensation can erase, which channel it must populate, and whether the final observable isolates that channel**.

## Strongest justified principle

WI-115--WI-118 make the support-one screening obstruction structural. Universal termwise positivity forces endpoint taper, and Fejér averaging makes the canonical critical-lattice mirror-pair/double-zero statistic asymptotically blind. WI-120 restores a moving-edge response but leaves open cancellation by a surrounding screening background.

WI-121 adds independent source rigidity: Fujii short-interval moments rule out the canonical long exact double-density critical-lattice island as a positive-density model for the actual zeta zeros. This narrows one extremizer but does not repair the representation alias.

WI-122 shows why count rigidity alone is insufficient. A compensated finite motif can contain a positive density of off-line mirror pairs while keeping cumulative zero counts within bounded discrepancy of the critical control and cancelling the moving-edge quadratic signal down to lower order. Thus a configuration can evade both naive overcrowding and the first signed marginal.

WI-123 then proves a complementary rigidity for **finite-period** compensation: if such a motif has nonzero horizontal displacement and the required functional-equation balance, its power sums cannot all match the critical motif. Newton--Girard forces a nonzero reciprocal harmonic at some subcritical frequency, and periodic repetition produces a Bragg-scale signal there. The compensation is therefore not information-free; it relocates information between channels.

## Evidence synthesis and boundaries

The harmonic leakage theorem does not by itself yield an RH criterion. In the full zeta configuration, a selected block's Bragg contribution may be cancelled by the complement, and the available global form-factor bounds do not automatically localize that block. Irregular, aperiodic, sparse, or growing-period screening is also outside the finite-period theorem.

The supported principle is therefore two-stage: first prove that a class of compensators must leak into some source-compatible spectral channel; then prove an **extraction/localization inequality** showing that the surrounding zeros cannot erase that channel at the required scale. Without the second step, leakage is diagnostic rather than coercive.

## Status / novelty

Fujii moments, Fejér analysis, Newton identities, and Bragg harmonics are classical. The persisted synthesis is the channel-transfer view of screening: exact compensation in a marginal can force spectral leakage elsewhere, but only a representation with quantitative extraction converts that leakage into a selector.

## Falsification criterion

Construct a finite-period off-line motif satisfying the WI-123 balance conditions whose every subcritical reciprocal harmonic matches the critical control, or prove that the forced harmonic can always be cancelled by a source-admissible complement with no detectable cost in any admissible localized observable. Conversely, a coercive extraction inequality for the forced harmonic would materially strengthen the intuition.

## Lean-formalizable core

- Exact support-one screening identity.
- Endpoint taper from universal termwise positivity.
- Finite-motif bounded-discrepancy compensation.
- Newton--Girard implication from equal power sums to equality of the finite motif.
- Periodic repetition and Bragg-harmonic amplification.
