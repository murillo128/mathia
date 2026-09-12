# MI-017 — Sliding first-crossing localization is information-complete only at the exact-profile level

**Evidence level:** supported by the exact sliding-window identity WI-253 and the profile inversion/small-radius saturation theorem WI-254; no incompatibility with a compactly supported global first zero mode is proved.

At the first unrestricted localized Weil crossing `a_*`, translation freedom produces for a normalized zero mode `v` an aperture profile

\[
\mathcal F_v(r)
=
\frac1{2\pi}\int\Sigma_r(z)|\widehat v(z)|^2\,dz
\ge r\lambda_r>0,
\qquad 0<r<a_*.
\]

WI-253 derives this as a continuum of source-dependent spectral averages against one nonnegative density. The parameter `r` is not merely redundant repetition: the kernel changes at every prime-power threshold.

WI-254 identifies the exact information carried by that parameter. After writing the profile as a `min`-transform of the source-weighted real autocorrelation, distributional second differentiation recovers the source measure. The one-sided slope jump at `r=(log n)/2` is

\[
-2\frac{\Lambda(n)}{\sqrt n}C(\log n),
\]

and between thresholds the second derivative recovers the continuous archimedean-weighted autocorrelation. Apart from one removable zero of the continuous weight, the exact profile determines the whole real autocorrelation.

The obstruction is therefore **not aperture information loss**. It is the replacement of the exact profile by the pointwise firstness inequality. A lower envelope cannot be differentiated into jump signs. Moreover the universal small-radius singularity already saturates firstness at leading order:

\[
\mathcal F_v(r)\sim r\log(1/r),
\qquad
r\lambda_r\sim r\log(1/r).
\]

There is no fixed multiplicative coercivity reserve to harvest as `r->0`.

The live route must supply additional control on the exact profile: a source-sensitive subleading asymptotic, a medium-radius relation among curvature and prime jumps, or an identity from the zero-mode equation that couples several radii. More apertures without stronger profile control do not add a new inequality.

**Boundary.** Exact-profile invertibility does not mean firstness determines the profile. Positivity cannot be differentiated, and small-radius saturation is driven by the universal logarithmic core. No pointwise symbol sign, autocorrelation sign, global first-mode exclusion, or RH consequence follows.
