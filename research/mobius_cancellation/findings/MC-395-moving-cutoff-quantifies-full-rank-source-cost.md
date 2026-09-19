# MC-395 — Moving cutoff quantifies the full-rank source-cost deficit

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint/source-package setting of `MC-374`, `MC-379`, `MC-392`, `MC-393`, and `MC-394`. Write

\[
P=P(y),
\qquad
A(y):=\frac{\log P}{\log y},
\qquad
R=R(y)\to\infty,
\qquad
L:=\log\log y.
\]

The fixed-cutoff quantifier argument in `MC-394` can be made quantitative by returning to the explicit differencing inequality of Cochrane--Granville--Zheng rather than treating the shell-power cutoff as fixed.

There is an absolute constant `C>0` such that every exact endpoint source package in the regime

\[
R=o(L)
\tag{1}
\]

satisfies, for all sufficiently large `y`,

\[
\boxed{
A
\ge
R-C\left(\frac{R^2}{L}+\log(R+2)\right).
}
\tag{2}
\]

Thus the coefficient-one conclusion of `MC-394` has an explicit deficit scale. In particular,

\[
R-A
=O\!\left(\frac{R^2}{\log\log y}+\log R\right).
\tag{3}
\]

When `R^2/(\log\log y)=o(\log R)`, this becomes the near-pointwise architecture bound

\[
A\ge R-O(\log R).
\tag{4}
\]

No estimate for `M(x)` and no RH consequence follows.

The underlying moving-cutoff statement is useful independently of the optimized form. Let

\[
0<\delta\le\frac14,
\qquad
\beta:=1-\delta,
\]

and assume a trial source bound `P\le y^A`. There is an absolute `C_0>0` such that if

\[
\boxed{
2^{C_0A/\delta}
\bigl(\log\log y+\log(R+2)\bigr)
=o(\delta\log y),
}
\tag{5}
\]

then the surviving source-mode subspace after imposing the incidence constraints from source primes `p>y^\beta` has

\[
c_\delta:=\operatorname{codim}W_\delta
\le\frac{A}{1-\delta},
\qquad
d_\delta:=\dim W_\delta
\ge R-\frac{A}{1-\delta},
\tag{6}
\]

and all but `O(R)` of its nonzero modes obey

\[
|g(I)|=o(R^{-1/2}).
\tag{7}
\]

Consequently `MC-392` forces

\[
\boxed{
d_\delta\le 2\log_2 R+O(1)}
\tag{8}
\]

whenever `A<R` and `(5)` holds. Equation `(2)` is obtained by choosing the gap `\delta` from the hypothetical source-cost deficit rather than fixing it in advance.

## 1. A moving shell-power cutoff costs `A/(1-delta)` dimensions

Assume `P\le y^A`. Impose the parity constraints

\[
\langle I,c_p\rangle=0
\]

for every source prime

\[
p>y^{1-\delta}.
\]

Each such prime contributes more than `(1-\delta)\log y` to `\log P`, so their number is at most `A/(1-\delta)`. Therefore `(6)` is exact source-cost bookkeeping and uses no character-sum estimate.

Fix now a nonzero surviving mode whose minimum primitive source conductor is greater than `y`. As in `MC-374`, only `O(R)` endpoint modes fail this condition. Let `q` be the canonical primitive squarefree conductor of a good mode. Then

\[
y<q\mid P,
\qquad
P^+(q)\le y^{1-\delta}.
\tag{9}
\]

The point is to derive the good-mode estimate uniformly while `\delta` tends to zero.

## 2. The explicit Proposition 7 inequality is uniform enough for a moving gap

Return to Proposition 7 of Cochrane--Granville--Zheng (`MC-S46`), rather than invoking their fixed-parameter Theorem 1. If

\[
q=q_1\cdots q_kQ
\]

with pairwise-coprime factors and

\[
M_j=\left\lfloor(N/q_j)^{2/3}\right\rfloor,
\]

their inequality is explicitly

\[
|\mathbf E_q(a)|
\le
4\sum_{j=1}^k M_j^{-2^{-j}}
+4\,\mathbf E_Q(a(M_1,\ldots,M_k))^{2^{-k}}.
\tag{10}
\]

This is the load-bearing uniform statement. The familiar `kN^{-\epsilon/2^k}` form of their Corollary 11 is an immediate consequence of `(10)`; no fixed-`\epsilon` theorem constant is needed here.

Choose a roughness threshold

\[
T:=2^{K A/\delta}
\tag{11}
\]

with a sufficiently large absolute `K`, and split

\[
q=S q_r,
\qquad
S:=\prod_{\substack{p\mid q\\p\le T}}p.
\tag{12}
\]

The standard Chebyshev bound for the product of primes up to `T`, together with `(5)`, gives

\[
\log S=o(\delta\log y),
\qquad
q_r>y^{1-o(\delta)}.
\tag{13}
\]

Every prime factor of `q_r` lies in

\[
T<p\le y^{1-\delta}.
\]

Greedily pack those prime factors into blocks capped at

\[
y^{1-\delta/2}.
\]

Whenever a new prime would cross the cap, the completed block is larger than

\[
y^{\delta/2}.
\tag{14}
\]

Hence there are at most

\[
\frac{2A}{\delta}+O(1)
\tag{15}
\]

completed blocks. Use one completed block as the terminal factor `Q`; if `q_r` itself never crosses the cap, take `Q=q_r`. Put the remaining blocks, the final remainder, and `S` when nontrivial among the preliminary factors. Thus one obtains a factorization with

\[
\boxed{
k\le C_1 A/\delta,}
\tag{16}
\]

all preliminary factors at most `y^{1-\delta/2}` apart from the much smaller factor `S`, and a rough squarefree terminal factor satisfying

\[
\boxed{Q\ge y^{\delta/2},
\qquad P^-(Q)>T.}
\tag{17}
\]

Condition `(5)` in particular implies `\delta\log y\gg\log\log y`. For every shell interval occurring in the Selberg/Bombieri transfer below, the interval length is therefore large enough that all preliminary factors in this construction are bounded by `N^{1-\delta/4}`.

## 3. Rough terminal cancellation loses only `2^{O(A/delta)}`

The squarefree terminal calculation of `MC-379` is uniform in the differencing depth once every terminal prime exceeds a sufficiently large exponential function of that depth. Because `(11)` was chosen with `K` large relative to `(16)`, the same local estimates give

\[
\mathbf E_Q
\ll Q^{-1/4}.
\tag{18}
\]

Apply `(10)`. Since every preliminary factor is at most `N^{1-\delta/4}`, one has

\[
M_j\gg N^{\delta/6},
\]

while `(17)` gives the corresponding terminal decay. After absorbing the harmless factor `k`, there are absolute constants `c,C_2>0` such that

\[
\boxed{
\left|\frac1N\sum_{n\in J}\chi_q(n)\right|
\ll y^{-\sigma_{A,\delta}},
\qquad
\sigma_{A,\delta}
\ge
c\delta\,2^{-C_2A/\delta}.
}
\tag{19}
\]

This is the moving-gap version of `MC-393`'s fixed-`\beta` saving. Its cost has a transparent origin: `(15)` requires `O(A/\delta)` differencing stages, and Proposition 7 takes a `2^{-k}` root after those stages.

Transfer `(19)` through the same Selberg-sieve/Bombieri prime-shell argument already audited in `MC-379` and `MC-393`. Taking the Selberg cutoff exponent proportional to `\sigma_{A,\delta}` leaves the factorization admissible because `\sigma_{A,\delta}\ll\delta`. One gets

\[
|g(I)|
\ll
 y^{-c'\sigma_{A,\delta}}\log y
\tag{20}
\]

for every good surviving endpoint difference. Condition `(5)` says precisely, after enlarging `C_0`, that the exponent in `(20)` dominates both the sieve logarithm and the `R^{-1/2}` target. Therefore `(7)` follows.

The other nonzero surviving modes form the same `O(R)` low-conductor exceptional family already isolated in `MC-374`; no larger exceptional set is introduced by the moving cutoff.

## 4. Codimension feedback leaves only logarithmically many unpaid dimensions

Apply `MC-392` on `W_\delta`. Let `B` be the `O(R)` exceptional family from the previous section and let

\[
H_\delta=2^{d_\delta}.
\]

Its exact codimension/exception inequality gives

\[
|B|+1
\ge
\frac{H_\delta}{2c_\delta+3}
\left(1-R\varepsilon^2\right)^2,
\tag{21}
\]

where `\varepsilon=o(R^{-1/2})` by `(7)`. In the only nontrivial branch `A<R`, equation `(6)` gives `c_\delta=O(R)`. Since `|B|=O(R)`, `(21)` implies

\[
2^{d_\delta}=O(R^2),
\]

and hence `(8)`.

This is the quantitative feedback that a fixed `\beta` cannot exploit. Once the good-mode estimate is made uniform in the moving gap, the source cutoff may approach the shell scale until the `2^{O(A/\delta)}` analytic tariff becomes comparable with `\log y`.

## 5. Optimizing the moving gap proves `(2)`

Assume `(1)`. By `MC-394`, eventually `A\ge R/2`; otherwise its already proved coefficient-one liminf statement gives a contradiction. Thus it remains only to consider

\[
0<D:=R-A\le R/2.
\tag{22}
\]

Choose

\[
\delta:=\frac{D}{2R},
\qquad
\beta=1-\delta.
\tag{23}
\]

Then

\[
R-\frac{A}{1-\delta}
=
\frac{RD}{2R-D}
\ge\frac D2,
\tag{24}
\]

so `(6)` gives

\[
d_\delta\ge D/2.
\tag{25}
\]

Also

\[
\frac{A}{\delta}
\le\frac{2R^2}{D}.
\tag{26}
\]

Suppose, toward contradiction, that for a sufficiently large absolute `K`,

\[
D
\ge
K\left(\frac{R^2}{L}+\log(R+2)\right).
\tag{27}
\]

The first term in `(27)` and `(26)` give

\[
A/\delta\le 2L/K.
\]

Choosing `K` large relative to the absolute constant in `(5)` makes

\[
2^{C_0A/\delta}\le (\log y)^{1/4}
\tag{28}
\]

for all sufficiently large `y`. The second term in `(27)` gives

\[
\delta\ge \frac{K\log(R+2)}{2R}.
\tag{29}
\]

Since `R=o(L)`, one has `\log(1/\delta)=o(L)`. Combining `(28)`--`(29)` shows that the left side of `(5)` is `(\log y)^{1/4+o(1)}`, while `\delta\log y=(\log y)^{1-o(1)}`. Thus `(5)` holds.

Equation `(8)` now gives

\[
d_\delta\le2\log_2R+O(1),
\]

whereas `(25)` and `(27)` give `d_\delta\ge D/2` with `D` larger than any sufficiently large fixed multiple of `\log R`. This is impossible. Therefore `(27)` cannot occur, proving `(2)`--`(3)`.

The optimization is intentionally coarse. Constants in `(2)` are not optimized because the important new information is the deficit scale `R^2/(\log\log y)+\log R`, not its leading coefficient.

## Prior art and novelty boundary

The external analytic input is unchanged: `MC-S46`, Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026). A fresh source check on 19 September 2026 confirms that their Proposition 7 states the explicit iterated inequality `(10)` with `M_j=\lfloor(N/q_j)^{2/3}\rfloor`; Corollary 11 records the resulting `kN^{-\epsilon/2^k}` loss when every preliminary factor is at most `N^{1-\epsilon}`. Their main Theorem 1 is stated for fixed positive parameters, so the moving-`\delta` argument above deliberately returns to Proposition 7 rather than substituting a vanishing parameter into a fixed-parameter theorem.

The rough squarefree terminal estimate `(18)`, the prime-shell transfer, and the low-conductor `O(R)` exceptional family are already established and prior-art audited in `MC-374`, `MC-379`, and `MC-393`. The codimension feedback `(21)` is exactly `MC-392`.

A targeted mechanism-level search on 19 September 2026 for moving smoothness gaps in incomplete character sums and quantitative source-incidence/codimension feedback found the Cochrane--Granville--Zheng differencing machinery above but no external theorem that supplies `(2)` as a named result. That absence is not evidence of novelty. No novelty is claimed for Proposition 7, rough squarefree cancellation, prime sieves, or the elementary optimization. The Mathia-specific delta is their explicit moving-gap composition with the endpoint source-cost and codimension constraints.

## Boundaries and falsification tests

- **The sub-loglog rank regime is load-bearing for `(2)`.** When `R` is comparable with `\log\log y`, the error term `R^2/(\log\log y)` is already of order `R` and the optimized conclusion gives no coefficient-one information.
- **The proof must use Proposition 7 directly.** Substituting `\delta(y)` into a theorem whose constants were proved only for fixed smoothness parameters would be invalid. Equation `(10)` is used precisely to avoid that mistake.
- **Squarefree canonical source conductors remain load-bearing.** The terminal estimate `(18)` uses the source-specific squarefree specialization from `MC-379`.
- **The roughness threshold moves exponentially in `A/\delta`.** Condition `(5)` pays for the small-prime factor `S` as well as the `2^{-k}` differencing loss. Dropping that cost would produce a false stronger rate.
- **The `O(R)` low-conductor exceptional theorem is load-bearing.** A substantially larger exceptional family changes `(21)` and the logarithmic residual dimension in `(8)`.
- **No exact coefficient-one pointwise bound is proved.** Equation `(2)` leaves a quantitative deficit, and nothing here implies `P\ge y^R`.
- **No new character-sum theorem is claimed.** The analytic inequalities are a source-specific repacking of the already cited literature plus `MC-379`'s audited terminal specialization.
- **No Möbius/RH consequence.** The result is an internal source-cost obstruction for the exact endpoint architecture.

## Consequence for the research line

`MC-394` closed every fixed proportional source-cost deficit below the `\log\log y` rank scale but deliberately gave no rate because its cutoff parameter was fixed before `y\to\infty`. The explicit Proposition 7 bookkeeping shows that the cutoff can instead move toward one at a controlled price. The remaining unpaid endpoint rank is at most

\[
O\!\left(\frac{R^2}{\log\log y}+\log R\right).
\]

This leaves a sharper transition boundary. Improving the sub-loglog regime further now requires either beating the `2^{-k}` loss inherent in the present differencing chain, reducing the `O(A/\delta)` number of source blocks, or finding a source relation whose cost is not paid one distinct large prime at a time. Merely choosing a cutoff closer to the shell scale no longer creates an unquantified escape.