# PF-038 — the intrinsic untwisted reflection does not provide a canonical relative determinant

**Status:** `DECISIVE-NEGATIVE` for the most natural symmetry-based attempt to renormalize the prime-flute spectrum.

## 1. Motivation

PF-017 showed that the visually natural inversion in the original unit circle is an **ambient** interior/exterior duality, not an intrinsic self-map of the prime-flute. There is, however, a different involution which *is* intrinsic to every untwisted/zero-twist flute: the standard reflection

\[
r(e^{i\theta},t)=(e^{-i\theta},t).
\]

This is the involution used in the classical definition of an untwisted flute (Haas). The prime-flute is zero-twist, so its Laplacian commutes with this reflection. It is therefore tempting to use the canonical decomposition

\[
L^2(X)=L^2_+(X)\oplus L^2_-(X)
\]

and hope that the spectral difference between the even and odd sectors cancels the infinite-volume and short-orbit backgrounds that killed the absolute heat trace, Selberg zeta, and determinant in PF-020/PF-033/PF-035/PF-036.

Equivalently, cutting along the fixed set of \(r\) gives a half-flute: even functions correspond to Neumann boundary conditions and odd functions to Dirichlet boundary conditions. On compact bordered hyperbolic surfaces this is a standard and useful construction; Selberg trace formulas and determinant identities for the Dirichlet/Neumann problems are known.

For the prime-flute, however, the cusp geometry gives a local obstruction before any global short-orbit issue is reached.

## 2. Exact cusp model under the reflection

Every cusp of the untwisted flute is fixed by \(r\). Normalize one cusp to

\[
C_Y=\{(x,y):y>Y\}/(x\sim x+1),
\qquad
 ds^2=\frac{dx^2+dy^2}{y^2}.
\]

After a harmless translation of \(x\), the reflection is

\[
\boxed{r(x,y)=(-x,y).}
\]

The half-cusp is

\[
C_Y^+=\{0<x<1/2,\ y>Y\}.
\]

The even sector of the full cusp is exactly the Neumann problem on the two geodesic sides \(x=0,1/2\); the odd sector is exactly the Dirichlet problem.

With \(t=\log y\), Fourier decomposition in \(x\) and the standard unitary conjugation give the one-dimensional radial operators

\[
\boxed{
H_m=-\frac{d^2}{dt^2}+\frac14+(2\pi m)^2e^{2t}.
}
\]

For the Neumann half-cusp,

\[
m=0,1,2,\ldots,
\]

whereas for the Dirichlet half-cusp,

\[
m=1,2,\ldots.
\]

(The sine/cosine normalizations differ but the positive transverse eigenvalues agree.)

Thus the two parity sectors differ by the **entire zeroth cusp channel**

\[
\boxed{
H_0=-\frac{d^2}{dt^2}+\frac14
}
\]

on a half-line.

This is precisely the standard cusp channel responsible for continuous spectrum \([1/4,\infty)\).

## 3. The Neumann/Dirichlet difference is not a trace-class renormalization

For \(m\ge1\), the potential

\[
(2\pi m)^2e^{2t}\to\infty
\]

confines the radial mode in the cusp. The zero mode has no such potential and is a free half-line Schrödinger channel shifted by \(1/4\).

Consequently a single reflected cusp already prevents the parity difference from being a trace-class spectral subtraction in the sense needed for a relative heat determinant: the Neumann side has a complete noncompact channel which is absent on the Dirichlet side.

The prime-flute has infinitely many pairwise disjoint reflected cusps. This makes the failure stronger. Choose a normalized packet \(f\) supported sufficiently deep in the standard half-cusp and constant in the transverse direction. Replicate it in distinct cusps to obtain an orthonormal sequence \(f_j\). On the Neumann side these packets propagate through the \(H_0\) channel with a norm bounded below for every fixed heat time \(\tau>0\). On the Dirichlet side there is no transverse zero mode; deep in the cusp every mode sees the exponentially large potential \((2\pi m)^2e^{2t}\). Taking the packet sufficiently deep gives

\[
\left\|
\left(e^{-\tau\Delta_N}-e^{-\tau\Delta_D}\right)f_j
\right\|\ge c_\tau>0
\]

uniformly in \(j\).

Hence

\[
\boxed{
e^{-\tau\Delta_N}-e^{-\tau\Delta_D}
\text{ is not compact, hence not trace class.}
}
\]

Equivalently, the equivariant heat operator

\[
r\,e^{-\tau\Delta_X}
\]

cannot have a finite ordinary trace obtained by subtracting the odd sector from the even sector.

Therefore the most canonical parity-relative zeta/determinant candidate,

\[
\frac{\det(\Delta_+ -\lambda)}{\det(\Delta_- -\lambda)}
\quad\text{or}\quad
\det_{\rm rel}(\Delta_N,\Delta_D),
\]

does **not** exist by the standard trace-class relative construction.

## 4. Why this is independent of the short-orbit obstruction

This failure occurs in the universal local geometry of a cusp and does not use the primitive closed geodesics with lengths tending to zero.

Thus even if one somehow removed the entire PF-020/PF-035/PF-036 short-orbit sector, the intrinsic reflection would still not provide a canonical finite determinant: its even and odd sectors have inequivalent asymptotic cusp channels.

This is important because symmetry looked like the only non-arbitrary way to obtain a background from the prime-flute itself. The local Fourier decomposition shows that it does not cancel the universal continuum; it leaves an unmatched zero mode in every cusp.

## 5. Relation to the original interior/exterior duality

Do not identify this reflection with the ambient inversion of PF-017.

- The original circle inversion exchanges the interior disk with a separate exterior copy and is **not** an operator on \(L^2(X_{\rm prime})\).
- The untwisted-flute reflection \(r\) is a genuine intrinsic isometry of the zero-twist prime-flute and does act on \(L^2(X_{\rm prime})\).

PF-038 says that even this stronger intrinsic symmetry does not yield the desired relative determinant.

The exact orthogonal-circle geometry and the ambient inside/outside reciprocity remain valid; they simply cannot be used to reinterpret the failed parity subtraction as an intrinsic two-channel cancellation.

## 6. Literature / novelty check

Known ingredients:

- Haas' classical theory of untwisted flutes defines exactly the reflection involution used above and describes its geodesic fixed set.
- Fourier decomposition of a hyperbolic cusp is standard; the zeroth Fourier mode is the source of the \([1/4,\infty)\) continuous spectrum.
- Even/Neumann and odd/Dirichlet decompositions under reflection are standard. They are used, for example, in the spectral theory of hyperbolic triangles and cusp forms.
- Bolte--Steiner derive Selberg trace formulas for compact bordered hyperbolic surfaces with Dirichlet and Neumann boundary conditions.
- Guillarmou--Guillopé relate Dirichlet-to-Neumann determinants and Selberg/Ruelle zeta functions for compact surfaces with boundary / geometrically finite uniformizations.

Those results do not provide a relative determinant for an infinite-type half-flute with infinitely many reflected cusps. The obstruction above is local and elementary once the cusp parity decomposition is written down, so no novelty is claimed for the analytic mechanism itself. Its value is as a decisive negative result for the prime-flute program.

## 7. Research consequence

This rules out the branch

\[
\boxed{
\text{zero-twist reflection}
\to
\text{even/odd cancellation}
\to
\text{canonical relative heat trace}
\to
\text{relative zeta/determinant}.
}
\]

A surviving relative construction would have to remove the zeroth cusp channels **before** comparing parity sectors (for example through a canonical cusp-form or pseudo-Laplacian projection) and would then still have to deal with the infinite short-orbit accumulation. Unless that projection is forced by the original geometry rather than chosen for analytic convenience, it should not be counted as a new prime-specific zeta.
