# MC-380 — Tiny source primes can be packed before terminal differencing

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint source-package setup of `MC-377`--`MC-379`. Write

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

There is an absolute constant `C>0` such that if a moving exponent `A=A(y)>=2` satisfies

\[
A^2=o(R)
\tag{2}
\]

and

\[
2^{CA}\log\log y=o(\log y),
\tag{3}
\]

then an exact endpoint realization cannot satisfy

\[
P\le y^A
\tag{4}
\]

for all sufficiently large `y`.

Consequently there is an absolute `c>0` such that every exact endpoint source package obeys

\[
\boxed{
\frac{\log P}{\log y}
\ge
c\min\left\{
\sqrt{\frac{R}{\log(R+2)}},
\ \log\log y
\right\}
}
\tag{5}
\]

for all sufficiently large `y`.

This combines the two previously separate strengths of `MC-378` and `MC-379`. `MC-378` preserved the strong rank-side condition `A^2=o(R)` but inherited a `log log log y` analytic ceiling. `MC-379` lifted the analytic ceiling to `log log y`, but did so by killing every source coordinate below `2^{O(A)}`, which replaced the rank-side condition by `2^{O(A)}=o(R)`. The present observation is that those tiny source primes do **not** need to be killed. Their entire product is `y^{o(1)}` in the moving range `(3)`, so they can be packed into one preliminary factor in the Cochrane--Granville--Zheng differencing decomposition. Only the terminal factor needs the lower roughness cutoff.

No estimate for `M(x)`, no RH consequence, and no new general character-sum theorem follows.

## 1. Kill only the genuinely large source coordinates

Assume `(4)` toward contradiction. Put

\[
\theta:=\frac1{64A},
\qquad
\delta:=\frac1{16A}=4\theta.
\tag{6}
\]

For every source prime let

\[
c_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_R})\in\mathbb F_2^R
\tag{7}
\]

be its incidence column. A source prime `p>y^\theta` contributes more than `\theta\log y` to `\log P`; hence

\[
\#\{p\in U:p>y^\theta\}
\le \frac A\theta
=64A^2.
\tag{8}
\]

Define only the large-prime kernel

\[
W:=\{I\in\mathbb F_2^R:
\langle I,c_p\rangle=0
\text{ for every }p>y^\theta\}.
\tag{9}
\]

Then

\[
\boxed{
\dim W\ge R-64A^2,
\qquad
H:=|W|\ge2^{R-64A^2}.
}
\tag{10}
\]

By `(2)`, `H=2^{R-o(R)}`. Every canonical source character indexed by `W`, and every pairwise difference character in its frame, is primitive quadratic with squarefree conductor supported on primes at most `y^\theta`.

This is exactly the rank geometry of `MC-378`. In particular no `2^{O(A)}` family of tiny-prime incidence columns has been removed.

## 2. The total tiny-prime factor is subpower and can be isolated

Let `q` be the primitive squarefree conductor of a nonprincipal pair character arising from `W`. As in `MC-379`, first discard the `O(R)` endpoint differences whose minimum primitive source conductor is at most `y`; call the remaining differences **good**. For a good difference,

\[
q>y,
\qquad
q\mid P,
\qquad
q\le y^A.
\tag{11}
\]

Choose an absolute `K` large enough that for every differencing depth `k<=50A`, every prime-local exceptional factor in the specialization `f(x)=x`, `g(x)=0` of Cochrane--Granville--Zheng Proposition 6 is at most

\[
T_A:=2^{KA},
\tag{12}
\]

and, for `p>T_A`, the two rough-terminal absorptions used in `MC-379` hold:

\[
C_k\le p^{1/16},
\qquad
1+\frac{k}{\sqrt p}\le p^{1/16},
\tag{13}
\]

where `C_k=2^{k+2}` is the prime-local complete-sum constant in this specialization.

Split

\[
q=S q_r,
\qquad
S:=\prod_{\substack{p\mid q\\p\le T_A}}p,
\qquad
q_r:=\prod_{\substack{p\mid q\\p>T_A}}p.
\tag{14}
\]

The key point is that `S` is bounded by the full primorial below `T_A`, independently of how many tiny source coordinates occur in the incidence code. By the classical Chebyshev bound `\vartheta(t)=\sum_{p\le t}\log p\ll t`,

\[
\log S\le\vartheta(T_A)\ll2^{KA}.
\tag{15}
\]

After taking the absolute constant `C` in `(3)` larger than `K`, condition `(3)` gives

\[
2^{KA}=o(\log y),
\qquad
S=y^{o(1)}.
\tag{16}
\]

Therefore `(11)` implies

\[
\boxed{q_r>y^{1-o(1)}.}
\tag{17}
\]

Thus the tiny source primes may be numerous, but in the admissible moving range they cannot carry a positive proportion of the logarithmic conductor of any good mode.

## 3. Pack the tiny factor before a rough squarefree terminal block

All prime factors of `q_r` lie in

\[
T_A<p\le y^\theta.
\tag{18}
\]

By `(17)` and `\theta=\delta/4`, for all sufficiently large `y` every such prime also satisfies

\[
p\le q_r^{\delta/3}.
\tag{19}
\]

Choose a product `Q` of prime factors of `q_r` greedily until it first exceeds `q_r^{\delta/3}`. Equation `(19)` gives

\[
q_r^{\delta/3}<Q\le q_r^{2\delta/3}.
\tag{20}
\]

Partition the remaining prime factors of `q_r/Q` greedily into pairwise coprime blocks. Every nonfinal block can be chosen in `(q_r^{\delta/3},q_r^{2\delta/3}]`, while the last may be smaller. Consequently

\[
q_r/Q=r_1\cdots r_m,
\qquad
m\le \frac3\delta+1<49A,
\tag{21}
\]

and every `r_j<=q_r^{2\delta/3}`. If `S>1`, include it as one additional preliminary factor. We have therefore factored

\[
q=q_1\cdots q_kQ,
\qquad
k\le50A,
\tag{22}
\]

into pairwise coprime factors with

\[
q_i\le y^{1/24}
\tag{23}
\]

for every preliminary factor once `y` is large: the rough blocks satisfy this because `q_r<=q<=y^A` and `2A\delta/3=1/24`, while `(16)` gives the same bound for the optional tiny factor `S`.

The terminal factor is squarefree, every `p|Q` exceeds `T_A`, and `(17)`, `(20)` give

\[
Q\ge y^{1/(64A)}
\tag{24}
\]

for all sufficiently large `y` after harmlessly weakening the exponent.

This is the step missed by the small-prime pruning in `MC-379`: Proposition 7 requires the preliminary factors and terminal factor to be pairwise coprime, but it imposes no lower roughness condition on the preliminary factors. The entire tiny-prime product can therefore be consumed before the terminal complete-sum estimate.

## 4. The MC-379 rough-terminal estimate survives unchanged

Apply Cochrane--Granville--Zheng Proposition 7 to `a_q(n)=\chi_q(n)` with the factorization `(22)`. For an interval of length

\[
N\ge y^{1-o(1)},
\tag{25}
\]

all preliminary factors satisfy `q_i<<N` by `(23)`, so the displacement parameters

\[
M_i=\left\lfloor(N/q_i)^{2/3}\right\rfloor
\]

tend to infinity with a fixed power of `y`.

The terminal-factor calculation of `MC-379` depends only on the facts that `Q` is squarefree, every `p|Q` exceeds the roughness cutoff, and the differencing depth is `k=O(A)`. Equations `(13)`, `(22)` therefore give exactly the same fixed-power terminal estimate

\[
\mathbf E_Q\ll Q^{-1/4}.
\tag{26}
\]

Proposition 7 then yields

\[
\left|\frac1N\sum_{n\in J}\chi_q(n)\right|
\ll
\sum_{i=1}^k M_i^{-2^{-i}}
+Q^{-1/(4\,2^k)}.
\tag{27}
\]

Using `(23)`, `(24)`, and `k<=50A`, the preliminary terms and the terminal term are all bounded by a moving power saving

\[
\boxed{
\left|\sum_{n\in J}\chi_q(n)\right|
\ll N y^{-\sigma_A},
\qquad
\sigma_A\ge2^{-C_1A}
}
\tag{28}
\]

for an absolute `C_1>0`. The factor `1/A` implicit in converting `(24)` into a `y`-exponent is absorbed into `2^{-C_1A}` because `A>=2`.

Crucially, deriving `(28)` costs **no tiny-prime source codimension**. Tiny primes affect one preliminary factor and increase `k` by at most one; they do not enter the rough terminal product where the constants `C_k^{\omega(Q)}` and `\prod_{p|Q}(1+k/\sqrt p)` must be absorbed.

## 5. The prime frame now keeps the stronger rank condition

Transfer `(28)` through the same Selberg-sieve/Bombieri prime-frame argument as `MC-379`. Choose

\[
b:=\sigma_A/100,
\qquad
B:=y^b.
\tag{29}
\]

The Selberg expansion leaves inner intervals of length `y^{1-o(1)}`, so `(28)` remains uniform after its `B^2` cost. The `O(R)` low-conductor pair differences from `MC-374` are paid for trivially as sparse bad neighbours. Thus, for the normalized shell Gram matrix `G`,

\[
\lambda_{\max}(G)
\ll
R\sigma_A^{-1}
+H y^{-c_0\sigma_A}\log y
\tag{30}
\]

for an absolute `c_0>0`.

On the other hand exact endpoint row constancy gives

\[
\operatorname{rank}G\le R,
\qquad
\operatorname{tr}G=H,
\qquad
\lambda_{\max}(G)\ge\frac HR.
\tag{31}
\]

By `(10)` and `(2)`,

\[
H=2^{R-o(R)},
\]

so the first term in `(30)`, divided by `H`, is `o(1/R)`. Under `(4)`, source-incidence independence also gives

\[
R\le |U|\le\log_2P\ll A\log y.
\tag{32}
\]

After taking the absolute constant in `(3)` larger than the one in `(28)`, condition `(3)` implies

\[
R y^{-c_0\sigma_A}\log y=o(1).
\tag{33}
\]

Dividing `(30)` by `H` now contradicts `(31).` This proves `(2)`--`(4)`.

## 6. Explicit rate

Choose a sufficiently small absolute `c>0` and put

\[
A_*(y):=
 c\min\left\{
\sqrt{\frac{R}{\log(R+2)}},
\ \log\log y
\right\}.
\tag{34}
\]

Then

\[
\frac{A_*^2}{R}\le\frac{c^2}{\log(R+2)}\to0.
\tag{35}
\]

Also `A_*<=c\log\log y`, so for `c` small relative to the absolute constant in `(3)`,

\[
2^{CA_*}\log\log y=o(\log y).
\tag{36}
\]

If an exact endpoint had `\log P/\log y<A_*`, then `P<=y^{A_*}` and the moving theorem would give a contradiction. This proves `(5)`.

The resulting rate strictly combines the complementary bounds of `MC-378` and `MC-379`: it keeps the `sqrt(R/log R)` rank scale of the former while keeping the `log log y` analytic scale of the latter.

## Prior art and novelty boundary

The analytic machinery remains Cochrane--Granville--Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026), retained as `MC-S46`. Proposition 7 explicitly permits an arbitrary pairwise-coprime decomposition `q=q_1\cdots q_kQ`; its displayed bound charges the preliminary factors only through the displacement quantities `M_i`, while the complete-sum average is taken solely over the terminal factor `Q`. Their proof of Theorem 4 likewise groups nonterminal prime-power factors into blocks `q_i` before applying Theorem 3. These are literature facts, not new character-sum claims.

`MC-379` supplied the source-specific rough-squarefree terminal calculation from Propositions 6--7 and Lemma 7. The present finding changes only the arithmetic factorization fed into that calculation: rather than annihilating every source incidence column below `2^{O(A)}`, it uses `\vartheta(2^{O(A)})=2^{O(A)}` to show that their entire squarefree product is subpower and places that product among the preliminary factors.

A fresh targeted literature audit on 18 September 2026 checked the current arXiv v1 manuscript together with the established Graham--Ringrose/Heath-Brown smooth-modulus lineage and later composite-modulus work. The literature explicitly contains the `q`-van der Corput factorization principle and arbitrary preliminary blocks, but no source was found stating the endpoint/source-incidence consequence `(2)` or the rate `(5)`. Absence from that search is not evidence of novelty, and **no standalone novelty claim is made**.

As in `MC-379`, the load-bearing analytic input is still manuscript-level evidence. A material revision of Cochrane--Granville--Zheng Proposition 6, Proposition 7, or Lemma 7 requires re-audit.

## Decisive audit and boundaries

- **The tiny-prime product is small only in the moving range used here.** The argument needs `2^{KA}=o(log y)` so that the complete primorial below `T_A=2^{KA}` is `y^{o(1)}`. Condition `(3)` is deliberately stronger and supplies this.
- **Only the terminal factor is required to be rough.** The preliminary tiny block may contain all exceptional and small primes. Treating it as part of `Q` would reintroduce the `C_k^{\omega(Q)}` obstruction from `MC-379`.
- **Squarefree primitive source conductors remain load-bearing.** The packing argument uses one copy of each tiny prime and the terminal estimate still multiplies prime-local square-root bounds over a squarefree `Q`.
- **The `A^2` rank tariff is still real.** Source primes above `y^{1/(64A)}` are genuinely removed to ensure the remaining rough part has uniformly small prime factors. The proof does not remove that codimension cost.
- **The final `2^{-O(A)}` differencing root is still real.** Packing the tiny block removes the exponential rank tariff, not the exponential analytic loss. This is why the analytic ceiling in `(5)` remains `log log y` rather than a larger scale.
- **The sparse low-conductor family is not ignored.** Exactly as in `MC-379`, the `O(R)` bad pair differences from `MC-374` are carried through the frame with trivial diagonal-scale control.
- **No circular zero information is used.** The argument uses finite character-sum estimates, source incidence, Selberg/Bombieri transfer, and elementary primorial growth. It does not use RH, GRH, a critical-strip zero-free region, or a desired bound for `M(x)`.
- **No estimate for `M(x)` follows.** The theorem only sharpens the source-realizability obstruction inside the exact endpoint branch.