# MC-298 — Finite-order endpoint overlaps do not control high-cardinality Page parity

**Status:** canonical finding  
**Evidence:** `CLASSICAL-MECHANISM + EXACT-DERIVED + NEGATIVE/OBSTRUCTION`

## Claim

Fix a Page family of `m` endpoint-defect sets `D_1,...,D_m`, and let

\[
K(x)=\sum_{i=1}^m \mathbf 1_{D_i}(x)
\]

be the endpoint-defect multiplicity. The Page sign is `(-1)^K`, so its negative mass is

\[
q=\Pr(K\text{ odd})=\frac{1-\mathbf E[(-1)^K]}2.
\]

For every fixed order `r<m`, knowledge of all symmetric endpoint intersections through order `r` does **not** determine `q`. Equivalently, no bounded hierarchy of low-order overlap statistics can by itself control the parity of a high-cardinality Page mode.

This strengthens the pair-overlap obstruction in `MC-297`: pairwise information is only the `r=2` case of a general finite-order parity barrier.

## Exact exchangeable reduction

Consider an exchangeable finite endpoint system obtained by first drawing an integer-valued random variable

\[
K\in\{0,1,\dots,m\},
\]

and then, conditional on `K=k`, choosing uniformly a `k`-subset of `{1,...,m}` as the active defect set.

For distinct indices `i_1,...,i_j`,

\[
\Pr(i_1,\dots,i_j\text{ are all active})
=\frac{\mathbf E[(K)_j]}{(m)_j},
\]

where `(K)_j=K(K-1)\cdots(K-j+1)` is the falling factorial. Thus all symmetric `j`-fold endpoint intersections through order `r` are exactly equivalent to the factorial moments

\[
\mathbf E[(K)_j],\qquad 0\le j\le r.
\]

By contrast, Page parity is the full-degree observable `(-1)^K`.

## Explicit three-source witness

Take `m=3`. Define two laws on `K=0,1,2,3`:

\[
A=(1/6,\ 1/2,\ 0,\ 1/3),
\qquad
B=(1/3,\ 0,\ 1/2,\ 1/6).
\]

Both satisfy

\[
\mathbf E[K]=\frac32,
\qquad
\mathbf E[K(K-1)]=2.
\]

Hence every individual defect set has density `1/2`, every pair has overlap `1/3`, the total source cost is

\[
D=\frac32,
\]

and the total pair overlap is

\[
B=1.
\]

Nevertheless,

\[
\mathbf E_A[(-1)^K]= -\frac23,
\qquad
\mathbf E_B[(-1)^K]= +\frac23,
\]

so

\[
q_A=\frac56,
\qquad
q_B=\frac16.
\]

Identical one-way and pairwise endpoint statistics therefore coexist with a `2/3` difference in negative Page mass.

## General finite-order construction

Fix `r\ge0` and define, for `0\le k\le r+1`,

\[
v_k=(-1)^k\binom{r+1}{k}.
\]

The `(r+1)`-st finite-difference identity gives

\[
\sum_{k=0}^{r+1} v_k P(k)=0
\]

for every polynomial `P` of degree at most `r`. In particular,

\[
\sum_k v_k (k)_j=0,
\qquad 0\le j\le r.
\]

But parity is not annihilated:

\[
\sum_{k=0}^{r+1} v_k(-1)^k
=\sum_{k=0}^{r+1}\binom{r+1}{k}
=2^{r+1}.
\]

Choose any strictly positive probability vector `p=(p_0,...,p_{r+1})`. For sufficiently small rational `\varepsilon>0`,

\[
p^{\pm}_k=p_k\pm\varepsilon v_k
\]

remain probability vectors. They have identical factorial moments through order `r`, hence identical symmetric endpoint intersections through order `r`, while their parity expectations differ by

\[
2\varepsilon\,2^{r+1}.
\]

For any `m\ge r+1`, embedding these laws in the exchangeable `m`-source construction yields two endpoint systems indistinguishable by every intersection statistic of order at most `r` but with different Page negative mass.

Because the probabilities can be rational, the construction can be realized exactly on a finite deterministic atom space; the obstruction does not rely on a probabilistic heuristic.

## Consequence for the current frontier

`MC-297` showed that pair overlap plus the available Landau/Page estimates can collapse low-source-cost negative spectrum but leaves high-source-cost/high-multiplicity Page modes alive. The present result rules out a generic repair by simply adding **any fixed finite number of higher-overlap levels**.

If the selected Page cardinality grows, an overlap hierarchy of bounded order can remain blind to the parity observable. A successful arithmetic argument therefore needs at least one of:

- interaction information whose effective order grows with the Page cardinality;
- an exact arithmetic identity linking low-order overlaps to the full parity observable;
- structural restrictions on the actual Möbius defect sets that exclude the moment-matched controls above;
- a different observable that detects the surviving high-cost negative modes without reconstructing parity from bounded-order marginals.

This narrows the search target from “add more overlap information” to “find arithmetic rigidity that defeats the finite-order parity barrier.”

## Prior-art audit

The mechanism itself is classical. In probability/combinatorics, exchangeable Bernoulli systems encode `j`-way intersections by factorial moments of the count variable. In Boolean/Fourier language, parity is a top-degree Walsh character and is invisible to bounded low-degree moment or marginal information; `k`-wise information need not determine full parity. The binomial finite-difference vector used above is the elementary moment-matching certificate for that phenomenon.

The contribution here is the exact specialization to the endpoint/Page framework of `MC-297` and the resulting no-go statement for the current Möbius-cancellation frontier. No novelty is claimed for the underlying moment/parity fact.

## Boundaries

This is a matched-control obstruction, not a theorem that the actual Möbius endpoint defects are exchangeable or realize these laws. It does not show that arithmetic endpoint sets lack additional rigidity, nor does it imply anything directly about zeta zeros.

The conclusion is only that low-order endpoint intersections **alone** cannot generically certify Page parity. Any Möbius-specific escape must identify and prove extra arithmetic structure rather than infer it from finite-order overlap data.