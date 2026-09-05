# MC-078 — Fixed residue-class prime allocation produces only logarithmic factor cancellation

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-074` requires any useful factorization of Möbius to fix the Dirichlet-convolution gauge by arithmetic structure external to the identity `a*k=mu`. `MC-075` closes the most intrinsic internal fixing, fractional powers of `zeta`, and `MC-077` closes arbitrary gauges made cheap merely by approaching the convolution identity in a harmonic coefficient norm.

A natural remaining escape is genuinely arithmetic and far from the identity: **partition the rational primes into fixed congruence classes, assign each prime wholly to one factor, and let the two disjoint prime sets recombine to Möbius.** This fixes a nontrivial gauge without fractionally splitting any Euler factor.

That route still cannot distribute Mertens power cancellation.

Fix an integer `q>=3`. Let `G=(Z/qZ)^*`, choose a nonempty proper subset `S subset G`, put `T=G\S`, and write

\[
\delta=\frac{|S|}{\varphi(q)}\in(0,1).
\tag{1}
\]

Assign the finitely many primes dividing `q` arbitrarily to one of the two sides. Define multiplicative functions `a_S,b_T` by the prime-local rules

\[
A_p(z)=\sum_{j\ge0}a_S(p^j)z^j,
\qquad
B_p(z)=\sum_{j\ge0}b_T(p^j)z^j,
\]

with

\[
(A_p(z),B_p(z))=
\begin{cases}
(1-z,1),&p\in P_S,\\
(1,1-z),&p\in P_T,
\end{cases}
\tag{2}
\]

where, away from the conductor primes, `P_S` consists of primes whose residue modulo `q` lies in `S` and `P_T` is its complement. Then every prime receives the Möbius Euler factor exactly once, so coefficientwise

\[
\boxed{a_S*b_T=\mu.}
\tag{3}
\]

Both factors are square-free supported and take only values in `{-1,0,1}`. They are not near the convolution identity in the sense of `MC-077`: each contains a positive-density set of prime coefficients equal to `-1`.

Nevertheless the fixed-modulus prime number theorem in arithmetic progressions gives, for every fixed `A>0`,

\[
\sum_{p\le x}a_S(p)\log p
=-\delta x+O_{q,A}\!\left(\frac{x}{(\log x)^A}\right),
\tag{4}
\]

and

\[
\sum_{p\le x}b_T(p)\log p
=-(1-\delta)x+O_{q,A}\!\left(\frac{x}{(\log x)^A}\right).
\tag{5}
\]

Applying the Granville--Koukoulopoulos Landau--Selberg--Delange theorem (`MC-S14`) therefore yields nonzero constants `C_S,C_T` such that

\[
\boxed{
\sum_{n\le x}a_S(n)
\sim
C_S\,x(\log x)^{-1-\delta},
}
\tag{6}
\]

and

\[
\boxed{
\sum_{n\le x}b_T(n)
\sim
C_T\,x(\log x)^{-2+\delta}.
}
\tag{7}
\]

In particular, neither factor has any fixed power saving:

\[
\sum_{n\le x}a_S(n)\ne O(x^{1-\eta}),
\qquad
\sum_{n\le x}b_T(n)\ne O(x^{1-\eta})
\tag{8}
\]

for every fixed `eta>0`.

For a balanced prime allocation `delta=1/2`, both sides have the same scale

\[
\boxed{x(\log x)^{-3/2}.}
\tag{9}
\]

Thus a discrete, source-natural, externally fixed prime partition reproduces the same logarithmic exponent as the symmetric fractional gauge `d_{-1/2}` in `MC-075`, even though the local constructions are completely different. In `MC-075` every prime Euler factor is split fractionally between the two factors; here every prime is assigned integrally to exactly one side. The common obstruction is the positive prime-density exponent at `s=1`, not the particular fractional-power parametrization.

No improved estimate for `M(x)` is claimed.

## 1. Exact disjoint-prime factorization

For `p` assigned to `S`, equation `(2)` gives

\[
A_p(z)B_p(z)=1-z.
\]

The same identity holds when `p` is assigned to `T`. Hence the local factor of the Dirichlet convolution `a_S*b_T` is `1-z` at every prime. That is exactly the local factor of Möbius, proving `(3)`.

Equivalently, ignoring the harmless finite convention at primes dividing `q`,

\[
a_S(n)=
\begin{cases}
\mu(n),&\text{every prime divisor of }n\text{ lies in }P_S,\\
0,&\text{otherwise},
\end{cases}
\tag{10}
\]

and analogously for `b_T`. The two factors therefore have genuinely different supports, but their Dirichlet convolution assigns each square-free prime factor to its unique prescribed side and reconstructs the Möbius coefficient exactly.

This is an externally fixed gauge in the sense demanded by `MC-074`: once `q`, `S`, and the finite conductor convention are fixed, there is no arbitrary convolution unit left in the definition.

## 2. Prime-density parameters are negative fractions

For primes not dividing `q`, one has

\[
a_S(p)=-1_{p\bmod q\in S}.
\]

The fixed-modulus prime number theorem in arithmetic progressions (`MC-S15`) gives

\[
\sum_{\substack{p\le x\\p\bmod q\in S}}\log p
=\delta x+O_{q,A}\!\left(\frac{x}{(\log x)^A}\right)
\]

for every fixed `A`, which proves `(4)`. The complement gives `(5)`. Finitely many primes dividing `q` affect only `O_q(\log q)` and cannot change the exponent.

The crucial point is that the Landau--Selberg--Delange prime-average parameters are

\[
\alpha_S=-\delta,
\qquad
\alpha_T=-(1-\delta).
\tag{11}
\]

Both lie strictly between `-1` and `0`. Consequently neither encounters a zero of `1/Gamma(alpha)`; the exceptional integer parameter `alpha=-1` corresponding to Möbius occurs only after the two prime sets are recombined.

## 3. Selberg--Delange gives nonzero near-linear means

Let

\[
F_S(s)=\sum_{n\ge1}\frac{a_S(n)}{n^s}
=\prod_{p\in P_S}(1-p^{-s})
\qquad(\operatorname{Re}s>1),
\tag{12}
\]

with the chosen finite conductor-prime convention included, and define `F_T` analogously. Then

\[
F_S(s)F_T(s)=\frac1{\zeta(s)}.
\tag{13}
\]

Theorem 1 of `MC-S14` applies because `a_S` and `b_T` are multiplicative, bounded by `1`, and satisfy the arbitrarily strong fixed-modulus prime-average errors `(4)`--`(5)`. Its leading terms have the form

\[
\sum_{n\le x}a_S(n)
=
\frac{c_S}{\Gamma(-\delta)}
 x(\log x)^{-1-\delta}
\left(1+O_{q,S}\!\left(\frac1{\log x}\right)\right),
\tag{14}
\]

and

\[
\sum_{n\le x}b_T(n)
=
\frac{c_T}{\Gamma(-(1-\delta))}
 x(\log x)^{-2+\delta}
\left(1+O_{q,S}\!\left(\frac1{\log x}\right)\right).
\tag{15}
\]

Here the leading Euler constants are finite and nonzero. One direct audit is to compare `F_S` with `zeta(s)^(-delta)`. For `sigma>1`,

\[
\log\!\bigl(F_S(s)\zeta(s)^\delta\bigr)
=
-\sum_p\frac{1_S(p)-\delta}{p^s}
+O\!\left(\sum_p p^{-2\sigma}\right),
\tag{16}
\]

up to the finite conductor-prime correction. The residue-class function `1_S-\delta` on `G` is a finite linear combination of nonprincipal Dirichlet characters. The first sum in `(16)` therefore has a finite limit as `s->1+`, since the corresponding nonprincipal `L(1,chi)` values are nonzero; the second sum converges absolutely. Thus

\[
0<|c_S|<\infty.
\tag{17}
\]

The same argument applies to `c_T`. Along the positive real axis the Euler products are positive, so no branch ambiguity is needed to establish nonvanishing. Equation `(13)` also forces the normalized singular factors to be complementary.

Because `0<delta<1`, both `Gamma(-delta)` and `Gamma(-(1-delta))` are finite and nonzero. Equations `(14)`--`(15)` therefore prove `(6)`--`(7)` with nonzero constants.

Finally, for every fixed `eta>0` and fixed `c`,

\[
\frac{x/(\log x)^c}{x^{1-\eta}}
=\frac{x^\eta}{(\log x)^c}\longrightarrow\infty,
\]

which proves `(8)`.

## 4. Balanced allocation and comparison with the symmetric gauge

Take, for example, an odd modulus with a union of exactly half of the reduced residue classes on each side; modulo `3`, the two nonzero classes already give the simplest balanced case. Then `delta=1/2`, and both factors in `(3)` satisfy

\[
\sum_{n\le x}a_S(n),\ 
\sum_{n\le x}b_T(n)
\asymp
\frac{x}{(\log x)^{3/2}}
\]

with nonzero signed leading constants.

This matches the logarithmic exponent in `MC-075`, where the unique exchange-symmetric factor is `d_{-1/2}`. But the coefficient mechanisms are distinct:

- `MC-075`: each local factor `(1-z)` is replaced by two copies of `(1-z)^{1/2}`;
- here: one side receives `(1-z)` and the other receives `1`, prime by prime.

The agreement of exponents is therefore informative. The ordinary summatory scale is controlled by the **average first-order prime coefficient**. A fixed factor owning a fraction `delta` of the Möbius prime factors has parameter `-delta` and hence only a logarithmic mean saving. Recombining the complementary prime fractions changes the parameter from the two nonintegral values in `(11)` to the exceptional integer `-1`, where the generic Selberg--Delange main term disappears.

This is the same discontinuity isolated in `MC-075`, now shown to survive a discrete arithmetic gauge fixing rather than a fractional analytic interpolation.

## 5. Prior art and novelty boundary

Every analytic ingredient is classical. `MC-S14` is the retained theorem-level Landau--Selberg--Delange source; `MC-S15` supplies the fixed-modulus prime number theorem in arithmetic progressions. Granville and Koukoulopoulos explicitly formulate their theorem for multiplicative functions whose prime values have average `alpha`, which is exactly the mechanism used in `(4)`--`(15)`.

There is also old and direct literature on integers all of whose prime factors lie in prescribed arithmetic progressions. Landau already obtained asymptotics for such sets, and Ben Saïd and Nicolas, *Sur une application de la formule de Selberg--Delange*, Colloquium Mathematicum 98 (2003), 223--247, DOI `10.4064/cm98-2-8`, explicitly studies Selberg--Delange asymptotics under prime-factor congruence restrictions. That literature makes clear that prime allocation by arithmetic progression is not a new number-theoretic object.

No novelty is claimed for `(3)`, for the residue-class Euler products, or for the asymptotics `(6)`--`(7)`. The durable Mathia result is the **frontier obstruction** obtained by applying that classical mechanism to the gauge-fixing requirement from `MC-074`--`MC-077`: even a fixed arithmetic partition that is far from the identity and assigns complete Euler factors discretely to the two sides fails to split Möbius into factors with power cancellation.

This result is also distinct from `MC-005`. There the comparator has Möbius's full square-free support and uses residue classes only to choose `+/-` prime signs, showing that exact support plus multiplicativity plus qualitative mean cancellation is too weak. Here the residue classes instead **partition the support of the prime Euler factors between two exact convolution factors of Möbius**. The conclusion concerns factorization/gauge splitting, not a standalone matched sign sequence.

## 6. Boundaries and falsification tests

The obstruction is strong for fixed prime allocations but deliberately not universal.

- The modulus and residue partition are fixed as `x->infinity`. A scale-dependent or dynamically chosen prime partition is not covered by this fixed-parameter Selberg--Delange argument and would require its own uniform theorem and gauge-identifiability audit.
- The conclusion applies to ordinary partial sums of the two factors. It does not rule out a coupled bilinear or weighted statistic in which their nonzero Selberg--Delange modes cancel before absolute values are taken.
- The factors are square-free supported but do not individually have Möbius's full square-free support. That is intentional: their convolution, not either factor alone, carries every prime factor.
- The finite assignment of primes dividing `q` changes only the leading constants, never the logarithmic exponents.
- The proof uses the strong equidistribution available for fixed congruence classes. A highly irregular prime partition with no stable density is outside the claim.
- If one side has density `0` or `1`, the construction collapses to the trivial endpoint factorization `epsilon*mu`; those endpoints are excluded by `(1)`.
- The nonzero leading term depends on the regular fixed-residue distribution. The argument would fail for a prime set whose first-order density cancels but whose Euler product has a different singular structure.
- Nothing here rules out an externally justified gauge class whose factors have genuine sign cancellation at the primes rather than disjoint negative-support allocation.

The finding is falsified if the local identity `(2)` does not yield `(3)`, if the PNT in arithmetic progressions does not give `(4)`--`(5)`, if `MC-S14` does not apply to these bounded multiplicative functions, or if the normalized Euler factors in `(16)` fail to have finite nonzero limits at `s=1`.

## Consequence for the active frontier

`MC-077` left open gauges that are far from the convolution identity and selected by independent arithmetic structure. Fixed congruence-class prime allocation is a clean example of exactly that escape: it is discrete, multiplicative, source-natural, and not produced by coefficient dilution.

It still fails. **Any nontrivial fixed residue-density split gives each factor an ordinary partial sum of order `x` times a fixed negative power of `log x`, never a fixed power saving.** The balanced split even lands on the same `x/log^(3/2)x` scale as the canonical fractional square root from `MC-075`.

A surviving factorization strategy must therefore demand more than external gauge fixing plus a regular division of Euler factors. It must introduce prime-level sign cancellation inside the factors, a nontrivial coupled observable that cancels their Selberg--Delange modes before estimation, or a scale-dependent arithmetic mechanism whose gain survives a uniform identifiability and inversion audit. Merely assigning different rational-prime sectors to different factors cannot distribute the RH-scale Mertens burden.