# MC-381 — Fixed-power smoothness makes source cost linear in rank

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint source-package setup of `MC-377`--`MC-380`. Write

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R,
\qquad R\to\infty,
\]

for the nonempty endpoint defect cells, choose fixed lower-prime product representatives `V_i` for their independent quadratic endpoint generators, and put

\[
U=\bigcup_{i=1}^R V_i,
\qquad
P=\prod_{p\in U}p.
\tag{1}
\]

There are absolute constants `c_0,C>0` such that, for every moving exponent `A=A(y)>=2`, an exact endpoint realization cannot satisfy

\[
P\le y^A
\tag{2}
\]

for all sufficiently large `y` whenever

\[
A\le c_0 R
\tag{3}
\]

and

\[
2^{CA}\log\log y=o(\log y).
\tag{4}
\]

Consequently there is an absolute `c>0` such that every exact endpoint source package obeys

\[
\boxed{
\frac{\log P}{\log y}
\ge
c\min\{R,\log\log y\}
}
\tag{5}
\]

for all sufficiently large `y`.

The improvement over `MC-380` is a rank-budget observation coupled to the smooth-modulus scale already present in Cochrane--Granville--Zheng. `MC-380` killed source primes above the moving threshold `y^{1/(64A)}`. Under the trial bound `(2)` there can be `O(A^2)` such primes, so that finding imposed `A^2=o(R)` and obtained the rank-side scale `sqrt(R/log R)`. But the terminal differencing argument does not require every surviving source prime to be that small. It only requires the preliminary factors and terminal block to be a fixed power below the shell interval, while the terminal block is squarefree and rough from below. We may therefore fix once and for all a small `beta>0`, kill only source primes above `y^beta`, and pay only `O(A)` codimension.

A second, independent sharpening is that the prime-frame contradiction never needs the surviving subspace to have dimension `R-o(R)`. A fixed positive fraction of the `R` endpoint dimensions already leaves exponentially many rows, which is enough to dominate the polynomial and `2^{O(A)}` frame losses. Hence `A` may be a sufficiently small fixed multiple of `R`, not merely `o(R)`.

No estimate for `M(x)`, no RH consequence, and no new general character-sum theorem follows.

## 1. A fixed-power cutoff costs only linear codimension

Fix once and for all

\[
\beta:=\frac1{100}.
\tag{6}
\]

Assume `(2)` toward contradiction. For every source prime let

\[
c_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_R})\in\mathbb F_2^R
\tag{7}
\]

be its incidence column. Since every source prime `p>y^\beta` contributes more than `\beta\log y` to `\log P`,

\[
\#\{p\in U:p>y^\beta\}
\le\frac A\beta.
\tag{8}
\]

Define

\[
W:=\{I\in\mathbb F_2^R:
\langle I,c_p\rangle=0
\text{ for every }p>y^\beta\}.
\tag{9}
\]

Then

\[
\boxed{
\dim W\ge R-\frac A\beta,
\qquad
H:=|W|\ge2^{R-A/\beta}.
}
\tag{10}
\]

Choose `c_0` in `(3)` small enough that `A/\beta<=R/4`. Then

\[
\boxed{
\dim W\ge\frac{3R}{4},
\qquad
H\ge2^{3R/4}.
}
\tag{11}
\]

Every canonical source character indexed by `W`, and every pairwise difference character in its frame, is primitive quadratic with squarefree conductor supported only on source primes at most `y^\beta`.

This is the first source of the new rank scale: a trial exponent `A` costs only `O(A)` dimensions when the smoothness cutoff is fixed at the shell scale.

## 2. Tiny source primes are still packed, not deleted

As in `MC-379`--`MC-380`, use `MC-374` at fixed `delta=1` to call the `O(R)` endpoint differences whose minimum primitive source conductor is at most `y` **bad**, and call all remaining nonzero differences **good**. The prerequisite

\[
R y^{-c_1}\log y=o(1)
\tag{12}
\]

holds under the trial hypothesis: source-incidence independence gives

\[
R\le |U|\le\log_2P\ll A\log y,
\tag{13}
\]

while `(4)` implies `A=O(\log\log y)`.

Fix a good pair difference in `W` and let `q` be its canonical primitive squarefree source conductor. Then

\[
q>y,
\qquad
q\mid P,
\qquad
q\le y^A,
\qquad
P^+(q)\le y^\beta.
\tag{14}
\]

Let `k` denote the eventual differencing depth. Choose an absolute `K` large enough that, whenever `k<=C_2A`, all exceptional primes and all prime-local constants in the specialization `f(x)=x`, `g(x)=0` of Cochrane--Granville--Zheng Proposition 6 are absorbed above

\[
T_A:=2^{KA},
\tag{15}
\]

exactly as in `MC-379`--`MC-380`. Split

\[
q=S q_r,
\qquad
S:=\prod_{\substack{p\mid q\\p\le T_A}}p.
\tag{16}
\]

By the Chebyshev bound for the primorial,

\[
\log S\le\vartheta(T_A)\ll2^{KA}.
\tag{17}
\]

After taking the constant `C` in `(4)` larger than `K`,

\[
S=y^{o(1)},
\qquad
T_A<y^\beta,
\tag{18}
\]

and therefore `(14)` gives

\[
\boxed{q_r>y^{1-o(1)}.}
\tag{19}
\]

Thus the same packing principle as `MC-380` survives the fixed-power cutoff: tiny source coordinates consume one preliminary factor, not source codimension.

## 3. Fixed-power blocks give the same moving character saving

All prime factors of `q_r` lie in

\[
T_A<p\le y^\beta.
\tag{20}
\]

Greedily multiply distinct prime factors until the product first exceeds `y^\beta`. Because each factor is at most `y^\beta`, every completed block `B` satisfies

\[
y^\beta<B\le y^{2\beta}.
\tag{21}
\]

Continue until only a remainder at most `y^\beta` is left. Equation `(19)` and `3\beta<1` imply that, for sufficiently large `y`, at least two completed blocks exist; otherwise `q_r\le y^{3\beta}`, contradicting `(19)`.

Choose one completed block as the terminal factor `Q`. Use every other completed block, the possible final remainder, and the optional tiny factor `S` as preliminary factors. We obtain a pairwise-coprime factorization

\[
q=q_1\cdots q_kQ
\tag{22}
\]

with

\[
y^\beta<Q\le y^{2\beta},
\tag{23}
\]

and, for all sufficiently large `y`,

\[
q_i\le y^{2\beta}
\tag{24}
\]

for every preliminary factor. Since `q<=y^A`, the number of completed blocks is at most `A/\beta+O(1)`, so

\[
\boxed{k\le C_2A}
\tag{25}
\]

for an absolute constant `C_2` depending only on the fixed choice `(6)`.

Every prime divisor of `Q` exceeds `T_A`. Therefore the rough-squarefree terminal calculation proved in `MC-379` applies verbatim and gives

\[
\mathbf E_Q\ll Q^{-1/4}.
\tag{26}
\]

Now let `J` be any interval of length

\[
N\ge y^{1-o(1)}.
\tag{27}
\]

Because `2\beta=1/50`, equations `(18)`, `(24)` and `(23)` put every preliminary factor and `Q` a fixed power below `N`. Cochrane--Granville--Zheng Proposition 7 therefore gives, with

\[
M_i=\lfloor(N/q_i)^{2/3}\rfloor,
\]

\[
\left|\frac1N\sum_{n\in J}\chi_q(n)\right|
\ll
\sum_{i=1}^k M_i^{-2^{-i}}
+Q^{-1/(4\,2^k)}.
\tag{28}
\]

The fixed gaps in `(23)`--`(24)` and the depth bound `(25)` imply

\[
\boxed{
\left|\sum_{n\in J}\chi_q(n)\right|
\ll N y^{-\sigma_A},
\qquad
\sigma_A\ge2^{-C_3A}
}
\tag{29}
\]

for an absolute `C_3>0`.

This is analytically no stronger than the source-specific estimate already obtained in `MC-380`; the gain is that fixed-power smoothness requires deleting only `O(A)` source coordinates instead of `O(A^2)`.

The current Cochrane--Granville--Zheng manuscript is consistent with this scale independently of the above explicit specialization: its abstract allows smoothness up to `N^{1-\varepsilon}`, Corollary 11 permits pairwise-coprime preliminary factors `q_i<=N^{1-\varepsilon}`, and Remark 1 states that the proof can let the smoothness parameter move down to order `1/\log\log q`. The present proof nevertheless uses Propositions 6--7 explicitly, because the parameter `A` moves with `y` and the endpoint application needs the dependence visible.

## 4. A positive-fraction endpoint subspace is enough for the frame contradiction

Transfer `(29)` through the same Selberg-sieve/Bombieri prime-frame argument as `MC-379`--`MC-380`. Set

\[
b:=\sigma_A/100,
\qquad
B:=y^b.
\tag{30}
\]

The Selberg expansion leaves intervals of length `y^{1-o(1)}`. Equations `(23)`--`(24)` remain a fixed power below those intervals, so `(29)` is uniform through the expansion. The `O(R)` low-conductor pair differences from `MC-374` are paid for trivially as sparse bad neighbours. Hence the normalized shell Gram matrix `G` satisfies

\[
\lambda_{\max}(G)
\ll
R\sigma_A^{-1}
+H y^{-c_2\sigma_A}\log y
\tag{31}
\]

for an absolute `c_2>0`.

Exact endpoint row constancy still gives

\[
\operatorname{rank}G\le R,
\qquad
\operatorname{tr}G=H,
\qquad
\lambda_{\max}(G)\ge\frac HR.
\tag{32}
\]

Combining `(31)`--`(32)` and dividing by `H` yields

\[
\frac1R
\ll
\frac{R\sigma_A^{-1}}H
+y^{-c_2\sigma_A}\log y.
\tag{33}
\]

The earlier moving source-cost arguments imposed `\dim W=R-o(R)` as a convenient sufficient condition. Equation `(33)` shows that this was stronger than necessary. From `(11)` and `(29)`,

\[
\frac{R^2\sigma_A^{-1}}H
\ll
R^2\,2^{C_3A-3R/4}.
\tag{34}
\]

After shrinking `c_0` in `(3)` so that `C_3c_0<1/4`, `(34)` tends to zero exponentially. Thus the first term on the right of `(33)` is `o(1/R)` even though the kernel loses a fixed positive fraction of the endpoint dimensions.

For the second term, `(13)` and `(29)` show that it is `o(1/R)` after enlarging the constant in `(4)`: that condition guarantees

\[
\sigma_A\log y\gg\log R+\log\log y.
\tag{35}
\]

Both terms in `(33)` are therefore `o(1/R)`, a contradiction. This proves `(2)`--`(4)`.

## 5. Explicit linear-in-rank rate

Choose a sufficiently small absolute `c>0` and put

\[
A_*(y):=c\min\{R,\log\log y\}.
\tag{36}
\]

For `c` smaller than the constant in `(3)`, `A_*<=c_0R`. Also, choosing `c` so that `C c\log2<1/2`,

\[
2^{CA_*}\log\log y
\le
(\log y)^{1/2}\log\log y
=o(\log y).
\tag{37}
\]

If an exact endpoint had `\log P/\log y<A_*`, then `P<=y^{A_*}` and the moving theorem would give a contradiction. This proves `(5)`.

Compared with `MC-380`, the rank-side obstruction improves from

\[
\sqrt{R/\log R}
\]

to a fixed positive multiple of `R`; the analytic ceiling remains `\log\log y`. In the rank-limited regime the bound is therefore linear in the number of independent endpoint defect cells, up to an absolute nonoptimized constant.

## Prior art and novelty boundary

The analytic machinery is not new. The retained source `MC-S46` is Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026). A fresh check on 18 September 2026 found the arXiv record still at version 1. Its abstract explicitly states that the smoothness parameter can be taken to `N^{1-\varepsilon}`. Proposition 7 supplies the iterated pairwise-coprime factorization used in `(22)`--`(29)`, and Corollary 11 records the corresponding fixed-power-below-`N` regime. Remark 1 explicitly discusses moving the parameter down to order `1/\log\log q`.

The rough-squarefree terminal estimate `(26)` is the source-specific specialization already derived in `MC-379`, and the tiny-prime packing step is `MC-380`. The new derived point is their combination with a **fixed shell-power source cutoff** and the observation that the frame inequality only needs exponentially many surviving modes, not `2^{R-o(R)}` modes. Together those facts change the source-incidence codimension from `O(A^2)` to `O(A)` and permit `A` to be a sufficiently small fixed fraction of `R`.

A targeted literature search on 18 September 2026 found the Cochrane--Granville--Zheng manuscript and the usual smooth-modulus character-sum lineage, but no source stating the endpoint/source-incidence implication `(3)`--`(5)`. Absence from that search is not evidence of novelty, and no standalone novelty claim is made. The character-sum estimate, `q`-van der Corput factorization, complete-sum input, Selberg transfer, and trace/rank frame inequality are all prior or elementary ingredients.

As in `MC-379`--`MC-380`, `MC-S46` is manuscript-level evidence. A material revision of its Proposition 6, Proposition 7, Corollary 11, or the displacement-divisor input would require re-audit.

## Decisive audit and boundaries

- **Fixed-power smoothness, not a new character-sum theorem, supplies the codimension gain.** The proof deliberately chooses the nonoptimized constant `beta=1/100`; any sufficiently small fixed `beta` would serve. The analytic literature already handles far larger smoothness thresholds.
- **Positive-fraction rank retention is enough.** The frame lower bound is `H/R`, while the nonexponential losses are at most polynomial in `R` and exponential only in `O(A)`. Hence `H>=2^{cR}` suffices after taking `A<=c_0R` with a small enough absolute constant. No step requires `dim W=R-o(R)`.
- **Tiny primes remain packed rather than deleted.** The primorial estimate and condition `(4)` are load-bearing. Killing all primes below `2^{O(A)}` would reintroduce the rank loss of `MC-379`.
- **Primitive squarefree source structure remains load-bearing.** The terminal estimate `E_Q<<Q^{-1/4}` uses multiplication of the prime-local bounds over a rough squarefree terminal block. The result does not automatically extend to arbitrary prime-power conductors.
- **Low-conductor modes remain explicit exceptions.** The `O(R)` family from `MC-374` is paid for as sparse bad neighbours; no moving character-sum saving is asserted for it.
- **The `log log y` ceiling remains.** The terminal factor is now a fixed power of `y`, but the final `2^{-k}` differencing loss with `k=O(A)` still gives `sigma_A=2^{-O(A)}`. Beating the analytic branch in `(5)` requires a genuinely different depth loss or terminal mechanism.
- **This is a common-source architecture obstruction.** It lower-bounds the shared radical `P`; it does not say that every individual endpoint mode has large minimum conductor, and it does not by itself reach a quantity relevant to the Mertens function.
- **No RH, GRH, zero-density, or Möbius square-root cancellation input is used.** No estimate for `M(x)` follows.