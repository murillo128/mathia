# MC-394 — Sub-loglog endpoint rank forces asymptotically full source cost

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `SOURCE-COST` · `STRUCTURAL-OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint/source-package setting of `MC-392` and `MC-393`. For a family of exact endpoints write

\[
P=P(y),
\qquad
A(y):=\frac{\log P}{\log y},
\qquad
R=R(y)\to\infty.
\]

If

\[
R=o(\log\log y),
\tag{1}
\]

then the near-full-rank source-cost theorem of `MC-393` actually closes every **fixed proportional deficit**:

\[
\boxed{
\liminf_{y\to\infty}\frac{\log P}{R\log y}\ge1.
}
\tag{2}
\]

Equivalently, for every fixed `\eta>0`, all sufficiently large members of such a family satisfy

\[
\boxed{
P\ge y^{(1-\eta)R}.
}
\tag{3}
\]

This does **not** assert the pointwise bound `P\ge y^R`, and it does not require a theorem uniform as the cutoff exponent tends to one. The quantifiers are important: one fixes `\eta`, invokes the corresponding fixed-parameter theorem from `MC-393`, and only then lets `y\to\infty`.

There is also a finite-scale refinement behind `(2)`. Fix any `0<\beta<1` for which the `MC-393` analytic condition

\[
2^{C_\beta A}\log\log y=o(\log y)
\tag{4}
\]

holds. Let `W_\beta` be the surviving source-mode subspace after imposing the incidence constraints from source primes `p>y^\beta`, and put

\[
c_\beta:=\operatorname{codim}W_\beta,
\qquad
d_\beta:=\dim W_\beta.
\]

Then, in the nontrivial branch `A\le R`,

\[
\boxed{
A\ge \beta R-O_\beta(\log R).
}
\tag{5}
\]

Thus for each fixed cutoff below the shell scale, the exact endpoint can leave only logarithmically many dimensions unpaid after source codimension and the sparse-exception budget are combined. In the sub-loglog-rank regime `(1)`, condition `(4)` is automatically compatible with every fixed `\beta<1` when `A\le R`; taking fixed `\beta` arbitrarily close to one recovers `(2)` without any moving-`\beta` estimate.

No estimate for `M(x)` and no RH consequence follows.

## 1. The architecture-level bound already implies coefficient one in the sub-loglog regime

`MC-393` proves that for every fixed `\eta\in(0,1)` there is a constant `a_\eta>0` such that, for all sufficiently large exact endpoints in the rank-growing regime,

\[
A(y)
\ge
\min\left\{(1-\eta)R(y),\ a_\eta\log\log y\right\}.
\tag{6}
\]

Fix `\eta>0`. Assumption `(1)` gives

\[
\frac{(1-\eta)R(y)}{a_\eta\log\log y}\to0.
\]

Because `a_\eta` is now a fixed positive constant, the first term in `(6)` is eventually the smaller one. Hence

\[
A(y)\ge(1-\eta)R(y)
\]

for all sufficiently large `y`. Dividing by `R(y)` gives

\[
\liminf_{y\to\infty}\frac{A(y)}{R(y)}\ge1-\eta.
\]

Since this holds for every fixed `\eta>0`, `(2)` follows.

The argument does not exchange limits and does not need any information about how `a_\eta` behaves as `\eta\downarrow0`. This is why it is compatible with the explicit `MC-393` warning that no uniform coefficient-one theorem was proved there.

## 2. Source codimension leaves at most logarithmically many unpaid dimensions

The sharper finite-scale statement `(5)` comes directly from the exact codimension/exception inequality in `MC-392`.

For fixed `\beta<1`, `MC-393` gives

\[
c_\beta\le\frac A\beta,
\qquad
d_\beta\ge R-\frac A\beta.
\tag{7}
\]

It also supplies an exceptional set `B\subset W_\beta\setminus\{0\}` with

\[
|B|\le C_0R
\tag{8}
\]

for a fixed constant `C_0` in this endpoint architecture, while every other nonzero mode has

\[
|g(I)|\le\varepsilon(y),
\qquad
\varepsilon=o(R^{-1/2}).
\tag{9}
\]

Apply `MC-392` with `H_\beta=2^{d_\beta}`. Its exact inequality gives

\[
|B|+1
\ge
\frac{2^{d_\beta}}{2c_\beta+3}
\left(1-R\varepsilon^2\right)^2.
\tag{10}
\]

For sufficiently large `y`, `(9)` makes the last factor at least `1/2`. Combining `(7)`--`(10)` yields

\[
2^{d_\beta}
\le
2(C_0R+1)\left(2A/\beta+3\right).
\tag{11}
\]

Therefore

\[
d_\beta
\le
\log_2\!\left(2(C_0R+1)(2A/\beta+3)\right).
\tag{12}
\]

Using the lower bound for `d_\beta` in `(7)`,

\[
R-\frac A\beta
\le
\log_2\!\left(2(C_0R+1)(2A/\beta+3)\right).
\tag{13}
\]

If `A>R`, `(5)` is trivial. In the only nontrivial branch `A\le R`, the right side of `(13)` is `O_\beta(\log R)`, and rearranging gives `(5)`.

This identifies the exact residual resource after `MC-392`: once the analytic theorem has reduced the exceptional family to `O(R)`, the surviving source frame cannot retain a positive-dimensional fraction of unpaid endpoint modes. At fixed `\beta`, only `O_\beta(\log R)` dimensions can remain.

## 3. Why the analytic ceiling disappears when `R=o(log log y)`

For a fixed `\beta<1`, the moving-depth condition needed by `MC-393` is `(4)`. In the branch `A\le R`, assumption `(1)` gives

\[
A=o(\log\log y).
\]

For fixed `C_\beta`, this alone does not imply `2^{C_\beta A}=o(\log y)` for every arbitrary `A=o(\log\log y)` unless the little-`o` is used quantitatively. Writing

\[
A=\theta(y)\log\log y,
\qquad \theta(y)\to0,
\]

one has

\[
2^{C_\beta A}
=(\log y)^{C_\beta(\log2)\theta(y)}
=(\log y)^{o(1)}.
\]

Hence

\[
2^{C_\beta A}\log\log y=o(\log y),
\]

so `(4)` holds for every fixed `\beta<1`.

Consequently the finite-scale inequality `(5)` is available at every fixed cutoff below one. Dividing `(5)` by `R` and using `R\to\infty` gives

\[
\liminf\frac AR\ge\beta.
\]

Since `\beta<1` was arbitrary but fixed, `(2)` follows again. This second proof makes explicit where the logarithmic residual dimension enters.

## Prior art and novelty boundary

The analytic input is unchanged from `MC-393`. In particular, `MC-S46`, Cochrane--Granville--Zheng, *Mixed incomplete character sums of rational functions with smooth moduli* (arXiv:`2601.10927v1`, 16 January 2026), supplies the smooth-modulus character-sum machinery used there. A fresh source check on 19 September 2026 confirms the arXiv record and its stated smoothness range up to `N^{1-\varepsilon}` for fixed `\varepsilon>0`.

The exceptional-family input and the projected-simplex fourth-moment inequality are exactly the already audited `MC-374` and `MC-392` results. No new external theorem is introduced here. A targeted mechanism-level search for an established theorem coupling this Mathia source-incidence codimension, sparse endpoint exceptions, and sub-loglog rank found no source that changes the classification; absence from that search is not evidence of novelty.

The new delta is an internal quantifier sharpening of `MC-393` plus the explicit residual-dimension inequality `(13)`. Accordingly this finding makes no standalone novelty claim.

## Boundaries and falsification tests

- **The sub-loglog rank hypothesis is load-bearing for `(2)`.** If `R` is comparable to or larger than `\log\log y`, the independent analytic ceiling `a_\eta\log\log y` in `MC-393` may be the smaller term.
- **No uniform cutoff theorem is used.** Both derivations fix `\eta` or `\beta` before taking `y\to\infty`. The constants may deteriorate arbitrarily as the fixed parameter approaches its endpoint.
- **Coefficient one is only a liminf statement.** Nothing here proves `A\ge R`, `P\ge y^R`, or even `A\ge R-O(\log R)` with a parameter-independent implied constant.
- **The `O(R)` exceptional-family theorem is load-bearing for `(5)`.** Replacing it by a much larger exceptional population changes `(11)` and may reopen residual dimension.
- **The projected-simplex quotient is load-bearing.** The fourth-moment inequality from `MC-392` is not a generic theorem for arbitrary character families.
- **The squarefree smooth-source analytic model remains load-bearing.** The result inherits the same conductor and factorization hypotheses as `MC-393`.
- **No Möbius/RH consequence.** This remains an obstruction internal to the exact endpoint/source-package program.

## Consequence for the research line

Below the `\log\log y` rank scale, the rank-side escape left by `MC-393` is now closed asymptotically: an exact endpoint source package must pay essentially one unit of `\log_y P` per endpoint rank. Optimizing a fixed cutoff or improving the constant below one cannot produce a surviving mechanism in this regime.

The remaining resource question is therefore concentrated at the transition where `R` reaches the independent `\log\log y` analytic ceiling, or in mechanisms that violate one of the source-incidence, sparse-exception, projected-simplex, or squarefree-smooth hypotheses. A useful next attack must change that ledger rather than merely seek another fixed proportional improvement.