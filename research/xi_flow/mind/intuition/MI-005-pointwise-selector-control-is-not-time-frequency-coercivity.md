# MI-005 — Static slow-cone coercivity fails, but positive-time tangent heat restores a matched selector frame

**Evidence level:** exact periodic tangent transport and matched-control hierarchy through XF-063

## Core intuition

The source-to-transition gap has two different regimes. For arbitrary static critical geometry, no weighting of the shrinking slow cone controls every defect: chirps, derivative-scale waves, and sparse local perturbations defeat successive selector norms. After a fixed positive amount of the exact tangent heat flow, however, the high-frequency sparse escape is damped and every surviving critical triple-flux mode is forced back into the slow cone, where the derivative-weighted moving-line selectors form an exact lower frame.

The missing theorem has therefore moved from “find a better aggregate norm” to “justify that the nonlinear Xi transition enters and retains the tangent positive-time regime without losing the critical defect.”

## Strongest justified principle

XF-057 gives a chirp with critical flux and vanishing pointwise coefficients. XF-058 shows unweighted square energy detects it. XF-060 constructs a high-slow pure wave with critical flux but vanishing unweighted square energy and identifies the derivative weight needed for that scale. XF-061 then moves one root by `kappa/M`; the normalized triple flux stays order one while the complete derivative-weighted energy in the shrinking slow cone tends to zero. This proves that static slow-cone weighting alone is not an inverse norm.

XF-062 changes the support picture after any fixed tangent heat time `tau>0`. In the exact periodic arithmetic-lattice linearization, very low modes cannot carry normalized third-difference flux and modes above the source selector band are exponentially damped. Uniformly over bounded tangents, all critical flux surviving to time `tau` is therefore concentrated in the same slow band controlled on the Xi source side.

XF-063 then supplies the missing lower frame. Compact Fourier support of the moving-line probe makes the periodic mode sidebands disjoint, so the derivative-weighted continuous selector square function diagonalizes with the same `M^3|e^{i xi}-1|^6` symbol as the tangent flux energy. Hence any bounded tangent retaining critical triple flux after fixed positive time has a positive selector norm, while the actual Xi carrier has vanishing norm in that band by the source estimates.

## What remains possible

The live bridge is nonlinear and dynamical: compare finite-amplitude gap geometry to the tangent frame after positive time, prove that the transition quantity cannot dissipate before this comparison becomes valid, and survive nonperiodic boundaries, collisions, or complex-root intervals. A nonlinear destination norm should reduce to the XF-063 frame and quantify the error of leaving the arithmetic lattice.

## Status / novelty

The Fourier semigroup, Poisson summation, sideband orthogonality, and discrete Sobolev estimates are classical. The durable synthesis is line-specific: **slow-frequency coercivity is false statically but becomes exact at positive tangent heat time; the remaining obstruction is transfer from nonlinear Xi dynamics to that repaired tangent category**.

## Falsification criterion

Produce a bounded periodic tangent with critical flux surviving fixed positive heat time but vanishing XF-063 selector energy, invalidate the XF-062 band concentration, or derive a nonlinear Xi comparison showing that the tangent frame already suffices through the relevant transition without additional hypotheses.
