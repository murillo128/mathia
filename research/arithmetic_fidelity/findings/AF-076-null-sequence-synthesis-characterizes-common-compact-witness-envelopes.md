# AF-076 — Null-sequence synthesis exactly characterizes common compact witness envelopes

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a real Banach space and let `A\subset V` be nonempty and bounded. For a norm-null sequence

\[
x=(x_j)_{j\ge1}\in c_0(V),
\]

define the associated `\ell^1` synthesis operator

\[
S_x:\ell^1\to V,
\qquad
S_x(a)=\sum_{j\ge1}a_jx_j,
\tag{1}
\]

and its closed synthesis envelope

\[
C_x
=
\overline{S_x(B_{\ell^1})}
=
\overline{\operatorname{aconv}}\{x_j:j\ge1\}.
\tag{2}
\]

Then:

1. **Common null-sequence envelopes are exactly norm precompactness.**
   \[
   \boxed{
   A\text{ is relatively norm-compact}
   \iff
   \exists x\in c_0(V)\text{ with }A\subseteq C_x.
   }
   \tag{3}
   \]
   Equivalently, every relatively compact witness family can be placed inside the compact image-closure of one bounded `\ell^1` coefficient ball under one synthesis map whose generator columns tend to zero.

2. **The synthesis operator is compact with an explicit finite-rank tail.** If
   \[
   S_{x,N}(a)=\sum_{j=1}^{N}a_jx_j,
   \tag{4}
   \]
   then
   \[
   \boxed{
   \|S_x-S_{x,N}\|
   =
   \sup_{j>N}\|x_j\|
   \longrightarrow0.
   }
   \tag{5}
   \]
   Hence `S_x` is an operator-norm limit of finite-rank maps and therefore compact. In particular,
   \[
   \boxed{
   d_N(C_x;V)
   \le
   \sup_{j>N}\|x_j\|,
   }
   \tag{6}
   \]
   where `d_N` is the Kolmogorov width from AF-075.

3. **AF-074 compact fidelity is exactly a common synthesis-envelope condition.** Retain AF-074's setting: `\mathcal K` is a nonempty family of closed cones in `V`, each containing `0`; `L\subseteq V` is a closed cone containing `0`; finite witnesses `F_n\subseteq\mathbb S_V` have approximation error
   \[
   g(F_n,K)
   =
   \inf\{\|f-u\|:f\in F_n,\ u\in K\cap\mathbb S_V\},
   \tag{7}
   \]
   with `g(F_n,{0})=+\infty`, and target margin `m_L(F_n)=d(F_n,L)`.

   Call `(F_n,\varepsilon_n,x)` a **common null-synthesis scheme at margin `\eta`** when `F_n` are nonempty finite sets, `\varepsilon_n>0` with `\varepsilon_n\to0`,
   \[
   g(F_n,K)\le\varepsilon_n
   \quad\forall K\in\mathcal K,\ \forall n,
   \qquad
   m_L(F_n)\ge\eta
   \quad\forall n,
   \tag{8}
   \]
   and one norm-null sequence `x\in c_0(V)` satisfies
   \[
   \bigcup_{n\ge1}F_n\subseteq C_x.
   \tag{9}
   \]

   Define
   \[
   \nu_{\mathcal K}(L)
   =
   \sup\{\eta\ge0:\text{a common null-synthesis scheme at margin }\eta\text{ exists}\},
   \tag{10}
   \]
   with value `0` if no such scheme exists. Then
   \[
   \boxed{
   \nu_{\mathcal K}(L)
   =
   \kappa_{\mathcal K}(L)
   =
   \tau_{\mathcal K}(L),
   }
   \tag{11}
   \]
   where `\kappa` is AF-074's precompact finite-scheme margin and `\tau` is AF-072's compact-transversal margin. Consequently,
   \[
   \boxed{
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   \nu_{\mathcal K}(L)=0.
   }
   \tag{12}
   \]

4. **Per-resolution compactness is vacuous; one common compact mechanism is load-bearing.** Every individual finite witness set is contained in the image of a finite-rank, hence compact, operator. This does not control the pooled family. In `V=\ell^2`, the singleton witnesses
   \[
   F_n=\{e_n\}
   \tag{13}
   \]
   each have a rank-one synthesis representation, while no single null-sequence envelope `C_x` can contain all of them. Thus a sequence of compact mechanisms `S_n` at separate resolutions is not a substitute for one common compact synthesis mechanism across resolutions.

5. **Common synthesis envelopes are stable under bounded linear post-processing.** If `B:V\to Y` is bounded linear into another Banach space and `A\subseteq C_x`, then
   \[
   B(A)\subseteq C_{Bx},
   \qquad
   Bx=(Bx_j)_{j\ge1}\in c_0(Y),
   \tag{14}
   \]
   and
   \[
   \sup_{j>N}\|Bx_j\|
   \le
   \|B\|\sup_{j>N}\|x_j\|.
   \tag{15}
   \]
   Hence the **non-escape resource** supplied by one compact envelope survives every bounded linear downstream map, even though the discriminator itself may still collapse under that map.

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\begin{array}{c}
\text{cross-scale compactness can be represented by one common vanishing generator family;}\\
\text{finite-level compactness alone carries no cross-scale provenance;}\\
\text{a source-derived common synthesis envelope is a composition-stable certificate of non-escape.}
\end{array}}
\tag{16}
\]

## Derivation

### A null generator sequence produces a compact synthesis envelope

Because `x_j\to0`, the sequence is bounded. For `a\in\ell^1`, the series in (1) converges absolutely and

\[
\|S_x(a)\|
\le
\sum_j|a_j|\,\|x_j\|
\le
\left(\sup_j\|x_j\|\right)\|a\|_1,
\tag{17}
\]

so `S_x` is bounded. Its truncation `S_{x,N}` has range contained in

\[
E_N=\operatorname{span}\{x_1,\ldots,x_N\},
\]

hence finite rank. Moreover,

\[
\begin{aligned}
\|(S_x-S_{x,N})a\|
&\le
\sum_{j>N}|a_j|\,\|x_j\|\\
&\le
\left(\sup_{j>N}\|x_j\|\right)\|a\|_1.
\end{aligned}
\tag{18}
\]

Taking `a=e_j` for tail indices approaching the supremum gives equality in operator norm, proving (5). Therefore `S_x` is compact.

Since compact operators map bounded sets to relatively compact sets,

\[
C_x=\overline{S_x(B_{\ell^1})}
\tag{19}
\]

is compact. The equality with the closed absolutely convex hull in (2) follows because finitely supported vectors are dense in `\ell^1`, and their unit-ball images are exactly the finite absolutely convex combinations of the generators.

Thus

\[
A\subseteq C_x
\Longrightarrow
A\text{ is relatively compact}.
\tag{20}
\]

### Grothendieck compactness produces one null synthesis envelope

Conversely, suppose `A` is relatively compact and put

\[
K=\overline A.
\tag{21}
\]

Then `K` is norm compact. The classical Grothendieck compactness principle states that every norm-compact subset of a Banach space is contained in the closed convex hull of a norm-null sequence. Hence there is

\[
x=(x_j)_{j\ge1}\in c_0(V)
\]

such that

\[
K\subseteq\overline{\operatorname{conv}}\{x_j:j\ge1\}.
\tag{22}
\]

Every finite convex combination of the `x_j` is an image under `S_x` of a nonnegative finitely supported `\ell^1` vector of norm `1`. Therefore

\[
\overline{\operatorname{conv}}\{x_j\}
\subseteq
\overline{S_x(B_{\ell^1})}
=C_x.
\tag{23}
\]

Together with (21) this proves the reverse implication in (3).

The theorem is stronger than merely saying that the closure of `A` is some compact set. It supplies one **countable vanishing generator family and one uniform coefficient budget** whose compact envelope contains the entire witness family.

### The generator tail controls the Kolmogorov-width tail

Let `y\in S_x(B_{\ell^1})`, so `y=S_x(a)` with `\|a\|_1\le1`. Since `S_{x,N}(a)\in E_N`,

\[
d(y,E_N)
\le
\|(S_x-S_{x,N})a\|
\le
\sup_{j>N}\|x_j\|.
\tag{24}
\]

Distance to the closed finite-dimensional subspace `E_N` is continuous, so the same estimate holds on `C_x`. Since `\dim E_N\le N`, taking the infimum over all `N`-dimensional approximating subspaces gives (6).

This places AF-075's width criterion and the present synthesis criterion in the same hierarchy. Width decay is intrinsic and optimizes over all finite-dimensional models; a null synthesis envelope gives one explicit nested family of approximating spans. Grothendieck's principle proves that some such family exists whenever the pooled witnesses are precompact, but it does not make that family canonical.

### AF-074 turns the classical compactness principle into an exact fidelity criterion

Suppose first that a common null-synthesis scheme exists at margin `\eta`. Its pooled set

\[
A=\bigcup_nF_n
\]

lies in compact `C_x`, hence is relatively compact. It is therefore an AF-074 precompact finite approximation scheme at the same margin, so

\[
\kappa_{\mathcal K}(L)\ge\nu_{\mathcal K}(L).
\tag{25}
\]

Conversely, let an AF-074 precompact scheme exist at margin `\eta`. Its pooled set `A` is relatively compact, so (3) gives a norm-null sequence `x` with `A\subseteq C_x`. The same finite witnesses and errors then form a common null-synthesis scheme at margin `\eta`, and

\[
\nu_{\mathcal K}(L)\ge\kappa_{\mathcal K}(L).
\tag{26}
\]

Hence `\nu=\kappa`; AF-074 gives `\kappa=\tau`, proving (11), and AF-072 gives (12).

No extra compactness hypothesis has been inserted. The operator representation and AF-074's pooled-precompactness representation are exactly equivalent at the existence level.

## Exact controls

### Separate finite-rank envelopes do not assemble

Let `V=\ell^2` and `F_n=\{e_n\}`. For every `n`, define

\[
R_n:\mathbb R\to\ell^2,
\qquad
R_n(t)=t e_n.
\tag{27}
\]

Each `R_n` has rank one and is compact, and

\[
F_n\subseteq R_n([-1,1]).
\]

Nevertheless the pooled family `{e_n:n\ge1}` is uniformly separated and has no convergent subsequence, so it is not relatively compact. By (3), there cannot exist any `x\in c_0(\ell^2)` with

\[
\{e_n:n\ge1\}\subseteq C_x.
\tag{28}
\]

Thus “every cutoff admits a compact representation” is no cross-scale statement at all. The representation must be **uniformly shared across cutoffs**.

This is the operator form of the AF-073--AF-075 escape controls. AF-073 showed that arbitrarily accurate finite witnesses can jump forever; AF-074 identified pooled precompactness as the exact missing resource; AF-075 measured its failure by a positive width floor. AF-076 packages the same resource as one common compact synthesis map.

### A common envelope need not be finite-dimensional

Take

\[
x_j=\frac{e_j}{j}\in\ell^2.
\tag{29}
\]

Then `x_j\to0`, so the synthesis envelope `C_x` is compact, while its linear span is infinite-dimensional. Its canonical truncations obey

\[
\|S_x-S_{x,N}\|
=
\frac1{N+1}.
\tag{30}
\]

Thus the common-envelope condition is not eventual finite-dimensionality. It is a single compactly controlled infinite-dimensional carrier whose unresolved tail vanishes uniformly.

### Compact post-processing preserves non-escape but may erase the discriminator

Equation (14) holds for every bounded linear `B`, not only injective ones. In particular `B=0` maps every compact envelope to `{0}`. Therefore envelope survival must not be confused with discriminator fidelity. The common envelope answers a different question: whether finite-resolution witnesses escape every compact reservoir before the downstream compression is even audited for collisions.

This separation is essential for Arithmetic Fidelity. Compactness/coherence is a **necessary assembly resource** for the AF-072 compact-target model; it is not a replacement for the fiberwise or matched-control tests that decide whether the desired discriminator survives.

## Prior art and novelty assessment

The central compactness theorem is classical.

- Alexander Grothendieck, ***Produits tensoriels topologiques et espaces nucléaires***, Memoirs of the American Mathematical Society 16 (1955), DOI `10.1090/memo/0016`. Role: original source of the norm-compactness principle used in (22): compact subsets of Banach spaces are contained in the closed convex hull of a norm-null sequence.
- Davide Ravasini, **“Haar null closed and convex sets in separable Banach spaces,”** *Bulletin of the London Mathematical Society* 55(1), 137–148 (2023), DOI `10.1112/blms.12716`. Role: a modern explicit statement of Grothendieck's characterization in the form that a closed subset of a Banach space is compact exactly when it lies in the closed convex hull of a sequence in `c_0(X)`; this paper uses the principle as a tool rather than claiming it as new.
- Rabindranath Sen, ***A First Course in Functional Analysis: Theory and Applications***, Chapter VIII, “Compact Operators on Normed Linear Spaces,” Anthem Press (2013), DOI `10.7135/9780857282224.010`. Role: standard compact-operator background: compact maps send bounded sets to relatively compact sets and finite-rank maps are the basic compact models.
- Allan Pinkus, ***n-Widths in Approximation Theory***, Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol. 7, Springer (1985), DOI `10.1007/978-3-642-69894-1`. Role: classical width framework already used in AF-075; equation (6) is the synthesis-tail upper bound for that established finite-dimensional approximation quantity.

No novelty is claimed for Grothendieck's compactness principle, compact operators, `\ell^1` synthesis, closed absolutely convex hulls, finite-rank truncation, or Kolmogorov widths. The implication from a null sequence to the compact synthesis operator is elementary, and the reverse existence statement is exactly the classical Grothendieck principle.

The durable Arithmetic Fidelity contribution is the **common-envelope boundary** obtained by composing that classical principle with AF-074's exact fidelity theorem. It makes an operator-level distinction that the previous formulations left implicit: finite-resolution witnesses may each possess excellent compact or finite-rank descriptions while their pooled family has no single compact synthesis carrier. Only a common carrier supplies cross-scale provenance. This gives operator/spectral applications a concrete pre-compression audit and a clean composition law under bounded linear post-processing.

A targeted prior-art check also found modern extensions of the Grothendieck principle to weak, ordinal-weak, absolute-weak, and super-weak compactness. Those results reinforce rather than weaken the boundary here: the topology is part of the fidelity category, and changing from norm compactness to another topology requires a different compactness principle rather than silently reusing (3).

## Boundary conditions and audit

- **Completeness of `V` is part of the stated category.** Grothendieck's principle is used in Banach space form, and compactness of the synthesis envelope is asserted in the norm topology.
- **The generator sequence is existential, not canonical.** Equation (3) does not identify a preferred `x`, and many unrelated null sequences may envelop the same compact set. A concrete arithmetic, spectral, or geometric application must derive its generator family or compact synthesis map from source structure if naturality matters.
- **Post-hoc synthesis is not an explanatory mechanism.** Once precompactness is already known, Grothendieck guarantees an envelope. Choosing that envelope after seeing the target discriminator does not establish that the original compression retained provenance.
- **One uniform coefficient budget is load-bearing.** Allowing the `\ell^1` radius to grow with resolution can destroy compactness even when `x_j\to0`; the fixed unit-ball envelope is what converts vanishing columns into uniform tail control.
- **The absolute convex enlargement is harmless for compactness but may be too large for another discriminator.** `C_x` is used here only as a compact envelope. Its extra sign/convex combinations are not asserted to be intrinsic states of the original source model.
- **The operator statement tracks non-escape, not injectivity or recovery.** A bounded post-processing map preserves the existence of a compact envelope while it may collapse every discriminator. AF-001/AF-002-style fiber audits remain separate.
- **No arbitrary compact operator is claimed to possess the column-tail identity (5).** The identity is specific to the `\ell^1` synthesis representation generated by `x_j\to0`. General compact operators between Banach spaces need not be operator-norm approximable by finite-rank maps unless suitable approximation-property hypotheses hold; the present construction avoids importing such a hypothesis.
- **Weak or weak-* compactness is a different category.** The literature contains distinct Grothendieck-type principles for those topologies. They cannot be substituted for norm precompactness in AF-072--AF-075 without rebuilding the destination topology and witness theorem.
- **No arithmetic specialization is asserted.** A prime/RH transfer must identify a source-natural bounded coefficient model and generators before this theorem can certify cross-scale non-escape.

## Consequences for Arithmetic Fidelity

AF-073 initially expressed surviving cross-scale provenance through explicit Hausdorff coherence. AF-074 showed that no particular transition map between adjacent resolutions is fundamental: a precompact pooled reservoir is enough for compactness to select a coherent branch. AF-075 then measured that reservoir intrinsically by vanishing Kolmogorov widths.

AF-076 gives the same exact resource an operator presentation that is closer to the spectral and truncation mechanisms appearing elsewhere in Mathia. A successful finite-window or increasing-degree construction can now certify the assembly gate by exhibiting **one source-derived null generator family with a uniform `\ell^1` coefficient budget**, or an equivalent common compact synthesis carrier. The finite-rank truncations of that one carrier automatically provide controlled approximations at every scale, with tail (5).

The main unresolved issue is therefore sharper. Abstract existence is already classical and complete: every precompact pooled witness family has some null-synthesis envelope. What an RH-relevant construction must supply is not another existential compactness proof, but a **canonical or independently forced common envelope whose generators still encode the rational-prime discriminator before downstream compression**. If a proposed construction only produces a different compact operator at each cutoff, AF-076 says it has not crossed the assembly gate at all.