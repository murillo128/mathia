# PC-379 — Branch-resolved Chebyshev refinement is a flat tent/Cuntz system

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most canonical matrix-valued escape left after PC-376--PC-378. Keeping every inverse branch of the source-forced Chebyshev refinement before the scalar average does retain information that `P_m` discards, and the resulting branch operators are genuinely noncommuting. However, after the canonical angle coordinate they are exactly the standard branch isometries of an `m`-fold full tent map. For each degree they form a Cuntz family, and across different refinement factorizations every apparent matrix cocycle is only a permutation between two labelings of the same final branches. The transition permutations are flat: around every factorization loop their product is the identity. The intrinsic branch orientation and half-density Jacobian also multiply exactly and create no projective phase. Thus the branch-resolved Chebyshev correspondence itself supplies no new Prime-Circle arithmetic or RH-sensitive matrix holonomy.

## 1. The arcsine Chebyshev system is exactly a full tent map

PC-372 forced the real shell-2 coordinate

\[
\lambda=\frac{1+\cos\theta}{2}
\]

and the refinement maps

\[
C_m(\lambda)=\frac{1+T_m(2\lambda-1)}2,
\qquad m\ge2.
\tag{1}
\]

PC-373--PC-376 then identified the invariant arcsine probability measure

\[
d\mu(\lambda)=\frac{d\lambda}{\pi\sqrt{\lambda(1-\lambda)}}.
\tag{2}
\]

Put

\[
t=\frac1\pi\arccos(2\lambda-1)\in[0,1],
\qquad
\lambda(t)=\frac{1+\cos(\pi t)}2.
\tag{3}
\]

Equation (2) becomes exactly Lebesgue measure `dt`. In this coordinate, (1) is conjugate to

\[
F_m(t)=\frac1\pi\arccos\!\bigl(\cos(m\pi t)\bigr).
\tag{4}
\]

This is the full `m`-fold tent map. On the monotonicity interval

\[
I_{m,j}=\left[\frac jm,\frac{j+1}{m}\right],
\qquad 0\le j<m,
\tag{5}
\]

its slope is `(-1)^j m`, and the inverse branch is

\[
\tau_{m,j}(x)=
\begin{cases}
(j+x)/m,&j\ \text{even},\\
(j+1-x)/m,&j\ \text{odd}.
\end{cases}
\tag{6}
\]

Thus the full inverse-branch geometry that is hidden by the averaged transfer operator is not merely analogous to a generic expanding map: it is exactly a piecewise-linear full tent system after the canonical invariant-measure coordinate change.

## 2. Resolving the branches gives a canonical Cuntz family

Work on

\[
H=L^2([0,1],dt).
\]

For each branch define

\[
(S_{m,j}f)(t)
:=\sqrt m\,\mathbf 1_{I_{m,j}}(t)\,f(F_m(t)).
\tag{7}
\]

Since `F_m:I_{m,j}->[0,1]` is a bijection of absolute slope `m`, a change of variables gives

\[
S_{m,j}^*S_{m,k}=\delta_{jk}I,
\qquad
\sum_{j=0}^{m-1}S_{m,j}S_{m,j}^*=I.
\tag{8}
\]

So for every `m` the complete branch-resolved row is a Cuntz family. Its adjoints are explicitly

\[
(S_{m,j}^*g)(x)=m^{-1/2}g(\tau_{m,j}(x)).
\tag{9}
\]

The scalar transfer used in PC-376 is just the symmetric branch compression

\[
P_mg
=\frac1m\sum_{j=0}^{m-1}g\circ\tau_{m,j}
=\frac1{\sqrt m}\sum_{j=0}^{m-1}S_{m,j}^*g.
\tag{10}
\]

Therefore it is correct that `P_m` loses branch information. The important question is whether the **full row** carries a source-forced cross-level matrix invariant that survives the classical scalar collapse. The answer below is negative for the canonical branch correspondence itself.

## 3. Cross-level products are only reflected mixed-radix relabelings

The Chebyshev/tent maps satisfy

\[
F_n\circ F_m=F_m\circ F_n=F_{mn}.
\tag{11}
\]

More strongly, the branch operators multiply exactly. For `0<=j<m` and `0<=k<n`, define

\[
\ell_{m,n}(j,k)
=
\begin{cases}
jn+k,&j\ \text{even},\\
jn+n-1-k,&j\ \text{odd}.
\end{cases}
\tag{12}
\]

Then direct substitution of (6) gives

\[
\tau_{m,j}\circ\tau_{n,k}
=\tau_{mn,\ell_{m,n}(j,k)},
\tag{13}
\]

and hence

\[
\boxed{
S_{m,j}S_{n,k}
=S_{mn,\ell_{m,n}(j,k)}.
}
\tag{14}
\]

For fixed `m,n`, the map

\[
E_{m,n}:(j,k)\longmapsto \ell_{m,n}(j,k)
\tag{15}
\]

is a bijection from the `mn` ordered branch pairs onto the `mn` final branches of `F_{mn}`. The apparent noncommutativity between the two factorization orders is therefore only the permutation

\[
\Pi_{m,n}=E_{n,m}^{-1}E_{m,n}
\tag{16}
\]

between two mixed-radix labelings of the **same geometrically ordered final branch set**.

This extends without change to any factorization `N=m_1...m_r`. Multiplying the corresponding branch isometries gives a unique `S_{N,l}`, so every factorization path `alpha` defines a bijection

\[
E_\alpha:\prod_i\{0,\ldots,m_i-1\}\longrightarrow\{0,\ldots,N-1\}.
\tag{17}
\]

For two factorizations `alpha,beta` of the same `N`, the transition matrix is the permutation induced by

\[
\Pi_{\alpha,\beta}=E_\beta^{-1}E_\alpha.
\tag{18}
\]

Consequently, for any three such paths,

\[
\Pi_{\beta,\gamma}\Pi_{\alpha,\beta}
=\Pi_{\alpha,\gamma},
\qquad
\Pi_{\alpha,\alpha}=I.
\tag{19}
\]

In particular **every closed factorization loop has trivial holonomy**. Any nontrivial-looking spectrum of an individual path-swap permutation is a coordinate effect of comparing two branch labelings. Label the paths by their canonical final interval `I_{N,l}` and the entire cocycle becomes the identity.

## 4. Orientation and half-density weights do not repair the flatness

The one source-forced branch phase discarded by an absolute Jacobian is the orientation sign. From (5),

\[
\varepsilon_{m,j}=\operatorname{sgn}F_m'|_{I_{m,j}}=(-1)^j.
\tag{20}
\]

Equation (12) gives the exact parity identity

\[
(-1)^{\ell_{m,n}(j,k)}=(-1)^{j+k},
\tag{21}
\]

so branch orientation composes multiplicatively:

\[
\varepsilon_{mn,\ell}
=\varepsilon_{m,j}\varepsilon_{n,k}.
\tag{22}
\]

Thus retaining the intrinsic sign does not create a projective factorization cocycle. Under the canonical final-branch label it is simply the orientation of that final branch.

The same is true of the Jacobian amplitude. In the angle coordinate every branch has constant absolute slope `m`, so any natural density or half-density factor is a scalar power of `m` and satisfies exact multiplicativity under `m,n -> mn`. In the original `lambda` coordinate this is precisely the endpoint/arcsine coboundary already isolated in PC-373 and the half-density normalization of PC-374. Resolving the branches does not turn that scalar coboundary into a matrix curvature.

PC-375 already showed that an arbitrary unimodular one-map branch decoration cannot change the normalized `L^2(mu)` spectrum. PC-379 adds the missing cross-level statement for the **canonical branch labels themselves**: before averaging, their multi-degree factorization coherence is still flat.

## 5. Matched control is exact and removes the cyclotomic source

Equations (4)--(19) use only the full `m`-fold tent maps and Lebesgue measure. They can be defined directly on `[0,1]` without roots of unity, primitive layers, cyclotomic polynomials, or the common anchored vertex. The branch family, its noncommutativity, its Cuntz relations, and every factorization transition permutation are then literally identical.

This is a stronger matched control than replacing a prime degree by a composite degree. Even if the degrees retained are exactly the primes, the branch-resolved architecture itself is the generic full-tent architecture; multiplying prime generators only recovers the same integer-degree semigroup. Primality enters only through the external choice of which degrees to highlight, not through a different branch law.

Therefore neither a determinant of the path-swap matrices, nor their eigenvalues, nor a matrix product around refinement-order loops can be counted as a new Prime-Circle invariant. The last class is exactly trivial by (19), while the first two depend on a noncanonical comparison of branch coordinates and are reproduced by the nonarithmetic tent control.

## 6. Prior-art and novelty audit

The operator-algebraic setting is classical. PC-241 already identified the original unit-circle coordinate plus power-map refinement with Cuntz's established `ax+b` semigroup algebra; the Chebyshev maps arise from that circle power map after the inversion/Joukowski fold. The exact reflected mixed-radix law (12) is the interval/tent manifestation of that same addition-dilation architecture.

More generally, Kajiwara and Watatani associate Cuntz--Pimsner algebras to rational-map dynamics in **C*-Algebras associated with complex dynamical systems**, *Indiana University Mathematics Journal* 54:3 (2005), 755--778, DOI `10.1512/iumj.2005.54.2530`; their basic examples explicitly include the interval/tent dynamics obtained from `z^2-2`. Their later **Dimension groups for self-similar maps and matrix representations of the cores of the associated C*-algebras**, *Canadian Journal of Mathematics* 73:4 (2021), treats the full tent map itself as an established self-similar operator-algebraic model. These references confirm that a branch-resolved tent/Cuntz construction is prior-art territory rather than a new RH spectral mechanism.

The project-local exact contribution is narrower: equations (12)--(19) classify the simultaneous multi-degree Chebyshev branch factorization relevant to the current Prime-Circle frontier and show that its most obvious cross-level matrix cocycle is a **flat permutation coboundary**. This conclusion is proved directly and does not depend on a literature nonexistence claim, so no new `SOURCES.md` dependency is required.

## 7. Falsification checks and sharp boundary

The result is directly falsifiable. In the angle coordinate: (i) verify that each `F_m` has the inverse branches (6); (ii) compose two branches and recover (12)--(14); (iii) enumerate all `mn` pairs and check that `E_{m,n}` is bijective; (iv) compare three factorization labelings and verify (19); and (v) retain the derivative signs and verify (21). Exhaustive finite checks for `2<=m,n<=8` agree with the exact formulas, but the formulas themselves are the evidence.

PC-379 does **not** rule out every matrix or noncommuting cross-shell construction. It rules out the most canonical candidate obtained by retaining the complete inverse-branch label of the Chebyshev refinement, its intrinsic orientation, and its natural Jacobian normalization. A surviving matrix mechanism must add source data that is not determined by the generic full-tent covering: for example a primitive-shell/chord/cyclotomic amplitude attached to branches, a genuinely nonlinear interaction of branch values before the final-branch identification, a source-forced domain/topology not equivalent to the tent correspondence, or a multi-shell operator that cannot be trivialized by labeling paths with the common final branch.

## Research consequence

The sequence PC-372--PC-378 showed that shell-2 order refinement is real but its canonical scalar Koopman/transfer, phase, all-prime sum, and commuting Euler-product completions are universal or classical. The obvious next repair was to stop averaging and keep the full inverse-branch matrix data. PC-379 closes that repair at the level forced by the Chebyshev covering itself: **the branch row is a generic Cuntz/tent system and cross-level factorization order carries no intrinsic holonomy beyond a flat relabeling**. Any meaningful continuation must couple branch labels to additional Prime-Circle geometry rather than promote the branch labels themselves to the missing arithmetic carrier.