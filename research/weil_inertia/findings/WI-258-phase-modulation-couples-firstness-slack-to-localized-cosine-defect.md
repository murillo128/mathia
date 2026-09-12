# WI-258 — Phase modulation couples firstness slack to a localized cosine defect

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

`WI-253`--`WI-257` leave a precise gap: the first-crossing aperture profile gives an exact `min`-transform of the zeta source-weighted autocorrelation, but its scalar lower bound cannot be differentiated into prime-threshold signs, its first small-radius correction is universal, and generic bounded-perturbation zero-mode regularity does not control the next translation-defect modulus. There is nevertheless another exact family available at the same first crossing. Multiplying the null mode by a phase does not change its support, so positivity of the localized Weil form applies to every modulation.

For the actual zeta source this gives two coupled constraints on the same signed measure `mu_v` from `WI-254`. Globally,

\[
\boxed{
\mathcal M_v(t):=
\int_0^{2a_*}(1-\cos(th))\,d\mu_v(h)\ge0
\qquad(t\in\mathbb R).
}
\tag{1}
\]

More importantly, combining modulation with the translated-window localization of `WI-253` gives, for every `0<r<a_*` and `t\in\mathbb R`,

\[
\boxed{
\mathcal F_v(r)
+\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h)
\ge r\lambda_r.
}
\tag{2}
\]

Thus, if

\[
S_v(r):=\mathcal F_v(r)-r\lambda_r\ge0,
\tag{3}
\]

then

\[
\boxed{
S_v(r)\ge
\sup_{t\in\mathbb R}
\left[-\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h)\right]_+.
}
\tag{4}
\]

Equation (4) is an exact **defect-to-slack interface**: a negative localized cosine defect of size `epsilon` forces at least `epsilon` of strict reserve over the original firstness bound. It is not yet an RH contradiction. The unresolved zeta-specific step is to force such a negative defect from the actual von-Mangoldt atoms, the archimedean density, compact support, and positive-definiteness of the autocorrelation.

## 1. First-crossing normalization and the source measure

Assume RH is false and let `a_*` be the first unrestricted crossing from `WI-238` and `WI-253`. Write

\[
q:=Q_W^{a_*},\qquad
\|v\|_2=1,\qquad q(v)=0,
\tag{5}
\]

with `q\ge0` on functions supported in an interval of length `2a_*`. Suzuki's form has real coefficients and commutes with complex conjugation. Since a null vector of a nonnegative Hermitian form is orthogonal, in the form sense, to its whole form domain, the real and imaginary parts of any null vector are themselves null whenever nonzero. We may therefore choose `v` real.

Extend `v` by zero and put

\[
C_v(h)=\int_{\mathbb R}v(x+h)v(x)\,dx.
\tag{6}
\]

Retain the source measure of `WI-254`,

\[
d\mu_v(h)=C_v(h)\left[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
+w(h)\,dh
\right],
\tag{7}
\]

where

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2}.
\tag{8}
\]

The measure is only locally finite at `0`, but every integral below is convergent: `w(h)\sim1/(2h)`, while `1-\cos(th)=O(h^2)` and the localized weight in (2) adds no singularity.

The aperture profile is

\[
\mathcal F_v(r)=\int_0^{2a_*}\min(h,2r)\,d\mu_v(h),
\tag{9}
\]

and `WI-253` proves `\mathcal F_v(r)\ge r\lambda_r`.

## 2. Exact phase-modulation identity

For fixed real `t`, set

\[
v_t(x)=e^{itx}v(x).
\tag{10}
\]

Modulation preserves compact support and the logarithmic form domain. Hence `q(v_t)\ge0` at the first crossing. We now compute the difference from the null vector exactly.

For real `v`, the autocorrelation of `v_t` has real part

\[
\operatorname{Re}\int v_t(x+h)\overline{v_t(x)}\,dx
=\cos(th)C_v(h).
\tag{11}
\]

Suzuki's localized Lagrangian formula writes

\[
q(u)=\mathcal L_{a_*}(u)-(2A+1)\|u\|_2^2
-2\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}C_u(\log n)
-2\int_0^{2a_*}r''(h)C_u(h)\,dh.
\tag{12}
\]

The physical-space logarithmic term changes under modulation by

\[
\mathcal L_{a_*}(v_t)-\mathcal L_{a_*}(v)
=\int_0^{2a_*}\frac{1-\cos(th)}{h}C_v(h)\,dh.
\tag{13}
\]

The prime and regular archimedean terms contribute respectively

\[
2\sum_{\log n<2a_*}
\frac{\Lambda(n)}{\sqrt n}(1-\cos(t\log n))C_v(\log n)
\tag{14}
\]

and

\[
2\int_0^{2a_*}r''(h)(1-\cos(th))C_v(h)\,dh.
\tag{15}
\]

`WI-255` established the exact Suzuki identity

\[
r''(h)=w(h)-\frac1{2h}.
\tag{16}
\]

Consequently the logarithmic singularity cancels:

\[
\frac1h+2r''(h)=2w(h).
\tag{17}
\]

Using `q(v)=0`, equations (13)--(17) yield

\[
\boxed{
q(v_t)=2\int_0^{2a_*}(1-\cos(th))\,d\mu_v(h)
=2\mathcal M_v(t).
}
\tag{18}
\]

Because `q\ge0`, this proves (1). The small-frequency limit also gives the exact second-moment constraint

\[
\boxed{
q(xv)=
\int_0^{2a_*}h^2\,d\mu_v(h)\ge0.
}
\tag{19}
\]

Here multiplication by `x` preserves the compactly supported logarithmic form domain, and (19) follows either by expanding (18) at `t=0` or by differentiating the form along `v_t`.

## 3. Modulated translated windows give a two-parameter inequality

Let `eta_{c,r}` be the translated hard window used in `WI-253`, with radius `r`. The generalized localization identity for an arbitrary form-domain vector `u` is

\[
q(\eta_{c,r}u)
=\operatorname{Re}q(u,\eta_{c,r}^2u)
+\text{source localization defect}.
\tag{20}
\]

`WI-253` justified the hard-window formula by smooth approximation in the closed form domain; the same approximation applies to `v_t` because fixed modulation preserves that domain. Averaging the window center gives

\[
\int_{\mathbb R}\operatorname{Re}q(v_t,\eta_{c,r}^2v_t)\,dc
=2r\,q(v_t),
\tag{21}
\]

since `\int\eta_{c,r}(x)^2dc=2r`. The center-averaged source defect uses

\[
\int_{\mathbb R}
(\eta_{c,r}(x+h)-\eta_{c,r}(x))^2dc
=2\min(h,2r)
\tag{22}
\]

and (11), hence equals

\[
2\int_0^{2a_*}\min(h,2r)\cos(th)\,d\mu_v(h).
\tag{23}
\]

Every localized function `eta_{c,r}v_t` is supported in an interval of length `2r`. Translation invariance of the global Weil form therefore gives

\[
q(\eta_{c,r}v_t)\ge\lambda_r\|\eta_{c,r}v\|_2^2.
\tag{24}
\]

Integrating (24) over `c`, using (21)--(23) and `\int\|\eta_{c,r}v\|_2^2dc=2r`, gives

\[
rq(v_t)
+\int_0^{2a_*}\min(h,2r)\cos(th)\,d\mu_v(h)
\ge r\lambda_r.
\tag{25}
\]

Substituting (18) and rearranging proves (2), because

\[
2r(1-\cos(th))+\min(h,2r)\cos(th)
=\min(h,2r)+(2r-h)_+(1-\cos(th)).
\tag{26}
\]

Only lags `h<2r` survive in the correction. This localization is the key structural feature absent from the global modulation inequality alone.

## 4. Prime thresholds enter with an explicit triangular phase factor

Expanding the correction in (2) gives

\[
\begin{aligned}
J_v(r,t):={}&
\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h)\\
={}&
\sum_{\log n<2r}
\frac{\Lambda(n)}{\sqrt n}
(2r-\log n)(1-\cos(t\log n))C_v(\log n)\\
&+\int_0^{2r}
(2r-h)(1-\cos(th))w(h)C_v(h)\,dh.
\end{aligned}
\tag{27}
\]

Thus a prime-power atom does not affect this extra constraint before its aperture threshold `r=(\log n)/2`; after the threshold it enters continuously with a linear triangular factor. In particular, away from the continuous endpoint term, its one-sided contribution to `\partial_rJ_v` switches on as

\[
2\frac{\Lambda(n)}{\sqrt n}
(1-\cos(t\log n))C_v(\log n).
\tag{28}
\]

The frequency `t` can therefore suppress or emphasize individual prime-power shifts without changing the spatial support of the test. Equation (4) says exactly what would be gained if these source-specific phase weights force `J_v(r,t)<0`.

## 5. The cosine cone is not implied by scalar aperture positivity

The new constraint must not be confused with a formal consequence of the scalar inequalities `\mathcal F_v(r)>0`. At the abstract signed-measure level take

\[
\mu=-\delta_1+2\delta_2.
\tag{29}
\]

Its `min`-transform is strictly positive for every `s>0`:

\[
\int\min(h,s)\,d\mu(h)
=\begin{cases}
s,&0<s\le1,\\-1+2s,&1<s\le2,\\3,&s\ge2.
\end{cases}
\tag{30}
\]

But at `t=\pi`,

\[
\int(1-\cos(\pi h))\,d\mu(h)=-2<0.
\tag{31}
\]

So positivity of the complete scalar aperture family does not imply (1). This toy measure is only a transform-level separation test; it is not claimed to satisfy the zeta source factorization, compact-support autocorrelation constraints, or Suzuki's zero-mode equation.

There is also an important converse boundary. `WI-254` proves that the **exact** aperture profile determines `\mu_v` distributionally. Therefore (1)--(2) do not add new raw data once the exact profile is already known; their value is that first-crossing positivity places an additional cone of inequalities on the otherwise underdetermined profiles compatible with the scalar lower envelope.

## 6. Stress tests and evidence boundary

The derivation uses only established first-crossing nonnegativity, Suzuki's exact source decomposition, and the translated-window localization already justified in `WI-253`. It does not use a conjectural pair-correlation statement, RH, or an unproved regularity upgrade.

The following limitations are essential.

- **No contradiction is proved.** Neither (1) nor (2) shows that the actual zeta `mu_v` has a negative localized cosine defect.
- **Generic positivity remains a falsification control.** An analogous modulation inequality exists for any translation-invariant nonnegative first-crossing form. In particular the pure logarithmic-core model of `WI-239` is not excluded merely by phase modulation. A successful RH-facing continuation must use the actual von-Mangoldt atoms and archimedean weight in (27), not just the abstract fact that `1-cos` is nonnegative.
- **`WI-257` is not bypassed by hidden regularity.** Equations (1)--(4) do not infer a quadratic translation modulus from generic zero-modehood. They supply a different exact variational family whose possible gain is explicitly the source-localized defect `J_v(r,t)`.
- **The transform-level counterexample is not a zeta countermodel.** Its only role is to prove logical nonredundancy with scalar `min`-transform positivity.

The decisive next test is therefore concrete: determine whether the explicit finite von-Mangoldt sum and continuous `w(h)` term in (27), together with positive-definiteness and compact support of `C_v`, force

\[
\inf_{t\in\mathbb R}J_v(r,t)<0
\tag{32}
\]

for some `r<a_*`, with a quantitative negative margin. Any such margin feeds directly into (4). A failure should be exhibited by a source-compatible compact-support autocorrelation model satisfying both the scalar aperture bounds and the phase-modulated family.

## 7. Prior art and novelty audit

The provenance is separated as follows.

- **Established Suzuki theory:** the localized Weil quadratic form, its finite von-Mangoldt translation terms, the logarithmic form, and the regular archimedean kernel are from Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2 (17 Aug 2026), especially equations (2.5)--(2.7): <https://arxiv.org/abs/2606.09096>.
- **Persisted Mathia input:** `WI-253` supplies the first global crossing and translated-window localization; `WI-254` supplies the signed source measure and exact aperture transform; `WI-255` supplies `r''=w-1/(2h)`; `WI-257` supplies the generic bounded-perturbation falsification boundary.
- **Classical analytic operations:** fixed modulation, polarization of nonnegative forms, and IMS/window averaging are standard. No novelty is claimed for those operations themselves.
- **Derived here:** applying modulation to the first-crossing zeta null mode gives the exact source cancellation (18); combining it with sliding-window localization gives the triangular two-parameter inequality (2)/(27) and the defect-to-slack bound (4).

A targeted literature search for Suzuki's localized Weil form combined with phase modulation, the `1-cos(th)` source defect, and sliding-aperture first-crossing inequalities located Suzuki's primary form but no source stating this coupled zeta-specific identity. Search absence is audit context only and is **not** a priority claim.

## Research consequence

The accepted sliding-autocorrelation direction now has a sharper falsifiable gate. It is no longer necessary to ask only whether the scalar profile `\mathcal F_v(r)` can be differentiated or asymptotically sharpened. The same first-crossing mode must satisfy the two-parameter cone (2). A source-specific negative value of `J_v(r,t)` cannot be screened for free: it becomes strict firstness slack by (4). The useful continuation is therefore to test the actual prime-threshold phase structure in (27), especially at medium radii containing the first few prime powers, against autocorrelation positive-definiteness. Generic modulation positivity alone is not a solution.