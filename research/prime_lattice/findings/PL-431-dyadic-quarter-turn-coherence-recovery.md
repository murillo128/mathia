# PL-431 — A vanishing quarter-turn vertical shift recovers dyadic-band coherence from two scalar samples

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-NARROWBAND-STRUCTURE + ANALYTIC-TARGET-REFINEMENT`.

**Parent findings:** `PL-428`, `PL-429`, `PL-430`.

## Claim

`PL-429` shows that the imaginary mod-5 character coherences invisible to same-shift product variances become recoverable from the real scalar response along the vertical `log n` flow. `PL-430` then gives a finite-aperture conjugate-Poisson estimator that works for arbitrary positive-frequency support `2 <= n <= N`.

For the actual short-interval prime source, the frequency support has more structure: when the averaging variable lies in `y in [X,2X]` and `h <= X`, every contributing integer lies in the fixed multiplicative band

\[
X < n \le 3X.
\]

On such a band, all frequencies `log n` are asymptotically monochromatic relative to their carrier `log X`. This collapses the tomography problem further. Let

\[
C_X(t)=\sum_{n\in I_X}\beta_n e^{it\log n},
\qquad
R_X(t)=2\Re C_X(t),
\]

with

\[
I_X\subseteq [X,CX],\qquad C>1\text{ fixed},
\qquad
B_X:=\sum_{n\in I_X}|\beta_n|.
\]

Set the single vanishing quarter-turn shift

\[
\boxed{
 t_X:=-\frac{\pi}{2\log X}.
}
\tag{1}
\]

Then

\[
\boxed{
\left|
\frac12 R_X(t_X)-\Im C_X(0)
\right|
\le
\frac{\pi\log C}{2\log X}\,B_X.
}
\tag{2}
\]

Since also

\[
\frac12R_X(0)=\Re C_X(0),
\tag{3}
\]

the full complex zero-shift coherence is recovered, up to an explicit `O(B_X/log X)` error, from only the two real scalar values

\[
R_X(0),\qquad R_X\!\left(-\frac{\pi}{2\log X}\right).
\]

For the short-interval support above one may take `C=3`, giving

\[
\boxed{
\left|
\frac12 R_X(t_X)-\Im C_X(0)
\right|
\le
\frac{\pi\log3}{2\log X}\,B_X.
}
\tag{4}
\]

Thus the live arithmetic target after `PL-430` can be narrowed again: **one does not need a scalar shifted-product theorem uniform on a fixed vertical interval for the dyadically localized short-prime covariance. Pointwise control at zero and at one shift of size `1/log X` is sufficient, provided the coefficient-mass error in (2) is below the `PL-421` covariance margin.**

This is not an RH result and does not supply that scalar arithmetic estimate. It is a representation/conditioning refinement that replaces finite-aperture Hilbert quadrature by asymptotic carrier phase-locking in the actual localized source geometry.

## 1. Exact phase-locking estimate

Write

\[
\log n=\log X+\log(n/X).
\]

At the shift (1),

\[
e^{it_X\log n}
=
 e^{-i\pi/2}
 e^{-i\frac{\pi}{2\log X}\log(n/X)}
=
-i\,
 e^{-i\frac{\pi}{2\log X}\log(n/X)}.
\tag{5}
\]

Because `1 <= n/X <= C`, the elementary inequality `|e^{iu}-1| <= |u|` gives

\[
\left|e^{it_X\log n}+i\right|
\le
\frac{\pi}{2\log X}\log(n/X)
\le
\frac{\pi\log C}{2\log X}.
\tag{6}
\]

Hence

\[
C_X(t_X)
=-iC_X(0)+E_X,
\tag{7}
\]

where

\[
|E_X|
\le
\frac{\pi\log C}{2\log X}
\sum_{n\in I_X}|\beta_n|
=
\frac{\pi\log C}{2\log X}B_X.
\tag{8}
\]

Taking real parts and using

\[
\Re(-iz)=\Im z
\]

proves (2).

The mechanism is therefore not spectral resolution. It is the opposite regime: the arithmetic frequencies in a fixed multiplicative band have relative bandwidth

\[
\frac{\max_{n\in I_X}|\log n-\log X|}{\log X}
\le
\frac{\log C}{\log X}
\longrightarrow0.
\tag{9}
\]

A shift of duration `pi/(2 log X)` rotates the carrier by ninety degrees while rotating every frequency in the band by the same amount up to `O(1/log X)`.

## 2. Stability with theorem or measurement error

Suppose only two approximate scalar values are available,

\[
|\widetilde R_X(0)-R_X(0)|\le\eta_0,
\qquad
|\widetilde R_X(t_X)-R_X(t_X)|\le\eta_1.
\tag{10}
\]

Define

\[
\widehat C_X
:=
\frac12\widetilde R_X(0)
+i\frac12\widetilde R_X(t_X).
\tag{11}
\]

Then (2)--(3) imply

\[
\boxed{
|\widehat C_X-C_X(0)|
\le
\frac{\eta_0+\eta_1}{2}
+
\frac{\pi\log C}{2\log X}B_X.
}
\tag{12}
\]

The bound is deliberately stated in a slightly non-sharp scalar form; it makes the arithmetic requirement transparent. Unlike the estimator in `PL-430`, there is no integral over shifts and therefore no logarithmic amplification of a uniform response error. Only the errors at the two sampled shifts enter.

For fixed `C`, the deterministic quadrature error tends to zero relative to `B_X` automatically. There is no regularization parameter to tune and no aperture to enlarge when higher accuracy is required. The second sample actually approaches the unshifted channel as `X -> infinity`.

## 3. Why this applies to the short-prime matrix route

In the short-interval notation already used in `PL-423`--`PL-425`,

\[
P_a(y;h)
=
\sum_{\substack{y<n\le y+h\\n\equiv a\pmod5}}\Lambda(n),
\qquad y\in[X,2X].
\tag{13}
\]

If `h <= X`, every integer entering any of these windows satisfies

\[
X<n\le 3X.
\tag{14}
\]

Passing to character channels does not enlarge this support. The vertical translation from `PL-429` multiplies the second character source by `n^{-it}`; after forming the cross response, the resulting `C_{j,k}(t)` has positive frequencies `log n` indexed by precisely that second source support. Therefore (4) applies to each of the three hidden coherences isolated in `PL-428`, subject to the same centering convention and coefficient-mass bookkeeping already required by `PL-429`--`PL-430`.

For the principal character, deterministic model subtraction must still be transported consistently under the shift. The natural shifted main term is itself an integral over the same physical interval and obeys the same carrier approximation. What is not permitted is to keep an unshifted deterministic center while shifting only the prime source and then interpret the mismatch as arithmetic coherence.

The practical consequence is a strict weakening of the theorem surface requested at the end of `PL-430`. Instead of proving

\[
\sup_{|t|\le T}|E_{j,k}(t)|\le\eta
\]

on a nontrivial fixed interval and feeding that through a conjugate-Poisson integral, it is enough for this dyadic short-interval application to control the scalar observable at the two parameter values

\[
t=0,
\qquad
t=-\frac{\pi}{2\log X}.
\tag{15}
\]

A theorem valid only at `t=0` still does not suffice: the second sample is genuinely oriented and is exactly what exposes the imaginary covariance. But the required displacement is now vanishing rather than macroscopic.

## 4. Relation to `PL-430`

This result does not supersede the conjugate-Poisson reconstruction in `PL-430`. The two statements address different support geometries.

For arbitrary support `2 <= n <= N`, the ratio between the largest and smallest positive frequencies is unbounded and no single shift can approximate a uniform quarter turn on the whole spectrum. The Hilbert/conjugate-Poisson multiplier is designed precisely to give the same sign-sensitive phase response to every positive frequency.

For support in `[X,CX]` with fixed `C`, however, the frequencies form a narrow band around the diverging carrier `log X`. The exact Hilbert multiplier can then be replaced, for the single aggregate value `C_X(0)`, by the physical time shift (1) with relative phase error `O(1/log X)`. This is the arithmetic analogue of ordinary narrowband quadrature/heterodyning; no novelty is claimed for that generic signal principle.

The line-specific gain is quantitative and procedural: the actual short-prime source used by the mod-5 covariance route is dyadically localized, so the analytic continuation of the research program no longer needs continuum vertical-shift control merely to reconstruct the blind covariance sector.

## 5. Prior-art and novelty audit

The underlying ingredients are classical. A narrow spectral band can be treated as a carrier plus a slowly varying envelope, and a quarter-period carrier shift supplies an approximate quadrature component. Analytic-signal/Hilbert-transform theory already organizes the exact positive-frequency version of this principle; `PL-429`--`PL-430` explicitly record that prior art.

Targeted searches around narrowband quadrature, analytic signals, small vertical shifts of Dirichlet polynomials, and `n^{it}` phases did not locate a number-theoretic theorem with the line-specific conclusion (2): for the dyadically localized `log n` spectrum of the mod-5 short-prime covariance, the missing complex coherence can be read from one vanishing vertical shift with an explicit `B_X/log X` error. No novelty is claimed for `|e^{iu}-1|<=|u|`, vertical translation of Dirichlet series, or generic narrowband phase rotation.

The durable content is the changed arithmetic target. `PL-430` asks for bounded-aperture uniform shifted-product control because it treats a broad positive spectrum. On the actual dyadic source, the same reconstruction needs only a two-point, `1/log X`-scale deformation.

## 6. Adversarial audit and boundaries

1. **Dyadic localization is load-bearing.** If the support extends from `O(1)` to `N`, then `log n/log X` is not uniformly close to one and (6) fails. In that broad-band setting `PL-430` remains the correct reconstruction tool.
2. **The coefficient mass can still be the bottleneck.** Equation (2) is useful for the `PL-421` spectral-floor test only if `B_X/log X` is small compared with the available covariance margin. As in `PL-430`, a bad normalization can make a formally small phase error analytically useless.
3. **A same-shift theorem is not automatically a shifted theorem.** The fact that `t_X -> 0` does not justify substituting `t_X` into an asymptotic proved only at exactly zero. Uniformity, continuity with a proved error, or a direct two-point argument is still required.
4. **Model subtraction must shift coherently.** In particular, the principal-character deterministic term cannot be frozen while the prime coefficients are modulated. Any mismatch would create a spurious oriented component.
5. **The result reconstructs a covariance; it does not prove its size.** Nothing here supplies the unconditional mixed-character source estimate or the `lambda_min >= 1/4` bound required by `PL-421`.
6. **No analytic continuation is inferred.** The derivation is an exact finite exponential-polynomial estimate. Its RH relevance remains entirely through the already established source/zero-transfer program, whose non-circular arithmetic bridge is still missing.
7. **The sign is fixed by the convention in `PL-429`.** There `C(t)` carries `e^{+it log n}`. With `t_X<0`, the carrier tends to `-i`, so `R(t_X)/2` estimates `Im C(0)`. Reversing the vertical-shift convention reverses the sign of the quarter-turn sample.

## Consequence

The representation problem exposed in `PL-428` is now cheaper than `PL-430` suggests for the actual localized prime source. The three missing imaginary mod-5 coherences can, in principle, be reconstructed from scalar data with only one additional sample at a **vanishing** vertical displacement.

The next useful analytic audit should therefore ask a narrower question than uniform finite-aperture tomography:

\[
\boxed{
\text{Can the relevant model-subtracted scalar short-interval variance/cross-response be controlled}
\\
\text{non-circularly at }t=0\text{ and }t=-\pi/(2\log X),
\text{ with error }o(\text{PL-421 margin})?
}
\]

If yes, the three-dimensional coherence blind sector can be supplied without a Hilbert integral or coefficientwise Fourier recovery. If no, the obstruction is no longer vertical aperture or close `log n` frequencies; it is the arithmetic stability of the source/zero transfer under an `O(1/log X)` oriented deformation.