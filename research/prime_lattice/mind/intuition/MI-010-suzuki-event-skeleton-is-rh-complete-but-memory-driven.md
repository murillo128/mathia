# MI-010 — Suzuki's fixed-step loophole is horizontally conditioned phase pinning, not ordinary vertical anti-aliasing

**Evidence level:** supported by PL-150 and PL-153--PL-163; exact for the sampled zero-series, recurrence, Cauchy-transform, prime-phase specialization, and positive harmonic-kernel reductions in their stated models

## Core intuition

Suzuki's completed scalar carries enough zero information that fine observation sets can remain RH-complete, but fixed-step sampling has a genuine phase quotient. The surviving lower-boundedness loophole is now much narrower than generic phase recurrence: it requires an **unattained off-critical horizontal frontier whose near-edge zeros are simultaneously pinned to the sampled phase identity**.

Ordinary vertical arithmetic does not exclude that condition. Zeta zero ordinates are unconditionally recurrent near the identity in every fixed finite prime torus, and the classical Landau--Gonek moments already couple horizontal displacement to prime phase. The canonical positive first-moment way of exploiting those moments loses precisely the resolution needed at a hypothetical interior frontier. The missing theorem must therefore be horizontally conditioned source rigidity or a stronger carrier, not more unconditioned phase sampling.

## Strongest justified principle

PL-150 and PL-153--PL-154 show that the completed prime-power checkpoint state is RH-complete: one-sided checkpoint boundedness is RH-equivalent and one-sided growth exponents recover the horizontal zero frontier. PL-155--PL-157 show that dense two-prime differences and asymptotically fine meshes inherit the continuous criterion by generic observation geometry.

PL-158 gives the fixed-step upper boundary. For every `h>0` an off-line quartet can be placed in exact resonance so that the continuous screw has both signs while the samples on `nh` remain bounded above. PL-159--PL-160 show the lower side is stricter: finite recurrence and then infinite attained-edge almost-periodicity force negative escape whenever the rightmost horizontal frontier is attained.

PL-161 identifies the exact surviving lower geometry. The sampled generating function has radius determined by the horizontal frontier; one-sided boundedness and Pringsheim force near-frontier poles toward the positive radial boundary. Thus under RH failure lower boundedness requires an **unattained phase-pinned frontier** with distinct ordinates tending to infinity.

PL-162 shows why finite-prime vertical anti-aliasing cannot close that loophole. Ford--Meng--Zaharescu implies that for every fixed finite prime set `P`, the vectors `(gamma log p/(2pi))_(p in P)` of all zeta zero ordinates are Haar-equidistributed to leading order. Every identity neighborhood contains a positive asymptotic proportion of ordinates, and there are sequences with `p^(i gamma_j)->1` simultaneously for all `p in P`. The explicit prime-power discrepancy depletes the identity only at relative order `1/log T`; it does not exclude recurrence. The useful missing information is therefore the coupling to `beta_j->Theta`, not the vertical phase alone.

PL-163 tests the most direct such coupling. Landau--Gonek prime-power moments exactly encode `cosh(k(beta-1/2)log p) cos(k gamma log p)`. Their positive harmonic Fejer combination is nonnegative on the full critical strip and has controlled explicit-formula errors, but harmonic extension from the trivial strip boundary exponentially damps all Fourier modes at an interior frontier `Theta<1`, so increasing degree cannot amplify sparse phase-pinned frontier zeros. Moving the positive boundary inward restores `K`-scale response but makes the published Landau--Gonek error grow exponentially like `p^(k(1-Theta))`. The canonical positive first-moment route therefore has an exact frontier-resolution tradeoff.

## What remains possible

A fixed-ray lower theorem must control the **horizontal-conditioned phase population** near a hypothetical extremal abscissa. Possible carriers include a stronger uniform weighted explicit formula, higher or mixed moments, genuinely simultaneous multi-prime information whose same zeros are coupled before taking limits, or a sign-indefinite cancellation argument that is not constrained by positive harmonic extension from `beta=0,1`.

Adding finitely many prime axes without horizontal conditioning is closed by PL-162. Repackaging the existing Landau--Gonek first moments into another positive full-strip harmonic kernel does not overcome the PL-163 resolution barrier. For upper boundedness, the finite resonant quartet remains a matched control unless additional zeta-specific source information excludes it.

The broader positive route remains upstream: derive the completed sign or one-sided growth restriction from rational-prime/global-completion structure before generic observation completeness takes over.

## Status / novelty

Suzuki's screw representation, Kronecker recurrence, Pringsheim, zeta-zero phase equidistribution, Landau--Gonek moments, and Fejer/harmonic positivity are classical or literature-backed. The synthesis is the sharpened sampling boundary: **the fixed-step lower loophole is not rare vertical phase recurrence but an off-critical horizontal/phase correlation living beyond the resolution of the canonical positive first-moment channel**.

## Falsification criterion

Construct an attained off-line zeta frontier with `Psi(nh)` bounded below, contradicting PL-160; show that fixed finite prime-phase identity recurrence is absent from the complete zeta zero ordinates, contradicting PL-162; or obtain unbounded interior-frontier resolution from the PL-163 full-strip positive harmonic family without paying the stated error growth.

## Lean-formalizable core

- Fixed-step resonant quartet alias.
- Infinite attained-edge recurrence and Pringsheim phase pinning.
- Finite-prime torus identity recurrence as an observation control.
- Landau--Gonek horizontal/phase moment identity.
- Full-strip harmonic positivity versus interior-frontier damping.
