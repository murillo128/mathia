# MC-002 — Prime-harmonic ceiling for single-scale pretentiousness

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`.

## Claim

For multiplicative functions `f,g` with values in the closed unit disk, the standard pretentious distance at scale `x` is

\[
\mathbb D(f,g;x)^2
=
\sum_{p\le x}\frac{1-\operatorname{Re}(f(p)\overline{g(p)})}{p}.
\]

Because each summand is at most `2/p`, one has the universal prime-harmonic ceiling

\[
\mathbb D(f,g;x)^2
\le 2\sum_{p\le x}\frac1p
=2\log\log x+O(1).
\tag{1}
\]

In particular, for the Halász parameter

\[
\mathcal M(f;x,T)
=
\min_{|t|\le T}\mathbb D(f,n^{it};x)^2,
\]

one always has

\[
\mathcal M(f;x,T)\le 2\log\log x+O(1).
\tag{2}
\]

Therefore a **single-scale black-box Halász estimate whose cancellation input is only** `M = M(f;x,T)` cannot by itself certify any polynomial saving

\[
\left|\sum_{n\le x}f(n)\right|=O(x^{1-c})
\qquad(c>0).
\tag{3}
\]

Indeed, the standard Halász term `(1+M)e^{-M}` could be `O(x^{-c})` only if

\[
M\ge c\log x-O(\log\log x),
\tag{4}
\]

which contradicts (2). Truncated versions carrying an additional `1/T` term are no stronger at this information level; in the commonly quoted range `1<=T<=log x`, that term alone is only logarithmically small.

For Möbius the limitation is visible even without minimizing over twists. Since `mu(p)=-1` for every prime,

\[
\mathbb D(\mu,1;x)^2
=
2\sum_{p\le x}\frac1p
=
2\log\log x+2B_1+o(1).
\tag{5}
\]

The Hall–Tenenbaum real-valued mean-value bound recorded in `MC-S5`,

\[
\left|\sum_{n\le x}f(n)\right|
\ll
x\exp\!\left(-\tau\mathbb D(f,1;x)^2\right),
\qquad \tau=0.3286\ldots,
\]

therefore specializes to only

\[
|M(x)|
\ll
x(\log x)^{-2\tau+o(1)}
=
x(\log x)^{-0.6572\ldots+o(1)}.
\tag{6}
\]

This is asymptotically much weaker than the unconditional Korobov–Vinogradov-shaped bound already recorded in `MC-S3`, and enormously weaker than the RH target `x^{1/2+epsilon}`.

The obstruction is thus structural: **standard single-scale pretentious distance contains only `Theta(log log x)` total prime-harmonic mass, whereas a Halász exponential would need `Theta(log x)` distance to yield a polynomial global saving.** Any RH-relevant use of pretentious ideas must introduce additional information beyond that one scalar distance.

## Exact derivation of the ceiling

For every prime `p`, `|f(p)|<=1` and `|g(p)|<=1`, hence

\[
\operatorname{Re}(f(p)\overline{g(p)})
\ge -|f(p)\overline{g(p)}|
\ge -1.
\]

Therefore

\[
0\le 1-\operatorname{Re}(f(p)\overline{g(p)})\le 2,
\]

and summing with weight `1/p` gives

\[
\mathbb D(f,g;x)^2\le 2\sum_{p\le x}\frac1p.
\]

Mertens' second theorem (`MC-S6`) gives the last equality in (1). Since a minimum is no larger than any admissible value, (2) follows immediately for every `T>=0`.

Now let

\[
F(M)=(1+M)e^{-M}.
\]

For `M>=0`, `F` is decreasing. If a deduction from the Halász term alone were to prove normalized polynomial cancellation `F(M)=O(x^{-c})`, then taking logarithms gives

\[
M-\log(1+M)\ge c\log x-O(1),
\]

hence (4). But (2) is `O(log log x)`, so this is impossible for every fixed `c>0` once `x` is large.

This argument concerns the **information content of the standard scalar pretentious parameter inside the generic theorem**, not the actual size of the summatory function. A crude upper bound may of course exceed the true value by an arbitrarily large factor.

## Möbius specialization and comparison

For `f=mu` and `g=1`, every prime contributes exactly `2/p`, giving (5) without any unproved arithmetic input beyond the reciprocal-prime asymptotic.

Substituting (5) into the real-valued Hall–Tenenbaum estimate from `MC-S5` yields

\[
\exp(-\tau\mathbb D(\mu,1;x)^2)
=(\log x)^{-2\tau+o(1)},
\]

which proves (6).

By contrast, `MC-S3` records the unconditional estimate

\[
M(x)
\ll
x\exp\!\left(
-c(\log x)^{3/5}(\log\log x)^{-1/5}
\right).
\]

Its saving beats every fixed power of `1/log x`. Thus even classical zeta zero-free-region machinery already extracts substantially more global Möbius cancellation than the generic one-distance mean-value bound.

This comparison is useful because it prevents a false research direction: merely proving that Möbius is "very non-pretentious" in the standard `1/p` metric cannot close the RH gap. That metric has no room to grow to the scale required by the generic exponential transfer.

## Prior art and novelty assessment

The pretentious distance, Halász mean-value bounds, Hall–Tenenbaum specialization, and reciprocal-prime asymptotic are all established prior art (`MC-S4`–`MC-S6`). No novelty is claimed for any of those ingredients or for inequality (1).

The durable contribution of this finding is the **line-specific quantitative no-go audit** obtained by putting their scales together: the standard single-scale pretentious parameter has an intrinsic `O(log log x)` mass ceiling, so feeding it through the usual Halász exponential cannot produce the `x^{-c}` normalized saving needed for any RH-scale route.

The modern literature explicitly uses pretentious distance as an effective scalar controller for mean values and records sharp examples for closely related real-valued bounds. The literature search did not justify elevating this scale comparison to a new theorem in multiplicative number theory; it is stored only as an obstruction that narrows what a Möbius-cancellation mechanism must add.

## Boundaries and failure modes

This finding does **not** rule out pretentious number theory as a component of an RH attack. It rules out only routes whose decisive quantitative input is a single standard prime-harmonic distance at one scale and whose global saving is obtained through the generic Halász-type dependence on that scalar.

It does not exclude:

- proof-level uses of Halász identities combined with zero-density, bilinear, or correlation information;
- genuinely multiscale observables that retain additional relations between scales rather than merely re-summing the same `1/p` mass;
- richer distances or energies whose total available mass grows like `log x` or faster;
- arithmetic information specific to Möbius, square-free support, prime-factor decompositions, or exceptional-set geometry not encoded in `D`;
- arguments where pretentiousness is only a classification step and the polynomial gain comes from a separate theorem.

One must also not misread (2) as a lower bound on `M`. For Möbius, proving a large lower bound on the minimizing distance can still be useful for qualitative or logarithmic cancellation; the point is that **even the maximum scale permitted by the metric is too small for polynomial cancellation through the generic exponential transfer**.

## Relation to MC-001

`MC-001` showed that almost-all short-interval magnitude plus exceptional-set measure has an insufficient information budget for RH-scale aggregation. `MC-002` identifies an independent bottleneck in the pretentious route: the standard scalar distance itself has only logarithmic-logarithmic dynamic range.

Together they eliminate two natural black-box strategies:

1. aggregate strong local bounds while discarding signed/coherent window structure;
2. convert stronger and stronger single-scale non-pretentiousness directly through Halász's generic mean-value bound.

The common lesson is not merely that existing estimates are quantitatively weak. In both cases the **summary statistic being retained is structurally too compressed** to carry the polynomial-strength information required by the target.

## Consequences for the line

Future pretentiousness-based candidates should be required to answer one precise question before substantial investment:

> What additional datum, beyond the single number `D(f,n^{it};x)^2`, accumulates enough independent arithmetic information to overcome the `O(log log x)` prime-harmonic ceiling?

Promising answers would have to involve genuinely additional structure — for example correlations across scales, bilinear prime-factor interactions, exceptional-set organization, or another quantity whose effective information budget is not bounded by `sum_{p<=x}1/p`.

A proposed bootstrap that merely recomputes or strengthens the same standard distance at nested scales should be audited for double-counting: the disjoint prime-harmonic increments across all scales still total only `O(log log x)`.