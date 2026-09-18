# MC-382 — Iterated q-vdC has an intrinsic log-log source horizon

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The `log log y` ceiling that remains in `MC-381` is not merely an artifact of the particular fixed-power block packing used there. It is already built into the **single-character iterated q-van-der-Corput architecture** of Cochrane--Granville--Zheng Proposition 7 when that proposition is closed only with generic square-root cancellation for the terminal complete sum.

More precisely, let an interval have length

\[
N=y^{1+o(1)},
\]

and suppose a primitive squarefree character has conductor

\[
q=y^{a+o(1)}=N^{a+o(1)}
\qquad(a\ge 2).
\tag{1}
\]

Consider a Proposition-7 factorization

\[
q=q_1\cdots q_k Q
\tag{2}
\]

with pairwise coprime factors, where the preliminary factors are used through

\[
M_i=\left\lfloor (N/q_i)^{2/3}\right\rfloor
\tag{3}
\]

and the terminal factor is controlled only through the generic square-root local mechanism that, after the rough-squarefree bookkeeping used in `MC-379`, has the schematic normalized form

\[
E_Q\ll N^{o(1)}
\left(1+\frac{Q\log Q}{N}\right)Q^{-1/2+o(1)}.
\tag{4}
\]

Any **nontrivial black-box use** of this architecture in which every displayed Proposition-7 contribution tends to zero necessarily satisfies

\[
\boxed{k\ge a-2-o(1).}
\tag{5}
\]

Indeed the preliminary terms require `q_i<N` asymptotically, while `(4)` can tend to zero only when

\[
Q\le N^{2+o(1)}.
\tag{6}
\]

Consequently `(2)` gives

\[
q\le N^{k+2+o(1)},
\]

which is `(5)`.

Proposition 7 then raises the terminal estimate to the power `2^{-k}`. Even granting the route the **ideal loss-free square-root terminal estimate**

\[
E_Q\ll Q^{-1/2+o(1)},
\tag{7}
\]

its generic certified power-saving scale after `k` differencing steps is no better, in exponent order, than

\[
\boxed{
\sigma(a)\lesssim 2^{-a+O(1)}.
}
\tag{8}
\]

Thus a frame argument of the type used in `MC-379`--`MC-381`, which needs at least

\[
\sigma(a)\log y\to\infty
\tag{9}
\]

(and in practice needs it to dominate logarithmic rank/Selberg losses), cannot be extended by **repacking the same q-vdC factorization alone** to source exponents

\[
a\gg\log\log y.
\tag{10}
\]

At best such repacking can improve the absolute constant multiplying `log log y`; it cannot change the order of the analytic horizon. Raising the source-cost rate beyond the `log log y` side of `MC-381` therefore requires a genuinely different input: for example a collective estimate that avoids one square-rooting per conductor-scale layer, a terminal estimate substantially stronger than generic square-root cancellation for the actual source family, or another mechanism that does not pass through the Proposition-7 recursion.

This is a **method obstruction**, not a theorem that all character-sum methods have a log-log horizon. It does not prove the `MC-381` lower bound optimal, and it gives no estimate for `M(x)`.

## 1. Proposition 7 charges one square root per preliminary factor

For the normalized incomplete sum `E_q(a)`, Cochrane--Granville--Zheng Proposition 7 writes `q` as in `(2)`, sets `M_i` as in `(3)`, and gives an iterated estimate of the shape

\[
|E_q(a)|
\le
\sum_{i=1}^k O\!\left(M_i^{-2^{-i}}\right)
+
O\!\left(E_Q(a^{(M_1,\ldots,M_k)})^{2^{-k}}\right).
\tag{11}
\]

The important feature here is structural rather than constant-level: after `k` preliminary differencing steps, **every terminal saving is seen through a `2^{-k}` root**.

This is exactly the loss already visible in the explicit specialization used by `MC-379` and `MC-381`, where the terminal rough-squarefree estimate produces

\[
Q^{-1/(4\,2^k)}.
\tag{12}
\]

Changing the greedy block packing can change `k` by constants, but it cannot remove the exponentiation by `2^{-k}` while Proposition 7 remains the engine.

## 2. A polynomial conductor exponent forces linear differencing depth

The lower bound `(5)` is elementary but useful because the previous source-cost findings only needed an **upper** bound `k=O(a)`.

First consider a preliminary factor. If `q_i\ge N`, then `(3)` gives `M_i=0` (or, at the boundary, no growing differencing parameter), so its Proposition-7 contribution cannot provide asymptotic cancellation. Any application in which every preliminary contribution in `(11)` tends to zero must therefore have

\[
q_i<N^{1-o(1)}
\tag{13}
\]

for each `i`; for the weaker counting argument below, `q_i\le N^{1+o(1)}` already suffices.

Now consider the terminal factor. The squarefree terminal calculation in `MC-379`, before imposing `Q<N`, comes from prime-local square-root cancellation and has the schematic dependence `(4)`. If

\[
Q=N^{b+o(1)},
\]

then the large-`Q` part of `(4)` is

\[
N^{o(1)}\frac{Q^{1/2+o(1)}}N
=N^{b/2-1+o(1)}.
\tag{14}
\]

For this black-box terminal bound itself to tend to zero one must have

\[
b\le2+o(1),
\]

which is `(6)`. The stricter `Q<N` choice in `MC-379`--`MC-381` is therefore convenient, but **not responsible for linear depth**: even allowing the terminal block to grow all the way to the edge permitted by generic square-root cancellation only saves two interval-length exponents.

Combining `(2)`, `(6)`, and `q_i\le N^{1+o(1)}` gives

\[
N^{a+o(1)}=q
\le N^{k+2+o(k+1)}.
\tag{15}
\]

In the moving regime relevant here `k=O(a)` and `a=o(\log N)`, so the accumulated `o(1)` terms can be absorbed into `o(a)`. Hence

\[
k\ge a-2-o(a).
\tag{16}
\]

For fixed or slowly moving `a`, this is the stated `(5)` after the usual normalization of the error term. In particular, a conductor occupying `a` interval-length exponents cannot be processed by this recursion in `o(a)` differencing depth.

## 3. Ideal terminal square-root cancellation still leaves exponential loss in `a`

To isolate the architecture rather than constants, grant a stronger terminal input than `MC-379` actually proves: delete all roughness constants, collision factors, logarithms, and local exceptional-prime losses, and suppose simply that

\[
E_Q\ll Q^{-1/2+o(1)}.
\tag{17}
\]

After Proposition 7 this contributes

\[
E_Q^{2^{-k}}
\ll
Q^{-2^{-k-1}+o(2^{-k})}.
\tag{18}
\]

The strongest possible choice compatible with the square-root terminal mechanism has `Q\le N^{2+o(1)}`. Equations `(5)` and `(18)` therefore place the generic terminal power-saving exponent on the scale

\[
2^{-k}
\le
2^{-a+2+o(a)}.
\tag{19}
\]

The preliminary terms cannot repair the fact that the recursion has already accumulated this depth: they are additional positive error terms in `(11)`, and optimizing their sizes only changes where the bottleneck occurs. Thus the **best exponent scale certifiable by the loss-free black-box recursion** is exponential in `-a`, as stated in `(8)`.

This conclusion is deliberately about theorem use, not about the true size of a particular character sum. A special terminal sum may vanish, a specially structured family may admit cancellation beyond square root after averaging, and a different identity may bypass `(11)` entirely. None of those possibilities is excluded.

## 4. Exponential depth loss forces the log-log horizon

Suppose the character estimate delivered to the prime-frame stage has the form

\[
\left|\sum_{n\in J}\chi(n)\right|
\ll |J|\,y^{-\sigma(a)}.
\tag{20}
\]

The `MC-381` frame transfer requires the off-diagonal factor

\[
y^{-c\sigma(a)}\log y
\tag{21}
\]

to be small compared with the rank-scale lower pressure. A necessary condition even before paying that rank pressure is simply

\[
\sigma(a)\log y\to\infty.
\tag{22}
\]

Insert the idealized architecture scale `(8)`. Condition `(22)` can hold only while

\[
2^{-a+O(1)}\log y\to\infty,
\]

or equivalently

\[
a\le \log_2\log y-\omega(1)
\tag{23}
\]

up to constant-level changes caused by a different block convention. Once the actual Selberg/rank losses are restored, one needs a margin such as

\[
2^{C a}\log\log y=o(\log y),
\]

which is the form already appearing in `MC-381`.

Therefore the surviving `log log y` term in

\[
\frac{\log P}{\log y}
\ge c\min\{R,\log\log y\}
\]

has a different status from the old rank-side losses removed by `MC-380`--`MC-381`. The latter came from how many source coordinates were deleted. The former is tied to the **depth-versus-conductor geometry of the iterated q-vdC recursion itself**.

## 5. Prior art and novelty boundary

The analytic engine is prior art: Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026), retained locally as `MC-S46`. Proposition 7 supplies the iterated q-van-der-Corput recursion and its `2^{-k}` terminal exponent. The same manuscript explicitly remarks that its current proof can let the smoothness parameter move only down to order `1/log log q`; this is consistent with the depth audit above and is not a Mathia discovery.

A fresh check on 19 September 2026 found the arXiv record still at version 1. Its introduction states both that the fixed-parameter theorem permits moduli smooth up to `N^{1-epsilon}` and that the current moving-parameter proof requires `delta >> 1/log log q`. The present finding does **not** strengthen their character-sum theorem.

The durable derived point is narrower: after `MC-381` removed the source-incidence `A^2` loss, equations `(5)`--`(23)` identify why merely repacking the same Proposition-7 recursion cannot remove the remaining `log log y` source-cost ceiling. The obstruction follows from three ingredients already present in the method: preliminary factors must fit below the interval, generic square-root terminal cancellation can absorb at most two interval-length exponents, and every preliminary stage halves the terminal saving exponent.

No standalone novelty claim is made for q-van-der-Corput differencing, square-root complete-sum bounds, or the observation that repeated Cauchy--Schwarz takes roots of savings.

## Boundaries and falsification tests

- **This is a method obstruction, not a character-sum lower bound.** It does not say that some character of conductor `y^a` actually has a large interval sum.
- **The terminal hypothesis is explicit.** Equation `(6)` is forced only when the terminal stage is bounded through the generic square-root mechanism `(4)`. A source-family theorem with stronger terminal cancellation could move the boundary.
- **Exceptional exact cancellation is not excluded.** If the actual terminal complete sum is zero or has additional algebraic cancellation, Proposition 7 may perform better than the black-box audit predicts for that character.
- **Collective estimates are outside the obstruction.** A frame/large-sieve theorem controlling the whole selected source family without applying `(11)` separately to every pair could avoid the one-root-per-layer tariff. `MC-302` shows that the ordinary all-quadratic large-sieve envelope has a different energy bottleneck, but that does not rule out a thinner source-family estimate.
- **The constant is not optimized.** Allowing `Q` close to `N^2`, changing the preliminary block sizes, or improving rough-squarefree constants can alter the coefficient of `log log y`; `(10)` concerns the asymptotic order.
- **The conclusion is local to the current endpoint/source-cost program.** No implication for `M(x)`, RH, arbitrary smooth-modulus character sums, or other Mathia research lines is asserted.

## Research consequence

The next useful attack on the analytic side should not spend another cycle optimizing greedy block sizes inside Proposition 7. To beat the `log log y` source horizon one must change at least one of the load-bearing mechanisms above: avoid linear differencing depth, avoid the `2^{-k}` root cascade, obtain source-family terminal cancellation beyond the generic square-root envelope, or move to a collective theorem that never reduces each pair independently through the same recursion.