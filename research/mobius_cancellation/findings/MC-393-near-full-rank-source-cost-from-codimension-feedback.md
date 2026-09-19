# MC-393 — Codimension feedback lifts fixed-power source cost to near full rank

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `SOURCE-COST` · `STRUCTURAL-OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint/source-package setup of `MC-374`, `MC-379`, `MC-381`, and `MC-392`. Write

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R,
\qquad
P=\prod_{p\in U}p,
\]

for the rank-`R` endpoint partition and the fixed lower-prime source package. Then the fixed-power cutoff in `MC-381` can be pushed from the convenient value `\beta=1/100` to **every fixed**

\[
0<\beta<1.
\]

More precisely, for each fixed `\beta<1` there is a constant `C_\beta>0` such that a trial bound

\[
P\le y^A,
\qquad A\ge2,
\tag{1}
\]

with

\[
2^{C_\beta A}\log\log y=o(\log y)
\tag{2}
\]

has the following consequence. If

\[
W_\beta
:=\{I\in\mathbf F_2^R:
\langle I,c_p\rangle=0
\text{ for every source prime }p>y^\beta\},
\tag{3}
\]

and

\[
c_\beta:=\operatorname{codim}W_\beta,
\qquad
d_\beta:=\dim W_\beta,
\qquad H_\beta:=|W_\beta|,
\]

then

\[
\boxed{c_\beta\le A/\beta,
\qquad
d_\beta\ge R-A/\beta.}
\tag{4}
\]

All but `O(R)` nonzero modes in `W_\beta` have normalized shell correlation

\[
|g(I)|\le\varepsilon_{A,\beta}(y),
\qquad
\varepsilon_{A,\beta}(y)=o(R^{-1/2}).
\tag{5}
\]

The key analytic point is that `(5)` does **not** require `\beta<1/3` or `\beta<1/2`. Once every surviving source prime is at most `y^\beta` with fixed `\beta<1`, its squarefree conductor can be packed into pairwise-coprime blocks bounded by `y^\gamma`, where

\[
\gamma:=\frac{1+\beta}{2}<1,
\tag{6}
\]

while every completed block has size greater than

\[
y^{\gamma-\beta}=y^{(1-\beta)/2}.
\tag{7}
\]

Thus the rough-squarefree terminal estimate of `MC-379` and Proposition 7 of Cochrane--Granville--Zheng still give a moving power saving with differencing depth `k=O_\beta(A)`.

Combining `(4)`--`(5)` with the exact codimension/exception inequality of `MC-392` produces a much stronger rank-side source-cost barrier. For every fixed `\eta\in(0,1)` there is a constant `a_\eta>0` such that every exact endpoint source package satisfies, for all sufficiently large `y` in the regime `R\to\infty`,

\[
\boxed{
\frac{\log P}{\log y}
\ge
\min\left\{(1-\eta)R,\ a_\eta\log\log y\right\}.
}
\tag{8}
\]

Hence the rank-limited coefficient can be made arbitrarily close to **one**. The earlier `MC-381` bound `c\min\{R,\log\log y\}` used a deliberately small fixed cutoff and a direct frame-eigenvalue comparison; feeding the later codimension/exception obstruction back into the source-cost argument removes that small rank coefficient. The `\log\log y` ceiling remains, with a constant that deteriorates as `\eta\downarrow0` because the block gap `1-\beta` shrinks and the differencing depth constant grows.

No estimate for `M(x)` and no RH consequence follows.

## 1. A cutoff at any fixed shell power below one costs at most `A/β` dimensions

Assume `(1)`. For every source prime let

\[
c_p=(\mathbf1_{p\in V_1},\ldots,\mathbf1_{p\in V_R})\in\mathbf F_2^R
\]

be its incidence column, as in `MC-379`--`MC-381`. Every source prime `p>y^\beta` contributes more than `\beta\log y` to `\log P`, so

\[
\#\{p\in U:p>y^\beta\}
\le\frac A\beta.
\tag{9}
\]

Imposing the parity constraints in `(3)` therefore gives `(4)`. Every canonical source character indexed by `W_\beta` has squarefree conductor supported only on primes at most `y^\beta`.

This step uses no character-sum estimate. It is the exact weighted-source-cost/codimension dictionary that later enters `MC-392`.

## 2. Cap-packing removes the artificial `3β<1` restriction

Fix a nonzero mode in `W_\beta` whose minimum primitive source conductor exceeds `y`; `MC-374` shows that only `O(R)` endpoint modes fail this condition under `(2)`. Let `q` be its canonical primitive squarefree source conductor. Then

\[
q>y,
\qquad q\mid P,
\qquad q\le y^A,
\qquad P^+(q)\le y^\beta.
\tag{10}
\]

As in `MC-379`--`MC-381`, choose

\[
T_A=2^{K_\beta A}
\]

large enough to absorb the depth-`O_\beta(A)` local constants and exceptional primes in the rough-squarefree terminal estimate, and split

\[
q=S q_r,
\qquad
S:=\prod_{\substack{p\mid q\\p\le T_A}}p.
\tag{11}
\]

Condition `(2)`, after enlarging `C_\beta`, gives

\[
S=y^{o(1)},
\qquad T_A<y^\beta,
\qquad q_r>y^{1-o(1)}.
\tag{12}
\]

The grouping in `MC-381` used a block threshold `y^\beta` and bounded an overshooting block by `y^{2\beta}`. Requiring two such completed blocks led to the convenient sufficient condition `3\beta<1`. That restriction is not intrinsic.

Instead set `\gamma=(1+\beta)/2`. Greedily multiply unused prime factors of `q_r` while the product remains at most `y^\gamma`; whenever the next prime would make the product exceed `y^\gamma`, close the current block and start another. Since every prime factor is at most `y^\beta`, every closed block `B` satisfies

\[
\boxed{
y^{\gamma-\beta}<B\le y^\gamma.}
\tag{13}
\]

There may be one final remainder at most `y^\gamma`. Because `q_r>y^{1-o(1)}` whereas `\gamma<1`, at least two nontrivial factors are present for sufficiently large `y`: either there are at least two closed blocks, or there is one closed block and a nontrivial final remainder. Choose one closed block as the terminal factor `Q`; use all other blocks, the final remainder when nontrivial, and `S` when nontrivial as preliminary factors. Thus

\[
q=q_1\cdots q_kQ
\tag{14}
\]

with pairwise-coprime factors,

\[
y^{(1-\beta)/2}<Q\le y^\gamma,
\qquad
q_i\le y^\gamma
\tag{15}
\]

for all sufficiently large `y`, and

\[
\boxed{k\le C'_\beta A.}
\tag{16}
\]

Indeed every closed block consumes more than `((1-\beta)/2)\log y` of `\log q`, so there are only `O_\beta(A)` of them.

This is the point that allows every fixed `\beta<1`: the blocks are capped below the shell interval rather than bounded by an overshoot of the cutoff itself.

## 3. The existing rough-terminal estimate still gives a moving power saving

Every prime divisor of `Q` exceeds `T_A`, so the squarefree terminal calculation of `MC-379` gives

\[
\mathbf E_Q\ll Q^{-1/4}.
\tag{17}
\]

For every interval length

\[
N\ge y^{1-o(1)},
\]

`(15)` puts all preliminary factors and `Q` below

\[
N^{1-\epsilon_\beta}
\]

for some fixed `\epsilon_\beta>0`, because `\gamma<1`. Proposition 7 / Corollary 11 of Cochrane--Granville--Zheng therefore applies to `(14)`. Combining the fixed gap `1-\gamma=(1-\beta)/2`, the terminal lower bound in `(15)`, `(16)`, and `(17)` yields

\[
\boxed{
\left|\sum_{n\in J}\chi_q(n)\right|
\ll_\beta N y^{-\sigma_{A,\beta}},
\qquad
\sigma_{A,\beta}\ge2^{-C''_\beta A}.
}
\tag{18}
\]

The same Selberg-sieve/Bombieri transfer already audited in `MC-379`--`MC-381` converts `(18)` into a normalized shell-correlation bound on every such good endpoint difference,

\[
|g(I)|
\ll_\beta y^{-c_\beta'\sigma_{A,\beta}}\log y.
\tag{19}
\]

Under `(2)`, `(19)` is `o(R^{-1/2})`. To see that no hidden growth of `R` is being ignored, source-incidence independence and `(1)` give the same crude bound as `MC-381`,

\[
R\le |U|\le\log_2P\ll A\log y.
\tag{20}
\]

Thus `\log R=O(\log\log y)` whenever `(2)` is active, while `\sigma_{A,\beta}\log y/\log\log y\to\infty` after enlarging `C_\beta`. This proves `(5)`.

The only endpoint differences excluded from `(19)` are the `O(R)` modes whose minimum primitive source conductor is at most `y`, exactly the fixed-`\delta=1` exceptional family supplied by `MC-374`.

## 4. MC-392 turns exponentially many surviving modes into a near-full-rank cost

Apply `MC-392` to `W_\beta`. Let `B\subset W_\beta\setminus\{0\}` be the low-conductor exceptional family. Then

\[
|B|=O(R),
\tag{21}
\]

and every other nonzero mode satisfies `(5)`. Since `(4)` gives

\[
c_\beta\le A/\beta,
\]

`MC-392` yields

\[
|B|+1
\ge
\frac{H_\beta}{2c_\beta+3}
\left(1-R\varepsilon_{A,\beta}(y)^2\right)^2
=
(1-o(1))\frac{2^{d_\beta}}{2c_\beta+3}.
\tag{22}
\]

Now fix `\eta\in(0,1)` and choose any fixed

\[
1-\eta<\beta<1,
\tag{23}
\]

for example `\beta=1-\eta/2`. If a trial exponent also satisfies

\[
A\le(1-\eta)R,
\tag{24}
\]

then `(4)` gives a fixed positive-dimensional fraction

\[
d_\beta
\ge
\left(1-\frac{1-\eta}{\beta}\right)R
=:\delta_\eta R,
\qquad \delta_\eta>0.
\tag{25}
\]

Hence the right side of `(22)` is exponential in `R`, while `(21)` is only linear. For `R\to\infty` this is impossible. Therefore `(1)`, `(2)`, and `(24)` cannot hold simultaneously.

This is the feedback missing from `MC-381`: once the later fourth-moment/codimension theorem is available, the surviving source frame does not need enough dimension to beat the factor `2^{O(A)}` through a direct largest-eigenvalue estimate. Any fixed positive fraction of the endpoint dimensions already makes the exact `MC-392` exceptional-set lower bound exponentially larger than the `O(R)` analytic exceptional family.

## 5. Architecture-level rate

Fix `\eta>0` and choose `\beta` as in `(23)`. Let `C_\beta` be large enough for the previous sections, and choose `a_\eta>0` so small that

\[
C_\beta a_\eta\log2<\frac12.
\tag{26}
\]

Set

\[
A_*(y)
:=
\min\{(1-\eta)R,\ a_\eta\log\log y\}.
\tag{27}
\]

Then

\[
2^{C_\beta A_*}\log\log y
\le
(\log y)^{1/2}\log\log y
=o(\log y).
\tag{28}
\]

If `P\le y^{A_*}` for arbitrarily large `y`, Sections 1--4 give a contradiction. Therefore `(8)` follows, after harmlessly decreasing `a_\eta` to cover the finite threshold where `A_*<2`.

The rank-side coefficient is now asymptotically arbitrary below one. What prevents setting `\eta=0` is analytic rather than combinatorial: the block cap must remain a fixed power below the shell interval, so `\beta<1` is load-bearing and the constants in `(16)`--`(19)` deteriorate as `\beta\uparrow1`.

## Prior art and novelty boundary

The analytic inputs are prior art already retained in this line. `MC-S46` is Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026). A fresh check on 19 September 2026 found the arXiv record still at version 1. Its Corollary 11 explicitly allows a factorization `q=q_1\cdots q_kQ` with every factor `q_j\le N^{1-\epsilon}`; Proposition 7 supplies the iterated differencing inequality. The rough squarefree terminal estimate `(17)` is the source-specific specialization already derived from Propositions 6--7 and Lemma 7 in `MC-379`.

The `O(R)` low-conductor family is the Schlage-Puchta prime-frame consequence already established and prior-art audited in `MC-374`. The codimension/exception inequality `(22)` is exactly `MC-392`; its additive-energy ingredients are classical and that finding already carries the corresponding audit.

A targeted mechanism-level search on 19 September 2026 for smooth-modulus factorization together with source-incidence rank/codimension and binary Cayley-frame exception bounds found the character-sum literature above but no external source needed to treat `(8)` as an existing named theorem. This absence is not evidence of novelty. The new Mathia delta is the elementary **cap-packing optimization** `(13)`--`(16)` plus the feedback composition `MC-374 + MC-379 + MC-392`, which upgrades the rank coefficient in the internal endpoint/source-cost obstruction. No standalone novelty claim is made.

## Boundaries and falsification tests

- **`\beta<1` is load-bearing.** The block cap `\gamma=(1+\beta)/2` must stay a fixed power below the shell interval. The proof is not uniform as `\beta\uparrow1`.
- **The squarefree canonical source conductor is load-bearing.** The terminal estimate `(17)` is the rough-squarefree specialization of `MC-379`; arbitrary prime-power conductors reintroduce the generic complete-sum losses.
- **The minimum-conductor exception theorem is load-bearing.** Equation `(21)` uses `MC-374` at fixed threshold `y`; without only `O(R)` low-conductor modes, `MC-392` need not contradict the analytic decomposition.
- **The endpoint projected-simplex geometry is load-bearing.** Equation `(22)` is not a generic character-family inequality; it depends on the exact endpoint/source-frame hypotheses of `MC-392`.
- **The analytic ceiling remains.** The near-unit coefficient applies on the rank side of `(8)` only while the moving-depth saving satisfies `(2)`. This finding does not remove the `\log\log y` horizon.
- **No statement at coefficient exactly one.** For each fixed `\eta>0` the theorem gives `(1-\eta)R`; no uniform limit `\eta\to0` is claimed.
- **No Möbius/RH consequence.** The result strengthens only the internal source-package obstruction for the exact endpoint program.

## Consequence for the research line

The live source-incidence question after `MC-392` is sharper than “can the source supply linear codimension?” The existing smooth-modulus machinery can retain a subspace after deleting source primes above **any fixed power below the shell scale**, and the exact codimension feedback then forces source package exponent essentially one unit per endpoint rank before the analytic `\log\log y` ceiling intervenes.

Accordingly, further optimization of the small `\beta=1/100` constants in `MC-381` is no longer a frontier. The remaining escape must change one of the load-bearing inputs: beat the moving-depth `\log\log y` ceiling, invalidate the exact squarefree source model, enlarge the low-conductor exceptional family beyond `O(R)`, or leave the endpoint projected-simplex geometry to which `MC-392` applies.