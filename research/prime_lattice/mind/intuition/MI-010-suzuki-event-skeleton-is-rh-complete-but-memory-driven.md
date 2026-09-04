# MI-010 — Suzuki's completed scalar is RH-complete on fine sets; fixed-step sampling leaves only a phase-pinned frontier loophole

**Evidence level:** supported by PL-150 and PL-153--PL-161; exact for the sampled zero-series, recurrence, Cauchy-transform, and Pringsheim reductions in their stated models

## Core intuition

Suzuki's completed scalar carries enough zero information that thin observation sets can remain RH-complete, but fixed-step sampling has a genuine phase quotient. The quotient is now sharply asymmetric. Upper boundedness still has an exact resonant off-line control, whereas lower boundedness cannot be hidden by any attained horizontal frontier; any surviving failure of RH must use an unattained frontier whose near-edge zeros are pinned to the sampled phase identity.

Thus fixed-step observation is not simply “incomplete.” Its remaining ambiguity has a precise zero-side geometry, and excluding that geometry would require source-specific information not supplied by sampling itself.

## Strongest justified principle

PL-150 and PL-153--PL-154 show that the completed prime-power checkpoint state is RH-complete: one-sided checkpoint boundedness is RH-equivalent and one-sided growth exponents recover the horizontal zero frontier. PL-155--PL-157 show that dense two-prime differences and asymptotically fine meshes inherit the continuous criterion by generic observation geometry.

PL-158 gives the fixed-step boundary. For every `h>0` an off-line quartet can be placed in exact resonance so that the continuous screw has both signs while the samples on `nh` are bounded above. This remains a decisive control against a generic upper-bounded fixed-ray criterion.

PL-159 shows that the same finite alias cannot hide lower escape: finite torus recurrence returns the dominant phases to identity, where ordinary high-ordinate off-line quartets have a common negative leading sign. PL-160 removes finiteness and isolation. If the rightmost horizontal zero frontier is attained, even by infinitely many zeros and with arbitrarily close subedge lines, absolute zero-weight summability and uniform almost-periodicity force `Psi(nh)` to `-infinity` along a subsequence for every fixed `h`.

PL-161 identifies the exact surviving one-sided geometry. The sampled generating function has Taylor radius `exp(-(Theta-1/2)h)`, because no realized displacement circle can cancel completely after aliasing. If the samples are bounded on either side, a shift to nonnegative coefficients and the Vivanti--Pringsheim theorem force a singularity at the positive radial boundary. Hence there are near-frontier zeros with

`exp(i T_j h) -> 1`.

For lower boundedness, PL-160 adds that the frontier must be unattained, so the only remaining RH-failure alternative is an **unattained, phase-pinned frontier** with distinct ordinates tending to infinity.

## What remains possible

A fixed-ray lower criterion would need to rule out that unattained phase-pinned frontier using information external to generic sampling: zero-density or ordinate-distribution constraints, a source relation coupling horizontal approach to phase, or a genuinely simultaneous multi-axis theorem. Separate boundedness statements on two incommensurable prime rays do not by themselves synchronize the near-frontier subsequences selected by Pringsheim.

For upper boundedness, the exact resonant quartet remains a matched control unless additional zeta-specific anti-aliasing excludes it.

The broader positive route remains upstream: derive the completed sign or one-sided growth restriction from rational-prime/global-completion structure before generic observation completeness takes over.

## Status / novelty

Suzuki's screw representation, Kronecker recurrence, Cauchy transforms, and Vivanti--Pringsheim are classical or literature-backed. The synthesis is the sharpened sampling boundary: **fixed-step lower boundedness under RH failure requires an unattained frontier accumulating at sampled phase identity; upper boundedness still admits finite exact resonance**.

## Falsification criterion

Construct an attained off-line zeta frontier with `Psi(nh)` bounded below for some fixed `h`, contradicting PL-160, or a one-sided bounded fixed-step sequence whose near-frontier sampled pole support avoids the positive radial boundary, contradicting PL-161. A source theorem excluding the unattained phase-pinned alternative would close the remaining lower loophole rather than falsify the sampling analysis.

## Lean-formalizable core

- Fixed-step resonant quartet alias.
- Finite and infinite attained-edge recurrence.
- Absolute-summability removal of subedge modes.
- Sampled Cauchy-transform radius equals horizontal frontier.
- Pringsheim phase pinning of near-frontier zeros.
