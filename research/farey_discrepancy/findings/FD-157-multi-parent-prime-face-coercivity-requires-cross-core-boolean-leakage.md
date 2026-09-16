# FD-157 — Multi-parent prime-face coercivity requires cross-core Boolean leakage

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact obstruction / multi-parent boundary / prime-coordinate mixing law
- **Depends on:** FD-151, FD-154, FD-155, FD-156

## Claim

FD-156 leaves genuinely multi-parent divisibility geometry as the main architecture escape on the finite-prime avoidance anchor. Multiple parents do remove the tree-branch argument used there, but they do not by themselves remove the Boolean packet obstruction. To beat the exponential prime-coordinate load, the edge measure must export a quantitatively comparable amount of boundary mass out of the pure `S`-coordinate fiber.

Retain

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
\nu_T(n):=|V_T|^{-1},
\tag{1}
\]

fix a nonempty finite set of primes `S`, and write

\[
P_S:=\prod_{p\in S}p,
\qquad
s:=|S|,
\qquad
D_{S,T}:=\{n\in V_T:(n,P_S)=1\}.
\tag{2}
\]

Assume `T>=P_S` and put `R_(S,T)=V_T\setminus D_(S,T)`. Let `E_T^*` be an arbitrary positive directed divisibility relation on `V_T`: every edge is `(n,m)` with `n|m` and `n<m`. A child may have any number of parents. Let `eta_T` be any nonnegative probability measure on `E_T^*`, define

\[
h_{S,T}
:=
\inf_{\varnothing\ne A\subseteq R_{S,T}}
\frac{\eta_T(\partial A)}{\nu_T(A)},
\tag{3}
\]

and let the anchor-side parent distortion be

\[
P_{S,T}
:=
\max_{d\in D_{S,T}}
\frac{\eta_T^-(d)}{\nu_T(d)},
\qquad
\eta_T^-(d):=
\sum_{m:(d,m)\in E_T^*}\eta_T(d,m).
\tag{4}
\]

The pure `S`-coordinate packet is

\[
B_S:=\{q:q\mid P_S,\ q>1\},
\qquad
N_S:=|B_S|=2^s-1.
\tag{5}
\]

Define the cross-core edge set leaving that packet by

\[
E_{\rm mix}(S,T)
:=
\{(q,m)\in E_T^*:q\in B_S,\ m\notin B_S\},
\tag{6}
\]

and its coefficient-scale flux by

\[
L_{S,T}
:=
|V_T|\,\eta_T(E_{\rm mix}(S,T)).
\tag{7}
\]

Then every multi-parent architecture satisfies the exact resource inequality

\[
\boxed{
 h_{S,T}
 \le
 \frac{P_{S,T}+L_{S,T}}{2^s-1}.
}
\tag{8}
\]

Equivalently,

\[
\boxed{
P_{S,T}+L_{S,T}
\ge
h_{S,T}(2^s-1).
}
\tag{9}
\]

The new term is not an arbitrary correction. Every edge in `E_mix` necessarily changes the `S`-free core: its child contains at least one prime outside `S`. Consequently, if all nonanchor-to-nonanchor edges preserve

\[
c_S(n):=\frac{n}{(n,P_S)},
\tag{10}
\]

then `L_(S,T)=0`, and the sharp FD-156 law survives **without any one-parent hypothesis**:

\[
\boxed{
\frac{P_{S,T}}{h_{S,T}}
\ge
2^s-1.
}
\tag{11}
\]

Thus adding arbitrarily many parents inside each prime-coordinate fiber cannot improve the exponential expansion/load tradeoff. A genuine multi-parent escape must mix distinct `S`-free cores.

There is also a sharp anti-hub consequence under bounded child distortion. Write

\[
\eta_T^+(m)
:=
\sum_{n:(n,m)\in E_T^*}\eta_T(n,m)
\tag{12}
\]

and suppose

\[
\eta_T^+(m)\le K_{S,T}\nu_T(m)
\qquad(m\in R_{S,T}).
\tag{13}
\]

Let

\[
C_{\rm mix}(S,T)
:=
\{m\in R_{S,T}\setminus B_S:
\exists q\in B_S\text{ with }(q,m)\in E_T^*\}
\tag{14}
\]

be the set of cross-core recipient vertices. Then

\[
\boxed{
|C_{\rm mix}(S,T)|
\ge
\frac{\bigl(h_{S,T}(2^s-1)-P_{S,T}\bigr)_+}
{K_{S,T}}.
}
\tag{15}
\]

Hence if `h_(S,T)>=c>0`, `K_(S,T)<=K<infinity`, and `P_(S,T)=o(2^s)`, a multi-parent escape requires

\[
\boxed{
|C_{\rm mix}(S,T)|
\ge
\left(\frac cK-o(1)\right)2^s.
}
\tag{16}
\]

It cannot funnel the `2^s-1` pure Boolean states through a bounded or subexponential family of shared children while retaining bounded child distortion.

Combining (16) with the prime-coordinate thinning scale from FD-155 makes the architecture cost explicit. For the first-`s`-prime faces, reducing the limiting anchored coefficient mass to at most `alpha` requires

\[
s_\alpha=\exp\!\bigl(\alpha^{-1+o(1)}\bigr).
\tag{17}
\]

Therefore any family on that scale with fixed positive expansion, bounded child distortion, and `P=o(2^{s_alpha})` must use at least

\[
|C_{\rm mix}|
\ge
2^{s_\alpha+O(1)},
\tag{18}
\]

up to the fixed constants in (16), and in particular

\[
\boxed{
\log\log |C_{\rm mix}|
\ge
\alpha^{-1+o(1)}.
}
\tag{19}
\]

The interpretation is deliberately narrower than an impossibility theorem. Multi-parent mixing may still evade the FD-156 root-load obstruction when `T` supplies enough cross-core recipients. What (8)--(19) prove is that **multi-parent alone is not the resource**: bounded-distortion escape must export the full Boolean packet across `S`-free cores rather than merge it through a small core-preserving gadget.

## 1. The pure Boolean packet has only one possible incoming anchor

Take `q in B_S`. Every divisor of `q` is itself a divisor of `P_S`. If a divisor belongs to the prime-avoidance anchor, it contains no prime of `S`; the only such divisor is `1`.

Therefore any edge crossing into `B_S` from its complement must be

\[
(1,q)
\qquad(q\in B_S).
\tag{20}
\]

There is no second anchor vertex, no outside-core divisor, and no multi-parent mechanism that can create another incoming edge to a pure `S`-state. This is exactly the finite rigidity that powered FD-156, but now we do not partition the graph into tree branches.

Conversely, suppose an edge crosses out of `B_S`:

\[
(q,m),
\qquad q\in B_S,
\qquad m\notin B_S.
\tag{21}
\]

Since `q|m` and both vertices are squarefree, if every prime of `m` belonged to `S` then `m` would also divide `P_S` and would lie in `B_S`. Hence `m` must contain a prime outside `S`, so

\[
c_S(m)>1=c_S(q).
\tag{22}
\]

Thus every outgoing crossing edge is exactly a cross-core edge in the sense of (6).

Equations (20)--(22) give the exact boundary decomposition

\[
\boxed{
\eta_T(\partial B_S)
=
\sum_{\substack{q\in B_S\\(1,q)\in E_T^*}}
\eta_T(1,q)
+
\eta_T(E_{\rm mix}(S,T)).
}
\tag{23}
\]

No edge is missing from (23): an edge crossing the set either has its child in `B_S`, when (20) applies, or its parent in `B_S`, when (21)--(22) apply.

## 2. One Cheeger test gives the flux law

Because `1 in D_(S,T)`, the first term in (23) is bounded by the full parent marginal at `1`:

\[
\sum_{q\in B_S}\eta_T(1,q)
\le
\eta_T^-(1)
\le
\frac{P_{S,T}}{|V_T|}.
\tag{24}
\]

By definition of `L_(S,T)`, the second term is `L_(S,T)/|V_T|`. Also

\[
\nu_T(B_S)
=
\frac{2^s-1}{|V_T|}.
\tag{25}
\]

Testing `A=B_S` in (3), then using (23)--(25), gives

\[
\begin{aligned}
h_{S,T}
&\le
\frac{\eta_T(\partial B_S)}{\nu_T(B_S)}\\
&\le
\frac{P_{S,T}+L_{S,T}}{2^s-1},
\end{aligned}
\tag{26}
\]

which proves (8)--(9).

The coefficient `1` in front of both resources cannot be improved in this class. In the uniform direct star of FD-154, `E_mix` is empty and FD-155 gives

\[
P_{S,T}^{\rm dir}
=(2^s-1)K_{S,T},
\qquad
h_{S,T}^{\rm dir}=K_{S,T}.
\tag{27}
\]

Therefore equality holds in (8). The direct construction is still extremal for the packet cut; multi-parent geometry can improve its anchor load only by turning on the second resource in (9).

## 3. Core-preserving multi-parent DAGs do not help

Suppose every edge `(n,m)` with both endpoints outside the anchor satisfies

\[
c_S(n)=c_S(m).
\tag{28}
\]

For `q in B_S`, `c_S(q)=1`. Hence every nonanchor child `m` of `q` also has `c_S(m)=1`. A squarefree integer with `S`-free core `1` uses only primes from `S`, so it divides `P_S`; because it is larger than `q`, it remains in `B_S`.

Thus (28) implies

\[
E_{\rm mix}(S,T)=\varnothing,
\qquad
L_{S,T}=0.
\tag{29}
\]

Substitution into (8) proves (11). Notice that nothing here restricts the number of parents of a child, the number of edges between Boolean states, the ancestry depth, or the edge weights. Arbitrarily dense DAGs inside a fixed `S`-free fiber therefore obey exactly the same exponential `P/h` law as the optimal direct star.

This sharpens the architecture boundary after FD-156. The essential distinction is not tree versus DAG. It is **fiber-preserving versus core-mixing**. Tree structure forced the load even when cores could change; once multiple parents are allowed, the finite certificate survives exactly until edge mass is exported across the core quotient.

## 4. Bounded child distortion forbids a small mixing hub

Every edge in `E_mix` ends at a vertex of `C_mix`. Hence

\[
\eta_T(E_{\rm mix})
\le
\sum_{m\in C_{\rm mix}}\eta_T^+(m).
\tag{30}
\]

Under the child-marginal bound (13),

\[
\eta_T(E_{\rm mix})
\le
\frac{K_{S,T}|C_{\rm mix}|}{|V_T|},
\tag{31}
\]

or equivalently

\[
L_{S,T}
\le
K_{S,T}|C_{\rm mix}|.
\tag{32}
\]

Equation (9) gives

\[
L_{S,T}
\ge
\bigl(h_{S,T}(2^s-1)-P_{S,T}\bigr)_+.
\tag{33}
\]

Combining (32)--(33) proves (15). The result is a recipient-cardinality statement, not a degree statement: a single mixed child may have exponentially many pure parents, but bounded child distortion prevents it from absorbing exponentially many coefficient-scale units of edge mass.

This distinction matters for the most obvious multi-parent repair of FD-156. One may try to merge many pure Boolean states into a small collection of common multiples that also have anchor co-parents. Such diamond gadgets are permitted by divisibility and really do destroy the one-parent branch partition. Equations (15)--(16) show that, under the same bounded endpoint-conditioning philosophy used throughout FD-148--FD-156, a small shared hub cannot carry enough boundary mass. The repair must proliferate cross-core recipients on the same exponential state scale as the Boolean packet itself.

## 5. Thinning converts that packet scale into a double-exponential architecture scale

FD-155 already optimizes the anchor density at fixed coordinate count. If `S_s` is the set of the first `s` primes and

\[
a_s
:=
\prod_{p\in S_s}\frac{p}{p+1},
\tag{34}
\]

then

\[
a_s=(\log s)^{-1+o(1)},
\qquad
s_\alpha
:=
\min\{s:a_s\le\alpha\}
=
\exp\!\bigl(\alpha^{-1+o(1)}\bigr).
\tag{35}
\]

At coordinate count `s_alpha`, (16) requires a constant fraction of

\[
N_{S_{s_\alpha}}
=2^{s_\alpha}-1
\tag{36}
\]

cross-core recipients whenever expansion and child distortion stay bounded away from zero/infinity and the anchor parent load is `o(N)`. This proves (18)--(19) in the same fixed-coordinate-then-thinning asymptotic sense as FD-155.

The conclusion should not be confused with an information lower bound. The recipient vertices may be generated by a compact deterministic rule, and their cardinality alone does not count independent source bits or source-independent tests. FD-144's information-budget gate therefore remains separate. What is ruled out here is a specific geometric compression: one cannot thin the prime-coordinate anchor, retain bounded endpoint distortion and positive expansion, and then merge the pure Boolean packet through only a small number of cross-core states.

## 6. Prior art, scope, and falsification boundary

Weighted Dirichlet Cheeger constants and their relation to graph `p`-Laplacians are classical; a targeted literature audit found, for example, Bobo Hua and Lili Wang, *Dirichlet p-Laplacian eigenvalues and Cheeger constants on symmetric graphs*, Advances in Mathematics **364** (2020), 106997. Boolean-lattice and divisor-poset graph structures are likewise classical, with Sperner's theorem already anchored elsewhere in this line. None of those results is load-bearing here: the new statement is the finite boundary identity (23) and its resource consequences inside the FD-154 prime-face model.

The audit did not locate a published statement matching (8) or (15) in this Möbius prime-avoidance setting. Broad novelty is not claimed for taking a Cheeger cut or for Boolean-lattice combinatorics. No new external theorem is used, so `SOURCES.md` requires no additional anchor.

The hypotheses and limitations are material. The edge measure must be nonnegative; signed edge measures are outside the Cheeger framework used here. Equation (11) applies only when nonanchor edges preserve the `S`-free core. Equations (15)--(19) additionally require bounded child marginal distortion. Cross-core mixing is **not** proved impossible, expensive in raw global edge mass, or circular. The theorem does not show that the recipient count equals an information budget, does not supply the anchor orientation from Farey data, and does not transfer coefficient coercivity to the Franel--Landau discrepancy.

The finding is falsified if a divisibility edge can enter `B_S` from a vertex other than `1`, if an edge can leave `B_S` without changing the `S`-free core, if the direct FD-154 star fails to attain equality in (8), or if a bounded-child-marginal architecture violates (15). All four are finite structural checks.

## 7. Consequence for the current Farey frontier

FD-156 correctly identified multi-parent ancestry as the remaining architecture escape from its tree theorem, but `FD-157` makes that escape substantially narrower. **Multiple parents within the prime-coordinate fiber buy nothing.** To lower the anchor parent load while preserving expansion, the graph must couple the pure `S`-Boolean packet to vertices carrying primes outside `S`; with bounded child distortion it must do so across a recipient family of the same exponential cardinality as the packet.

The next useful architecture test is therefore not an arbitrary DAG on the Boolean coordinate cube. It is a genuinely cross-core construction, together with a proof that the induced core mixing remains well conditioned and that its required anchor/source data are available from a Farey-native observable without Möbius reconstruction. Only after that source-provenance gate is passed does the separate Franel--Landau destination problem become relevant.