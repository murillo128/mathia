# WI-250 — First-odd-mode cutoff flux has an explicit nonlocal IMS budget

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IMS + STRUCTURAL-REDUCTION + PRIOR-ART-AUDITED`.
- **Scope:** this validates and quantifies the cutoff-flux mechanism proposed after `WI-247` and `WI-249`. It gives an exact source-side inequality satisfied by every attained first odd zero mode. It does **not** prove RH: the remaining obstruction is now a quantitative one involving the smaller-window spectral gap, interior mass, and the signed von Mangoldt cutoff flux.
- **Novelty boundary:** the double-commutator/IMS algebra is classical, and Suzuki's localized closed-form framework plus `WI-241`/`WI-245` supply the zeta-specific ingredients. A targeted audit found generic local and nonlocal IMS identities but no source deriving the explicit Weil-discrepancy budget below. No priority claim is made.

## Claim

Let `a=a_*^-` be the first odd zero radius of `WI-247`, and let `v=v_*` be a normalized attained odd zero mode,

\[
\|v\|_2=1,
\qquad
A_a v=0,
\qquad
q_a(v)=0,
\]

with

\[
\lambda_b^->0\qquad(0<b<a).
\]

Retain the exact odd source decomposition of `WI-241`,

\[
q_a(u)=Q_{\rm mean}(u)-2\Delta_\Lambda^a(u),
\]

and the signed finite-radius source measure

\[
d\nu_a(h)
=
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
-e^{h/2}\mathbf 1_{(0,2a)}(h)\,dh,
\]

so that

\[
\Delta_\Lambda^a(u)=\int_0^{2a}C_u(h)\,d\nu_a(h),
\qquad
C_u(h)=\operatorname{Re}\int u(x+h)\overline{u(x)}\,dx.
\]

Let `chi` be a real even smooth function with support in `(-b,b)`, `b<a`. Define

\[
D_\chi(v;h)
:=
\int_{\mathbb R}
(\chi(x+h)-\chi(x))^2
\operatorname{Re}\bigl(v(x+h)\overline{v(x)}\bigr)\,dx.
\]

Then the first-zero-mode equation gives the exact localization identity

\[
\boxed{
q_b(\chi v)
=
\mathcal E_{\chi,\mathrm{mean}}(v)
+
\int_0^{2a}D_\chi(v;h)\,d\nu_a(h),
}
\]

where the entire archimedean localization defect is explicitly

\[
\boxed{
\mathcal E_{\chi,\mathrm{mean}}(v)
=
\frac12\sum_{m=1}^{\infty}\frac1{b_m}
\iint_{\mathbb R^2}
K_{\alpha_m}(x-y)
(\chi(x)-\chi(y))^2
\operatorname{Re}\bigl(v(x)\overline{v(y)}\bigr)
\,dx\,dy,
}
\]

with the positive-resolvent parameters from `WI-245`,

\[
b_m=m+\frac14,
\qquad
\alpha_m=2b_m,
\qquad
K_\alpha(t)=\frac\alpha2e^{-\alpha|t|}.
\]

Although this nonlocal IMS term is not sign-definite, it has a universal Lipschitz bound:

\[
\boxed{
|\mathcal E_{\chi,\mathrm{mean}}(v)|
\le
C_{\rm IMS}\,\|\chi'\|_\infty^2\,\|v\|_2^2,
\qquad
C_{\rm IMS}
=
\frac14\zeta\!\left(3,\frac54\right)
=0.165967492192115\ldots .
}
\]

Consequently every first odd zero mode satisfies the directional arithmetic constraint

\[
\boxed{
\int_0^{2a}D_\chi(v;h)\,d\nu_a(h)
\ge
\lambda_b^-\|\chi v\|_2^2
-
\frac14\zeta\!\left(3,\frac54\right)
\|\chi'\|_\infty^2.
}
\]

This is stronger than the null equation alone and is immune to the uniform-all-odd obstruction of `WI-249`: it applies only to the attained first zero mode and imports positivity from every strict interior radius. It also identifies exactly what still has to be supplied. A successful cutoff-flux proof must make the positive quantity `lambda_b^- ||chi v||_2^2` quantitatively dominate both the nonlocal IMS cost and the allowable signed source flux for at least one, or a controlled family of, interior cutoffs.

## 1. Exact source localization and the sign

For a fixed shift `h`, the real polarization of the autocorrelation is

\[
B_h(u,w)
=
\frac12\operatorname{Re}\int
\left(
 u(x+h)\overline{w(x)}
+w(x+h)\overline{u(x)}
\right)dx,
\]

so `B_h(u,u)=C_u(h)`. Taking `u=chi v` and `w=chi^2v` gives

\[
\begin{aligned}
C_{\chi v}(h)-B_h(v,\chi^2v)
&=\int
\left[
\chi(x+h)\chi(x)
-rac{\chi(x+h)^2+\chi(x)^2}{2}
\right]
\operatorname{Re}\bigl(v(x+h)\overline{v(x)}\bigr)dx\\
&=-\frac12D_\chi(v;h).
\end{aligned}
\]

Integrating against `nu_a` therefore yields

\[
\Delta_\Lambda^a(\chi v)
-
\operatorname{Re}\Delta_\Lambda^a(v,\chi^2v)
=
-\frac12\int_0^{2a}D_\chi(v;h)\,d\nu_a(h).
\]

The factor and sign matter. Since the Weil form contains `-2 Delta`, its contribution to

\[
q_a(\chi v)-\operatorname{Re}q_a(v,\chi^2v)
\]

is **plus** the signed flux integral. This verifies the sign proposed in `CLUE-first-odd-mode-cutoff-flux-constraint.md`; no absolute value or triangle inequality has been inserted into the arithmetic term.

Because `v` is an eigenvector with eigenvalue zero of the odd self-adjoint realization, the weak eigen-equation gives

\[
q_a(v,w)=0
\]

for every admissible odd form-domain `w`. The function `chi^2 v` is odd, so

\[
\operatorname{Re}q_a(v,\chi^2v)=0.
\]

Finally `chi v` is supported in `(-b,b)`, and the zero-extension compatibility used in `WI-247` gives

\[
q_a(\chi v)=q_b(\chi v).
\]

Thus only the mean-sector localization error remains to be computed.

## 2. The mean sector has an exact nonlocal IMS formula

`WI-245` gives the positive-resolvent expansion

\[
M(z)-M(0)
=
\sum_{m=1}^{\infty}
\frac1{b_m}\frac{z^2}{z^2+\alpha_m^2}.
\]

The multiplier `alpha^2/(alpha^2+z^2)` is convolution by

\[
K_\alpha(t)=\frac\alpha2e^{-\alpha|t|},
\qquad
\int_{\mathbb R}K_\alpha(t)dt=1.
\]

Hence the `m`-th positive mean piece is

\[
Q_m(u)
=
\frac1{b_m}\langle u,(I-K_{\alpha_m})u\rangle.
\]

For any real multiplier `chi`, the identity part cancels exactly in

\[
Q_m(\chi v)-\operatorname{Re}Q_m(v,\chi^2v).
\]

Symmetrizing the convolution term gives

\[
Q_m(\chi v)-\operatorname{Re}Q_m(v,\chi^2v)
=
\frac1{2b_m}
\iint
K_{\alpha_m}(x-y)
(\chi(x)-\chi(y))^2
\operatorname{Re}\bigl(v(x)\overline{v(y)}\bigr)
\,dx\,dy.
\]

The constant `M(0)||u||_2^2` also cancels because

\[
\|\chi v\|_2^2=\langle v,\chi^2v\rangle.
\]

Summing gives the displayed formula for `mathcal E_{chi,mean}`. This is the integral-kernel version of the classical double-commutator/IMS identity

\[
-\frac12\langle v,[\chi,[\chi,A]]v\rangle,
\]

but the quadratic-form calculation above is primary and does not assume that `v` lies in the operator domain of the individual resolvent pieces or has classical endpoint regularity.

## 3. The complete archimedean localization loss has a closed constant

Let `L=||chi'||_infty`. By symmetry of `K_alpha` and

\[
|\operatorname{Re}(v(x)\overline{v(y)})|
\le\frac{|v(x)|^2+|v(y)|^2}{2},
\]

we obtain

\[
|\mathcal E_{\chi,\mathrm{mean}}(v)|
\le
\frac12\sum_{m\ge1}\frac1{b_m}
\int |v(x)|^2
\left[
\int K_{\alpha_m}(x-y)(\chi(x)-\chi(y))^2dy
\right]dx.
\]

The Lipschitz bound gives

\[
(\chi(x)-\chi(y))^2\le L^2(x-y)^2,
\]

while

\[
\int_{\mathbb R}K_\alpha(h)h^2dh
=
\frac{2}{\alpha^2}.
\]

Therefore

\[
|\mathcal E_{\chi,\mathrm{mean}}(v)|
\le
L^2\|v\|_2^2
\sum_{m=1}^{\infty}\frac1{b_m\alpha_m^2}.
\]

Since `alpha_m=2b_m`,

\[
\sum_{m=1}^{\infty}\frac1{b_m\alpha_m^2}
=
\frac14\sum_{m=1}^{\infty}\frac1{(m+1/4)^3}
=
\frac14\zeta\!\left(3,\frac54\right).
\]

No prime estimate enters this bound. It quantifies the entire mean-sector price of localization in the normalization already used by `WI-241`--`WI-247`.

## 4. Form-domain justification

The calculation can be started on the smooth odd core and passed to Suzuki's closed form without granting `H^1` regularity to the first zero mode.

For each positive resolvent piece,

\[
Q_m(u)
=
\frac1{2b_m}
\iint K_{\alpha_m}(x-y)|u(x)-u(y)|^2dxdy.
\]

If `chi` is bounded and Lipschitz, then

\[
|\chi(x)u(x)-\chi(y)u(y)|^2
\le
2\|\chi\|_\infty^2|u(x)-u(y)|^2
+2|u(y)|^2|\chi(x)-\chi(y)|^2.
\]

After integration and summation, the second term is controlled by the convergent series

\[
2\|\chi'\|_\infty^2
\sum_{m\ge1}\frac1{b_m\alpha_m^2}\|u\|_2^2.
\]

Thus smooth bounded Lipschitz multiplication preserves the mean form domain. At fixed `a`, the signed source perturbation is an `L^2`-bounded quadratic form: there are finitely many translated prime-power terms, and the continuum comparison has finite total weight on `(0,2a)`. Hence the full localized form has the same form domain as its mean part, multiplication by `chi` and `chi^2` is admissible, and the core identity passes to the attained eigenvector by form-norm approximation.

This is exactly the domain issue flagged by the clue. No boundary value or classical double commutator for `v` is required.

## 5. Interior positivity becomes a directional source constraint

Since `chi v` is odd and supported in `(-b,b)`, the definition of the smaller-window bottom eigenvalue gives

\[
q_b(\chi v)
\ge
\lambda_b^-\|\chi v\|_2^2.
\]

Combining this with the exact localization identity yields

\[
\int_0^{2a}D_\chi(v;h)d\nu_a(h)
\ge
\lambda_b^-\|\chi v\|_2^2
-
\mathcal E_{\chi,\mathrm{mean}}(v),
\]

and the universal IMS bound gives the claimed explicit inequality.

This is a genuine first-crossing restriction. The recurrent carriers of `WI-249` were chosen only to make the signed source large; they were not required to obey the weak zero-mode equation or all smaller-window positivity inequalities. Any candidate countergeometry for the present route must now satisfy the displayed flux inequality for **every** admissible interior even cutoff simultaneously.

Nested cutoffs therefore do provide a coherent family of exact constraints. For two cutoffs `chi_1,chi_2`, subtraction retains the signed difference

\[
\int(D_{\chi_1}-D_{\chi_2})d\nu_a
\]

rather than replacing either source term by an absolute norm. What is not yet available is a quantitative relation turning that family into a positive collar-mass or phase-exclusion theorem.

## 6. What the identity does and does not buy

The reduction exposes three independent quantities that a closing argument must control.

First, continuity from `WI-247` gives only

\[
\lambda_b^->0\quad(b<a),
\qquad
\lambda_b^-\downarrow0\quad(b\uparrow a),
\]

with no lower rate near the first crossing. Second, strict non-support of `v` in a smaller interval does not give a quantitative lower bound for `||chi v||_2`; concentration in the outer collar has not been excluded. Third, although the mean IMS error is now completely controlled, `WI-249` rules out a useful uniform upper bound for signed prime discrepancy over the whole odd window.

These facts prevent an automatic bootstrap from the localization identity. For a cutoff transitioning across a collar of width `ell`, the explicit cost behaves like `O(ell^{-2})`, while no theorem presently forces `lambda_b^- ||chi v||_2^2` to stay comparable. Letting `b` approach `a` therefore makes the known positive term weaker, not stronger.

Conversely, the formula sharply narrows the remaining theorem. It would suffice to prove one of the following on the actual first-zero-mode class: a quantitative interior-mass estimate coupled to a lower bound for `lambda_b^-`; a signed-source flux upper bound that is stronger than the right-hand side above; or a multi-cutoff inequality in which the source phases cannot satisfy all nested flux constraints simultaneously. Any such input would be genuinely zeta-specific or first-mode-specific and would evade the all-odd recurrence barrier.

## 7. Stress tests

1. **Constant multiplier.** If `chi` is constant, both `D_chi` and the mean localization error vanish, as required.
2. **Sign calibration.** The source contribution enters with a plus sign because the discrepancy polarization produces `-D_chi/2` while the Weil form contains `-2 Delta`. Reversing either sign would invalidate the first-mode inequality.
3. **No positivity of the IMS kernel form.** `K_alpha` is positive, but `Re(v(x) overline{v(y)})` need not be. The derivation uses an absolute bound, not a false positivity claim.
4. **No hidden `H^1` assumption.** The multiplier argument is made at the level of the positive resolvent form and the bounded finite-radius source perturbation; the first zero mode need only lie in Suzuki's closed form/operator domain.
5. **Ordinary first crossings are not contradicted.** A Dirichlet Schrödinger operator can obey analogous localization identities at a genuine first crossing. The present result is therefore a constraint, not an abstract contradiction; a closing step must use the actual signed Weil source.
6. **WI-249 remains intact.** Its recurrent high-frequency odd carriers need not satisfy the zero-mode equation. The new inequality does not assert a uniform discrepancy bound over all odd tests.
7. **No percentage claim.** This finding belongs to the defect-elimination/RH-facing branch of the canonical mandate and does not change the current unconditional simple-critical proportion.

## Prior-art and provenance audit

The operator/form framework is anchored in Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), which constructs the localized lower-bounded self-adjoint Weil operators on finite intervals and supplies the closed-form setting used in `WI-247`. The exact odd source decomposition and density-one cancellation are reconstructed in `WI-241`; the positive exponential-resolvent expansion is reconstructed in `WI-245`; the finite attained first odd zero mode is established in `WI-247`.

The algebraic localization pattern is classical IMS/double-commutator theory. A targeted search for cutoff localization of the Weil quadratic form, nonlocal IMS identities, and prime-discrepancy localization found generic local/nonlocal IMS formulas and Suzuki's operator framework, but no primary source stating the zeta-specific signed identity with the explicit Hurwitz-zeta constant above. This search absence is only audit context and is not a priority claim.

## Falsification and next gate

The finding fails if any of the following occurs: the `WI-241` source sign/normalization is wrong; the real polarization gives a factor different from `-1/2`; the `WI-245` positive-resolvent coefficients or exponential-kernel normalization are wrong; multiplication by a smooth Lipschitz cutoff fails to preserve Suzuki's closed form domain; zero extension changes the localized form for a vector supported in a strict subinterval; or the attained zero eigenvector does not satisfy the weak form equation against `chi^2v`.

Assuming these checks stand, the next gate is no longer to derive an IMS identity. It is to obtain a **quantitative first-mode estimate** that makes at least one nested cutoff inequality coercive: either a lower bound for `lambda_b^- ||chi v||_2^2`, a zeta-specific upper bound for the signed flux `int D_chi dnu_a`, or a compatibility theorem showing that the actual prime phases cannot satisfy the full family of nested cutoff constraints at a first odd crossing.
