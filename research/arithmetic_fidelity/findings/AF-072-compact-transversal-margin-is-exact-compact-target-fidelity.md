# AF-072 — Compact-transversal margin exactly classifies compact-target fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a real normed space. Let `\mathcal K` be a nonempty family of cones in `V`, each containing `0`, and let `L\subseteq V` be a closed cone containing `0`. Retain

\[
H_{\mathcal K}(S)
=
\bigcap_{K\in\mathcal K}(S-K),
\]

and say that `L` is a **compact-target consequence** of `\mathcal K` when

\[
H_{\mathcal K}(S)\subseteq S-L
\qquad
\text{for every nonempty compact }S\subset V.
\tag{1}
\]

Write

\[
\mathbb S_V=\{u\in V:\|u\|=1\}.
\]

A **compact unit-direction transversal** for `\mathcal K` is a norm-compact set

\[
C\subseteq\mathbb S_V
\]

such that

\[
C\cap K\ne\varnothing
\qquad\forall K\in\mathcal K.
\tag{2}
\]

Let `\mathfrak T_c(\mathcal K)` be the family of all such transversals. For compact `C` put

\[
d(C,L)=\inf_{u\in C}d(u,L),
\]

and define the **compact-transversal margin**

\[
\tau_{\mathcal K}(L)
=
\sup_{C\in\mathfrak T_c(\mathcal K)}d(C,L),
\tag{3}
\]

with the explicit convention `\tau_{\mathcal K}(L)=0` when `\mathfrak T_c(\mathcal K)=\varnothing`. Since `0\in L` and `C\subseteq\mathbb S_V`, always `0\le\tau_{\mathcal K}(L)\le1`.

Then:

1. **Compact-target fidelity is exactly compact-transversal intersection.**
   \[
   \boxed{
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   C\cap L\ne\varnothing
   \quad\forall C\in\mathfrak T_c(\mathcal K).
   }
   \tag{4}
   \]
   Equivalently,
   \[
   \boxed{
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   \tau_{\mathcal K}(L)=0.
   }
   \tag{5}
   \]
   Thus the exact obstruction to compact-target consequence is not merely a direction that stays away from `L`, but a **simultaneously realizable compact family of unit directions** that hits every retained cone while remaining uniformly separated from `L`.

2. **The compact-transversal margin is always bounded by AF-071's normalized excess.** With
   \[
   \varepsilon(K\mid L)
   =
   \sup_{x\in K\setminus\{0\}}
   \frac{d(x,L)}{\|x\|},
   \qquad
   \delta_{\mathcal K}(L)
   =
   \inf_{K\in\mathcal K}\varepsilon(K\mid L),
   \tag{6}
   \]
   one has
   \[
   \boxed{
   0\le\tau_{\mathcal K}(L)\le\delta_{\mathcal K}(L)\le1.
   }
   \tag{7}
   \]
   Normalized excess measures how far each cone can individually reach from `L`; `\tau` measures how much of that separation can be realized **simultaneously inside one compact directional witness**.

3. **Collective directional precompactness makes the two defects identical.** If
   \[
   U_{\mathcal K}
   =
   \bigcup_{K\in\mathcal K}(K\cap\mathbb S_V)
   \tag{8}
   \]
   has norm-compact closure, then
   \[
   \boxed{
   \tau_{\mathcal K}(L)=\delta_{\mathcal K}(L).
   }
   \tag{9}
   \]
   Hence AF-071's precompact-direction criterion is not only sufficient to recover the zero/nonzero test: it makes normalized excess exactly equal to the compactly realizable separation margin.

4. **AF-071's infinite-dimensional escape example is explained exactly by loss of compact transversals.** For pairwise uniformly separated unit vectors `(u_n)` and rays
   \[
   K_n=\mathbb R_{\ge0}u_n,
   \qquad
   \mathcal K=\{K_n:n\ge1\},
   \qquad
   L=\{0\},
   \tag{10}
   \]
   AF-071 gives
   \[
   \delta_{\mathcal K}(\{0\})=1
   \quad\text{and}\quad
   \{0\}\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K).
   \]
   Here in fact
   \[
   \mathfrak T_c(\mathcal K)=\varnothing,
   \qquad
   \tau_{\mathcal K}(\{0\})=0.
   \tag{11}
   \]
   Every unit transversal would have to contain every `u_n`, impossible for a compact set because the directions are uniformly separated.

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\begin{array}{c}
\text{pointwise directional separation is not the exact compact-target obstruction;}\\
\text{the exact obstruction is compactly realizable simultaneous separation.}
\end{array}}
\tag{12}
\]

This replaces the finite-/infinite-dimensional dichotomy by a direct witness criterion that works in every normed space.

## Derivation

### Any failed compact-target consequence normalizes to a compact transversal

Assume that `L` is **not** a compact-target consequence. Then some nonempty compact `S\subset V` and some

\[
m\in H_{\mathcal K}(S)\setminus(S-L)
\tag{13}
\]

exist. Put

\[
A=S-m.
\tag{14}
\]

Because `m\in S-K` for every `K\in\mathcal K`, the translated compact set `A` meets every cone:

\[
A\cap K\ne\varnothing
\qquad\forall K\in\mathcal K.
\tag{15}
\]

Moreover,

\[
m\notin S-L
\iff
A\cap L=\varnothing.
\tag{16}
\]

Since `0\in L`, equation (16) implies `0\notin A`. Compactness therefore gives

\[
r:=\min_{a\in A}\|a\|>0.
\tag{17}
\]

The normalization map

\[
N:V\setminus\{0\}\to\mathbb S_V,
\qquad
N(a)=\frac{a}{\|a\|},
\tag{18}
\]

is continuous on `A`, so

\[
C=N(A)
\tag{19}
\]

is norm-compact. Because every `K` is a cone, (15) implies `C\cap K\ne\varnothing` for every `K`. Thus `C\in\mathfrak T_c(\mathcal K)`.

Because `L` is also a cone, `C\cap L=\varnothing`: if `a/\|a\|\in L`, then positive homogeneity gives `a\in L`, contradicting (16). Finally, a compact set disjoint from a closed set has positive distance, so

\[
d(C,L)>0.
\tag{20}
\]

Hence every failed compact-target consequence produces a compact transversal with positive margin, and therefore

\[
L\notin\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
\Longrightarrow
\tau_{\mathcal K}(L)>0.
\tag{21}
\]

### Any compact transversal avoiding `L` is already a falsifying target

Conversely, let `C\in\mathfrak T_c(\mathcal K)` satisfy `C\cap L=\varnothing`. Since `C` meets every `K`,

\[
0\in C-K
\qquad\forall K\in\mathcal K,
\]

so

\[
0\in H_{\mathcal K}(C).
\tag{22}
\]

But

\[
0\in C-L
\iff
C\cap L\ne\varnothing,
\tag{23}
\]

which is false. Therefore `C` itself violates (1). This proves (4).

Because `L` is closed and `C` is compact, `C\cap L=\varnothing` is equivalent to `d(C,L)>0`. Taking the supremum over compact transversals yields (5). Notice that if there is **no** compact unit-direction transversal, (5) says compact-target consequence holds automatically. This is not a convention-induced artifact: if consequence failed, the normalization argument above would construct such a transversal.

### Comparison with normalized excess

Because `L` is a cone,

\[
\varepsilon(K\mid L)
=
\sup_{u\in K\cap\mathbb S_V}d(u,L)
\tag{24}
\]

whenever `K` contains a nonzero vector; for `K=\{0\}` the normalized excess is `0` by convention.

Fix a compact transversal `C`. For each `K` choose `u_K\in C\cap K`. Then

\[
d(C,L)
\le d(u_K,L)
\le\varepsilon(K\mid L).
\tag{25}
\]

Since this holds for every `K`,

\[
d(C,L)\le\delta_{\mathcal K}(L).
\tag{26}
\]

Taking the supremum over `C` proves `\tau\le\delta`. If some `K=\{0\}`, there is no unit transversal, while `\delta=0`; the same inequality and exact consequence criterion remain valid.

### Precompact directions realize every subcritical normalized margin

Assume now that `\overline{U_{\mathcal K}}` is norm-compact. If `\delta_{\mathcal K}(L)=0`, (7) already gives `\tau=0`. Suppose instead that

\[
\delta_{\mathcal K}(L)>0
\]

and choose any

\[
0<\eta<\delta_{\mathcal K}(L).
\tag{27}
\]

Define

\[
A_\eta
=
U_{\mathcal K}
\cap
\{u:d(u,L)\ge\eta\}.
\tag{28}
\]

For every `K`, equation (24) and `\varepsilon(K\mid L)\ge\delta>\eta` provide some unit vector of `K` with distance strictly larger than `\eta`; hence `A_\eta` meets every `K`. Its closure

\[
C_\eta=\overline{A_\eta}
\tag{29}
\]

is compact, lies in the unit sphere, remains a transversal because it contains `A_\eta`, and satisfies

\[
d(C_\eta,L)\ge\eta
\tag{30}
\]

because `{u:d(u,L)\ge\eta}` is closed. Therefore `\tau\ge\eta` for every `\eta<\delta`, so

\[
\tau_{\mathcal K}(L)\ge\delta_{\mathcal K}(L).
\tag{31}
\]

Together with (7), this proves (9).

## Exact controls

### A zero cone forces consequence and destroys unit transversals

If some `K_0=\{0\}` belongs to `\mathcal K`, then every `m\in H_{\mathcal K}(S)` already lies in `S`, hence in `S-L` because `0\in L`. Thus every such `L` is a compact-target consequence. At the same time no subset of the unit sphere can meet `K_0`, so `\mathfrak T_c(\mathcal K)=\varnothing` and `\tau=0`. The criterion handles this degeneracy without an extra exception.

### A single nonzero cone has no simultaneous-selection defect

If `\mathcal K=\{K\}` with `K\ne\{0\}`, every unit vector `u\in K` is itself a compact transversal. Therefore

\[
\tau_{\{K\}}(L)
=
\sup_{u\in K\cap\mathbb S_V}d(u,L)
=
\varepsilon(K\mid L).
\tag{32}
\]

The gap between `\tau` and `\delta` is consequently a genuinely **family-level** phenomenon: it appears only when separated witnesses from many constraints must be realized simultaneously inside one compact set.

### Finite-dimensional spaces recover AF-070 automatically

In finite-dimensional `V`, the unit sphere is compact, so every `U_{\mathcal K}` has compact closure. Equation (9) gives `\tau=\delta` for every cone family. Combining this with (5) recovers AF-070's normalized-excess classification without a separate compactness argument.

### Directional escape is the sharp opposite control

For AF-071's separated rays, any unit transversal must contain the unique unit vector on each ray, hence contains the uniformly separated set `{u_n}`. Such a set cannot be relatively compact. Thus no compact transversal exists, `\tau=0`, and compact-target consequence holds despite maximal normalized excess `\delta=1`. This is the strongest possible separation between the pointwise and compactly realizable margins.

## Prior art and novelty assessment

The ingredients are classical. Normalization away from the origin, compact-versus-closed positive distance, and cone homogeneity are elementary. Gap/excess functionals belong to classical hyperspace and variational set-distance theory; Gerald Beer's *Topologies on Closed and Closed Convex Sets* gives a standard reference for gap and excess functionals. Measures of noncompactness, developed from Kuratowski's compactness ideas and treated systematically by Banaś and Goebel, provide the established neighboring language for quantifying when bounded families fail to be relatively compact. In particular, separation-based measures of noncompactness explain why AF-071's uniformly separated directions cannot be packed into a compact witness.

A targeted search across compact-transversal/hitting-set terminology for families of cones and Banach-space noncompactness did not locate the exact equivalence (4)–(5). That search result is **not** evidence of novelty, and no novelty is claimed for compact hitting sets, measures of noncompactness, or the elementary normalization argument. The durable contribution is the Arithmetic Fidelity organization of these mechanisms into an exact category-specific classifier: compact-target consequence is controlled by compact simultaneous directional transversals, while normalized excess is only a pointwise relaxation and becomes exact precisely when the available directions are collectively precompact.

Literature anchors:

- Gerald Beer, ***Topologies on Closed and Closed Convex Sets***, Mathematics and Its Applications 268, Kluwer (1993), DOI `10.1007/978-94-015-8149-3`. Role: classical framework for gap/excess functionals and set convergence.
- Józef Banaś and Kazimierz Goebel, ***Measures of Noncompactness in Banach Spaces***, Lecture Notes in Pure and Applied Mathematics 60, Marcel Dekker (1980), ISBN `0-8247-1248-X`. Role: classical systematic treatment of measures of noncompactness; neighboring language for the compactness resource whose failure creates directional escape.
- James C. Robinson, ***An Introduction to Functional Analysis***, Cambridge University Press (2020), Chapter 5, DOI `10.1017/9781139030267`. Role: standard Riesz-lemma and finite-dimensional compactness background already used in AF-071; it supplies the canonical separated-direction control against which the compact-transversal criterion is tested.

## Boundary conditions and audit

- Compactness and closedness are **norm-topological** throughout. Replacing norm compactness by weak compactness changes the witness category and requires a separate theorem.
- `L` must be closed for the quantitative equivalence between disjointness and positive compact-set distance. The set-theoretic intersection criterion (4) itself does not need closedness, but the margin formulation (5) does.
- Cone homogeneity is load-bearing twice: it makes normalization preserve membership in every `K`, and it makes disjointness from `L` survive normalization.
- The criterion concerns compact targets. For arbitrary or merely bounded targets the normalization image need not be compact, exactly matching the failures already isolated in AF-069.
- `\tau` is an exact **fidelity classifier**, not asserted to be a complete metric on cone families or a canonical measure of noncompactness. Different families may have the same `\tau` for a given `L` while differing strongly elsewhere.
- The inequality `\tau\le\delta` can be strict even maximally, as AF-071 shows. Therefore pointwise margin arguments cannot replace compact-transversal analysis outside a precompact directional regime.
- No arithmetic specialization is used. Any later prime/RH application must identify its actual constraint family, target category, and retained cone-like geometry before importing this theorem.

## Consequences for Arithmetic Fidelity

AF-071 separated two mechanisms—directional approach and directional escape—but still expressed the first through normalized excess and the second through an example. AF-072 closes that gap: **one exact witness object, the compact unit-direction transversal, governs both**.

The practical audit is now dimension-free. Given a family of retained directional constraints, first ask whether a compact simultaneous transversal avoiding the candidate consequence exists. If yes, it is already a concrete compact falsifier. If no, compact-target consequence holds even when every individual cone remains far from the candidate in normalized excess. Collective directional precompactness is precisely the regime in which the cheaper pointwise quantity `\delta` can replace this simultaneous-transversal test.

For the wider program, this gives a reusable warning about compression: a family can preserve strong discriminator directions one constraint at a time while no compactly realizable object preserves them **together**. The missing structure is then not another scalar invariant but a compactness/coherence condition on simultaneous witnesses. Any transfer to arithmetic, spectral, or positivity settings must prove an analogue of that coherence rather than infer global fidelity from large local margins.