# MC-439 — Principal-minor determinants survive the Möbius gate, but fixed-rank kernels collapse to additive feature moments

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-MECHANISM · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-438` rules out the most immediate global-looking statistics built by *adding* fixed-size motifs along the selected-prime chain: their top Boolean/Möbius interaction collapses to boundary-spanning terms. A genuinely nonadditive statistic can escape that specific collapse.

Let

\[
n=p_1\cdots p_r
\]

be squarefree, and let `K_n=(\kappa(p_i,p_j))_{1\le i,j\le r}` be a matrix obtained from a fixed pair kernel `\kappa` on primes. For every subset `T\subseteq[r]`, let `K_n[T]` be the corresponding principal submatrix, with the standard convention `\det K_n[\varnothing]=1`. Define the divisor statistic

\[
A_\kappa\!\left(\prod_{i\in T}p_i\right):=\det K_n[T].
\tag{1}
\]

Then its full Möbius interaction is exactly

\[
\boxed{
(\mu*A_\kappa)(n)
=
\sum_{T\subseteq[r]}(-1)^{r-|T|}\det K_n[T]
=
\det(K_n-I_r).
}
\tag{2}
\]

Thus a principal-minor determinant is an explicit **global nonadditive survivor** of the `MC-437` gate. Unlike the additive chain scores in `MC-438`, its top interaction need not collapse to endpoint motifs or vanish at large `r`.

However, this escape has a second exact obstruction. Suppose the kernel has a fixed separable feature rank `d`, so on every prime set

\[
K_n=U_nV_n^{\mathsf T},
\qquad
U_n,V_n\in\mathbb C^{r\times d},
\tag{3}
\]

with `d` independent of `r`. Sylvester's determinant identity gives

\[
\boxed{
(\mu*A_\kappa)(n)
=(-1)^r
\det\!\left(I_d-V_n^{\mathsf T}U_n\right).
}
\tag{4}
\]

If

\[
\kappa(p,q)=\sum_{a=1}^d f_a(p)g_a(q),
\tag{5}
\]

then the `d\times d` matrix in `(4)` has entries

\[
(V_n^{\mathsf T}U_n)_{ab}
=
\sum_{i=1}^r g_a(p_i)f_b(p_i).
\tag{6}
\]

So the apparently full-order interaction factors through only the fixed family of additive feature moments in `(6)`. In the Gram case `\kappa(p,q)=\langle\phi(p),\phi(q)\rangle` with `\phi(p)\in\mathbb C^d`, the survivor is

\[
(\mu*A_\kappa)(n)
=(-1)^r
\det\!\left(I_d-\sum_{p\mid n}\phi(p)\phi(p)^*\right).
\tag{7}
\]

The key boundary is therefore sharper than “nonzero full interaction”: **a statistic can have a nonzero order-`r` Boolean coefficient while that coefficient still factors through a fixed-dimensional collection of additive prime features.** Nonadditivity alone does not certify transport of the factorial gap-order structure from `MC-436`.

No estimate for `M(x)` follows.

## 1. Exact principal-minor calculation

For any `r\times r` matrix `K`, the characteristic-polynomial/principal-minor expansion is

\[
\det(K+tI_r)
=
\sum_{T\subseteq[r]}
\det K[T]\, t^{r-|T|}.
\tag{8}
\]

Setting `t=-1` gives

\[
\det(K-I_r)
=
\sum_{T\subseteq[r]}(-1)^{r-|T|}\det K[T].
\tag{9}
\]

By `MC-437`, the right-hand side is exactly the Boolean top coefficient of the divisor statistic `(1)`, hence exactly `(\mu*A_\kappa)(n)`. This proves `(2)`.

The empty principal minor is load-bearing only as the standard determinant convention. At `r=1`, `(2)` reads

\[
A_\kappa(p)-A_\kappa(1)=\kappa(p,p)-1,
\]

which agrees with `\det(K-I_1)`. At `r=2`, expansion gives

\[
\det K-\kappa(p_1,p_1)-\kappa(p_2,p_2)+1
=
\det(K-I_2),
\]

providing the first nontrivial check.

Equation `(2)` also makes clear why the result does not contradict the bounded-degree theorem of `MC-437`. Even if a rank-`d` matrix has `\det K[T]=0` whenever `|T|>d`, the *values* of the set function being supported on small subsets does not mean that its Boolean Möbius expansion has degree at most `d`. Inclusion-exclusion of those low-cardinality values can generate a nonzero coefficient on the full set.

## 2. Fixed-rank factorization

From `(3)`,

\[
\det(K_n-I_r)
=(-1)^r\det(I_r-U_nV_n^{\mathsf T}).
\tag{10}
\]

Sylvester's determinant theorem

\[
\det(I_r-UV^{\mathsf T})
=
\det(I_d-V^{\mathsf T}U)
\tag{11}
\]

then proves `(4)`. Under the separable representation `(5)`, choosing row `i` of `U_n` as `(f_1(p_i),\ldots,f_d(p_i))` and row `i` of `V_n` as `(g_1(p_i),\ldots,g_d(p_i))` gives `(6)` directly.

This is an exact factorization, not an entropy estimate. It does **not** by itself prove that the `d^2` complex numbers in `(6)` carry only finitely many bits, nor that they cannot encode the prime set under an artificial choice of features. The justified conclusion is structural: the determinant survivor has no dependence beyond the matrix of additive feature sums. Any claim that this transports a particular relational discriminator must prove that the discriminator is recoverable or analytically useful through those moments.

Rank one makes the collapse transparent. If `K_n=u_nv_n^{\mathsf T}`, then

\[
(\mu*A_\kappa)(n)
=(-1)^r\left(1-v_n^{\mathsf T}u_n\right)
=(-1)^r\left(1-\sum_{i=1}^r v_i u_i\right).
\tag{12}
\]

The full order-`r` Möbius coefficient is nonzero in general, yet it is only a scalar additive aggregate followed by an affine map.

## 3. Consequence for the gap-order frontier

The next object requested by `MC-438` was a genuinely global nonadditive statistic on every selected divisor whose full Boolean interaction can be computed. Principal-minor determinants satisfy that request exactly: `(2)` computes the interaction in closed form and proves that nonadditivity can evade the endpoint cancellation theorem.

But `(4)`--`(6)` show that **finite separable rank is a false escape** if the intended claim is that the determinant itself preserves a genuinely growing-order relation. A fixed-rank pair kernel may look global because `\det K[T]` combines all selected indices nonlinearly, while its Möbius survivor is determined by a fixed-size feature-space matrix.

For the factorial adjacent-gap permutation of `MC-436`, this yields a concrete gate. A determinant route must do at least one of the following before its source capacity can be credited downstream:

1. use a kernel whose effective separable rank grows with the number of prime factors;
2. use features whose fixed moment matrix is independently proved to retain the required order discriminator; or
3. use a genuinely set-dependent kernel for which the principal matrix on a subset is not simply a principal submatrix of one fixed pair-kernel matrix.

Merely replacing an additive gap score by a determinant of a bounded-feature kernel does not establish transport of the gap permutation.

## 4. Classical prior art and novelty boundary

Both algebraic identities used above are classical. The coefficient expansion `(8)` is the standard expression of the characteristic polynomial in terms of principal minors; equivalently, the finite-dimensional Fredholm determinant satisfies `det(I+K)=sum_T det K[T]`. Sylvester's determinant theorem `(11)` is standard matrix analysis.

There is also a direct probabilistic incarnation in determinantal point processes. For a marginal DPP kernel `0\le K\le I`, the inclusion probabilities are

\[
\Pr(T\subseteq Y)=\det K[T].
\]

Inclusion-exclusion then gives the void probability `\Pr(Y=\varnothing)=\det(I-K)`. Thus, up to the factor `(-1)^r`, equation `(2)` is exactly the classical inclusion-to-exact-event Möbius transform of principal-minor marginals. Kulesza and Taskar also develop the standard low-dimensional/dual feature representation for finite-rank determinantal models.

Primary/authoritative prior-art anchors checked for this calculation include:

- Terence Tao, *Topics in Random Matrix Theory*, Graduate Studies in Mathematics 132, American Mathematical Society (2012), ISBN `978-0-8218-7430-1`, for the standard principal-minor/characteristic-polynomial linear algebra;
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press (2013), DOI `10.1017/CBO9781139020411`, for standard determinant and matrix-factorization identities;
- Alex Kulesza and Ben Taskar, *Determinantal Point Processes for Machine Learning*, Foundations and Trends in Machine Learning 5 (2012), 123--286, DOI `10.1561/2200000044`, for principal-minor marginal kernels and finite-rank dual representations.

No novelty is claimed for principal-minor expansions, Sylvester's theorem, DPP inclusion-exclusion, or low-rank determinant reduction. The durable contribution is the **frontier classification** produced by applying those classical mechanisms to `MC-437`--`MC-438`: determinant statistics are an explicit nonadditive survivor of the Möbius top-interaction gate, but bounded feature rank can make that survival algebraically high-order while structurally factoring through fixed additive moments.

## Boundaries and falsification tests

- **Principal-submatrix consistency is load-bearing.** Equation `(2)` assumes that the divisor statistic for every subset is the determinant of the corresponding principal submatrix of one fixed source matrix. A kernel rebuilt after each deletion can have a different top interaction.
- **Fixed separable rank is the obstruction in `(4)`.** A generic pair kernel can have rank growing with `r`; the theorem does not collapse such a kernel to fixed-dimensional moments.
- **Factorization is not a cardinality theorem.** Fixed-dimensional real or complex moments can encode substantial information. Any stronger information-loss conclusion needs regularity, resolution, stability, or matched-control assumptions.
- **Nonzero top interaction is not analytic cancellation.** Equation `(2)` says what survives one divisor-lattice operation; it supplies no bound on averages of that survivor and no improvement for `M(x)`.
- **Positive-semidefinite kernels are not required algebraically.** The DPP interpretation needs positivity/contraction hypotheses, but `(2)` and `(4)` hold for arbitrary finite matrices over a commutative field where the determinants are defined.
- **The empty determinant convention matters.** Replacing `A_\kappa(1)=1` by another normalization changes the top coefficient by the corresponding `(-1)^r` constant term.
- **No zero-free input is used.** The derivation is finite linear algebra and Boolean inclusion-exclusion.

## Consequence for the research line

The first genuinely global nonadditive test after `MC-438` is now classified. Principal-minor determinants prove that the boundary-collapse theorem is not universal: a natural nonadditive set functional can carry a nonzero full Möbius interaction, and that interaction is exactly computable.

At the same time, finite-rank determinant constructions expose a new false-positive mode. “Full interaction” can be present only because inclusion-exclusion packages a fixed collection of lower-dimensional feature moments into an order-`r` coefficient. The next useful determinant/kernel candidate should therefore be tested first for **effective separable rank and feature-moment factorization**. If those stay bounded while `r` grows, the route has not yet shown that the growing gap-order relation survives.