---
id: WP-307
title: Pole-normalized Mangoldt curvature stays positive under every orientation-preserving affine spectral recentering
branch: weil_positivity
status: supported
kind: affine-spectral-recentering-gamma-curvature-obstruction
claim_strength: exact affine transformation law plus a source-specific positive lower bound for the translation-invariant second logarithmic coefficient of the WP-305 Mangoldt Laplace transform; closes the unrestricted real-translation loophole left by WP-306 and all positive-dilation-plus-translation variants after leading-density normalization
created: 2026-09-14
related: [WP-273, WP-275, WP-304, WP-305, WP-306]
prior_art:
  - NIST Digital Library of Mathematical Functions, Sections 25.2 and 5.2, for the Laurent normalization of the Stieltjes constants and Euler's constant
  - Iaroslav V. Blagouchine, Expansions of generalized Euler's constants into the series of polynomials in pi^{-2} and into the formal enveloping series with rational coefficients only, Journal of Number Theory 158 (2016), 365-396, DOI 10.1016/J.JNT.2015.06.012, for explicit enveloping estimates on Stieltjes constants
  - J. Barkley Rosser and Lowell Schoenfeld, Approximate formulas for some functions of prime numbers, Illinois Journal of Mathematics 6 (1962), 64-94, DOI 10.1215/ijm/1255631807, Theorem 12, for the unconditional global Chebyshev bound psi(x) < 1.03883 x
  - Fritz Gesztesy and Eduard Tsekanovskii, On Matrix-Valued Herglotz Functions, Mathematische Nachrichten 218 (2000), 61-138, DOI 10.1002/1522-2616(200010)218:1<61::AID-MANA61>3.0.CO;2-D, for the classical Herglotz/Nevanlinna framework
---

# WP-307 — Pole-normalized Mangoldt curvature stays positive under every orientation-preserving affine spectral recentering

## Claim

`WP-306` proved that the first reflected Herglotz curvature of the canonical Mangoldt source cannot acquire the Riemann-Gamma sign under translations that keep all source energies nonnegative. The support restriction is unnecessary.

Let

\[
\mu_+=\sum_{n\ge2}\frac{\Lambda(n)}{n+1}\,\delta_{\log n}
\tag{1}
\]

and, as in `WP-305`--`WP-306`, write

\[
F(s)=\int e^{-sE}\,d\mu_+(E)
=\frac1s+C_++A_0s+O(s^2),
\qquad s\to0^+,
\tag{2}
\]

with

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

The second coefficient of the pole-normalized logarithm is

\[
\boxed{
J:=[s^2]\log\!\bigl(sF(s)\bigr)
=A_0-\frac{C_+^2}{2}.
}
\tag{5}
\]

For the actual Riemann Mangoldt source,

\[
\boxed{
J>\frac7{300}>0.
}
\tag{6}
\]

Now allow the entire orientation-preserving affine freedom in the spectral coordinate,

\[
E\longmapsto aE+t,
\qquad a>0,\quad t\in\mathbb R,
\tag{7}
\]

and renormalize the pushed measure by the unique positive scalar `a` that restores unit asymptotic density. Thus

\[
\nu_{a,t}:=a\,(E\mapsto aE+t)_*\mu_+.
\tag{8}
\]

If

\[
G_{a,t}(s)=\int e^{-sE}\,d\nu_{a,t}(E)
=\frac1s+C_{a,t}+A_{a,t}s+O(s^2),
\tag{9}
\]

then exactly

\[
\boxed{
A_{a,t}
=a^2J+\frac{(t-aC_+)^2}{2}>0
\qquad(a>0,\ t\in\mathbb R).
}
\tag{10}
\]

Hence every density-normalized positive affine recentering of the already-forced source has the same wrong sign after reflection:

\[
\operatorname{Re}m_{a,t,-}(iy)
=\log y-B_{a,t}+\frac{A_{a,t}}{y^2}+o(y^{-2}),
\tag{11}
\]

while

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)
=\log\frac y2-\frac1{24y^2}+O(y^{-4}).
\tag{12}
\]

In particular, even translations `t<-log 2` that move finitely many Mangoldt atoms to negative energy cannot fix the mismatch. The remaining escape is not a better origin or scale choice: it requires a genuinely new boundary/archimedean sector, quotient/compression, non-affine coupling, determinant/scattering mechanism, or another structural modification.

## 1. The logarithmic second coefficient is the exact translation invariant

From (2),

\[
sF(s)=1+C_+s+A_0s^2+O(s^3),
\tag{13}
\]

so

\[
\log(sF(s))
=C_+s+\left(A_0-\frac{C_+^2}{2}\right)s^2+O(s^3).
\tag{14}
\]

A translation by `t` multiplies `F` by `e^{-ts}`. Therefore

\[
\log\!\bigl(s e^{-ts}F(s)\bigr)
=-ts+\log(sF(s)),
\tag{15}
\]

and the quadratic coefficient `J` is unchanged. This is the conceptual form of the quadratic law in `WP-306`: completing the square gives

\[
A_t
=J+\frac{(t-C_+)^2}{2}.
\tag{16}
\]

Thus the unrestricted-translation question reduces exactly to the sign of one source invariant. No support assumption enters (14)--(16).

## 2. The same invariant controls translation and positive dilation together

The density-normalized affine transform (8) has Laplace transform

\[
G_{a,t}(s)=a e^{-ts}F(as).
\tag{17}
\]

Multiplying by `s` and taking logarithms yields the particularly rigid identity

\[
\log\!\bigl(sG_{a,t}(s)\bigr)
=-ts+\log\!\bigl(asF(as)\bigr).
\tag{18}
\]

Consequently

\[
C_{a,t}=aC_+-t,
\qquad
A_{a,t}-\frac{C_{a,t}^2}{2}=a^2J.
\tag{19}
\]

Solving (19) for `A_{a,t}` gives (10). Positive dilation can rescale the obstruction but cannot reverse it, and translation can only add the nonnegative square. This also shows why choosing `t` from the target cannot help: even the formal optimum `t=aC_+` leaves the strictly positive residue `a^2J`.

The scalar factor `a` in (8) is not a tuning parameter. A pushforward under `E->aE+t` changes the asymptotic source density from `1` to `1/a`; multiplying by `a` is forced if the leading `log y` coefficient is to remain the Riemann-Gamma one. An arbitrary additional positive scalar would simply spoil that already-matched leading normalization.

## 3. A coarse exact bound already gives `J>0`

Substituting (3)--(4) into (5) gives

\[
J
=\frac{\gamma^2}{2}+2\gamma_1
+T-\frac{D^2}{2},
\qquad
T:=\sum_{n\ge2}
\frac{\Lambda(n)(\log n-\gamma)}{n(n+1)}.
\tag{20}
\]

The proof needs only deliberately coarse rational estimates.

First, `D<1/2`. Put `f(x)=1/(x(x+1))` and `psi(x)=sum_{n<=x}Lambda(n)`. Rosser--Schoenfeld's global estimate `psi(x)<1.03883x` allows the weaker convenient bound

\[
\psi(x)<\frac{26}{25}x.
\tag{21}
\]

The terms through `10` are

\[
D_{10}
=\log2\left(\frac16+\frac1{20}+\frac1{72}\right)
+\log3\left(\frac1{12}+\frac1{90}\right)
+\frac{\log5}{30}+\frac{\log7}{56}.
\tag{22}
\]

Using `log2<7/10`, `log3<11/10`, `log5<17/10`, and `log7<2`,

\[
D_{10}<\frac{9013}{25200}.
\tag{23}
\]

For the tail, Stieltjes integration by parts gives

\[
R_{10}:=\sum_{n\ge11}\Lambda(n)f(n)
=-\psi(10)f(10)+\int_{10}^{\infty}\psi(x)(-f'(x))\,dx.
\tag{24}
\]

Since `psi(10)=log 2520>7`, (21), `f(10)=1/110`, and `log(11/10)<1/10` imply

\[
\begin{aligned}
R_{10}
&<\frac{\frac{26}{25}10-7}{110}
+\frac{26}{25}\int_{10}^{\infty}\frac{dx}{x(x+1)}\\
&<\frac{17/5}{110}+\frac{26}{25}\frac1{10}
=\frac{371}{2750}.
\end{aligned}
\tag{25}
\]

Therefore

\[
D<D_{10}+R_{10}
<\frac{682699}{1386000}
<\frac12.
\tag{26}
\]

Second, every term of `T` is positive because `log2>gamma`. It is enough to keep the prime powers at most `10`. Using

\[
\gamma<\frac35,
\qquad
\log2>\frac{69}{100},
\qquad
\log3>1,
\qquad
\log5>\frac85,
\qquad
\log7>\frac{19}{10},
\tag{27}
\]

one obtains directly

\[
\begin{aligned}
T
&>\frac{69/100}{6}\left(\frac{69}{100}-\frac35\right)
+\frac1{12}\left(1-\frac35\right)\\
&\quad+\frac{69/100}{20}\left(\frac{138}{100}-\frac35\right)
+\frac{8/5}{30}\left(\frac85-\frac35\right)\\
&\quad+\frac{19/10}{56}\left(\frac{19}{10}-\frac35\right)
+\frac{69/100}{72}\left(\frac{207}{100}-\frac35\right)\\
&\quad+\frac1{90}\left(2-\frac35\right)\\
&=\frac{4981457}{25200000}
>\frac{19}{100}.
\end{aligned}
\tag{28}
\]

Finally, the classical bounds

\[
\frac12<\gamma<\frac35,
\qquad
\gamma_1>-\frac1{12}
\tag{29}
\]

(the latter from the same Blagouchine enveloping estimate already used in `WP-306`) combine with (20), (26), and (28):

\[
J
>\frac18-\frac16+\frac{19}{100}-\frac18
=\boxed{\frac7{300}}.
\tag{30}
\]

The margin is intentionally loose. The point is the exact sign, not a fitted numerical coefficient.

## 4. Adversarial controls

### Generic positivity does not force `J>0`

The sign in (6) is arithmetic-source-specific, not a generic consequence of a positive Herglotz measure. For the positive unit-density control

\[
d\mu_{q,L}(E)=\mathbf 1_{[0,\infty)}(E)\,dE+q\,\delta_L,
\qquad q,L>0,
\tag{31}
\]

its Laplace transform is

\[
F_{q,L}(s)=\frac1s+q-qLs+O(s^2),
\tag{32}
\]

so

\[
J_{q,L}=-qL-\frac{q^2}{2}<0.
\tag{33}
\]

Thus neither positivity, unit asymptotic density, nor Herglotz theory itself imposes the Mangoldt sign. The obstruction comes from the exact arithmetic source in (1).

### The result is not a Weil-positivity theorem

Equation (30) does not prove any global Weil quadratic form nonnegative. It only rules out an affine-coordinate escape from the local finite-source/Gamma mismatch found in `WP-305`. The global pole term, the full archimedean sector, and an independent geometric sign theorem remain absent.

### Negative dilation is a different operation

The restriction `a>0` is structural: it preserves the orientation of the one-sided high-energy carrier. A negative dilation reverses that carrier and duplicates the reflection/orientation operation already separated in `WP-305`; it is not an affine recentering of the same positive-side source.

### Non-affine and genuinely global modifications remain open

A new positive boundary measure, a non-affine source transformation, a quotient/compression, a finite--archimedean coupling, or a determinant/scattering construction can change the quadratic coefficient. Such a modification is admissible only if Mathia forces it independently; choosing it to manufacture `-1/24` would be the target-programming excluded by the line mandate.

## 5. Prior-art and novelty audit

The Herglotz representation, the Laurent/Stieltjes constants, and the fact that translation adds only a linear term to a logarithmic Laplace transform are classical. Rosser--Schoenfeld supplies only the coarse unconditional estimate used to certify `D<1/2`. None of those ingredients is claimed as new.

A targeted search around Herglotz/Nevanlinna representations, translated Mangoldt measures, Stieltjes-constant expansions, and Gamma-factor spectral models did not locate a standard theorem identifying the specific coefficient

\[
[s^2]\log\!\left(
 s\sum_{n\ge2}\frac{\Lambda(n)}{n+1}n^{-s}
\right)
\tag{34}
\]

as strictly positive and using that sign to exclude every density-normalized affine recentering from the Riemann-Gamma curvature. The durable contribution here is therefore narrow: an exact source-specific obstruction and the invariant that exposes it, not a new general Herglotz or cumulant theorem.

The closest local prior art is `WP-305`, which found the wrong curvature at the canonical origin, and `WP-306`, which derived the translation law but only proved positivity on the support-preserving half-line `t>=-log2`. Equation (30) removes that remaining support hypothesis, while (18)--(19) simultaneously closes positive dilation plus arbitrary translation.

## Consequence for `weil_positivity`

The canonical finite Mangoldt source has now survived three increasingly permissive normalization tests: additive Herglotz constants cannot alter curvature (`WP-305`), support-preserving translations cannot alter its sign (`WP-306`), and in fact **no real translation or orientation-preserving positive affine rescaling can alter the sign once the leading density is normalized**.

So the finite source cannot be turned into the Riemann archimedean response by choosing a better spectral zero or energy scale. Any surviving Mathia-native route must add structure before the sign theorem: a genuinely new archimedean/boundary sector, a nonlocal finite--infinite coupling, a quotient/compression, determinant/scattering data, or another intrinsic mechanism that produces the Gamma curvature rather than fitting it afterward.
