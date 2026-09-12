# WI-251 — Layer-cake averaging removes the smooth IMS collar cost

## Status

- **Evidence:** `EXACT-DERIVED + CLASSICAL-LAYER-CAKE + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** this strengthens the first-odd-crossing localization interface of `WI-250`. Instead of choosing one smooth cutoff and paying an `O(ell^{-2})` Lipschitz cost across a collar of width `ell`, it averages the full nested family of **sharp radial cutoffs** and obtains one finite source-flux constraint with no collar parameter. It does **not** prove RH: the remaining gate is still an arithmetic upper bound or incompatibility theorem for the signed von-Mangoldt flux on the actual first zero mode.
- **Novelty boundary:** the layer-cake/Cavalieri identity and nonlocal IMS algebra are classical. Suzuki supplies the localized closed Weil forms, while `WI-241`, `WI-245`, `WI-247`, and `WI-250` supply the zeta-specific source decomposition, resolvent expansion, first odd zero mode, and localization sign. A targeted search found standard layer-cake/coarea formulas and generic nonlocal IMS identities, but no source stating the averaged Weil-discrepancy constraint below. No priority claim is made.

## Claim

Assume RH is false and let

\[
a=a_*^-,\qquad \|v\|_2=1,
\]

be the attained first odd zero mode from `WI-247`, so

\[
q_a(v)=0,\qquad A_av=0,
\qquad \lambda_r^->0\quad(0<r<a).
\]

For `0<r<a`, let

\[
\eta_r(x):=\mathbf 1_{\{|x|<r\}},
\qquad
u_r:=\eta_r v.
\]

Although a sharp cutoff need not preserve the form domain for every `r`, it does so for almost every `r`; moreover the complete nested family is integrable in the mean form. For almost every such `r`, `nu_r` is odd, is supported in `[-r,r]`, and satisfies

\[
q_r(\nu_r)
=q_a(\nu_r)-\operatorname{Re}q_a(v,\nu_r)
\ge \lambda_r^-\|\nu_r\|_2^2.
\]

The second term vanishes by the weak zero-mode equation.

Define

\[
\delta(x,y):=\bigl||x|-|y|\bigr|.
\]

The exact layer-cake identity is

\[
\boxed{
\int_0^a
\bigl(\eta_r(x)-\eta_r(y)\bigr)^2\,dr
=\delta(x,y)
}
\]

for `|x|,|y|<a`. Consequently the entire nested family of `WI-250` localization identities integrates to

\[
\boxed{
\overline{\mathcal E}_{a,\mathrm{mean}}(v)
+
\int_0^{2a}R_v(h)\,d\nu_a(h)
\ge
\int_0^a \lambda_r^-\|\eta_rv\|_2^2\,dr,
}
\tag{1}
\]

where `d nu_a` is the signed prime-minus-density measure of `WI-241`/`WI-250`,

\[
d\nu_a(h)=
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
-e^{h/2}\mathbf 1_{(0,2a)}(h)\,dh,
\]

and

\[
\boxed{
R_v(h):=
\int_{\mathbb R}
\bigl||x+h|-|x|\bigr|
\operatorname{Re}\bigl(v(x+h)\overline{v(x)}\bigr)\,dx.
}
\tag{2}
\]

The averaged mean localization error is the explicit nonlocal form

\[
\boxed{
\overline{\mathcal E}_{a,\mathrm{mean}}(v)
=
\frac12\sum_{m=1}^{\infty}\frac1{b_m}
\iint
K_{\alpha_m}(x-y)\,\delta(x,y)
\operatorname{Re}\bigl(v(x)\overline{v(y)}\bigr)
\,dx\,dy,
}
\tag{3}
\]

with

\[
b_m=m+\frac14,
\qquad
\alpha_m=2b_m,
\qquad
K_\alpha(t)=\frac\alpha2e^{-\alpha|t|}.
\]

It obeys the radius-dependent universal bound

\[
\boxed{
\left|\overline{\mathcal E}_{a,\mathrm{mean}}(v)\right|
\le C_{\rm lc}(a)
:=\frac14\sum_{m=1}^{\infty}
\frac{\bigl(1-e^{-2b_ma}\bigr)^2}{b_m^2}
<\frac14\zeta\!\left(2,\frac54\right).
}
\tag{4}
\]

Numerically,

\[
\frac14\zeta\!\left(2,\frac54\right)
=0.2993322886267776848\ldots .
\]

Since the first-crossing term on the right of (1) is strictly positive, every hypothetical first odd zero mode therefore satisfies the single arithmetic compatibility condition

\[
\boxed{
\int_0^{2a}R_v(h)\,d\nu_a(h)
>
-C_{\rm lc}(a)
>
-\frac14\zeta\!\left(2,\frac54\right).
}
\tag{5}
\]

Thus the `O(ell^{-2})` cost in `WI-250` is not an intrinsic obstruction of the first-mode localization route. It is a cost of insisting on one smooth collar. Averaging the nested sharp cutoffs replaces it by a finite universal budget and compresses all strict-interior positivity into one signed radial-flux observable.

## 1. Sharp radial cutoffs are admissible for almost every radius

The first issue is form-domain legitimacy. No endpoint values or `H^1` regularity of `v` are assumed.

By `WI-245`, the positive part controlling the mean form is the sum

\[
Q_m(u)
=\frac1{2b_m}
\iint K_{\alpha_m}(x-y)|u(x)-u(y)|^2\,dx\,dy.
\]

For `u=eta_r v`,

\[
|\eta_r(x)v(x)-\eta_r(y)v(y)|^2
\le
2|v(x)-v(y)|^2
+2|v(y)|^2|\eta_r(x)-\eta_r(y)|^2.
\]

Integrating in `r` and using

\[
\int_0^a|\eta_r(x)-\eta_r(y)|^2\,dr
=\delta(x,y)
\le |x-y|
\]

gives

\[
\int_0^a Q_m(\eta_rv)\,dr
\le
2aQ_m(v)
+
\frac1{b_m\alpha_m}\|v\|_2^2,
\]

because

\[
\int_{\mathbb R}K_\alpha(h)|h|\,dh=\frac1\alpha.
\]

After summing over `m`,

\[
\sum_{m\ge1}\frac1{b_m\alpha_m}
=\frac12\sum_{m\ge1}\frac1{b_m^2}<\infty.
\]

The original vector `v` is already in the closed mean-form domain, so Tonelli implies

\[
\int_0^a\sum_{m\ge1}Q_m(\eta_rv)\,dr<\infty.
\]

Hence `eta_r v` belongs to the mean-form domain for almost every `r`. At fixed `a` the signed prime/density perturbation is `L^2`-bounded: only finitely many prime-power translations occur and the continuum weight has finite mass on `(0,2a)`. Therefore the full localized Weil form has the same form domain, so `eta_rv` is an admissible odd test for almost every `r`.

For such `r`, the weak equation for the attained odd zero eigenvector gives

\[
q_a(v,\eta_rv)=0.
\]

Zero-extension compatibility gives `q_a(eta_rv)=q_r(eta_rv)`, and the definition of the odd bottom eigenvalue gives

\[
q_r(\eta_rv)\ge\lambda_r^-\|\eta_rv\|_2^2.
\]

This establishes the pointwise-in-`r` inequality needed before averaging.

## 2. Layer cake converts the nested family into absolute-radius distance

For numbers `s,t in [0,a)`,

\[
\int_0^a
\bigl(\mathbf1_{\{s<r\}}-\mathbf1_{\{t<r\}}\bigr)^2dr
=|s-t|.
\]

Taking `s=|x|` and `t=|y|` gives the displayed identity for `delta(x,y)`.

Apply this first to the mean IMS kernel in `WI-250`. Fubini is legitimate after taking absolute values by the bounds in the next section, and yields exactly (3).

For the signed source part, at each shift `h` the sharp-cutoff defect is

\[
D_{\eta_r}(v;h)
=
\int
(\eta_r(x+h)-\eta_r(x))^2
\operatorname{Re}\bigl(v(x+h)\overline{v(x)}\bigr)\,dx.
\]

Integrating in `r` gives

\[
\int_0^aD_{\eta_r}(v;h)\,dr
=R_v(h).
\]

The signed measure `nu_a` has finite total variation for fixed `a`. Moreover, if the product `v(x+h)v(x)` is nonzero then both points lie in `[-a,a]`, and therefore

\[
\bigl||x+h|-|x|\bigr|
\le \min\{h,2a-h\}
\qquad(0\le h\le2a).
\]

Cauchy--Schwarz then controls the absolute source average by this bounded weight times the finite total variation of `nu_a`. Thus Fubini also applies to the signed arithmetic term.

Integrating the almost-everywhere pointwise first-crossing inequality now gives (1). If desired, one may first integrate over `[epsilon,a-epsilon]` and then pass monotonically to the endpoints; this avoids assigning any pointwise meaning at exceptional radii.

## 3. The averaged mean budget is finite and explicit

For `0<=h<=2a`, set

\[
g_a(h):=
\begin{cases}
h,&0\le h\le a,\\
2a-h,&a\le h\le2a.
\end{cases}
\]

Whenever `x,y in [-a,a]` and `h=|x-y|`,

\[
\delta(x,y)\le g_a(h).
\]

The first branch is the reverse triangle inequality. On the second branch the two points must lie on opposite sides of the origin (up to a null endpoint case), so `h=|x|+|y|` and

\[
\delta=\bigl||x|-|y|\bigr|
\le2a-h.
\]

For the exponential kernel,

\[
\int_{\mathbb R}K_\alpha(h)g_a(|h|)\,dh
=
\alpha\int_0^{2a}e^{-\alpha h}g_a(h)\,dh
=
\boxed{\frac{(1-e^{-\alpha a})^2}{\alpha}}.
\]

Using

\[
2|v(x)v(y)|\le |v(x)|^2+|v(y)|^2
\]

in (3), followed by the previous Schur bound and `||v||_2=1`, gives

\[
|\overline{\mathcal E}_{a,\mathrm{mean}}(v)|
\le
\frac12\sum_{m\ge1}\frac1{b_m}
\frac{(1-e^{-\alpha_ma})^2}{\alpha_m}.
\]

Since `alpha_m=2b_m`, this is exactly (4). In particular the averaged localization loss is uniformly bounded as the cutoff family approaches the outer boundary; no derivative of a cutoff appears.

## 4. The interior spectral contribution is genuinely positive

The right side of (1) is not merely nonnegative. Write

\[
m(r):=\|\eta_rv\|_2^2.
\]

Because `v` is normalized and supported in `[-a,a]`, `m(r)` increases to `1` as `r` increases to `a`. Hence there is `r_0<a` with `m(r_0)>0`. Choose any `r_1` with `r_0<r_1<a`. By `WI-247`, `lambda_r^->0` for every `r<a`, and its continuity gives

\[
\min_{r\in[r_0,r_1]}\lambda_r^->0.
\]

Since `m(r)>=m(r_0)` on this interval,

\[
\int_0^a\lambda_r^-m(r)\,dr
\ge
(r_1-r_0)m(r_0)
\min_{r\in[r_0,r_1]}\lambda_r^-
>0.
\]

The improper integral is finite because the integrated left side of (1) is finite and the pointwise first-crossing quantity is nonnegative. Combining strict positivity with (4) proves (5).

Equivalently, Fubini writes the positive term as

\[
\int_{-a}^a|v(x)|^2
\left(\int_{|x|}^a\lambda_r^-\,dr\right)dx,
\]

which makes clear that the averaged inequality couples the whole interior-gap profile to the spatial mass of the same first zero mode.

## 5. What this changes and what it does not

`WI-250` left three possible gates: quantitative interior gap-times-mass, a zeta-specific upper bound for signed cutoff flux, or incompatibility among several nested cutoff constraints. The present identity removes one nuisance from that list. There is no need to choose a collar width and then fight the `||chi'||_infty^2=O(ell^{-2})` cost. The entire nested family can be compressed exactly into the radial source functional `R_v`, while retaining a strictly positive integrated first-crossing term.

This does **not** supply the missing arithmetic sign. Taking absolute values of the prime source would return to the phase-blind losses already closed by `WI-248` and `WI-249`; the useful quantity is the signed integral in (5). High-frequency recurrent odd carriers from `WI-249` are also not counterexamples: they are not first zero modes and need not satisfy the weak eigen-equation used above.

The next RH-facing statement is consequently sharper than after `WI-250`: exclude a first odd zero mode by proving that its actual signed radial flux in (5) is too negative, or exploit the positive weighted gap integral in (1) together with an independent arithmetic relation. A theorem controlling arbitrary odd tests remains neither necessary nor plausible.

## Prior art and provenance

Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), supplies the localized lower-bounded self-adjoint Weil operators and closed forms used by `WI-247` and `WI-250`.

The identity

\[
\int(\mathbf1_{\{s<r\}}-\mathbf1_{\{t<r\}})^2dr=|s-t|
\]

is the elementary layer-cake/Cavalieri mechanism underlying classical coarea representations; analogous threshold-set identities are standard in nonlocal perimeter theory. Generic nonlocal IMS/double-commutator formulas are likewise classical and were already audited for `WI-250`.

A targeted search for Weil-form localization by nested sharp cutoffs, layer-cake averaging of the localized Weil quadratic form, and nonlocal coarea identities applied to the von-Mangoldt discrepancy found the classical ingredients but no primary source giving (1)--(5). This search absence is recorded only as novelty-audit context, not as evidence of priority.

## Falsification and boundary checks

The result fails if any of the following fails: the first odd zero mode of `WI-247` is not a weak form eigenvector; zero extension does not identify the form of a strict subwindow with the ambient form on a vector supported there; the `WI-245` positive-resolvent coefficients are misnormalized; the `WI-250` source sign is wrong; sharp cutoff multiplication is not form-admissible on a full-measure set of radii; or one of the Fubini passages above lacks absolute control.

The almost-everywhere cutoff-domain argument is essential. The claim does not assert that `eta_r v` belongs to the form domain for every `r`, does not assign classical boundary values to `v`, and does not smuggle in `H^1` regularity.

An ordinary operator with a genuine first crossing can also satisfy a layer-cake localization identity. Therefore the abstract first-crossing algebra plus (1) cannot prove a contradiction by itself. The remaining decisive information must distinguish the actual signed von-Mangoldt source from a generic nonlocal first-crossing operator.
