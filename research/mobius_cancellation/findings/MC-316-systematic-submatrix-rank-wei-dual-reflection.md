# MC-316 — The half-rate endpoint is a systematic submatrix-rank condition, and dualization adds no independent coercivity

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `NEGATIVE/OBSTRUCTION` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the generic binary-code endpoint isolated in `MC-313`–`MC-315`. Let

\[
C\le \mathbf F_2^{2R},\qquad \dim C=R,
\]

and write `d_j(C)` for its generalized Hamming weights. Fix integers

\[
1\le t,\qquad a\ge0,\qquad t+a+1\le R.
\]

After a coordinate permutation choose a systematic parity-check matrix

\[
H=[I_R\mid P],\qquad P\in \mathbf F_2^{R\times R}.
\tag{1}
\]

Then the following three conditions are equivalent:

\[
\boxed{d_t(C)\ge R-a,}
\tag{2}
\]

\[
\boxed{
\operatorname{rank} Q\ge g-t+1
\quad\text{for every }t\le g\le R-a-1
\text{ and every }(g+a+1)\times g\text{ submatrix }Q\text{ of }P,
}
\tag{3}
\]

and

\[
\boxed{d_{t+a+1}(C^\perp)\ge R+a+2.}
\tag{4}
\]

Thus the near-middle generalized-weight condition is not accompanied by an independent dual constraint. It is **exactly reflected** to a shifted generalized weight of the dual, and in systematic coordinates both sides impose the same rectangular-submatrix rank condition, seen through transposition.

For the exact-natural-scale frontier of `MC-314`–`MC-315`, put

\[
t=t_R:=\left\lceil2\log_2(R+1)\right\rceil,
\qquad a=2.
\]

Then

\[
\boxed{
 d_{t_R}(C)\ge R-2
 \iff
 \operatorname{rank}Q\ge g-t_R+1
 \ \forall Q\in\mathbf F_2^{(g+3)\times g},\ t_R\le g\le R-3,
 \iff
 d_{t_R+3}(C^\perp)\ge R+4,
}
\tag{5}
\]

where the middle quantifier ranges over **all actual submatrices of the one systematic matrix `P`**, not over arbitrary binary matrices of that size.

Equation `(5)` closes a tempting generic escape from `MC-315`: imposing the dual generalized-weight hierarchy, applying the same generalized-Griesmer machinery to the dual, or treating the primal and dual near-capacity erasure statements as two independent restrictions cannot by itself strengthen the endpoint. Any useful dual route must exploit additional **arithmetic meaning of the dual relations**, not generic code duality.

No estimate for `M(x)` follows.

## 1. Threshold generalized weight equals uniform rectangular rank

For a coordinate set `E`, let

\[
C(E):=\{c\in C:\operatorname{supp}(c)\subseteq E\}.
\]

By the definition of generalized Hamming weight,

\[
d_t(C)\ge R-a
\iff
\dim C(E)\le t-1
\quad\text{for every }|E|\le R-a-1.
\tag{6}
\]

It is enough to test sets of exactly `R-a-1` coordinates: if a smaller set supported a `t`-dimensional subcode, any extension to that size would support the same subcode.

Now let `|E|=R-a-1`. Suppose `E` uses `g` columns from the `P` half of `(1)` and `R-a-1-g` identity columns. Write `T` for the chosen `P` columns and `S` for the row indices of the chosen identity columns. Using those identity columns as pivots gives

\[
\operatorname{rank}H_E
=
|S|+\operatorname{rank}P_{S^c,T}.
\tag{7}
\]

Since

\[
|S^c|
=R-(R-a-1-g)
=g+a+1,
\tag{8}
\]

we obtain

\[
\dim C(E)
=|E|-\operatorname{rank}H_E
=g-\operatorname{rank}P_{S^c,T}.
\tag{9}
\]

Therefore `(6)` is equivalent to

\[
\operatorname{rank}P_{S^c,T}\ge g-t+1.
\tag{10}
\]

As `S` and `T` vary, `P_{S^c,T}` runs over every `(g+a+1)\times g` submatrix of `P`. For `g<t` the lower bound is automatic, so the nontrivial range is exactly the one in `(3)`. This proves `(2)\iff(3)`.

The specialization `a=2` is especially concrete: every `g` chosen columns must retain rank at least `g-t_R+1` after restricting to **any** `g+3` chosen rows. The diagonal projective-cap problem of `MC-315` can therefore be attacked equivalently as an existence/nonexistence problem for an `R\times R` binary systematic matrix with this uniform rank profile.

## 2. Wei duality reflects the endpoint exactly

Wei's generalized-weight duality says that for an `[n,k]` linear code

\[
\{d_i(C):1\le i\le k\}
\sqcup
\{n+1-d_j(C^\perp):1\le j\le n-k\}
=
\{1,\ldots,n\}.
\tag{11}
\]

For `n=2R`, condition `(2)` says that among the integers

\[
1,\ldots,R-a-1
\]

at most `t-1` can be weights of `C`. Hence at least

\[
(R-a-1)-(t-1)=R-a-t
\tag{12}
\]

of those integers must be reflected dual weights `2R+1-d_j(C^\perp)`. Such a reflected value is at most `R-a-1` exactly when

\[
d_j(C^\perp)\ge R+a+2.
\tag{13}
\]

Since the `R` dual generalized weights are strictly increasing, having at least `R-a-t` of them at or above `(13)` is equivalent to saying that at most `a+t` lie below that threshold, namely

\[
d_{t+a+1}(C^\perp)\ge R+a+2.
\]

This proves `(2)\iff(4)`. The converse is the same count reversed; no asymptotic input is involved.

The systematic calculation makes the lack of independence even more explicit. A generator matrix for `C` may be taken as `[P^T\mid I_R]` over `\mathbf F_2`, so after swapping the two coordinate halves a systematic parity-check matrix for `C^\perp` is `[I_R\mid P^T]`. Testing `(4)` by shortened coordinate sets of size `R+a+1` yields, after writing `g'=g+a+1`,

\[
\operatorname{rank}(P^T)_{Q,T}\ge g'-t-a
=g-t+1,
\tag{14}
\]

on `g\times(g+a+1)` submatrices of `P^T`. Transposition turns `(14)` into exactly `(3)`. The apparent dual family is literally the same family of rectangular rank tests.

## 3. The erasure-capacity picture is mirrored, not doubled

At `a=2`, `d_{t_R}(C)\ge R-2` means every erasure set of size at most `R-3` leaves shortened-code dimension at most `t_R-1`. Thus the worst compatible list size is at most

\[
2^{t_R-1}<(R+1)^2,
\tag{15}
\]

at erasure fraction

\[
\frac{R-3}{2R}=\frac12-\frac{3}{2R}.
\tag{16}
\]

The dual reflection `(5)` says simultaneously that every erasure set of size at most `R+3` in `C^\perp` leaves ambiguity dimension at most `t_R+2`, hence list size at most

\[
2^{t_R+2}<8(R+1)^2,
\tag{17}
\]

at erasure fraction

\[
\frac{R+3}{2R}=\frac12+\frac{3}{2R}.
\tag{18}
\]

The above-capacity appearance of `(18)` is not a contradiction. With `R+3` erasures only `R-3` symbols remain, so `2^R` codewords are mapped into only `2^{R-3}` received strings: the **average** list size is already `8`. The allowed polynomial list in `(17)` easily accommodates that constant overshoot. Hence capacity bookkeeping cannot turn the dual statement into a new impossibility theorem.

This also explains why the primal and dual list conditions should not be multiplied as though they were independent rare events. They are one Wei-dual threshold expressed on opposite sides of the half-rate erasure boundary.

## 4. Reapplying generalized Griesmer to the dual gives the same collapse

`MC-313` showed that the binary generalized Griesmer bound collapses to generalized Singleton whenever the tested generalized weight is below `2^r-1`. At the reflected dual index

\[
r=t_R+3,
\]

we have trivially

\[
d_r(C^\perp)\le2R,
\]

while

\[
2^{t_R+3}\ge8(R+1)^2.
\tag{19}
\]

Thus `d_r(C^\perp)<2^r-1` by a huge margin for large `R`. Generalized Griesmer therefore again reduces to Singleton and supplies no extra redundancy. Combining the reflected lower bound `d_r(C^\perp)\ge R+4` with Singleton yields only

\[
2R\ge (R+4)+R-(t_R+3)=2R-t_R+1,
\tag{20}
\]

which is automatic.

So the route "apply the higher-weight bound to both `C` and `C^\perp`" does not repair the failure found in `MC-313`: Wei duality identifies the two threshold statements, and the same parameter regime makes the generic bound non-coercive on both sides.

## 5. Prior-art boundary

Nothing in the coding mechanism above is claimed as new. Generalized Hamming weights and their duality were introduced by V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412–1418, DOI `10.1109/18.133259`. The partition identity `(11)` is the classical Wei-duality theorem.

The systematic-matrix language is also established prior art. G. Viswanath and B. Sundar Rajan, *Matrix characterization of linear codes with arbitrary Hamming weight hierarchy*, Linear Algebra and its Applications 412 (2006), 396–407, DOI `10.1016/j.laa.2005.07.008`, characterize arbitrary generalized-weight hierarchies by ranks of rectangular submatrices of a systematic check matrix and use the generalized Singleton defects

\[
\mu_i(C)=n-k+i-d_i(C).
\]

The derivation `(6)`–`(10)` is included because the Mathia endpoint needs only one threshold inequality, so the exact `a,t,R` dependence is clearer from a direct shortening calculation than from importing their full hierarchy theorem. `MC-S49`–`MC-S53` remain the neighboring stored anchors for generalized weights, erasure list decoding, Griesmer bounds, and projective systems.

The durable Mathia delta is therefore **not** a new coding theorem. It is the exact specialization of classical machinery to the diagonal endpoint of `MC-314`–`MC-315`: the projective-cap target has a single systematic rectangular-rank representation, and the most obvious proposed extra generic constraint—its dual hierarchy—is already the same condition.

## Boundaries and falsification tests

- **The exact-natural-scale source hypothesis remains hypothetical.** `MC-314` explains what `Z\le y^{1/R}` would force; this finding does not prove that source cap.
- **The result does not settle the matrix/projective existence problem.** It neither constructs nor rules out an `R\times R` binary `P` satisfying `(5)` for unbounded `R`.
- **Systematic form loses no coding invariant.** The coordinate permutation used to put a parity check in form `[I\mid P]` preserves generalized Hamming weights. The rectangular condition is representation-dependent in appearance but equivalent to the invariant statement `(2)`.
- **Dual arithmetic structure could still matter.** What is closed is a *generic* dual-weight escape. If `C^\perp` has an independently proved arithmetic interpretation imposing restrictions beyond its generalized weights, those restrictions are not contained in Wei duality and remain a legitimate route.
- **The matrix condition is not ordinary MDS superregularity.** Here an `O(\log R)` rank defect is permitted and the tested blocks are rectangular. Results about all square minors being nonzero cannot be imported without an exact parameter translation.
- **Primal and dual erasure statements are not independent controls.** Any probabilistic or capacity argument multiplying their likelihoods double-counts the same weight-hierarchy information.
- **No RH or Mertens estimate follows.** This is a matched-control/frontier reduction inside the reciprocal source-incidence program.

## Consequence for the research line

`MC-315` reduced the exact-natural-scale generic control to a diagonal projective generalized-cap question. The present result removes a natural but redundant way of trying to strengthen it. There is no second generic constraint hiding in `C^\perp`: at half rate the constant-defect threshold reflects exactly through Wei duality and becomes the transpose of the same systematic rank condition.

The generic matched-control frontier can therefore be stated in a more concrete form. For

\[
t_R=\lceil2\log_2(R+1)\rceil,
\]

decide whether there exist binary matrices `P_R\in\mathbf F_2^{R\times R}` for unbounded `R` such that **every** `(g+3)\times g` submatrix has rank at least `g-t_R+1` for `t_R\le g\le R-3`. A construction settles the generic side in favor of compatibility; a universal obstruction settles it against compatibility.

Until that matrix/projective problem is resolved, generic duality, a second generalized-Griesmer pass, and mirrored erasure-capacity bookkeeping should be treated as closed reformulations rather than new escape routes. Any stronger route must either exploit a genuinely sharper binary submatrix-rank theorem or return to the arithmetic realizability of the lower-prime source columns.