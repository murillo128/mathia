# WI-254 — The sliding-aperture profile is invertible, but small-scale firstness is asymptotically saturated

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

`WI-253` shows that a hypothetical first unrestricted localized Weil zero mode produces a continuum of positive sliding-window fluxes. The aperture parameter contains more exact information than was used there: after the window center has been averaged out, the whole profile is a classical `min`-transform of a signed source-weighted autocorrelation measure, so its distributional second derivative recovers that measure exactly. In particular, prime-power thresholds appear as literal slope jumps and the archimedean part recovers the continuous autocorrelation away from one explicit harmless zero of its weight.

This does **not** turn the positivity inequality of `WI-253` into a contradiction. Pointwise lower bounds on the profile cannot be differentiated to control those slope jumps. Moreover the aperture family is asymptotically saturated at the small-radius end: for every normalized first-crossing zero mode,

\[
\mathcal F_v(r)\sim r\log(1/r),
\qquad
r\lambda_r\sim r\log(1/r),
\qquad
\frac{\mathcal F_v(r)}{r\lambda_r}\longrightarrow1.
\]

Thus no argument based on a uniform multiplicative reserve over the firstness lower bound can close the problem near `r=0`. The live information must be subleading, medium-radius, threshold-coupled, or imported from the zero-mode equation itself.

## 1. Exact `min`-transform form

Retain the notation of `WI-253`. Under RH failure let `a_*` be the first unrestricted crossing, choose a normalized zero mode `v`, and put

\[
C(h):=\operatorname{Re}\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx,
\qquad C(0)=1.
\]

Since translation is strongly continuous on `L^2`, `C` is continuous and even. Since `v` is supported in `[-a_*,a_*]`, `C(h)=0` for `|h|\ge2a_*` in the `L^2` autocorrelation sense.

Write

\[
\kappa(h)=\frac{e^{-5h/2}}{1-e^{-2h}},
\qquad
w(h):=\kappa(h)-e^{h/2},
\]

and define the finite signed measure on `(0,2a_*)`

\[
d\mu_v(h)
:=C(h)\left[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
+w(h)\,dh
\right].
\tag{1}
\]

The `1/h` singularity of `w` at zero prevents treating its density alone as a finite measure on a neighborhood of zero, but every truncated interval `[\epsilon,2a_*]` is finite and the weighted `min`-transform below is locally integrable. `WI-253` is exactly

\[
\boxed{
\mathcal F_v(r)=
\int_0^{2a_*}\min(h,2r)\,d\mu_v(h),
\qquad 0<r<a_*.
}
\tag{2}
\]

It is cleaner to set `t=2r` and

\[
L_v(t):=\mathcal F_v(t/2)
=\int_0^{2a_*}\min(h,t)\,d\mu_v(h).
\tag{3}
\]

On every compact subinterval of `(0,2a_*)`, elementary limited-expectation calculus gives, distributionally,

\[
\boxed{L_v''=-\mu_v.}
\tag{4}
\]

The abstract identity (4) is classical `min`-kernel / limited-expected-value inversion; no novelty is claimed for that calculus. The zeta-specific content is what the known prime atoms and archimedean density make (4) say about the first-crossing autocorrelation.

## 2. Prime powers are exact slope jumps

Away from the thresholds `r_n=(\log n)/2`, differentiating (2) is legitimate because the lower endpoint `2r` stays away from the singularity at zero. One obtains

\[
\boxed{
\mathcal F_v'(r)
=2\sum_{\log n>2r}\frac{\Lambda(n)}{\sqrt n}C(\log n)
+2\int_{2r}^{2a_*}w(h)C(h)\,dh.
}
\tag{5}
\]

At a prime-power threshold `r_n=(\log n)/2` with `\log n<2a_*`, the continuous part has no jump while the corresponding atom changes from the linear to the saturated branch. Hence

\[
\boxed{
\mathcal F'_{v,+}(r_n)-\mathcal F'_{v,-}(r_n)
=-2\frac{\Lambda(n)}{\sqrt n}C(\log n).
}
\tag{6}
\]

Thus the source atom is not merely visible qualitatively: if the aperture profile itself is known, its one-sided slope jump reads off the real autocorrelation at that exact prime-power shift.

Between thresholds a second differentiation gives

\[
\boxed{
\mathcal F_v''(r)=-4w(2r)C(2r).
}
\tag{7}
\]

Equivalently, on `(0,a_*)` in the distributional sense,

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

Equations (6)--(8) are the exact `r`-variation requested by the live sliding-symbol clue.

## 3. The continuous archimedean weight loses only one point

The coefficient `w` has exactly one zero on the positive axis. Put `x=e^h>1`. Then

\[
\kappa(h)=\frac{x^{-1/2}}{x^2-1},
\]

so

\[
w(h)=0
\iff
x^3-x-1=0.
\tag{9}
\]

The polynomial is strictly increasing for `x>1`, hence it has one root there, the plastic constant

\[
\rho=1.3247179572447460259\ldots.
\]

Therefore

\[
h_0=\log\rho
=0.2811995743229618465\ldots,
\qquad
r_0=h_0/2
=0.1405997871614809233\ldots
\tag{10}
\]

is the unique positive point at which (7) cannot be divided directly by the known density. For every non-threshold `h\ne h_0`,

\[
\boxed{
C(h)=-\frac{\mathcal F_v''(h/2)}{4w(h)}.
}
\tag{11}
\]

At prime-power shifts the same value is independently encoded by (6). At `h_0`, continuity of the autocorrelation recovers the missing value from either side; `e^{h_0}=\rho` is not an integer, so it does not collide with a von Mangoldt atom.

Consequently the **exact aperture profile** `r\mapsto\mathcal F_v(r)` determines the entire real autocorrelation `C(h)` on `(0,2a_*)`, and hence on the real line by evenness and compact support. Equivalently it determines the even cosine-spectral information encoded by `C`. This statement must not be strengthened to recovery of an arbitrary unsymmetrized complex spectral density: `WI-253` deliberately passed to the real autocorrelation.

This also clarifies what is and is not gained by using many radii. The family is not a weak collection of unrelated scalar tests; as an identity it is information-complete at the real-autocorrelation level. Any remaining loss comes from knowing only an inequality for that profile, not from the `min` transform itself.

## 4. The small-aperture family is universally saturated at leading order

The same formula gives a sharp barrier at `r\downarrow0`. Since

\[
\kappa(h)=\frac1{2h}+O(1)
\qquad(h\downarrow0)
\tag{12}
\]

and `C(h)\to C(0)=1`, split the `\kappa` contribution in (2) at a fixed sufficiently small `\delta>0`. For `r<\delta/2`,

\[
\begin{aligned}
\int_0^{2a_*}\min(h,2r)\kappa(h)C(h)\,dh
&=
2r\int_{2r}^{\delta}\left(\frac{C(h)}{2h}+O(1)\right)dh+O(r)\\
&=r\log(1/r)+o\!\left(r\log(1/r)\right).
\end{aligned}
\tag{13}
\]

The interval `0<h<2r` contributes only `O(r)`. The smooth `-e^{h/2}` density contributes `O(r)`, as do all prime-power atoms: once `r<(\log2)/2`, every fixed atom is on the linear branch `2r`, and only finitely many atoms occur below `2a_*`. Hence

\[
\boxed{
\mathcal F_v(r)
=r\log(1/r)+o\!\left(r\log(1/r)\right).
}
\tag{14}
\]

Independently, Suzuki's Theorem 1.4 gives for the actual localized Weil ground-state energy

\[
\boxed{
\lambda_r
=\log(1/r)+\mu_1-\log(2\pi)+\psi(2)-1+O(r)
}
\qquad(r\downarrow0),
\tag{15}
\]

with `\mu_1>0`. Therefore

\[
\boxed{
\frac{\mathcal F_v(r)}{r\lambda_r}\longrightarrow1.
}
\tag{16}
\]

The firstness inequality of `WI-253`, `\mathcal F_v(r)\ge r\lambda_r>0`, is thus sharp at the universal leading scale. In particular, for no fixed `\epsilon>0` can one prove

\[
\mathcal F_v(r)\ge(1+\epsilon)r\lambda_r
\]

for all sufficiently small `r` from the actual first-crossing profile. Any contradiction must see the subleading term or leave the small-radius regime.

Primary source for (15): Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), Theorem 1.4: <https://arxiv.org/abs/2606.09096>.

## 5. Why threshold jumps cannot be read from positivity alone

`WI-253` proves

\[
\mathcal F_v(r)\ge r\lambda_r>0,
\tag{17}
\]

but (17) cannot be differentiated. In particular, (6) does **not** imply a sign for `C(\log n)`. Pointwise positivity or a positive lower envelope places no sign restriction on a derivative jump. The elementary family

\[
G(r)=Mr+J(r-r_0)_+
\tag{18}
\]

has an arbitrary prescribed slope jump `J` at `r_0`; choosing `M>|J|` makes `G(r)>0` for every `r>0` on a bounded interval. This is only a logical stress test, not a matched zeta countermodel, but it decisively forbids differentiating (17) as a route to prime autocorrelation signs.

Accordingly, the slope-jump formulas become useful only if another exact relation controls `\mathcal F_v` more tightly than pointwise firstness does. Candidates include the zero-mode equation, a subleading small-`r` expansion with a source-sensitive constant, or coupled information at medium radii. Merely sampling more radii and differentiating their positivity inequalities adds no justified sign information.

## 6. Stress test against the pure logarithmic core

`WI-239` proves that the universal logarithmic core itself has a genuine attained first zero mode. That countermodel already kills arguments using only nested domains, compactness, continuity, or the existence of a first crossing. The present result respects that boundary in two ways.

First, the invertibility statement uses the **actual zeta source decomposition** of `WI-253`: the von Mangoldt atoms and the explicit archimedean density `w`. It is therefore not a generic consequence of firstness. Second, the small-`r` saturation (16) is driven by the same logarithmic singularity that underlies the pure-core crossing. It confirms rather than evades the warning of `WI-239`: the universal ultraviolet behavior has no spare leading-order coercivity reserve.

The first potentially zeta-specific information in this aperture representation must therefore occur after subtracting that universal leading behavior or at radii where the prime thresholds and the full source profile matter.

## 7. Prior art and novelty audit

The load-bearing provenance separates cleanly.

- **Established Suzuki theory:** the localized self-adjoint Weil operator, continuity of `\lambda_a`, and the small-radius asymptotic (15) are from Suzuki 2026. Suzuki's 2023 nondegeneracy theorem and `WI-238` supply the finite first-crossing framework.
- **Established local Mathia input:** `WI-253` supplies the exact sliding-window identity (2) and the firstness lower bound (17). `WI-239` supplies the pure-core falsification boundary.
- **Classical transform calculus:** the map `\mu\mapsto[t\mapsto\int\min(h,t)d\mu(h)]` is the classical limited-expected-value / integrated-tail transform; distributional second differentiation recovers the underlying signed measure. No novelty is claimed for this abstract inversion.
- **Mathia deduction recorded here:** specializing that inversion to the zeta source gives the explicit prime-power jump formula (6), continuous recovery (11), the unique archimedean blind point (9)--(10), and the small-aperture saturation (14)--(16). The strategic negative conclusion is that neither derivative signs from pointwise positivity nor a uniform small-radius multiplicative reserve can close the first-crossing problem.

A targeted search for the exact combination of localized Weil sliding windows, `min(h,2r)` aperture differentiation, prime-power slope jumps, and first-crossing autocorrelation did not locate a primary source stating these zeta-specific consequences. The search absence is recorded only as novelty-audit context and is not a priority claim.

## 8. Boundaries and falsification

1. This finding does not prove RH and does not improve the simple-critical-zero percentage.
2. Recovery in Section 3 assumes the **exact profile** `\mathcal F_v`, whereas firstness currently supplies only the lower bound (17). The inversion is structural information, not an algorithm for computing the unknown zero mode.
3. Equation (17) cannot be differentiated or subtracted at two radii without additional control on `\lambda_r` and on the profile; doing so would be an invalid strengthening.
4. The unique zero `h_0` of `w` is removable only because `C` is continuous. No pointwise regularity of `v` is used.
5. The asymptotic (14) uses only normalization, compact support, continuity of `C`, and the explicit `\kappa(h)=1/(2h)+O(1)` singularity. If any coefficient in the `WI-253` decomposition is off by a factor, the matching coefficient in (14) changes and (16) must be re-audited.
6. The pure logarithmic core is not the zeta operator. It is used only to stress-test claims that pretend firstness or the universal singularity alone is coercive.

## Consequence for the research line

The sliding-symbol clue survives, but its decisive test is narrower. The aperture transform itself loses no real-autocorrelation information; the loss lies in replacing the exact profile by the pointwise firstness inequality. The small-radius endpoint is also exhausted at leading order. The next source-side target should therefore be one of:

- derive a source-sensitive **subleading** relation for `\mathcal F_v(r)-r\lambda_r` as `r\downarrow0`;
- use the zero-mode equation to constrain the curvature or slope jumps of the exact aperture profile;
- or find a genuine incompatibility across medium radii, where prime-power thresholds are not asymptotically negligible.

A future argument that merely differentiates `\mathcal F_v(r)\ge r\lambda_r` or seeks a fixed relative small-radius gap should be rejected immediately by Sections 4--5.