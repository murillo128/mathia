# MI-029 — Pair-correlation transfer is jointly limited by packet conditioning and source-window support

**Evidence level:** literature-plus-exact synthesis from [VIS-257](../../findings/VIS-257-cusp-annihilation-exposes-finite-window-quadratic-conditioning.md) through [VIS-260](../../findings/VIS-260-rodgers-fixed-margin-error-pays-cusp-packet-conditioning.md), together with the short-interval transfer boundary in [VIS-265](../../findings/VIS-265-wang-short-interval-support-length-gate.md). The external pair-correlation theorems and their scopes are inherited from those audited findings.

The cusp-packet problem has an intrinsic conditioning scale. After cancelling mass, the sine-kernel cusp and all even moments below order `2m`, a unit `2m`-th retained moment costs exactly

`E_m^(-1) b^(-2m)`

in total variation on `[-b,b]`. If the scalar pair statistic is known uniformly with error `epsilon_T`, the packetized theorem error is therefore at most `epsilon_T E_m^(-1)b^(-2m)`. The theorem accuracy must outrun the same exponent paid to isolate the carrier.

Rodgers supplies one fixed-margin calibration. For fixed support margin `epsilon>0`, fixed smooth weight and fixed `delta<epsilon/2`, the pair-correlation prediction has error `O_delta(T^(-delta))`. Hence the optimally conditioned packet is certified only when

`T^(-delta)b^(-2m) -> 0`.

For `b=T^(-beta)`, some admissible `delta` exists exactly when `beta<epsilon/(4m)`. This is a theorem-relative bandwidth condition, not a universal support-edge law.

VIS-265 adds an independent **source-height localization budget** from Wang's 2026 short-interval Montgomery theorem. For a zero window of length `H=T^theta`, a fixed pair-frequency test with Fourier support inside `[-lambda,lambda]` is covered only when `lambda<theta`, and the normalized theorem error is

`O(1/log T + T^(lambda-theta) log T)`.

Thus pair-frequency support consumes source-window exponent. A probe reaching radius `a` needs `theta>a`; approaching the Montgomery edge `a=1-epsilon` forces `theta>1-epsilon`. A fixed physical or polylogarithmic source window has effective exponent tending to zero, so this theorem supplies no fixed positive pair-frequency support there. “Short interval” is therefore not enough by itself: the theorem's admissible frequency support must be compared with the actual source-window scale of the statistic.

The error scale creates a second boundary. Even in the admissible power-length regime, Wang's stated normalized `O(1/log T)` term cannot resolve a deterministic arithmetic residual of size `c/log T`. A lower-order coefficient requires a theorem whose remainder is smaller than the coefficient scale, or one that carries the lower-order term explicitly. This is logically separate from the `b^(-2m)` packet-conditioning bill.

The combined audit has three independent coordinates: **packet conditioning, pair-frequency support versus source-window length, and theorem remainder versus the intended residual scale**. Passing one does not imply the others. In particular, Wang narrows the previous global-versus-local gap but does not validate the bounded-source tent of VIS-128 and does not transport the prime-power residual isolated in VIS-264 into that regime.

**Boundary.** Rodgers and Wang use different fixed theorem classes; neither statement supplies moving-edge uniformity or the four-level covariance needed by the original edge--edge statistic. Source-height taper and pair-separation weighting are also distinct objects and cannot be identified. Any future transfer must preserve the exact statistic's localization, support and normalization before a source-specific carrier is credited.