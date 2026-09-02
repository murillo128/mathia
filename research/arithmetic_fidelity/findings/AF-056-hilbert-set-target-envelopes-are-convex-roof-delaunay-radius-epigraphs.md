# AF-056 — Hilbert set-target safe envelopes are convex-roof variance epigraphs and finite targets are Delaunay radius epigraphs

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `PRIOR-ART-REDIRECT`, `STRUCTURAL-CLASSIFICATION`

## Claim

Let `Y` be a real Hilbert space, let `M\subseteq Y` be a finite-dimensional closed linear subspace, and let

\[
C:M\hookrightarrow Y
\]

be the inclusion. Let `S\subset M` be nonempty and compact. For every `y\in Y`, write the orthogonal decomposition

\[
y=m+v,
\qquad
m=P_My\in M,
\qquad
v\in M^\perp.
\tag{1}
\]

Define the **barycentric variance roof**

\[
V_S(m)
=
\inf\left\{
\sum_{i=1}^k\lambda_i\|s_i-m\|^2:
\begin{array}{l}
k\ge1,\ s_i\in S,\ \lambda_i\ge0,\\
\sum_i\lambda_i=1,\ \sum_i\lambda_i s_i=m
\end{array}
\right\},
\tag{2}
\]

with the convention `V_S(m)=+\infty` when `m\notin\operatorname{conv}(S)`. Compactness and finite dimensionality make the infimum a minimum whenever it is finite.

Then:

1. **AF-054's maximal safe target envelope has an exact orthogonal-epigraph form.**
   \[
   \boxed{
   \mathcal E_C(S)
   =
   \left\{
   m+v:
   m\in\operatorname{conv}(S),\ v\in M^\perp,
   \ \|v\|^2\ge V_S(m)
   \right\}.
   }
   \tag{3}
   \]
   Thus a new orthogonal degree of freedom is safe exactly when its squared size pays the minimum barycentric variance required to represent the descended point by the original target.

2. **The threshold is a standard convex-roof quantity.** Define the extended-real function
   \[
   f_S(z)=
   \begin{cases}
   \|z\|^2,&z\in S,\\
   +\infty,&z\notin S.
   \end{cases}
   \tag{4}
   \]
   and let `f_S^{**}` be its Fenchel biconjugate. Then
   \[
   \boxed{
   V_S(m)=f_S^{**}(m)-\|m\|^2.
   }
   \tag{5}
   \]
   Equivalently, `f_S^{**}` is the lower closed convex envelope of the squared norm restricted to `S`, and `V_S` is its vertical gap above the paraboloid.

3. **The original compact target is exactly the zero-threshold locus.**
   \[
   \boxed{
   V_S(m)=0
   \iff
   m\in S.
   }
   \tag{6}
   \]
   More quantitatively,
   \[
   V_S(m)\ge \operatorname{dist}(m,S)^2
   \qquad
   (m\in\operatorname{conv}(S)).
   \tag{7}
   \]
   Hence the collective safe points found in AF-055 do not erase the target: they occupy orthogonal fibers above `\operatorname{conv}(S)\setminus S` at a strictly positive threshold.

4. **Convex targets have no collective horizontal enlargement.** If `S` is convex, then
   \[
   V_S(m)=
   \begin{cases}
   0,&m\in S,\\
   +\infty,&m\notin S,
   \end{cases}
   \tag{8}
   \]
   and therefore
   \[
   \boxed{
   \mathcal E_C(S)=S+M^\perp.
   }
   \tag{9}
   \]
   If `S` is nonconvex and `M^\perp\ne\{0\}`, every point of `\operatorname{conv}(S)\setminus S` generates genuinely collective safe points at sufficiently large orthogonal radius.

5. **For a finite target, the threshold is exactly the classical lower-paraboloid/Delaunay radius function.** Let `S\subset M\cong\mathbb R^d` be finite and consider the lifted sites
   \[
   \widehat s=(s,\|s\|^2)\in\mathbb R^{d+1}.
   \tag{10}
   \]
   The graph of `f_S^{**}` over `\operatorname{conv}(S)` is the lower convex hull of these lifted sites. Its projected faces form the ordinary Delaunay subdivision, with nonsimplicial cells allowed in cospherical degeneracies.

   On a Delaunay cell `D` supported by an empty circumsphere with center `c_D` and radius `R_D`,
   \[
   f_S^{**}(m)
   =2\langle c_D,m\rangle+R_D^2-\|c_D\|^2
   \qquad(m\in D),
   \tag{11}
   \]
   so
   \[
   \boxed{
   V_S(m)=R_D^2-\|m-c_D\|^2
   \qquad(m\in D).
   }
   \tag{12}
   \]
   Therefore, over each Delaunay cell,
   \[
   \boxed{
   m+v\in\mathcal E_C(S)
   \iff
   \|m-c_D\|^2+\|v\|^2\ge R_D^2.
   }
   \tag{13}
   \]
   The unsafe refined target points above `D` are precisely those lying strictly inside its empty circumsphere after the orthogonal refinement is included.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{finite-dimensional Hilbert set-target safety}
\ =\ 
\text{convex-roof / Delaunay radius geometry};
}
\tag{14}
\]

so the set-valued Hilbert residual left open by AF-055 is largely classical rather than a new fidelity mechanism. The remaining research frontier must move to settings where this reduction no longer applies: non-Hilbert metrics, nonlinear refinements, category-constrained target transport, or arithmetic-specific admissibility.

## Derivation

### Reduction to a scalar threshold on the orthogonal fiber

AF-054 defines

\[
\mathcal E_C(S)
=
\left\{
 y\in Y:
 \|x-y\|\ge\operatorname{dist}(x,S)
 \text{ for every }x\in M
\right\}.
\tag{15}
\]

Write `y=m+v` as in (1). Since `x-m\in M` and `v\in M^\perp`, Pythagoras gives

\[
\|x-y\|^2
=
\|x-m\|^2+\|v\|^2.
\tag{16}
\]

Hence `y` is safe iff

\[
\|v\|^2
\ge
\sup_{x\in M}
\left(
\operatorname{dist}(x,S)^2-\|x-m\|^2
\right).
\tag{17}
\]

Call the supremum on the right `\Delta_S(m)`.

### Fenchel biconjugation identifies the threshold

For fixed `x`, expand

\[
\begin{aligned}
\operatorname{dist}(x,S)^2-\|x-m\|^2
&=
\inf_{s\in S}
\left(
\|x-s\|^2-\|x-m\|^2
\right)\\
&=
\inf_{s\in S}
\left(
2\langle x,m-s\rangle
+\|s\|^2-\|m\|^2
\right).
\end{aligned}
\tag{18}
\]

For `f_S` from (4),

\[
f_S^*(p)
=
\sup_{s\in S}
\left(
\langle p,s\rangle-\|s\|^2
\right).
\tag{19}
\]

Therefore

\[
\begin{aligned}
f_S^{**}(m)
&=
\sup_{p\in M}
\left(
\langle p,m\rangle-f_S^*(p)
\right)\\
&=
\sup_{p\in M}
\inf_{s\in S}
\left(
\langle p,m-s\rangle+\|s\|^2
\right).
\end{aligned}
\tag{20}
\]

Setting `p=2x`, which ranges over all of `M`, and comparing (18) with (20) yields the exact identity

\[
\Delta_S(m)=f_S^{**}(m)-\|m\|^2.
\tag{21}
\]

Thus the safe-envelope problem is already a convex-envelope problem.

### Convex-roof representation equals barycentric variance

In finite dimension, `f_S^{**}` is the closed convex envelope of `f_S`. Since the lifted graph

\[
\{(s,\|s\|^2):s\in S\}
\tag{22}
\]

is compact, its convex hull is compact. Consequently, for `m\in\operatorname{conv}(S)`, the minimum vertical coordinate above `m` is attained and equals

\[
f_S^{**}(m)
=
\min
\left\{
\sum_i\lambda_i\|s_i\|^2:
\sum_i\lambda_i s_i=m,
\ \lambda_i\ge0,
\ \sum_i\lambda_i=1
\right\}.
\tag{23}
\]

For every admissible barycentric representation,

\[
\sum_i\lambda_i\|s_i\|^2-\|m\|^2
=
\sum_i\lambda_i\|s_i-m\|^2,
\tag{24}
\]

because the cross term vanishes under `\sum_i\lambda_i(s_i-m)=0`. Combining (21)--(24) proves

\[
\Delta_S(m)=V_S(m).
\tag{25}
\]

If `m\notin\operatorname{conv}(S)`, a strict separating affine functional can be scaled in (20), giving

\[
f_S^{**}(m)=+\infty.
\tag{26}
\]

Substituting into (17) proves the envelope formula (3).

### The zero set and the convex case

Every term in (2) is nonnegative, so `V_S\ge0`. If `m\in S`, the one-point barycentric representation gives `V_S(m)=0`.

Conversely, if `m\in\operatorname{conv}(S)`, then every admissible representation satisfies

\[
\sum_i\lambda_i\|s_i-m\|^2
\ge
\operatorname{dist}(m,S)^2.
\tag{27}
\]

Taking the minimum proves (7). Since `S` is compact, `m\notin S` implies `\operatorname{dist}(m,S)>0`, so `V_S(m)>0`. This proves (6).

If `S` is convex, then `\operatorname{conv}(S)=S`; hence (6) and the convention outside the convex hull give (8), and (3) reduces to (9).

If `S` is nonconvex, choose `m\in\operatorname{conv}(S)\setminus S`. Then

\[
0<V_S(m)<\infty.
\tag{28}
\]

When `M^\perp` is nontrivial, choose any `v` with `\|v\|^2\ge V_S(m)`. The point `m+v` is safe although its projection `m` is not in the original target. This is exactly the collective phenomenon isolated qualitatively in AF-055.

### Finite targets are lower paraboloid hulls

Now let `S` be finite. Equation (23) says that the graph of `f_S^{**}` is the lower boundary of the convex hull of the lifted sites (10). This is the standard paraboloid lifting construction for the Delaunay subdivision.

Let `D` be the projection of one lower face. Its vertices lie on a sphere with center `c_D` and radius `R_D`, so for every site `s` on that face,

\[
\|s-c_D\|^2=R_D^2.
\tag{29}
\]

Expanding gives

\[
\|s\|^2
=
2\langle c_D,s\rangle
+R_D^2-\|c_D\|^2.
\tag{30}
\]

The empty-sphere condition says all other sites lie on or outside that sphere, hence their lifted heights lie on or above the affine hyperplane in (30). Therefore that hyperplane is exactly the lower-hull piece over `D`, proving (11). Subtracting `\|m\|^2` gives

\[
\begin{aligned}
V_S(m)
&=
2\langle c_D,m\rangle
+R_D^2-\|c_D\|^2-\|m\|^2\\
&=
R_D^2-\|m-c_D\|^2,
\end{aligned}
\tag{31}
\]

which proves (12), and (13) follows from (3).

## Exact controls

### AF-055's two-point example becomes the exterior of a disk over its chord

Take

\[
M=\mathbb R\times\{0\}\subset Y=\mathbb R^2,
\qquad
S=\{(-1,0),(1,0)\}.
\tag{32}
\]

For `m=(t,0)` with `|t|\le1`, the unique barycentric weights are

\[
\lambda_- =\frac{1-t}{2},
\qquad
\lambda_+=\frac{1+t}{2}.
\tag{33}
\]

Both sites lie on the one-dimensional sphere with center `0` and radius `1`, so

\[
V_S(t)=1-t^2.
\tag{34}
\]

Writing `v=(0,h)`, formula (3) gives the complete safe envelope

\[
\boxed{
\mathcal E_C(S)
=
\{(t,h): |t|\le1,\ t^2+h^2\ge1\}.
}
\tag{35}
\]

Thus AF-055's point `(0,1)` is not an isolated curiosity: it lies exactly on the Delaunay-radius boundary. The unsafe target additions over the chord are the points strictly inside the unit disk.

### Adding a target point refines the Delaunay safety geometry

If the target is enlarged to

\[
S'=\{(-1,0),(0,0),(1,0)\},
\tag{36}
\]

then the Delaunay cells are the intervals `[-1,0]` and `[0,1]`, each with radius `1/2`. Consequently

\[
V_{S'}(t)=|t|-t^2
\qquad(|t|\le1).
\tag{37}
\]

In particular `V_{S'}(0)=0`, as required because the newly added midpoint is now a genuine target point. The single collective cap of (35) splits into two smaller Delaunay caps. This verifies that the threshold records the exact finite target rather than only its convex hull.

## Prior art and novelty assessment

The mathematics behind this classification is classical. No novelty is claimed for convex biconjugation, lower convex hulls, paraboloid lifting, Delaunay mosaics, or their radius functions.

- R. Tyrrell Rockafellar, ***Convex Analysis***, Princeton University Press (1970). Role: Fenchel conjugacy/biconjugacy and the identification of the biconjugate with the closed convex envelope in finite-dimensional convex analysis.
- David W. Walkup and Roger J.-B. Wets, **“Lifting Projections of Convex Polyhedra,”** *Pacific Journal of Mathematics* 28(2), 465--475 (1969), DOI `10.2140/pjm.1969.28.465`. Role: classical lifting-projection framework for convex polyhedra.
- Phan Thanh An, Nam Dung Hoang, and Nguyen Kieu Linh, **“The Lifting Projection of Convex Polyhedra for Finding Delaunay Triangulations,”** *Journal of Convex Analysis* 29(1), 143--156 (2022). Role: explicit modern account of obtaining Delaunay cells from the lower convex hull after paraboloid lifting.
- Ranita Biswas, Sebastiano Cultrera di Montesano, Herbert Edelsbrunner, and Morteza Saghafian, **“Continuous and Discrete Radius Functions on Voronoi Tessellations and Delaunay Mosaics,”** *Discrete & Computational Geometry* 67, 811--842 (2022), DOI `10.1007/s00454-022-00371-2`. Role: decisive direct prior art for the finite-target residual. Their Delaunay-side continuous function is the difference between a piecewise-linear convex envelope and the paraboloid; with their normalization `\varpi(x)=\|x\|^2/2`, the unweighted finite-site mechanism is exactly `V_S/2` on the Delaunay cells.
- Kewei Zhang, **“Compensated Convexity and its Applications,”** *Annales de l'Institut Henri Poincaré C, Analyse non linéaire* 25(4), 743--771 (2008), DOI `10.1016/J.ANIHPC.2007.08.001`. Role: nearby convex-envelope theory for squared-distance functions to compact and finite sets, reinforcing that quadratic convexification of distance geometry is an established analytic mechanism.

AF-055 already identified ordinary singleton safe envelopes with classical best coapproximation and flagged simultaneous coapproximation as adjacent literature. A bounded follow-up search confirms that a best-simultaneous-coapproximation literature exists, but the accessible sources checked here do not establish an exact identity with the variable-nearest-target relation in (15). No such equivalence or novelty claim is made.

The durable contribution of this finding is therefore **classification and redirection** inside Arithmetic Fidelity: the general AF-054 condition, specialized to compact targets in finite-dimensional Hilbert refinements, has a complete convex-roof description, and its finite-target collective geometry is an established Delaunay radius construction rather than a new mathematical species.

## Boundaries and failure modes

- Finite dimensionality of `M` and compactness of `S` are used to avoid closure/attainment complications in the convex-roof representation. Infinite-dimensional or noncompact variants require separate hypotheses.
- The orthogonal decomposition and squared Pythagorean identity are essential. The theorem does not extend verbatim to general Banach norms or arbitrary metric refinements.
- The finite-target Delaunay statement is Euclidean. Cospherical degeneracies produce nonsimplicial Delaunay cells, but the lower-face and empty-sphere formula remains valid cellwise.
- The theorem classifies the maximal **metric** safe envelope. It does not decide which target enlargements are admissible under an external category, naturality condition, operator structure, arithmetic provenance constraint, or other line-specific notion of legitimate repair.
- The result does not imply that every set-target coapproximation problem in the literature is equivalent to AF-054; only the exact Hilbert safe-envelope problem stated here has been classified.
- Nothing here distinguishes rational primes or supplies an RH mechanism. Its value is to remove another apparently new abstract escape route before arithmetic specialization.

## Consequence for the Arithmetic Fidelity frontier

AF-054 showed that target transport, not only representation geometry, controls repair-radius invariance. AF-055 then classicalized singleton linear targets as best coapproximation while leaving genuinely set-valued targets as a residual.

This finding closes a large part of that residual in Hilbert geometry:

\[
\boxed{
\text{compact set target}
\longrightarrow
\text{convex roof of }\|\cdot\|^2
\longrightarrow
\text{barycentric variance threshold},
}
\tag{38}
\]

and, for finite targets,

\[
\boxed{
\text{barycentric variance threshold}
\longrightarrow
\text{lower paraboloid hull}
\longrightarrow
\text{Delaunay radius function}.
}
\tag{39}
\]

Future work should therefore not mine ordinary Hilbert set-target envelopes for purportedly new fidelity structure. A nonclassical residual must come from an additional restriction that the convex-roof/Delaunay reduction does not encode: non-Hilbert geometry, nonlinear embeddings, intrinsically constrained target families, categorical/naturality requirements, or the later arithmetic problem of preserving rational-prime provenance under a declared compression.