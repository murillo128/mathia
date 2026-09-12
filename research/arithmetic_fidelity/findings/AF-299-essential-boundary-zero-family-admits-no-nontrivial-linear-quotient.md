# AF-299 — Essential boundary-zero families admit no nontrivial linear target-null quotient

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `TARGET-RELATIVE`, `HYPERPLANE-ARRANGEMENT`, `LINEAR-QUOTIENT`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-298 leaves reduction of the target-relevant perturbation dimension as one possible escape from the sharp `N^{-1/2}` margin ceiling for full-rank boundary-observation Gram metrics. For the AF-290 boundary-zero discriminant, however, **global linear dimension reduction cannot be target-null**.

The underlying statement is elementary and more general. Let `V` be a finite-dimensional complex vector space, let

\[
\{\ell_a:V\to\mathbb C\}_{a\in A}
\]

be a family of nonzero linear functionals, and define the failure set

\[
\Delta:=\bigcup_{a\in A}\ker\ell_a
\]

and its common invisible subspace

\[
C:=\bigcap_{a\in A}\ker\ell_a.
\]

For a linear compression `q:V\to W` with kernel `K`, exactly two regimes occur:

1. If `K\subseteq C`, then `\Delta` is saturated by the quotient fibers and
   \[
   \boxed{\Delta=q^{-1}(q(\Delta)).}
   \tag{1}
   \]
   Thus failure membership can descend through `q`.
2. If `K\not\subseteq C`, then
   \[
   \boxed{q(\Delta)=q(V).}
   \tag{2}
   \]
   Every quotient state is compatible with a failure input. If `\Delta\ne V`, failure membership therefore cannot factor through `q` at all.

Consequently the largest linear subspace that may be quotiented out while preserving this union-of-hyperplanes failure discriminator is exactly the common center `C`. When `C=\{0\}`, the hyperplane family is essential in the relevant linear sense and **every exact linear quotient preserving failure membership is injective**.

For the finite Dirichlet-polynomial coefficient space

\[
P_c(s)=\sum_{n=1}^N c_n n^{-s},
\qquad c\in\mathbb C^N,
\]

and AF-290's boundary-zero discriminant

\[
\Delta_{\Gamma,N}
:=
\{c:\exists z\in\Gamma\text{ with }P_c(z)=0\},
\]

where `Gamma` is a compact rectifiable Jordan curve, the common center is trivial:

\[
\boxed{
\bigcap_{z\in\Gamma}\ker L_z=\{0\},
\qquad L_z(c)=P_c(z).
}
\tag{3}
\]

Moreover `\Delta_{\Gamma,N}\ne\mathbb C^N`, since the coefficient vector `(1,0,\ldots,0)` gives the constant polynomial `1`. Therefore every linear compression `q:\mathbb C^N\to W` with nonzero kernel satisfies

\[
\boxed{
q(\Delta_{\Gamma,N})=q(\mathbb C^N).
}
\tag{4}
\]

In particular, for every boundary-safe coefficient vector `b`, including the eta truncation vector used in AF-291--AF-298, there exists `c\in\Delta_{\Gamma,N}` with `q(c)=q(b)`. The quotient cannot assign any positive distance from `q(b)` to the image of boundary failure: that distance is exactly zero.

The same obstruction applies to every rank-deficient positive-semidefinite coefficient metric. If `G\ge0` and `\operatorname{rank}G<N`, then with

\[
\|x\|_G=(x^*Gx)^{1/2}
\]

one has, for every `b`,

\[
\boxed{
\operatorname{dist}_G(b,\Delta_{\Gamma,N})=0.
}
\tag{5}
\]

Thus the most literal attempt to beat AF-298 by lowering the linear observation dimension does not merely fail to improve the `N^{-1/2}` rate. It destroys exact boundary-zero robustness completely. Any useful effective-dimension reduction must therefore be justified by structure outside a global linear quotient of the unrestricted coefficient space: for example a nonlinear symmetry quotient, a source-restricted admissible class whose discarded directions cannot reach the discriminant, or genuinely richer coupled/source-derived information.

## Quotient saturation for a family of failure hyperplanes

Let `K=ker q`.

If `K\subseteq C`, then every `h\in K` lies in every `ker ell_a`. Hence

\[
\ell_a(v+h)=\ell_a(v)
\qquad(a\in A).
\]

Membership in every individual failure hyperplane, and therefore membership in their union `Delta`, is constant on cosets of `K`. This is exactly (1).

Now suppose `K\not\subseteq C`. Choose `h\in K` with `h\notin C`. By definition of `C`, there is some `a_0\in A` such that

\[
\ell_{a_0}(h)\ne0.
\]

Take an arbitrary `v\in V` and set

\[
v'
:=
v-
\frac{\ell_{a_0}(v)}{\ell_{a_0}(h)}h.
\tag{6}
\]

Then

\[
\ell_{a_0}(v')=0,
\]

so `v'\in\Delta`. But `v-v'` is a scalar multiple of `h\in K`, hence

\[
q(v')=q(v).
\]

Because `v` was arbitrary, every point of `q(V)` is the image of some failure input. This proves (2).

The conclusion is stronger than a generic loss-of-information statement. Once the quotient deletes even one direction seen by one failure functional, **the failure set becomes surjective onto the whole quotient**, rather than merely producing a few mixed fibers.

If `Delta ne V`, exact recovery of the Boolean discriminator `1_Delta` is therefore equivalent to `K subseteq C`: sufficiency follows from (1), while necessity follows from (2), because a point outside `Delta` then shares its quotient value with a point inside `Delta`.

This is the union-of-linear-failure-surfaces specialization of AF-001's general fiber criterion, with the common kernel `C` giving the maximal admissible target-null linear subspace explicitly.

## Boundary evaluation has trivial common kernel

For the Dirichlet boundary family, write

\[
L_z(c)=\sum_{n=1}^N c_n n^{-z}.
\]

Suppose `c` belongs to every `ker L_z` for `z\in\Gamma`. Then the entire function

\[
P_c(s)=\sum_{n=1}^N c_n e^{-s\log n}
\]

vanishes on all of `Gamma`. The curve contains accumulation points in `\mathbb C`, so the identity theorem gives

\[
P_c(s)\equiv0.
\]

Finite Dirichlet expansions are linearly independent. One direct proof is enough here. If `c\ne0`, let `m` be the least index with `c_m\ne0`. For real `sigma`,

\[
0=m^\sigma P_c(\sigma)
=c_m+
\sum_{n>m}c_n\left(\frac{m}{n}\right)^\sigma.
\]

Letting `sigma\to+\infty` forces `c_m=0`, a contradiction. Therefore `c=0`, proving (3).

Equivalently, the evaluation normals `{r_z:z\in\Gamma}` span `\mathbb C^N`. In particular a finite subset of at most `N` boundary evaluations already spans the dual and has trivial common kernel. Thus the obstruction does not depend on treating the continuum of boundary points as a nonstandard infinite hyperplane arrangement: a finite essential subarrangement is already enough to force (4).

## Rank-deficient Gram and seminorm geometries have zero failure margin

Let `G\ge0` have rank strictly smaller than `N`. Its nullspace

\[
K:=\ker G
\]

is nonzero. By (3), `K` cannot lie in the common kernel of all boundary evaluations. Hence choose `h\in K` and `z\in\Gamma` with `L_z(h)\ne0`.

For any nominal coefficient vector `b`, define

\[
c
:=
b-
\frac{L_z(b)}{L_z(h)}h.
\tag{7}
\]

Then `L_z(c)=0`, so `c\in\Delta_{\Gamma,N}`. At the same time

\[
b-c\in\ker G,
\]

and therefore

\[
\|b-c\|_G=0.
\]

This proves (5) exactly.

The conclusion covers a broad class of seemingly attractive dimension-reducing repairs: a singular observation Gram matrix, an orthogonal projection followed by any positive-definite metric on its image, or any other linear feature map with rank below `N`. If the perturbation class remains the full coefficient space, the deleted direction can always be used to move the nominal point onto one of the boundary-zero hyperplanes without changing the compressed representation.

## Relation to AF-298's effective-dimension ceiling

AF-298 proved that every full-rank metric generated by positive averages of scalar boundary evaluations pays a sharp normalized margin of order `N^{-1/2}` after optimal reweighting. Its trace identity

\[
\int_\Gamma K_{\mu,N}(z)\,d\mu(z)=N
\]

identified full target-relevant dimension as the remaining bill, and left a justified lower-dimensional representation as one possible escape.

AF-299 separates two notions that could otherwise be conflated:

- **conditioning the same `N`-dimensional target geometry** can redistribute leverage but cannot beat the `N^{-1/2}` ceiling inside AF-298's class;
- **deleting linear coefficient directions globally** does not reduce that bill to `\sqrt r` for some `r<N`; instead it makes the boundary-zero discriminant fill the quotient and collapses the exact margin to zero.

So a useful statement such as "the target really has effective dimension `r<N`" now has an additional proof obligation. It must show why the discarded degrees of freedom are absent, gauge, constrained, or otherwise inadmissible **before** taking the quotient. Merely observing that the final target is low-dimensional, choosing a low-rank metric, or projecting the coefficients onto a smaller linear feature space cannot establish target-nullity.

This also clarifies why AF-295's global complex-scalar projective quotient is not contradicted by the theorem. Multiplication by a nonzero complex scalar is a group action on nonzero coefficient rays, not translation along a fixed additive kernel. The boundary-zero discriminant is homogeneous under that action, so projectivization is a genuine symmetry quotient. AF-299 rules out nontrivial **additive linear kernels** in coefficient space, not independently justified nonlinear or projective gauges.

## Prior art and novelty assessment

The general linear-algebra ingredients are classical and no broad novelty is claimed.

- Peter Orlik and Hiroaki Terao, ***Arrangements of Hyperplanes***, Grundlehren der mathematischen Wissenschaften 300, Springer (1992), DOI `10.1007/978-3-662-02772-1`, is the standard comprehensive source for finite hyperplane arrangements, including rank/essentiality and the role of the common intersection. In standard arrangement language a central arrangement is essential when its hyperplane normals span the ambient dual space, equivalently when its common intersection is trivial.
- Passing from an inessential arrangement to its essential part by removing the common invisible directions is standard arrangement theory. Here the finite subfamily of Dirichlet boundary evaluations with spanning normals is already essential.
- The implication `K not subset C => q(Delta)=q(V)` is derived above in one line of linear algebra. No novelty is claimed for it as an abstract theorem, even if this exact saturation formulation is not usually singled out in arrangement terminology.
- The identity theorem for holomorphic functions and linear independence of finite exponential/Dirichlet sums are classical.

The Arithmetic Fidelity contribution is the exact placement of these facts at the AF-298 frontier. AF-290's ill-posed set is not merely a generic complicated discriminant: it is a union of evaluation hyperplanes with trivial common center. That makes the hoped-for global linear target-null quotient impossible in the strongest form—every proper linear quotient identifies every output with some boundary failure input.

## Boundaries and failure modes

- The theorem concerns a **global linear quotient of the full finite coefficient space**. It does not rule out a lower-dimensional nonlinear source manifold whose tangent or secant geometry excludes the constructed failure moves.
- A source-restricted family may evade the obstruction if the vector `v'` in (6) or (7) is not an admissible source. Such a claim requires an explicit source class and a proof that its quotient fibers do not meet the discriminant in the forbidden way.
- The result does not rule out genuine symmetry quotients such as projectivization by global nonzero scaling, nor other nonlinear equivalence relations under which `Delta` is saturated.
- It does not rule out derivative, vector-valued, coupled, nonlocal, or source-derived observables. Those may change the relevant failure set rather than merely quotient the same scalar-evaluation discriminant.
- It does not say that a low-dimensional final statistic is impossible. It says that an exact low-dimensional **linear coefficient representation** cannot retain the boundary-zero failure discriminator on the unrestricted coefficient class.
- The result is finite-dimensional and target-relative. It establishes no global zeta reconstruction, zero-free region, or RH consequence.

## Consequence for the line

After AF-298, "reduce the effective target dimension" was a legitimate but underspecified escape. AF-299 removes its most direct linear realization. For the boundary-zero target, there is no nonzero additive coefficient direction that is invisible to every failure surface, so there is no nontrivial global target-null linear quotient to take.

The live dimension-reduction question must therefore become source-relative or nonlinear: identify a canonical constrained source class or genuine symmetry for which the discarded directions cannot move a valid source to boundary failure, and quantify whether the resulting lower-dimensional geometry still carries the arithmetic discriminator needed downstream. Otherwise the apparent dimension reduction is only deletion of directions that the zero-count target actually uses.