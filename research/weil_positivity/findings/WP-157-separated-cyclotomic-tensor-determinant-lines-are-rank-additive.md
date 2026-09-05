# WP-157 — Separated cyclotomic tensor determinant lines are rank-additive

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE + MULTIVARIATE-SEPARATED-COMPLETE-INTERSECTION + TRACE-DISCRIMINANT + PRODUCT-GRAM + KRONECKER-FACTORIZATION + RANK-NORMALIZED-ADDITIVITY + NO-IRREDUCIBLE-MIXED-PRIME-COUPLING + MATCHED-POPULATION-CONTROL + PRIOR-ART-CLASSICALIZATION` for the separated-variable multivariate/tensor-product determinant-line escape left open by `WP-156`.

`WP-156` shows that grouping Prime-Circle cyclotomic shells inside one **univariate** polynomial does not create a new global interaction: block resultants and discriminants factor through the old pairwise resultant carrier. The next canonical determinant-line escape is genuinely multivariate in variables but still geometrically separated: give different prime coordinates different variables, form the product finite scheme / tensor product of their cyclotomic coordinate algebras, and use its trace discriminant or a positive product Gram metric.

That move also fails before any subtle number theory enters. For finite-dimensional algebras, the trace pairing on a tensor product is the tensor product of the trace pairings. Its Gram matrix is a Kronecker product, so its determinant is a rank-weighted product of the factor determinants. After the natural normalization by total rank, the logarithmic determinant is **exactly additive over factors**. Every mixed finite difference between two distinct prime coordinates vanishes.

The same statement holds for any positive product Gram geometry: positivity survives perfectly, but its normalized log-volume contains only the sum of the local log-volumes. If one keeps the full positive tensor Gram form instead of taking its determinant, mixed coefficients appear as products and give the generic full-support positive completion rather than the sparse Weil selector. Thus the separated multivariate construction reproduces the same selector/sign tension in a sharper categorical form: product positivity gives mixed bulk, while the logarithmic determinant that exposes `log p` forgets the mixed geometry.

Consequently `WP-156` can be narrowed: **multivariate variables by themselves are not enough.** A surviving determinant/cohomological route must introduce source-forced equations, correspondences, differentials, metrics, or boundary data that couple distinct prime coordinates (and ultimately the real place) before the determinant or positivity theorem is applied. Merely tensoring independent cyclotomic factors cannot do it.

## 1. The trace pairing of a tensor product is a Kronecker product

Let `A` and `B` be finite-dimensional unital algebras over `Q`, of dimensions

\[
\dim_{\mathbf Q}A=m,
\qquad
\dim_{\mathbf Q}B=n.
\tag{1}
\]

Use the regular traces

\[
\tau_A(a)=\operatorname{Tr}(L_a),
\qquad
\tau_B(b)=\operatorname{Tr}(L_b),
\tag{2}
\]

where `L_a` denotes left multiplication. On the tensor-product algebra, left multiplication by a pure tensor factorizes:

\[
L_{a\otimes b}=L_a\otimes L_b.
\tag{3}
\]

The elementary trace identity for Kronecker products therefore gives

\[
\boxed{
\tau_{A\otimes B}(a\otimes b)
=
\tau_A(a)\tau_B(b).
}
\tag{4}
\]

Choose bases `e_1,...,e_m` of `A` and `f_1,...,f_n` of `B`. Their trace-pairing Gram matrices are

\[
G_A=(\tau_A(e_i e_j))_{i,j},
\qquad
G_B=(\tau_B(f_k f_\ell))_{k,\ell}.
\tag{5}
\]

In the product basis `e_i\otimes f_k`, equation (4) gives the exact matrix identity

\[
\boxed{
G_{A\otimes B}=G_A\otimes G_B.
}
\tag{6}
\]

No choice of ordering of the product basis changes the determinant except by the square of a permutation determinant, hence not at all. For separable algebras the trace forms are nondegenerate and the discriminants are nonzero.

## 2. Rank normalization removes every apparent mixed determinant interaction

For square matrices of sizes `m` and `n`,

\[
\det(G_A\otimes G_B)
=
(\det G_A)^n(\det G_B)^m.
\tag{7}
\]

Hence

\[
\boxed{
\log|\det G_{A\otimes B}|
=
n\log|\det G_A|+m\log|\det G_B|.
}
\tag{8}
\]

The raw determinant can look collective because each local logarithm is multiplied by the population of the other factor. That is exactly the population effect already isolated for `N\log N` in `WP-156`. Normalize by the number `mn` of product states:

\[
\delta(A)
:=
\frac1{\dim A}\log|\det G_A|.
\tag{9}
\]

Then (8) becomes

\[
\boxed{
\delta(A\otimes B)=\delta(A)+\delta(B).
}
\tag{10}
\]

For a finite family `A_1,...,A_r`, with `d_i=\dim A_i` and `D=\prod_i d_i`, iteration yields

\[
\det G_{\otimes_i A_i}
=
\prod_i (\det G_{A_i})^{D/d_i},
\tag{11}
\]

and therefore

\[
\boxed{
\frac1D\log|\det G_{\otimes_i A_i}|
=
\sum_i \frac1{d_i}\log|\det G_{A_i}|.
}
\tag{12}
\]

If the factor in coordinate `i` varies through a family `A_i(x_i)`, the normalized determinant density has the form

\[
\delta(x_1,\ldots,x_r)=\sum_i\delta_i(x_i).
\tag{13}
\]

Thus for distinct coordinates `i\ne j`, every mixed finite difference vanishes exactly:

\[
\boxed{
\Delta_i\Delta_j\,\delta=0.
}
\tag{14}
\]

This is a stronger obstruction than merely observing a sparse example. The canonical separated tensor discriminant has no algebraic slot in which an irreducible mixed-prime term can occur after rank normalization.

## 3. Cyclotomic specialization gives exactly the old prime-coordinate additive density

For a prime power `p^a`, take the cyclotomic factor algebra

\[
A_{p,a}
=
\mathbf Q[z_p]/(\Phi_{p^a}(z_p)).
\tag{15}
\]

It is a finite separable field of rank `\varphi(p^a)`, and the determinant of its trace pairing in the power basis is the cyclotomic discriminant up to the conventional sign. `WP-156` already records the exact normalized absolute value

\[
\boxed{
\delta(A_{p,a})
=
\left(a-\frac1{p-1}\right)\log p.
}
\tag{16}
\]

Now give distinct primes independent variables and form the separated multivariate coordinate algebra

\[
A_P
=
\bigotimes_{p\in P} A_{p,a_p}.
\tag{17}
\]

Equations (12) and (16) give

\[
\boxed{
\delta(A_P)
=
\sum_{p\in P}
\left(a_p-\frac1{p-1}\right)\log p.
}
\tag{18}
\]

So the canonical zero-dimensional multivariate product does not improve the self-discriminant density from `WP-156`; it reproduces it exactly. In particular it is nonzero on many integers with `\Lambda(n)=0`, and on a prime-power tower it depends on the exponent `a` rather than returning the exponent-independent Mangoldt value `\log p`.

For pairwise coprime prime-power conductors the tensor product is the corresponding cyclotomic compositum, and (18) agrees with the ordinary cyclotomic discriminant formula for the product conductor. The separated multivariate presentation therefore does not reveal hidden interaction that was lost by writing the same arithmetic object in one variable.

## 4. Positive product metrics obey the same determinant law

The preceding trace form need not itself be a positive real quadratic form, so it cannot be used to smuggle positivity into the conclusion. Instead take arbitrary finite-dimensional real or complex Hilbert spaces `H_i` with independently positive definite Gram matrices `M_i`. The canonical product metric on

\[
H=\bigotimes_i H_i
\tag{19}
\]

has Gram matrix

\[
\boxed{M=\bigotimes_i M_i\succ0.}
\tag{20}
\]

Its determinant satisfies exactly the same formula (11), and hence its rank-normalized log-volume satisfies exactly the same additivity (12).

Thus an **independent geometric positivity theorem is fully compatible with the obstruction**: product positivity does not create the needed interaction. The normalized determinant line can export local logarithmic scales, but it exports them only additively.

There is also a complementary failure if one refuses to collapse the metric to its determinant. Matrix entries of a product Gram form factor as products of local entries. Generic nontrivial local factors therefore produce mixed-coordinate coefficients automatically. Those terms are the positive bulk required by tensor-product positivity; they do not have the one-prime/prime-power sparsity of the finite Weil selector. Projecting them away afterward returns to the positive-quotient and sparse-self-energy obstructions already isolated in `WP-096`--`WP-099`.

So the two natural readouts separate cleanly:

\[
\boxed{
\begin{array}{ll}
\text{keep the positive product Gram form}
&\Rightarrow \text{mixed full-support bulk},\\[2mm]
\text{take normalized log determinant}
&\Rightarrow \text{prime-coordinate additive scalar}.
\end{array}}
\tag{21}
\]

Neither is the missing global Weil-positive pairing.

## 5. Appending an independent archimedean factor still does not couple places

The branch objective requires one structure to produce not only the finite prime coefficients but also the archimedean and polar/global counterterms. A separated tensor completion cannot obtain that by adding one more factor.

Let `H_\infty` carry any independently defined positive Gram matrix `M_\infty` of finite rank, and form

\[
H_{\mathrm{tot}}
=
H_\infty\otimes\bigotimes_{p\in P}H_p
\tag{22}
\]

with the product metric. Then

\[
\boxed{
\delta(M_{\mathrm{tot}})
=
\delta(M_\infty)+\sum_{p\in P}\delta(M_p).
}
\tag{23}
\]

Every finite--archimedean mixed difference still vanishes. The real place can contribute its own positive determinant density, but no counterterm is generated from interaction with the finite places because there is no interaction to begin with.

The same qualitative conclusion holds for an orthogonal direct-sum completion: determinants multiply over blocks, so logarithms add. A nonseparable finite--archimedean metric, boundary condition, differential, or correspondence is therefore not a cosmetic refinement; it is exactly the new mathematical datum required to evade (23).

## 6. Matched controls show that raw rank weighting is not arithmetic coupling

The only apparent interaction left in the unnormalized formula (8) is the rank weighting. It is not specific to primes. Replace the cyclotomic factors by arbitrary finite-dimensional separable algebras or positive Gram spaces `B_\alpha` with the same ranks and local determinant densities. Their tensor product obeys the identical formulas (8)--(14).

Consequently any mixed finite difference visible in the **raw** quantity

\[
\log|\det G_{\otimes_i B_i}|
\tag{24}
\]

can be reproduced purely by changing factor populations. Dividing by total rank removes it exactly. This is the tensor analogue of the `N\log N` control in `WP-156`: extensive volume can mimic collectivity without a new incidence law.

This control also prevents a nonlinear rescue from being counted automatically. Applying a nonlinear function to the total rank or determinant can manufacture mixed derivatives, but the same function manufactures them in the nonarithmetic matched model. Such a readout would need its own source-forced definition, exact Weil normalization, and independent sign theorem.

## 7. Exact escape boundary: the equations or metric must become entangled before positivity

This finding closes only the **separated** multivariate completion. Several mathematically different constructions remain outside it:

- a multivariate complete intersection whose defining equations themselves couple different prime variables;
- a source-forced correspondence complex with a differential mixing prime coordinates before its determinant line is formed;
- an entangled sublattice, quotient, extension, or boundary condition not isomorphic to the product object with its product trace/Gram geometry;
- an analytic or Quillen-type determinant metric whose anomaly/curvature is produced by genuinely coupled geometry rather than by a product metric;
- a finite--archimedean determinant formed only after a nonseparable real/finite incidence has been introduced.

These are not evasions by notation. Each changes the mathematical object upstream of the Kronecker factorization and can therefore create interaction terms not covered by (14). The decisive audit for any such candidate is now simple: before taking a determinant or invoking positivity, exhibit the exact non-product map, equation, differential, or metric and show that its mixed term survives matched arbitrary-label controls.

Conversely, if the candidate object still decomposes as a tensor product with product trace/Gram metric, equations (6)--(14) kill the route immediately.

## 8. Prior art and novelty audit

No new theorem about tensor products, trace forms, discriminants, or Kronecker determinants is claimed. The factorization (6)--(12) is classical linear algebra once regular trace is used. A directly relevant stronger reference is Jason Gaddis, Ellen Kirkman, and W. Frank Moore, *On the discriminant of twisted tensor products*, Journal of Algebra **477** (2017), 29--55, DOI `10.1016/j.jalgebra.2016.12.019`, arXiv `1606.03105`. Their Theorem 5.1 treats a substantially more general twisted-tensor setting; the proof identifies the trace matrix with a Kronecker-product form and derives the corresponding multiplicative discriminant law. The ordinary untwisted formula used here is the simplest special case.

The cyclotomic specialization uses only the classical discriminant formula already audited in `WP-156`. A targeted literature search found no independent Weil/RH positivity mechanism arising from the separated tensor trace discriminant itself. Nearby Weil-positive literature instead relies on globally assembled trace/compression or cohomological structures, where the coupling is present before the sign theorem.

The durable Mathia-specific result is therefore not a new algebra theorem but an exact boundary on the current escape route:

\[
\boxed{
\text{separated multivariate cyclotomic product}
\;\Longrightarrow\;
G=\bigotimes_p G_p
\;\Longrightarrow\;
\delta(G)=\sum_p\delta(G_p)
\;\Longrightarrow\;
\Delta_p\Delta_q\delta=0\quad(p\ne q).
}
\tag{25}
\]

## Consequence for the research line

The determinant-line frontier should no longer treat “make the construction multivariate” as sufficient. If the prime variables remain independent and the metric/trace is the canonical product one, the determinant density is exactly place-additive and an independent positive product metric supplies only generic mixed bulk.

A viable next construction must therefore identify **where non-product arithmetic incidence is forced before positive completion**. In particular, a genuinely coupled multivariate resultant, correspondence differential, determinant-line anomaly, or finite--archimedean boundary map is now a necessary structural feature rather than an optional embellishment. That is the smallest remaining determinant/cohomological boundary not already reduced to the pairwise resultant, population weighting, or generic product positivity mechanisms.