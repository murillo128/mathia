# MI-010 — Suzuki's completed scalar is RH-complete on thin sets, but fixed-step sampling can alias off-line modes

**Evidence level:** supported by PL-150, PL-153--PL-158; the fixed-step matched control and sampling identities are exact in their stated models

## Core intuition

Suzuki's completed scalar carries enough zero information that very thin observation sets can remain RH-complete, but observation-set sufficiency depends on the sampling geometry. Dense or asymptotically fine sets recover the continuous completed state; one fixed geometric ray does not.

PL-158 supplies the missing adversarial boundary. Every fixed step admits an exact completed-polynomial off-line quartet whose Suzuki-type continuous screw has both signs, yet whose sampled sequence is one-signed because the oscillatory frequency is resonantly aliased. The horizontal displacement survives as radial growth, but the ordinate is observed only modulo the sampling frequency. Thus a single prime-power ray is not generically RH-complete merely because it samples a completed criterion.

## Strongest justified principle

PL-150 and PL-153--PL-154 show that the completed prime-power checkpoint state is extraordinarily informative: one-sided checkpoint boundedness is RH-equivalent, and the one-sided exponential growth exponents recover the rightmost-zero frontier.

PL-155--PL-157 then separate completed-state information from sampling density. A fixed two-prime face has a dense difference group and therefore extends kernel positivity to the continuum; the ordinary-prime basis and broad exogenous meshes with sub-`3/4` gaps transfer one-sided boundedness and growth by interpolation. These facts are generic observation properties once the completed scalar/kernel already exists.

PL-158 shows why the same conclusion cannot be pushed to one fixed step `h`. For every `h>0`, a symmetric completed polynomial with off-critical zeros can be chosen with ordinate `tau=2 pi m/h`. Its exact Suzuki-type screw satisfies the same finite logarithmic-derivative transform, but on `t=nh` the oscillatory phase freezes and the samples are nonpositive. In discrete generating-function language, the off-line mode is folded onto an allowed positive real boundary pole. A single prime ray `t=n log p` therefore has an exact aliasing control.

This does not contradict the two-prime face: two incommensurable log-prime directions make the difference group dense, whereas one ray has the discrete group `Z log p`. Nor does it contradict the fine-mesh interpolation results, whose gaps tend to zero relative to the required scale.

## What remains possible

A one-prime sampling theorem would need extra zeta-specific anti-aliasing information, a second incommensurable scale, or a source relation that excludes the resonant controls. Lower boundedness, two-sided boundedness, or other discrete functionals are not closed by PL-158 unless separately reduced to the same alias.

The broader positive route remains upstream: derive the completed sign or one-sided growth restriction from rational-prime/global-completion structure before generic observation completeness takes over.

## Status / novelty

Suzuki's screw representation is literature-backed and equispaced exponential aliasing is classical. The synthesis is the sampling boundary: **after completion, dense/fine observation sets can be RH-complete for generic reasons, while fixed-step rays have an exact off-line alias unless additional source information breaks the phase quotient**.

## Falsification criterion

Show an algebraic failure in the PL-158 resonant quartet control, or prove a zeta-specific theorem that forbids the relevant fixed-step alias while using hypotheses genuinely weaker than the completed RH criterion. A two-scale or dense-difference construction evades rather than falsifies the one-step obstruction.

## Lean-formalizable core

- Prime-power checkpoint one-sided criterion and growth frontier.
- Dense two-prime-face continuity extension.
- Fine-mesh interpolation transfer.
- Fixed-step exponential aliasing and resonant quartet sample formula.
