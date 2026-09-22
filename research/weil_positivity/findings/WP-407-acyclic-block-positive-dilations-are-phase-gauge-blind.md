---
id: WP-407
title: Acyclic block-positive dilations are phase-gauge blind
branch: weil_positivity
status: supported
kind: gain-graph-switching-block-positivity-no-go
claim_strength: exact RH-independent classification showing that every central scalar edge-phase assignment on an acyclic Hermitian block coupling is removable by diagonal corner unitaries, so positivity is phase-blind even with arbitrary source-forced diagonal blocks; cycle holonomy is the first possible scalar phase-sensitive invariant and a triangle realizes the sharp boundary
created: 2026-09-22
related: [WP-297, WP-299, WP-301, WP-351, WP-405, WP-406]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - Nathan Reff, Spectral Properties of Complex Unit Gain Graphs, Linear Algebra Appl. 436 (2012), 3165-3176, arXiv:1110.4554, DOI 10.1016/j.laa.2011.10.021
  - classical gain-graph switching/balance theorem: a gain graph is balanced iff it is switching-equivalent to the trivial gain; every gain assignment on a tree is balanced
---

# WP-407 — Acyclic block-positive dilations are phase-gauge blind

## Claim

`WP-406` showed that the most immediate `2 x 2` positive linking-matrix escape from `WP-405` is too cheap: every bounded source element admits a positive scalar-diagonal completion, and scalar phase is invisible to that positivity. A natural next move is to replace the single link by a larger source-forced block system with nontrivial diagonal blocks and several couplings.

There is an exact obstruction before any arithmetic input enters. Let `G=(V,E)` be a finite graph, let `A` be a unital `C*`-algebra, and let

\[
P=[P_{ij}]\in M_{|V|}(A)
\]

be Hermitian with arbitrary self-adjoint diagonal blocks `P_{ii}=a_i=a_i^*`, arbitrary off-diagonal blocks `P_{ij}=x_{ij}` on the oriented edges, `P_{ji}=x_{ij}^*`, and zero off the graph. Give every oriented edge a central scalar phase

\[
\omega_{ij}\in\mathbb T,
\qquad
\omega_{ji}=\overline{\omega_{ij}},
\]

and form the phase-twisted Hermitian block matrix `P^omega` by

\[
(P^\omega)_{ii}=a_i,
\qquad
(P^\omega)_{ij}=\omega_{ij}x_{ij}.
\]

If the phase field is a vertex coboundary,

\[
\omega_{ij}=u_i\overline{u_j}
\qquad (u_i\in\mathbb T),
\]

then with `U=diag(u_i1_A)` one has the exact unitary equivalence

\[
\boxed{P^\omega=UPU^*.}
\]

Hence

\[
\boxed{P^\omega\succeq0\iff P\succeq0.}
\]

Every scalar gain assignment on a forest is a coboundary. Therefore **every acyclic block-positive completion is exactly blind to all independent scalar edge phases**, even when its diagonal blocks are non-scalar, unequal, source-forced, or otherwise highly structured. Replacing the scalar bath of `WP-406` by a chain, star, or arbitrary tree of source-derived diagonal blocks does not create a scalar phase orientation.

For a graph with cycles, choose a spanning forest. Switching gauges all forest-edge phases to `1`; the remaining chord phases are exactly representatives of cycle holonomy. Thus scalar edge phases modulo corner gauge have one invariant per independent cycle. If `G` has `c` connected components, the number of independent `U(1)` phase degrees of freedom is

\[
\boxed{|E|-|V|+c.}
\]

Accordingly, **a cycle is the first place where scalar phase can affect positivity at all**. This boundary is sharp: a `3 x 3` scalar triangle has a determinant that depends on the cycle holonomy and can change sign when only that holonomy changes.

This does not make a cyclic completion arithmetic. It only identifies a necessary structural condition for a phase-sensitive positive block route. A surviving Mathia construction must still source-force the cycle and its holonomy, survive matched generalized/non-arithmetic controls, and recover the finite plus archimedean Weil destination without choosing the holonomy to fit the desired sign.

**Classification:** `EXACT-DERIVED + CENTRAL-U1-GAIN-SWITCHING + ACYCLIC-BLOCK-POSITIVITY-PHASE-BLINDNESS + ARBITRARY-DIAGONAL-BLOCKS + CYCLE-HOLONOMY-FIRST-INVARIANT + SHARP-TRIANGLE-CONTROL + GAIN-GRAPH-PRIOR-ART-CLASSICALIZATION + SOURCE-PROVENANCE-STILL-REQUIRED + NOT-WEIL-POSITIVITY`.

## 1. Vertex switching is unitary conjugacy of the full block matrix

Let `u=(u_i)_{i\in V}` with `|u_i|=1` and put

\[
U=\operatorname{diag}(u_i1_A)\in M_{|V|}(A).
\]

Because every `u_i` is a central scalar, the diagonal blocks are fixed:

\[
(UPU^*)_{ii}
=u_i a_i\overline{u_i}
=a_i.
\]

On an edge `ij`,

\[
(UPU^*)_{ij}
=u_i x_{ij}\overline{u_j}
=(u_i\overline{u_j})x_{ij}.
\]

Thus the scalar gain transformation

\[
\omega_{ij}=u_i\overline{u_j}
\]

is literally unitary conjugation of the complete operator-valued block matrix, not merely a similarity of a scalar adjacency matrix. Positivity, spectrum, invertibility, inertia, determinant in finite scalar representations, and every unitarily invariant positive readout are unchanged.

The important point for `WP-406` is that this argument makes **no assumption at all on the diagonal blocks beyond self-adjointness**. They may be source-forced and may carry all the nontrivial local operator structure one wants. Acyclic scalar phase still gauges away because the corner unitary is scalar and therefore commutes with every diagonal block.

## 2. Every phase field on a forest gauges away

Suppose first that `G` is a tree. Choose a root `r` and set `u_r=1`. Traverse away from the root. If `i` is the parent of `j`, define

\[
u_j=\overline{\omega_{ij}}u_i.
\]

Then

\[
u_i\overline{u_j}=\omega_{ij}.
\]

Because a tree has a unique path from the root to each vertex, this recursively defines a consistent vertex phase on the entire graph. Hence every edge phase is a coboundary and can be removed by the unitary `U` above. The same construction is applied separately on each component of a forest.

Therefore, for every forest,

\[
\boxed{
P^\omega\succeq0
\iff
P\succeq0
\quad\text{for every edge-phase assignment }\omega.
}
\]

This is stronger than the single-edge result of `WP-406`. There the diagonal bath was scalar and sufficiently large, so positive completion itself was universal. Here the diagonal blocks may be fixed in advance, non-scalar, and source-derived; positivity may be highly nontrivial as a function of amplitudes and diagonal data, but it remains completely insensitive to the entire scalar phase field as long as the coupling graph is acyclic.

The corresponding matched control is exact. Hold fixed the graph, every diagonal block `a_i`, and every operator-valued edge block `x_{ij}`, while replacing each arithmetic scalar edge phase by an arbitrary independent `\mathbb T`-valued phase. On a forest the resulting matrices are all unitarily equivalent. No positivity theorem on that family can select the arithmetic phase from those alternatives.

## 3. Cycles are exactly the first scalar phase invariants

Now let `G` be arbitrary. Choose a spanning forest `T`. By the tree argument there is a vertex switching that makes every phase on `T` equal to `1`. Each remaining edge `e` closes a unique fundamental cycle with the tree. After the tree phases have been fixed, the phase left on `e` is the ordered product of the original gains around that cycle.

Equivalently, for every oriented cycle

\[
C=(v_0,v_1,\ldots,v_k=v_0),
\]

define its scalar holonomy

\[
\operatorname{Hol}_\omega(C)
:=
\prod_{j=0}^{k-1}\omega_{v_jv_{j+1}}.
\]

Under vertex switching every factor acquires `u_{v_j}\overline{u_{v_{j+1}}}`, and these factors telescope. Hence `Hol_omega(C)` is gauge-invariant. Conversely, after fixing a spanning forest, the holonomies of the fundamental cycles determine the switching class of a `U(1)` gain field.

Thus the quotient of edge phases by corner gauge has dimension equal to the first Betti number

\[
\boxed{b_1(G)=|E|-|V|+c.}
\]

For a forest `b_1=0`; there is no scalar phase datum left for positivity to detect. For a graph with a cycle, a genuine gauge-invariant phase survives and positivity can in principle depend on it.

This is the finite block-completion analogue of the flat-versus-holonomy distinction encountered earlier in `WP-297` and `WP-299`, but the statement is different. `WP-299` assumed an exactly source-equivariant linear response and proved that the source-generated image lies in the fixed sector of output holonomy. The present result assumes no source intertwiner at all: it classifies which scalar phases can even survive as invariants of the positive block matrix before any response map is imposed.

## 4. Triangle control: cycle holonomy can really change positivity

The cycle boundary is not only necessary; it is sharp. Consider the scalar Hermitian triangle

\[
P_\Phi=
\begin{pmatrix}
1&r&r e^{-i\Phi}\\
r&1&r\\
r e^{i\Phi}&r&1
\end{pmatrix},
\qquad 0<r<1.
\]

All one- and two-vertex principal minors are independent of `Phi`. The determinant is

\[
\boxed{
\det P_\Phi
=1-3r^2+2r^3\cos\Phi.
}
\]

Set `r=3/5`. Then the `2 x 2` principal minors are

\[
1-r^2=\frac{16}{25}>0.
\]

At trivial holonomy,

\[
\det P_0
=\frac{44}{125}>0,
\]

so `P_0` is positive definite. At holonomy `Phi=pi`,

\[
\det P_\pi
=-\frac{64}{125}<0,
\]

so `P_pi` is indefinite. The diagonal blocks, edge magnitudes, graph, and every tree-edge gauge choice are unchanged; only the cycle holonomy differs.

This control proves exactly what the forest theorem leaves open: **cycle holonomy can enter positivity**, and the smallest simple scalar architecture where that happens is a triangle. It does not prove that an arithmetic cycle has been found.

## 5. What this closes after `WP-406`

`WP-406` left open the possibility that source-forced diagonal blocks or a more structured linking construction might prevent the trivial scalar bath from swallowing the arithmetic phase. The present result splits that escape cleanly.

If the structured linking graph is acyclic, source-forcing the diagonals does not help with scalar phase selection. A chain of boundary sectors, a star around an archimedean corner, or any tree of local prime/auxiliary sectors remains phase-gauge blind. Positivity may constrain norms and amplitudes, but it cannot distinguish the physical scalar phase assignment from an arbitrary phase control on the same edges.

If the graph contains cycles, positivity may see only the gauge-invariant cycle holonomies. Therefore a phase-sensitive continuation must explain why the **source itself canonically supplies a particular cycle and holonomy**. Merely introducing a loop and choosing its phase from the target would be another programmable completion, not an independently signed arithmetic mechanism.

This also sharpens `WP-351`. There, standard contraction-defect positivity forgot one global scalar phase. Here an entire independent family of edge phases is invisible on every forest, while cycles identify exactly what additional scalar phase information could survive ordinary corner gauge.

## 6. Arithmetic provenance remains the decisive gate

The gain-graph mechanism is generic. Replace rational primes by arbitrary generator labels, preserve the same coupling graph, diagonal blocks, edge amplitudes, and cycle gains, and the switching theorem is unchanged. Nothing in the acyclic no-go or the cyclic sharpness control singles out rational primes, Mangoldt weights, or the completed zeta function.

Consequently the first potentially useful cyclic construction must pass a stricter test than `P>=0`:

1. the vertices and edges must be forced by the source geometry rather than chosen to manufacture a loop;
2. the surviving holonomy must be source-derived and stable under legitimate changes of presentation;
3. generalized-prime or randomized matched controls must fail for an arithmetic reason rather than because labels were hard-coded;
4. the same construction must account for the finite prime terms and the archimedean/polar compensation under one audited normalization;
5. the sign theorem must precede, not follow from, tuning the cycle holonomy to the desired Weil sign.

Until those conditions are met, a cyclic block matrix is only a generic gain-graph device that happens to admit phase-sensitive positivity.

## Representation audit

The primary object is the Hermitian operator-valued block matrix `P in M_|V|(A)`. The only phase freedom considered is a **central scalar** `U(1)` gain on each oriented edge. This restriction is deliberate: it isolates exactly the scalar phase-selection problem left by `WP-351`, `WP-405`, and `WP-406`, while allowing completely arbitrary operator-valued edge amplitudes and diagonal blocks.

The theorem does not claim that non-central operator-valued gains are classified by scalar cycle holonomy. Nor does it say that acyclic positivity is trivial: amplitudes and diagonal blocks can still decide positivity. It says only that scalar edge phases cannot do so on a forest.

The triangle is a scalar finite-dimensional witness for sharpness, not an arithmetic model. No zeta zeros, RH assumption, regularization, or target Weil kernel enters the derivation.

## Prior-art and novelty audit

The switching theory is classical gain-graph mathematics. In particular, complex unit gain graphs, switching equivalence, balance, and the fact that every gain assignment on a tree is balanced are standard; Reff's 2012 treatment is a direct literature anchor. The statement that switching corresponds to diagonal unitary conjugation of gain-graph matrices is likewise standard. None of that is claimed as new mathematics.

The derived contribution here is the line-specific obstruction obtained by applying that classical switching structure to the operator-valued positive block completions left open by `WP-406`: arbitrary source-forced diagonal blocks do **not** rescue scalar phase selectivity on any acyclic coupling architecture, because central corner switching leaves those diagonals fixed. The exact sharp boundary is then a cycle holonomy, with the triangle calculation showing that positivity can genuinely become holonomy-sensitive once that boundary is crossed.

This is not a global Weil positivity theorem and does not supply a canonical arithmetic cycle. It removes a broad class of structured but acyclic block completions and identifies the first extra datum that a surviving block-positive route must source-force.

## Verdict

**Supported exact negative with a sharp boundary.** For central scalar edge phases, every forest-valued Hermitian block completion is gauge-equivalent to its all-positive-phase representative, independently of how nontrivial the diagonal blocks are. Therefore acyclic linking positivity cannot orient the scalar arithmetic phase. The first possible phase-sensitive invariant is cycle holonomy, and a triangle already shows that changing only that holonomy can flip positivity.

The next admissible block-positive route is consequently not “use more blocks” but **derive a canonical cyclic coupling with source-forced holonomy and then test whether its positivity survives arithmetic matched controls and the full finite--archimedean Weil normalization**.