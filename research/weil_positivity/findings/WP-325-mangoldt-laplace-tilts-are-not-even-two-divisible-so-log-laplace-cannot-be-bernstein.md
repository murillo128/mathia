---
id: WP-325
title: Mangoldt Laplace tilts are not even two-divisible, so their log-Laplace transform cannot be Bernstein
branch: weil_positivity
status: supported
kind: source-log-laplace-infinite-divisibility-obstruction
claim_strength: exact support-theoretic failure of square-root complete monotonicity for every positive Laplace tilt of the pole-normalized Mangoldt source, closing the canonical nonlinear log-Laplace/Bernstein escape left after direct translation total positivity failed
created: 2026-09-16
related: [WP-009, WP-304, WP-324]
prior_art:
  - René L. Schilling, Renming Song, and Zoran Vondracek, Bernstein Functions: Theory and Applications, 2nd revised and extended edition, De Gruyter Studies in Mathematics 37, 2012, for Bernstein functions as Laplace exponents of subordinators and complete monotonicity of their exponential semigroups
  - Gwo Dong Lin and Chin-Yuan Hu, The Riemann zeta distribution, Bernoulli 7 (2001), no. 5, 817-828, for the classical infinitely divisible zeta distribution in the Euler-product half-plane
  - Takashi Nakamura and Masatoshi Suzuki, On infinitely divisible distributions related to the Riemann hypothesis, Statistics & Probability Letters 201 (2023), 109889, DOI 10.1016/j.spl.2023.109889, for the classical prime-power Levy measure of the zeta distribution and the RH-equivalent completed infinite-divisibility criterion
---

# WP-325 — Mangoldt Laplace tilts are not even two-divisible, so their log-Laplace transform cannot be Bernstein

## Claim

`WP-324` shows that the direct Laplace transform of the positive pole-normalized Mangoldt source does not escape universal positive-measure geometry: its ordered translation minors have the wrong sign for Pólya-frequency positivity, while reversing orientation gives universal Hankel total positivity. A natural nonlinear escape remains. Instead of using the Laplace transform itself as the positive kernel, normalize it to a probability law and ask whether its **negative logarithm** is a Bernstein/Lévy exponent. If that worked, positivity would be inherited from a genuine source-dependent convolution semigroup rather than from a Gram identity valid for every positive measure.

For the exact source from `WP-304`,

\[
\mu_+
=
\sum_{n=p^k}\frac{\Lambda(n)}{n+1}\,\delta_{\log n},
\qquad
L(s)=\int_0^\infty e^{-sE}\,d\mu_+(E),
\quad s>0,
\tag{1}
\]

fix any `s>0` and form the exponentially tilted probability measure

\[
\nu_s(dE)
:=
\frac{e^{-sE}}{L(s)}\,\mu_+(dE).
\tag{2}
\]

Its normalized future Laplace transform is

\[
R_s(t)
:=
\frac{L(s+t)}{L(s)}
=
\int_0^\infty e^{-tE}\,d\nu_s(E),
\qquad t\ge0.
\tag{3}
\]

Thus `R_s` is completely monotone for the universal reason that it is a probability Laplace transform. The source-selective nonlinear candidate is

\[
\psi_s(t):=-\log R_s(t).
\tag{4}
\]

The decisive fact is

\[
\boxed{
\nu_s\text{ is not even two-divisible for any }s>0.
}
\tag{5}
\]

Equivalently,

\[
\boxed{
\sqrt{R_s(t)}\text{ is not completely monotone on }[0,\infty).
}
\tag{6}
\]

Consequently

\[
\boxed{
\psi_s=-\log R_s\text{ is not a Bernstein function for any }s>0.
}
\tag{7}
\]

The proof uses only the first two prime-power atoms and one forced convolution atom. Let

\[
a=\log2,
\qquad
b=\log3.
\tag{8}
\]

Every atom of `nu_s` has positive mass, `a` is its smallest support point, `b` is its second smallest support point, and there is no source mass in `(a,b)`. If a probability `rho` satisfied `rho*rho=nu_s`, the atom at `a` forces an atom of `rho` at `a/2`. The gap `(a,b)` then forces `rho` to have no mass in `(a/2,b-a/2)`. But the positive atom of `nu_s` at `b` consequently forces an atom of `rho` at

\[
c=b-\frac a2.
\tag{9}
\]

The self-convolution of that atom then forces positive `nu_s` mass at

\[
2c=2b-a
=
\log\frac92,
\tag{10}
\]

which is impossible because `9/2` is not an integer prime power. This contradiction is independent of the actual positive weights and therefore survives every exponential tilt in (2).

This closes a genuinely different escape from `WP-324`. The direct transform failed because positivity of a measure forces the wrong translation-determinant curvature. Here the nonlinear logarithm would have converted the source into a **source-selective** positive convolution geometry if the source law were infinitely divisible, but the exact prime-power support itself forbids even the first nontrivial convolution root.

There is an important matched control. The alternative nonlinear map

\[
1-R_s(t)
=
\int_0^\infty(1-e^{-tE})\,d\nu_s(E)
\tag{11}
\]

*is* a Bernstein function for every probability measure on positive energies. It is simply the Laplace exponent of the compound-Poisson process having `nu_s` as its jump law. Its sign is therefore universal rather than arithmetic-selective, and the resulting state law immediately acquires sums of distinct prime-power energies, i.e. logarithms of mixed composites. So the two canonical source-native Bernstein attempts separate cleanly:

\[
\boxed{
1-R_s\text{ is universally Bernstein but loses prime-power localization,}
}
\tag{12}
\]

whereas

\[
\boxed{
-\log R_s\text{ would retain the law itself as an infinitely-divisible state, but fails already at the square root.}
}
\tag{13}
\]

The classical Riemann zeta distribution is not a counterexample. In the Euler-product half-plane the normalized zeta law is compound Poisson on the **full multiplicative semigroup of integers**, while its Lévy measure is supported on prime powers. The present `nu_s` is instead the normalized **prime-power jump carrier itself**. Confusing the law with its Lévy measure would turn the exact support obstruction above into the already-known Euler-product construction. Likewise, the Nakamura--Suzuki completed infinite-divisibility criterion is RH-equivalent and, under RH, moves the positive Lévy measure to zero ordinates; it does not supply an independent sign theorem for the Mathia source.

**Classification:** `EXACT-DERIVED + DECISIVE-NEGATIVE + NONLINEAR-SOURCE-SELECTIVE + PRIME-POWER-SUPPORT-OBSTRUCTION + NOT-TWO-DIVISIBLE + SQUARE-ROOT-CM-FAILURE + LOG-LAPLACE-NOT-BERNSTEIN + COMPOUND-POISSON-MATCHED-CONTROL + ZETA-DISTRIBUTION-PRIOR-ART-REDIRECT + NOT-WEIL-POSITIVITY`.

## 1. Every positive tilt is a probability with the same exact prime-power support

`WP-324` proves that `L(s)` in (1) is finite and strictly positive exactly for `s>0`. Therefore (2) is a probability measure for every such `s`. Explicitly,

\[
\nu_s
=
\frac1{L(s)}
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}n^{-s}\,\delta_{\log n}.
\tag{14}
\]

All coefficients in (14) are strictly positive. Hence

\[
\operatorname{supp}\nu_s
=
\{\log(p^k):p\text{ prime},\ k\ge1\}
\tag{15}
\]

for every `s>0`; exponential tilting changes masses but not support.

The first support points are

\[
\log2<\log3<\log4<\log5<\cdots.
\tag{16}
\]

Only the first gap in (16) is needed below. In particular,

\[
\nu_s((\log2,\log3))=0,
\qquad
\nu_s(\{\log2\})>0,
\qquad
\nu_s(\{\log3\})>0.
\tag{17}
\]

This makes the obstruction insensitive to the asymptotic prime distribution, the prime number theorem, Gamma terms, zeros, or any critical-line hypothesis.

## 2. A convolution square root is impossible

Assume for contradiction that a probability measure `rho` on `[0,infinity)` satisfies

\[
\rho*\rho=\nu_s.
\tag{18}
\]

Set `a=log 2`. Because `nu_s` has no mass below `a`, `rho` cannot have positive mass below `a/2`: if `rho([0,d])>0` for some `d<a/2`, then

\[
(\rho*\rho)([0,2d])
\ge
\rho([0,d])^2>0,
\tag{19}
\]

contradicting (17). Thus

\[
\rho([0,a/2))=0.
\tag{20}
\]

Now `nu_s` has a positive atom at `a`. Under (20), the only way two support points of `rho` can sum to `a` is for both to equal `a/2`. Therefore

\[
0<\nu_s(\{a\})
=(\rho*\rho)(\{a\})
=\rho(\{a/2\})^2,
\tag{21}
\]

so `rho` has a positive atom at `a/2`.

Set `b=log 3`. Because convolution with the atom `a/2` translates every positive piece of `rho`, the source gap `(a,b)` forces

\[
\rho\bigl((a/2,b-a/2)\bigr)=0.
\tag{22}
\]

Indeed, any mass in that interval, convolved with `rho({a/2})>0`, would put positive `nu_s` mass in `(a,b)`.

But `nu_s({b})>0`. With (20) and (22), any pair `x,y` from the support of `rho` satisfying `x+y=b` must have one coordinate equal to `a/2`. If both were strictly larger, each would be at least `b-a/2`, so

\[
x+y\ge2b-a>b.
\tag{23}
\]

Therefore the atom at `b` forces another positive atom at

\[
c=b-a/2:
\qquad
\rho(\{c\})>0.
\tag{24}
\]

Self-convolving this atom gives

\[
(\rho*\rho)(\{2c\})
\ge
\rho(\{c\})^2>0.
\tag{25}
\]

Yet

\[
2c=2\log3-\log2=\log(9/2),
\tag{26}
\]

and `9/2` is not an integer, hence certainly not a prime power. Equations (15), (18), and (25) contradict each other. This proves (5).

The argument is stronger than a weight calculation. **Any probability law with positive atoms at `log 2` and `log 3`, no mass below `log 2` or between those atoms, and support excluding `log(9/2)` fails two-divisibility.** The Mathia source satisfies these conditions for every positive exponential tilt.

## 3. Failure of two-divisibility forbids the Bernstein log-Laplace route

By the Hausdorff--Bernstein--Widder theorem, a function on `[0,infinity)` with value one at the origin is completely monotone exactly when it is the Laplace transform of a probability measure on `[0,infinity)`. Thus if `sqrt(R_s)` were completely monotone there would be a probability `rho` with

\[
\sqrt{R_s(t)}
=
\int_0^\infty e^{-tE}\,d\rho(E).
\tag{27}
\]

Squaring (27) and using uniqueness of Laplace transforms would give `rho*rho=nu_s`, contradicting Section 2. Hence (6).

Now suppose `psi_s=-log R_s` were Bernstein. Standard Bernstein/subordinator calculus says that for every `q>0`,

\[
e^{-q\psi_s(t)}
\tag{28}
\]

is completely monotone: it is the Laplace transform of the subordinator at time `q`. Taking `q=1/2` gives

\[
e^{-\psi_s(t)/2}=\sqrt{R_s(t)},
\tag{29}
\]

contradicting (6). Therefore (7) follows.

This is exactly the source-selective test that `WP-324` could not supply. Complete monotonicity of `R_s` itself says only `nu_s>=0`; failure of complete monotonicity after taking the square root detects an additive-closure obstruction specific to the prime-power support.

## 4. Universal compound-Poissonization is positive but destroys the localization one wanted to preserve

For any probability measure `nu` on `[0,infinity)`,

\[
\Phi_\nu(t)
:=
\int(1-e^{-tE})\,d\nu(E)
\tag{30}
\]

is a Bernstein function with finite Lévy measure `nu`. Applied to `nu_s`, this is exactly (11). Consequently

\[
\exp[-u(1-R_s(t))]
\tag{31}
\]

is completely monotone for every `u>=0`.

But (30) is a matched control: it works for every positive probability law. Its compound-Poisson state after two or more jumps contains sums

\[
\log(p^k)+\log(q^\ell)
=
\log(p^kq^\ell),
\qquad p\ne q,
\tag{32}
\]

so mixed composites appear immediately. The prime-power support remains only in the Lévy **jump intensity**, not in the state distribution whose Laplace transform carries the positive semigroup.

This distinction is exactly what happens in the classical zeta distribution. For `sigma>1`, Euler's product gives an infinitely divisible law on logarithms of all integers whose Lévy measure is supported on prime powers. `WP-009` already records the corresponding intensities. Lin--Hu and the summary in Nakamura--Suzuki are therefore close prior art, but they do not contradict Section 2: they prove infinite divisibility of the semigroup closure generated by prime-power jumps, not of the normalized prime-power jump law itself.

## 5. Prior-art and novelty audit

No novelty is claimed for the Hausdorff--Bernstein--Widder theorem, Bernstein functions, subordinators, Lévy--Khintchine theory, compound-Poissonization, or the infinite divisibility of the classical zeta distribution in the Euler-product half-plane. Schilling--Song--Vondracek is the standard reference for the Bernstein/subordinator equivalence used in Section 3. Lin--Hu and Nakamura--Suzuki provide the closest number-theoretic probability controls.

A bounded search around `prime power`, `von Mangoldt`, `infinitely divisible`, and `convolution root` found nearby work on the zeta distribution and functions associated with `log zeta`, but no need to import a literature theorem for the obstruction here: (20)--(26) are an elementary support proof. The Mathia-specific content is the application of that support proof to the exact pole-normalized source isolated in `WP-304`, showing that the most direct nonlinear convolution-semigroup escape left by `WP-324` fails for **every** admissible positive Laplace tilt.

Nakamura--Suzuki also supplies the stronger novelty warning already retained in `WP-009`: a completed zeta object can be infinitely divisible exactly when RH holds, with its positive Lévy measure then expressed through zero ordinates. Such a construction is outside the mandate's independent-sign requirement and is not a rescue of (4).

## Consequence for the research line

`WP-324` left open the possibility that a nonlinear source-forced transformation could turn the positive Mangoldt Herglotz/Laplace carrier into a source-selective positive geometry. `WP-325` separates the two canonical Bernstein possibilities and closes both as routes to the required sign:

- keeping the normalized source law and taking its logarithmic Laplace exponent fails because the law is not even two-divisible;
- treating the source law as a Lévy jump measure succeeds automatically, but only by universal compound-Poissonization and by enlarging support to mixed composites.

Thus a surviving scalar nonlinear mechanism cannot obtain its independent sign merely from **infinite divisibility generated by the exact positive prime-power carrier**. It must either use a different exact source invariant, introduce the finite/archimedean completion before positivity is taken, or change category to a matrix/operator-valued, nonseparable, infinite-domain, or genuinely cohomological construction.

This finding does **not** exclude every nonlinear functional of `L`, every infinitely divisible law constructed from richer arithmetic data, or every convolution structure after a source-forced global completion. It excludes the canonical normalized log-Laplace/Bernstein route and identifies universal compound-Poissonization as its matched-control fallback rather than a Weil positivity mechanism.