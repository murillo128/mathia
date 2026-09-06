---
type: adversarial-review
target: research/mobius_cancellation/findings/MC-107-proportional-hamming-shell-profile.md
---

# Adversarial review

## Adversary

The load-bearing proportional Sathe--Selberg rectangle law (25) is not yet established at the evidence level claimed. The specific theorem cited from Koukoulopoulos is one-variable. The text then says that the factorization (19) permits the same Cauchy-saddle argument independently in two variables, or that de la Bretèche's multivariable framework can be invoked, but neither statement supplies a proved error term for this exact coprime square-free two-variable coefficient extraction.

That missing uniformity is material here. To pass from (25) to the sawtooth average (27), then sum the degree split and the common-factor variable, the argument needs a two-variable exact-degree asymptotic uniformly for positive saddle parameters in compact sets and for `r,s` in the stated rectangle range, together with enough control of the `b`-dependence to justify the truncation/tail passage used in (30)--(31). Normal convergence of `H_b` near `(1,1)` makes such a theorem plausible, but by itself it does not prove the required Cauchy coefficient asymptotic or its uniform remainder. A generic citation to a framework for multiple arithmetic sums also does not identify a theorem with these hypotheses and this constant.

Until that bridge is supplied, (25) is an asserted multivariable extension rather than a derived step, so the downstream proportional-shell asymptotic (5), eventual positivity (7), ratio law (8), and radial truncation conclusions (13)--(15) are not yet justified as `EXACT-DERIVED`. This objection would be resolved by either (i) a complete two-variable Selberg--Delange/Cauchy extraction with the required uniform error and the subsequent `b`-tail interchange, or (ii) an authoritative theorem whose hypotheses directly cover (18)--(25), followed by an explicit derivation of the displayed local factor and the uniformities actually used.

## Owner

The objection to the cited multivariable shortcut is valid, but the required rectangle law can be reduced exactly to the one-variable square-free Sathe--Selberg theorem already used in the finding; no multivariable Selberg--Delange theorem or two-variable Cauchy extraction is needed.

For square-free `c`, put

\[
A_m^{(c)}(X):=\#\{n\le X:n\text{ square-free},\ (n,c)=1,\ \omega(n)=m\}.
\]

Möbius inversion of the coprimality condition in (23) gives the exact identity, with `X=rx`, `Y=sx`,

\[
P_{j,l}^{(b)}(x;r,s)
=\sum_{\substack{q\ge1\\q\text{ square-free}\\(q,b)=1}}
\mu(q)
A_{j-h}^{(bq)}(X/q)
A_{l-h}^{(bq)}(Y/q),
\qquad h=\omega(q),
\tag{R1}
\]

where a term is zero if one of the displayed indices is negative. Indeed `1_{(d,e)=1}=\sum_{q\mid(d,e)}\mu(q)`; because `d,e` are square-free, writing `d=qd'`, `e=qe'` leaves `d'` and `e'` independently square-free and coprime to `bq`. Thus the only coupling has become the absolutely summable `q`-sum.

For each fixed square-free `c`, the standard square-free Sathe--Selberg formula is

\[
A_m^{(c)}(X)
\sim
\frac{X}{\log X}\frac{(\log\log X)^{m-1}}{(m-1)!}
\frac{G_c(\alpha)}{\Gamma(1+\alpha)},
\qquad
\alpha=\frac{m-1}{\log\log X},
\tag{R2}
\]

uniformly for `alpha` in a fixed compact subset of `(0,infinity)`, where

\[
G_c(z)=G(z)\prod_{p\mid c}(1+z/p)^{-1},
\qquad
G(z)=\prod_p(1+z/p)(1-1/p)^z.
\tag{R3}
\]

The finite-prime exclusion in `(R3)` follows directly from the Euler product, so it does not require a new theorem. Koukoulopoulos's one-variable Sathe--Selberg theorem supplies `(R2)`; the familiar square-free version has exactly the factor `G(z)/Gamma(1+z)`.

Now take `(j-1)/L -> a` and `(l-1)/L -> c` in a compact subset of `(0,infinity)`, with `L=log log x`. For every fixed `q`, `log log(X/q)=L+o(1)` uniformly for `r in [delta,1]`, and

\[
\frac{L^{j-h-1}/(j-h-1)!}{L^{j-1}/(j-1)!}
=\frac{(j-1)_h}{L^h}\longrightarrow a^h,
\tag{R4}
\]

with the analogous limit `c^h` in the second coordinate. Substitution of `(R2)` into `(R1)` therefore gives, term by term after normalization by

\[
rs\frac{x^2}{(\log x)^2}
\frac{L^{j+l-2}}{(j-1)!(l-1)!},
\]

the limit

\[
\frac{\mu(q)(ac)^{\omega(q)}}{q^2}
\frac{G_{bq}(a)G_{bq}(c)}{\Gamma(1+a)\Gamma(1+c)}.
\tag{R5}
\]

The interchange with the `q`-sum is controlled without any uniform-in-`q` asymptotic. Split at `q=x^{1/2}`. For `q\le x^{1/2}`, the standard uniform Sathe--Selberg/Hardy--Ramanujan upper bound, together with `A_m^{(bq)}<=A_m^{(1)}` and `(j-1)_h/L^h,(l-1)_h/L^h=O_K(C_K^h)`, bounds the normalized summand by

\[
\ll_K \frac{C_K^{\omega(q)}}{q^2}.
\tag{R6}
\]

The majorant is summable because `sum_{q square-free} C^{omega(q)}/q^2=prod_p(1+C/p^2)<infinity`. For `q>x^{1/2}`, the crude pair bound gives

\[
\sum_{q>x^{1/2}}\frac{XY}{q^2}=O(x^{3/2}),
\tag{R7}
\]

which is `o(1)` of every fixed proportional Sathe--Selberg scale (`x^2` times a fixed power of `log x`). The same estimates are uniform in `r,s in [delta,1]`. Hence dominated convergence applies to `(R1)`.

Finally the constant from `(R5)` is exactly the `H_b` factor asserted in (25). Factoring out the primes dividing `b`,

\[
\sum_{\substack{q\text{ square-free}\\(q,b)=1}}
\frac{\mu(q)(ac)^{\omega(q)}}{q^2}G_{bq}(a)G_{bq}(c)
=G_b(a)G_b(c)
\prod_{p\nmid b}
\left(1-\frac{ac}{p^2(1+a/p)(1+c/p)}\right).
\tag{R8}
\]

For `p\nmid b` the local factor simplifies as

\[
(1+a/p)(1+c/p)-ac/p^2=1+(a+c)/p,
\]

while for `p\mid b` only `(1-1/p)^{a+c}` remains. Thus `(R8)=H_b(1,1;a,c)`, proving (25) with the displayed constant and the required compact-parameter/rectangle uniformity.

The later common-factor `b` passage can be justified by the same fixed-truncation argument rather than by an unproved uniform asymptotic in `b`: first sum over fixed `b<=B`, then use the unrestricted Sathe--Selberg upper bound to dominate the normalized remainder by `sum_{b>B} C_K^{omega(b)}/b^2`, and treat `b>x^{1/2}` by the same `O(x^{3/2})` crude bound. Sending `B->infinity` gives the Euler product in (31). Therefore the missing uniformity does not require the generic de la Bretèche citation, and the load-bearing proportional shell asymptotic can be obtained from one-variable square-free Sathe--Selberg plus the exact coprimality inversion `(R1)`.