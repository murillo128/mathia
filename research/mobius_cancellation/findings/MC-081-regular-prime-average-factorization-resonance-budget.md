# MC-081 — Regular prime-average Möbius factorizations have an indivisible Selberg–Delange resonance budget

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-075`, `MC-078`, `MC-079`, and `MC-080` exhibit several very different multiplicative factorizations of Möbius whose separate factors have near-linear Landau–Selberg–Delange means. Those examples could still leave the impression that the obstruction comes from the particular local factorization geometry: fractional zeta powers, prime partitions, square-free support, or bounded infinite prime-power tails.

It does not. In the regular prime-average regime, the obstruction is forced before any of those local choices are specified.

Let `r>=2`, and let

\[
f_1,\dots,f_r:\mathbb N\to\mathbb C
\]

be normalized multiplicative functions satisfying

\[
\boxed{f_1*\cdots*f_r=\mu.}
\tag{1}
\]

Assume that for each `j` there is a fixed divisor-bound parameter `k_j>0` with

\[
|f_j(n)|\le \tau_{k_j}(n),
\tag{2}
\]

and a fixed complex prime-average parameter `\alpha_j` such that, for every fixed `A>0`,

\[
\sum_{p\le x}f_j(p)\log p
=
\alpha_j x+O_{A,j}\!\left(\frac{x}{(\log x)^A}\right).
\tag{3}
\]

Then the prime-average parameters satisfy the exact budget

\[
\boxed{\alpha_1+\cdots+\alpha_r=-1.}
\tag{4}
\]

Moreover, if

\[
F_j(s)=\sum_{n\ge1}\frac{f_j(n)}{n^s}
\qquad(\operatorname{Re}s>1)
\tag{5}
\]

and

\[
c_{j,0}:=
\lim_{s\to1^+}(s-1)^{\alpha_j}F_j(s),
\tag{6}
\]

then the Landau–Selberg–Delange continuation supplied by `MC-S14` makes every limit in `(6)` finite, and the exact factorization `(1)` forces

\[
\boxed{\prod_{j=1}^r c_{j,0}=1.}
\tag{7}
\]

In particular, **none of the leading normalized Euler constants can vanish**.

Consequently, for every factor whose prime-average parameter is not a nonpositive integer,

\[
\alpha_j\notin\mathbb Z_{\le0},
\]

`MC-S14` gives the nonzero leading asymptotic

\[
\boxed{
\sum_{n\le x}f_j(n)
\sim
\frac{c_{j,0}}{\Gamma(\alpha_j)}
 x(\log x)^{\alpha_j-1}.
}
\tag{8}
\]

Hence such a factor has no fixed power saving:

\[
\sum_{n\le x}f_j(n)\ne O(x^{1-\eta})
\qquad(\eta>0\text{ fixed}).
\tag{9}
\]

Therefore, if **all** separate factors are even to avoid an explicit nonzero near-linear Selberg–Delange main term—and in particular if all are to have fixed power cancellation—then necessarily

\[
\alpha_j\in\mathbb Z_{\le0}\qquad(1\le j\le r).
\tag{10}
\]

Together with `(4)`, this has only one possibility:

\[
\boxed{
(\alpha_1,\dots,\alpha_r)
\text{ is a permutation of }
(-1,0,\dots,0).
}
\tag{11}
\]

Thus the exceptional prime-average parameter `-1` responsible for Möbius's disappearance from the generic Selberg–Delange main-term regime **cannot be split nontrivially among several regular multiplicative factors**. Any regular balanced or fractional allocation of the prime average moves the factors away from the Gamma-zero resonance and restores near-linear means.

No improved estimate for `M(x)` is claimed. Equation `(11)` is only a necessary structural condition on any separate-factor power-cancellation strategy in the regular prime-average class; it does not prove power cancellation for the exceptional `-1` factor or for the `0`-average factors.

## 1. The convolution identity fixes the total prime average

At a prime `p`, normalized Dirichlet convolution has no nontrivial proper divisors. Equation `(1)` therefore gives

\[
\mu(p)
=
\sum_{j=1}^r f_j(p).
\tag{12}
\]

Since `\mu(p)=-1`, multiplying by `\log p` and summing over primes yields

\[
\sum_{j=1}^r\sum_{p\le x}f_j(p)\log p
=-\vartheta(x),
\tag{13}
\]

where

\[
\vartheta(x)=\sum_{p\le x}\log p.
\]

Insert `(3)` on the left. The prime number theorem gives `\vartheta(x)=x+o(x)`, hence

\[
(\alpha_1+\cdots+\alpha_r)x+o(x)=-x+o(x),
\]

which proves `(4)`.

This step uses only the coefficient of `p` in the exact convolution. No square-free support, local Bell-series truncation, sign restriction, prime partition, or special Euler-factor parametrization is involved.

## 2. Exact recombination forbids vanishing leading Euler constants

Because `(2)` gives absolute convergence of every `F_j(s)` for `\operatorname{Re}s>1`, equation `(1)` implies

\[
\prod_{j=1}^rF_j(s)
=
\frac1{\zeta(s)}
\qquad(\operatorname{Re}s>1).
\tag{14}
\]

For each `j`, the strong prime-average hypothesis `(3)` is exactly the input of the Granville–Koukoulopoulos theorem retained as `MC-S14`. In particular,

\[
Q_j(s):=(s-1)^{\alpha_j}F_j(s)
\tag{15}
\]

has a continuous boundary value at `s=1` from the half-plane `\operatorname{Re}s\ge1`, with

\[
Q_j(1)=c_{j,0}.
\tag{16}
\]

Along the positive real axis there is no branch ambiguity in `(s-1)^{\alpha_j}`. Multiply `(15)` over `j` and use `(4)` and `(14)`:

\[
\prod_{j=1}^rQ_j(s)
=
(s-1)^{-1}\frac1{\zeta(s)}.
\tag{17}
\]

The classical Laurent expansion `\zeta(s)\sim 1/(s-1)` at `s=1` gives

\[
\lim_{s\to1^+}(s-1)^{-1}\frac1{\zeta(s)}=1.
\tag{18}
\]

Taking limits in `(17)` proves `(7)`.

This removes a possible loophole in a naive prime-average argument. One might hope that a factor has a generic nonintegral `\alpha_j` but an accidentally vanishing normalized Euler constant, so that the leading Selberg–Delange term disappears. Exact recombination to Möbius rules that out simultaneously for every factor: the normalized constants multiply to one.

## 3. Nonresonant prime averages force near-linear separate means

Fix `j` with

\[
\alpha_j\notin\mathbb Z_{\le0}.
\]

The Gamma function has no zeros and has poles precisely at the nonpositive integers, so

\[
\frac1{\Gamma(\alpha_j)}\ne0.
\tag{19}
\]

By `(7)`, `c_{j,0}\ne0`. Apply Theorem 1 of `MC-S14` with `A` chosen arbitrarily large in `(3)`. Its expansion begins with

\[
\frac{c_{j,0}}{\Gamma(\alpha_j)}
 x(\log x)^{\alpha_j-1},
\tag{20}
\]

while every later retained term has an additional inverse power of `\log x`, and the theorem's remainder can be made lower order because `(3)` is available for every fixed `A`. This proves `(8)`.

If `\alpha_j` is complex, the factor `(\log x)^{i\operatorname{Im}\alpha_j}` only rotates the leading phase; its modulus is one. Thus

\[
\left|\sum_{n\le x}f_j(n)\right|
\asymp
x(\log x)^{\operatorname{Re}\alpha_j-1}
\tag{21}
\]

up to a relative `o(1)` along sufficiently large `x`. For every fixed `\eta>0` and fixed real `C`,

\[
\frac{x(\log x)^{-C}}{x^{1-\eta}}
=
\frac{x^\eta}{(\log x)^C}\longrightarrow\infty,
\]

so `(9)` follows regardless of the finite logarithmic exponent.

The only way the generic leading family in `MC-S14` can disappear at the first coefficient while `(7)` holds is therefore the classical Gamma resonance

\[
\alpha_j\in\mathbb Z_{\le0}.
\]

At such parameters `1/\Gamma(\alpha_j-m)=0` for every integer `m\ge0`, so the usual finite Selberg–Delange polynomial main-term expansion vanishes termwise. This is a necessary opening for stronger cancellation, not a proof of it.

## 4. The resonance budget is indivisible

Suppose every separate factor is required to have a fixed power saving, or merely to avoid the forced nonzero near-linear main term `(8)`. Then `(10)` is necessary.

But nonpositive integers summing to `-1` have only the pattern `(11)`: exactly one parameter equals `-1`, and every other parameter equals `0`.

This is the precise sense in which the regular prime-average cancellation budget is indivisible. Möbius itself has prime average `-1`. A factorization can move coefficient-level structure among the factors, including arbitrarily complicated infinite prime-power tails as `MC-080` shows, but if all factors retain stable regular prime averages then the exceptional Selberg–Delange resonance cannot be divided fractionally among them while preserving separate strong cancellation.

For example, a balanced `r`-way allocation has

\[
\alpha_j=-\frac1r
\qquad(1\le j\le r).
\tag{22}
\]

Every parameter is nonresonant, so `(8)` gives

\[
\sum_{n\le x}f_j(n)
\sim
C_j x(\log x)^{-1-1/r},
\qquad C_j\ne0.
\tag{23}
\]

This recovers the logarithmic exponent found independently in the balanced prime-partition class of `MC-079`. For `r=2`, it also recovers the `x(\log x)^{-3/2}` scale seen in the symmetric fractional factor `MC-075`, the balanced residue partition `MC-078`, and the balanced bounded infinite-tail family `MC-080`. The agreement is not an accident of those constructions: it is dictated by their common prime-average parameter `-1/2`.

## 5. Prior art and novelty boundary

The analytic mechanism is classical. `MC-S14` is the retained primary theorem-level source for the Landau–Selberg–Delange expansion from a regular prime average `\alpha`; its formula explicitly contains the factor `1/\Gamma(\alpha-m)`. The exceptional role of nonpositive integer prime averages is therefore standard Selberg–Delange structure, not a new theorem.

The convolution identity `(12)`, multiplication of Dirichlet series `(14)`, and the simple zero of `1/\zeta(s)` at `s=1` are likewise classical. A targeted prior-art search found the same nonpositive-integer small-partial-sum boundary described in the modern multiplicative-function literature; no novelty is claimed for that general principle.

The durable Mathia result is the **scope closure for the current factorization frontier**: combining the exact Möbius convolution with the classical Selberg–Delange boundary forces both the additive budget `(4)` and the nonvanishing product `(7)`. Therefore all regular factorization geometries—regardless of square-free support, finite versus infinite local tails, or how Euler factors are split—face the same all-factor resonance constraint `(11)`.

## 6. Boundaries and falsification tests

- **Regular prime averages are essential.** The claim assumes each factor has a fixed `\alpha_j` with the strong error `(3)`. Highly irregular, scale-dependent, or nonconvergent prime averages are outside the result.
- **The divisor bound is the `MC-S14` entry condition.** A factor outside the theorem's growth class requires a separate asymptotic theory.
- **Equation `(11)` is necessary, not sufficient.** A factor with `\alpha=-1` may still contain essentially the full Möbius difficulty, while factors with `\alpha=0` need not have power cancellation. The theorem does not produce useful factors at the exceptional tuple.
- **The result concerns separate ordinary partial sums.** A coupled signed observable may cancel large factor contributions before separate estimates are taken; this remains one of the principal escapes left by `MC-080`.
- **Nonmultiplicative factorizations are outside the local prime-average setup.** Equation `(12)` uses normalized Dirichlet convolution but the `MC-S14` transfer requires multiplicativity of each factor.
- **No critical-strip zero information is imported.** The only zeta fact used in `(18)` is the classical simple pole at `s=1`; no zero-free continuation toward `\operatorname{Re}s=1/2` enters.
- **Finite Euler-factor cancellations cannot defeat `(7)`.** Whatever local mechanism a factor uses, its normalized boundary constant cannot vanish as long as all hypotheses and exact recombination `(1)` hold.

The finding is falsified if the prime coefficient of `(1)` does not imply `(12)`, if the regular prime averages can satisfy `(3)` with a total parameter different from `-1`, if `MC-S14` fails to give the boundary constants and expansion used above, or if exact recombination permits `\prod_j c_{j,0}\ne1`. Equations `(12)`–`(18)` reduce the new scope claim to direct convolution algebra, the prime number theorem, the simple pole of zeta at one, and the retained classical theorem.

## Consequence for the active frontier

`MC-080` showed that abandoning locally finite Bell series cheaply reopens multiplicative factorization freedom, but its explicit bounded infinite-tail family still had near-linear separate means. The present result explains why that failure persisted and removes the need to classify further regular local splitting formulas one by one.

**Any exact multiplicative Möbius factorization with stable Selberg–Delange prime averages can distribute the prime coefficients, but it cannot distribute the exceptional `-1` resonance among several separately power-cancellative regular factors.** If every factor is to escape a forced near-linear main term, one factor must retain the entire `-1` prime-average parameter and all remaining factors must lie at `0`.

A surviving factorization strategy must therefore exploit structure outside this regular separate-factor regime: genuinely irregular or scale-dependent prime averages with a uniform analytic gain, a coupled signed statistic estimated before the factors are separated, or a nonmultiplicative mechanism. Searching for further balanced fixed multiplicative splits with regular prime statistics cannot distribute the RH-scale Mertens burden.