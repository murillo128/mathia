# MI-006 — Separated propagation changes the endpoint currency to low-output leakage

**Evidence level:** exact seam decomposition, lowest-pole control, and post-propagation leakage reduction through PF-271

## Core intuition

The positive lowest finite-seam pole kills a bare supercritical separated weight, but that is not the correct final obstruction once the deterministic far propagation is composed first. Propagation can pay for high output modes exponentially; what it cannot pay for is source energy leaked from high input into output frequencies low enough to remain essentially undamped.

The endpoint theorem should therefore ask for one-sided high-to-low spectral leakage control, not global smoothing or graph-domain invariance of the conversion operator.

## Strongest justified principle

PF-258--PF-268 establish the intrinsic-six tangent, fixed-axis fractional window, positive odd-mass ladder, and the `N^-2` proportional high-high floor from the lowest pole. That floor proves unboundedness if an `R>1` input weight is demanded directly from the bare seam.

PF-269 shows that this ordering is overstrong: spatial propagation may regularize the output before the endpoint norm is applied. PF-270 reduces the sufficient condition to one-sided graph locality of the conversion. PF-271 sharpens it again. With arbitrarily strong far-leg smoothing, only leakage from a high input block into a sublinear low-output block can survive the propagation penalty; with exponential propagation, the dangerous output window is only logarithmic in the input scale. The proportional high-high seam floor lies outside that window and is therefore not an obstruction to the composed separated map, whereas a high-to-fixed-low mixer remains fatal.

## Program consequence

Estimate the physical Robin/reflection conversion directly in the composed geometry. Prove the required high-input to logarithmic/sublinear-low-output decay in the endpoint normalization, or identify an exact source cancellation that removes this leakage. Do not require full pre-propagation smoothing when the far leg already pays the corresponding modes.

## Counterevidence / boundary

PF-271 is a reduction of the transport obligation, not a proof that the physical conversion satisfies it. Low-output leakage may still be too large. The exact dangerous window depends on the propagation law and endpoint weight, and a different far leg can change the required scale. PF-268 remains decisive for the bare seam problem even though its proportional high-high floor is no longer decisive after separation.

## Epistemic status

**Exact transport refinement: after separated propagation, the supercritical endpoint problem is governed by high-to-low spectral leakage of the conversion operator, with logarithmic output windows under exponential damping; physical leakage control remains open.**

## Falsification criterion

Show that the composed PF-271 map can be unbounded while every stated high-to-low leakage bound holds, or prove that the physical Robin/reflection conversion necessarily violates the required logarithmic-window decay under the same separation geometry.
