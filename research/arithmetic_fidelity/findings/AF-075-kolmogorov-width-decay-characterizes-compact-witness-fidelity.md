# AF-075 — Vanishing Kolmogorov widths exactly characterize compact witness fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a real Banach space and let `A\subset V` be nonempty and bounded. For `m\ge 0`, define its Kolmogorov width

\[
d_m(A;V)
=
\inf_{\substack{E\le V\\ \dim E\le m}}
\sup_{a\in A} d(a,E).
\tag{1}
\]

Then:

1. **Width decay is exactly norm precompactness.**
   \[
   \boxed{
   A\text{ is relatively norm-compact}
   \iff
   d_m(A;V)\longrightarrow0.
   }
   \tag{2}
   \]
   Thus AF-074's apparently qualitative requirement that all finite-resolution witnesses remain in one precompact reservoir has an intrinsic quantitative reformulation: the entire pooled witness family must admit uniformly accurate approximation by finite-dimensional subspaces of increasing dimension.

2. **Kolmogorov-width tightness exactly recovers AF-074's compact-transversal fidelity.** Retain AF-074's setting: `\mathcal K` is a nonempty family of closed cones in `V`, each containing `0`; `L\subseteq V` is a closed cone containing `0`; finite witness sets `F_n\subseteq\mathbb S_V` have approximation error
   \[
   g(F_n,K)
   =
   \inf\{\|f-u\|:f\in F_n,\ u\in K\cap\mathbb S_V\},
   \tag{3}
   \]
   with `g(F_n,{0})=+\infty`, and target margin
   \[
   m_L(F_n)=d(F_n,L).
   \tag{4}
   \]

   Call `(F_n,\varepsilon_n)` a **width-tight finite approximation scheme at margin `\eta`** when each `F_n` is nonempty finite, `\varepsilon_n>0` with `\varepsilon_n\to0`,
   \[
   g(F_n,K)\le\varepsilon_n
   \quad\forall K\in\mathcal K,\ \forall n,
   \qquad
   m_L(F_n)\ge\eta
   \quad\forall n,
   \tag{5}
   \]
   and the pooled set
   \[
   A=\bigcup_{n\ge1}F_n
   \tag{6}
   \]
   satisfies
   \[
   d_m(A;V)\longrightarrow0.
   \tag{7}
   \]

   Define
   \[
   \omega_{\mathcal K}(L)
   =
   \sup\{\eta\ge0:\text{a width-tight finite approximation scheme at margin }\eta\text{ exists}\},
   \tag{8}
   \]
   with value `0` if no such scheme exists. Then, with `\tau_{\mathcal K}(L)` the compact-transversal margin from AF-072 and `\kappa_{\mathcal K}(L)` the precompact finite-scheme margin from AF-074,
   \[
   \boxed{
   \omega_{\mathcal K}(L)
   =
   \kappa_{\mathcal K}(L)
   =
   \tau_{\mathcal K}(L).
   }
   \tag{9}
   \]
   Consequently,
   \[
   \boxed{
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   \omega_{\mathcal K}(L)=0.
   }
   \tag{10}
   \]

3. **In Hilbert space, width tightness becomes a uniform finite-rank tail condition.** Let `H` be separable Hilbert and let `(P_m)` be increasing finite-rank orthogonal projections with `P_m\to I` strongly. For every bounded `A\subset H`,
   \[
   \boxed{
   A\text{ is relatively norm-compact}
   \iff
   \sup_{a\in A}\|(I-P_m)a\|\longrightarrow0.
   }
   \tag{11}
   \]
   Hence AF-074's finite witness pool is compactly selectable exactly when, in any fixed exhaustive orthogonal coordinate system, its high-dimensional tail vanishes **uniformly over all resolutions and all selected witnesses**:
   \[
   \sup_{n}\sup_{f\in F_n}\|(I-P_m)f\|\longrightarrow0.
   \tag{12}
   \]

4. **Per-resolution low complexity does not imply pooled fidelity.** In `H=\ell^2`, let `F_n=\{e_n\}` for the standard orthonormal basis. Every individual witness set lies in a one-dimensional subspace, but for the pooled set `A=\{e_n:n\ge1\}`,
   \[
   \boxed{
   d_m(A;H)=1
   \quad\forall m<\infty.
   }
   \tag{13}
   \]
   Thus there is maximal finite-dimensional escape even though every resolution separately has the smallest possible nontrivial linear description. This is the width-theoretic form of AF-073/AF-074's jumping-witness obstruction.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{compactly selectable provenance is equivalent to vanishing finite-dimensional approximation error;}\\
\text{the relevant complexity is that of the pooled witness family, not of each finite level separately;}\\
\text{a positive asymptotic width floor is an exact certificate of irreducible directional escape.}
\end{array}}
\tag{14}
\]

## Derivation

### Relative compactness forces Kolmogorov widths to vanish

Assume `A` is relatively compact and put `C=\overline A`, so `C` is compact. Fix `\varepsilon>0`. Choose a finite `\varepsilon`-net

\[
\{a_1,\ldots,a_N\}\subset C.
\tag{15}
\]

Let

\[
E=\operatorname{span}\{a_1,\ldots,a_N\}.
\tag{16}
\]

Then `\dim E\le N`, and every `a\in A` lies within `\varepsilon` of some `a_j\in E`. Hence

\[
d_N(A;V)\le\varepsilon.
\tag{17}
\]

Since `(d_m(A;V))_m` is nonincreasing, arbitrary `\varepsilon` gives

\[
d_m(A;V)\to0.
\tag{18}
\]

No convexity or linear structure of `A` is used. The finite-dimensional subspace is only a common approximation reservoir for a finite net of the compact set.

### Vanishing widths force total boundedness

Conversely, suppose `A` is bounded and

\[
d_m(A;V)\to0.
\tag{19}
\]

Choose `M<\infty` with `\|a\|\le M` for every `a\in A`. Fix `\varepsilon>0`. By (19), choose a finite-dimensional subspace `E\le V` such that

\[
\sup_{a\in A}d(a,E)<\varepsilon/3.
\tag{20}
\]

For each `a\in A`, choose `e_a\in E` with

\[
\|a-e_a\|<\varepsilon/3.
\tag{21}
\]

Then

\[
\|e_a\|\le M+\varepsilon/3.
\tag{22}
\]

The bounded subset

\[
B_E(0,M+\varepsilon/3)
\tag{23}
\]

is totally bounded because `E` is finite-dimensional. Choose a finite `\varepsilon/3`-net `Q\subset E` for that ball. For every `a\in A`, some `q\in Q` satisfies

\[
\|a-q\|
\le
\|a-e_a\|+\|e_a-q\|
<2\varepsilon/3
<\varepsilon.
\tag{24}
\]

Thus `A` is totally bounded. Since `V` is complete, its closure is compact, proving (2).

This direction identifies the load-bearing hypotheses precisely: width decay gives uniform approximation by finite-dimensional spaces; boundedness makes the approximating pieces bounded; finite-dimensionality turns boundedness into total boundedness; completeness turns total boundedness into relative compactness.

### AF-074 converts the classical compactness criterion into an exact fidelity criterion

For any pooled witness set in (6), boundedness is automatic because

\[
A\subseteq\mathbb S_V.
\tag{25}
\]

By (2), condition (7) is therefore equivalent to AF-074's requirement that `A` be relatively compact. The admissible schemes defining `\omega_{\mathcal K}(L)` and `\kappa_{\mathcal K}(L)` are exactly the same schemes written in two equivalent languages. Hence

\[
\omega_{\mathcal K}(L)=\kappa_{\mathcal K}(L).
\tag{26}
\]

AF-074 proves

\[
\kappa_{\mathcal K}(L)=\tau_{\mathcal K}(L),
\tag{27}
\]

which gives (9), and AF-072 then gives (10).

The substantive change is therefore not a new compactness theorem. It is an exact quantitative coordinate on the escape mechanism isolated by AF-071--AF-074: instead of asking only whether the pooled witnesses are precompact, one may measure how much irreducible error remains after the best `m`-dimensional compression.

## Hilbert-space uniform-tail criterion

Let `(P_m)` satisfy the hypotheses of item 3 and put

\[
Q_m=I-P_m.
\tag{28}
\]

Each `Q_m` is an orthogonal projection, so `\|Q_m\|\le1`, and strong convergence of `P_m` to `I` means

\[
Q_mx\to0
\qquad\forall x\in H.
\tag{29}
\]

If `A` is relatively compact, let `C=\overline A`. Fix `\varepsilon>0` and choose a finite `\varepsilon/3`-net `\{c_1,\ldots,c_N\}` for `C`. For sufficiently large `m`,

\[
\|Q_mc_j\|<\varepsilon/3
\qquad(j=1,\ldots,N).
\tag{30}
\]

For any `a\in A`, choose `c_j` with `\|a-c_j\|<\varepsilon/3`; then

\[
\|Q_ma\|
\le
\|Q_m(a-c_j)\|+\|Q_mc_j\|
<2\varepsilon/3.
\tag{31}
\]

Thus convergence is uniform on `A`.

Conversely, suppose

\[
\sup_{a\in A}\|Q_ma\|\to0.
\tag{32}
\]

For given `\varepsilon>0`, choose `m` so the supremum is below `\varepsilon/2`. The set `P_mA` is bounded inside the finite-dimensional range of `P_m`, hence has a finite `\varepsilon/2`-net. Since every `a\in A` lies within `\varepsilon/2` of `P_ma`, the same finite net is an `\varepsilon`-net for `A`. Therefore `A` is totally bounded and, because `H` is complete, relatively compact. This proves (11).

Equation (12) follows by substituting `A=\bigcup_nF_n`. It is stronger than pointwise tail decay for every fixed witness: the supremum over all resolutions must vanish.

## Exact controls

### Rotating one-dimensional witnesses have maximal pooled width

Let `A=\{e_n:n\ge1\}` in `\ell^2`. Fix an arbitrary `m`-dimensional subspace `E` and let `P_E` be its orthogonal projection. Choose an orthonormal basis `v_1,\ldots,v_m` for `E`. By Bessel's inequality,

\[
\sum_{n\ge1}\|P_Ee_n\|^2
=
\sum_{j=1}^m\sum_{n\ge1}|\langle e_n,v_j\rangle|^2
\le m.
\tag{33}
\]

Hence `\|P_Ee_n\|\to0` along a subsequence. Therefore

\[
\sup_n d(e_n,E)
=
\sup_n\sqrt{1-\|P_Ee_n\|^2}
=1.
\tag{34}
\]

Taking the infimum over all `E` proves (13). In the standard coordinate filtration, the same failure appears as

\[
\sup_n\|(I-P_m)e_n\|=1
\qquad\forall m.
\tag{35}
\]

Thus “every finite level has a low-dimensional witness” is not a substitute for a common low-dimensional approximation hierarchy.

### Width decay does not mean eventual finite-dimensionality

Let

\[
A=\{0\}\cup\{e_n/n:n\ge1\}\subset\ell^2.
\tag{36}
\]

This set is compact but has infinite-dimensional linear span. For

\[
E_m=\operatorname{span}\{e_1,\ldots,e_m\},
\]

one has

\[
d_m(A;\ell^2)
\le
\sup_{n>m}\frac1n
=
\frac1{m+1}
\longrightarrow0.
\tag{37}
\]

The fidelity resource is therefore **compressibility with improving dimension**, not containment in one fixed finite-dimensional model.

### Individual width bounds do not control the pooled width

Every singleton `F_n=\{e_n\}` has `d_1(F_n;H)=0`, yet their union has `d_m=1` for every finite `m`. Any truncation-based fidelity claim must therefore quantify over the pooled family or an equivalent cross-resolution object. Bounds proved separately at each resolution can be completely vacuous about survival in the limit.

## Prior art and novelty assessment

The width mechanism is classical.

- A. N. Kolmogoroff, **“Über die beste Annäherung von Funktionen einer gegebenen Funktionenklasse,”** *Annals of Mathematics* 37(1) (1936), 107–110. Role: original source of the finite-dimensional best-approximation quantity that became the Kolmogorov `n`-width.
- Allan Pinkus, ***n-Widths in Approximation Theory***, Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol. 7, Springer, Berlin (1985), DOI `10.1007/978-3-642-69894-1`. Role: standard monograph for Kolmogorov widths and their basic approximation-theoretic properties.
- Tizian Wenzel, Gabriele Santin, and Bernard Haasdonk, **“Analysis of Target Data-Dependent Greedy Kernel Algorithms: Convergence Rates for f-, f·P- and f/P-Greedy,”** *Constructive Approximation* 57 (2023), 45–74, DOI `10.1007/s00365-022-09592-3`. Role: modern explicit use of the standard compactness criterion `d_n\to0` and of Kolmogorov widths as the optimal common finite-dimensional approximation error; the paper cites Pinkus for the classical result.

No novelty is claimed for Kolmogorov widths, the equivalence between compactness and width decay for bounded sets in a Banach space, uniform convergence of exhaustive orthogonal projections on compact subsets of Hilbert space, or reduced finite-dimensional approximation itself. The prior-art audit makes clear that these are mature approximation-theoretic mechanisms.

The durable Arithmetic Fidelity result is the **exact translation of AF-074's compact-selectability criterion into width language**. AF-074 established that a global compact discriminator exists exactly when increasingly accurate finite witnesses can be chosen from one precompact pooled reservoir. AF-075 shows that this reservoir condition is equivalent to a quantitative hierarchy of common finite-dimensional models with vanishing worst-case residual, and that in Hilbert settings it can be tested by a uniform finite-rank tail. The contribution is therefore a reusable audit coordinate for the already-derived fidelity theorem, not a claim of a new theorem in approximation theory.

## Boundary conditions and audit

- **Boundedness is load-bearing for the converse in (2).** Vanishing distance to finite-dimensional subspaces does not by itself control unbounded motion inside those subspaces. For AF-074 witness pools boundedness is automatic because all witnesses lie on the unit sphere.
- **Completeness is load-bearing for relative compactness in `V`.** Width decay gives total boundedness in a normed space. Without completeness, the closure may become compact only after passing to the completion.
- **The topology is the norm topology.** Weak, weak-*, strong-operator, spectral-measure, probability-tightness, or other destination topologies require their own compactness and approximation criteria.
- **Kolmogorov widths are intrinsic but not necessarily constructive.** They optimize over all finite-dimensional subspaces. A small width does not by itself provide a canonical basis, algorithm, or natural lift.
- **Do not replace widths by a fixed projection sequence in an arbitrary Banach space.** General Banach spaces need not admit a useful exhaustive sequence of uniformly controlled finite-rank projections; the Hilbert corollary relies on orthogonal projections and separability. Equation (1) avoids imposing an approximation-property hypothesis that is irrelevant to the intrinsic compactness statement.
- **A positive width floor is a certificate of non-precompactness, not automatically of arithmetic failure.** A concrete RH application must first prove that its declared finite witnesses and norm topology are the correct carriers of the rational-prime discriminator.
- **No arithmetic specialization is asserted here.** The theorem supplies a candidate audit for truncations, spectral windows, finite moments, or bounded test families only after the concrete research line identifies the natural witness pool and proves that the compact-transversal model applies.

## Consequences for Arithmetic Fidelity

AF-071 showed that infinite-dimensional compact-target fidelity can fail through **directional escape** even when every individual cone stays maximally far from the target. AF-072 replaced that phenomenon by the exact compact-transversal criterion. AF-073 expressed the compact witness through a coherent finite multiscale tower, and AF-074 showed that explicit adjacency data are not fundamental: a precompact pooled witness reservoir is enough for compactness to select a coherent branch.

AF-075 now gives that reservoir an exact approximation profile. The sequence

\[
m\longmapsto d_m\!\left(\bigcup_nF_n;V\right)
\tag{38}
\]

measures how much common finite-dimensional structure remains unavailable at dimension `m`. Its vanishing is equivalent to survival of a compactly selectable discriminator; a positive limiting floor proves that every finite-dimensional description leaves a uniform residual and therefore that the proposed witness family escapes compact selection.

This supplies a practical conceptual rule for later compression audits: **do not ask only whether each finite truncation contains a discriminator; ask whether all those discriminators can be approximated uniformly by one growing finite-dimensional hierarchy.** In Hilbert/operator settings this becomes the concrete uniform-tail test (12). If the tail does not vanish, finite-level success does not assemble into a global retained structure; if it does vanish, AF-074's compactness machinery can extract one without requiring a predeclared identity map across resolutions.