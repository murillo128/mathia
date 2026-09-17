# MI-041 — One-point phase pseudorandomness cannot cancel a positive diagonal variance

**Evidence level:** exact synthesis from [WI-331](../../findings/WI-331-all-start-nilsequence-control-removes-the-low-theta-location-obstruction.md), [WI-332](../../findings/WI-332-all-interval-u2-control-still-misses-the-bow-diagonal-variance-scale.md), and [WI-333](../../findings/WI-333-square-root-phase-pseudorandomness-still-leaves-diagonal-bow-variance.md). The obstruction is exact for the stated covariance reduction; no pointwise Weil bound or RH criterion follows.

Below the all-start threshold `theta<3/16`, the distinguished-source-location problem is no longer the main obstacle: the signed source `Lambda-Lambda_X^sharp` is controlled on every relevant interval. But WI-332 and WI-333 show that strengthening the available **one-point** cancellation in the obvious ways still does not reach the bow covariance norm.

WI-332 tests local `U^2` control. The bow carrier `n^(iU)` has genuinely nonlinear second differences at the relevant height, so linear-phase invariance does not absorb it. Even in an untwisted reduction, a generic Fourier/Hölder conversion from local `U^2` size `delta` yields a sliding variance bound of order `delta^2 X K^2`, whereas the desired covariance scale is `o(X K log X)`. Logarithmic savings in `delta` therefore miss a whole factor of `K`.

WI-333 gives a categorical countermodel. Random-sign coefficients of size `sqrt(log N)` can have essentially square-root cancellation against every fixed-degree polynomial phase on every short interval and arithmetic progression, yet their sliding twisted variance remains

`(1+o(1)) N K log N`

for arbitrary prescribed unit phases. Strong one-point pseudorandomness drives off-diagonal correlations toward zero; it does **not** make the positive diagonal disappear.

The reusable lesson is that the required improvement is not “more phase pseudorandomness” in a one-point sense. **To beat the diagonal variance scale, the arithmetic source must generate a signed two-point mechanism whose off-diagonal contribution cancels a macroscopic part of the diagonal, or supply an equivalent source-fixed subtraction before squaring.** Generic randomness is the wrong model precisely because it leaves the diagonal intact.

This separates the surviving regimes cleanly. For `theta<3/16`, location uniformity is available and the missing theorem is fundamentally a two-point/covariance statement. For larger surviving `theta`, the same covariance requirement remains, with the additional distinguished-start exceptional-set problem.

**Boundary.** WI-332 does not rule out stronger higher-order uniformity norms with a theorem quantitatively matched to the bow phase, and WI-333 is a deterministic/probabilistic countermodel rather than a statement about the von Mangoldt source itself. The conclusion is only that one-point phase cancellation, even at square-root strength across rich phase families, is insufficient without a mechanism that addresses the diagonal.