# AF-074 — Precompact finite witness pools exactly characterize compact-transversal fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a real Banach space with unit sphere

\[
\mathbb S_V=\{u\in V:\|u\|=1\}.
\]

Let `\mathcal K` be a nonempty family of **closed cones** in `V`, each containing `0`, and let `L\subseteq V` be a closed cone containing `0`. Retain AF-072's compact unit-direction transversals and margin

\[
\tau_{\mathcal K}(L)
=
\sup_{C\in\mathfrak T_c(\mathcal K)}d(C,L),
\tag{1}
\]

with value `0` when no compact transversal exists. Retain AF-073's finite-set gap

\[
g(F,K)
=
\inf\{\|f-u\|:f\in F,\ u\in K\cap\mathbb S_V\},
\tag{2}
\]

with `g(F,\{0\})=+\infty`, and write

\[
m_L(F)=d(F,L).
\tag{3}
\]

A **precompact finite approximation scheme at margin `\eta\ge0`** is a sequence of nonempty finite sets

\[
F_n\subseteq\mathbb S_V
\]

and positive errors `\varepsilon_n\to0` such that

\[
g(F_n,K)\le\varepsilon_n
\quad\forall K\in\mathcal K,\ \forall n,
\qquad
m_L(F_n)\ge\eta
\quad\forall n,
\tag{4}
\]

and the pooled witness set

\[
A=\bigcup_{n\ge1}F_n
\tag{5}
\]

is relatively norm-compact in `V`.

Define

\[
\kappa_{\mathcal K}(L)
=
\sup\{\eta\ge0:\text{a precompact finite approximation scheme at margin }\eta\text{ exists}\},
\tag{6}
\]

with value `0` if no such scheme exists. Then:

1. **Precompact finite witness pools recover exactly the compact-transversal margin.**
   \[
   \boxed{
   \kappa_{\mathcal K}(L)=\tau_{\mathcal K}(L).
   }
   \tag{7}
   \]
   Thus the exact finite-resolution resource is not a prescribed correspondence between every consecutive approximation. It is the existence of arbitrarily accurate finite witnesses whose **union stays inside one compact reservoir**.

2. **Compact-target fidelity has an equivalent precompactness certificate.** By AF-072,
   \[
   \boxed{
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   \kappa_{\mathcal K}(L)=0.
   }
   \tag{8}
   \]

3. **AF-073's explicit Hausdorff coherence and pooled precompactness are equivalent at the existence level.** Let `\theta_{\mathcal K}(L)` be AF-073's coherent finite-tower margin. Then
   \[
   \boxed{
   \kappa_{\mathcal K}(L)=\theta_{\mathcal K}(L)=\tau_{\mathcal K}(L).
   }
   \tag{9}
   \]
   More precisely, every precompact approximation scheme contains a subsequence that satisfies AF-073's summable Hausdorff-coherence condition after choosing suitable summable error bounds, while every AF-073 coherent tower has relatively compact pooled witnesses.

4. **Adjacent cross-resolution tracking is therefore sufficient but not intrinsically necessary.** A raw sequence may jump by a fixed Hausdorff distance forever while its pooled set is compact; compactness then permits selection of a coherent subsequence. What fails in AF-073's Hilbert-space counterexample is stronger: the pooled singleton witnesses escape every compact subset of the unit sphere, so no coherent branch can be selected.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{finite-resolution discriminators need not come with a predetermined identity map across scales;}\\
\text{it is enough that all sufficiently accurate witnesses remain in a common precompact reservoir;}\\
\text{compactness then selects a coherent branch, while escape from every such reservoir destroys fidelity.}
\end{array}}
\tag{10}
\]

This sharpens AF-073's phrase “provenance across scale.” Provenance can be supplied constructively by explicit transition/coherence data, but it can also arise **existentially by compactness selection**. The invariant requirement is not continuity of one chosen approximation sequence; it is non-escape of the family of admissible finite witnesses.

## Derivation

### A compact transversal gives a precompact finite scheme

Fix a compact transversal

\[
C\in\mathfrak T_c(\mathcal K)
\]

and let

\[
m=d(C,L).
\tag{11}
\]

Choose any positive sequence `\varepsilon_n\downarrow0`. Since `C` is compact, for every `n` choose a nonempty finite `\varepsilon_n`-net

\[
F_n\subseteq C.
\tag{12}
\]

For each `K\in\mathcal K`, choose `u_K\in C\cap K\cap\mathbb S_V`. The net property supplies `f\in F_n` with

\[
\|f-u_K\|\le\varepsilon_n,
\]

hence

\[
g(F_n,K)\le\varepsilon_n.
\tag{13}
\]

Also `F_n\subseteq C` gives

\[
m_L(F_n)\ge d(C,L)=m.
\tag{14}
\]

Finally,

\[
\bigcup_nF_n\subseteq C,
\]

so the pooled witness set is relatively compact. Thus every compact transversal of margin `m` gives a precompact finite scheme at the same margin, and therefore

\[
\kappa_{\mathcal K}(L)
\ge
\tau_{\mathcal K}(L).
\tag{15}
\]

### A precompact finite scheme closes to one exact compact transversal

Conversely, suppose `(F_n,\varepsilon_n)` is a precompact scheme at margin `\eta`. Put

\[
C=\overline{\bigcup_nF_n}.
\tag{16}
\]

By hypothesis `C` is compact. Because every point of every `F_n` satisfies `d(\cdot,L)\ge\eta` and the set

\[
\{x:d(x,L)\ge\eta\}
\]

is closed, one has

\[
d(C,L)\ge\eta.
\tag{17}
\]

Fix a nonzero `K\in\mathcal K`. For each `n`, the definition of the infimum in (2) permits choices

\[
f_n\in F_n,
\qquad
u_n\in K\cap\mathbb S_V
\]

with

\[
\|f_n-u_n\|
\le
\varepsilon_n+\frac1n.
\tag{18}
\]

Compactness of `C` gives a subsequence `f_{n_j}\to f\in C`. Since the right-hand side of (18) tends to zero,

\[
u_{n_j}\to f.
\tag{19}
\]

Closedness of `K\cap\mathbb S_V` therefore gives

\[
f\in C\cap K\cap\mathbb S_V.
\tag{20}
\]

Thus `C` intersects every nonzero cone in `\mathcal K`, so it is a compact unit-direction transversal. Equation (17) gives a transversal margin at least `\eta`; hence

\[
\tau_{\mathcal K}(L)\ge\eta.
\]

Taking the supremum over precompact schemes proves

\[
\tau_{\mathcal K}(L)\ge\kappa_{\mathcal K}(L).
\tag{21}
\]

Together with (15), this proves (7).

If `\mathcal K` contains `K_0=\{0\}`, no finite approximation scheme exists because `g(F,K_0)=+\infty`; AF-072 likewise has no unit-direction transversal and sets `\tau=0`. The equality remains exact in that degeneracy.

## Equivalence with AF-073's coherent towers

The equality `\kappa=\theta` already follows from (7), AF-073's `\theta=\tau`, but there is a stronger direct statement.

### Precompactness lets compactness select a coherent subsequence

Let `(F_n,\varepsilon_n)` be a precompact scheme and let `C` be (16). Every `F_n` is a nonempty compact subset of the compact metric space `C`. The hyperspace

\[
\mathcal K(C)
\]

of nonempty compact subsets of `C`, equipped with Hausdorff distance, is compact. Hence some subsequence satisfies

\[
F_{n_j}\xrightarrow[d_H]{}D
\tag{22}
\]

for a nonempty compact `D\subseteq C`.

Pass to a further subsequence such that

\[
d_H(F_{n_j},D)\le2^{-j-3},
\qquad
\varepsilon_{n_j}\le2^{-j-3}.
\tag{23}
\]

Set

\[
q_j=2^{-j}.
\tag{24}
\]

Then `\sum_jq_j<\infty`, the approximation bound in (4) gives

\[
g(F_{n_j},K)\le q_j
\quad\forall K,
\tag{25}
\]

and the Hausdorff triangle inequality gives

\[
\begin{aligned}
d_H(F_{n_j},F_{n_{j+1}})
&\le d_H(F_{n_j},D)+d_H(D,F_{n_{j+1}})\\
&\le2^{-j-3}+2^{-j-4}
<q_j.
\end{aligned}
\tag{26}
\]

The margin `m_L(F_{n_j})\ge\eta` is unchanged. Thus the selected subsequence is an AF-073 coherent tower. Compactness does not say that the original approximation sequence had a stable identity; it says that non-escape guarantees the existence of a stable branch.

### Every coherent tower has a precompact witness pool

Conversely, let `(F_n,q_n)` be an AF-073 coherent tower. AF-073 proves that `(F_n)` is Hausdorff-Cauchy and converges to some nonempty compact

\[
D\subseteq\mathbb S_V.
\tag{27}
\]

To see directly that the pooled set `A=\bigcup_nF_n` is relatively compact, fix `r>0`. For all sufficiently large `n`,

\[
d_H(F_n,D)<r/2.
\]

A finite `r/2`-net for compact `D` is then an `r`-net for every such `F_n`. The finitely many earlier `F_n` have finite union and can be added to that net. Hence `A` is totally bounded. Since `V` is complete, its closure is compact.

This proves the direct equivalence between “precompact pooled witnesses” and “a coherently extractable finite branch.”

## Exact controls

### A raw finite-resolution sequence may jump forever without losing fidelity

Take `V=\mathbb R^2` with its Euclidean norm,

\[
K=\mathbb R_{\ge0}e_1+\mathbb R_{\ge0}e_2,
\qquad
\mathcal K=\{K\},
\qquad
L=\{0\}.
\tag{28}
\]

Let

\[
F_{2n}=\{e_1\},
\qquad
F_{2n+1}=\{e_2\},
\qquad
\varepsilon_n=2^{-n}.
\tag{29}
\]

Every `F_n` is an exact transversal of `K`, so `g(F_n,K)=0`, and every one has margin

\[
m_L(F_n)=1.
\]

The pooled set is just `{e_1,e_2}`, hence compact. Nevertheless

\[
d_H(F_n,F_{n+1})=\sqrt2
\quad\forall n.
\tag{30}
\]

Thus adjacent coherence of the **given** sequence is not an invariant requirement. Passing to either parity subsequence immediately recovers a coherent branch. The relevant fact was the compact reservoir, not the arbitrary ordering in which its witnesses were presented.

### AF-073's jumping Hilbert witnesses fail exactly by non-precompactness

AF-073 constructed singleton approximate transversals

\[
F_n=\{e_n\}
\]

in a separable infinite-dimensional Hilbert space, with approximation error tending to zero for every retained cone and with fixed distance `1` from `L=\{0\}`, while no compact exact transversal exists. Their pooled set

\[
\{e_n:n\ge1\}
\]

is uniformly separated and therefore not relatively compact. AF-074 identifies this as the exact missing hypothesis: the finite-scale witnesses do not merely lack a chosen transition map; they **escape every compact witness reservoir**.

### Pointwise boundedness is not a substitute for precompactness

All finite witnesses already lie on the unit sphere, so boundedness is automatic. AF-073's Hilbert control shows that boundedness alone gives no compactness in infinite dimension. The strengthening from bounded to relatively compact is therefore substantive and cannot be removed outside finite-dimensional settings.

## Prior art and novelty assessment

The compactness and hyperspace mechanisms are classical.

- Phil Diamond and Peter Kloeden, **“A note on compact sets in spaces of subsets,”** *Bulletin of the Australian Mathematical Society* 38(3) (1988), 393–395, DOI `10.1017/S0004972700027763`. The paper characterizes compact subsets of the Hausdorff hyperspace `K(X)` of nonempty compact subsets of a complete metric space and uses that framework to prove a Blaschke selection theorem. It is direct prior art for the compact-hyperspace subsequence extraction used in (22).
- Gerald Beer, ***Topologies on Closed and Closed Convex Sets***, Mathematics and Its Applications 268, Kluwer/Springer (1993), DOI `10.1007/978-94-015-8149-3`. Role: standard hyperspace framework for Hausdorff, gap, excess, and set-convergence constructions already used in AF-070–AF-073.
- Dmitri Burago, Yuri Burago, and Sergei Ivanov, ***A Course in Metric Geometry***, Graduate Studies in Mathematics 33, American Mathematical Society (2001), ISBN `978-0-8218-2129-9`. Role: standard metric-space background for total boundedness, compactness, Hausdorff distance, and compact-set limits.

No novelty is claimed for total boundedness, precompactness, finite nets, Hausdorff hyperspace compactness, Blaschke selection, or subsequence extraction. A targeted search did not locate the exact cone-family equality (7), but search absence is not evidence of priority.

The durable contribution is the **boundary correction to AF-073's interpretation**. AF-073 correctly proved that one coherent Hausdorff-Cauchy tower is sufficient and complete as a certificate. AF-074 shows that explicit adjacent coherence is only one presentation of the underlying resource: at the existence level, the exact condition is a vanishing-error finite witness family whose entire pool is precompact. Compactness can then manufacture the coherent branch by selection.

## Boundary conditions and audit

- **Closedness of each `K` is load-bearing.** The limit in (19) lands in `K` only because `K\cap\mathbb S_V` is closed. With nonclosed cones, approximate hits may converge to an omitted boundary direction.
- **Completeness of `V` is used in the equivalence with total boundedness/coherent towers.** Relative compactness may be taken as “compact closure” directly, but AF-073's Hausdorff-limit formulation and the converse total-boundedness argument naturally live in a Banach space.
- **The pooled precompactness condition is global across resolutions.** It is stronger than requiring each individual finite `F_n` to be compact, which is automatic and carries no cross-scale information.
- **No prescribed subsequence is canonical.** Several coherent branches may coexist. The theorem certifies survival of at least one compact discriminator, not uniqueness or an intrinsic identity assignment between finite resolutions.
- **The theorem is norm-topological and category-specific.** Weak compactness, weak-* compactness, probability tightness, Fell/Wijsman convergence, strong/weak operator topology, and spectral-measure convergence require their own versions of the selection argument.
- **The margin is uniform.** If `m_L(F_n)` tends to zero, compactness may select a branch that lands in `L`; that is loss of the discriminator rather than positive-fidelity survival.
- **No arithmetic specialization is asserted.** A future prime/RH application must identify the natural destination topology and prove either explicit coherence or precompactness/tightness of its finite-level prime-discriminating witnesses before passing to an infinite/global object.

## Consequences for Arithmetic Fidelity

AF-071 separated pointwise directional separation from compact realizability. AF-072 identified the exact compact simultaneous witness. AF-073 gave that witness a finite multiscale semantics using a Hausdorff-coherent tower. AF-074 now removes a presentation artifact from that semantics: **the researcher need not know in advance which finite witness at level `n` is the continuation of which witness at level `n+1`.**

For compression audits built from truncations, spectral windows, bounded test families, finite moments, or finite numerical approximants, there are now two mathematically valid routes to a global discriminator. One may construct explicit transition maps or Hausdorff-Cauchy coherence, or one may prove that all chosen increasingly accurate witnesses remain in a common precompact region and invoke compactness to extract a coherent branch. What is not valid is merely showing that every finite level has some strong witness while allowing those witnesses to escape through ever-new directions.

This is a more precise formulation of structural provenance under limiting compression: **provenance need not be labeled in advance, but it must be compactly selectable.**