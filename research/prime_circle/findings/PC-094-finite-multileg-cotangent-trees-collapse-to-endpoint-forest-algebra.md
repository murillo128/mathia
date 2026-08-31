# PC-094 — finite multileg cotangent trees collapse to endpoint forest algebra

**Status:** `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-BOUNDARY` for finite acyclic networks built only from the intrinsic Prime-Circle cotangent kernel, pairwise-disjoint exact-order shells, and arbitrary shell-local scalar weights. PC-095 closes the two-external-leg tree case under the precise PC-092-compatible exposed-path disjointness hypothesis. The exact Hermite cotangent product identity closes the remaining finite-tree loophole under global pairwise disjointness: eliminating a hidden shell vertex of arbitrary valence replaces it by a finite sum of cotangent forests on its neighbors plus one-body endpoint transforms. Induction removes every hidden vertex.

This does **not** close networks with cycles or repeated-edge powers, genuinely different intrinsic edge operators/tensors, infinite-depth limits, Hardy/Hankel constructions, global uniformization/monodromy, or a later cross-level use of the surviving one-body endpoint profiles. It also does not say those endpoint profiles are arithmetically trivial. The exact obstruction is narrower: **finite acyclic branching of the canonical cotangent propagator does not retain an irreducible hidden-shell tensor when the participating shell sets are pairwise disjoint, regardless of the number of exposed legs.**

## 1. The arbitrary-valence cotangent star has an exact endpoint reduction

For distinct points `z,w` on the unit circle use

\[
K(z,w)
=i\cot\!\left(\frac{\theta_z-\theta_w}{2}\right)
=-\frac{z+w}{z-w},
\qquad K(z,z)=0.
\]

Fix pairwise distinct external points `z_1,...,z_d` and a variable `u` distinct from them. Put

\[
\boxed{
 c_i(z_1,\ldots,z_d)
 =\prod_{\substack{1\le j\le d\\j\ne i}}K(z_j,z_i).
}
\]

Then

\[
\boxed{
\prod_{i=1}^{d}K(z_i,u)
=\varepsilon_d
+\sum_{i=1}^{d}c_i(z_1,\ldots,z_d)K(z_i,u),
}
\]

where

\[
\boxed{
\varepsilon_d=\frac{1+(-1)^d}{2}
=\begin{cases}1,&d\text{ even},\\0,&d\text{ odd}.
\end{cases}}
\]

Equivalently,

\[
\boxed{
\sum_{i=1}^{d}c_i
=\frac{1-(-1)^d}{2}.
}
\]

Thus an arbitrary-valence product through one common hidden circle point is not a new `d`-body kernel. It is a constant for even valence plus a sum of **one-leg cotangent propagators**, with coefficients made entirely from direct cotangent interactions among the exposed points.

## 2. Rational partial fractions give an exact proof

Write

\[
K(z_i,u)=\frac{z_i+u}{u-z_i}
=1+\frac{2z_i}{u-z_i}.
\]

As a rational function of `u`,

\[
R(u)=\prod_{i=1}^{d}K(z_i,u)
\]

has only simple poles at `u=z_i` and satisfies `R(u)->1` as `u->infinity`. The residue at `u=z_i` is

\[
2z_i\prod_{j\ne i}K(z_j,z_i)=2z_i c_i.
\]

Because

\[
K(z_i,u)-1=\frac{2z_i}{u-z_i},
\]

partial fractions therefore give

\[
R(u)
=1+\sum_i c_i\bigl(K(z_i,u)-1\bigr)
=1-\sum_i c_i+\sum_i c_iK(z_i,u).
\]

Evaluating at `u=0` gives `K(z_i,0)=-1`, hence

\[
(-1)^d=1-2\sum_i c_i.
\]

This proves both displayed identities. No root-of-unity, primality, shell, limiting, or spectral assumption is used.

The same formula is Hermite's classical cotangent product identity in circle coordinates. Warren P. Johnson, **Trigonometric Identities à la Hermite**, *The American Mathematical Monthly* 117:4 (2010), 311–327, DOI `10.4169/000298910X480784`, gives the standard identity

\[
\prod_{j=1}^{d}\cot(t-a_j)
=\cos\!\left(\frac{d\pi}{2}\right)
+\sum_{i=1}^{d}
\left(\prod_{j\ne i}\cot(a_i-a_j)\right)
\cot(t-a_i),
\]

including a partial-fraction derivation. The Prime-Circle star reduction is therefore a direct specialization/reparameterization of classical prior art, not a historically new cotangent identity.

## 3. An arbitrary weighted hidden shell leaves only one-body endpoint transforms

Let `B` be any finite set disjoint from all external points and let `f:B->C` be arbitrary. As in PC-092 define

\[
(T_Bf)(z)=\sum_{u\in B}f(u)K(z,u),
\qquad
s_B(f)=\sum_{u\in B}f(u).
\]

Multiplying the star identity by `f(u)` and summing over `u in B` gives

\[
\boxed{
\sum_{u\in B}f(u)\prod_{i=1}^{d}K(z_i,u)
=\varepsilon_d s_B(f)
+\sum_{i=1}^{d}c_i(z_1,\ldots,z_d)(T_Bf)(z_i).
}
\]

The weight `f` is completely unrestricted. It may already contain chord potentials, products of messages from other shells, or nested transforms produced by earlier eliminations. Consequently the identity is stable under recursive tree elimination: whatever arithmetic a contracted subtree sends into a hidden vertex is merely another scalar weight for the next star reduction.

For `d=2` this is the same local algebra behind the weighted two-hop collapse of PC-092, up to the orientation signs forced by `K(z,w)=-K(w,z)`. For `d>=3` it is the missing multileg analogue.

## 4. Primitive-shell specialization remains endpoint cyclotomic data

For an unweighted primitive shell `B=P_r^*`, PC-089 gives

\[
(T_{P_r^*}1)(z)
=\sigma_r(z)
=\varphi(r)-2z\frac{\Phi_r'(z)}{\Phi_r(z)}.
\]

Hence the complete unweighted `d`-leg primitive-shell star is

\[
\boxed{
\sum_{u\in P_r^*}\prod_{i=1}^{d}K(z_i,u)
=\varepsilon_d\varphi(r)
+\sum_{i=1}^{d}c_i(z_1,\ldots,z_d)
\left(
\varphi(r)-2z_i\frac{\Phi_r'(z_i)}{\Phi_r(z_i)}
\right).
}
\]

If one exposed point is the common anchor `1`, its unweighted primitive-shell transform vanishes by cyclotomic reciprocity, `sigma_r(1)=0`, exactly as in PC-089. The remaining dependence on the hidden primitive shell is still carried by one-body endpoint cyclotomic potentials rather than an irreducible multileg shell tensor.

This does **not** imply that arbitrary weighted transforms `T_Bf` are classical one-cyclotomic logarithmic derivatives. It says only that the star topology itself supplies no further many-body carrier beyond those one-body transforms and direct endpoint cotangent coefficients.

## 5. Every finite acyclic multileg network reduces by hidden-vertex elimination

Let `T=(V,E)` be a finite tree. Assign to every vertex `v` a finite unit-circle set `S_v` and a scalar local weight `f_v:S_v->C`. For the clean Prime-Circle specialization take pairwise distinct exact orders, so the primitive shell sets `S_v=P_{n_v}^*` are pairwise disjoint. Choose any subset `X subseteq V` of exposed vertices and sum over every hidden vertex `V\X`.

Fix an orientation of each edge once and for all. Before eliminating a hidden vertex `v`, use antisymmetry of `K` to orient every incident factor toward `x_v`; this contributes only a known overall sign. If the current neighbors of `v` are `w_1,...,w_d`, every term has the local form

\[
f_v(x_v)\prod_{i=1}^{d}K(x_{w_i},x_v),
\]

where `f_v` may already include arbitrary one-body factors generated by previous eliminations. Section 3 replaces the sum over `x_v` by

\[
\varepsilon_d s_{S_v}(f_v)
+\sum_i
\left(\prod_{j\ne i}K(x_{w_j},x_{w_i})\right)
(T_{S_v}f_v)(x_{w_i}).
\]

There are two topological outcomes.

- The even-valence scalar term deletes `v` and its incident edges, leaving a forest of its neighbor components.
- Each `i` term deletes `v` and reconnects its `d` former neighbor components by a star centered at `w_i`. Because deleting a vertex from a tree separates its neighbors into distinct components, adding those `d-1` star edges creates another tree on one fewer vertex, not a cycle. The new factor `(T_{S_v}f_v)(x_{w_i})` is simply absorbed into the one-body weight at `w_i`.

Thus every hidden-vertex elimination strictly decreases the number of hidden vertices and preserves the class "finite linear combination of weighted forests". Induction gives:

\[
\boxed{
\text{finite cotangent tree with arbitrary exposed legs}
\Longrightarrow
\text{finite linear combination of weighted cotangent forests on exposed legs only}.
}
\]

More explicitly, after all hidden variables have been summed the result is a finite sum of terms of the form

\[
\boxed{
C\,
\prod_{a\in X}h_a(x_a)
\prod_{\{a,b\}\in F}K(x_a,x_b),
}
\]

where `F` is a forest on the exposed vertices, `C` is a scalar, and each `h_a` is a one-variable endpoint profile generated by nested weighted shell transforms. **No hidden-shell index and no irreducible multileg hidden-shell tensor remains.**

For `|X|=2`, the conclusion is compatible with the stronger endpoint-displacement normal form of PC-092/PC-095 on its stated disjoint-path domain. PC-094 extends the topological obstruction to arbitrary finite external valence under the global pairwise-disjoint hypothesis, though it deliberately makes only the weaker endpoint-forest claim needed for that extension.

## 6. Why cycles are the first finite topology not eliminated by this theorem

The induction depends on tree topology. Eliminating a vertex of a tree never creates a cycle, and every hidden variable can eventually be removed by the Hermite star identity.

For a graph with a cycle, however, repeated elimination can create parallel endpoint edges or powers such as `K(z,w)^2`. Those are no longer simple Hermite stars with one copy of each distinct external pole. A residual closed word can therefore survive the tree reduction. PC-090 and PC-091 already constrain fully contracted odd/even cotangent loops, but they do not amount to a general classification of weighted cyclic multileg networks.

Accordingly PC-094 closes **finite acyclic branching under global pairwise shell disjointness**, not all finite cotangent tensor networks. The first genuinely different finite topology left to the accepted cocycle clue is a residual cycle/loopy network, a repeated-shell/coincidence network, or a construction using a second intrinsic operator that is not reducible to the same cotangent edge.

## 7. Prime-blind matched control and RH relevance

The star identity and the tree-elimination proof hold for arbitrary finite pairwise-disjoint sets of unit-circle points. Neither uses exact order, primality, cyclotomic factorization, or the common anchor. Therefore the same reduction holds on matched non-prime controls with the same graph topology and cotangent rule.

Primitive-shell arithmetic can enter the numerical values of the one-body transforms `T_Bf`, but it cannot alter the Hermite composition law. A claimed prime-specific associator, cocycle, curvature, or spectral carrier derived solely from finite acyclic cotangent branching in this disjoint class must therefore first demonstrate information **outside** the endpoint-forest normal form; branching itself is not such information.

No spectral parameter `s`, zeta divisor, functional equation, gamma completion, or critical-line selector is produced. The result is a structural no-go boundary for one natural route toward those objects, not a bridge to RH.

## 8. Prior-art and novelty audit

No historical novelty is claimed for the algebraic engine.

1. Hermite's product-to-sum cotangent identity is classical. Johnson's 2010 Monthly article gives the exact arbitrary-valence identity and a partial-fraction explanation matching Sections 1–2.
2. Eliminating hidden variables on a finite tree is standard acyclic factor-graph / sum-product reasoning, already used and audited in the two-leg tree reduction now stated precisely in PC-095.
3. PC-092 supplies the stronger two-leg endpoint-displacement closure, while PC-089 supplies the primitive-shell cyclotomic logarithmic derivative. PC-094 does not relabel these ingredients as a new spectral theorem.
4. Directed novelty checking around Hermite cotangent identities, cotangent product-to-sum formulas, finite cotangent matrices, and tree contraction found the star algebra squarely in classical territory. The durable contribution is the **Prime-Circle-specific boundary** obtained by combining that classical identity with the exact-shell tree architecture: the finite multileg tree escape is not an independent information carrier under the stated disjointness hypotheses.

The result should therefore be read as a decisive route restriction, not as a novelty claim.

## 9. Falsification controls

The claim is finite and directly auditable.

1. For arbitrary distinct unit-circle points `z_1,...,z_d,u`, compare the product `prod_i K(z_i,u)` with the Hermite endpoint sum for `d=1,2,...`.
2. Verify `sum_i c_i=0` for even `d` and `1` for odd `d`.
3. For an arbitrary finite intermediate set `B` and arbitrary complex weights `f`, compare direct summation with the weighted star formula in Section 3.
4. Test a globally pairwise-disjoint tree with at least two hidden branching vertices by brute-force summation and by eliminating the hidden vertices in different orders. All elimination orders must give the same endpoint function.
5. Replace every primitive shell by matched generic pairwise-disjoint unit-circle sets. The reduction must remain unchanged.
6. A counterexample in which a finite tree in the stated disjoint class, built solely from one copy of `K` per edge, leaves an unsummed hidden-shell tensor after recursive Hermite elimination refutes the theorem.

The pairwise-disjoint-shell hypothesis is part of the theorem. If the same exact shell is reused at nonadjacent vertices, elimination can create coincidence strata and repeated poles; that repeated-shell case is not claimed here and belongs with the cyclic/repeated-edge boundary.

## 10. Consequence for the surviving preimage-tube cocycle clue

`CLUE-preimage-tube-fiber-sector-cocycle` remains accepted after the corrected two-leg boundary PC-095 because genuinely multileg branching was still outside that theorem. PC-094 closes the globally pairwise-disjoint finite acyclic canonical-cotangent part of that escape:

\[
\boxed{
\text{finite acyclic cotangent network}
+\text{pairwise-disjoint shell sets}
+\text{arbitrary number of exposed shell legs}
\Longrightarrow
\text{endpoint weighted-forest algebra}.
}
\]

The clue therefore remains live only beyond this class: residual cyclic/loopy or repeated-shell/repeated-edge networks, genuinely distinct intrinsic multioperator couplings, infinite-depth/limit constructions, or a cross-level use of the surviving endpoint profiles that escapes the finite-tree reduction. Hardy/Hankel higher-word constructions and global uniformization/monodromy remain separate branches.

PC-094 is a structural negative boundary. It supplies no evidence that any of the surviving classes carries an RH mechanism.