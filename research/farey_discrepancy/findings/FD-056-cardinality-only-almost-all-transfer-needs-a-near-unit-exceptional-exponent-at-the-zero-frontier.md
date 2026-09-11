# FD-056 — cardinality-only almost-all transfer needs a near-unit exceptional exponent at the zero frontier

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-SPECIFIC + ALMOST-ALL-MOBIUS + EXCEPTIONAL-SET-LOCALIZATION + ZERO-FRONTIER + ADDITIVE-TRANSFER + NEGATIVE/ROUTE-RESTRICTION + JOINT-NONSQUAREFREE-OCCUPATION`.

`FD-054` and `FD-055` reduce the positive quadratic-transfer problem to a very local source question. If

\[
A_X:=|\mathcal H(X)|
\]

is a large quotient-shell value, then a squarefree Jordan host can transfer comparable energy to a nearby nonsquarefree row provided the corresponding quotient endpoint stays inside a short interval on which `mathcal H` changes by `o(A_X)`. `FD-055` obtains this for **all** source intervals of exponent greater than `0.55`, using the Matomäki--Teräväinen all-short-interval Möbius theorem.

A tempting way to remove that `0.55` restriction is to replace an all-interval theorem by a much stronger **almost-all** theorem. The 2026 theorem of Matomäki--Radziwiłł--Shao--Tao--Teräväinen reaches Möbius intervals of length `X^(1/3+epsilon)` with arbitrary fixed logarithmic saving, so its interval-length range already covers every false-RH zero-frontier exponent `Theta>1/2`.

The obstruction is not interval length. It is localization.

Assume

\[
\frac12<\Theta<1
\]

and take a zero-frontier spike sequence supplied by `FD-046`, so that

\[
\boxed{
A_X=X^{\Theta+o(1)}.
}
\tag{1}
\]

For any fixed `B>=0`, put

\[
R_X:=A_X(\log X)^B.
\tag{2}
\]

Every additive-transfer attempt which preserves the spike while moving its source endpoint by at most `O(R_X)` is confined to a deterministic corridor

\[
\mathcal C_X(B)
:=
[X-C R_X,\,X+C R_X]
\tag{3}
\]

for some fixed `C>0`. Hence

\[
\boxed{
|\mathcal C_X(B)|
=
X^{\Theta+o(1)}.
}
\tag{4}
\]

The one-Lipschitz transfer of `FD-054` lives in such a corridor with `B=0`; the logarithmic penetration of `FD-055` merely replaces it by a polylogarithmically wider corridor and therefore does not change its power exponent.

Now suppose an almost-all short-interval theorem at scale `R_X` says that all source starts are good except for an exceptional set satisfying

\[
\boxed{
|\mathcal E_X|
\ll
X R_X^{-c+o(1)}
}
\tag{5}
\]

for some fixed `c>=0`, and suppose optimistically that its cancellation estimate is already strong enough to preserve the spike whenever the selected start is good.

Then **exceptional-set cardinality alone** can force a good start inside the adaptive transfer corridor only if

\[
|\mathcal E_X|=o(|\mathcal C_X(B)|).
\]

Using (1)--(5), this requires

\[
1-c\Theta<\Theta,
\]

or equivalently

\[
\boxed{
c>
\frac{1-\Theta}{\Theta}.
}
\tag{6}
\]

Thus the almost-all route has an exact localization threshold. Near the critical line it needs an exceptional-set exponent arbitrarily close to `1`:

\[
\frac{1-\Theta}{\Theta}
\longrightarrow 1
\qquad(\Theta\downarrow1/2).
\tag{7}
\]

At the upper edge of the band not covered by `FD-055`, `Theta=0.55`, the required exponent is already

\[
\boxed{
\frac{1-0.55}{0.55}
=
\frac9{11}
=0.81818\ldots .
}
\tag{8}
\]

So the missing input is not a generic statement that the bad intervals have density zero, nor even an arbitrary unspecified power saving. A cardinality-only bridge through the unresolved near-critical regime needs a quantitatively near-optimal exceptional-set exponent.

## 1. Why the 2026 almost-all theorem does not close the gap

Theorem 1.1(i) of Matomäki--Radziwiłł--Shao--Tao--Teräväinen gives, after taking the trivial nilsequence, the Möbius estimate

\[
\left|
\sum_{x<n\le x+H}\mu(n)
\right|^*
\le
\frac{H}{(\log X)^K}
\tag{9}
\]

for any fixed `K>0`, whenever

\[
X^{1/3+\varepsilon}
\le H\le
X^{1-\varepsilon},
\]

outside an exceptional set of measure

\[
\boxed{
O_{K,\varepsilon}
\!\left(
\frac{X}{(\log X)^K}
\right).
}
\tag{10}
\]

On a spike sequence with `1/2<Theta<1`, the choice

\[
H=R_X=A_X(\log X)^B
\]

lies inside this length range for suitable fixed `epsilon>0`. If `K>B`, the analytic error in (9) has size

\[
\frac{R_X}{(\log X)^K}
=
A_X(\log X)^{B-K}
=o(A_X),
\tag{11}
\]

which is exactly the kind of relative error the additive-transfer mechanism would like.

But the allowed exceptional set is much larger than the entire transfer corridor:

\[
\boxed{
\frac{X(\log X)^{-K}}
{R_X}
=
X^{1-\Theta+o(1)}
(\log X)^{-K-B}
\longrightarrow\infty.
}
\tag{12}
\]

This remains true for **every fixed** `K`. Choosing a larger fixed logarithmic saving never beats the polynomial localization gap `X^(1-Theta)`.

Consequently the 2026 theorem is logically compatible with the entire corridor `mathcal C_X(B)` being exceptional. It may well be that the actual exceptional set is located elsewhere, but its published global measure bound does not say so. Therefore the theorem cannot, by itself, certify even one good adaptive transfer interval tied to a zero-frontier spike.

This conclusion is deliberately stronger than needed in one respect: (12) is a **best-case obstruction**. Passing an almost-all estimate for `mu` through the divisor convolution defining `Delta mathcal H` could introduce additional exceptional sets at rescaled starts. Even if that transfer were granted for free with no loss in exceptional-set size, the localization problem (12) would remain.

## 2. The general exponent threshold

Equation (6) is useful independently of the specific 2026 result. Suppose future work provides a power-saving exceptional estimate

\[
|\mathcal E_X|
\ll X H^{-c+o(1)}
\]

at `H=X^(Theta+o(1))`, together with an error small enough to preserve a zero-frontier spike. Then pure cardinality crosses the adaptive corridor precisely when

\[
c>rac{1-\Theta}{\Theta}.
\]

For `Theta` just above `1/2`, this is essentially an `X/H`-scale exceptional budget. Put differently, the number of bad starts must be nearly as small as one would expect from an inverse-length law before global counting alone can locate a good start inside a corridor whose own length is only `H`.

This explains why the distinction between **all intervals** and **almost all intervals** is unusually severe here. For ordinary average applications a density-zero exceptional set is often enough. Here the source spike itself selects a window of only `X^(Theta+o(1))` possible endpoints inside an ambient interval of length `asymp X`; when `Theta` is near `1/2`, that window occupies only about a square-root fraction of the ambient scale.

Matomäki--Radziwiłł's quantitative almost-all theory already supplies power-saving exceptional-set estimates for multiplicative functions and is therefore important prior art for this question. The point of (6) is not that power-saving exceptional bounds are new, but that Mathia's adaptive transfer requires a very specific exponent **at the same error tolerance that preserves the spike**. That tolerance/exponent matching must be checked theorem by theorem; an unspecified positive power saving is not enough in the near-critical band.

## 3. Adversarial checks

There are several easy ways to overstate this barrier.

First, (6) is **not** a theorem saying that the spike corridor is actually exceptional. It says only that a global exceptional-set cardinality bound weaker than the corridor size cannot rule that possibility out. Any additional structural information proving that the exceptional set avoids reciprocal/floor-selected endpoints could bypass the counting threshold completely.

Second, the maximal `*` in the 2026 theorem does not repair the localization problem. It strengthens the cancellation statement *inside each nonexceptional interval* by taking a supremum over arithmetic progressions, but it does not constrain where the exceptional starting points lie.

Third, allowing the `FD-055` corridor to grow by arbitrary fixed powers of `log X` does not change (6):

\[
R_X=X^{\Theta+o(1)}
\]

with or without those factors. A genuine power enlargement of the admissible transfer distance would be different, but that is exactly the source regularity not presently available.

Fourth, `FD-046` supplies spike sequences, not a positive density of spike locations in every dyadic block. One therefore cannot average the global exceptional set over many spike corridors without an additional density theorem for large shell values.

Finally, the restriction `Theta<1` is intentional. The unresolved regime targeted here is `1/2<Theta<=0.55`, where the comparison is decisive. If the zero frontier were `Theta=1`, the corridor could have nearly ambient power size and a separate analysis would be needed.

## 4. Consequence for the live route

`FD-055` left the interval-length threshold `0.55` as the obvious literature bottleneck. The present calculation separates two different ways of trying to cross it.

An **all-interval** Möbius theorem below exponent `0.55` would feed the existing `FD-048`--`FD-055` mechanism directly. An **almost-all** theorem can replace it only if it also solves the localization problem. For a cardinality-only argument near the critical line, that means an exceptional-set exponent approaching `1`; alternatively one needs source-specific structure showing that the adaptive quotient endpoints avoid the bad set.

So the next useful theorem is not merely

\[
\text{“Möbius cancels on almost all intervals of length }X^{1/2+o(1)}\text{.”}
\]

The needed input is closer to one of the following: local exceptional-density control inside every window of starting points of length `A_X X^{o(1)}`; an avoidance/equidistribution theorem for the reciprocal/floor endpoints generated by nearby nonsquarefree rows; or a truly all-interval estimate in the remaining near-critical length range.

This narrows the external analytic target substantially. The 2026 almost-all theorem has enough **cancellation strength** and enough **interval-length reach** for the false-RH band, but its presently available global exceptional-set localization is too coarse for the adaptive quadratic-transfer problem.

## 5. Prior-art boundary and provenance

The load-bearing external comparison is Theorem 1.1(i) of Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones Mathematicae **244** (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`. Their theorem owns the almost-all Möbius cancellation and the global `X/log^K X` exceptional-set estimate used in (9)--(12).

The quantitative exceptional-set literature already includes Kaisa Matomäki and Maksym Radziwiłł, *Multiplicative functions in short intervals II*, arXiv `2007.04290` (2020), which obtains power-saving exceptional-set bounds in a broad multiplicative-function framework. No novelty is claimed for quantitative almost-all cancellation itself. The new statement here is the source-specific threshold (6) obtained by matching such exceptional budgets against the zero-frontier adaptive transfer corridor created by `FD-046`, `FD-054`, and `FD-055`.

Repository provenance:

- `FD-046` supplies the exact zero-frontier power exponent for the quotient-shell source;
- `FD-054` identifies the additive nonsquarefree-twin transfer and its natural source displacement;
- `FD-055` enlarges that transfer corridor logarithmically using all-short-interval Möbius cancellation;
- the present finding compares the resulting deterministic corridor size against global almost-all exceptional-set budgets.

The result is therefore a route restriction, not a proof of positive nonsquarefree occupation. It rules out a superficially attractive shortcut and replaces it with an explicit quantitative target: **near the critical line, global counting alone needs an exceptional exponent nearly equal to one, or it must be supplemented by structural avoidance of the bad starts.**
