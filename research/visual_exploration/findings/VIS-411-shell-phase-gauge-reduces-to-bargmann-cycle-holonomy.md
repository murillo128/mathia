# VIS-411 — independent shell phases reduce to Bargmann cycle holonomy

## Claim

Let

`F=(f_1,...,f_K)`

be a finite labelled family of nonzero vectors in a complex Hilbert space, and write

`G_(jk)=<f_j,f_k>`

for its Gram matrix. Let the **frame graph** have vertices `1,...,K` and an undirected edge `{j,k}` exactly when `G_(jk) != 0`.

Suppose the individual shell representatives are meaningful only up to independent phase choices

`f_j -> exp(i alpha_j) f_j`.

Then the phase of an individual off-diagonal Gram entry is not intrinsic:

`G_(jk) -> exp(i(alpha_k-alpha_j)) G_(jk)`.

By contrast, for every oriented cycle

`C=(i_1,i_2,...,i_m,i_1)`

the cyclic product

`Delta_C = G_(i_1 i_2) G_(i_2 i_3) ... G_(i_m i_1)`

is exactly invariant. These are the pure-state Bargmann cycle invariants.

More strongly, on every connected component of the frame graph, the edge magnitudes together with Bargmann invariants for any fundamental cycle basis determine the entire Gram matrix on that component **up to the independent vertex-phase gauge**. Choose a spanning tree `T`; phase-gauge the tree edges to be positive real. Every non-tree edge closes one unique fundamental cycle, and the phase of its cycle product then fixes the phase of that edge. Thus there is no further pairwise phase information hidden outside the cycle holonomies.

When all pairwise overlaps are nonzero, a star tree rooted at shell `1` shows that the pairwise magnitudes together with the triangular invariants

`Delta_(1jk)=G_(1j) G_(jk) G_(k1)`

for `2 <= j < k <= K` already reconstruct the Gram matrix up to diagonal phase gauge.

Equivalently, if `P_j=|f_j><f_j|`, then

`tr(P_j P_k)=|G_(jk)|^2`

and

`tr(P_i P_j P_k)=G_(ij) G_(jk) G_(ki)`.

So the first phase-sensitive relational scalars that survive independent shell rephasing are closed-cycle quantities, not raw pairwise phases.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-BARGMANN/FINITE-FRAME-INVARIANTS + DECISIVE-REPRESENTATION-CONTROL + NO-NOVELTY-CLAIM`.

This does not identify a new arithmetic invariant. It identifies the correct gauge quotient for the multi-shell coherence left open by `VIS-410`.

## 1. Edge phases are a vertex-gauge field

Use the standard convention in which the inner product is conjugate-linear in the first argument. Under

`f_j' = exp(i alpha_j) f_j`,

one has

`G'_(jk)=exp(i(alpha_k-alpha_j)) G_(jk)`.

Thus an edge phase transforms by the difference of two vertex phases. In graph language, the edge phase is a `U(1)` one-cochain and changing shell representatives adds a vertex coboundary.

Take an oriented cycle `C=(i_1,...,i_m,i_1)`. Multiplying the transformed overlaps gives the phase factor

`exp(i[(alpha_(i_2)-alpha_(i_1))+...+(alpha_(i_1)-alpha_(i_m))])=1`.

Hence `Delta_C` is gauge invariant. Reversing the cycle conjugates the invariant, as expected.

The magnitude of `Delta_C` contains no new information once the edge magnitudes are known:

`|Delta_C| = product_(edges e in C) |G_e|`.

The additional relational information is its cycle phase.

## 2. A spanning tree fixes the gauge and the remaining chords are cycle phases

Assume first that the frame graph component is connected. Choose a spanning tree `T` and a root `r`.

Because a tree has no cycles, phases can be chosen recursively from the root so that every oriented tree overlap is positive real. There is no consistency obstruction: each new vertex is reached for the first time along exactly one tree edge.

Now let `e={u,v}` be a non-tree edge. The tree path from `u` to `v` together with `e` forms one fundamental cycle `C_e`. In the tree gauge, every tree factor on that cycle is real with known positive magnitude. Therefore the argument of `Delta_(C_e)` determines the argument of `G_(uv)` up to the orientation convention, while `|G_(uv)|` is already known.

Doing this for every chord reconstructs every nonzero Gram entry. Since a connected graph with `|V|` vertices and `|E|` edges has `|E|-|V|+1` independent fundamental cycles, this is exactly the number of residual edge phases left after quotienting the `|V|-1` effective vertex phases.

For a disconnected frame graph, the argument applies independently to each connected component. Relative phases between orthogonal components are unobservable because no nonzero overlap joins them.

## 3. Complete-overlap families reduce to triangles

If all `G_(jk)` are nonzero, choose the star tree with root `1`. Gauge all `G_(1j)` to be positive real.

For every pair `j,k>1`,

`Delta_(1jk)=G_(1j) G_(jk) G_(k1)`

has the same phase as `G_(jk)` in this gauge because the two root edges are positive real. Therefore the set

- norms `G_(jj)`;
- magnitudes `|G_(jk)|`;
- triangular Bargmann phases `arg Delta_(1jk)`;

reconstructs the full Gram matrix up to independent shell rephasing.

This does not make triangles universally sufficient on a sparse frame graph: a missing chord can force a longer fundamental cycle. The correct invariant object is the cycle space of the nonzero-overlap graph.

## 4. Operator form removes representative phases entirely

The rank-one shell projectors

`P_j=|f_j><f_j|`

are individually invariant under `f_j -> exp(i alpha_j) f_j`. Direct multiplication gives

`tr(P_j P_k)=|<f_j,f_k>|^2`

and

`tr(P_i P_j P_k)`
` = <f_i,f_j><f_j,f_k><f_k,f_i>`.

More generally,

`tr(P_(i_1) ... P_(i_m)) = Delta_C`

for the corresponding cycle. Hence Bargmann cycles are not an arbitrary phase-fixing convention: they are representative-free operator invariants of the shell rays themselves.

This sharpens the interpretation of `VIS-410`. The full matrix-valued cross-Wigner field retains the labelled vectors up to one common phase, so it contains raw relative shell phases when those representatives are part of the source data. But if the source construction itself specifies only shell rays, then independent shell rephasing is a genuine representation gauge. In that quotient, an individual cross-Wigner block phase is not intrinsic; closed-cycle combinations are.

## 5. Prior art and novelty boundary

The load-bearing invariant theory is classical. Tuan-Yow Chien and Shayne Waldron, **A Characterization of Projective Unitary Equivalence of Finite Frames and Applications**, *SIAM Journal on Discrete Mathematics* 30:2 (2016), 976–994, DOI `10.1137/15M1042140`, characterize projective unitary equivalence of finite frames by Bargmann/projective invariants and use the frame graph plus a small invariant set for reconstruction. This directly bounds novelty for the spanning-tree/cycle reconstruction above.

Michał Oszmaniec, Daniel J. Brod, and Ernesto F. Galvão, **Measuring relational information between quantum states, and applications**, *New Journal of Physics* 26 (2024), 013053, DOI `10.1088/1367-2630/ad1a27`, formulate the same relational-information problem in terms of state overlaps and higher Bargmann invariants and explicitly use a frame graph and spanning tree to recover projective-unitary information.

The older geometric-phase literature likewise treats cyclic overlap products as Bargmann invariants; for example N. Mukunda, Arvind, S. Chaturvedi, and R. Simon, **Bargmann invariants and off-diagonal geometric phases for multilevel quantum systems: a unitary-group approach**, *Physical Review A* 65 (2001), 012102, DOI `10.1103/PhysRevA.65.012102`.

No novelty is claimed for Bargmann invariants, frame graphs, cycle-space reconstruction, or projective-unitary equivalence. The Mathia-specific value is the **representation boundary following `VIS-409` and `VIS-410`**: once independent shell phases are treated as gauge, a multi-shell phase-space visualization should be judged through closed-cycle relational invariants rather than visually salient pairwise phase patterns.

## 6. Research consequence

A future multi-shell visual experiment should first state whether the source supplies **vectors with fixed relative phases** or only **projective shell rays**. In the first case the full cross-Wigner matrix may legitimately retain relative coherence already present in the source, as `VIS-410` states. In the second case any claim based on an individual off-diagonal phase is gauge-dependent and should be rejected or rewritten in terms of Bargmann cycles.

This gives a sharper admissibility test for the next positive direction. A source-derived cross-shell mechanism must force a cycle invariant, a family of cycle invariants, or another explicitly gauge-invariant relation that differs from matched controls for an intrinsic arithmetic reason. A striking cross-Wigner interference pattern is not sufficient unless its claimed content survives the shell-phase quotient.

Determining whether the current Wang/prime-circle source constructions actually force such nontrivial cycle laws is a separate research question and is intentionally left for a later invocation.