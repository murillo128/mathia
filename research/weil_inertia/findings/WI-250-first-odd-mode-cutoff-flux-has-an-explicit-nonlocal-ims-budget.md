# WI-250 — First-odd-mode cutoff flux has an explicit nonlocal IMS budget

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IMS + STRUCTURAL-REDUCTION + PRIOR-ART-AUDITED`.
- **Scope:** this validates and quantifies the cutoff-flux mechanism proposed after `WI-247` and `WI-249`. It gives an exact source-side inequality satisfied by every attained first odd zero mode. It does **not** prove RH: the remaining obstruction is quantitative and involves the smaller-window spectral gap, interior mass, and the signed von Mangoldt cutoff flux.
- **Novelty boundary:** the double-commutator/IMS algebra is classical. Suzuki's localized closed-form framework plus `WI-241`, `WI-245`, and `WI-247` supply the zeta-specific ingredients. A targeted audit found generic local/nonlocal IMS identities but no source deriving the explicit Weil-discrepancy budget below. No priority claim is made.

## Claim

Let `a=a_*^-` be the first odd zero radius of `WI-247`, and let `v=v_*` be a normalized attained odd zero mode,

\[
\|v\|_2=1,\qquad A_av=0,\qquad q_a(v)=0,
\]

with `lambda_b^->0` for every `0<b<a`. Retain the exact odd decomposition from `WI-241`,

\[
q_a(u)=Q_{\rm mean}(u)-2\Delta_\Lambda^a(u),
\]

and write the discrepancy with the signed finite-radius measure

\[
d\nu_a(h)=
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
-e^{h/2}\mathbf 1_{(0,2a)}(h)\,dh,
\]

so that

\[
\Delta_\Lambda^a(u)=\int_0^{2a}C_u(h)\,d\nu_a(h),
\qquad
C_u(h)=\operatorname{Re}\int u(x+h)\overline{u(x)}\,dx.
\]

For a real even smooth cutoff `chi` supported in `(-b,b)`, define

\[
D_\chi(v;h)=
\int_{\mathbb R}(\chi(x+h)-\chi(x))^2
\operatorname{Re}\bigl(v(x+h)\overline{v(x)}\bigr)\,dx.
\]

Then the first-zero-mode equation gives the exact localization identity

\[
\boxed{
q_b(\chi v)=
\mathcal E_{\chi,\mathrm{mean}}(v)
+
\int_0^{2a}D_\chi(v;h)\,d\nu_a(h).
}
\]

The archimedean localization defect is

\[
\boxed{
\mathcal E_{\chi,\mathrm{mean}}(v)=
\frac12\sum_{m=1}^{\infty}\frac1{b_m}
\iint K_{\alpha_m}(x-y)(\chi(x)-\chi(y))^2
\operatorname{Re}\bigl(v(x)\overline{v(y)}\bigr)\,dx\,dy,
}
\]

where, as in `WI-245`,

\[
b_m=m+\frac14,
\qquad
\alpha_m=2b_m,
\qquad
K_\alpha(t)=\frac\alpha2e^{-\alpha|t|}.
\]

This term is not sign-definite, but it has the universal bound

\[
\boxed{
|\mathcal E_{\chi,\mathrm{mean}}(v)|
\le
\frac14\zeta\!\left(3,\frac54\right)
\|\chi'\|_\infty^2\|v\|_2^2,
}
\]

with

\[
\frac14\zeta\!\left(3,\frac54\right)
=0.165967492192115\ldots .
\]

Consequently every first odd zero mode satisfies

\[
\boxed{
\int_0^{2a}D_\chi(v;h)\,d\nu_a(h)
\ge
\lambda_b^-\|\chi v\|_2^2
-
\frac14\zeta\!\left(3,\frac54\right)\|\chi'\|_\infty^2.
}
\]

This is a genuinely first-mode-specific constraint: unlike the uniform all-odd estimates closed by `WI-249`, it imports positivity from every strict interior radius through the same attained zero mode.

## 1. Exact source localization and sign

For fixed `h`, real polarization of the autocorrelation gives

\[
B_h(u,w)=\frac12\operatorname{Re}\int
\left(u(x+h)\overline{w(x)}+w(x+h)\overline{u(x)}\right)dx,
\]

with `B_h(u,u)=C_u(h)`. Taking `u=chi v` in the quadratic term and polarizing against `chi^2v` yields

\[
\begin{aligned}
C_{\chi v}(h)-B_h(v,\chi^2v)
&=\int\left[
\chi(x+h)\chi(x)-
\frac{\chi(x+h)^2+\chi(x)^2}{2}
\right]
\operatorname{Re}\bigl(v(x+h)\overline{v(x)}\bigr)dx\\
&=-\frac12D_\chi(v;h).
\end{aligned}
\]

Therefore

\[
\Delta_\Lambda^a(\chi v)
-
\operatorname{Re}\Delta_\Lambda^a(v,\chi^2v)
=-\frac12\int_0^{2a}D_\chi(v;h)\,d\nu_a(h).
\]

Because the Weil form contains `-2 Delta`, the source contribution to

\[
q_a(\chi v)-\operatorname{Re}q_a(v,\chi^2v)
\]

is **plus** the signed flux integral. This fixes both the sign and the factor proposed in `CLUE-first-odd-mode-cutoff-flux-constraint.md` without taking absolute values of the arithmetic source.

The attained zero eigenvector obeys the weak form equation `q_a(v,w)=0` for every admissible odd form-domain `w`; since `chi` is even, `chi^2v` is odd. Hence `q_a(v,chi^2v)=0`. Also `chi v` is supported in `(-b,b)`, so the zero-extension compatibility used in `WI-247` gives `q_a(chi v)=q_b(chi v)`. Only the mean localization term remains.

## 2. Exact nonlocal IMS formula for the mean sector

`WI-245` gives

\[
M(z)-M(0)=
\sum_{m=1}^{\infty}\frac1{b_m}
\frac{z^2}{z^2+\alpha_m^2}.
\]

The multiplier `alpha^2/(alpha^2+z^2)` is convolution by `K_alpha`. Thus the `m`-th positive mean piece is

\[
Q_m(u)=\frac1{b_m}\langle u,(I-K_{\alpha_m})u\rangle.
\]

For real `chi`, the identity part cancels in
`Q_m(chi v)-Re Q_m(v,chi^2v)`. Symmetrizing the convolution term gives exactly

\[
Q_m(\chi v)-\operatorname{Re}Q_m(v,\chi^2v)
=
\frac1{2b_m}
\iint K_{\alpha_m}(x-y)(\chi(x)-\chi(y))^2
\operatorname{Re}\bigl(v(x)\overline{v(y)}\bigr)\,dx\,dy.
\]

The constant `M(0)||u||_2^2` also cancels because `||chi v||_2^2=<v,chi^2v>`. Summing proves the displayed formula for `mathcal E_{chi,mean}`. Algebraically this is the integral-kernel version of the classical IMS/double-commutator identity, but the quadratic-form derivation is primary and does not grant classical endpoint regularity to `v`.

## 3. Closed Lipschitz cost

Using

\[
|\operatorname{Re}(v(x)\overline{v(y)})|
\le\frac{|v(x)|^2+|v(y)|^2}{2}
\]

and symmetry of `K_alpha`,

\[
|\mathcal E_{\chi,\mathrm{mean}}(v)|
\le
\frac12\sum_{m\ge1}\frac1{b_m}
\int |v(x)|^2
\left[\int K_{\alpha_m}(x-y)(\chi(x)-\chi(y))^2dy\right]dx.
\]

If `L=||chi'||_infty`, then `(chi(x)-chi(y))^2<=L^2(x-y)^2`, while

\[
\int_{\mathbb R}K_\alpha(h)h^2dh=\frac{2}{\alpha^2}.
\]

Hence

\[
|\mathcal E_{\chi,\mathrm{mean}}(v)|
\le
L^2\|v\|_2^2
\sum_{m=1}^{\infty}\frac1{b_m\alpha_m^2}
=
\frac14\zeta\!\left(3,\frac54\right)L^2\|v\|_2^2.
\]

No prime estimate enters this constant.

## 4. Form-domain justification

The calculation may be proved first on Suzuki's smooth odd core and then passed to the closed form. For each positive resolvent piece,

\[
Q_m(u)=\frac1{2b_m}\iint K_{\alpha_m}(x-y)|u(x)-u(y)|^2dxdy.
\]

For bounded Lipschitz `chi`,

\[
|\chi(x)u(x)-\chi(y)u(y)|^2
\le
2\|\chi\|_\infty^2|u(x)-u(y)|^2
+2|u(y)|^2|\chi(x)-\chi(y)|^2.
\]

The second term is controlled after summation by

\[
2\|\chi'\|_\infty^2
\sum_{m\ge1}\frac1{b_m\alpha_m^2}\|u\|_2^2<\infty.
\]

Thus smooth bounded Lipschitz multiplication preserves the mean form domain. At fixed `a`, the signed source perturbation is `L^2`-bounded: there are only finitely many translated prime-power terms and the continuum comparison has finite total weight on `(0,2a)`. Therefore the full localized form has the same form domain as its mean part, `chi v` and `chi^2v` are admissible, and the core identity extends by form-norm closure. No hidden `H^1` hypothesis is used.

## 5. Interior positivity and the remaining gate

Since `chi v` is odd and supported in `(-b,b)`,

\[
q_b(\chi v)\ge\lambda_b^-\|\chi v\|_2^2.
\]

Combining this with the exact localization identity and the Lipschitz cost proves the claimed directional source inequality. It must hold for every admissible interior even cutoff, so nested cutoffs give a coherent family of exact constraints on one and the same first zero mode.

The identity does **not** yet close the argument. `WI-247` supplies only `lambda_b^->0` for `b<a` and continuity to zero as `b` approaches `a`; it gives no useful lower rate. Non-support in a smaller interval does not give a quantitative lower bound for `||chi v||_2`. And `WI-249` blocks a useful uniform upper bound for signed discrepancy over the entire odd window. For a cutoff transitioning across a collar of width `ell`, the explicit IMS cost is naturally `O(ell^{-2})`, while the presently known positive term need not stay comparable.

Thus the next theorem is sharply specified: prove, on the actual first-zero-mode class, either a quantitative lower bound for `lambda_b^- ||chi v||_2^2`, a zeta-specific upper bound for the signed flux `int D_chi dnu_a`, or a multi-cutoff compatibility theorem showing that the prime phases cannot satisfy all nested inequalities simultaneously.

## 6. Stress tests and boundaries

1. If `chi` is constant, both `D_chi` and the mean localization error vanish.
2. The source sign is calibrated directly: discrepancy polarization gives `-D_chi/2`, and the Weil form contains `-2 Delta`.
3. The mean IMS term is not assumed positive; its bound uses `|Re(v(x) overline{v(y)})|`.
4. No classical endpoint values or `H^1` regularity of the first zero mode are assumed.
5. Ordinary operators with a genuine first crossing can satisfy analogous IMS identities, so first-crossing minimality plus localization algebra alone cannot prove a contradiction. The closing input must use the actual Weil source.
6. `WI-249` remains intact: its high-frequency recurrent carriers are not weak zero modes and need not satisfy the nested first-mode constraints.
7. This finding makes no new simple-zero proportion claim; it belongs to the canonical defect-elimination branch.

## Prior art and provenance

Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), supplies the localized lower-bounded self-adjoint Weil operators and closed-form framework used by `WI-247`. `WI-241` reconstructs the odd density-one cancellation and signed discrepancy; `WI-245` reconstructs the positive exponential-resolvent expansion; `WI-247` establishes the finite attained first odd zero mode under RH failure.

The localization algebra is classical IMS/double-commutator theory. A targeted search for cutoff localization of the Weil quadratic form, nonlocal IMS identities, and prime-discrepancy localization found generic IMS formulas and Suzuki's operator framework, but no primary source stating this zeta-specific signed cutoff identity with the explicit Hurwitz-zeta localization constant. Search absence is recorded only as audit context, not as a priority claim.

## Falsification

The result fails if the `WI-241` source sign/normalization is wrong, if real polarization gives a factor other than `-1/2`, if the `WI-245` resolvent coefficients or exponential-kernel normalization are wrong, if smooth Lipschitz multiplication does not preserve Suzuki's closed form domain, if zero extension changes the form on a strict subinterval, or if the attained zero eigenvector does not satisfy the weak form equation against `chi^2v`.
