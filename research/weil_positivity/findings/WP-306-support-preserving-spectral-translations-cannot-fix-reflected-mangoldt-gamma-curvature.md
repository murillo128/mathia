---
id: WP-306
title: Support-preserving spectral translations cannot fix reflected Mangoldt Gamma curvature
branch: weil_positivity
status: supported
kind: support-preserving-translation-gamma-curvature-obstruction
claim_strength: exact translation law for the WP-305 curvature coefficient and a strict positive lower bound for every spectral translation that preserves the canonical Mangoldt carrier on the nonnegative half-line; closes the support-preserving translation escape left open by WP-305
created: 2026-09-14
related: [WP-273, WP-275, WP-304, WP-305]
prior_art:
  - NIST Digital Library of Mathematical Functions, Sections 25.2 and 5.2, for the Laurent normalization of the Stieltjes constants and Euler's constant
  - Iaroslav V. Blagouchine, Expansions of generalized Euler's constants into the series of polynomials in pi^{-2} and into the formal enveloping series with rational coefficients only, Journal of Number Theory 158 (2016), 365-396, DOI 10.1016/J.JNT.2015.06.012, for explicit enveloping estimates on Stieltjes constants
  - Fritz Gesztesy and Eduard Tsekanovskii, On Matrix-Valued Herglotz Functions, Mathematische Nachrichten 218 (2000), 61-138, DOI 10.1002/1522-2616(200010)218:1<61::AID-MANA61>3.0.CO;2-D, for the classical Herglotz/Nevanlinna framework
---

# WP-306 — Support-preserving spectral translations cannot fix reflected Mangoldt Gamma curvature

## Claim

`WP-305` left a nontrivial spectral translation as the simplest unresolved way to alter the wrong-sign first real curvature of the canonical reflected Mangoldt Herglotz response. That escape is impossible as long as the translation preserves the intrinsic one-sided nonnegative-energy carrier.

Let

\[
\mu_+=\sum_{n\ge2}\frac{\Lambda(n)}{n+1}\,\delta_{\log n}
\tag{1}
\]

and write its Laplace transform, using the notation of `WP-305`, as

\[
F(s)=\int_0^\infty e^{-sE}\,d\mu_+(E)
=\frac1s+C_++A_0s+O(s^2),
\qquad s\to0^+,
\tag{2}
\]

where

\[
C_+=-\gamma-D,
\qquad
D:=\sum_{n\ge2}\frac{\Lambda(n)}{n(n+1)},
\tag{3}
\]

and

\[
A_0=\gamma^2+2\gamma_1+S,
\qquad
S:=\sum_{n\ge2}\frac{\Lambda(n)\log n}{n(n+1)}.
\tag{4}
\]

Translate every source energy by a real constant `t`,

\[
E\longmapsto E+t,
\qquad
\mu_t:=(E\mapsto E+t)_*\mu_+.
\tag{5}
\]

The translated carrier stays on `[0,infinity)` exactly when

\[
t\ge-\log2.
\tag{6}
\]

For every such `t`, the coefficient controlling the first even real Herglotz correction is

\[
\boxed{
A_t=A_0-tC_++\frac{t^2}{2}>0.
}
\tag{7}
\]

In fact the coefficient is strictly increasing throughout the entire support-preserving range and satisfies the explicit bound

\[
\boxed{
A_t\ge A_{-\log2}>\frac{583}{60000}>0.
}
\tag{8}
\]

Consequently the reflected translated response still has

\[
\operatorname{Re}m_{t,-}(iy)
=\log y-B_t+\frac{A_t}{y^2}+o(y^{-2}),
\tag{9}
\]

whereas the Riemann Gamma/digamma sector has coefficient `-1/24`. No additive real normalization, reflection, or support-preserving spectral translation of the already-forced source can repair the sign mismatch. This uses no zero data and no RH assumption.

## 1. Translation acts exactly on the pole expansion

Because translation multiplies a Laplace transform by `e^{-ts}`,

\[
F_t(s):=\int e^{-sE}\,d\mu_t(E)=e^{-ts}F(s).
\tag{10}
\]

Expanding (10) at `s=0` gives

\[
F_t(s)
=\frac1s+(C_+-t)
+\left(A_0-tC_++\frac{t^2}{2}\right)s
+O(s^2).
\tag{11}
\]

Thus

\[
C_t=C_+-t,
\qquad
A_t=A_0-tC_++\frac{t^2}{2}.
\tag{12}
\]

For a support-preserving translation the counting law of `mu_t` still has the form

\[
M_t(R)=R+C_t+\varepsilon_t(R),
\qquad
\int_0^\infty\varepsilon_t(E)\,dE=A_t.
\tag{13}
\]

The possible boundary atom at zero when `t=-log 2` causes no difficulty: Stieltjes integration by parts uses the left boundary value `M_t(0-)=0`, and (11) remains exact.

Repeating the `WP-305` Herglotz expansion therefore replaces `A_0` by `A_t`. Reflection changes the positive-side coefficient `-A_t/y^2` into `+A_t/y^2`; real subtraction constants affect only `B_t`.

## 2. The curvature coefficient is monotone on the admissible range

Differentiate (12):

\[
A_t'=t-C_+.
\tag{14}
\]

It is enough to show

\[
C_+<-\log2.
\tag{15}
\]

The first two nonzero terms of `D` give

\[
D\ge \frac{\log2}{6}+\frac{\log3}{12}.
\tag{16}
\]

Using the classical elementary bound `gamma>1/2`, together with `log 2<7/10` and `log 3>1`,

\[
\gamma+D-\log2
>
\frac12+\frac{\log2}{6}+\frac{\log3}{12}-\log2
>
\frac7{12}-\frac56\frac7{10}=0.
\tag{17}
\]

Hence `gamma+D>log 2`, proving (15). Therefore for every `t>=-log 2`,

\[
A_t'=t-C_+>-\log2-C_+>0.
\tag{18}
\]

So the smallest curvature compatible with the nonnegative carrier occurs at the extreme shift that places the first atom exactly at zero:

\[
\min_{t\ge-\log2}A_t=A_{-\log2}.
\tag{19}
\]

This already rules out a hidden interior tuning parameter: there is no support-preserving translated value at which the curvature can turn through zero.

## 3. The boundary value is still strictly positive

Put `L=log 2`. Substituting (3)-(4) into (12) at `t=-L` gives

\[
A_{-L}
=
\gamma^2+2\gamma_1-\gamma L+\frac{L^2}{2}
+
\sum_{n\ge2}
\frac{\Lambda(n)(\log n-L)}{n(n+1)}.
\tag{20}
\]

Every term in the final series is nonnegative because `n>=2`, and the `n=3` term alone gives

\[
\sum_{n\ge2}
\frac{\Lambda(n)(\log n-L)}{n(n+1)}
\ge
\frac{\log3\,\log(3/2)}{12}.
\tag{21}
\]

For the Stieltjes constant, Blagouchine's enveloping expansion gives the convenient rigorous bound

\[
\gamma_1>-\frac1{12}.
\tag{22}
\]

Also `gamma>1/2`. Since

\[
x\mapsto x^2-Lx+\frac{L^2}{2}
\tag{23}
\]

is increasing for `x>=1/2` because `L<1`, equations (20)-(22) imply

\[
A_{-L}
>
\frac1{12}-\frac L2+\frac{L^2}{2}
+
\frac{\log3\,\log(3/2)}{12}.
\tag{24}
\]

No delicate numerical constant is needed. The elementary rational enclosures

\[
\frac{69}{100}<\log2<\frac7{10},
\qquad
\log3>1,
\qquad
\log(3/2)>\frac25
\tag{25}
\]

suffice. The first three terms on the right of (24) are increasing as a function of `L` for `L>1/2`, so

\[
A_{-L}
>
\frac1{12}
-\frac{69}{200}
+\frac{69^2}{2\cdot100^2}
+\frac1{30}
=
\frac{583}{60000}>0.
\tag{26}
\]

Combining (19) and (26) proves (8).

## 4. Consequence for the reflected Gamma comparison

For every `t>=-log 2`, the support-preserving translated positive Herglotz response has the same unit-density leading logarithm as in `WP-305`, with only its constant and lower asymptotic moments changed. After reflection,

\[
\operatorname{Re}m_{t,-}(iy)
=
\log y-B_t+\frac{A_t}{y^2}+o(y^{-2}),
\qquad A_t>0.
\tag{27}
\]

The completed-zeta archimedean term remains

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)
=
\log\frac y2-\frac1{24y^2}+O(y^{-4}).
\tag{28}
\]

Thus the mismatch survives the entire support-preserving translation family:

\[
\boxed{
+\frac{A_t}{y^2}
\quad\text{versus}\quad
-\frac1{24y^2},
\qquad t\ge-\log2.
}
\tag{29}
\]

A subsequent positive spectral dilation can rescale the magnitude but not reverse this sign. Hence the affine support-preserving family generated from the canonical carrier is also excluded.

## 5. Aggressive falsification and exact scope

The hypothesis `t>=-log 2` is essential to this finding. If `t<-log 2`, the first source atom moves to negative energy. The translated measure is still a positive Borel measure, so abstract Herglotz positivity alone does not forbid that operation. What fails is the one-sided nonnegative-energy structure inherited from the Mathia carrier. Therefore this finding does **not** claim that every real translation is impossible.

This distinction is the matched control. If later Mathia geometry independently forces a shifted generator with negative low-energy states, that construction evades (6) and must be tested separately. Merely choosing such a shift because it changes the Gamma coefficient would be target programming rather than an intrinsic derivation.

The obstruction is also not a generic theorem about arbitrary positive unit-density measures. Equations (16), (20), and (21) use the exact canonical weights `Lambda(n)/(n+1)` and their first arithmetic atoms. A synthetic positive measure may have different offset and moment data and may cross zero under translation.

No zeros of zeta enter the argument. The only zeta-side constants used are the pole/Stieltjes coefficients already present in the exact source expansion of `WP-305`; the sign bound is independent of RH.

## 6. Prior-art and novelty audit

The transform law `F_t(s)=e^{-ts}F(s)` and translation of Herglotz representing measures are classical. The Laurent normalization of `gamma` and `gamma_1` is standard and recorded by DLMF. Blagouchine's rational enveloping expansion supplies a convenient literature bound for `gamma_1`; no novelty is claimed for that estimate.

A bounded search over Herglotz/Nevanlinna formulations of the Riemann explicit formula, translated von-Mangoldt measures, Gamma-factor asymptotics, and spectral translations did not identify a source stating the exact obstruction (7)-(29) for the `WP-304`/`WP-305` carrier. Search results instead returned standard explicit-formula and Herglotz background. The novelty claim is therefore deliberately local: this is a source-specific falsification of the live Mathia translation escape, not a new theorem about Herglotz functions or the Riemann explicit formula in general.

Relevant references:

- NIST DLMF, Riemann zeta Laurent expansion and Stieltjes constants: https://dlmf.nist.gov/25.2
- NIST DLMF, Euler's constant: https://dlmf.nist.gov/5.2
- I. V. Blagouchine, *Expansions of generalized Euler's constants into the series of polynomials in pi^{-2} and into the formal enveloping series with rational coefficients only*, J. Number Theory 158 (2016), 365-396, DOI `10.1016/J.JNT.2015.06.012`, arXiv:1501.00740.
- F. Gesztesy and E. Tsekanovskii, *On Matrix-Valued Herglotz Functions*, Math. Nachr. 218 (2000), 61-138.

## 7. Consequence for the research frontier

`WP-305` showed that reflection, additive normalization, and positive dilation cannot fix the first Riemann-specific curvature of the canonical source. `WP-306` removes the remaining **support-preserving translation** freedom: even pushing the lowest Mangoldt atom all the way to zero leaves a strictly positive curvature coefficient, and every less aggressive admissible shift only increases it.

The surviving source-only translation escape is therefore sharply localized to shifts that abandon the nonnegative one-sided spectrum. More importantly, a genuine Mathia completion still needs additional structure that changes the source remainder before exact Gamma matching: an independently forced archimedean/boundary sector, quotient or compression, nonlocal finite--infinite coupling, or another intrinsic observable. Translation of the existing positive carrier is not that structure.

## Conclusion

The canonical Mangoldt Herglotz carrier cannot repair its `WP-305` Gamma-curvature mismatch by any spectral translation that preserves its intrinsic nonnegative support. The exact translated coefficient is convex, already increasing on the admissible half-line, and remains bounded away from zero at the most extreme admissible shift. The obstruction is source-specific, unconditional, and leaves only translations that abandon the one-sided positive-energy geometry or genuinely new finite--archimedean structure as live escapes.
