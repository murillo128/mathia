# MC-001 — Local-to-global exceptional-mass barrier

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`.

## Claim

Let `a_n` be any complex sequence with `|a_n| <= 1`. For integers `X >= 1` and `1 <= H <= X/2`, define

\[
S_H(x)=\sum_{x<n\le x+H} a_n
\]

for real `x`, and let

\[
T(X)=\sum_{X<n\le 2X} a_n.
\]

Suppose there is a measurable exceptional set `E subset [X,2X-H]` of measure `B` such that

\[
|S_H(x)|\le \eta H
\]

for every `x` outside `E`. Then

\[
|T(X)|\le \eta X+B+2H.
\tag{1}
\]

Consequently, a black-box local-to-global argument that retains only a relative short-interval bound `eta`, exceptional-set measure `B`, and trivial boundedness cannot certify an RH-scale dyadic estimate `T(X)=O(X^{1/2+delta})` unless its error budget is polynomially strong at approximately

\[
\eta X+B+H=O(X^{1/2+\delta}).
\tag{2}
\]

For Möbius, the 2026 almost-all short-interval theorem in `MC-S2`, specialized to the trivial nilsequence, gives for every fixed `A>0`

\[
|S_H(x)|\ll H(\log X)^{-A}
\]

outside a set of measure `B \ll X(\log X)^{-A}` when `X^{1/3+epsilon} <= H <= X^{1-epsilon}`. Choosing an integer `H asymp X^{1/3+epsilon}` with fixed `0<epsilon<1/6` and inserting these two theorem outputs into (1) yields only

\[
|M(2X)-M(X)|
\ll_A \frac{X}{(\log X)^A}+X^{1/3+\epsilon}.
\tag{3}
\]

Thus the currently available almost-all theorem, used only through local magnitude plus exceptional-set size, does **not** approach square-root cancellation. In fact, for every fixed `A`, (3) is asymptotically weaker than the classical Korobov–Vinogradov global bound recorded in `MC-S3`.

## Exact transfer derivation

Integrate the moving short sum over starting points:

\[
I=\int_X^{2X-H} S_H(x)\,dx.
\]

Interchanging the finite sum and integral gives

\[
I=\sum_{X<n\le 2X} w_n a_n,
\]

where

\[
w_n=\operatorname{meas}([X,2X-H]\cap[n-H,n)).
\]

For terms at distance at least `H` from both dyadic endpoints, `w_n=H`; only at most `2H` endpoint terms have smaller weights, and always `0 <= w_n <= H`. Therefore

\[
\left|HT(X)-I\right|
\le \sum_{X<n\le 2X}(H-w_n)|a_n|
\le 2H^2.
\]

On the other hand, trivial boundedness gives `|S_H(x)| <= H` everywhere, so

\[
|I|
\le \int_{[X,2X-H]\setminus E}\eta H\,dx
   +\int_E H\,dx
\le \eta HX+HB.
\]

Divide by `H` and combine the two estimates to obtain (1).

For the Möbius specialization, take the constant polynomial phase / trivial nilsequence in `MC-S2`. Its maximal short-sum estimate is stronger than the ordinary `S_H(x)` estimate needed here. Because `H` may be chosen integral, the theorem's real-`x` exceptional-set measure is directly compatible with the integral argument above.

## What the obstruction actually says

The obstacle is not merely that exceptional intervals exist. Even if `B=0`, a local estimate of relative strength only `eta=(log X)^(-A)` feeds through the triangle inequality as `eta X`, still far above `X^(1/2+delta)` for every fixed `A` and `delta<1/2`. Conversely, even extremely small typical-window sums do not suffice if the exceptional measure remains much larger than the target global scale.

So an RH-relevant local route needs **additional polynomial-strength information** somewhere: much smaller typical-window magnitude, a polynomially smaller exceptional set, or structure that permits cancellation between windows instead of discarding their signs by absolute values.

The `B` dependence is unavoidable at this information level. For general bounded sequences one can place a coherent nonzero block on a set of length `L`; only windows intersecting that block are exceptional, while the global sum contributed by the block is of order `L`. This control is deliberately non-multiplicative: it establishes only that exceptional-set measure cannot be ignored by a generic transfer theorem.

## Prior art and novelty assessment

The moving-window identity underlying (1) is elementary averaging/convolution; **no novelty is claimed for it**. `MC-S1` and `MC-S2` supply the established short-interval Möbius theory, while `MC-S3` supplies the classical global comparison scale.

The useful derived result here is the explicit information-budget audit: inserting the present almost-all theorem parameters into the exact transfer inequality shows that the theorem statement, treated as a black box, can recover at best logarithmic global saving and is not competitive with the existing unconditional global bound. This sharply separates "very strong local pseudorandomness" from the quantitatively different information required for RH-scale global cancellation.

A targeted literature search found the local theorems and their applications to Chowla/uniformity, but no basis for upgrading this elementary transfer audit to a new theorem of analytic number theory. The finding is therefore stored as a line-specific obstruction, not as a novelty claim.

## Boundaries and failure modes

This finding does **not** show that Matomäki–Radziwiłł-type methods are incapable of contributing to RH. It rules out only a black-box aggregation that keeps local magnitudes and exceptional-set measure while forgetting the signs, correlations, multiplicative structure, and proof-level organization of the windows.

In particular:

- correlations between overlapping short sums could make the signed integral much smaller than its absolute-value bound;
- multiplicativity may constrain exceptional windows in ways absent from arbitrary bounded sequences;
- a multiscale argument may use more information than one fixed-`H` theorem statement;
- smoothing can improve endpoint bookkeeping, but it does not by itself remove the `eta X` or `B` terms;
- the exceptional-set witness above is not multiplicative and must not be presented as a Möbius counterexample.

The decisive audit test for any proposed local-to-global improvement is therefore: **identify the exact extra datum beyond `(eta,B,H)` that prevents the triangle-inequality loss in (1), and prove a polynomial gain from that datum.**

## Consequences for the line

The next useful Möbius-cancellation mechanisms should not merely seek stronger qualitative "almost all" cancellation. They should target one of three quantitatively distinct upgrades:

1. polynomial-strength decay of typical short sums;
2. polynomial control of exceptional mass at a compatible scale; or
3. a provable signed/coherent relation among windows that bypasses the absolute-value transfer.

This provides a concrete filter for short-interval, Chowla, Gowers-uniformity, and pretentiousness inputs before investing in a global bootstrap.