# AF-071 — Universal normalized-excess fidelity characterizes finite dimensionality

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a real normed space, not assumed finite-dimensional. Let `\mathcal K` be a nonempty family of cones in `V`, each containing `0`, and let `L\subseteq V` be a closed cone containing `0`. For a cone `K`, retain AF-070's directed normalized excess

\[
\varepsilon(K\mid L)
=
\sup_{x\in K\setminus\{0\}}
\frac{d(x,L)}{\|x\|},
\qquad
\varepsilon(\{0\}\mid L)=0,
\tag{1}
\]

and

\[
\delta_{\mathcal K}(L)
=
\inf_{K\in\mathcal K}\varepsilon(K\mid L).
\tag{2}
\]

For nonempty compact targets `S\subset V`, write as before

\[
H_{\mathcal K}(S)
=
\bigcap_{K\in\mathcal K}(S-K),
\tag{3}
\]

and say that `L` is a compact-target consequence of `\mathcal K` when

\[
H_{\mathcal K}(S)\subseteq S-L
\qquad
\text{for every nonempty compact }S\subset V.
\tag{4}
\]

Define the collective unit-direction set

\[
U_{\mathcal K}
=
\bigcup_{K\in\mathcal K}
\{u\in K:\|u\|=1\}.
\tag{5}
\]

Then:

1. **Zero normalized excess is sufficient in every normed space.** Without any finite-dimensionality assumption,
   \[
   \boxed{
   \delta_{\mathcal K}(L)=0
   \Longrightarrow
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K).
   }
   \tag{6}
   \]
   The compact-target recovery half of AF-070 is therefore dimension-free.

2. **Relative compactness of all test directions restores the converse.** If `U_{\mathcal K}` has compact closure in the norm topology, then
   \[
   \boxed{
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   \delta_{\mathcal K}(L)=0.
   }
   \tag{7}
   \]
   Thus finite dimensionality in AF-070 was used through a more precise resource: collective precompactness of the unit-scale directions from which a compact falsifier must be assembled.

3. **The universal AF-070 equivalence characterizes finite-dimensional norm geometry.** The following are equivalent:

   (a) `V` is finite-dimensional;

   (b) for every nonempty cone family `\mathcal K` and every closed cone `L` containing `0`,
   \[
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   \delta_{\mathcal K}(L)=0.
   \tag{8}
   \]

   Hence the finite-dimensional hypothesis in AF-070 is not a technical convenience. It is exactly the ambient condition under which normalized directional proximity universally classifies compact-target consequence.

4. **Infinite-dimensional spaces admit maximal-excess consequences created purely by directional escape.** If `V` is infinite-dimensional, there exist unit vectors `(u_n)` and some fixed `\alpha>0` such that
   \[
   \|u_n-u_m\|>\alpha
   \qquad(n\ne m).
   \tag{9}
   \]
   Put
   \[
   K_n=\mathbb R_{\ge0}u_n,
   \qquad
   \mathcal K=\{K_n:n\ge1\},
   \qquad
   L=\{0\}.
   \tag{10}
   \]
   Then
   \[
   \varepsilon(K_n\mid\{0\})=1
   \quad\forall n,
   \qquad
   \delta_{\mathcal K}(\{0\})=1,
   \tag{11}
   \]
   yet
   \[
   \boxed{
   \{0\}\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K).
   }
   \tag{12}
   \]
   No cone approaches `L` at all in normalized excess. The consequence arises because a compact target cannot keep supplying nonzero witnesses along a uniformly separated sequence of directions unless those witnesses collapse to `0`.

5. **Compact-target fidelity therefore has two logically different mechanisms beyond finite dimension.** A consequence can be forced either by
   \[
   \text{directional approach to }L
   \quad(\delta_{\mathcal K}(L)=0),
   \tag{13}
   \]
   or by
   \[
   \text{escape of all positive-scale witness directions from norm-compact sets}.
   \tag{14}
   \]
   AF-070 sees only the first mechanism because finite-dimensional unit spheres are compact, so the second cannot occur independently.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{compactness of the target does not by itself make directional excess complete;}\\
\text{completeness also requires compactness/tightness of the available witness directions;}\\
\text{finite dimension supplies that condition automatically, while infinite dimension does not.}
\end{array}
}
\tag{15}
\]

This separates **proximity loss** from **escape loss**. In an infinite-dimensional compression audit, a positive distance from every candidate retained constraint does not guarantee a compact matched control: the witnesses needed to realize that positive margin may themselves have no compact directional realization.

## Derivation

### Zero excess remains sufficient without finite-dimensionality

Assume

\[
\delta_{\mathcal K}(L)=0.
\tag{16}
\]

Let `S\subset V` be nonempty compact and suppose first that

\[
0\in H_{\mathcal K}(S),
\tag{17}
\]

so `S\cap K\ne\varnothing` for every `K\in\mathcal K`. If `S\cap L=\varnothing`, then `0\notin S` because `0\in L`. Therefore

\[
r(s)=\frac{d(s,L)}{\|s\|}
\tag{18}
\]

is continuous and strictly positive on compact `S`. Hence

\[
\eta=\min_{s\in S}r(s)>0.
\tag{19}
\]

Choose `K\in\mathcal K` with

\[
\varepsilon(K\mid L)<\eta.
\tag{20}
\]

Every nonzero `x\in K` then satisfies

\[
\frac{d(x,L)}{\|x\|}<\eta,
\tag{21}
\]

while every `s\in S` has the opposite inequality `r(s)\ge\eta`. Also `0\notin S`, so `S\cap K=\varnothing`, a contradiction. Thus `S\cap L\ne\varnothing`.

For arbitrary `m\in H_{\mathcal K}(S)`, apply the same argument to the compact translate `S-m`. It meets every `K`, hence also `L`; therefore `m\in S-L`. This proves (6). No sphere compactness, local compactness of `V`, or dimension assumption was used.

### Collective directional precompactness recovers the positive-margin falsifier

Assume now that `\overline{U_{\mathcal K}}` is norm-compact and that

\[
c=\delta_{\mathcal K}(L)>0.
\tag{22}
\]

Choose `0<\eta<c` and define

\[
A_\eta
=
U_{\mathcal K}
\cap
\{u\in V:d(u,L)\ge\eta\}.
\tag{23}
\]

For every `K\in\mathcal K`, equation (22) gives

\[
\varepsilon(K\mid L)\ge c>\eta.
\tag{24}
\]

By the definition of supremum, some unit `u_K\in K` satisfies `d(u_K,L)>\eta`, so `A_\eta\cap K\ne\varnothing`.

Let

\[
S_\eta=\overline{A_\eta}.
\tag{25}
\]

This set is compact because it is a closed subset of the compact set `\overline{U_{\mathcal K}}`. Continuity of `d(\cdot,L)` gives

\[
d(u,L)\ge\eta
\qquad\forall u\in S_\eta,
\tag{26}
\]

so `S_\eta\cap L=\varnothing`. But `S_\eta` still meets every `K`, because it contains `A_\eta`. Hence

\[
0\in H_{\mathcal K}(S_\eta)
\qquad\text{and}\qquad
0\notin S_\eta-L.
\tag{27}
\]

Thus positive normalized excess contradicts compact-target consequence whenever the collective unit directions are relatively compact. Combining this with (6) proves (7).

This is the exact replacement for AF-070's finite-dimensional sphere argument. The whole ambient sphere need not be compact; only the directions actually used by the declared cone family must be collectively precompact.

### Infinite dimension produces separated rays

Suppose `V` is infinite-dimensional. Riesz's lemma yields, for any fixed `0<\alpha<1`, a sequence of unit vectors `(u_n)` with pairwise separation greater than `\alpha`: inductively choose `u_{n+1}` at distance greater than `\alpha` from the finite-dimensional closed span of `u_1,\ldots,u_n`. Since every earlier `u_j` lies in that span,

\[
\|u_{n+1}-u_j\|>\alpha.
\tag{28}
\]

For the rays in (10), every nonzero `x\in K_n` satisfies

\[
\frac{d(x,\{0\})}{\|x\|}=1,
\tag{29}
\]

which proves (11).

It remains to prove (12). Let `S` be nonempty compact and suppose

\[
0\in H_{\mathcal K}(S),
\tag{30}
\]

so `S` meets every ray `K_n`. If `0\in S` there is nothing to prove. Otherwise compactness and continuity of the norm give

\[
a:=\min_{s\in S}\|s\|>0.
\tag{31}
\]

Choose `x_n\in S\cap K_n`. Since `0\notin S`, write uniquely

\[
x_n=t_nu_n,
\qquad t_n>0.
\tag{32}
\]

Compactness of `S` gives a convergent subsequence `x_{n_j}\to x\in S`. Equation (31) implies `x\ne0`, so normalization is continuous along this subsequence and

\[
u_{n_j}
=
\frac{x_{n_j}}{\|x_{n_j}\|}
\longrightarrow
\frac{x}{\|x\|}.
\tag{33}
\]

This contradicts the uniform separation (9). Therefore every compact `S` meeting all the rays must contain `0`.

After translating, if `m\in H_{\mathcal K}(S)`, then `S-m` is compact and meets every `K_n`, hence contains `0`; therefore `m\in S`. Since `S-\{0\}=S`, this is exactly (12).

The construction has the largest possible normalized excess, `1`. The failure of AF-070's converse is therefore not a small perturbative defect: positive separation from the candidate consequence can coexist with exact consequence on every compact target.

### The universal equivalence is equivalent to finite dimension

If `V` is finite-dimensional, AF-070 proves (8). Conversely, if `V` is infinite-dimensional, the separated-ray construction has `L=\{0\}` with compact-target consequence but `\delta_{\mathcal K}(L)=1`. Hence (8) fails. This proves item 3.

Equivalently, the universality of the normalized-excess criterion detects the classical compactness boundary of normed spaces: finite-dimensional unit balls/spheres are compact, while Riesz's lemma produces a separated unit sequence in every infinite-dimensional normed space.

## Exact controls

### Precompact rays restore AF-070 without finite-dimensional ambient geometry

Let `(u_n)` be any norm-convergent sequence of unit vectors in an arbitrary normed space, with `u_n\to u`, and set

\[
K_n=\mathbb R_{\ge0}u_n.
\tag{34}
\]

Then `U_{\mathcal K}=\{u_n:n\ge1\}` has compact closure. For every closed cone `L`, the criterion (7) applies even if `V` is infinite-dimensional. Thus the obstruction is not infinite dimension by itself; it is the availability of a non-precompact family of retained directions.

### Radial collapse and directional escape are distinct

For the separated-ray family, a compact target can meet every ray in only two possible ways. If witness norms tend to `0` along a subsequence, compact closure forces `0` into the target. If witness norms stay bounded below, compactness would force their normalized directions to have a convergent subsequence, impossible by (9). These are exhaustive because a compact target is bounded and closed.

This matched dichotomy identifies what AF-070's finite-dimensional sphere falsifier concealed: compactness must control both **scale** and **direction**. Normalized excess removes scale algebraically, but in infinite dimension the remaining direction space itself need not be compact.

### The failure is norm-topological, not merely cardinal

Nothing in the counterexample depends on an uncountable cone family. A countable family of one-dimensional rays already breaks the converse. Conversely, arbitrarily large cone families satisfy (7) whenever their collective unit-direction set is relatively norm-compact. Cardinality is therefore not the relevant control; directional precompactness is.

## Prior art and novelty assessment

The functional-analytic mechanisms are classical.

- James C. Robinson, ***An Introduction to Functional Analysis***, Cambridge University Press (2020), Chapter 5, book DOI `10.1017/9781139030267`. Role: authoritative modern source for Riesz's lemma and the classical equivalence between finite dimensionality and compactness of the closed unit ball. This supplies the separated-unit-sequence mechanism used in item 4 and the ambient compactness boundary behind item 3.
- P. M. Anselone and T. W. Palmer, **“Collectively Compact Sets of Linear Operators,”** *Pacific Journal of Mathematics* 25(3) (1968), 417–422. Role: established neighboring language for a family-level compactness condition defined by compact closure of the union of unit-ball images. AF-071's `U_{\mathcal K}` condition is not an operator theorem from that paper, but the analogy is exact at the structural level: compactness must hold collectively across the whole family, not merely object by object.
- Gerald Beer, ***Topologies on Closed and Closed Convex Sets***, Mathematics and Its Applications 268, Kluwer/Springer (1993), DOI `10.1007/978-94-015-8149-3`. Role: classical hyperspace framework for gap/excess functionals, Hausdorff-type set comparison, and set convergence. The normalized excess itself remains classical set-distance machinery, as already recorded in AF-070.

No novelty is claimed for Riesz's lemma, compact-unit-ball characterizations, collective compactness, or one-sided excess. A targeted prior-art search did not locate the exact cone-hull statement (6)–(12), but absence from that search is not evidence of mathematical novelty. The durable contribution is the **Arithmetic Fidelity classification** obtained by combining those classical mechanisms: AF-070's zero-excess criterion extends in only one direction to arbitrary normed spaces; its converse is recovered by collective directional precompactness; and universal validity of the equivalence is itself equivalent to finite dimensionality.

## Boundary conditions and audit

- The topology in items 1–4 is the **norm topology**. Replacing norm compactness by weak compactness changes the problem materially; normalized directions that are norm-separated may still have weakly convergent subsequences in reflexive spaces.
- The compact-target class is essential. For noncompact targets, AF-069 already shows that moving witnesses may escape even in finite dimension.
- The candidate consequence cone `L` must be closed for the positive minimum argument and the distance-zero interpretation. No convexity is required.
- Relative compactness in item 2 is a sufficient hypothesis for the converse, not claimed to be necessary for one fixed pair `(\mathcal K,L)`. A non-precompact direction family may still admit a compact positive-margin falsifier for a particular `L`.
- Item 3 is universal over all cone families and closed consequence cones. It should not be weakened into the false statement that every individual AF-070-style equivalence fails in every infinite-dimensional space.
- The separated-ray counterexample uses only one-dimensional closed convex cones, so the failure cannot be blamed on pathological nonclosed or nonconvex test sets.

A stronger next theorem would need to classify, for a fixed infinite-dimensional family `\mathcal K`, exactly when every positive-excess relation admits a compact transversal away from `L`. The present result isolates collective directional precompactness as a clean sufficient condition and proves that no ambient theorem based on normalized excess alone can avoid an additional tightness/compactness hypothesis.

## Consequences for Arithmetic Fidelity

AF-069 and AF-070 showed that changing the admissible target category changes which infinite collections of constraints become logically recoverable. AF-071 adds an orthogonal category axis: **the ambient direction space matters even when the target category remains compact**.

For future spectral, operator, harmonic, or arithmetic applications in infinite-dimensional spaces, an audit based only on a scalar loss margin can therefore be incomplete. Before converting a positive separation margin into a matched compact counterexample, one must also ask whether the corresponding witness family is collectively tight/precompact in the topology used by the downstream construction.

This is directly relevant to the line's composition objective. A downstream compactness argument can appear to recover information for two very different reasons: because retained constraints genuinely converge toward the missing discriminator, or because all alternative witnesses escape the admissible compact category. These mechanisms should not be conflated. The first is a proximity statement about what the compression retains; the second is a compactness statement about which counterexamples the destination category is capable of representing.