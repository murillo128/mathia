# MC-006 — Averaged two-point Chowla gives only logarithmic global saving through van der Corput

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`.

## Claim

Let `a_1,...,a_X` be complex numbers with `|a_n|<=1`, let

\[
S(X)=\sum_{n\le X}a_n,
\]

and for `1<=h<H<=X` define the truncated additive correlations

\[
C_h(X)=\sum_{n\le X-h}a_{n+h}\overline{a_n}.
\]

A standard van der Corput inequality gives

\[
|S(X)|^2
\ll \frac{X^2}{H}
 +\frac{X}{H}\sum_{1\le h<H}|C_h(X)|.
\tag{1}
\]

Thus, if

\[
R(X,H)=\frac1{HX}\sum_{1\le h<H}|C_h(X)|,
\]

then

\[
\frac{|S(X)|}{X}
\ll H^{-1/2}+R(X,H)^{1/2}.
\tag{2}
\]

This makes the quantitative information requirement of a correlation-to-global route explicit. To deduce a fixed power saving

\[
|S(X)|\ll X^{1-c}
\qquad(c>0)
\tag{3}
\]

from (2), one needs, at the same scale, roughly

\[
H\gg X^{2c}
\qquad\text{and}\qquad
R(X,H)\ll X^{-2c}.
\tag{4}
\]

In particular, an RH-scale target `X^(1/2+delta)` would require a polynomially small averaged correlation budget of scale approximately

\[
H\gg X^{1-2\delta},
\qquad
R(X,H)\ll X^{-1+2\delta},
\tag{5}
\]

unless an argument uses structure beyond the black-box van der Corput transfer.

For the Möbius function, the quantitative averaged Chowla theorem of Matomäki–Radziwiłł–Tao (`MC-S13`) states, in the `k=2` specialization and equally for `mu`, that

\[
\sum_{1\le h\le H}
\left|\sum_{n\le X}\mu(n)\mu(n+h)\right|
\ll
\left(
\frac{\log\log H}{\log H}
+
\frac1{(\log X)^{1/3000}}
\right)HX
\tag{6}
\]

for `10<=H<=X`.

Feeding this theorem into (1) after the harmless truncation audit below and taking `H=floor(sqrt X)` gives the unconditional black-box consequence

\[
|M(X)|
\ll
X\left(
\frac{\log\log X}{\log X}
+
\frac1{(\log X)^{1/3000}}
ight)^{1/2}
+O(X^{3/4}),
\tag{7}
\]

and therefore, in particular,

\[
|M(X)|\ll \frac{X}{(\log X)^{1/6000}}
\tag{8}
\]

for large `X` after adjusting the implicit constant.

This is a genuine local/correlation-to-global transfer, but it is asymptotically much weaker than the classical Korobov–Vinogradov-shaped bound already recorded in `MC-S3`.

The conclusion is not that averaged Chowla information is irrelevant. It is sharper: **the currently proved averaged two-point correlation decay has only logarithmic quantitative strength, and van der Corput takes its square root. A black-box route through this correlation norm therefore cannot approach any fixed power saving, let alone the RH scale, without polynomially stronger correlation information or an additional arithmetic mechanism.**

## 1. Exact correlation-to-sum transfer

Extend `a_n` by zero outside `[1,X]`. Averaging `H` shifted copies and applying Cauchy–Schwarz gives the standard van der Corput estimate

\[
\left|\sum_{n\le X}a_n\right|^2
\ll
\frac{X^2}{H}
+
\frac{X}{H}
\sum_{1\le h<H}
\left|\sum_{n\le X-h}a_{n+h}\overline{a_n}\right|,
\]

which is (1). No multiplicativity or number theory enters this step.

If the average absolute correlation satisfies

\[
\sum_{h<H}|C_h(X)|\le R H X,
\]

then (1) immediately gives

\[
|S(X)|^2\ll X^2(H^{-1}+R),
\]

and hence (2).

The exponents in (4) are therefore forced at this information level. If `H=X^theta` and `R=X^{-rho}`, then the two terms in (2) give at best

\[
|S(X)|\ll X^{1-\min(\theta,\rho)/2}.
\tag{9}
\]

A logarithmic decay `R=(log X)^(-A)` cannot yield `X^(1-c)` for any fixed `c>0`, regardless of how large the fixed logarithmic exponent `A` is.

## 2. Specialization of averaged Chowla to Möbius

`MC-S13`, Theorem 1.1, proves for Liouville and every fixed `k` an averaged shift estimate with quantitative factor

\[
r(X,H)
=
\frac{\log\log H}{\log H}
+
\frac1{(\log X)^{1/3000}}.
\tag{10}
\]

The same paper explicitly states that the argument gives Theorem 1.1 with `lambda` replaced by `mu`. For `k=2`, its stronger anchored form is precisely

\[
\sum_{1\le h\le H}
\left|\widetilde C_h(X)\right|
\ll r(X,H)HX,
\qquad
\widetilde C_h(X)
:=\sum_{n\le X}\mu(n)\mu(n+h).
\tag{11}
\]

Van der Corput uses the truncated correlation

\[
C_h(X)=\sum_{n\le X-h}\mu(n+h)\mu(n).
\]

Since `|mu|<=1`, the difference is supported on at most `h` terminal values, so

\[
|C_h(X)-\widetilde C_h(X)|\le h.
\tag{12}
\]

Summing (12) over `h<H` gives

\[
\sum_{h<H}|C_h(X)|
\ll r(X,H)HX+H^2.
\tag{13}
\]

Substitution into (1) yields

\[
|M(X)|^2
\ll
\frac{X^2}{H}
+r(X,H)X^2
+XH.
\tag{14}
\]

Taking `H=floor(sqrt X)` balances the two elementary boundary terms and gives

\[
|M(X)|
\ll
X\sqrt{r(X,\sqrt X)}+X^{3/4}.
\tag{15}
\]

Because

\[
r(X,\sqrt X)
\ll
\frac{\log\log X}{\log X}
+
(\log X)^{-1/3000},
\]

(7) follows. Asymptotically the very small fixed exponent `1/3000` term dominates the first term, and taking the square root gives (8).

The exact exponent `1/6000` is not important and is not presented as competitive. Its role is to make the information loss explicit: the correlation theorem supplies logarithmic normalized decay, and the generic quadratic transfer can only turn it into another logarithmic decay.

## 3. Why this does not improve the known Mertens bound

`MC-S3` records the unconditional estimate

\[
M(X)
\ll
X\exp\!\left(
-c(\log X)^{3/5}(\log\log X)^{-1/5}
\right),
\tag{16}
\]

which beats every fixed inverse power of `log X`. Therefore (8) is mathematically valid but asymptotically weaker than already-known global cancellation.

This comparison rules out a tempting inference from modern correlation language: the fact that (6) is a quantitatively strong averaged Chowla theorem does not mean that its **stated norm and rate**, used as a black box, contain more global Mertens information than classical zero-free-region machinery.

The authors of `MC-S13` themselves note that their method cannot produce a gain much larger than order `1/log H` in the averaged Chowla estimate. Even an idealized improvement of (10) to `R(X,H)\asymp1/log H` would still feed through (2) as only a square-root logarithmic saving. Reaching (5) would require a qualitatively different quantitative regime, not optimization of the fixed logarithmic exponents in the present theorem.

## 4. What extra information could escape the ceiling

Equation (2) is deliberately a black-box inequality. It discards the signs and phases of the correlations by summing their absolute values. A stronger argument could in principle use information that (1) throws away, including:

- cancellation among the correlations as `h` varies;
- multiplicative relations tying additive shifts to prime-factor decompositions;
- multiscale identities in which the same correlation mass cannot recur independently at every scale;
- a structured signed kernel replacing the absolute-value van der Corput majorant;
- exceptional-shift geometry strong enough to isolate a much smaller dangerous set;
- higher-order correlations that constrain the pair-correlation matrix rather than merely bounding its entrywise `l^1` norm.

But any such route must exhibit the additional datum explicitly. Merely invoking more qualitative Chowla cancellation does not change the rate barrier, and merely improving the logarithmic constant in (6) does not change its polynomial information class.

## Prior art and novelty assessment

Van der Corput's inequality is classical, and the averaged Chowla estimate is the established theorem `MC-S13`. No novelty is claimed for either ingredient or for the general principle that correlation bounds control partial sums.

The durable line-specific contribution is the **quantitative composition audit**: specialize the modern averaged two-point theorem to Möbius, pass it through the exact correlation-to-sum inequality, account for the endpoint mismatch, and compare the resulting information scale with both the RH target and the classical global Mertens bound. A targeted literature search found the averaged Chowla theorem and standard van der Corput correlation inequalities, but no reason to treat this elementary composition as a new theorem of analytic number theory. It is stored as an obstruction and rate budget.

## Boundaries and failure modes

This finding does **not** show that Chowla-type methods cannot contribute to RH. It rules out only a route that retains the averaged absolute two-point correlation norm at its currently proved logarithmic rate and then uses a generic van der Corput transfer.

In particular:

- the proof methods behind `MC-S13` contain more structure than the single scalar bound (6);
- a future theorem with polynomially small averaged correlations over polynomially many shifts would cross a genuinely different threshold;
- signed rather than absolute shift averages can behave much better than the `l^1` norm used here;
- the truncation term `H^2` in (13) is an endpoint bookkeeping cost of composing the exact stated forms, not an intrinsic barrier to all correlation approaches;
- higher correlations may impose positive-semidefinite, rank, or consistency constraints unavailable from pairwise magnitudes alone;
- this result does not model hypothetical off-critical zeros or prove any new pointwise property of the actual Möbius function beyond the weak consequence (8).

The decisive audit test for a continuation is:

> exhibit a correlation observable actually controlled for Möbius whose normalized strength is polynomial in `X`, or prove a signed/structural transfer that converts the existing logarithmic averaged information into a polynomial gain without reintroducing a zero-free region equivalent to the desired conclusion.

## Relation to the obstruction chain

`MC-001` showed that almost-all short-interval magnitude plus exceptional-set measure is too compressed for RH-scale aggregation. `MC-002` showed that one standard pretentious scalar has only `O(log log X)` dynamic range. `MC-003` showed that the natural Möbius/Liouville prime-power enrichment hits the square-root transfer threshold without an independently easier comparator. `MC-004` showed that exact support plus all qualitative fixed-shift Chowla limits still allows near-linear bias when multiplicativity is absent. `MC-005` showed that exact support plus multiplicativity plus qualitative mean cancellation still allows arbitrarily slow logarithmic cancellation.

The present finding addresses the natural next repair: **combine genuinely arithmetic multiplicative input with a quantitative averaged Chowla theorem.** The combination does transfer to an anchored global sum, but the theorem's current rate remains logarithmic, so the resulting global information is still far below a fixed power saving.

This narrows the frontier from "perhaps multiplicativity plus correlations is enough" to a quantitative question: what mechanism can make the interaction carry polynomial information rather than logarithmic information?