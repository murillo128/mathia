# MC-371 — Defect imbalance does not evade the quartic source floor

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `DECISIVE-NEGATIVE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The quartic common-source lower bound of `MC-324` and the half-loaded source-mass stability of `MC-327` do **not** require equal endpoint defect cells. They survive for every exact endpoint partition.

Continue the exact endpoint partition of `MC-296`:

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R,
\qquad
 d_i:=\frac{|D_i|}{|\mathcal R_y|}>0,
\qquad
\sum_{i=1}^R d_i=1,
\tag{1}
\]

with independent shell functionals `\lambda_1,\ldots,\lambda_R`. For `I\subseteq[R]`, `MC-296` gives the complete selected Fourier profile

\[
 x_{\lambda_I}
 =(-1)^{|I|}\bigl(1-2d(I)\bigr),
\qquad
 d(I):=\sum_{i\in I}d_i.
\tag{2}
\]

Choose arbitrary fixed lower-prime product representatives `V_i` for the generators and put

\[
U:=\bigcup_iV_i,
\qquad
P:=\prod_{p\in U}p,
\qquad
m_{ij}:=\prod_{p\in V_i\triangle V_j}p.
\tag{3}
\]

For a source prime `p\in U`, write

\[
a_p:=\#\{i:p\in V_i\},
\qquad
\nu_p:=\frac{\log p}{\log P},
\tag{4}
\]

and retain the logarithmically weighted source-imbalance energy from `MC-327`,

\[
\mathcal B_R
:=
\sum_{p\in U}\nu_p
\left(\frac{2a_p-R}{R}\right)^2.
\tag{5}
\]

Then for every fixed `\delta\in(0,2)`, as `R\to\infty`,

\[
\boxed{
(1-\mathcal B_R)\frac{\log P}{\log y}
\ge
(4-2\delta)
\left(1-\frac{15}{R}+O(R^{-2})\right)
-O_\delta(R^{-2}).
}
\tag{6}
\]

Consequently every admissible exact endpoint sequence satisfies

\[
\boxed{
\liminf_{y\to\infty}
(1-\mathcal B_R)\frac{\log P}{\log y}
\ge4,
}
\tag{7}
\]

and therefore in particular

\[
\boxed{
\liminf_{y\to\infty}\frac{\log P}{\log y}\ge4.
}
\tag{8}
\]

No balance assumption on the defect masses `d_i` appears in `(6)`--`(8)`.

If the package saturates the quartic floor,

\[
\frac{\log P}{\log y}=4+o(1),
\tag{9}
\]

then `(7)` forces

\[
\boxed{\mathcal B_R\to0.}
\tag{10}
\]

Thus the main near-equality conclusion of `MC-327` is also defect-agnostic: a quartic-cost package must place asymptotically all logarithmic source mass on incidence columns with loading `R/2+o(R)`.

The mechanism is simple but decisive. Although the individual endpoint cells may be very unequal, only `O(1)` of them can carry macroscopic mass. Hence **all but `O(R)` pair modes still have fixed prime-shell bias**. The varying-modulus prime Halász--Montgomery theorem already audited in `MC-323` then makes almost all of those pair modes individually expensive. The weighted Plotkin double count from `MC-324` converts that pairwise bill into the same quartic total-source bill.

This removes equal defect mass as a possible escape from the quartic source obstruction. It does **not** prove the `L^2` defect-cell balance required by the finite-resolution theorem `MC-370`; source-incidence balance and endpoint defect-mass balance remain distinct currencies. No estimate for `M(x)` follows.

## 1. Almost every generator is strongly biased without equal cells

For a singleton `I={i}`, equation `(2)` gives

\[
x_{\lambda_i}=2d_i-1.
\tag{11}
\]

Let

\[
H_1:=\{i:d_i>1/4\}.
\]

Because the positive `d_i` sum to one,

\[
|H_1|\le3.
\tag{12}
\]

For every `i\notin H_1`,

\[
|x_{\lambda_i}|
=1-2d_i
\ge\frac12.
\tag{13}
\]

Apply the varying-modulus prime Halász--Montgomery consequence `(8)` of `MC-323` with threshold `\tau=1/2`. For every fixed `\delta>0`, only `O_\delta(1)` distinct primitive cubefree source characters of conductor at most `y^{2-\delta}` can have shell bias at least `1/2`. Therefore

\[
\boxed{
\#\left\{i:\mathcal Q(\lambda_i)\le y^{2-\delta}\right\}
=O_\delta(1),
}
\tag{14}
\]

up to the harmless absolute contribution of the at most three indices in `H_1`.

So the near-quadratic generator-conductor saturation from `MC-323` was never essentially tied to equal defects. An exact partition by itself already makes all but finitely many generator modes macroscopically biased.

## 2. All but linearly many pair modes are strongly biased

For a pair `I={i,j}`, equation `(2)` gives

\[
\boxed{
x_{\lambda_i+\lambda_j}=1-2(d_i+d_j).}
\tag{15}
\]

Define

\[
H_2:=\{i:d_i>1/8\}.
\]

Again `sum_i d_i=1` implies

\[
|H_2|\le7.
\tag{16}
\]

If `i,j\notin H_2`, then

\[
d_i+d_j\le\frac14,
\]

so

\[
\boxed{x_{\lambda_i+\lambda_j}\ge\frac12.}
\tag{17}
\]

Hence at least

\[
\binom{R-7}{2}
\tag{18}
\]

pair modes have fixed bias at least `1/2`, irrespective of how the remaining defect mass is distributed.

Distinct unordered pairs give distinct nonzero functionals because the `\lambda_i` are independent. Applying `MC-323` to this pair family shows that, for every fixed `\delta>0`, all but `E_\delta=O_\delta(1)` of the pairs counted in `(18)` have minimum primitive source conductor exceeding `y^{2-\delta}`. Since the symmetric-difference package representative satisfies

\[
\mathcal Q(\lambda_i+\lambda_j)\le m_{ij},
\]

we obtain

\[
\boxed{
m_{ij}>y^{2-\delta}}
\tag{19}
\]

for at least

\[
\binom{R-7}{2}-E_\delta
\tag{20}
\]

unordered pairs.

The loss from arbitrary defect imbalance is therefore only `O(R)` pairs out of `\Theta(R^2)`. This is asymptotically negligible for the source-capacity argument.

## 3. Weighted Plotkin counting recovers the quartic floor

The source-incidence identity from `MC-324` is purely combinatorial and does not involve the defect masses:

\[
\sum_{1\le i<j\le R}\log m_{ij}
=
\sum_{p\in U}a_p(R-a_p)\log p.
\tag{21}
\]

Using

\[
a_p(R-a_p)
=\frac{R^2}{4}
\left[
1-\left(\frac{2a_p-R}{R}\right)^2
\right]
\]

gives the exact refinement from `MC-327`,

\[
\boxed{
\sum_{i<j}\log m_{ij}
=
\frac{R^2}{4}(1-\mathcal B_R)\log P.
}
\tag{22}
\]

On the other hand, `(19)`--`(20)` give

\[
\sum_{i<j}\log m_{ij}
\ge
\left(\binom{R-7}{2}-E_\delta\right)
(2-\delta)\log y.
\tag{23}
\]

Combining `(22)` and `(23)`,

\[
(1-\mathcal B_R)\frac{\log P}{\log y}
\ge
\frac{4(2-\delta)}{R^2}
\left(\binom{R-7}{2}-E_\delta\right).
\tag{24}
\]

Since

\[
\binom{R-7}{2}
=\frac{R^2-15R+56}{2},
\]

this is exactly `(6)`. Taking `liminf` for fixed `\delta` and then letting `\delta\downarrow0` proves `(7)`, while `0\le\mathcal B_R\le1` gives `(8)`.

If `(9)` holds, `(7)` and `\mathcal B_R\ge0` imply `(10)` immediately.

Thus the equal-cell assumption in `MC-324` and `MC-327` was stronger than needed for the asymptotic quartic source obstruction. The source floor is driven by the abundance of pair modes whose defect-mass sum stays away from `1/2`, and an exact probability partition necessarily supplies quadratically many such pairs.

## 4. Natural source-scale and near-equality corollaries also survive

If the package has `n=|U|` source primes and

\[
Z:=\max U\le y^{(1+o(1))/R},
\tag{25}
\]

then

\[
P\le Z^n.
\]

Together with `(8)`, this gives

\[
\boxed{n\ge(4-o(1))R.}
\tag{26}
\]

So the four-source-coordinates-per-rank barrier from `MC-324` is also independent of endpoint defect balance.

Under quartic saturation `(9)`, `\mathcal B_R\to0` implies

\[
\sum_{p\in U}\nu_p
\left|\frac{a_p}{R}-\frac12\right|
=o(1)
\tag{27}
\]

by Cauchy--Schwarz. Therefore

\[
\frac1R\sum_{i=1}^R\log m_i
=
\sum_{p\in U}\frac{a_p}{R}\log p
=\left(\frac12+o(1)\right)\log P
=(2+o(1))\log y,
\tag{28}
\]

where `m_i=prod_{p in V_i}p`.

Combining this average with `(14)` shows that for every fixed `\epsilon>0`,

\[
\boxed{
\frac1R
\#\left\{i:
\left|\frac{\log m_i}{\log y}-2\right|>\epsilon
\right\}
\longrightarrow0.
}
\tag{29}
\]

Likewise, `(22)` and `(9)`--`(10)` give

\[
\binom R2^{-1}
\sum_{i<j}\log m_{ij}
=(2+o(1))\log y.
\tag{30}
\]

The `O(R)` pair modes involving `H_2` have zero density, while every other pair outside `O_\delta(1)` exceptions has the lower bound `(19)`. Hence for every fixed `\epsilon>0`,

\[
\boxed{
\binom R2^{-1}
\#\left\{\{i,j\}:
\left|\frac{\log m_{ij}}{\log y}-2\right|>\epsilon
\right\}
\longrightarrow0.
}
\tag{31}
\]

Thus the double near-equality picture of `MC-327` survives as well: quartic total cost forces half-loaded source columns and near-quadratic generator/pair package costs in density, even when the endpoint defect cells themselves are highly nonuniform.

## 5. Prior art and novelty boundary

The analytic input is not new here. The varying-modulus prime Halász--Montgomery estimate is Jan-Christoph Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143--149, Theorem 3, DOI `10.4064/aa106-2-4`, already audited and normalized in `MC-323`. The primary publication page was rechecked for this finding.

The pair-distance upper bound is the classical Plotkin column-count mechanism already used in `MC-324`--`MC-327`; equation `(22)` is their exact weighted defect identity. The new combinatorial observation is only the elementary heavy/light consequence of `sum_i d_i=1`: at most seven cells can exceed mass `1/8`, so quadratically many pairs automatically retain fixed character bias. A targeted prior-art check on weighted Plotkin bounds, unequal coordinate weights, and pairwise character-bias families did not identify a standalone theorem matching this endpoint-specific composition.

**No standalone novelty claim is made.** The durable delta is the removal of an unnecessary hypothesis from the live Mathia endpoint obstruction: equal endpoint defects are not needed for the quartic source floor or its source-incidence stability consequences.

## Boundaries and falsification tests

- **Exact endpoint partition remains load-bearing.** Equation `(2)` uses the disjoint-cover profile from `MC-296`. Overlapping defect sets require the correction terms of `MC-297`; this finding does not suppress them.
- **Growing rank.** The asymptotic conclusion assumes `R\to\infty`. The constants `3` and `7` are chosen only to produce the fixed bias threshold `1/2`; they are not claimed optimal.
- **Primitive versus package conductors.** `MC-323` constrains minimum primitive cubefree source conductors. The transfer to `m_i` and `m_{ij}` uses only that every fixed package representative is at least as large as the corresponding minimum representative.
- **The Puchta range is unchanged.** The threshold `y^{2-\delta}` comes from the already-audited varying-modulus theorem. No stronger conductor range is smuggled into the heavy/light argument.
- **Source incidence is not defect-cell balance.** `\mathcal B_R\to0` controls how lower source primes are distributed across generator representatives. It does not imply
  \[
  \left\|d-R^{-1}\mathbf1\right\|_2\to0,
  \]
  let alone the stronger `MC-370` scale `O(1/(R\sqrt{\log R}))`. Any bridge between those quantities must be proved arithmetically.
- **Exact-real side channel remains live.** Even a near-balanced defect distribution can encode all source phases through the raw scalar shell bias by `MC-368`. This theorem does not provide the canonical finite-resolution quotient required by `MC-369`--`MC-370`.
- **No Mertens consequence.** The result strengthens the endpoint source obstruction only; it does not bound `M(x)` or establish a zero-free half-plane.

## Consequence for the research line

Defect imbalance is no longer a plausible escape from the quartic source-cost barrier. Any exact endpoint partition produces enough strongly biased generator and pair characters for the prime Halász--Montgomery family bound to force the same `P\ge y^{4-o(1)}` common-source cost. If that cost is saturated, the source package must again be asymptotically half loaded and its generator/pair representatives must sit near quadratic conductor in density.

This also clarifies the post-`MC-370` frontier. The newly isolated `L^2` cell-balance condition for finite-resolution stability is **not** a hidden consequence of the source-cost argument: the latter now holds for arbitrarily imbalanced defect masses. The next useful arithmetic step must therefore control the actual defect distribution or justify canonical resolution directly, rather than hoping that quartic source saturation itself supplies the `MC-370` balance tariff.