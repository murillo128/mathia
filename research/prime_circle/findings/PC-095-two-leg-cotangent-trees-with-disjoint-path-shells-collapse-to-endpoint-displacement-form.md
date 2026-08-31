# PC-095 — two-leg cotangent trees with disjoint path shells collapse to endpoint displacement form

**Status:** `EXACT-DERIVED` + `STRUCTURAL-COLLAPSE` + `DECISIVE-BOUNDARY` for finite acyclic two-external-leg networks built from the intrinsic Prime-Circle cotangent kernel and arbitrary shell-local scalar weights, under the precise hypothesis that the exact-order shells occurring on the unique exposed path are pairwise disjoint. The same conclusion holds for a direct return whose two exposed shell sets coincide, provided every internal path shell is pairwise disjoint and disjoint from that endpoint shell.

Off-path shell labels may repeat: tree contraction only turns each off-path subtree into a scalar message at its attachment point. What is essential for the final PC-092 reduction is that the **serial path itself** satisfies PC-092's disjointness hypotheses. Reusing an exact-order shell at two nonadjacent vertices of the exposed path is not covered here and remains a repeated-shell/coincidence boundary.

## 1. Two exposed legs reduce every off-path branch to a scalar message

For distinct unit-circle points use the oriented Prime-Circle cotangent kernel

\[
K(z,w)=i\cot\!\left(\frac{\theta_z-\theta_w}{2}\right)
=-\frac{z+w}{z-w},
\qquad K(z,z)=0.
\]

Let `T=(V,E)` be a finite tree. Assign to each vertex `v` a finite root set `S_v` and a scalar profile

\[
f_v:S_v\to\mathbb C.
\]

Adjacent sets are assumed disjoint so every edge kernel is nonsingular. Choose two exposed vertices `a,b`. Because `T` is a tree, there is a unique path

\[
a=v_0,v_1,\ldots,v_m=b.
\]

Remove the path edges. Every remaining connected component is a rooted tree attached to exactly one path vertex. Orient each such component toward its attachment. For a branch vertex `v` with parent `p`, define recursively

\[
\boxed{
M_{v\to p}(x_p)
=
\sum_{x_v\in S_v}
K(x_p,x_v)\,f_v(x_v)
\prod_{c\in\operatorname{ch}(v)}M_{c\to v}(x_v).
}
\]

At a leaf the empty product is `1`. After all variables below `v` are summed, the entire branch therefore contributes **one scalar function of the parent coordinate**. This uses only finiteness and tree topology; it does not require shell labels in different branches to be distinct from one another.

For each path vertex define the effective one-body weight

\[
g_j(x)=f_{v_j}(x)
\prod_{c\in\mathcal B_j}M_{c\to v_j}(x),
\]

where `\mathcal B_j` denotes the off-path branches attached at `v_j`. The functions `g_j` may be arithmetically complicated. They can contain nested chord/cotangent sums, products of earlier messages, or repeated off-path shell information. None of that changes their one-variable character.

## 2. The remaining network is exactly a weighted serial word

After all off-path components are contracted, finite Fubini rearrangement gives

\[
\boxed{
\mathcal T_{a,b}
=
D_{g_0}
K_{S_{v_0},S_{v_1}}
D_{g_1}
K_{S_{v_1},S_{v_2}}
\cdots
D_{g_{m-1}}
K_{S_{v_{m-1}},S_{v_m}}
D_{g_m}.
}
\]

No branching tensor remains. Branching has only renormalized the scalar weights along the exposed path.

PC-092 proves that a finite serial word of the canonical cotangent blocks with arbitrary intermediate diagonal weights lies in the endpoint-displacement class when the shell sets along the path are pairwise disjoint. For disjoint endpoints `A,C`, that class is

\[
\mathcal E(A,C)
=
\left\{
\sum_{j=1}^{r}D_{a_j}K_{A,C}D_{c_j}
+
\sum_{k=1}^{t}u_kv_k^{\mathsf T}
\right\}.
\]

For a return `A=C`, PC-092 allows the corresponding endpoint diagonal correction.

Therefore, if

\[
S_{v_0},S_{v_1},\ldots,S_{v_m}
\]

are pairwise disjoint, then

\[
\boxed{
\mathcal T_{a,b}
\in
D_{g_0}\,\mathcal E(S_a,S_b)\,D_{g_m}.
}
\]

If `S_a=S_b` is a direct return and every internal path shell is pairwise disjoint and disjoint from `S_a`, the same conclusion holds with PC-092's return-diagonal extension.

Thus every finite two-leg cotangent tree in this precisely stated class is a finite sum of endpoint-weighted copies of the direct endpoint cotangent block plus separable rank-one corrections, and endpoint-local diagonals in the return case. **No hidden off-path shell index survives.**

## 3. The Y-branch illustrates what branching can and cannot add

Take a path `A-B-C` and attach an extra shell `D` to `B`. With local weights `f_B` and `h_D`,

\[
\mathcal Y(a,c)
=
\sum_{b\in B}\sum_{u\in D}
 f_B(b)h_D(u)
 K(a,b)K(b,c)K(b,u).
\]

The branch contributes the scalar message

\[
m_D(b)=\sum_{u\in D}h_D(u)K(b,u),
\]

so identically

\[
\boxed{
\mathcal Y
=K_{A,B}D_{f_Bm_D}K_{B,C}.
}
\]

When `A,B,C` are pairwise disjoint, PC-092 then gives

\[
\boxed{
\mathcal Y
=D_{T_B(f_Bm_D)|_A}K_{A,C}
-K_{A,C}D_{T_B(f_Bm_D)|_C}
-s_B(f_Bm_D)J_{A,C}.
}
\]

The branch can make the one-body profile `m_D` highly nontrivial, but it does not create a new two-leg matrix species.

## 4. Why path-shell disjointness is the exact hypothesis needed here

The message-passing step and the endpoint-displacement step use different hypotheses.

- Off-path contraction needs only that each actual tree edge joins disjoint point sets so its cotangent factor is defined.
- PC-092's iterative weighted two-hop reduction requires the serial shell sets being eliminated to be disjoint from the relevant endpoint sets. Pairwise disjointness along the exposed path guarantees this at every step.
- If the exposed path revisits the same exact-order shell at nonadjacent vertices, later reductions can encounter coincidence strata or repeated poles. The special `A=C` return identity in PC-092 handles a direct return, but it does not by itself classify arbitrary repeated internal path shells.

Hence the valid implication is

\[
\boxed{
\text{finite two-leg tree}
+
\text{PC-092-compatible exposed path}
\Longrightarrow
\text{endpoint displacement}.
}
\]

There is no claim here for arbitrary repeated-shell paths.

## 5. Prime-blind matched control

Neither the branch-message reduction nor the PC-092 cotangent identity uses primality. The same proof works for matched generic finite unit-circle sets satisfying the same disjointness pattern.

For Prime Circle, take path vertices from pairwise distinct exact-order shells `P_{n_j}^*`. Primality can change the values of the scalar branch messages or endpoint transforms, but it does not change the composition law. A prime discriminator would therefore have to be extracted later from the surviving endpoint profiles or from a construction outside this finite two-leg disjoint-path class.

No spectral parameter, functional equation, gamma factor, critical-line selector, or new zeta divisor is produced.

## 6. Relation to the multileg boundary

PC-094 uses Hermite's arbitrary-valence cotangent identity to prove a complementary statement: when **all** shell sets in a finite cotangent tree are pairwise disjoint, any number of exposed legs can be reduced to a weighted forest algebra on those exposed variables.

The two results have different strengths.

- PC-095 permits repeated shell labels in off-path branches and gives the stronger PC-092 endpoint-displacement normal form, but only for two exposed legs and a PC-092-compatible path.
- PC-094 handles arbitrary exposed valence, but states the clean theorem under global pairwise disjointness and leaves repeated-shell/coincidence cases outside its scope.

Together they close the ordinary finite acyclic cotangent-tree route under the disjointness hypotheses actually proved, without claiming a theorem for repeated internal shell paths.

## 7. Prior-art and novelty audit

No historical novelty is claimed for the abstract tree-contraction mechanism.

- Exact inward message passing on cycle-free factor graphs is standard; see F. R. Kschischang, B. J. Frey and H.-A. Loeliger, **Factor Graphs and the Sum-Product Algorithm**, *IEEE Transactions on Information Theory* 47:2 (2001), 498–519, DOI `10.1109/18.910572`.
- The endpoint-displacement step is the Prime-Circle-specific exact cotangent algebra already established in PC-092, itself tied to classical Cauchy-like/displacement structure.
- PC-094 supplies the classical Hermite cotangent identity as the arbitrary-valence local elimination law under global disjointness.

The durable contribution is the precise research boundary: **two-leg acyclic branching does not evade PC-092 when the exposed path satisfies PC-092's actual disjointness domain.** Repeated path shells are explicitly not promoted from an unproved case to a theorem.

## 8. Falsification controls

1. Contract every off-path subtree directly and by recursive messages; the results must agree pointwise.
2. Verify that the contracted network is exactly the weighted serial word in Section 2.
3. On pairwise-disjoint path shells, recursively apply PC-092 and compare with brute-force summation.
4. Repeat with non-prime finite unit-circle controls satisfying the same disjointness pattern; the structural reduction must be unchanged.
5. Do **not** use a repeated nonadjacent path shell as a positive test of this theorem. Such a configuration lies outside the stated domain unless separately reduced by a new overlap/repeated-pole argument.

A counterexample within the pairwise-disjoint path domain refutes the endpoint-displacement claim. A repeated-shell counterexample does not: it tests the deliberately excluded boundary.