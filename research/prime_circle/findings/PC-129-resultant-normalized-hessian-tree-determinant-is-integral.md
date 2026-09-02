# PC-129 — resultant-normalized Hessian tree determinant is integral

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `PRIOR-ART-REDIRECTION` + `NEGATIVE` for treating the raw finite determinant/pseudodeterminant of the PC-128 vertexwise resultant Hessian as a new zeta-like analytic object.

PC-128 identifies the full vertexwise second variation of the logarithmic interaction between two primitive shells with a positive weighted complete-bipartite Laplacian whose edge conductances are inverse-square chord lengths. A natural next attempt is to use a genuinely collective invariant of that maximal-rank matrix, rather than its individual entries: its reduced determinant or pseudodeterminant.

That invariant has an exact arithmetic collapse. Multiplying the reduced determinant by the square of the classical cyclotomic resultant always gives a positive integer. For coprime shell indices the resultant is `1`, so the reduced determinant itself is an integer. In the same coprime case, the entire edge-weight multiset is exactly the common-anchor inverse-square profile of the product shell `P_{mn}^*`, with the complete-bipartite incidence supplied only by the CRT factorization.

Thus the finite determinant does combine all pairwise edges, but it does not create a new transcendental or spectral parameter. It is a weighted spanning-tree polynomial evaluated on cyclotomic chord integers, with its only possible denominator controlled by the already-classical shell resultant.

## 1. The PC-128 Hessian and its Kirchhoff cofactor

Let

\[
A=P_m^*,\qquad B=P_n^*,\qquad m\ne n,
\]

with

\[
r=\varphi(m),\qquad s=\varphi(n).
\]

The shells are disjoint. For `alpha in A` and `beta in B`, define the squared chord and its inverse conductance

\[
\delta_{\alpha,\beta}:=|\alpha-\beta|^2,
\qquad
c_{\alpha,\beta}:=\delta_{\alpha,\beta}^{-1}.
\]

PC-128 proves that minus the Hessian of the real logarithmic resultant energy is the weighted Laplacian

\[
L_{m,n}=
\begin{pmatrix}
\operatorname{diag}(C\mathbf 1)&-C\\
-C^T&\operatorname{diag}(C^T\mathbf 1)
\end{pmatrix},
\qquad
C=(c_{\alpha,\beta}),
\]

of the complete bipartite graph `K_{r,s}`. All conductances are positive, so the graph is connected and `rank L_{m,n}=r+s-1`.

Let `kappa_{m,n}` denote any principal cofactor of `L_{m,n}`. By the weighted Matrix-Tree Theorem,

\[
\boxed{
\kappa_{m,n}
=
\sum_{T\in\mathcal T(K_{r,s})}
\prod_{e\in T}c_e,
}
\]

where every spanning tree has `r+s-1` edges. Equivalently, if `det'` denotes the product of the nonzero eigenvalues,

\[
\boxed{
\det' L_{m,n}=(r+s)\kappa_{m,n}.
}
\]

This is the most direct scalar spectral invariant of the maximal-rank Hessian left by PC-128.

## 2. The product of all chord denominators is exactly the cyclotomic resultant squared

Because both shells lie on the unit circle,

\[
\delta_{\alpha,\beta}
=(\alpha-\beta)(\overline\alpha-\overline\beta)
=(\alpha-\beta)(\alpha^{-1}-\beta^{-1}).
\]

Each `delta_{alpha,beta}` is therefore a real cyclotomic algebraic integer. Multiplying over all ordered shell pairs gives

\[
\prod_{\alpha\in P_m^*}
\prod_{\beta\in P_n^*}
\delta_{\alpha,\beta}
=
\left|
\prod_{\alpha\in P_m^*}
\prod_{\beta\in P_n^*}
(\alpha-\beta)
\right|^2.
\]

The inner product is the cyclotomic resultant up to its irrelevant conventional sign. Put

\[
R_{m,n}:=|\operatorname{Res}(\Phi_m,\Phi_n)|.
\]

Then exactly

\[
\boxed{
\prod_{e\in E(K_{r,s})}\delta_e=R_{m,n}^2.
}
\]

Now complement every spanning tree inside the complete edge set:

\[
\prod_{e\in T}c_e
=
\frac1{\prod_e\delta_e}
\prod_{e\notin T}\delta_e.
\]

Hence

\[
\boxed{
R_{m,n}^2\kappa_{m,n}
=
\sum_{T\in\mathcal T(K_{r,s})}
\prod_{e\notin T}\delta_e.
}
\]

The right-hand side is a finite polynomial with integer coefficients in the squared chord algebraic integers. This formula is exact and contains no limiting or analytic-continuation step.

## 3. Galois symmetry forces integrality

Let `L=lcm(m,n)`. Every `delta_{alpha,beta}` lies in the real subfield of `Q(mu_L)`. For any Galois automorphism

\[
\sigma_k:\zeta_L\mapsto\zeta_L^k,
\qquad k\in(\mathbb Z/L\mathbb Z)^\times,
\]

primitive `m`-th roots are permuted among themselves and primitive `n`-th roots are permuted among themselves. Thus `sigma_k` permutes the vertices, edges, and spanning trees of the weighted complete-bipartite graph. It follows that

\[
I_{m,n}:=
\sum_T\prod_{e\notin T}\delta_e
\]

is fixed by the full Galois group of `Q(mu_L)/Q`.

But `I_{m,n}` is also an algebraic integer, since it is a sum of products of algebraic integers. Therefore

\[
I_{m,n}\in\mathbb Q\cap\mathcal O_{\mathbb Q(\mu_L)}=\mathbb Z.
\]

All terms are positive under the standard complex embedding, so `I_{m,n}>0`. Consequently

\[
\boxed{
R_{m,n}^2\kappa_{m,n}=I_{m,n}\in\mathbb Z_{>0}.
}
\]

Equivalently,

\[
\boxed{
\kappa_{m,n}\in R_{m,n}^{-2}\mathbb Z_{>0},
\qquad
R_{m,n}^2\det' L_{m,n}=(r+s)I_{m,n}\in\mathbb Z_{>0}.
}
\]

So the reduced determinant of the inverse-square resultant Hessian is always rational, with denominator bounded by a completely classical cyclotomic resultant.

Apostol's cyclotomic-resultant theorem makes the denominator classification explicit. If `1<m<n`, then

\[
R_{m,n}=
\begin{cases}
p^{\varphi(m)},& n/m=p^a\text{ for a prime }p\text{ and }a\ge1,\\
1,&\text{otherwise}.
\end{cases}
\]

Therefore almost every pair of distinct shell indices has an **integral** Hessian cofactor; only prime-power-related nested indices can introduce a denominator, and even there that denominator divides the square of the known prime-power resultant.

## 4. Coprime shells are exactly the product-shell anchor profile reshaped by CRT

There is a stronger structural collapse when `(m,n)=1`. The map

\[
\boxed{
P_m^*\times P_n^*
\longrightarrow P_{mn}^*,
\qquad
(\alpha,\beta)\longmapsto\alpha\beta^{-1}
}
\]

is a bijection.

Indeed, writing `alpha=zeta_m^a` and `beta=zeta_n^b`, both `a` and `b` are units in their respective moduli. In `mu_{mn}` the quotient has exponent

\[
u=na-mb.
\]

Modulo `m`, `u congruent n a`, and modulo `n`, `u congruent -m b`; both are units because `(m,n)=1`. Hence `u` is a unit modulo `mn`, so the quotient is primitive of exact order `mn`. Conversely the two CRT residues recover `a` and `b`, and the cardinalities agree:

\[
\varphi(m)\varphi(n)=\varphi(mn).
\]

The chord conductance then satisfies

\[
\boxed{
 c_{\alpha,\beta}
 =\frac1{|\alpha-\beta|^2}
 =\frac1{|1-\alpha\beta^{-1}|^2}.
}
\]

Thus, as a weighted **edge set**, the PC-128 interaction between two coprime primitive shells contains exactly the same inverse-square values as the common-anchor profile on the single product shell `P_{mn}^*`. No new edge values appear at all. The only extra information in the Hessian is how the CRT projections of each primitive `mn`-th root attach that edge to its `m`-vertex and `n`-vertex endpoints.

Since coprime indices are certainly not related by a prime-power quotient, Apostol also gives `R_{m,n}=1`, so

\[
\boxed{
(m,n)=1
\Longrightarrow
\kappa_{m,n}=I_{m,n}\in\mathbb Z_{>0}.
}
\]

This links the PC-128 two-shell Hessian directly back to the pointed inverse-square profile classified in PC-035/PC-036, while identifying the CRT incidence as the only finite relational information not already present in the edge multiset.

## 5. Exact audit examples

For `(m,n)=(3,4)`, both shells have two vertices and

\[
C=
\begin{pmatrix}
2+\sqrt3&2-\sqrt3\\
2-\sqrt3&2+\sqrt3
\end{pmatrix}.
\]

Here `R_{3,4}=1`, and direct evaluation of any Laplacian cofactor gives

\[
\boxed{\kappa_{3,4}=8.}
\]

For the prime-power-related pair `(m,n)=(3,6)`,

\[
C=
\begin{pmatrix}
1&1/4\\
1/4&1
\end{pmatrix},
\qquad
R_{3,6}=4.
\]

The four spanning trees of `K_{2,2}` give

\[
\boxed{
\kappa_{3,6}=\frac58,
\qquad
R_{3,6}^2\kappa_{3,6}=16\cdot\frac58=10\in\mathbb Z.
}
\]

These two small cases exercise both branches of the resultant denominator formula.

## 6. Prior-art and novelty audit

The ingredients are classical, and no theorem-level novelty is claimed.

- The weighted Matrix-Tree Theorem is the standard Kirchhoff cofactor identity: a reduced weighted Laplacian determinant is the spanning-tree generating polynomial evaluated at its edge conductances. Modern weighted treatments use exactly this form.
- Apostol's 1970 theorem on resultants of cyclotomic polynomials, already anchored in `research/prime_circle/SOURCES.md`, gives the exact `1` versus prime-power classification of `R_{m,n}`.
- The coprime product-shell bijection is the ordinary Chinese-remainder decomposition of primitive roots of unity. It is cyclotomic structure, not a new arithmetic correspondence.
- PC-128 already identifies the Hessian itself with a classical inverse-square chord Laplacian and places the differential construction in the arrangement/Calogero neighborhood.

Directed searches combining weighted spanning-tree determinants, roots of unity, cyclotomic resultants, and resultant/master-function Hessians did not locate this exact Prime-Circle normalization statement. That absence is not a novelty claim. The durable contribution is the project-specific reduction: the most immediate collective scalar invariant of the PC-128 maximal-rank Hessian is arithmetically forced into a rational/integral Kirchhoff polynomial whose possible denominator is precisely controlled by classical cyclotomic resultant theory.

## 7. Research consequence and boundary

This closes the naive finite route

\[
\boxed{
\text{vertexwise shell resultant}
\to
\text{maximal-rank inverse-square Hessian}
\to
\text{raw reduced determinant / pseudodeterminant}
\to
\text{new zeta-like analytic factor}.
}
\]

At each fixed pair `(m,n)`, the determinant supplies no free complex spectral variable, no gamma factor, no functional equation, and no new zero divisor. After the canonical resultant normalization it is a positive integer; for coprime shells no normalization is needed at all. Turning the resulting integer sequence into a Dirichlet/Mellin generating function would be an additional cross-level construction whose analytic content would have to be justified separately rather than attributed to the finite Hessian determinant itself.

The result does **not** show that the full eigenvalue/eigenvector data of `L_{m,n}` are trivial. In the coprime case the CRT incidence pattern can still retain correlations invisible in the edge multiset. Nor does it rule out:

- genuinely cross-level operators coupling several Hessians before scalarization;
- nonlinear invariants of the CRT incidence data that are not fixed finite Kirchhoff evaluations;
- an infinite-level limit with an intrinsically forced normalization and proved analytic class;
- the nonlinear uniformization/monodromy branch of PC-017.

The practical boundary after PC-128 is therefore sharper: **taking the determinant is not enough**. Any surviving use of the bipartite Hessian must retain more than its Kirchhoff scalar, and for coprime shells it must exploit the CRT incidence of the already-known product-shell anchor weights rather than claim new local conductance data.