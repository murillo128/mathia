# PC-032 — the anchored inverse-square chord Laplacian has a derivative spectrum at prime levels

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the canonical single-level anchored inverse-square chord-Laplacian route at prime levels. The full regular-polygon `csc^2` spectrum is classical; no novelty is claimed for that spectral identity.

## 1. The operator is an intrinsic nonlocal escape from the regular-linear no-go

PC-021 rules out fixed bounded linear probes of the primitive-shell measure, but deliberately leaves open singular, nonlocal, shell-dependent operators. A particularly canonical such object comes directly from chord geometry.

For the full regular `n`-gon, write

\[
z_a=e^{2\pi i a/n},\qquad a\in\mathbb Z/n\mathbb Z,
\]

and define the inverse-square chord Laplacian

\[
(\mathcal L_n f)_a
=\sum_{b\ne a}
\frac{f_a-f_b}{|z_a-z_b|^2}.
\]

Because

\[
|z_a-z_b|^2
=4\sin^2\!\frac{\pi(a-b)}n,
\]

this is the exact finite-circle `csc^2` kernel

\[
(\mathcal L_n)_{ab}
=
-\frac1{4\sin^2(\pi(a-b)/n)}
\quad(a\ne b),
\]

with the diagonal chosen so each row sums to zero.

This operator is nonlocal, uses all pairwise chord distances, and its kernel is singular in the continuum limit. It therefore lies genuinely outside the bounded fixed-probe theorem of PC-021.

Now ground the common anchored vertex `z_0=1`: impose `f_0=0` and let

\[
G_n:=\mathcal L_n[\{1,\ldots,n-1\},\{1,\ldots,n-1\}]
\]

be the resulting principal block. When `n=p` is prime, every non-anchor vertex is primitive/new, so **`G_p` is exactly the anchored birth-layer Hessian of this nonlocal chord energy**.

## 2. The full polygon spectrum is elementary

The full matrix `\mathcal L_n` is circulant. Its Fourier vectors

\[
e_k(a)=e^{2\pi i ka/n}
\]

have eigenvalues

\[
\lambda_k
=
\sum_{r=1}^{n-1}
\frac{1-\cos(2\pi kr/n)}{4\sin^2(\pi r/n)}.
\]

Using the classical trigonometric identity

\[
\sum_{r=1}^{n-1}
\frac{1-\cos(2\pi kr/n)}{\sin^2(\pi r/n)}
=2k(n-k),
\]

we obtain

\[
\boxed{
\lambda_k=\frac{k(n-k)}2,
\qquad 0\le k<n.
}
\]

Thus

\[
\boxed{
P_n(t):=\det(tI-\mathcal L_n)
=t\prod_{k=1}^{n-1}
\left(t-\frac{k(n-k)}2\right).
}
\]

The `csc^2` matrix and these finite Fourier/trigonometric sums belong to the classical Calogero--Perelomov family; the prime-circle specialization does not create this spectrum.

## 3. Grounding the anchor differentiates the full characteristic polynomial

The key point is that the anchored block does not introduce an independent spectral object.

Jacobi's formula gives

\[
P_n'(t)
=\operatorname{tr}\!\left(\operatorname{adj}(tI-\mathcal L_n)\right),
\]

so `P_n'(t)` is the sum of the `n` principal cofactors of `tI-\mathcal L_n`. Because `\mathcal L_n` is circulant, cyclic symmetry makes all those cofactors identical. Each one is precisely

\[
\det(tI-G_n).
\]

Therefore

\[
\boxed{
\det(tI-G_n)=\frac1n P_n'(t).
}
\]

This identity holds for every `n`; at a prime `p` it becomes an exact statement about the full primitive/new-vertex layer because the only old vertex is the anchor.

For odd prime `p`, the nonzero full eigenvalues occur in pairs

\[
\lambda_k=\lambda_{p-k},
\qquad 1\le k\le\frac{p-1}2.
\]

Hence half of these values remain roots of `P_p'`, while the remaining anchored eigenvalues are simply the other critical points of the explicit polynomial `P_p`. There is no additional arithmetic spectral input hidden in the grounding operation.

## 4. The determinant collapses completely

Setting `t=0` gives the anchored spectral determinant. Since `p-1` is even,

\[
\begin{aligned}
\det G_p
&=\frac1p\prod_{k=1}^{p-1}\lambda_k\\
&=\frac1p
\prod_{k=1}^{p-1}\frac{k(p-k)}2\\
&=\boxed{
\frac{((p-1)!)^2}{p\,2^{p-1}}
}.
\end{aligned}
\]

Thus even the most obvious determinant attached to this singular nonlocal anchored operator is only a factorial expression in the polygon size. Any zeta function manufactured from these determinants would be a transform of this already explicit sequence, not a spectral explanation of Riemann zeros.

## 5. Why this is a substantive negative for prime-circle

This route satisfied several escape conditions left open by earlier no-go results:

- it is **anchored** at the common vertex, unlike PC-019;
- it is **nonlocal**, unlike the finite local jet of PC-020;
- it uses a **singular inverse-square kernel**, so PC-021's bounded-linear theorem does not apply;
- it is an actual matrix/operator on the whole vertex configuration rather than a scalar evaluation;
- at prime level its free coordinates are exactly the new vertices.

Nevertheless, prime-level spectralization still collapses:

\[
\boxed{
\text{prime birth shell}
\to
\text{anchored inverse-square chord Laplacian}
\to
\frac1p\,P_p'(t),
}
\]

where `P_p` already has the elementary regular-polygon spectrum `k(p-k)/2`.

So the prime character of the layer does **not** generate a new spectral law here. It only makes the primitive shell coincide with the complement of one grounded vertex in a highly symmetric circulant operator.

## 6. Prior art and novelty audit

The decisive ingredients are classical or elementary:

- Calogero and Perelomov computed spectra and trigonometric identities for finite matrices with `sin^{-2}((j-k)pi/n)` entries. This is directly on top of the full-polygon kernel used here.
- Fourier diagonalization of circulant matrices is standard.
- `P_n'(t)` as the sum of principal cofactors follows from the derivative-of-determinant/Jacobi identity; equality of the cofactors follows from cyclic symmetry.

No novelty is claimed for those facts. The project-specific consequence is the **scope obstruction**: a canonical singular/nonlocal operator that genuinely escapes PC-021 still becomes spectrally universal exactly at prime levels, because primality turns the birth shell into a one-vertex grounding of the complete regular polygon.

## 7. Boundary of the no-go

This finding does **not** rule out every nonlocal shell-dependent operator.

For composite `n`, the primitive shell is obtained only after removing all older/imprimitive vertices, not merely the common anchor. A principal block grounded on the entire old set can therefore have additional dependence on the reduced-residue pattern. The present derivative identity does not classify that multi-vertex grounding.

It also does not rule out:

- cross-level couplings between grounded operators;
- nonlinear dependence of the kernel itself on the primitive configuration;
- global uniformization/monodromy data of PC-017;
- operators in which prime and composite levels interact before spectralization.

The negative conclusion is narrower but decisive: **the most canonical one-level critical chord-energy operator cannot obtain a new RH mechanism from prime levels themselves.** A surviving operator route must use information beyond single-anchor grounding of the universal regular-polygon `csc^2` kernel.
