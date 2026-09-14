---
id: WP-293
title: Exact source-native relocalization is uniquely Möbius and restores the zeta zero screen
branch: weil_positivity
status: supported
kind: exact-convolution-relocalization-no-go
claim_strength: exact uniqueness theorem for scalar source-native arithmetic convolution, with reciprocal-zeta obstruction on the unique inverse
created: 2026-09-14
related: [WP-004, WP-291, WP-292]
prior_art:
  - classical identity 1 * Lambda = log and Möbius inversion Lambda = mu * log
  - G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers, Section 17.7
  - T. M. Apostol, Introduction to Analytic Number Theory, Chapter 2
---

# WP-293 — Exact source-native relocalization is uniquely Möbius and restores the zeta zero screen

## Claim

`WP-292` gives a canonical unconditional category descent by convolving the critical Mangoldt half-density with the counting half-density,

\[
\mu_\Lambda
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n},
\qquad
\nu
=\sum_{m\ge1}\frac1{\sqrt m}\,\delta_{\log m},
\]

so that

\[
\nu*\mu_\Lambda
=\omega
:=\sum_{N\ge2}\frac{\log N}{\sqrt N}\,\delta_{\log N}.
\tag{1}
\]

That finding showed that the canonical inverse is Möbius and therefore restores the reciprocal-zeta / RH-equivalent screen, but left open a narrower loophole: perhaps a *different* exact source-native arithmetic convolution kernel could recover the Mangoldt carrier from `omega` without reintroducing the same zero divisor.

That loophole is closed exactly.

Let `L(n)=log n`, and let `a` be any complex-valued arithmetic function. Define its half-density log-lattice kernel

\[
\eta_a:=\sum_{m\ge1}\frac{a(m)}{\sqrt m}\,\delta_{\log m}.
\tag{2}
\]

Then

\[
\boxed{
\eta_a*\omega=\mu_\Lambda
\quad\Longleftrightarrow\quad
a=\mu_{\rm Mob}.
}
\tag{3}
\]

Thus **Möbius inversion is not merely one convenient exact deconvolution: it is the unique scalar source-native arithmetic convolution that exactly restores Mangoldt localization**.

Consequently the only exact kernel has transform

\[
\mathcal L\eta_a(s)
=\sum_{m\ge1}\frac{\mu_{\rm Mob}(m)}{m^{s+1/2}}
=\frac1{\zeta(s+1/2)}
\tag{4}
\]

on its initial convergence half-plane. Exact relocalization therefore necessarily reinstates the reciprocal-zeta divisor and, after acting on `omega`, the logarithmic-derivative carrier already shown in `WP-291` to have the RH-equivalent temperedness gate after every finite source-native dilation-coboundary hierarchy.

The result is a route closure, not a new number-theory theorem. The arithmetic identities and Möbius inversion are classical; the Mathia-specific content is that the exact scalar convolution escape left open by `WP-292` has no alternative kernel to test.

**Classification:** `EXACT-DERIVED + SOURCE-NATIVE-ARITHMETIC-CONVOLUTION + UNIQUE-MOBIUS-RELOCALIZATION + RECIPROCAL-ZETA-RESTORED + ZERO-SCREEN-UNAVOIDABLE-IN-THIS-CLASS + SIGNED-KERNEL + ROUTE-CLOSURE + CLASSICAL-ARITHMETIC-ALGEBRA + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Half-density convolution reduces exactly to Dirichlet convolution

For any arithmetic function `a`, the coefficient of `eta_a * omega` at `log N` is

\[
\begin{aligned}
(\eta_a*\omega)(\{\log N\})
&=\sum_{d\mid N}
\frac{a(d)}{\sqrt d}
\frac{\log(N/d)}{\sqrt{N/d}}\\
&=\frac1{\sqrt N}
\sum_{d\mid N}a(d)L(N/d)\\
&=\frac{(a*L)(N)}{\sqrt N}.
\end{aligned}
\tag{5}
\]

Therefore exact recovery of the critical Mangoldt half-density is equivalent coefficientwise to

\[
a*L=\Lambda.
\tag{6}
\]

The classical divisor identity

\[
\mathbf 1*\Lambda=L
\tag{7}
\]

and Möbius inversion give one solution,

\[
\mu_{\rm Mob}*L=\Lambda.
\tag{8}
\]

The question is whether another arithmetic kernel can satisfy (6).

## 2. Dirichlet convolution has no zero divisors

The uniqueness does not require analytic continuation or any information about zeta zeros. It follows from an elementary property of the arithmetic-function convolution ring.

Let `f` and `g` be nonzero arithmetic functions. Choose the least positive integers `m,n` with

\[
f(m)\ne0,
\qquad
g(n)\ne0.
\]

In

\[
(f*g)(mn)=\sum_{d\mid mn}f(d)g(mn/d),
\tag{9}
\]

any nonzero summand must satisfy `d>=m` by minimality of `m`, while `mn/d>=n` by minimality of `n`. The latter inequality gives `d<=m`. Hence the only possible nonzero summand is `d=m`, and

\[
(f*g)(mn)=f(m)g(n)\ne0.
\tag{10}
\]

So the Dirichlet-convolution ring of arithmetic functions is an integral domain.

Now if `a` satisfies (6), subtract (8):

\[
(a-\mu_{\rm Mob})*L=0.
\tag{11}
\]

Since `L` is not the zero arithmetic function, (10) forces

\[
\boxed{a=\mu_{\rm Mob}}.
\tag{12}
\]

This proves (3).

## 3. The unique exact inverse is signed and carries the reciprocal-zeta divisor

The uniqueness theorem sharpens the tradeoff in `WP-292`. There is no second exact scalar arithmetic kernel whose coefficients might be positive, better behaved, or analytically independent of the zeta divisor. The unique inverse is the signed Möbius kernel.

On `Re(s)>1/2`, its half-density Laplace transform is

\[
\mathcal L\eta_{\mu}(s)
=\sum_{m\ge1}\frac{\mu_{\rm Mob}(m)}{m^{s+1/2}}
=\frac1{\zeta(s+1/2)}.
\tag{13}
\]

Applying it to the all-integer logarithmic carrier gives

\[
\frac1{\zeta(s+1/2)}\bigl(-\zeta'(s+1/2)\bigr)
=-\frac{\zeta'}{\zeta}(s+1/2),
\tag{14}
\]

exactly the transform of `mu_Lambda`. Thus every nontrivial zeta zero again appears through the reciprocal factor. In particular, composing with any finite source-native dilation-coboundary polynomial gives the class treated by `WP-291`; exact recovery has returned to the same RH-equivalent category gate rather than creating a new positive geometric route.

The sign failure is equally rigid inside this class. Möbius takes both signs infinitely often already on squarefree integers (`mu(p)=-1`, `mu(pq)=+1` for distinct primes), so exact scalar relocalization cannot be performed by a nonnegative source-native arithmetic convolution kernel.

## 4. What this closes — and what it does not

The no-go is deliberately narrow. It rules out only **exact, scalar, linear, source-native arithmetic convolution on the log-integer semigroup** as a way to recover the Mangoldt carrier after the counting smoothing of `WP-292` while avoiding the reciprocal-zeta screen.

It does **not** rule out off-lattice translation-invariant distributions, non-translation-invariant or boundary-conditioned operators, nonlinear/geometric recovery, multi-channel constructions, or approximate/coarse localization. Such mechanisms are genuinely different objects and require their own sign and matched-control tests.

The surviving search frontier is therefore sharper: after the unconditional smoothing in `WP-292`, any route that wants arithmetic localization without immediately returning to `1/zeta` must relax at least one of

\[
\boxed{
\text{exactness},\qquad
\text{scalar source-native convolution},\qquad
\text{one-channel linear recovery}.
}
\tag{15}
\]

That is a concrete reduction of the candidate space. Merely changing the arithmetic convolution coefficients cannot help.

## 5. Falsification and novelty audit

Three failure modes were checked explicitly.

First, the half-density factors in (5) introduce no hidden weight: `sqrt(d)sqrt(N/d)=sqrt(N)`, so the coefficient equation is exactly ordinary Dirichlet convolution. Second, uniqueness does not assume that `L` has a Dirichlet inverse; it uses only the no-zero-divisor property, proved directly in (9)--(10), so the fact that `L(1)=0` is harmless. Third, the conclusion is not promoted beyond the operator class actually tested: arbitrary positive compressions, boundary responses, and nonlinear geometric maps remain outside the theorem.

The literature audit confirms that the ingredients are classical. Standard references record `sum_{d|n} Lambda(d)=log n` and its Möbius inverse, and the ordinary Dirichlet-convolution algebra of arithmetic functions. No novelty is claimed for these facts. The new value for this research line is the exact uniqueness consequence for the `WP-292` smoothing/relocalization program and the resulting closure of an otherwise live alternative-kernel branch.

## Conclusion

`WP-292` showed that counting convolution removes the nontrivial-zero screen by replacing the Mangoldt carrier with the all-integer logarithmic carrier. The present result shows that there is **exactly one** scalar source-native arithmetic convolution that reverses that step: Möbius inversion. Its transform is `1/zeta(s+1/2)`, so exact re-localization necessarily puts the zero divisor back.

Within this operator class there is therefore no hidden exact positive deconvolution waiting to be chosen. Any further attempt to retain the unconditional category improvement of `WP-292` while recovering arithmetic specificity must leave the exact scalar arithmetic-convolution setting rather than tune it.
