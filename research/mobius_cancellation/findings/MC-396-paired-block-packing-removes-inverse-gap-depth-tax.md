# MC-396 — Paired block packing removes the inverse-gap differencing tax

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint/source-package setting of `MC-374`, `MC-379`, `MC-392`, and `MC-395`. Write

\[
P=P(y),
\qquad
A:=\frac{\log P}{\log y},
\qquad
R=R(y)\to\infty,
\qquad
L:=\log\log y.
\]

The `A/\delta` differencing depth in the moving-cutoff argument of `MC-395` is not intrinsic. It comes from bounding **each** greedily closed conductor block below by only `y^{\delta/2}`. Pairing consecutive greedy blocks instead shows that their number is `O(A)` uniformly as the smoothness gap `\delta\downarrow0`.

More precisely, there is an absolute constant `C_0>0` such that the following holds. Let

\[
0<\delta\le\frac14,
\qquad
\beta=1-\delta,
\]

and assume the trial source bound `P\le y^A`. If

\[
\boxed{
2^{C_0A}
\bigl(L+\log(R+2)\bigr)
=o(\delta\log y),
}
\tag{1}
\]

then the surviving source-mode subspace obtained by imposing the incidence constraints from source primes `p>y^{1-\delta}` has

\[
c_\delta:=\operatorname{codim}W_\delta
\le\frac{A}{1-\delta},
\qquad
d_\delta:=\dim W_\delta
\ge R-\frac{A}{1-\delta},
\tag{2}
\]

and all but `O(R)` nonzero modes obey

\[
|g(I)|=o(R^{-1/2}).
\tag{3}
\]

Consequently, in the branch `A<R`, the exact codimension/exception inequality of `MC-392` again forces

\[
\boxed{d_\delta\le2\log_2R+O(1).}
\tag{4}
\]

The gain over `MC-395` is the replacement

\[
2^{O(A/\delta)}
\quad\longrightarrow\quad
2^{O(A)}
\]

in the analytic tariff. The gap `\delta` remains in the final power-saving exponent, but it no longer multiplies the number of differencing stages.

This closes the previous `R^2/L` source-cost deficit throughout the whole sub-loglog range:

\[
\boxed{
R=o(L)
\quad\Longrightarrow\quad
A\ge R-O(\log(R+2)).
}
\tag{5}
\]

Moreover, there is an absolute `\kappa_0>0` such that the same conclusion holds under the strictly larger regime

\[
\boxed{R\le\kappa_0L.}
\tag{6}
\]

Thus the near-pointwise source-cost barrier now reaches a fixed positive fraction of the `R\asymp\log\log y` transition rather than stopping at `R=o(\log\log y)`.

No estimate for `M(x)` and no RH consequence follows.

## 1. Consecutive greedy blocks have a uniform paired mass

Fix a nonzero surviving mode whose minimum primitive source conductor exceeds `y`; as in `MC-374`, only `O(R)` endpoint modes fail this condition. Let `q` be its canonical primitive squarefree source conductor. Then

\[
y<q\mid P,
\qquad
P^+(q)\le y^{1-\delta}.
\tag{7}
\]

Choose a roughness threshold

\[
T:=2^{KA}
\tag{8}
\]

with `K` a sufficiently large absolute constant, and split

\[
q=S q_r,
\qquad
S:=\prod_{\substack{p\mid q\\p\le T}}p.
\tag{9}
\]

By the standard Chebyshev bound for the primorial and `(1)`, after enlarging `C_0` if necessary,

\[
\log S=o(\delta\log y),
\qquad
q_r>y^{1-o(\delta)}.
\tag{10}
\]

Every prime factor of `q_r` therefore lies in

\[
T<p\le y^{1-\delta}.
\]

Set the block cap

\[
B:=y^{1-\delta/2}.
\tag{11}
\]

Run the ordinary next-fit greedy packing on the prime factors of `q_r`: multiply factors into the current block while the product stays at most `B`; when the next prime would exceed `B`, close the current block and start the next one with that prime. Write the resulting block products as

\[
B_1,\ldots,B_m.
\]

Each block satisfies `B_j\le B`. More importantly, whenever `j<m`, the first prime in `B_{j+1}` did not fit in `B_j`, so

\[
\boxed{B_jB_{j+1}>B.}
\tag{12}
\]

Pairing `(B_1,B_2),(B_3,B_4),\ldots` and using `q_r\le q\le y^A` gives

\[
B^{\lfloor m/2\rfloor}<q_r\le y^A.
\]

Hence

\[
\boxed{
m\le \frac{2A}{1-\delta/2}+1\le3A+1.}
\tag{13}
\]

This is the missing bookkeeping improvement. The earlier lower bound `B_j>y^{\delta/2}` for every closed block is true but unnecessarily weak for counting blocks: although one block can be tiny, two consecutive blocks cannot both be tiny.

Condition `(10)` and `\delta>0` give `q_r>B` for sufficiently large `y`, so `m\ge2`. By `(12)`, one of the first two blocks is larger than `B^{1/2}`. Choose such a block as the terminal factor `Q`. Then

\[
\boxed{
y^{1/2-\delta/4}<Q\le y^{1-\delta/2},
\qquad P^-(Q)>T.}
\tag{14}
\]

Use all remaining `B_j` and `S` when nontrivial as preliminary factors. Thus

\[
q=q_1\cdots q_kQ
\]

with pairwise-coprime factors,

\[
\boxed{k\le3A+1,}
\tag{15}
\]

and every non-small preliminary factor at most `y^{1-\delta/2}`.

The combinatorial observation `(12)` is the standard phenomenon behind the classical Next-Fit bin-packing bound: two consecutive bins have combined load exceeding one bin capacity. The present proof is self-contained and uses only that elementary property.

## 2. The rough terminal estimate now pays only `2^{O(A)}` stages

The rough squarefree terminal calculation of `MC-379` applies once every prime divisor of `Q` is sufficiently large compared with the differencing depth. Because `(15)` gives `k=O(A)`, the threshold `(8)` can be chosen so that the local complete-sum constant and collision factor are absorbed uniformly, giving

\[
\mathbf E_Q\ll Q^{-1/4}.
\tag{16}
\]

For the shell intervals used in the Selberg/Bombieri transfer, `(10)` gives interval length

\[
N\ge y^{1-o(\delta)}.
\]

Every preliminary block from `(11)` is therefore at most `N^{1-c\delta}` for some absolute `c>0` and all sufficiently large `y`; the small factor `S` is much smaller. Returning to Proposition 7 of Cochrane--Granville--Zheng (`MC-S46`), with

\[
M_j=\left\lfloor(N/q_j)^{2/3}\right\rfloor,
\]

gives

\[
M_j\ge N^{c'\delta}
\]

for an absolute `c'>0`. Since `k=O(A)`, every preliminary differencing term is bounded by a power with exponent at least

\[
c\delta\,2^{-C A}.
\]

The terminal contribution from `(14)` and `(16)` is at least as strong after the same `2^{-k}` root. Absorbing the `O(A)`-term sum into the exponent yields absolute `c,C>0` such that

\[
\boxed{
\left|\frac1N\sum_{n\in J}\chi_q(n)\right|
\ll y^{-\sigma_{A,\delta}},
\qquad
\sigma_{A,\delta}\ge c\delta\,2^{-CA}.
}
\tag{17}
\]

Compare this with `MC-395`, where the crude block count gave `\sigma\ge c\delta 2^{-C A/\delta}`.

Transfer `(17)` through the same already-audited Selberg-sieve/Bombieri prime-shell argument of `MC-379`, `MC-393`, and `MC-395`. Taking the sieve cutoff exponent proportional to `\sigma_{A,\delta}` gives

\[
|g(I)|\ll y^{-c'\sigma_{A,\delta}}\log y
\tag{18}
\]

for every good surviving endpoint difference. Condition `(1)` makes the exponent in `(18)` dominate the sieve logarithm and the `R^{-1/2}` target, proving `(3)`.

The only excluded nonzero modes are the same `O(R)` low-conductor family from `MC-374`. No new exceptional family is introduced by the paired packing.

## 3. Codimension feedback is unchanged

The source-incidence bookkeeping does not change. Each source prime above `y^{1-\delta}` costs more than `(1-\delta)\log y` in `\log P`, hence `(2)`.

Apply `MC-392` to `W_\delta`. Its exact fourth-moment/codimension inequality gives, with `B` the `O(R)` exceptional family,

\[
|B|+1
\ge
\frac{2^{d_\delta}}{2c_\delta+3}
\left(1-R\varepsilon^2\right)^2,
\qquad
\varepsilon=o(R^{-1/2}).
\tag{19}
\]

In the nontrivial branch `A<R`, equation `(2)` gives `c_\delta=O(R)`. Since `|B|=O(R)`, equation `(19)` implies

\[
2^{d_\delta}=O(R^2),
\]

which is `(4)`.

Thus the combinatorial improvement in Section 1 propagates directly to source cost: the endpoint geometry and exceptional-set argument need no modification.

## 4. The full sub-loglog regime now has only logarithmic unpaid rank

Assume first

\[
R=o(L).
\tag{20}
\]

If `A<R/2`, take `\delta=1/4`. Then `A=o(L)`, so

\[
2^{C_0A}=(\log y)^{o(1)},
\]

and `(1)` holds. But `(2)` gives

\[
d_\delta\ge R-\frac{4A}{3}>\frac R3,
\]

contradicting `(4)` for large `R`. Hence eventually `A\ge R/2`.

Put

\[
D:=R-A,
\qquad 0<D\le R/2.
\]

If `D` is already `O(\log R)`, there is nothing to prove. Otherwise choose

\[
\delta:=\frac{D}{2R}\le\frac14.
\tag{21}
\]

Then

\[
d_\delta
\ge
R-\frac{A}{1-\delta}
=
\frac{RD}{2R-D}
\ge\frac D2.
\tag{22}
\]

Because `A\le R=o(L)`, the factor `2^{C_0A}` in `(1)` is `(\log y)^{o(1)}`. If `D\gg\log(R+2)`, then

\[
\delta\ge\frac{D}{2R},
\qquad
\log(1/\delta)=O(\log R)=o(L),
\]

so the right side `\delta\log y` is `(\log y)^{1-o(1)}` while the left side of `(1)` is `(\log y)^{o(1)}`. Hence `(1)` holds. Equations `(4)` and `(22)` now contradict `D\gg\log R`.

Therefore

\[
D=O(\log(R+2)),
\]

which proves `(5)`.

This strictly improves the `MC-395` deficit

\[
O\!\left(\frac{R^2}{L}+\log R\right)
\]

throughout the range where `R^2/L` is larger than `\log R`.

## 5. The same logarithmic deficit reaches a fixed fraction of loglog scale

The previous proof uses `R=o(L)` only to ensure that `2^{C_0A}` is a sufficiently small power of `\log y`. Therefore choose an absolute `\kappa_0>0` small enough that

\[
C_0(\log2)\kappa_0<\frac14.
\tag{23}
\]

If

\[
R\le\kappa_0L,
\]

then throughout the nontrivial branch `A<R`,

\[
2^{C_0A}\le(\log y)^{1/4}.
\]

The fixed-gap argument `\delta=1/4` again rules out `A<R/2`. For `A\ge R/2`, if `D\gg\log R`, the choice `(21)` has

\[
\log(1/\delta)=O(\log R)=O(\log L)=o(L),
\]

so `(1)` again holds with a large power margin. Equations `(4)` and `(22)` force `D=O(\log R)`, proving `(6)`.

No value of `\kappa_0` is optimized. The significant point is qualitative but exact: after the paired-packing correction, the near-full-rank source-cost theorem crosses from a little-`o` rank horizon into a fixed positive fraction of the `\log\log y` transition.

## Prior art and novelty boundary

The analytic input remains `MC-S46`, Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli* (arXiv:2601.10927v1, 16 January 2026). Their Proposition 7 is the explicit iterated differencing inequality; the rough squarefree terminal specialization is already derived and audited in `MC-379`.

The packing observation `(12)` is classical algorithmic folklore associated with Next-Fit bin packing: consecutive bins produced by Next-Fit have combined load exceeding one bin capacity, yielding its elementary factor-two packing bound. A literature check on 19 September 2026 identified the classical performance-analysis literature, including D. S. Johnson, A. Demers, J. D. Ullman, M. R. Garey and R. L. Graham, *Worst-Case Performance Bounds for Simple One-Dimensional Packing Algorithms*, SIAM Journal on Computing 3 (1974), 299–325, DOI `10.1137/0203025`. The proof needed here is reproduced in `(12)`--`(13)` and does not rely on an unproved external optimization claim.

A targeted search for the combination of smooth-modulus character-sum factorization with this paired-bin count did not identify an existing theorem that changes the classification. Absence from that search is not evidence of novelty. No novelty is claimed for Next-Fit, Proposition 7, the rough squarefree terminal estimate, or the codimension argument. The Mathia-specific delta is the composition showing that the inverse smoothness-gap factor in the prior differencing depth was a packing artifact.

## Boundaries and falsification tests

- **The individual factor cap is load-bearing.** Every prime factor of `q_r` must satisfy `p\le y^{1-\delta}` so that no item already exceeds the bin capacity `y^{1-\delta/2}`.
- **Squarefree source conductors remain load-bearing.** Pairwise-coprime prime blocks and the terminal estimate `(16)` use the canonical quadratic source structure.
- **The total rough conductor must cross the cap.** Equation `(10)` and `(1)` ensure `q_r>y^{1-o(\delta)}>y^{1-\delta/2}`; otherwise the two-block argument selecting `Q` would fail.
- **The packing removes `1/\delta` only from the depth.** The preliminary factors still sit only `\asymp\delta` below the interval scale, so the power-saving exponent in `(17)` retains a multiplicative `\delta`.
- **The roughness cutoff still costs `2^{O(A)}`.** This is why the extension in `(6)` reaches only some fixed positive fraction of `L`, not arbitrary `R\asymp L`.
- **The `O(R)` low-conductor exceptional theorem is load-bearing.** Enlarging that family changes `(4)`.
- **`MC-392` is load-bearing.** Without its source-codimension/fourth-moment inequality, the analytic good-mode estimate does not force a logarithmic residual dimension.
- **No pointwise exact equality is proved.** The conclusion is `A\ge R-O(\log R)`, not `A\ge R`.
- **No Möbius or RH consequence.** This remains an internal obstruction for the endpoint/source-package mechanism.

## Consequence for the research line

The `R^2/L` deficit in `MC-395` was not an analytic barrier of the smooth character-sum theorem; it was created by a one-block-at-a-time lower bound in the modulus factorization. Pairing consecutive greedy blocks removes that artificial inverse-gap depth cost.

The source-cost frontier is therefore sharper: throughout `R=o(\log\log y)`, and even for `R` up to a sufficiently small fixed multiple of `\log\log y`, an exact endpoint source package must pay all but `O(\log R)` of the rank in `\log_y P`. Any surviving transition-scale mechanism must now beat the genuine `2^{O(A)}` differencing tariff, alter the `O(R)` exceptional-family theorem, or change the source-incidence/projected-simplex ledger itself.