# WI-254 — The sliding-aperture profile is invertible, but small-scale firstness is asymptotically saturated

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

`WI-253` shows that a hypothetical first unrestricted localized Weil zero mode produces a continuum of positive sliding-window fluxes. The aperture parameter carries more exact information than was used there: after averaging the window center, the whole profile is a classical `min`-transform of a source-weighted autocorrelation distribution. Its distributional second derivative recovers that source distribution exactly. Prime-power thresholds are literal slope jumps, while the continuous archimedean density recovers the real autocorrelation away from one explicit removable zero of its weight.

This does **not** turn the positivity inequality of `WI-253` into a contradiction. Pointwise lower bounds cannot be differentiated to control those slope jumps. Moreover the family is asymptotically saturated at the small-radius end:

\[
\mathcal F_v(r)\sim r\log(1/r),\qquad
r\lambda_r\sim r\log(1/r),\qquad
\frac{\mathcal F_v(r)}{r\lambda_r}\to1.
\]

Thus a fixed multiplicative reserve over firstness cannot close the problem near `r=0`. Any contradiction must use subleading information, medium radii, threshold coupling, or the zero-mode equation itself.

## 1. Exact `min`-transform

Retain the notation of `WI-253`. Under RH failure let `a_*` be the first unrestricted crossing, choose a normalized zero mode `v`, and define

\[
C(h):=\operatorname{Re}\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx,
\qquad C(0)=1.
\]

Translation continuity in `L^2` makes `C` continuous and even. Since `v` is supported in `[-a_*,a_*]`, `C(h)=0` for `|h|\ge2a_*` in the `L^2` autocorrelation sense. Put

\[
\kappa(h)=\frac{e^{-5h/2}}{1-e^{-2h}},
\qquad
w(h):=\kappa(h)-e^{h/2}.
\]

On `(0,2a_*)` define the **locally finite** signed source measure

\[
d\mu_v(h)
:=C(h)\left[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
+w(h)\,dh
\right].
\tag{1}
\]

Because `w(h)\sim1/(2h)` as `h\downarrow0`, this measure has infinite total variation at the left endpoint; it is finite on every compact subinterval of `(0,2a_*)`. The `min` weight makes the aperture integral finite. `WI-253` is exactly

\[
\boxed{
\mathcal F_v(r)=\int_0^{2a_*}\min(h,2r)\,d\mu_v(h),
\qquad 0<r<a_*.
}
\tag{2}
\]

Set `t=2r` and

\[
L_v(t):=\mathcal F_v(t/2)
=\int_0^{2a_*}\min(h,t)\,d\mu_v(h).
\tag{3}
\]

On every compact subinterval of `(0,2a_*)`, elementary limited-expectation calculus gives

\[
\boxed{L_v''=-\mu_v}
\tag{4}
\]

in the distributional sense. The abstract `min`-kernel inversion is classical; no novelty is claimed for it. The zeta-specific content is what the known prime atoms and archimedean density make (4) say about the first-crossing autocorrelation.

## 2. Prime-power thresholds are exact slope jumps

Away from thresholds `r_n=(\log n)/2`, differentiating (2) is legitimate because `2r>0` stays away from the singular endpoint:

\[
\boxed{
\mathcal F_v'(r)
=2\sum_{2r<\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}C(\log n)
+2\int_{2r}^{2a_*}w(h)C(h)\,dh.
}
\tag{5}
\]

At a prime-power threshold `r_n=(\log n)/2` with `\log n<2a_*`, the continuous term has no jump and the corresponding atom switches from the linear to the saturated branch. Hence

\[
\boxed{
\mathcal F'_{v,+}(r_n)-\mathcal F'_{v,-}(r_n)
=-2\frac{\Lambda(n)}{\sqrt n}C(\log n).
}
\tag{6}
\]

Between thresholds,

\[
\boxed{
\mathcal F_v''(r)=-4w(2r)C(2r).
}
\tag{7}
\]

Equivalently, on `(0,a_*)` distributionally,

\[
\boxed{
\mathcal F_v''
=-4w(2r)C(2r)\,dr
-2\sum_{\log n<2a_*}
\frac{\Lambda(n)}{\sqrt n}C(\log n)
\,\delta_{(\log n)/2}.
}
\tag{8}
\]

Thus, **if the exact aperture profile is known**, its one-sided slope jumps read off the real autocorrelation at every prime-power shift in range.

## 3. The continuous weight has one removable blind point

Put `x=e^h>1`. Since

\[
\kappa(h)=\frac{x^{-1/2}}{x^2-1},
\]

we have

\[
w(h)=0\iff x^3-x-1=0.
\tag{9}
\]

The polynomial is strictly increasing for `x>1`, so there is exactly one positive solution. Writing `\rho` for the plastic constant,

\[
\rho=1.3247179572447460259\ldots,
\]

its location is

\[
h_0=\log\rho=0.2811995743229618465\ldots,
\qquad
r_0=h_0/2=0.1405997871614809233\ldots.
\tag{10}
\]

For every non-threshold `h\ne h_0`,

\[
\boxed{
C(h)=-\frac{\mathcal F_v''(h/2)}{4w(h)}.
}
\tag{11}
\]

At prime-power shifts the same value is independently encoded by (6). At `h_0`, continuity of `C` recovers the value from either side; `\rho` is not an integer, so this point does not collide with a von Mangoldt atom.

Therefore the **exact** profile `r\mapsto\mathcal F_v(r)` determines the whole real autocorrelation `C(h)` on `(0,2a_*)`, hence on the real line by evenness and compact support. Equivalently it determines the cosine/even spectral information encoded by `C`. This must not be strengthened to recovery of an arbitrary unsymmetrized complex spectral density.

The family is therefore information-complete at the real-autocorrelation level as an identity. The remaining loss is that firstness gives only a lower bound for this profile, not the exact profile itself.

## 4. Small-radius firstness is saturated at leading order

Near zero,

\[
\kappa(h)=\frac1{2h}+O(1),
\tag{12}
\]

and `C(h)\to1`. Split the `\kappa` contribution in (2) at fixed small `\delta>0`. For `r<\delta/2`,

\[
\begin{aligned}
\int_0^{2a_*}\min(h,2r)\kappa(h)C(h)\,dh
&=2r\int_{2r}^{\delta}\left(\frac{C(h)}{2h}+O(1)\right)dh+O(r)\\
&=r\log(1/r)+o\!\left(r\log(1/r)\right).
\end{aligned}
\tag{13}
\]

The interval `0<h<2r` contributes `O(r)`. The smooth `-e^{h/2}` part also contributes `O(r)`. Once `r<(\log2)/2`, every prime-power atom is on the linear branch `2r`; only finitely many lie below `2a_*`, so their total is `O(r)`. Consequently

\[
\boxed{
\mathcal F_v(r)
=r\log(1/r)+o\!\left(r\log(1/r)\right).
}
\tag{14}
\]

Suzuki's Theorem 1.4 gives for the actual localized Weil ground-state energy

\[
\boxed{
\lambda_r
=\log(1/r)+\mu_1-\log(2\pi)+\psi(2)-1+O(r),
\qquad \mu_1>0.
}
\tag{15}
\]

Therefore

\[
\boxed{
\frac{\mathcal F_v(r)}{r\lambda_r}\to1.
}
\tag{16}
\]

The firstness inequality from `WI-253`, `\mathcal F_v(r)\ge r\lambda_r>0`, is sharp at the universal leading scale. Hence no fixed `\epsilon>0` can satisfy

\[
\mathcal F_v(r)\ge(1+\epsilon)r\lambda_r
\]

for all sufficiently small `r` along the actual first-crossing profile.

Primary source for (15): Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), Theorem 1.4: <https://arxiv.org/abs/2606.09096>.

## 5. Positivity cannot be differentiated into prime signs

`WI-253` proves only

\[
\mathcal F_v(r)\ge r\lambda_r>0.
\tag{17}
\]

Equation (17) cannot be differentiated. In particular, (6) does **not** imply a sign for `C(\log n)`. Pointwise positivity or a positive lower envelope places no sign restriction on a derivative jump. For example,

\[
G(r)=Mr+J(r-r_0)_+
\tag{18}
\]

has any prescribed jump `J`; choosing `M>|J|` keeps `G(r)>0` for `r>0` on a bounded interval. This is a logical stress test, not a matched zeta countermodel, but it decisively rules out differentiating (17) to obtain prime-autocorrelation signs.

The jump formulas become useful only if another exact relation controls `\mathcal F_v` more tightly than pointwise firstness. Candidates are a source-sensitive subleading small-`r` expansion, medium-radius coupling, or the zero-mode equation itself.

## 6. Pure-core stress test

`WI-239` proves that the universal logarithmic core itself has an attained first zero mode. It therefore kills arguments using only nested domains, compactness, continuity, or first crossing. The present result respects that boundary.

The inversion uses the **actual zeta source decomposition** of `WI-253`, including the von Mangoldt atoms and explicit archimedean weight, so it is not a generic consequence of firstness. Conversely, the small-`r` saturation (16) is driven by the same logarithmic singularity underlying the pure-core crossing. This confirms that the universal ultraviolet behavior has no spare leading-order coercivity reserve.

## 7. Prior art and novelty audit

The provenance separates as follows.

- **Established Suzuki theory:** the localized self-adjoint Weil operator, continuity of `\lambda_a`, and the small-radius asymptotic (15) are literature-backed. Suzuki 2023 together with `WI-238` supplies the finite first-crossing framework.
- **Persisted Mathia input:** `WI-253` supplies (2) and (17); `WI-239` supplies the pure-core falsification boundary.
- **Classical transform calculus:** `\mu\mapsto[t\mapsto\int\min(h,t)d\mu(h)]` is limited-expected-value / integrated-tail calculus, and distributional second differentiation recovers `\mu`. No novelty is claimed for this abstract identity.
- **Derived here:** applying that inversion to the zeta source yields the exact prime-power jump (6), continuous recovery (11), the unique removable blind point (9)--(10), and the saturation barrier (14)--(16).

A targeted search for the combination of localized Weil sliding windows, `min(h,2r)` aperture differentiation, prime-power slope jumps, and first-crossing autocorrelation did not locate a primary source stating these zeta-specific consequences. Search absence is only audit context, not a priority claim.

## 8. Boundaries and falsification

1. This finding neither proves RH nor improves the simple-critical-zero proportion.
2. Section 3 assumes the **exact profile** `\mathcal F_v`; firstness currently supplies only (17). The inversion is structural, not a computation of the unknown zero mode.
3. Equation (17) cannot be differentiated or differenced into derivative control without new information.
4. The zero `h_0` of `w` is removable only because the autocorrelation is continuous.
5. The small-radius coefficient depends on the exact normalization in `WI-253`; a normalization change would require re-auditing (14)--(16).
6. The pure logarithmic core is only a matched control for claims based on universal first-crossing structure; it is not the zeta operator.

## Consequence for the research line

The sliding-symbol direction survives, but its target is narrower. The aperture transform itself loses no real-autocorrelation information; the loss occurs when the exact profile is replaced by the pointwise firstness inequality. The small-radius endpoint is exhausted at leading order. The next source-side target should therefore be a source-sensitive **subleading** relation for `\mathcal F_v(r)-r\lambda_r`, a zero-mode constraint on medium-radius curvature/slope jumps, or a genuine incompatibility across radii where prime-power thresholds are not asymptotically negligible.

Any future route that merely differentiates `\mathcal F_v(r)\ge r\lambda_r` or seeks a fixed relative small-radius gap should be rejected by Sections 4--5.