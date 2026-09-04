# MI-008 — Inertia can identify off-line pairs exactly while every count-only norm charge collapses at confluence

**Evidence level:** proved for Lamzouri's finite Hilbert-space model through WI-140; source-level quantitative exclusion remains open

## Core intuition

Sign information and coercive magnitude are distinct. Lamzouri's finite tensor does something stronger than the earlier screening picture suggested: its negative index counts distinct off-line conjugate pairs exactly, and near extremality forces the negative eigenspace into the canonical horizontal-defect quotient. But the magnitude of those negative directions can collapse continuously as an off-line pair approaches a critical-line double.

Therefore exact inertia is a genuine zero-type discriminator, yet it cannot by itself produce a positive charge per off-line pair. Any defect-to-zero bootstrap must add source information that quantitatively separates actual zeta zeros from this confluence boundary.

## Strongest justified principle

WI-138 writes the canonical self-adjoint Lamzouri tensor as an invertible synthesis congruence of a diagonal signed form. Sylvester inertia then gives exactly one negative eigenvalue for every distinct non-real conjugate pair and none for repeated real points. Multiplicity changes eigenvalue sizes, not the inertia count.

WI-139 combines this with the complete finite slack. If `P_-` is the negative spectral projection and `P_H` the horizontal quotient projection, the same deficit controls both squared negative eigenvalue mass and the Hilbert--Schmidt distance `||P_--P_H||_HS^2`. A near-sharp configuration with many off-line pairs must therefore have many tiny negative eigenvalues whose eigenspace is nevertheless aligned with the specific odd/horizontal defect sector.

WI-140 gives the decisive finite countercontrol. An isolated simple off-line pair `x+-iy` has one negative eigenvalue for every `y>0`, but as `y->0` it confluent-limits to a critical-line double with negative eigenvalue and full Lamzouri deficit both vanishing quadratically. For every fixed `k`, one can place `k` such pairs far apart and make the total finite deficit arbitrarily small. Hence no abstract inequality `Delta>=phi(k)>0` can hold in the finite Proposition 2.1 class.

## What remains possible

The confluence controls are deliberately not models of the full zeta source. A useful theorem may exploit local density, horizontal separation, additional correlation observables, multiplicity statistics, or another arithmetic constraint that prevents a positive-density population of nearly confluent off-line pairs. Such information must be genuinely independent of the finite deficit/inertia already used.

## Status / novelty

Sylvester inertia, projection perturbation, and confluence continuity are classical ingredients. The line-specific synthesis is the exact separation: **negative index identifies the exceptional zero type, while quantitative coercivity is entirely a source-distance-from-confluence problem**.

## Falsification criterion

Derive from unconditional zeta information a quantitative lower bound on the relevant horizontal displacement/eigenvalue mass for a positive density of off-line pairs, or construct source-admissible configurations satisfying all such inputs while retaining arbitrarily small per-pair Lamzouri deficit.

## Lean-formalizable core

- Congruence inertia count for the signed synthesis operator.
- Negative-subspace alignment from Hilbert--Schmidt slack.
- Explicit one-pair confluence eigenvalues and deficit.
- Fixed-`k` no-go for positive count-only stability charge.
