# FD-239 — Sublinear off-dyadic response sampling still has a macroscopic signed nullspace

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response kernel / sparse point sampling / signed capacity / exact prescribed zeros / response-density boundary
- **Depends on:** FD-225, FD-231, FD-238
- **Classification:** `EXACT-DERIVED + COUNTERMODEL + SPARSE-POINT-SAMPLING-NULLSPACE + SIGNED-LINEAR-CAPACITY + RESPONSE-DENSITY-BOUNDARY`

## Claim

FD-238 shows that exact dyadic response coordinates leave a macroscopic signed nullspace. Adding a sublinear number of off-dyadic point samples per dyadic octave still does not remove that obstruction.

Let `S subset N` be any prescribed sampling set and write

\[
B_k=(2^{k-1},2^k]\cap\mathbb N,
\qquad
s_k=|S\cap B_k|.
\]

Assume only

\[
\boxed{s_k=o(2^k).}
\tag{1}
\]

Then there exists an integer sequence `(b_n)` such that

\[
\boxed{|b_n|\le n\qquad(n\ge1),}
\tag{2}
\]

whose divisor response

\[
(\mathscr A b)(m)
=
\sum_{d\le m}b_dM\!\left(\left\lfloor\frac md\right\rfloor\right)
\tag{3}
\]

vanishes at every prescribed sample:

\[
\boxed{(\mathscr A b)(s)=0\qquad(s\in S).}
\tag{4}
\]

The construction can simultaneously impose zero response at every dyadic endpoint, and its full off-sample response remains only linear:

\[
\boxed{(\mathscr A b)(2^j)=0\quad(j\ge0),
\qquad
(\mathscr A b)(m)=O(m).}
\tag{5}
\]

Nevertheless the coefficient vector retains the same macroscopic signed capacity as in FD-238:

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\ge
\frac{12}{\pi^2}-1.
}
\tag{6}
\]

Both signs remain macroscopic:

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}b_n^+}
     {\sum_{n\in B_k}n},
\quad
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}b_n^-}
     {\sum_{n\in B_k}n}
\ge
\frac12\left(\frac{12}{\pi^2}-1\right).
}
\tag{7}
\]

Consequently, any well-defined family of linear response rows that factors only through the point coordinates `{(mathscr A b)(s): s in S}` annihilates this profile exactly. In particular, augmenting the dyadic switched family by finitely many, polylogarithmically many, or more generally `o(2^k)` raw off-dyadic response samples in the `k`-th octave cannot yield signed coercivity on the natural linear-capacity box.

This gives a genuine density boundary for the point-sampling escape proposed after FD-238. It does **not** prove that positive-density sampling is sufficient. At the opposite endpoint, retaining every integer response is injective by the exact divisor inversion of FD-225. The intermediate positive-density regime remains open.

The construction is signed and therefore is not a physical nonnegative prime-reservoir occupancy. Positivity and source coherence remain possible mechanisms of transversality.

## 1. Put exact reset points at every requested sample

As in FD-238, start from an integer arithmetic function `g` and set

\[
b=\mathbf1*g,
\qquad
b_n=\sum_{d\mid n}g(d).
\tag{8}
\]

Since `mu*1=epsilon`, the divisor response has the exact cumulative form

\[
\boxed{
(\mathscr A b)(m)
=
\sum_{n\le m}g(n)
=:Y(m).
}
\tag{9}
\]

Set `g(1)=0`. Fix a dyadic band `B_k`. Order the points of `S cap B_k`, adjoin the right endpoint `2^k`, and use these points as consecutive cell boundaries. Thus `B_k` is partitioned into at most

\[
s_k+1
\tag{10}
\]

nonempty consecutive integer cells. The left endpoint `2^{k-1}` already has zero cumulative sum from the preceding band.

Treat each cell independently. Choose a pivot `e` in the cell for which `phi(e)` is maximal. Process all nonpivot integers in increasing order and assign

\[
g(n)\in\{-\varphi(n),+\varphi(n)\}
\tag{11}
\]

with sign opposite to the current nonpivot partial sum. If `W` is the largest nonpivot `phi`-weight in the cell, the one-dimensional greedy step keeps the running nonpivot sum within `[-W,W]`. At the end set the pivot value to the negative of the final nonpivot sum. Since `phi(e)` is maximal,

\[
|g(e)|\le W\le\varphi(e).
\tag{12}
\]

Hence every cell has exact total zero while all values are integral and satisfy

\[
|g(n)|\le\varphi(n).
\tag{13}
\]

Because every requested sample is a cell boundary and every preceding cell has total zero,

\[
Y(s)=0\qquad(s\in S).
\tag{14}
\]

The same is true at each adjoined dyadic endpoint. Equations `(9)` and `(14)` prove `(4)` and the first part of `(5)`.

## 2. The full response remains linearly bounded

The extra reset points do not worsen the between-sample response. Inside a cell the greedy nonpivot partial sum has modulus at most `W`. If the pivot occurs before the end of the cell in the natural integer order, inserting its final correction changes a natural-order partial sum into a difference of two greedy partial sums, so its modulus is at most `2W`.

For a cell in `B_k`, `W<=2^k`. Since every new cell starts again from cumulative value zero,

\[
|Y(m)|\le 2^{k+1}
\qquad(m\in B_k),
\tag{15}
\]

and therefore

\[
\boxed{Y(m)=O(m).}
\tag{16}
\]

By `(9)` this is the second assertion in `(5)`.

The coefficient envelope follows exactly as in FD-238. From `(8)`, `(13)`, and the classical identity `sum_(d|n) phi(d)=n`,

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|
\le
\sum_{d\mid n}\varphi(d)
=
\boxed n,
\tag{17}
\]

which proves `(2)`.

## 3. Sublinear sampling costs only negligible capacity

Every nonpivot integer still has the saturated magnitude

\[
|g(n)|=\varphi(n).
\tag{18}
\]

For such an `n`, separating the top divisor in `(8)` gives

\[
\begin{aligned}
|b_n|
&\ge
|g(n)|-
\sum_{\substack{d\mid n\\d<n}}|g(d)|\\
&\ge
\varphi(n)-
\sum_{\substack{d\mid n\\d<n}}\varphi(d)\\
&=
\boxed{2\varphi(n)-n}.
\end{aligned}
\tag{19}
\]

There are at most `s_k+1` pivots in `B_k`. Omitting their terms from the band sum in `(19)` changes the corresponding full-band lower bound by at most

\[
O((s_k+1)2^k)=o(4^k)
\tag{20}
\]

by assumption `(1)`. The standard summatory totient asymptotic

\[
\sum_{n\le x}\varphi(n)
=
\frac{3}{\pi^2}x^2+O(x\log x)
\tag{21}
\]

therefore gives

\[
\sum_{n\in B_k}|b_n|
\ge
\left(\frac{9}{2\pi^2}-\frac38\right)4^k
+o(4^k).
\tag{22}
\]

Since

\[
\sum_{n\in B_k}n
=
\frac38\,4^k+O(2^k),
\tag{23}
\]

this proves `(6)`.

To separate the two signs, let

\[
B(x)=\sum_{n\le x}b_n.
\]

Using `(8)` and Abel summation with `Y(d)=O(d)` from `(16)`,

\[
B(x)
=
Y(x)
+
\sum_{d<x}Y(d)
\left(
\left\lfloor\frac xd\right\rfloor
-
\left\lfloor\frac{x}{d+1}\right\rfloor
\right)
=
O(x\log x).
\tag{24}
\]

Thus the signed sum over `B_k` is `O(k2^k)=o(4^k)`, whereas `(6)` supplies absolute mass `Omega(4^k)`. Splitting total variation into positive and negative parts proves `(7)`.

## 4. What point sampling can and cannot repair

FD-238 left open whether adding off-dyadic/all-integer response coordinates might remove the exact dyadic signed kernel. The present result separates those two possibilities. **Sparse off-dyadic point sampling does not help at the capacity scale.** An arbitrary sublinear number of sampled integers in each octave can be promoted to exact reset points while sacrificing only a vanishing fraction of the saturated `phi`-weighted construction.

This statement is stronger than failure of any particular scalar normalization. The selected response coordinates themselves are exactly zero, so every linear row built only from them is also zero. The obstruction therefore applies to arbitrary weights, finite differences, or cross-sample linear combinations supported on the same sparse sample set.

The theorem deliberately stops at sampling density. If `|S cap B_k|` is comparable to `2^k`, the number of pivots may itself consume a positive fraction of the band and argument `(20)` no longer preserves the FD-238 capacity lower bound. This does not establish coercivity there; it only identifies the first regime not killed by this construction. Full all-integer data are injective: if `(mathscr A b)(m)=0` for every `m`, then the successive differences of `(9)` force `g=0`, hence `b=0`.

For the Farey research frontier, a response-topology refinement based on point samples must therefore either retain at least linearly many off-dyadic integers per octave, use measurements that do not factor through sparse point values, or rely essentially on the physical nonnegative/source-coherent coefficient class. Merely sprinkling additional off-dyadic checkpoints onto the existing switched grid cannot control signed repairs.

## Prior-art / novelty audit

The cellwise sign choice is a one-dimensional discrepancy-balancing argument, and general prefix/vector discrepancy is a substantial classical and modern literature. No novelty claim is made for that balancing principle. A targeted search of prefix-discrepancy and vector-balancing literature did not locate the specific line-local statement proved here: arbitrary sublinear prescribed zero sampling for the Mertens divisor-response transform together with retention of a fixed fraction of the natural linear coefficient capacity.

No external theorem is load-bearing beyond the standard totient identities already used in FD-231 and FD-238. The mathematical delta is the sampling-density obstruction obtained by combining independent exact-zero cells with the exact divisor-response inversion and the retained-capacity estimate.

## Status

**Proved.** The construction gives exact zeros on an arbitrary prescribed set with `o(2^k)` samples per dyadic band, uniform linear full-response control, the natural coefficient envelope, and macroscopic mass in both signs. It is a signed response-topology countermodel, not a physical nonnegative source and not an RH estimate.
