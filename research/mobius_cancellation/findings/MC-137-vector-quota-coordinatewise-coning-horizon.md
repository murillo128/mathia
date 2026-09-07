# MC-137 — Finite vector quota filtrations have a coordinatewise coning horizon

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Let `V` be a vertex set and let

\[
\widehat w:V\to(0,\infty)^d
\]

be a fixed finite-dimensional vector weight. For a positive quota vector

\[
q=(q_1,\dots,q_d)\in(0,\infty)^d,
\]

use the Pakianathan--Winfree vector-quota convention

\[
X_q=X[\widehat w:q]
 =\left\{F\subset V:\ F\text{ finite and }w_j(F)<q_j\text{ for some }1\le j\le d\right\},
\]

where

\[
w_j(F)=\sum_{v\in F}w_j(v).
\]

Fix any vertex `v_* in V` and write

\[
a=\widehat w(v_*)=(a_1,\dots,a_d).
\]

If two quota vectors satisfy the coordinatewise displacement condition

\[
Q_j\ge q_j+a_j\qquad(1\le j\le d),
\tag{1}
\]

then the canonical inclusion factors through the closed star of `v_*` in the later complex:

\[
\boxed{X_q\subseteq \operatorname{st}_{X_Q}(v_*)\subseteq X_Q.}
\tag{2}
\]

Consequently

\[
\boxed{X_q\hookrightarrow X_Q\text{ is null-homotopic whenever }Q\ge q+\widehat w(v_*)\text{ coordinatewise}.}
\tag{3}
\]

No common coordinatewise-minimum vertex is required. **Any fixed vertex supplies a finite coning displacement vector.**

In particular, consider any monotone affine ray of quota vectors

\[
q(t)=q^{(0)}+td,
\qquad d=(d_1,\dots,d_d),\qquad d_j>0\text{ for all }j.
\]

For the fixed vertex `v_*`, choose

\[
T\ge \max_{1\le j\le d}\frac{a_j}{d_j}.
\tag{4}
\]

Then for every `t>=0`,

\[
q(t+T)\ge q(t)+a
\]

coordinatewise, and hence

\[
\boxed{X_{q(t)}\hookrightarrow X_{q(t+T)}\text{ is null-homotopic for every }t.}
\tag{5}
\]

Thus every fixed finite-dimensional additive vector-quota filtration, when followed along a ray that advances positively in every quota coordinate, has a **uniformly bounded ordinary homotopy-persistence horizon**.

This closes the most immediate vector/multiparameter escape left open by `MC-136`: adding finitely many fixed additive quota coordinates can make the topology at an individual parameter arbitrarily complicated, but it cannot by itself create indefinitely persistent ordinary homotopy transport along a genuinely cofinal positive direction.

## 1. Coordinatewise coning proof

Take any simplex `F` of `X_q`. By definition there exists at least one witness coordinate `j` such that

\[
w_j(F)<q_j.
\]

If `v_*` already belongs to `F`, then `F` lies in the closed star of `v_*` trivially.

If `v_*` does not belong to `F`, add that vertex. In the same witness coordinate,

\[
w_j(F\cup\{v_*\})=w_j(F)+a_j<q_j+a_j\le Q_j.
\]

Therefore `F union {v_*}` is a simplex of `X_Q`, so `F` is a face of `st_{X_Q}(v_*)`. This proves `(2)`.

Because a closed simplicial star is a cone, the map `X_q -> X_Q` factors through a contractible subcomplex and is null-homotopic, proving `(3)`.

The key point is the existential `some coordinate` condition in the vector-quota definition. The coordinate witnessing membership of a given face is allowed to depend on the face. The same witness remains valid after adjoining `v_*` once the later quota has advanced by that vertex's weight in **every** coordinate. Hence the proof needs neither a single coordinate that controls all faces nor a vertex minimizing all coordinates simultaneously.

The ray statement `(5)` is then immediate from `(4)`.

## 2. Static universality does not imply persistent transport

Pakianathan and Winfree prove in their Appendix B that every finite simplicial complex is isomorphic to a finite vector-valued quota complex. Their vector formulation is therefore statically universal: at one quota vector, finite-dimensional additive quotas can realize arbitrary finite simplicial topology.

That fact might appear to make vector quotas a natural escape from `MC-136`, whose scalar complexes have rigid bouquet-of-spheres topology. The filtration calculation above shows that **static expressive power and long-range persistence are different questions**.

For fixed weights, translating a quota vector far enough in every positive coordinate allows the same chosen vertex to cone every earlier face. The result is independent of how complicated `X_q` or `X_Q` is individually. In particular, along every strictly positive affine ray, all reduced homology maps and every other invariant functorially determined by the ordinary homotopy class of the inclusion vanish after a uniformly bounded lag.

This yields a useful representation-level no-go:

> finite vector dimension plus fixed additive simplex weights can encode arbitrary finite topology at a snapshot, but ordinary long-range topological transport along cofinal positive quota directions still collapses by a one-vertex cone.

The scalar result `MC-136` is the one-dimensional special case, but the vector proof reveals why the apparent extra static freedom does not remove the transport obstruction.

## 3. Prior-art audit

The established framework is Pakianathan and Winfree's quota-complex theory. Their Definition 1.2 takes a vector weight

\[
\widehat w:V\to\mathbb R_+^d
\]

and a vector quota `q`, declaring `F` to be a face when

\[
w_j(F)<q_j
\]

for **some** coordinate `j`. Equivalently,

\[
X[\widehat w:q]=\bigcup_{j=1}^d X[w_j:q_j].
\]

Their Appendix A studies vector-weighted quota complexes through this union of scalar quota complexes and explicitly notes that the vector-weighted picture is less complete than the scalar one. Their Theorem B.1 proves that every finite simplicial complex can be represented by a vector-valued quota system with positive integer coordinates.

Primary source:

Jonathan Pakianathan and Troy Winfree, *Threshold complexes and connections to number theory*, Turkish Journal of Mathematics 37 (2013), no. 3, 511--539, DOI `10.3906/mat-1112-14`, arXiv `1104.4324`; see Definition 1.2, Appendix A, and Theorem B.1. The arXiv preprint appears under the title *Quota Complexes, Persistant Homology and the Goldbach Conjecture*.

A targeted literature search found the vector-quota definition, union decomposition, category bounds, and static universality theorem, but did not locate a published statement of the inter-parameter coordinatewise star factorization `(2)` or the cofinal-ray horizon `(5)`. This finding therefore makes **no novelty claim** for vector quota complexes or their static topology, and only records the exact filtration consequence needed by the Mathia frontier.

## Boundaries and falsification tests

- The argument requires a **fixed finite-dimensional additive vector weight**. If the weights themselves vary with scale, or the simplex score is nonadditive, the proof need not apply.
- The cofinal-ray corollary requires positive motion in every coordinate: `d_j>0`. If some quota coordinate remains frozen, `(4)` cannot absorb a vertex having positive weight in that coordinate. The theorem therefore does not classify arbitrary paths confined to a boundary face of parameter space.
- The theorem does not say that a multiparameter persistence module is trivial at short or incomparable parameter separations. It says that coordinatewise displacement by one fixed vertex weight makes the corresponding inclusion null-homotopic.
- Null-homotopy kills reduced homology maps and ordinary homotopy-invariant transport. For unreduced `H_0`, the induced map factors through the homology of a point rather than being literally the zero map.
- Static universality remains true. The obstruction concerns **transport under the fixed quota filtration**, not which isolated complexes admit vector-quota presentations.
- The theorem does not classify arithmetic labels on simplices or chains, incidence-level operators, higher coherent data not determined by individual homotopy-category maps, or statistics that deliberately retain the ordered sequence of births/deaths rather than only the maps between ordinary homotopy types.
- Infinite-dimensional quota systems are outside the claim. A proposal using infinitely many coordinates must still establish local finiteness, a canonical arithmetic construction, and an information budget rather than obtaining persistence by hiding the complete source in infinitely many coordinates.
- No Möbius cancellation estimate follows from `(3)` or `(5)`. This is a representation obstruction, not a source-to-amplitude theorem.

A counterexample to `(2)` under hypothesis `(1)` would require a face `F` and a witness coordinate `j` with `w_j(F)<q_j`, but simultaneously `w_j(F)+a_j>=Q_j`; this contradicts `Q_j>=q_j+a_j` directly.

## Consequence for the line

`MC-136` left genuine vector/multiparameter filtration data as a possible escape from scalar coning. This finding narrows that residual substantially. **Merely replacing one fixed additive quota by finitely many fixed additive quotas does not restore arbitrarily long ordinary homotopy transport along any direction that eventually advances all coordinates.**

The surviving topological carrier must therefore exploit structure not captured by this finite fixed-additive transport class: for example a noncofinal or intrinsically anisotropic parameter mechanism with arithmetic meaning, scale-dependent or nonadditive weights, raw labelled chain/incidence data, higher coherence across the parameter poset, an infinite-coordinate construction with a nontrivial information-budget theorem, or a genuinely different filtration.

As in `MC-133`--`MC-136`, none of those possibilities counts as progress until it supplies an independently controlled Möbius-specific **source** quantity whose transport to mean-absolute or endpoint Mertens amplitude is cheaper than reconstructing the target itself.