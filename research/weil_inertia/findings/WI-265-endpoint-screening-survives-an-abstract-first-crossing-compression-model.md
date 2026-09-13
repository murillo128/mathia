# WI-265 — endpoint screening survives an abstract first-crossing compression model

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + ABSTRACT-BARRIER + PRIOR-ART-AUDITED`.

`WI-264` leaves two pieces of genuine first-crossing information that its endpoint-bump screening countermodel does not reproduce: the quantitative positivity of every smaller aperture and the exact terminal null equation. The accepted first-crossing clue therefore asks whether either ingredient, before using the detailed arithmetic kernel, can force an actual zero mode away from the endpoint-gap geometry.

There is now an exact negative answer at the abstract operator level. The *same full-span antisymmetric endpoint-bump vector* used in `WI-264` can be made the unique terminal zero mode of a bounded positive rank-one-defect operator whose every proper centered compression is strictly positive. More strongly, every translated interval of any fixed length shorter than the full aperture has a uniform positive Rayleigh lower bound, and averaging localized copies of the terminal mode reproduces the same abstract firstness inequality used before `WI-253` inserts Suzuki's explicit source formula.

Thus the conjunction

\[
\text{full-span endpoint screening}
+\text{exact terminal zero mode}
+\text{strict positivity on every smaller window}
\]

is internally consistent. Neither nested positivity nor zero-modehood, even with uniform translated-window positivity, can by itself exclude the screening geometry. Any surviving contradiction must use information absent from this rank-one model: the **specific Suzuki kernel/source representation**, the exact von-Mangoldt translation coefficients, the archimedean term, or another source-specific relation tying the terminal null equation to its autocorrelation.

This is not a counterexample to Suzuki's localized Weil operator and does not show that the exact inequality `mathcal F_v(r) >= r lambda_r` from `WI-253` is satisfiable by the endpoint bumps. It closes only the generic-operator route to that inequality: the arithmetic identification of the localization defect with `mathcal F_v` is now the indispensable part.

## 1. Start with the screened full-span vector of WI-264

Fix a finite aperture `a>0` in the regime of `WI-264`, and choose `epsilon>0` small enough for the all-finite-prime screening construction there. Let `phi` be a nonnegative smooth bump with

\[
\operatorname{supp}\phi=[0,\varepsilon],
\qquad
\|\phi\|_2=1,
\]

with positive `L^2` mass in every nonempty subinterval of `(0,epsilon)`. Put

\[
u_-(x)=\phi(x+a),
\qquad
u_+(x)=\phi(a-x),
\qquad
f(x)=\frac{u_-(x)-u_+(x)}{\sqrt2}.
\tag{1}
\]

Then `||f||_2=1`, and the essential support of `f` reaches both endpoints `-a` and `a`: every neighborhood of either endpoint carries positive `L^2` mass. The ordinary autocorrelation of `f` is exactly the endpoint-bump autocorrelation used in `WI-264`. With the stated choice of `epsilon`, its open middle zero interval contains every active von-Mangoldt lag `log n<2a`, while its self- and cross-correlation pieces have the favorable signs against Suzuki's continuous source.

Nothing below changes `f`. The purpose is to test which consequences can follow from **first-crossing operator structure alone** while keeping the already-screened autocorrelation geometry fixed.

## 2. A rank-one defect makes the screened vector the exact terminal zero mode

Let

\[
H=L^2(-a,a)
\]

and define the bounded self-adjoint operator

\[
\boxed{
A=I-|f\rangle\langle f|,
}
\tag{2}
\]

where `|f><f| g = <g,f>f`. Since `||f||=1`, `|f><f|` is the orthogonal projection onto `span{f}`. Therefore

\[
\boxed{
A\succeq0,
\qquad
\ker A=\operatorname{span}\{f\},
\qquad
Af=0.
}
\tag{3}
\]

So the screened endpoint-bump vector is an **exact** terminal zero mode, not an approximate eigenvector.

For `0<s<a`, let `P_s` be multiplication by `1_{(-s,s)}` and let `H_s=P_sH`. The compression of (2) to `H_s` is

\[
A_s=P_sA|_{H_s}
=I_{H_s}-|P_sf\rangle\langle P_sf|.
\tag{4}
\]

Its spectrum consists of `1` on the orthogonal complement of `P_sf` and, when `P_sf\ne0`, the single eigenvalue

\[
1-\|P_sf\|_2^2.
\tag{5}
\]

Because `f` has positive mass arbitrarily close to both endpoints, every strict centered subinterval misses positive mass. Hence

\[
\boxed{
\lambda_s^{\rm abs}:=\inf\sigma(A_s)
=1-\|P_sf\|_2^2
=\|(I-P_s)f\|_2^2>0
\qquad(0<s<a),
}
\tag{6}
\]

while `lambda_a^{abs}=0`. Dominated convergence also gives

\[
\lambda_s^{\rm abs}\downarrow0
\qquad(s\uparrow a).
\tag{7}
\]

Thus (2)--(7) form an exact abstract analogue of a first singular aperture: every proper centered compression is positive, the bottom eigenvalue approaches zero continuously, and the first zero mode occurs only at the terminal aperture.

## 3. Every translated shorter window is uniformly positive

`WI-253` uses more than centered nesting: the global Weil form is tested on translated intervals of a fixed length. The rank-one model passes that stress test too.

For `0<r<a` and `c\in\mathbb R`, define

\[
I_{c,r}=(c-r,c+r),
\qquad
m_r(c)=\|\mathbf1_{I_{c,r}}f\|_2^2,
\qquad
M_r=\sup_{c\in\mathbb R}m_r(c).
\tag{8}
\]

The map `c -> m_r(c)` is continuous and tends to zero as `|c| -> infinity`, so its supremum is attained. Since an interval of length `2r<2a` cannot contain the full essential support span of `f`, no maximizer can have `m_r(c)=1`. Therefore

\[
\boxed{M_r<1.}
\tag{9}
\]

Now let `g` be any vector supported in `I_{c,r}`. Cauchy--Schwarz gives

\[
|\langle g,f\rangle|^2
=|\langle g,\mathbf1_{I_{c,r}}f\rangle|^2
\le m_r(c)\|g\|_2^2
\le M_r\|g\|_2^2.
\tag{10}
\]

Consequently the quadratic form `q(g)=<Ag,g>` obeys the **uniform translated-window bound**

\[
\boxed{
q(g)
=\|g\|_2^2-|\langle g,f\rangle|^2
\ge(1-M_r)\|g\|_2^2,
\qquad
0<r<a,
}
\tag{11}
\]

with `1-M_r>0` independent of the window center. Therefore even the stronger abstract statement

\[
\text{all translated windows of radius }r<a
\text{ have a common positive spectral reserve}
\]

coexists with the endpoint-screened terminal zero mode.

## 4. The localized terminal mode satisfies the abstract sliding-firstness inequality exactly

Let

\[
\eta_{c,r}=\mathbf1_{I_{c,r}}.
\]

Since `Af=0`, the localized terminal vector has

\[
\begin{aligned}
q(\eta_{c,r}f)
&=\|\eta_{c,r}f\|_2^2
-|\langle\eta_{c,r}f,f\rangle|^2\\
&=m_r(c)-m_r(c)^2\\
&=m_r(c)(1-m_r(c)).
\end{aligned}
\tag{12}
\]

Using (9),

\[
q(\eta_{c,r}f)
\ge(1-M_r)m_r(c).
\tag{13}
\]

Fubini gives the exact sliding mass identity

\[
\int_{\mathbb R}m_r(c)\,dc
=2r\|f\|_2^2
=2r.
\tag{14}
\]

Hence

\[
\boxed{
\int_{\mathbb R}q(\eta_{c,r}f)\,dc
\ge2r(1-M_r)>0
\qquad(0<r<a).
}
\tag{15}
\]

Equation (15) is the abstract operator-theoretic skeleton of the localization step behind `WI-253`: a terminal zero mode, strict positivity on every smaller translated window, and an averaged firstness reserve. In the actual Weil problem, the decisive additional step is that Suzuki's explicit quadratic form converts this averaged localization defect into the source-side functional

\[
\mathcal F_v(r)
=\int_0^{2a_*}\min(h,2r)\,d\mu_v(h),
\tag{16}
\]

and yields `mathcal F_v(r) >= r lambda_r`. The rank-one model deliberately does **not** reproduce (16). That failure identifies, rather than weakens, the barrier: the source-specific representation is exactly the information a successful proof must exploit.

## 5. Exact logical barrier

Combining `WI-264` with (2)--(15) produces one vector having all of the following properties simultaneously:

1. compact support with full support span `[-a,a]`;
2. the endpoint-gap autocorrelation geometry that screens every active finite prime-power lag and sign-screens the continuous source;
3. an exact terminal null equation `Af=0`;
4. strict positivity of every proper centered compression;
5. uniform strict positivity on every translated interval of each radius `r<a`;
6. the integrated localization lower bound (15) for every `r<a`.

Therefore none of properties 3--6, considered only as generic Hilbert-space/variational facts, can force nonzero autocorrelation at a prime lag or forbid a long interior autocorrelation gap.

This strengthens the abstract boundary of `WI-257`. That finding showed that generic bounded-perturbation zero-modehood does not upgrade translation regularity. The present result additionally preserves the *specific endpoint-screening geometry* and supplies an entire positive nested/translated compression family terminating at its zero mode. The obstruction is no longer merely “an arbitrary zero mode may be rough”; it is “the screened geometry itself is compatible with abstract first-crossing spectral structure.”

## 6. What remains genuinely open

The finding does **not** prove that the `WI-264` endpoint bumps satisfy the actual zeta-specific inequality

\[
\mathcal F_f(r)\ge r\lambda_r
\qquad(0<r<a_*),
\tag{17}
\]

nor does it solve Suzuki's actual null equation

\[
A_{a_*}^{\rm Weil}f=0.
\tag{18}
\]

The operator in (2) is a deliberately flexible abstract countermodel. Its role is to falsify deductions that would use only nesting, positivity, exact zero-modehood, translated-window positivity, or the generic localization argument. A contradiction to the screened geometry must use a relation that distinguishes `A_{a_*}^{Weil}` from (2).

The live targets are consequently sharper:

- evaluate or bound the **actual source-side** `mathcal F_f(r)` for the whole screened endpoint family against rigorous lower information on `r lambda_r`;
- use the explicit Suzuki kernel/null equation to show that an actual zero mode cannot have the long autocorrelation gap of `WI-264`;
- derive a global Fourier or moment identity from the exact arithmetic operator that is absent from arbitrary positive compression families.

Any proof that reduces the first-crossing input to (3), (6), (11), or (15) before using the arithmetic kernel has discarded too much information and is defeated by this construction.

## 7. Prior-art and novelty audit

The source-specific framework is established prior art. Masatoshi Suzuki's *Aspects of the screw function corresponding to the Riemann zeta-function*, J. London Math. Soc. 107 (2023), Theorems 1.3--1.4, gives the finite-window positivity/nondegeneracy framework. His *Weil's quadratic form via the screw function*, arXiv:2606.09096 (2026), gives the self-adjoint localized operator and continuous lowest-eigenvalue formulation used by `WI-238` and the subsequent first-crossing program.

Compression of an operator to a closed subspace, the rank-one projection `|f><f|`, and the spectrum of `I-|u><u|` are elementary classical Hilbert-space facts. A targeted prior-art search around localized Weil first crossings, operator compressions, and rank-one perturbations found the established ingredients but no source formulating the endpoint-screening stress test (1)--(15) for this zeta-specific program. Search absence is audit context only and is not a priority claim.

The Mathia deduction is the combination forced by the accepted clue: reuse the exact `WI-264` screened vector as the defect direction of a rank-one positive operator, then observe that its full support span makes every proper translated-window compression uniformly positive. This supplies the clue's requested “exact model satisfying an analogue of the null equation” and strengthens it to an analogue of the full abstract sliding-firstness step.

Primary source anchors:

- Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *J. London Math. Soc.* 107 (2023), DOI `10.1112/jlms.12785`: https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12785.
- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026): https://arxiv.org/abs/2606.09096.

## Falsification and audit test

The no-go is exact and can be checked without numerical computation. To falsify it one must find an error in at least one of the following steps:

1. the `WI-264` endpoint bump has essential support reaching both endpoints while retaining its screened autocorrelation;
2. `I-|f><f|` is positive semidefinite with kernel `span{f}`;
3. its centered compression has bottom eigenvalue `1-||P_sf||^2>0` for every `s<a`;
4. for fixed `r<a`, the maximal mass `M_r` captured by any interval of length `2r` is strictly below one;
5. Cauchy--Schwarz gives the uniform translated lower bound (11);
6. Fubini gives (14), hence the integrated firstness inequality (15).

None of these steps assumes RH, uses a zero table, or imports a numerical certificate. The logical boundary is equally exact: replacing the rank-one form by Suzuki's explicit arithmetic form may impose additional constraints, and those constraints are precisely what this finding leaves open.

## Consequence for the research line

The accepted first-crossing clue should no longer seek a contradiction from **generic first-crossing spectral structure** alone. The endpoint-screened countermodel survives an exact terminal null equation, all proper aperture positivity, all translated shorter-window positivity, and the corresponding averaged localization reserve.

The remaining question is source-specific: does the actual equality between Suzuki's localization defect and the von-Mangoldt/archimedean autocorrelation functional force something that the rank-one model cannot imitate? That is now the correct discriminator. If the actual `mathcal F_v(r) >= r lambda_r` family also admits a screened endpoint family, or if Suzuki's exact null equation can be matched by a source-compatible screened model, the current phase-defect route should be retired until a stronger invariant is found.