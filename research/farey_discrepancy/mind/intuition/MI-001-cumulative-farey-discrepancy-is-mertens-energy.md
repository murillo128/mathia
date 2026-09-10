# MI-001 — Cumulative Farey discrepancy is Mertens energy, and unrestricted horizon coherence is governed by squarefree-transition density

**Evidence level:** exact Farey--Mertens identities, GCD-duality reductions, collision/interpolation constructions, and pointwise/Cesaro integer-ratio classifications through FD-020

## Core intuition

The cumulative Farey observable is a signed Möbius/Mertens energy, so useful extra structure cannot come from a generic one-horizon Hilbert inequality. Multi-horizon coupling is real, but in the unrestricted source relaxation its coercive content is now sharply classified by how often bounded **squarefree** multiplicative transitions recur.

This turns the previous qualitative reconstruction-versus-interpolation tension into an exact combinatorial boundary. The remaining opportunity is source-specific: the actual Möbius sequence may obey restrictions that the free interpolation construction deliberately ignores.

## Strongest justified principle

Earlier findings identify the cumulative discrepancy with the Mertens source and reduce one-horizon extremality to a classical GCD kernel. FD-014--FD-015 prove strict incompatibility across squarefree multiplicative transitions, while FD-016--FD-017 construct joint saturation on sufficiently fresh sparse schedules.

FD-018 shows that a fixed integer dilation has an exact dichotomy: squarefree dilations forbid asymptotic saturation, whereas nonsquarefree dilations permit it because the finite equality ray vanishes on every nonsquarefree collision coordinate. FD-019 extends this to variable integer-ratio chains: pointwise saturation is possible exactly when bounded squarefree transition ratios eventually disappear.

FD-020 identifies the averaged threshold. Cesaro saturation is possible exactly when, for every fixed bound `B`, transitions with squarefree `q_j<=B` have density zero. If one such bounded family has positive density, its two-horizon gaps add to a nonvanishing average deficit.

## Program consequence

Stop treating generic overlap density as the missing theorem inside the unrestricted relaxation. Use the exact transition classification as a matched control and ask what the real Möbius source forbids beyond it: bounded increments, divisor consistency, squarefree/parity orientation, or another arithmetic constraint that prevents planting equality-ray prefixes.

A useful next theorem should convert such a source restriction into a quantitative deficit on a schedule that the unrestricted model can still saturate, or show that no nonreconstructive schedule can reach the Farey normalization even after source specificity is imposed.

## Counterevidence / boundary

The pointwise and Cesaro classifications are proved for integer-ratio horizon chains and arbitrary real sources. They do not describe general horizon schedules, and the interpolated sources need not resemble Mertens functions. The positive-density deficit also need not be large enough for RH-scale control.

## Epistemic status

**Exact classification of the unrestricted integer-ratio coherence boundary; the remaining leverage must come from Möbius-specific source structure or a genuinely different horizon geometry.**

## Falsification criterion

Construct an unrestricted source that violates the FD-019 or FD-020 classifications, or show that the equality-ray nonsquarefree vanishing used by the interpolation mechanism is false. A positive continuation should prove a source-specific obstruction beyond the classified free model.
