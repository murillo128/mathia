# WI-267 — Suzuki null modes admit no prime-translation-free support gap

## Status

- **Evidence:** `EXACT-DERIVED + SOURCE-SPECIFIC-RIGIDITY + LITERATURE+DERIVED + PRIOR-ART-AUDITED`.
- **Scope:** an exact support-propagation constraint for arbitrary null vectors of Suzuki's localized Weil operator. It strengthens `WI-266`, which excluded one explicit two-endpoint family, to a geometry-independent obstruction: any open support gap of a nonzero null vector must be hit by at least one active von-Mangoldt translation at every point.
- **What it does not claim:** this is not RH, not a new simple-zero proportion, and not yet a proof that some prime-power autocorrelation `C_v(log n)` is nonzero. A multi-component mode may still use translated mass inside every support gap to cancel the continuous convolution.

## Claim

Fix `a>0`. Let `A_a` be Suzuki's self-adjoint localized Weil operator on `L^2(-a,a)`, extend functions by zero outside `(-a,a)`, and define the finite active lag set

\[
\mathcal P_a
:=\{\log n:\Lambda(n)>0,\ \log n\le 2a\}.
\tag{1}
\]

Suppose

\[
0\ne v\in\mathfrak D(A_a),
\qquad
A_a v=0,
\tag{2}
\]

and let `S=supp(v)` be the closed essential support of the zero extension of `v`. Then

\[
\boxed{
(-a,a)
\subset
S\cup
\bigcup_{\ell\in\mathcal P_a}
\bigl((S-\ell)\cup(S+\ell)\bigr).
}
\tag{3}
\]

Equivalently, for every `x\in(-a,a)\setminus S` there is an active prime-power lag `\ell\in\mathcal P_a` such that

\[
\boxed{x+\ell\in S\quad\text{or}\quad x-\ell\in S.}
\tag{4}
\]

Thus a nonzero localized Weil null mode has **no prime-translation-free support gap**. More explicitly, there cannot exist a nonempty open interval `J\subset(-a,a)` for which

\[
J\cap S=\varnothing,
\qquad
(J+\ell)\cap S=(J-\ell)\cap S=\varnothing
\quad(\ell\in\mathcal P_a).
\tag{5}
\]

The statement is source-specific. Generic nested positivity and generic self-adjoint first-crossing structure do not imply it; `WI-265` supplies a countermodel to such an abstract implication.

## 1. The null equation is available distributionally on the full operator domain

The pointwise formula is the first delicate issue. Suzuki's current preprint, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (revised 17 Aug 2026), defines

\[
B_a=D^*G_aD,
\qquad
\mathfrak D(B_a)=H_0^1(-a,a),
\tag{6}
\]

and proves in Theorem 1.1 that `A_a` is the Friedrichs extension of `B_a`. Section 2.5 gives, for `u\in C_c^\infty(-a,a)`,

\[
(A_a u)(x)=\int_{-a}^a(-g''(x-y))u(y)\,dy,
\tag{7}
\]

with the distribution `-g''` expanded into its local singular term, the finite von-Mangoldt translations, and the regular archimedean remainder in equations (2.10)--(2.11).

Suzuki also explicitly warns that (2.11) is not a pointwise formula for a general `v\in\mathfrak D(A_a)`. What survives on the full domain is the distributional quadratic-form identity (2.9), obtained as a form-norm limit of `C_c^\infty` functions. That is enough here.

Indeed, by the Friedrichs/form representation,

\[
Q_W^a(v,\phi)=\langle A_a v,\phi\rangle=0
\qquad
(\phi\in C_c^\infty(-a,a)).
\tag{8}
\]

Choose `v_j\in C_c^\infty(-a,a)` converging to `v` in the form norm, as supplied by Suzuki's form-core result. The form norm controls the `L^2` norm, so `v_j\to v` in `L^2`. Polarizing (2.9) gives

\[
Q_W^a(v_j,\phi)
=\langle(-g'')*v_j,\phi\rangle.
\tag{9}
\]

For fixed test `\phi`, convolution of the tempered distribution `-g''` with `\phi` is smooth; restricted to the compact interval `[-a,a]` it is in `L^2`. Hence `L^2` convergence of `v_j` passes (9) to the limit. Therefore

\[
\boxed{(-g'')*v=0\quad\text{in }\mathcal D'(-a,a).}
\tag{10}
\]

This resolves the regularity caveat left explicit in the active first-crossing clue: the argument below never inserts pointwise values of a general element of `\mathfrak D(A_a)` into Suzuki's formula.

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2, Theorem 1.1, Corollary 1.2 and §2.5, equations (2.9)--(2.11): https://arxiv.org/abs/2606.09096.

## 2. On a translation-free gap only the regular kernel survives

Assume for contradiction that a nonempty open interval

\[
J=(\alpha,\beta)\subset(-a,a)
\tag{11}
\]

satisfies (5). On `J`, the local singular term of `-g''` sees no mass because `v=0` there, and every von-Mangoldt delta translation also vanishes because `J\pm\ell` misses `S` for every active lag. Thus the restriction of (10) to `J` is an ordinary convolution against the smooth part of the kernel.

As reconstructed in `WI-266`, for `h>0` away from prime-power atoms that regular even kernel is

\[
k(h)
=e^{h/2}-\frac{e^{-5h/2}}{1-e^{-2h}}.
\tag{12}
\]

The exact geometric-series expansion is

\[
\boxed{
k(h)
=e^{h/2}-\sum_{m=0}^{\infty}e^{-q_mh},
\qquad
q_m=\frac52+2m.
}
\tag{13}
\]

Because `v=0` almost everywhere on `J`, split the convolution into the portions to the left and right of the gap. For `x\in J`, (10) becomes

\[
0=F(x)
:=\int_{-a}^{\alpha}k(x-y)v(y)\,dy
 +\int_{\beta}^{a}k(y-x)v(y)\,dy.
\tag{14}
\]

Define

\[
\begin{aligned}
A_0&:=\int_{-a}^{\alpha}e^{-y/2}v(y)\,dy,
& B_0&:=\int_{\beta}^{a}e^{y/2}v(y)\,dy,\\
A_m&:=\int_{-a}^{\alpha}e^{q_my}v(y)\,dy,
& B_m&:=\int_{\beta}^{a}e^{-q_my}v(y)\,dy.
\end{aligned}
\tag{15}
\]

Since compactly supported `L^2` functions are in `L^1`, all coefficients are well defined. Substituting (13) into (14) gives the exact expansion

\[
\boxed{
F(x)
=A_0e^{x/2}+B_0e^{-x/2}
-\sum_{m=0}^{\infty}
\left(A_me^{-q_mx}+B_me^{q_mx}\right).
}
\tag{16}
\]

On every closed subinterval of `J` the two series converge normally. For example, if `\Re x\ge\alpha+\delta`, then

\[
|A_me^{-q_mx}|
\le \|v\|_1 e^{-q_m\delta},
\tag{17}
\]

and the right-hand series has the analogous bound using `\beta-\Re x`. Consequently `F` extends holomorphically to the strip

\[
\alpha<\Re x<\beta.
\tag{18}
\]

The distributional equality (14) therefore says that this analytic function vanishes on the real interval `J`, hence identically on the strip.

## 3. Laurent uniqueness forces all one-sided exponential moments to vanish

Set

\[
z=e^{x/2}.
\tag{19}
\]

Because `2q_m=5+4m`, equation (16) becomes a Laurent series on the annulus

\[
e^{\alpha/2}<|z|<e^{\beta/2}:
\tag{20}
\]

\[
\boxed{
F(z)
=A_0z+B_0z^{-1}
-\sum_{m=0}^{\infty}
\left(A_mz^{-(5+4m)}+B_mz^{5+4m}\right).
}
\tag{21}
\]

The exponent sets

\[
\{1,-1\},
\qquad
\{-(5+4m):m\ge0\},
\qquad
\{5+4m:m\ge0\}
\tag{22}
\]

are pairwise disjoint. Since the Laurent series vanishes identically on its annulus, uniqueness of Laurent coefficients yields

\[
A_0=B_0=0,
\qquad
A_m=B_m=0
\quad(m\ge0).
\tag{23}
\]

The infinite families in (23) determine each side of `v`. For the left side, put `t=e^{2y}`. Then

\[
A_m
=\frac12
\int_{e^{-2a}}^{e^{2\alpha}}
 t^m\,t^{1/4}v\!\left(\frac12\log t\right)dt
=0
\qquad(m\ge0).
\tag{24}
\]

Thus every polynomial moment of the finite complex `L^1` density

\[
f_L(t)=\frac12t^{1/4}v\!\left(\frac12\log t\right)
\tag{25}
\]

vanishes on a compact interval bounded away from zero. By the density of polynomials in continuous functions on a compact interval, the associated finite complex measure is zero, so

\[
v=0\quad\text{a.e. on }[-a,\alpha].
\tag{26}
\]

Likewise, with `t=e^{-2y}` on the right,

\[
B_m
=\frac12
\int_{e^{-2a}}^{e^{-2\beta}}
 t^m\,t^{1/4}v\!\left(-\frac12\log t\right)dt
=0
\qquad(m\ge0),
\tag{27}
\]

so

\[
v=0\quad\text{a.e. on }[\beta,a].
\tag{28}
\]

Together with the assumed gap, (26)--(28) give `v=0`, contradicting (2). This proves that (5) is impossible.

## 4. The pointwise support-cover form follows because the prime set is finite

The support-cover statement (3) is now immediate. If there were an `x\in(-a,a)\setminus S` for which all `x\pm\ell` also lay outside `S`, then `S` being closed and `\mathcal P_a` being finite would give a sufficiently small open interval `J` around `x` such that

\[
J\cap S=\varnothing,
\qquad
(J\pm\ell)\cap S=\varnothing
\quad(\ell\in\mathcal P_a),
\tag{29}
\]

contradicting the theorem above.

A weak geometric corollary, included only to calibrate the statement, is

\[
|S|\ge \frac{2a}{1+2|\mathcal P_a|},
\tag{30}
\]

because (3) covers `(-a,a)` by at most `1+2|\mathcal P_a|` translates of `S`. This measure bound is not expected to be sharp and is not the main result; the stronger information is the **pointwise translation domination** (3).

## 5. Consequence for the first-crossing program

Under RH failure, `WI-253` constructs the first unrestricted crossing

\[
a_*:=\inf\{a>0:\lambda_a\le0\}
\tag{31}
\]

with a nonzero attained mode

\[
A_{a_*}v=0.
\tag{32}
\]

Applying (3) at `a=a_*` gives an exact support-spreading condition for that hypothetical mode. This is precisely the weaker positive outcome requested by the accepted clue `CLUE-first-global-crossing-sliding-autocorrelation-symbol`: the actual Suzuki equation forbids not merely the `WI-264` endpoint geometry, but **every** gap on which all finite prime-power translations are inactive.

This materially narrows the remaining screening problem. Any surviving multi-component countermodel must have a support graph whose active prime-power translates hit every open gap point. Equivalently, cancellation on a gap cannot be purely archimedean: at least one discrete arithmetic translate must be active everywhere in that gap.

The result does **not** by itself imply

\[
C_v(\log n)\ne0
\tag{33}
\]

for some active prime power. A translated value can cancel the continuous convolution at a point where `v(x)=0`, while the global autocorrelation at that lag may still vanish by phase or sign cancellation. Thus the next gate is genuinely stronger: combine the pointwise translation domination with the null equation and/or the sliding lower-envelope inequalities strongly enough to force a quantitative non-screenable overlap, rather than only translated activity.

## 6. Prior-art and novelty audit

The operator, its Friedrichs-extension/domain structure, the form-core approximation, and the distributional formulas are Suzuki's results, not Mathia's. The current source is arXiv:2606.09096v2, revised 17 Aug 2026; using v2 matters because it explicitly states that the pointwise formula (2.11) need not make sense on all of `\mathfrak D(A_a)` while the form identity (2.9) survives by approximation.

Suzuki's earlier paper **Aspects of the screw function corresponding to the Riemann zeta-function**, *J. London Math. Soc.* 108 (2023), 1448--1487, DOI `10.1112/jlms.12785`, develops a different mean-periodic convolution equation `g*phi=0` and a Fourier--Carleman representation. That is relevant convolution-equation prior art, but it concerns a special global annihilator and does not state the finite-aperture support-cover theorem (3).

Bombieri's **A variational approach to the explicit formula**, *Comm. Pure Appl. Math.* 56 (2003), 1151--1164, DOI `10.1002/cpa.10089`, is prior art for the variational/Lagrangian formulation later represented by Suzuki's operator. A targeted search of Bombieri/Suzuki localized-Weil, null-vector, support-gap, compact-support and convolution literature found no statement of (3) or of the Laurent/moment argument above. Search absence is audit context only, not a priority claim.

The classical Titchmarsh convolution theorem is also adjacent prior art, but it does not directly give the present result: here the regular Weil kernel is not compactly supported and the equation is known only on a local gap, not on the whole line or a one-sided convolution interval. The decisive extra structure is the exact arithmetic progression of exponential rates in (13), which turns the local gap equation into the Laurent expansion (21) and then into a complete polynomial moment family.

Accordingly, the new Mathia deduction is the combination of Suzuki's full-domain distributional null equation with the exact exponential expansion of the regular Weil kernel and elementary Laurent/moment uniqueness. No claim of historical priority is made.

## Falsification and audit test

The finding uses no floating-point or computer-assisted certificate. A falsification must break at least one of the following load-bearing steps:

1. Suzuki's form-core statement and (2.9) do not justify the distributional extension (10) for a general `v\in\mathfrak D(A_a)` with `A_av=0`.
2. Under (5), some local singular or von-Mangoldt term of `-g''` remains active on `J`.
3. The ordinary regular kernel on that gap is not (12), or the exact expansion (13) fails.
4. The left/right convolution does not admit the normally convergent expansion (16) on the strip (18).
5. The substitution `z=e^{x/2}` does not produce the Laurent exponents in (21), or two exponent families collide.
6. Vanishing of all coefficients `A_m` or `B_m` fails to imply vanishing of the corresponding side of `v`; equations (24) and (27) reduce this to ordinary polynomial moment uniqueness for a finite complex measure on a compact interval.
7. The finite-lag neighborhood argument from the gap theorem to the pointwise cover (3) fails at an endpoint or at `\log n=2a`; zero extension outside `(-a,a)` removes that endpoint ambiguity.

The most delicate point is item 1, not the analytic uniqueness argument. Any review should therefore check the polarization/form-limit passage against Suzuki v2 before spending effort on the later elementary steps.

## Consequence for the research line

`WI-266` showed that one sign-screened two-endpoint geometry fails the actual source equation. The present result extracts the geometry-independent core of that obstruction: **every nonzero Suzuki null mode must be prime-translation dominating on the complement of its support**.

This is a genuine source-specific rigidity statement but not yet the desired defect-to-zero bootstrap. The next productive target is to determine whether a translation-dominating multi-component support can simultaneously satisfy the exact null equation and keep every relevant prime-lag autocorrelation screened. A positive lower bound on unavoidable translated overlap or on a source-weighted autocorrelation would connect this support propagation theorem back to the first-crossing inequalities of `WI-253`/`WI-258`; a source-compatible construction would instead identify the next exact barrier.