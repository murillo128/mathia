# MI-002 — Realizability can improve a scalar envelope, but the realized single-profile architecture still has a ceiling

**Evidence level:** supported by exact duality, geometric realizability gains, and explicit periodic countermodels

## Core intuition

The Weil-inertia program now separates three different losses. Fixed-window pinching loses feasible global witness coordinates; the scalar trace--energy envelope loses geometric information about which spectra are realizable by translation Gram blocks; and even after those two losses are repaired, a fixed **single-profile four-point pressure plus the same shifted assembly** still has matched periodic configurations that cap what that architecture can prove. “Better optimization” can help at the first two stages, but not once the full realized representation itself is matched by a countermodel.

## Strongest justified principle

The evidence now gives a hierarchy rather than one bottleneck.

1. **Optimization loss.** WI-012 proves the exact Fenchel representation of the collapsed defect and shows why block pinching is suboptimal: global coupling enlarges the feasible witness set without new arithmetic input.
2. **Envelope realizability loss.** WI-020 proves that the scalar trace--energy envelope is sharp among abstract spectra at fixed energy, but WI-021--WI-024 and WI-036 show that actual translation Gram blocks obey additional span/packing geometry. Positive span pressure can therefore recover part or all of the four-point energy that the scalar envelope discarded. Exact sharpness in the abstract spectral class did not imply attainability by the realized arithmetic matrices.
3. **Representation/assembly loss.** WI-025 computes the ceiling of the full-recovery-only four-point assembly, while WI-026 gives a period-33 witness that caps any universal same-pressure four-point block surplus passed through that same shifted assembly below the older target. This is now the genuine matched-representation obstruction for that architecture.

The live lesson is precise: **first optimize globally, then impose realizability, then ask whether the realized representation is itself information-complete.** A countermodel at the last stage cannot be repaired by another inequality using only the same represented data.

## Consequence

A further support-one improvement must introduce information not matched by the period-33/same-pressure architecture: an uncollapsed exceptional block, multiple genuinely independent profiles and cross-profile matrices, a different local pressure sensitive to additional span geometry, horizontal/depth information, or another arithmetic observable whose unconditional control is explicit.

This is compatible with MI-001. Screening is an upstream bandwidth obstruction; the realized single-profile ceiling is a downstream representation obstruction after substantial geometric information has already been retained.

## Evidence against overgeneralization

WI-025--WI-026 are not upper bounds on every support-one proof, every Gram-matrix argument, or the full zeta Weil matrix. They apply to the audited four-point/same-pressure shifted assembly. A different pressure, several profiles, a global Fenchel variable not factored through that architecture, or support beyond one can evade the periodic witness if it consumes genuinely new information.

## Status / novelty

The Fenchel identity, scalar-envelope sharpness, span/packing improvements, assembly ceiling, and periodic witness are persisted findings. Their three-layer organization is a supported synthesis.

## Falsification criterion

Exceed the WI-026 architecture ceiling using exactly the same realized single-profile four-point pressure and shifted assembly, with no additional observable or hypothesis. That would contradict the matched witness. An improvement using new realized data would instead confirm the stated boundary.

## Lean-formalizable core

- Exact Fenchel duality and block-feasible-set inclusion.
- Distinction between abstract fixed-energy spectra and translation-Gram realizability.
- Span-packing recovery inequalities.
- Evaluation of the period-33 witness under the fixed four-point pressure/assembly.
