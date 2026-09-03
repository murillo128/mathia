# MC-041 — quantitative logarithmic Chowla still needs a Tauberian bridge before van der Corput

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `RECENT-PREPRINT-DEPENDENCY`, `NO-NOVELTY-CLAIM`.

## Claim

A recent quantitative logarithmic Chowla theorem supplies substantially stronger harmonic correlation control than the qualitative fixed-shift results audited in `MC-039`–`MC-040`, including uniformity over growing shift ranges. However, the displayed logarithmically weighted bounds do **not** enter the ordinary van der Corput inequality at the same quantitative strength without an additional Tauberian mechanism.

For a bounded sequence `b_n`, write

\[
H_b(y)=\sum_{n\le y}\frac{b_n}{n},
\qquad
B_b(X)=\sum_{n\le X}b_n.
\]

Exact discrete summation by parts gives

\[
\boxed{
B_b(X)=XH_b(X)-\sum_{m=1}^{X-1}H_b(m).
}
\tag{1}
\]

Consequently a magnitude bound

\[
\sup_{y\le X}|H_b(y)|\le E(X)
\tag{2}
\]

implies only

\[
|B_b(X)|\le (2X-1)E(X).
\tag{3}
\]

Thus a power-of-log saving in a harmonic correlation primitive transfers black-box to at most a power-of-log saving in the corresponding ordinary correlation. It does not become a fixed power of `X` merely by removing the weight.

This loss is sharp at the information level of `(2)`: there are explicit `{-1,+1}` sequences whose harmonic prefixes remain uniformly bounded while their ordinary partial sums are linear along a subsequence, and such a sequence can be realized exactly as a fixed-lag autocorrelation `a_n a_{n+h}` of another `{-1,+1}` sequence.

When the quantitative tail bound from Guo (`MC-S29`, Theorem 1.3) is nevertheless composed carefully with `(1)` and the ordinary van der Corput transfer from `MC-006`, it yields, for the Liouville function and every fixed `B>0`, a black-box consequence of the shape

\[
\sum_{n\le X}\lambda(n)\ll_B \frac{X}{(\log X)^B},
\tag{4}
\]

but still no fixed power saving. This consequence is asymptotically weaker than the classical Korobov–Vinogradov-shaped Liouville bound already recorded in `MC-S8`.

The durable obstruction is therefore precise: **quantitative logarithmic Chowla over growing shifts is not yet a polynomial global-cancellation budget when only its harmonic-prefix magnitudes are retained. A route to a power saving must exploit additional arithmetic/scale structure or a genuinely stronger Tauberian input, rather than treating logarithmic correlations as ordinary correlations with the weight harmlessly removed.**

## 1. Exact harmonic-to-ordinary conversion

Let `X` be a positive integer. Since

\[
b_n=n\left(\frac{b_n}{n}\right),
\]

discrete Abel summation gives

\[
\sum_{n=1}^{X} b_n
=
X\sum_{n=1}^{X}\frac{b_n}{n}
-
\sum_{m=1}^{X-1}\sum_{n=1}^{m}\frac{b_n}{n},
\]

which is exactly `(1)`.

No number theory enters this identity. Taking absolute values immediately yields `(3)`.

The point is not that logarithmic averages are weak in general. It is that the map

\[
H_b(\cdot)\longmapsto B_b(X)
\]

contains an `X`-sized boundary/accumulation factor unless one controls the signed combination in `(1)` more finely than by `\sup|H_b|`. If `E(X)=(\log X)^{-A}`, then `(3)` gives only

\[
B_b(X)\ll X(\log X)^{-A}.
\tag{5}
\]

If one wants `B_b(X)\ll X^{1-c}`, a black-box estimate of this form would require harmonic-prefix size `E(X)\ll X^{-c}`, not merely arbitrarily large fixed logarithmic savings.

This is the exact Tauberian bottleneck relevant to correlation transfer: van der Corput in `MC-006` needs ordinary additive correlations, whereas logarithmic Chowla controls a different summability method.

## 2. Bounded harmonic prefixes can coexist with linear ordinary sums

Define the dyadic block sequence

\[
d_n=(-1)^k
\qquad\text{for}\qquad
2^k\le n<2^{k+1}.
\tag{6}
\]

The harmonic mass of the `k`-th block is

\[
\sum_{n=2^k}^{2^{k+1}-1}\frac1n
=
\log 2+O(2^{-k}).
\tag{7}
\]

Therefore the completed-block contributions to

\[
H_d(X)=\sum_{n\le X}\frac{d_n}{n}
\]

form an alternating series with asymptotically constant block sizes and summable block errors. Inside a single unfinished block the additional harmonic mass is at most `\log 2+O(2^{-k})`. Hence

\[
\boxed{\sup_X |H_d(X)|<\infty.}
\tag{8}
\]

In contrast, at

\[
N_K=2^{K+1}-1
\]

the ordinary sum is exact:

\[
\sum_{n\le N_K}d_n
=
\sum_{k=0}^{K}(-1)^k2^k
=
\frac{1-(-2)^{K+1}}{3}.
\tag{9}
\]

Thus

\[
\left|\sum_{n\le N_K}d_n\right|
\asymp N_K.
\tag{10}
\]

So even the much stronger condition `H_d(X)=O(1)` does not imply `B_d(X)=o(X)` for an arbitrary bounded sequence. This is an explicit obstruction, not merely a warning about the loss in the triangle inequality in `(3)`.

### Autocorrelation realization

The same obstruction can be embedded in the exact shape of a fixed-shift two-point correlation. Fix `h>=1`. Choose arbitrary initial values

\[
a_1,\ldots,a_h\in\{-1,+1\}
\]

and recursively set

\[
a_{n+h}=a_n d_n.
\tag{11}
\]

Then every `a_n` lies in `{-1,+1}` and

\[
\boxed{a_n a_{n+h}=d_n}
\tag{12}
\]

for every `n>=1`. Therefore

\[
\sup_X\left|\sum_{n\le X}\frac{a_na_{n+h}}n\right|<\infty,
\tag{13}
\]

while the unweighted lag-`h` correlation has linear-size values along the same dyadic endpoints.

This does **not** produce a multiplicative comparator to Möbius or Liouville. Its role is narrower and exact: no theorem whose only retained hypothesis is a per-shift magnitude bound on the logarithmic correlation can unweight that correlation to a power-saving ordinary bound. Any arithmetic escape must use structure discarded by that scalar hypothesis.

## 3. Audit of the recent quantitative logarithmic theorem

Guo (`MC-S29`) proves quantitative logarithmically weighted two-point Liouville correlation estimates with growing-shift uniformity. Two parts are especially relevant here.

First, Theorem 1.6 supplies an absolute `c>0` such that, for every fixed `A>0`, uniformly for

\[
1\le h\le (\log X)^A,
\]

one has a fixed power-of-log saving for

\[
\sum_{n\le X}\frac{\lambda(n)\lambda(n+h)}n.
\]

Second, Theorem 1.3 gives a stronger maximal statement on polynomial shift windows. Fix `theta>1/3`, `1<p<infinity`, and put `Q>=X^theta`. In the specialization relevant here, its refined tail estimate gives, for every fixed `A>0`,

\[
\left(
\frac1Q\sum_{h\le Q}
\sup_{y\le X}
\left|
\sum_{Q<n\le y}
\frac{\lambda(n)\lambda(n+h)}n
\right|^p
\right)^{1/p}
\ll_{A,p,\theta}(\log X)^{-A}.
\tag{14}
\]

The exact quantifiers and theorem remain literature evidence from a very recent preprint; this finding does not independently re-prove Guo's analytic argument.

Let

\[
u_{n,h}=\lambda(n)\lambda(n+h)\mathbf 1_{n>Q},
\qquad
U_h(y)=\sum_{n\le y}\frac{u_{n,h}}n.
\]

Applying `(1)` to `u_{n,h}` gives

\[
\left|\sum_{Q<n\le X}\lambda(n)\lambda(n+h)\right|
\le
2X\sup_{y\le X}|U_h(y)|.
\tag{15}
\]

Average `(15)` over `h<=Q` and use Hölder together with `(14)`. The initial segment `n<=Q` contributes trivially `O(Q)`, so for the anchored ordinary correlations

\[
\widetilde C_h(X)=\sum_{n\le X}\lambda(n)\lambda(n+h)
\]

we obtain

\[
\frac1Q\sum_{h\le Q}|\widetilde C_h(X)|
\ll
Q+X(\log X)^{-A}.
\tag{16}
\]

Van der Corput uses the truncated correlations

\[
C_h(X)=\sum_{n\le X-h}\lambda(n+h)\lambda(n).
\]

The endpoint difference satisfies

\[
|C_h(X)-\widetilde C_h(X)|\le h,
\]

so averaging over `h<=Q` changes `(16)` only by another `O(Q)` term. Consequently the normalized average correlation from `MC-006` obeys

\[
R(X,Q)
:=
\frac1{QX}\sum_{h<Q}|C_h(X)|
\ll
\frac QX+(\log X)^{-A}.
\tag{17}
\]

Insert `(17)` into the exact van der Corput budget of `MC-006`:

\[
\frac{|L(X)|}{X}
\ll
Q^{-1/2}+R(X,Q)^{1/2},
\qquad
L(X)=\sum_{n\le X}\lambda(n).
\tag{18}
\]

Taking `Q=X^{1/2}` is admissible because `1/2>1/3`, and gives

\[
\frac{|L(X)|}{X}
\ll
X^{-1/4}+ (\log X)^{-A/2}.
\tag{19}
\]

Since Theorem 1.3 allows an arbitrarily fixed `A`, for every fixed `B>0` choose `A=2B` and obtain `(4)` after enlarging constants.

This is genuine quantitative transfer from a modern growing-shift logarithmic correlation theorem into an ordinary global sum. But its information class remains logarithmic: for every fixed `B`,

\[
\frac{X}{(\log X)^B}
\gg X^{1-c}
\]

for every fixed `c>0` and all sufficiently large `X`. Moreover `MC-S8` already records a classical Korobov–Vinogradov-shaped unconditional bound for `L(X)` that is asymptotically smaller than every `X/(\log X)^B`.

Accordingly `(4)` is not presented as a competitive Liouville estimate. It is an audit of what the **displayed harmonic correlation norm plus black-box unweighting plus van der Corput** actually contains.

## 4. Why this does not transfer a new Möbius exponent

`MC-S29` is a theorem about Liouville correlations. The present calculation does not replace `lambda` by `mu` without a theorem authorizing that specialization.

More importantly, even a strong global Liouville estimate does not automatically bootstrap Möbius to a better exponent. `MC-003` audited the exact square-divisor convolution connecting `mu` and `lambda` and the Jung–Lemke Oliver power-cancellation transfer. The natural transfer threshold sits at exponent `beta>1/2`; the known Liouville input does not provide an independently easier fixed power-saving route that would lower the Möbius exponent.

Thus the recent logarithmic-correlation theorem is valuable here as a **strong comparator and information-budget stress test**, not as a hidden new Mertens theorem.

## 5. Prior art and novelty assessment

The conceptual distinction between logarithmic and ordinary summability is classical Tauberian territory. `MC-S30` is one historical anchor for logarithmic summability and the need for side conditions in converses. Equation `(1)` is elementary Abel summation, and no novelty is claimed for it.

Guo's growing-shift quantitative logarithmic Chowla estimates are recent external prior art (`MC-S29`). The dyadic sequence `(6)` is an elementary explicit counterexample tailored to this line's information audit; the recursion `(11)` embeds the same no-go into a genuine fixed-lag autocorrelation. No claim is made that this example is new in summability theory.

The durable line-specific contribution is the composition audit:

1. identify exactly the Tauberian map between harmonic and ordinary correlations;
2. show by an explicit autocorrelation realization that magnitude-only harmonic control can lose essentially all ordinary cancellation;
3. feed the strongest relevant growing-shift harmonic estimate through that map and the already-audited van der Corput budget;
4. locate the surviving logarithmic ceiling without mistaking modern logarithmic Chowla language for a polynomial Mertens information budget.

## 6. Boundaries and falsification controls

This finding rules out only a specific information quotient. It does **not** show that logarithmic-correlation methods cannot contribute to RH or to power cancellation.

In particular:

- `MC-S29` may contain simultaneous multi-shift, maximal, exceptional-set, or proof-internal structure stronger than the single scalar consequence `(14)` retained here.
- An arithmetic Tauberian theorem with side conditions independently verified for Möbius/Liouville could beat the generic identity-plus-triangle-inequality transfer.
- Cancellation among the harmonic primitives `H_h(y)` as `h` or `y` varies is discarded by `(15)`.
- A signed shift kernel, bilinear decomposition, multiplicative coupling, or positivity/rank constraint could use information that average absolute values erase.
- The dyadic autocorrelation realization is not multiplicative and therefore cannot falsify a theorem whose genuinely used hypotheses include multiplicativity or another Möbius-specific arithmetic constraint.
- The recent Guo theorem is treated as literature evidence pending ordinary independent source audit; only the Abel identity and counterexample are independently derived here.
- No new pointwise estimate for the true Mertens function is established.

A continuation therefore survives only by naming the extra datum explicitly. The decisive test is to prove either:

\[
\text{quantitative logarithmic correlation structure + independently weaker arithmetic side condition}
\Longrightarrow
\text{polynomial ordinary-correlation gain},
\]

or a direct global cancellation theorem that uses the joint logarithmic structure without first scalarizing it into per-shift harmonic magnitudes. A matched multiplicative control satisfying the proposed side conditions but retaining near-linear ordinary correlations would kill that candidate.

## Consequence for the research line

`MC-006` showed that the 2015 averaged ordinary two-point Chowla theorem, used through entrywise absolute correlations, carries only logarithmic global saving. `MC-039` and `MC-040` then showed that increasingly rich **qualitative logarithmic** correlation hierarchies can coexist with near-linear multiplicative bias in explicit exact-support controls.

`MC-041` closes the next obvious escape: even a modern **quantitative**, growing-shift logarithmic theorem does not automatically cross into a polynomial information class when the harmonic weights are removed by a generic Tauberian step. Its stated tail strength can be propagated through van der Corput to arbitrarily large fixed logarithmic savings, but not to a fixed power of `X`.

The live correlation frontier is therefore narrower. Further work should target a joint signed/multiscale arithmetic mechanism that either controls the Tauberian boundary combination in `(1)` directly or bypasses ordinary per-shift correlations altogether. Merely strengthening the fixed power of `log X` in a scalar harmonic-correlation estimate does not address the polynomial Mertens budget.