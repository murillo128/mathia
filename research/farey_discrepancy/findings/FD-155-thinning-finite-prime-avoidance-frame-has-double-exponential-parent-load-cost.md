# FD-155 — Thinning the finite-prime avoidance frame has double-exponential parent-load cost

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact resource law / prime-coordinate anchor / source-exposure boundary
- **Depends on:** FD-151, FD-154

## Claim

FD-154 gives an exact coercive frame for every fixed finite prime-avoidance anchor, but leaves open how expensive that construction becomes if one tries to reduce the amount of Möbius source that must be anchored by using more prime coordinates. For the direct one-edge-per-child frame of FD-154, that tradeoff can be optimized exactly at finite coordinate count and asymptotically across the fixed-coordinate family.

Let `S` be a nonempty finite set of primes, write

\[
\Pi_S:=\prod_{p\in S}p,
\qquad s:=|S|,
\]

and retain the notation of FD-154:

\[
V_T=\{n\le T:\mu^2(n)=1\},
\qquad
D_{S,T}=\{n\in V_T:(n,\Pi_S)=1\},
\qquad
R_{S,T}=V_T\setminus D_{S,T}.
\]

For each `m in R_(S,T)`, the direct frame uses the edge

\[
(c_S(m),m),
\qquad
c_S(m)=\frac{m}{(m,\Pi_S)},
\]

with uniform edge mass `1/|R_(S,T)|`. Define the minimal parent-distortion constant of this specific edge measure by

\[
P^*_{S,T}
:=
\max_{d\in D_{S,T}}
\frac{\eta^-_{S,T}(d)}{\nu_T(d)},
\qquad
\nu_T(d)=|V_T|^{-1}.
\tag{1}
\]

Then for every fixed `S` and every `T>=Pi_S`,

\[
\boxed{
P^*_{S,T}
=(2^s-1)\frac{|V_T|}{|R_{S,T}|}.
}
\tag{2}
\]

Thus the upper bound in FD-154 is sharp for its direct frame. Since

\[
a(S)
:=
\lim_{T\to\infty}\nu_T(D_{S,T})
=
\prod_{p\in S}\frac{p}{p+1},
\tag{3}
\]

we have the fixed-`S` limit

\[
\boxed{
P^*(S)
:=
\lim_{T\to\infty}P^*_{S,T}
=
\frac{2^s-1}{1-a(S)}.
}
\tag{4}
\]

Now let `p_1<p_2<...` be the primes, let

\[
S_s:=\{p_1,\ldots,p_s\},
\qquad
a_s:=a(S_s),
\tag{5}
\]

and, for `alpha downarrow 0`, define the least prime-coordinate count needed to expose at most an `alpha` fraction of the squarefree coefficient mass,

\[
s_\alpha
:=
\min\{s:a_s\le\alpha\}.
\tag{6}
\]

Among all prime sets of cardinality `s`, `S_s` minimizes the anchor density. Moreover the prime number theorem gives

\[
\boxed{
a_s=(\log s)^{-1+o(1)}}
\tag{7}
\]

and hence

\[
\boxed{
s_\alpha=\exp\!\bigl(\alpha^{-1+o(1)}\bigr).}
\tag{8}
\]

Finally define the best limiting parent distortion obtainable **within the FD-154 direct prime-avoidance frames** at anchor exposure at most `alpha`:

\[
\mathcal P_{\rm dir}(\alpha)
:=
\inf\{P^*(S):0<a(S)\le\alpha\}.
\tag{9}
\]

Then

\[
2^{s_\alpha}-1
\le
\mathcal P_{\rm dir}(\alpha)
\le
\frac{2^{s_\alpha}-1}{1-\alpha},
\tag{10}
\]

so

\[
\boxed{
\log\log \mathcal P_{\rm dir}(\alpha)
=
\alpha^{-1+o(1)},
}
\tag{11}
\]

or equivalently

\[
\boxed{
\mathcal P_{\rm dir}(\alpha)
=
\exp\!\left(\exp\!\bigl(\alpha^{-1+o(1)}\bigr)\right).
}
\tag{12}
\]

The direct ancestry depth also becomes expensive. For `T>=Pi_S` the child `Pi_S` is present and its direct edge from `1` has depth exactly `s`. Therefore the smallest possible maximal depth inside this same family under `a(S)<=alpha` is exactly `s_alpha`, hence singly exponential in `alpha^{-1+o(1)}`.

This is a resource theorem for the **specific positive construction of FD-154**, not a universal lower bound for every divisor-closed anchor or every possible ancestry edge measure. Its significance is that the most obvious attempt to reduce the macroscopic source exposure of FD-154 — add more avoided prime coordinates — does not make that construction cheap. It trades source mass for an exponentially growing coordinate/depth budget and a double-exponentially growing parent load.

## 1. The parent-load upper bound of FD-154 is attained at the root

FD-154 already proves

\[
P^*_{S,T}
\le
(2^s-1)\frac{|V_T|}{|R_{S,T}|}.
\tag{13}
\]

For the reverse inequality assume `T>=Pi_S`. Every nontrivial squarefree divisor `q` of `Pi_S` lies in `R_(S,T)` and has

\[
c_S(q)=1.
\]

There are exactly `2^s-1` such divisors. Each contributes one edge of mass `1/|R_(S,T)|` with parent `1`, so

\[
\eta^-_{S,T}(1)
=
\frac{2^s-1}{|R_{S,T}|}.
\tag{14}
\]

Since `1 in D_(S,T)` and `nu_T(1)=1/|V_T|`,

\[
\frac{\eta^-_{S,T}(1)}{\nu_T(1)}
=
(2^s-1)\frac{|V_T|}{|R_{S,T}|}.
\tag{15}
\]

Together with (13), this proves (2). Taking `T->infinity` and using the fixed-prime squarefree density from FD-154 proves (4).

The check at `s=1` recovers the exact one-prime identity of FD-154. For `S={2,3}`, for example, `a(S)=1/2`; asymptotically the Cheeger and child constants are `2`, while the direct-frame parent distortion is `3*2=6`.

## 2. The first `s` primes are the optimal coordinates for thinning the anchor

Write an arbitrary `s`-element prime set as

\[
S=\{q_1<\cdots<q_s\}.
\]

Then `q_j>=p_j` for every `j`. The function

\[
p\mapsto\frac{p}{p+1}
\]

is strictly increasing, so

\[
a(S)
=
\prod_{j=1}^s\frac{q_j}{q_j+1}
\ge
\prod_{j=1}^s\frac{p_j}{p_j+1}
=a_s.
\tag{16}
\]

Thus primorial coordinate sets minimize the anchored coefficient mass at fixed coordinate count. This extremality is elementary; no probabilistic prime-factor law is involved.

Consequently any `S` with `a(S)<=alpha` must satisfy `|S|>=s_alpha`. Conversely `S_(s_alpha)` is admissible. Substituting (4) gives immediately

\[
P^*(S)
\ge
2^{|S|}-1
\ge
2^{s_\alpha}-1,
\tag{17}
\]

whereas

\[
P^*(S_{s_\alpha})
=
\frac{2^{s_\alpha}-1}{1-a_{s_\alpha}}
\le
\frac{2^{s_\alpha}-1}{1-\alpha}.
\tag{18}
\]

This proves the sharp two-sided optimization (10) without any asymptotic prime-distribution input.

## 3. PNT turns coordinate count into an explicit source-exposure scale

The only asymptotic input needed for (7)--(12) is the prime number theorem already anchored in this line. In its standard `n`-th-prime form,

\[
p_j=(1+o(1))j\log j.
\tag{19}
\]

Because the comparison series diverges,

\[
\sum_{j\le s}\frac1{p_j}
=
(1+o(1))
\sum_{2\le j\le s}\frac1{j\log j}
=
(1+o(1))\log\log s.
\tag{20}
\]

Also `sum_p 1/p^2<infinity`, so expanding `log(1+1/p)` gives

\[
\begin{aligned}
-\log a_s
&=
\sum_{j\le s}\log\left(1+\frac1{p_j}\right)\\
&=
\sum_{j\le s}\frac1{p_j}+O(1)\\
&=
(1+o(1))\log\log s.
\end{aligned}
\tag{21}
\]

Exponentiating proves (7).

At the threshold in (6),

\[
a_{s_\alpha}\le\alpha<a_{s_\alpha-1}.
\tag{22}
\]

The ratio of consecutive values is

\[
\frac{a_{s-1}}{a_s}
=1+\frac1{p_s}
\longrightarrow1,
\tag{23}
\]

so the threshold jump is asymptotically negligible. Equations (7), (22), and (23) imply

\[
\log s_\alpha
=
\alpha^{-1+o(1)},
\tag{24}
\]

which is (8). Combining this with (10) gives

\[
\log \mathcal P_{\rm dir}(\alpha)
=(\log2+o(1))s_\alpha,
\]

and hence (11)--(12).

The classical Mertens prime-product theorem can sharpen (7) to an explicit leading constant, but that refinement is not needed for the double-exponential resource law and is not imported as a dependency here.

## 4. What resource is actually being spent

The striking feature is that coercivity itself does not deteriorate as the anchor is thinned. For every fixed `S`, FD-154 gives

\[
h_{D_{S,T}}
=K_{S,T}
\longrightarrow
\frac1{1-a(S)}.
\tag{25}
\]

Along the optimized family with `a(S)<=alpha->0`, this tends to `1`. The exact `L^q` Dirichlet frame therefore stays strong. What blows up is the architecture needed to realize it: the number of avoided prime coordinates, the maximal direct ancestry depth, and especially the root parent load.

This sharpens the source-information warning at the end of FD-154. A fixed one-prime face is cheap geometrically but anchors a positive fraction of all squarefree coefficients. Adding prime coordinates can make that anchored fraction arbitrarily small, but the best coordinate set needs

\[
s_\alpha=\exp(\alpha^{-1+o(1)})
\]

coordinates, and the uniform direct frame then pays roughly `2^(s_alpha)` parent distortion. Thus "use more prime coordinates" is not a low-cost route from the macroscopic anchor of FD-154 to a sparse-source construction.

This also complements, rather than supersedes, FD-151. FD-151 gives the universal complement-cut lower bound `P_T >= c(1-p_T)/p_T` for any divisor-closed anchor with positive expansion. FD-155 is much stronger only because it fixes the concrete direct prime-avoidance frame of FD-154. A different edge measure or a different Farey-native anchor may avoid the double-exponential load; no contrary claim is made.

## 5. Consequence for the current Farey frontier

The live question after FD-154 was whether a Farey-native observable could provide the required anchored orientation without already reconstructing Möbius. FD-155 does not solve that provenance problem, but it removes one tempting way of weakening it.

Within the finite-prime coordinate-face mechanism, there is no smooth interpolation from "anchor a macroscopic coefficient fraction" to "anchor very little" while retaining all other resources at moderate scale. The optimized family has the asymptotic hierarchy

\[
\text{anchor mass }\alpha
\quad\Longrightarrow\quad
\text{prime-coordinate/depth budget }
\exp(\alpha^{-1+o(1)})
\quad\Longrightarrow\quad
\text{direct parent load }
\exp\!\left(\exp(\alpha^{-1+o(1)})\right).
\tag{26}
\]

Therefore a useful next anchor proposal should not merely enlarge `S`. It must either obtain a macroscopic face from genuinely compressed Farey information, replace the uniform direct frame by a substantially better-conditioned ancestry measure, or use a different divisor-closed geometry whose source exposure and endpoint distortion obey a better joint law. In every case the map to the Franel--Landau destination remains a separate gate.

## 6. Prior-art, scope, and falsification boundary

The ingredients used here are classical: the prime number theorem, the finite-prime squarefree density already proved in FD-154, and the elementary fact that the first `s` primes extremize products of increasing one-prime factors. A literature audit also finds the expected Mertens prime-product and Dedekind-psi/primorial extremal literature; no novelty is claimed for those prime products or for primorial extremality. The present result derives its new content from coupling that elementary coordinate optimization to the exact parent marginal of the FD-154 ancestry frame. No new external theorem beyond the PNT already recorded in `SOURCES.md` is load-bearing, so no source-anchor update is required.

The order of limits is essential. For each finite `S`, equations (2)--(4) take `T->infinity`; only afterwards do (5)--(12) compare the resulting fixed-coordinate frames as `s->infinity` or `alpha->0`. No uniform theorem for a simultaneously growing set `S=S_T` is asserted.

The finding is falsified if the root `1` does not have exactly `2^s-1` direct children once `T>=Pi_S`, if an `s`-element prime set can have smaller anchor density than the first `s` primes, or if (19)--(21) fail to imply (7). It must not be cited as a lower bound for arbitrary edge measures on the same anchor, as a proof that every sparse Farey-native anchor has double-exponential distortion, as evidence that the anchor provenance problem is solved, or as an RH-strength discrepancy estimate.
