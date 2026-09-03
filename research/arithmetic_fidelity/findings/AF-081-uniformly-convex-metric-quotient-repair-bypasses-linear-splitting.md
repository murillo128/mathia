# AF-081 — Uniformly convex metric quotient repair bypasses linear splitting

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` be a real or complex Banach space, let `K\subseteq E` be a closed linear subspace, and let

\[
q:E\longrightarrow F=E/K
\tag{1}
\]

be the normalized quotient map, with `F` carrying the quotient norm

\[
\|y\|_F=\inf\{\|x\|_E:q x=y\}.
\tag{2}
\]

For `x\in E`, a **metric kernel repair** is obtained by choosing the nearest point of `K` to `x`. When that nearest point is unique, write

\[
P_K^{\mathrm{met}}(x)
=
\operatorname*{argmin}_{k\in K}\|x-k\|.
\tag{3}
\]

Then the following hold.

1. **Reflexivity and strict convexity give a unique norm-minimal repair for every closed quotient kernel.** If `E` is reflexive and strictly convex, every closed convex subset of `E`, hence every closed subspace `K`, is a Chebyshev set. Therefore (3) exists and is unique for every `x\in E`.

   The residual

   \[
   R_K(x)=x-P_K^{\mathrm{met}}(x)
   \tag{4}
   \]

   is invariant under translation by `K` and therefore factors uniquely through the quotient:

   \[
   R_K=s_K\circ q
   \tag{5}
   \]

   for a section

   \[
   s_K:F\to E,
   \qquad
   q\,s_K=I_F.
   \tag{6}
   \]

   It is characterized intrinsically by

   \[
   \boxed{
   q s_K(y)=y,
   \qquad
   \|s_K(y)\|=\|y\|_F.
   }
   \tag{7}
   \]

   Thus `s_K(y)` is the unique minimum-norm representative of the quotient class `y`, and

   \[
   \boxed{
   x=s_K(qx)+P_K^{\mathrm{met}}(x)
   }
   \tag{8}
   \]

   reconstructs the complete source from the retained quotient plus the metric repair coordinate.

2. **The metric repair is homogeneous and canonical relative to the declared norm geometry.** For every scalar `\alpha`,

   \[
   P_K^{\mathrm{met}}(\alpha x)=\alpha P_K^{\mathrm{met}}(x),
   \qquad
   s_K(\alpha y)=\alpha s_K(y).
   \tag{9}
   \]

   If `u:E\to E` is a surjective linear isometry with `u(K)=K`, and `v:F\to F` is the induced quotient isometry, then

   \[
   \boxed{
   P_K^{\mathrm{met}}u=uP_K^{\mathrm{met}},
   \qquad
   s_Kv=us_K.
   }
   \tag{10}
   \]

   Hence every symmetry preserving the full normed quotient data must preserve the repair. Unlike AF-078's unconstrained linear splittings, there is no shear torsor after minimum-norm selection has a unique solution.

3. **Uniform convexity closes a separate stability gate.** If `E` is uniformly convex, then it is reflexive and strictly convex, and the metric projection onto every closed convex subset is continuous. Consequently

   \[
   P_K^{\mathrm{met}}:E\to K
   \quad\text{and}\quad
   s_K:F\to E
   \tag{11}
   \]

   are continuous for every closed subspace `K`.

   The implication is genuinely stronger than existence and uniqueness. In general reflexive strictly convex spaces, metric projection onto an infinite-dimensional subspace can be discontinuous. Thus

   \[
   \boxed{
   \text{existence}\;\not\Rightarrow\;\text{uniqueness}\;\not\Rightarrow\;\text{stability}
   }
   \tag{12}
   \]

   without separate geometric hypotheses.

4. **Metric repair can exist canonically and continuously when every bounded linear repair is impossible.** For `1<p<\infty`, `p\ne2`, the space `\ell^p` is uniformly convex. By the Lindenstrauss--Tzafriri complemented-subspaces theorem, because `\ell^p` is not isomorphic to a Hilbert space, it contains a closed uncomplemented subspace `K`.

   For such a `K`, AF-078 gives

   \[
   \boxed{
   \text{no bounded linear }r:\ell^p\to K\text{ with }r|_K=I_K.
   }
   \tag{13}
   \]

   Nevertheless the uniformly convex norm gives the unique continuous metric repair

   \[
   P_K^{\mathrm{met}}:\ell^p\to K
   \tag{14}
   \]

   and the unique continuous minimum-norm section `s_K:\ell^p/K\to\ell^p` satisfying (7). Therefore the linear splitting obstruction is **category-specific rather than an absolute information-loss obstruction**: allowing the norm geometry to select a nonlinear representative can repair a quotient whose Banach-space extension does not split linearly.

5. **Linearity is an additional rigidity condition, not a consequence of canonical metric recovery.** Under the uniqueness hypotheses above, the metric section `s_K` is linear if and only if the quotient admits a linear isometric section. Indeed, if `s_K` is linear then (6)--(7) make it a linear isometric right inverse of `q`. Conversely, any linear section `t:F\to E` satisfying

   \[
   qt=I_F,
   \qquad
   \|t(y)\|=\|y\|_F
   \tag{15}
   \]

   already picks a minimum-norm representative in every fiber, so uniqueness forces `t=s_K`.

   Thus the uncomplemented `\ell^p` example forces the canonical continuous metric section to be nonlinear. Canonicity, continuity, homogeneity, and linearity are four distinct properties.

6. **Continuous nonlinear sections exist far beyond the metric regime, but generally without canonical selection.** The classical Bartle--Graves theorem says that every surjective bounded linear map between Banach spaces admits a continuous nonlinear right inverse; modern standard formulations can choose it positively homogeneous and with a norm bound arbitrarily close to the open-mapping constant.

   Applied to `q`, this means that continuity alone does not distinguish the metric construction: even a quotient with an uncomplemented kernel has many continuous nonlinear sections. The extra content of (7) is instead

   \[
   \boxed{
   \text{fiberwise norm minimality}+\text{uniqueness},
   }
   \tag{16}
   \]

   which makes the section intrinsic to the declared norm geometry. Bartle--Graves and metric projection therefore expose a useful tradeoff: generic topology supplies continuous selections with choice freedom, while sufficiently convex geometry can supply a distinguished minimum-norm selection.

7. **The canonicity is genuinely carried by the middle-space geometry, not by the endpoint spaces alone.** Take the same algebraic exact sequence

   \[
   0\to\mathbb R\times\{0\}
   \to\mathbb R^2
   \xrightarrow{q}\mathbb R
   \to0,
   \qquad
   q(x,y)=y,
   \tag{17}
   \]

   and for `\rho\in\mathbb R` equip the middle space with the Hilbert norm

   \[
   \|(x,y)\|_\rho
   =
   \sqrt{(x+\rho y)^2+y^2}.
   \tag{18}
   \]

   Every `\rho` induces the same norm `|x|` on `K` and the same quotient norm `|y|` on `F`, but the minimum-norm representative and repair are

   \[
   s_\rho(y)=(-\rho y,y),
   \qquad
   P_{K,\rho}^{\mathrm{met}}(x,y)=(x+\rho y,0).
   \tag{19}
   \]

   Thus even fixed endpoint norms and fixed algebraic inclusion/quotient maps do not determine the metric repair. The coupling encoded in the source norm is exactly the additional provenance that selects one complement.

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\begin{array}{c}
\text{quotient loss has different repair gates in different categories;}\\
\text{linear repair requires a split extension (AF-078), while metric repair need not;}\\
\text{reflexive strict convexity selects a unique norm-minimal representative in every fiber;}\\
\text{uniform convexity also gives continuity, but linearity remains a separate rigidity condition.}
\end{array}}
\tag{20}
\]

## Derivation

### Reflexivity gives existence and strict convexity gives uniqueness

Fix `y\in F` and choose `x_0\in E` with `qx_0=y`. The fiber

\[
C_y=x_0+K
\tag{21}
\]

is nonempty, closed, and convex. Its distance from the origin is exactly `\|y\|_F`.

Choose a minimizing sequence `x_n\in C_y` with

\[
\|x_n\|\downarrow\|y\|_F.
\tag{22}
\]

The sequence is bounded. Reflexivity supplies a weakly convergent subsequence after the standard weak-compactness reduction, say `x_{n_j}\rightharpoonup x_*`. Closed convex subsets of a Banach space are weakly closed, so `x_*\in C_y`. Weak lower semicontinuity of the norm gives

\[
\|x_*\|
\le
\liminf_j\|x_{n_j}\|
=
\|y\|_F.
\tag{23}
\]

The reverse inequality follows from the quotient-norm definition, hence equality holds and a minimum-norm representative exists.

Suppose `x_1,x_2\in C_y` are two distinct minimizers of common nonzero norm `d`. Their midpoint remains in `C_y`, while strict convexity gives

\[
\left\|\frac{x_1+x_2}{2}\right\|<d,
\tag{24}
\]

contradiction. For `d=0`, the unique minimizer is `0`. This proves existence and uniqueness of `s_K(y)`.

Equivalently, minimizing `\|x-k\|` over `k\in K` gives a unique point `P_K^{\mathrm{met}}(x)`. The two descriptions satisfy

\[
s_K(qx)=x-P_K^{\mathrm{met}}(x).
\tag{25}
\]

### Translation invariance makes the residual descend to the quotient

Let `k_0\in K`. If `p=P_K^{\mathrm{met}}(x)`, then for any `k\in K`,

\[
\|(x+k_0)-(p+k_0)\|
=
\|x-p\|
\le
\|x-k\|
=
\|(x+k_0)-(k+k_0)\|.
\tag{26}
\]

Uniqueness therefore forces

\[
P_K^{\mathrm{met}}(x+k_0)
=P_K^{\mathrm{met}}(x)+k_0.
\tag{27}
\]

Subtracting from `x+k_0` shows that `R_K` is constant on quotient fibers, proving (5). Equation (7) follows because `R_K(x)` is precisely the minimum-norm point in `x+K`.

Scalar homogeneity follows by the same uniqueness argument: multiplying a best approximation by `\alpha` multiplies all distances by `|\alpha|` and preserves `K`.

### Full normed symmetry forces equivariance

Let `u` be as in (10). If `p=P_K^{\mathrm{met}}(x)`, then `up\in K`, and for every `k\in K`, surjectivity of `u|_K` gives `k=uk'` for some `k'\in K`. Hence

\[
\|ux-up\|
=
\|x-p\|
\le
\|x-k'\|
=
\|ux-k\|.
\tag{28}
\]

So `up` is the nearest point of `K` to `ux`, and uniqueness proves the first identity in (10). Subtracting gives the section identity. This is the exact symmetry sense in which minimum-norm repair is canonical: every automorphism of the declared normed data fixes it.

### Uniform convexity upgrades the unique selection to a continuous one

Uniform convexity implies reflexivity and strict convexity. It also gives the Kadec--Klee/approximative-compactness control needed for convergence of minimizing points: if `x_n\to x`, the unique nearest points to a fixed closed convex set cannot remain separated while achieving distances converging to the same infimum. The classical metric-projection theorem therefore makes `P_K^{\mathrm{met}}` continuous.

Since

\[
R_K=I_E-P_K^{\mathrm{met}}
\tag{29}
\]

is continuous and constant on fibers of the quotient map, the factor `s_K` in (5) is continuous by the defining quotient topology. This establishes (11).

The stronger geometry is not cosmetic. Classical approximation theory contains reflexive strictly convex Banach spaces with infinite-dimensional Chebyshev subspaces whose metric projections are discontinuous. Hence strict convexity plus reflexivity closes the pointwise selection problem but does not universally close the stability problem.

### An uncomplemented `\ell^p` kernel separates nonlinear metric repair from AF-078

For `1<p<\infty`, `\ell^p` is uniformly convex. For `p\ne2` it is not isomorphic to Hilbert space. The Lindenstrauss--Tzafriri theorem states that a Banach space in which every closed subspace is complemented must be isomorphic to Hilbert space. Consequently there exists at least one closed uncomplemented

\[
K\subset\ell^p.
\tag{30}
\]

AF-078 identifies a bounded linear repair `r:E\to K`, `r|_K=I`, with a bounded projection onto `K`; therefore no such linear repair exists for (30).

But uniform convexity gives the unique continuous metric projection (14). This is a direct matched control against interpreting AF-078's nonsplitting obstruction as destruction of all possible intrinsic recovery. What fails is **linear** recovery in the Banach-space category. A richer admissible category retaining the norm geometry still contains enough structure to select the lost coordinate continuously, at the price of nonlinearity.

### The endpoint-preserving norm family isolates where the selection information lives

For (18), fixing `y` and minimizing over the `K` coordinate gives

\[
\inf_{x\in\mathbb R}
\sqrt{(x+\rho y)^2+y^2}
=|y|,
\tag{31}
\]

with unique minimizer `x=-\rho y`. Hence all `\rho` induce the same quotient norm while (19) varies with `\rho`.

Likewise on `K`, setting `y=0` gives `\|(x,0)\|_\rho=|x|`. Therefore neither endpoint norm changes. Only the middle-space coupling changes, and that change is exactly what moves the canonical complement. This is the metric analogue of AF-078's extension-gluing warning: endpoint categories alone need not encode the relational structure that selects a repair.

## Exact controls

### Nonunique control: strict convexity is not decorative

Take `E=(\mathbb R^2,\|\cdot\|_\infty)` and `K=\mathbb R\times\{0\}`. The point `(0,1)` has distance `1` from `K`, but every `(a,0)` with `|a|\le1` is a nearest point. Thus minimum-distance language alone does not define a canonical repair when the norm has flat faces.

### Continuous but noncanonical control: Bartle--Graves

For an arbitrary Banach quotient `q:E\to F`, Bartle--Graves supplies a continuous homogeneous right inverse even when `K` is uncomplemented. Such a selection is not determined by fiberwise norm minimization and generally comes from choices made in the selection construction. Therefore “a continuous nonlinear lift exists” is too weak to count as intrinsic provenance recovery.

The uniformly convex metric section is stronger in a different direction: it is the only section satisfying exact norm minimality (7), so its identity is forced by the declared geometry.

### Canonical but unstable boundary

Reflexive strict convexity is enough to make every closed subspace Chebyshev, but classical examples show that the resulting metric projection can be discontinuous for infinite-dimensional subspaces. Therefore a proposal that uses unique nearest representatives downstream must audit continuity or an equivalent stability property separately rather than infer it from uniqueness.

### Hilbert endpoint

In Hilbert space the metric repair is ordinary orthogonal projection. It is linear, norm one, and `1`-Lipschitz. AF-081 therefore contains the AF-078 Hilbert positive control as the special regime where metric canonicity, continuity, and linear splitting coincide. Away from Hilbert geometry they separate.

## Prior art and novelty assessment

The mathematical ingredients are classical approximation and Banach-space theory.

- **“Chebyshev set,”** *Encyclopedia of Mathematics*. It records the classical characterization that every closed convex subset of a Banach space is Chebyshev exactly when the space is reflexive and strictly convex.
- **“Metric projection,”** *Encyclopedia of Mathematics*. It records that metric projections onto Chebyshev subspaces are generally nonlinear, that discontinuity can occur for an infinite-dimensional subspace of a reflexive strictly convex space, and that Hilbert-space projection onto closed convex sets is `1`-Lipschitz.
- Robert G. Bartle and Lawrence M. Graves, **“Mappings between function spaces,”** *Transactions of the American Mathematical Society* 72 (1952), 400--413. DOI `10.1090/S0002-9947-1952-0047910-X`. This is the classical source behind continuous nonlinear selections for surjective Banach-space maps.
- Milen Ivanov, Jesús A. Jaramillo, Sebastián Lajara, and Nadia Zlateva, **“Continuous Selections and Invertibility of Nonsmooth Maps Between Banach Spaces,”** *Journal of Optimization Theory and Applications* 206 (2025). DOI `10.1007/s10957-025-02692-7`. Their Theorem 4 states a modern global Bartle--Graves formulation with a continuous positively homogeneous right inverse and quantitative norm control.
- Joram Lindenstrauss and Lior Tzafriri, **“On the complemented subspaces problem,”** *Israel Journal of Mathematics* 9(2) (1971), 263--269. DOI `10.1007/BF02771592`. Their theorem supplies the Hilbert-space characterization used to force an uncomplemented subspace inside `\ell^p`, `p\ne2`.

No novelty is claimed for Chebyshev subspaces, metric projections, Bartle--Graves selection, uniform convexity, or the Lindenstrauss--Tzafriri theorem. The Arithmetic Fidelity contribution is the **category comparison** forced by AF-078--AF-080: the same quotient can fail the linear repair gate while admitting a unique norm-minimal nonlinear repair, and canonicity, continuity, and linearity are controlled by different pieces of geometry. The endpoint-preserving family (18)--(19) makes explicit that the extra fidelity data live in the middle-space coupling rather than in the quotient endpoints alone.

## Boundaries and failure modes

- The metric repair recovers the whole lost kernel coordinate, so it is an upper-bound carrier, not a proof that a particular discriminator needs that much side information.
- `s_K` is norm-preserving in the radial sense `\|s_K(y)\|=\|y\|`, but it need not preserve pairwise distances because it need not be additive. Do not call it an isometric embedding unless linearity has been proved.
- Reflexivity without strict convexity gives existence of nearest points for closed convex fibers but not uniqueness in general.
- Strict convexity without an existence theorem does not guarantee that every closed fiber attains its infimum.
- Reflexive strict convexity gives a canonical pointwise repair but does not by itself guarantee continuity of every infinite-dimensional metric projection.
- Uniform convexity supplies continuity here, but not linearity or Hilbertian nonexpansiveness.
- Bartle--Graves proves that a continuous section exists for every Banach quotient, so continuity by itself is not evidence of an intrinsic or minimal repair.
- The `\ell^p` control proves existence of some uncomplemented closed `K`; it does not assert that every closed subspace of `\ell^p` is uncomplemented.
- The norm family (18) varies the middle-space geometry. Its purpose is precisely to show that endpoint data do not select a metric repair; it is not a counterexample to canonicity once the full norm on `E` is fixed.

## Consequences for Arithmetic Fidelity

AF-078 showed that exact linear kernel recovery has two gates: a split extension must exist, and extra structure is then needed to select a point from the repair torsor. AF-079 showed how symmetry changes both gates, and AF-080 showed that order can collapse the torsor exactly on projection bands.

AF-081 adds a qualitatively different regime. **Norm geometry can replace the linear splitting gate rather than merely refine it.** In a uniformly convex source every closed quotient kernel has a distinguished continuous repair, including kernels for which no bounded linear projection exists. The price is that the repair may be genuinely nonlinear.

This suggests a reusable audit for later Mathia compressions. When a canonical carrier appears impossible in one category, do not immediately conclude that the information is gone. Ask separately whether a richer structure supplies: (i) fiberwise attainment, (ii) uniqueness, (iii) stability, and (iv) compatibility with the downstream operator category. A repair that succeeds only by moving to nonlinear metric geometry cannot then be fed silently into a later argument that requires linear, spectral, trace, or positivity structure.
