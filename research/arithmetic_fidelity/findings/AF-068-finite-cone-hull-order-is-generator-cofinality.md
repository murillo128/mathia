# AF-068 — Finite cone-hull order is generator cofinality

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a real vector space and let

\[
\mathcal K=\{K_1,\ldots,K_r\},
\qquad
\mathcal L=\{L_1,\ldots,L_s\}
\]

be finite nonempty families of cones in `V`, each containing `0`. For an arbitrary subset `S\subseteq V`, define the associated finite directional hull operators

\[
H_{\mathcal K}(S)
=
\bigcap_{i=1}^r(S-K_i),
\qquad
H_{\mathcal L}(S)
=
\bigcap_{j=1}^s(S-L_j).
\tag{1}
\]

Equivalently,

\[
m\in H_{\mathcal K}(S)
\iff
S\cap(m+K_i)\ne\varnothing
\quad\forall i.
\tag{2}
\]

Then:

1. **Universal comparison of finite cone hulls is exactly generator cofinality.** One has
   \[
   \boxed{
   H_{\mathcal K}(S)\subseteq H_{\mathcal L}(S)
   \quad\text{for every }S\subseteq V
   }
   \]
   if and only if
   \[
   \boxed{
   \forall L\in\mathcal L\ \exists K\in\mathcal K
   \text{ with }K\subseteq L.
   }
   \tag{3}
   \]
   Thus a second presentation is universally weaker precisely when every one of its directional tests contains at least one test from the first presentation.

2. **Only inclusion-minimal generators matter.** Let
   \[
   \min(\mathcal K)
   =
   \{K\in\mathcal K:\nexists K'\in\mathcal K\text{ with }K'\subsetneq K\}.
   \tag{4}
   \]
   Then
   \[
   \boxed{
   H_{\mathcal K}=H_{\min(\mathcal K)}
   }
   \tag{5}
   \]
   as operators on all subsets of `V`. Any generator that properly contains another is redundant because hitting the smaller translate already forces a hit of the larger translate.

3. **Finite cone-hull operators have a canonical irredundant presentation.** For two finite cone families,
   \[
   \boxed{
   H_{\mathcal K}=H_{\mathcal L}
   \text{ on all subsets of }V
   \iff
   \min(\mathcal K)=\min(\mathcal L).
   }
   \tag{6}
   \]
   Equivalently, equality of the hull operators is mutual cofinality under inclusion. Once each family is reduced to an inclusion antichain, operator equality forces literal equality of the retained cones.

4. **The exact witness complexity at a point is a transversal number.** Suppose `m\in H_{\mathcal K}(S)` and define the nonempty witness sets
   \[
   E_i(m,S)=S\cap(m+K_i).
   \tag{7}
   \]
   Let
   \[
   c_{\mathcal K}(m;S)
   =
   \min\{|S_0|:S_0\subseteq S,\ m\in H_{\mathcal K}(S_0)\}.
   \tag{8}
   \]
   Then
   \[
   \boxed{
   c_{\mathcal K}(m;S)
   =
   \tau\bigl(\{E_i(m,S):1\le i\le r\}\bigr),
   }
   \tag{9}
   \]
   where `tau` is the minimum cardinality of a hitting set/transversal. In particular,
   \[
   c_{\mathcal K}(m;S)\le r,
   \tag{10}
   \]
   and the inclusion-minimal witness subsets are exactly the minimal transversals of the local witness hypergraph. When `S` is finite, their family is the classical blocker of the clutter obtained after deleting redundant witness edges.

5. **Invertible linear reparameterization changes the presentation but not the information state.** For every invertible linear map `A:V\to W`, let
   \[
   A\mathcal K=\{A K:K\in\mathcal K\}.
   \]
   Then
   \[
   \boxed{
   A\bigl(H_{\mathcal K}(S)\bigr)
   =
   H_{A\mathcal K}(A S).
   }
   \tag{11}
   \]
   Hence the canonical antichain transforms functorially:
   \[
   \min(A\mathcal K)=A\min(\mathcal K).
   \tag{12}
   \]
   Cone labels, ordering, duplicated tests, and invertible coordinate changes therefore cannot create a different finite directional fidelity state.

6. **AF-067's polyhedral facet presentation is already irredundant.** In the notation of AF-067,
   \[
   K_v
   =
   \{w:\varphi(w)\ge0\ \forall\varphi\in F_v\},
   \qquad
   v\in\operatorname{Vert}(B),
   \tag{13}
   \]
   where `F_v` is the dual facet corresponding to `v`. Distinct `K_v` are inclusion-incomparable. Consequently
   \[
   \boxed{
   \min\{K_v:v\in\operatorname{Vert}(B)\}
   =
   \{K_v:v\in\operatorname{Vert}(B)\}.
   }
   \tag{14}
   \]
   Thus AF-067's one-cone-per-primal-vertex system contains no purely presentation-level directional redundancy. Any smaller universal description of the same hull must use a genuinely different representation, not merely discard one of the facet cones.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{a finite directional compression has a canonical antichain of indispensable tests;}\\
\text{universal comparison is containment cofinality, and local certificate size is a hitting-set invariant.}
\end{array}
}
\tag{15}
\]

This separates two notions that AF-067 left together. The raw number of declared directions is presentation dependent, while the inclusion-minimal generator clutter is intrinsic to the resulting hull operator. At a particular target `S` and point `m`, the exact amount of retained provenance needed to certify membership is instead the transversal number of the induced local witness system.

## Derivation

### Universal inclusion is equivalent to containment cofinality

Assume first that every `L\in\mathcal L` contains some `K\in\mathcal K`. If `m\in H_{\mathcal K}(S)`, equation (2) gives

\[
S\cap(m+K)\ne\varnothing.
\]

Since `K\subseteq L`,

\[
m+K\subseteq m+L,
\]

so `S\cap(m+L)\ne\varnothing`. This holds for every `L\in\mathcal L`, proving

\[
H_{\mathcal K}(S)\subseteq H_{\mathcal L}(S)
\]

for every `S`.

Conversely, suppose that some `L_0\in\mathcal L` contains no member of `\mathcal K`. Then for every `K_i` choose

\[
x_i\in K_i\setminus L_0
\tag{16}
\]

and set

\[
S=\{x_1,\ldots,x_r\}.
\tag{17}
\]

Because `x_i\in K_i`, the set `S` meets every `K_i`, hence

\[
0\in H_{\mathcal K}(S).
\tag{18}
\]

But every selected point lies outside `L_0`, so

\[
S\cap L_0=\varnothing,
\qquad
0\notin H_{\mathcal L}(S).
\tag{19}
\]

Universal hull inclusion therefore fails. This proves (3) without topology, convexity, closedness, or finite-dimensionality; only finiteness of the declared generator family is used to build the finite separating target (17).

### Minimal generators are the canonical presentation

If `K'\subseteq K`, then for every `S`

\[
S-K'\subseteq S-K.
\tag{20}
\]

Thus the `K` constraint adds nothing once the `K'` constraint is present. Iterating this deletion over a finite family proves (5).

If `H_{\mathcal K}=H_{\mathcal L}`, applying (3) in both directions gives

\[
\forall K\in\mathcal K\ \exists L\in\mathcal L:L\subseteq K,
\qquad
\forall L\in\mathcal L\ \exists K\in\mathcal K:K\subseteq L.
\tag{21}
\]

Reduce both families to antichains. For `K\in\min(\mathcal K)`, choose `L\in\min(\mathcal L)` with `L\subseteq K`, then choose `K'\in\min(\mathcal K)` with `K'\subseteq L`. We obtain

\[
K'\subseteq L\subseteq K.
\tag{22}
\]

The antichain property forces `K'=K`, hence `L=K`. Therefore every minimal generator of one presentation is a minimal generator of the other; symmetry proves (6).

This is the exact presentation-level naturality test requested by the line mandate: harmless duplication, relabeling, or replacement by a containing directional test does not create new fidelity structure, while losing one antichain generator necessarily changes the operator on some finite target.

### Witness certificates are hypergraph transversals

For a fixed `m\in H_{\mathcal K}(S)`, equation (2) says precisely that every `E_i(m,S)` in (7) is nonempty. A subset `S_0\subseteq S` still certifies `m` exactly when

\[
S_0\cap E_i(m,S)\ne\varnothing
\qquad\forall i.
\tag{23}
\]

That is the definition of a hitting set/transversal of the witness hypergraph, proving (9). Selecting one point from each nonempty edge gives (10). When several directions can be witnessed by the same target point, `tau` can be much smaller than the number of generators; when the witness edges are disjoint singletons, the one-per-direction upper bound is sharp.

AF-067's `\ell^\infty_d` control

\[
S=\{\pm1\}^d,
\qquad
m=0
\]

is exactly the latter extremal case: each sign orthant meets `S` in its unique matching cube vertex, so the local witness clutter consists of `2^d` singleton edges and

\[
\tau=2^d.
\tag{24}
\]

Thus the sharp witness count in AF-067 is not merely a cardinality example; it is the maximum-transversal regime of the exact local blocker formulation.

### Linear equivariance

For an invertible linear map `A`,

\[
A(S-K)=AS-AK.
\tag{25}
\]

Because a bijection preserves finite intersections,

\[
\begin{aligned}
A(H_{\mathcal K}(S))
&=A\left(\bigcap_{K\in\mathcal K}(S-K)\right)\\
&=\bigcap_{K\in\mathcal K}(AS-AK)\\
&=H_{A\mathcal K}(AS),
\end{aligned}
\tag{26}
\]

which proves (11). Invertibility also preserves strict inclusion among cones, giving (12).

## Polyhedral specialization: facet cones are indispensable

Let `B` be the full-dimensional polyhedral unit ball from AF-067 and let

\[
N_B(v)
=
\{\varphi\in V^*:\varphi(v)\ge\varphi(x)\ \forall x\in B\}
\tag{27}
\]

be the normal cone at a vertex `v`. Since `F_v` is the dual facet normalized by `\varphi(v)=1`,

\[
N_B(v)=\operatorname{cone}(F_v).
\tag{28}
\]

With the nonnegative dual-cone convention,

\[
K_v=N_B(v)^+.
\tag{29}
\]

Suppose `K_v\subseteq K_w`. Duality reverses containment, so

\[
N_B(w)\subseteq N_B(v).
\tag{30}
\]

Normal cones at vertices are the full-dimensional maximal cones of the normal fan of `B`. Two distinct maximal cones of a fan cannot contain one another. Hence (30) forces

\[
N_B(w)=N_B(v),
\]

and a functional in the relative interior of this full-dimensional cone has a unique maximizing vertex on `B`, so `v=w`. This proves (14).

Therefore the finite reduction in AF-067 is stronger than merely replacing infinitely many directions by some convenient finite list: the resulting facet-cone family is already the canonical inclusion-antichain presentation of that directional hull.

## Prior art and novelty assessment

The finite set-system mechanism is classical.

- Jack Edmonds and D. R. Fulkerson, **“Bottleneck Extrema,”** *Journal of Combinatorial Theory* 8, 299–306 (1970), DOI `10.1016/S0021-9800(70)80083-7`. They define a clutter as an inclusion-antichain, define the blocker as the minimal subsets meeting every member, prove blocker involution, and explicitly note that arbitrary families reduce to their inclusion-minimal members for the relevant bottleneck problems. This is direct prior art for the antichain/blocker mathematics used in (5), (9), and the finite-witness interpretation.
- Claude Berge, ***Hypergraphs: Combinatorics of Finite Sets***, North-Holland Mathematical Library 45, North-Holland (1989). Role: standard hypergraph language for transversals, minimal transversals, and Sperner/clutter reductions underlying the finite local witness system.
- Eugene Fink and Derick Wood, ***Restricted-Orientation Convexity***, Springer (2004), DOI `10.1007/978-3-642-18849-7`. Role: nearby mature theory showing that equivalence and irredundancy questions for finite orientation systems already belong to established generalized-convexity mathematics. AF-068 does not identify its cone-hit hull with their restricted-orientation or strong restricted-orientation hulls.

No novelty is claimed for clutters, blockers, minimal transversals, antichain reduction, normal fans, or orientation-equivalence questions in generalized convexity. The universal comparison theorem (3) is an elementary exact consequence of the particular cone-hit representation (1), and the witness formula (9) is the corresponding hypergraph transversal identity.

The durable Arithmetic Fidelity contribution is narrower: AF-067 produced a finite directional closure as the exact destination of an analytic fidelity problem; AF-068 now removes presentation artifacts from that closure. It identifies the **canonical indispensable directional tests**, gives a finite counterexample whenever one is lost, and replaces the coarse one-witness-per-direction certificate bound by the exact local transversal number. These are audit tools for deciding whether two finite compression presentations carry the same structural discriminator, not evidence of a new theory of hypergraphs or convexity.

## Boundaries and failure modes

- The universal comparison theorem concerns equality/inclusion of the hull operators on **all** target subsets `S`. Two non-cofinal presentations can agree on one restricted source class or on one particular target; such relative equivalence requires a separate source-class analysis.
- Finiteness of the generator family is essential to the finite separating target in (17) and to the finite witness bound. Infinite directional systems can require compactness, topology, finite-subcover hypotheses, or genuinely infinite transversals.
- The canonical antichain is canonical only inside the declared cone-hit representation in the same ambient vector space. A nonlinear encoding, quotient, or category change may realize the same abstract closure operator using objects not comparable by literal cone inclusion.
- Equation (9) is point- and target-relative. The global generator clutter and the local witness clutter are different objects: clipping by `S` and translation by `m` can create new containments or overlaps among witness sets.
- AF-067 facet-cone irredundancy says that none of its directional constraints can be dropped **universally**. It does not say every facet is needed for every `S` or every `m`; local transversal compression can still make many directions share one witness.
- Restricted-orientation convexity is prior-art context, not an asserted identification. In particular, strong restricted-orientation convexity is a different closure notion and should not be used as evidence for cone-hit equivalence without an explicit theorem.
