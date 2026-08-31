# PC-093 — finite two-leg cotangent trees collapse to endpoint displacement form

**Status:** `EXACT-DERIVED` + `STRUCTURAL-COLLAPSE` + `DECISIVE-BOUNDARY` for finite acyclic two-external-leg networks built from the intrinsic Prime-Circle cotangent kernel, complete exact-order shells, and arbitrary shell-local scalar weights. PC-092 closed finite **serial** weighted cotangent paths but explicitly left branching tensors open. The theorem below closes the entire acyclic branching subclass whenever only two shell variables are retained: every off-path branch contracts to an ordinary scalar profile on the unique path, so the network becomes exactly a PC-092 serial word and hence lies in the same endpoint-displacement algebra.

This does **not** close genuinely multi-leg tensors, graphs with cycles, networks using a second intrinsic edge operator not reducible to the cotangent kernel, infinite-depth limits, Hardy/Hankel constructions, or global uniformization/monodromy. It also does not say that the effective endpoint profiles produced by branch contraction are arithmetically trivial. The exact obstruction is topological/algebraic: **finite tree memory with two exposed legs cannot retain an irreducible branching interior once arbitrary diagonal path weights are already allowed.**

## 1. The two-leg tree network

For distinct points `z,w` on the unit circle use the Prime-Circle oriented cotangent kernel

\[
K(z,w)
=
i\cot\!\left(\frac{\theta_z-\theta_w}{2}\right)
=
-\frac{z+w}{z-w},
\qquad K(z,z)=0.
\]

Let `T=(V,E)` be a finite tree. Assign to each vertex `v` a finite root set `S_v` and a scalar profile

\[
f_v:S_v\to\mathbb C.
\]

For the Prime-Circle specialization, take `S_v=P_{n_v}^*` with distinct exact orders along adjacent vertices, so adjacent root sets are disjoint. More generally the argument works for arbitrary finite disjoint unit-circle sets.

Choose two distinguished vertices `a,b in V` whose root variables are left uncontracted. Every other vertex is summed. The resulting two-leg kernel is

\[
\boxed{
\mathcal T_{a,b}(x_a,x_b)
=
\sum_{\{x_v\in S_v:\ v\neq a,b\}}
\left(\prod_{v\in V} f_v(x_v)\right)
\left(\prod_{\{u,v\}\in E}K(x_u,x_v)\right),
}
\]

where endpoint profiles `f_a,f_b` may be set to `1` or retained as left/right diagonal factors.

This is the canonical finite branching generalization of the serial shell words in PC-092: the same shell variable can now feed several cotangent edges before it is summed.

## 2. Every off-path branch is only a scalar message

Because `T` is a tree, there is a unique simple path

\[
a=v_0,v_1,\ldots,v_m=b.
\]

Remove the path edges. Every remaining connected component is a rooted finite tree attached to exactly one path vertex.

Orient such a component toward its attachment point. If `v` has parent `p`, define recursively the branch message

\[
\boxed{
M_{v\to p}(x_p)
=
\sum_{x_v\in S_v}
K(x_p,x_v)\,
f_v(x_v)
\prod_{c\in\operatorname{ch}(v)}
M_{c\to v}(x_v).
}
\]

At a leaf the empty product is `1`, so this is well-defined by finite recursion. Crucially, after all variables below `v` have been summed, **the entire branch contributes only one scalar function of the parent coordinate**. No matrix or higher tensor remains at the attachment point.

For a path vertex `v_j`, multiply together all messages arriving from branches not lying on the `a-b` path:

\[
g_j(x)
=
f_{v_j}(x)
\prod_{c\in\mathcal B_j}M_{c\to v_j}(x).
\]

The functions `g_j` can be arbitrarily complicated. They may contain chord sums, cyclotomic rational functions, products of previous messages, or prime-specific shell arithmetic. None of that matters for the next step, because PC-092 already allows an **arbitrary diagonal profile** on every intermediate shell.

## 3. Exact reduction to the PC-092 serial class

After contracting every off-path component, Fubini rearrangement of the finite sums gives exactly

\[
\boxed{
\mathcal T_{a,b}
=
D_{g_0}\,
K_{S_{v_0},S_{v_1}}
D_{g_1}\,
K_{S_{v_1},S_{v_2}}
\cdots
D_{g_{m-1}}\,
K_{S_{v_{m-1}},S_{v_m}}
D_{g_m}.
}
\]

Thus branching has disappeared completely. It has only renormalized the scalar weight on each vertex of the unique exposed path.

PC-092 defines, for disjoint endpoint sets `A,C`, the endpoint-displacement class

\[
\mathcal E(A,C)
=
\left\{
\sum_{j=1}^{r}D_{a_j}K_{A,C}D_{c_j}
+
\sum_{k=1}^{t}u_kv_k^{\mathsf T}
\right\},
\]

with endpoint diagonal terms additionally allowed for returns. Its exact weighted two-hop identity proves that arbitrary finite serial words of `K` with arbitrary intermediate diagonal weights remain in this class.

Applying that theorem to the effective weights `g_j` gives

\[
\boxed{
\mathcal T_{a,b}\in
D_{g_0}\,\mathcal E(S_a,S_b)\,D_{g_m}.
}
\]

Equivalently, every finite two-leg cotangent tree is a finite sum of endpoint-weighted copies of the **direct endpoint cotangent block** plus separable rank-one corrections; when the two exposed shell sets coincide, only the endpoint-local diagonal correction already present in PC-092 is added.

The representation size may grow with tree size, but no term carries an index over a hidden interior shell after reduction.

## 4. The simplest Y-branch already shows the mechanism

Take a main path `A-B-C` and attach one extra shell `D` to `B`. With local weights `f_B` and `h_D`, the branching kernel is

\[
\mathcal Y(a,c)
=
\sum_{b\in B}\sum_{u\in D}
f_B(b)h_D(u)
K(a,b)K(b,c)K(b,u).
\]

Define the branch message

\[
m_D(b)
=
\sum_{u\in D}h_D(u)K(b,u)
=
(T_Dh_D)(b).
\]

Then identically

\[
\boxed{
\mathcal Y
=
K_{A,B}D_{f_Bm_D}K_{B,C}.
}
\]

PC-092 immediately reduces this to

\[
\boxed{
\mathcal Y
=
D_{T_B(f_Bm_D)|_A}K_{A,C}
-
K_{A,C}D_{T_B(f_Bm_D)|_C}
-
s_B(f_Bm_D)J_{A,C}.
}
\]

So even the first genuine branch creates no new two-leg matrix species. Deeper branches merely replace `m_D` by recursively computed scalar messages before the same identity is applied.

## 5. Why this is stronger than the serial theorem but weaker than a tensor no-go

PC-092 starts from a chain and permits arbitrary scalar memory on each intermediate shell. PC-093 shows that, for a tree with exactly two exposed legs, **all finite off-chain branching is already contained in that arbitrary scalar memory**. The unique path property is the decisive fact.

This closes a natural loophole in the surviving cocycle program. One cannot escape the endpoint-displacement normal form merely by attaching finitely many additional exact-order shells as side branches, letting their cotangent interactions produce nonlinear scalar messages, and then reading a two-leg operator between two distinguished shells.

However, the theorem deliberately stops at the first topology where the reduction fails:

- with three or more exposed shell variables, a branching vertex can leave a genuine multi-leg tensor rather than a scalar message;
- with a cycle, removing leaves eventually leaves a loop rather than a unique serial path;
- with a different edge operator, the residual path need not lie in the PC-092 endpoint-displacement algebra;
- with infinite depth, exchanging limits with branch contraction requires a separate analytic theorem.

Those are mathematical boundaries, not suggestions that a positive RH mechanism exists there.

## 6. Prime-blind matched control

No step in the reduction uses primality, exact order, a cyclotomic polynomial, or even roots of unity beyond the final PC-092 cotangent identity. The tree-message step uses only finiteness and pairwise edge factorization. The endpoint-displacement step holds for arbitrary finite disjoint sets of unit-circle points.

Therefore the same mechanism applies unchanged to a matched non-prime control with the same tree topology and the same local cotangent rule:

\[
\boxed{
\text{finite two-leg tree}
\longrightarrow
\text{scalar branch messages on a unique path}
\longrightarrow
\text{PC-092 endpoint displacement}.
}
\]

Primality can change the numerical values of the messages `M_{v->p}` and of the endpoint transforms, but it does not alter the composition law or create a new branching carrier. Any prime discriminator would have to be extracted later from those surviving profiles by a construction outside the present finite two-leg tree class.

## 7. Prior-art and novelty audit

No historical novelty is claimed for the abstract elimination of branches.

- Exact inward message passing on cycle-free factor graphs is standard sum-product/tree contraction; see F. R. Kschischang, B. J. Frey and H.-A. Loeliger, **Factor Graphs and the Sum-Product Algorithm**, *IEEE Transactions on Information Theory* 47:2 (2001), 498–519, DOI `10.1109/18.910572`. That literature already explains why a fully contracted subtree is summarized at its attachment by a one-variable message.
- The second half of the argument is the Prime-Circle-specific ingredient already established in PC-092: arbitrary diagonal messages on a cotangent path remain in the endpoint-displacement class because the kernel is Cauchy-like and satisfies the exact weighted three-point identity.
- Classical Cauchy/displacement-structured matrix theory, already audited for PC-092, is a further warning against treating the resulting bounded endpoint representation as a novel spectral mechanism.

The durable contribution is therefore not a new tensor-network algorithm. It is the **research-specific closure of the acyclic branching escape hatch**: once PC-092 has proved closure for arbitrary path weights, generic exact tree contraction implies that every finite two-leg branching cotangent network is already inside that closed class.

Directed searches around tree tensor contraction/factor graphs and Cauchy-like displacement structure found no indication that this Prime-Circle specialization supplies an independent zeta or RH mechanism. The reduction itself explains why: all hidden branch coordinates disappear before any spectral interpretation.

## 8. Falsification controls

The theorem is finite and directly testable.

1. For the Y-network in Section 4, compare the direct double sum with `K_AB D_{f_B m_D} K_BC` for arbitrary complex weights.
2. For a deeper rooted branch, eliminate leaves recursively with the message formula and compare against brute-force summation over all branch variables.
3. For an arbitrary finite tree with two exposed vertices, remove the unique path and verify that every connected off-path component attaches at exactly one path vertex.
4. Contract all branches and compare the resulting kernel entrywise with the serial effective-weight product in Section 3.
5. Apply the PC-092 weighted two-hop identity recursively; no surviving term may contain an unsummed hidden-shell index.
6. Replace every primitive shell by a matched collection of generic unit-circle points. The same reduction must remain valid.

A counterexample in which a finite acyclic off-path branch leaves anything other than a scalar function of its attachment coordinate would refute the message reduction. A counterexample to the final endpoint-displacement form would refute PC-092 itself.

## 9. Consequence for the surviving preimage-tube cocycle clue

`CLUE-preimage-tube-fiber-sector-cocycle` remained open after PC-092 partly for **non-serial/branching tensors**. PC-093 splits that phrase sharply.

The following subclass is now closed:

\[
\boxed{
\text{finite acyclic cotangent network}
+
\text{exactly two exposed shell legs}
\Longrightarrow
\text{endpoint displacement}.
}
\]

Accordingly, adding finite tree-shaped side memories to a two-leg prime-tube transfer does not evade PC-092. A genuinely surviving finite branching candidate must retain at least three exposed legs, contain a cycle that cannot be leaf-eliminated, or use a genuinely different intrinsic edge operator/tensor. Infinite-depth limits and the separate Hardy/Hankel or global-uniformization branches also remain outside this result.

PC-093 introduces no spectral parameter, functional equation, gamma factor, critical-line selector, or new zeta divisor. It is a negative structural boundary on where a future Prime-Circle mechanism can still reside.
