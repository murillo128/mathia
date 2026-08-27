# PF-066 — the full DtN operator can be exactly collar-stripped; PF-065 loses information only after spectral compression

**Status:** `EXACT-DERIVED` + `POSITIVE-STRUCTURAL`; the layer-stripping mechanism is classical, while the prime-flute specialization gives a canonical localization operator. No RH claim.

## 1. Setup

Let \(\Omega_\varepsilon\) be one of the canonically isolated finite blocks from the prime flute, separated from the rest by a simple geodesic

\[
\beta_\varepsilon,
\qquad
\ell(\beta_\varepsilon)=\varepsilon\to0.
\]

Its maximal half-collar has the exact metric

\[
ds^2=dr^2+\varepsilon^2\cosh^2r\,d\theta^2,
\qquad
0\le r\le w(\varepsilon),
\quad \theta\in\mathbb R/\mathbb Z,
\]

where

\[
w(\varepsilon)=\operatorname{arsinh}\frac1{\sinh(\varepsilon/2)}.
\]

Introduce the conformal coordinate

\[
t(r)=\int_0^r\frac{du}{\varepsilon\cosh u}
=\frac1\varepsilon\arctan(\sinh r).
\]

The half-collar is therefore conformal to the flat cylinder \([0,T_\varepsilon]\times S^1\), with

\[
\boxed{
T_\varepsilon
=\frac1\varepsilon
\arctan\frac1{\sinh(\varepsilon/2)}
=\frac\pi{2\varepsilon}-\frac12+O(\varepsilon^2).
}
\]

At the outer geodesic \(r=0\), the conformal factor is exactly \(\varepsilon\). At the inner edge of the maximal collar it is

\[
\rho_\varepsilon
=\varepsilon\cosh w(\varepsilon)
=\boxed{\varepsilon\coth(\varepsilon/2)}
\longrightarrow2.
\]

Thus the inner edge converges to the canonical length-2 horocycle of the cusp created by pinching \(\beta_\varepsilon\).

## 2. Exact two-boundary DtN matrix of the collar

Let

\[
D=2\pi|D_\theta|
\]

on \(L^2(S^1)\). Define the operator functions

\[
B_T=D\coth(TD),
\qquad
C_T=D\operatorname{csch}(TD),
\]

with their continuous values on the constant mode

\[
B_T|_{\ker D}=C_T|_{\ker D}=\frac1T.
\]

For the flat cylinder, the two-boundary harmonic DtN/flux matrix is exactly

\[
\boxed{
\begin{pmatrix}q_0\\q_T\end{pmatrix}
=
\begin{pmatrix}
B_T&-C_T\\
-C_T&B_T
\end{pmatrix}
\begin{pmatrix}f_0\\f_T\end{pmatrix}.
}
\]

Let \(\Lambda_\varepsilon\) denote the physical DtN operator measured on the separating geodesic \(\beta_\varepsilon\), and put

\[
M_\varepsilon:=\varepsilon\Lambda_\varepsilon.
\]

Let \(\Lambda_\varepsilon^{\rm core}\) be the physical DtN operator of the remaining core at the inner collar edge, with normal pointing into the collar, and put

\[
A_\varepsilon:=\rho_\varepsilon\Lambda_\varepsilon^{\rm core}.
\]

These scalings convert physical normal derivatives into the flat-cylinder flux coordinate.

Gluing the collar to the core imposes flux conservation at \(t=T_\varepsilon\). Eliminating the interface value gives the exact Schur complement

\[
\boxed{
M_\varepsilon
=B_T-C_T(A_\varepsilon+B_T)^{-1}C_T.
}
\tag{1}
\]

This is the operator-level formula underlying the asymptotic Steklov universality of PF-065.

## 3. Exact inverse: the collar can be stripped with no limit

Because \(C_T\) is strictly positive and invertible for every finite \(T\) (including its constant-mode value \(1/T\)), equation (1) can be inverted algebraically:

\[
\boxed{
A_\varepsilon
=C_T\,(B_T-M_\varepsilon)^{-1}C_T-B_T.
}
\tag{2}
\]

Equivalently, define the renormalized response

\[
\boxed{
\mathcal R_\varepsilon
:=C_T^{-1}(B_T-M_\varepsilon)C_T^{-1}.
}
\]

Then

\[
\boxed{
\mathcal R_\varepsilon=(A_\varepsilon+B_T)^{-1}.
}
\tag{3}
\]

Thus the **full** DtN operator on the canonical outer geodesic determines the full core DtN operator exactly. There is no information-theoretic loss through the long collar.

The constant mode causes no exception: the definitions \(B_T(0)=C_T(0)=1/T\) make (1)--(3) valid by continuity. In the zero-frequency finite-area problem the global constant harmonic function gives the expected zero DtN mode.

## 4. Why PF-065 nevertheless found a universal Steklov spectrum

For a nonzero Fourier mode \(m\), write \(d_m=2\pi|m|\). As \(T\to\infty\),

\[
B_T(m)=d_m+O(e^{-2Td_m}),
\qquad
C_T(m)=2d_m e^{-Td_m}(1+o(1)).
\]

Hence

\[
B_T-M_\varepsilon
=C_T(A_\varepsilon+B_T)^{-1}C_T
=O(e^{-2Td_m}).
\]

The prime-sensitive core response is therefore hidden in an **exponentially small operator correction** to a universal diagonal collar response. Taking only eigenvalues before undoing this known transfer discards almost all of that correction, explaining PF-065.

But the attenuation is exactly reversible at the operator level:

\[
C_T^{-1}(B_T-M_\varepsilon)C_T^{-1}
=(A_\varepsilon+B_T)^{-1}.
\]

So the correct conclusion is

\[
\boxed{
\text{raw Steklov spectrum is asymptotically universal, but the full DtN operator is not information-blind.}
}
\]

## 5. Tangent limit

For a recurring isolated prime pattern \(H\), the exterior separating geodesic satisfies \(\varepsilon_j\to0\) and its collar width diverges. The geometry beyond the inner edge of the maximal half-collar converges to the corresponding tangent \(Y_H\) truncated at the cusp produced by the pinching.

The inner boundary length satisfies

\[
\rho_{\varepsilon_j}=\varepsilon_j\coth(\varepsilon_j/2)\to2,
\]

so this truncation is not arbitrary: it is the length-2 horocycle selected by the exact collar geometry.

Standard elliptic continuity on smoothly convergent compact collars/cores therefore gives, in the natural boundary identification,

\[
A_{\varepsilon_j}\longrightarrow A_H,
\]

where \(A_H\) is the flux-normalized DtN operator of the tangent core truncated at that canonical horocycle. Consequently

\[
\boxed{
C_{T_j}^{-1}(B_{T_j}-\varepsilon_j\Lambda_{\varepsilon_j})C_{T_j}^{-1}
\longrightarrow
(A_H+D)^{-1}
}
\]

on each fixed nonzero Fourier sector (and with the obvious \(1/T_j\) treatment of the constant sector).

This gives a **canonical spatial localization** of the tangent response using only the separating geodesic and its exact hyperbolic collar; no arbitrary cutoff function is needed.

## 6. Relation to the prime gaps / distinguished cuffs

The tangent \(Y_H\) is determined by the multi-gap geometry of the recurring prime pattern. For the first nontrivial four-punctured tangent,

\[
r=\frac{d_1}{d_2}
=\sinh^2\frac{L_r}{4},
\]

while the original distinguished cuffs satisfy

\[
\frac{d_1}{d_2}
=\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_1(P)-\ell_2(P)}2\right].
\]

PF-064 already showed that the tangent's unique systole recovers \(r\) in the hierarchical regime. PF-066 shows that the boundary response of that tangent can be obtained canonically from the **full** outer DtN operator of the actual isolated block, after stripping a completely known universal collar.

A stronger inverse statement from a single zero-energy DtN operator should be phrased cautiously because two-dimensional DtN data are conformal and punctures require care. If desired, the same Schur-complement/layer-stripping construction can be performed for the spectral-parameter-dependent DtN family; that family is the natural route to full boundary spectral/scattering reconstruction of the tangent.

## 7. Novelty check

The general mechanism is **not new**:

- Dirichlet-to-Neumann gluing by Schur complements is standard (Poincare--Steklov / BFK-type gluing).
- Layer stripping / invariant embedding of known boundary layers is classical in inverse problems.
- In dimension two, inverse DtN results recovering a bordered Riemann surface up to conformal equivalence are classical (Lassas--Uhlmann and later constructive/stability work).
- The Steklov/DtN problem on finite-volume hyperbolic surfaces with geodesic boundary is already established.

Directed searches did not find the specific prime-flute application in which the **maximal hyperbolic collar itself provides the exact de-embedding operator and a canonical length-2 tangent truncation**. The potentially new content is therefore narrow: not a new layer-stripping theorem, but the fact that the prime-derived pinching geometry supplies all of the renormalization data intrinsically and converts an apparently universal Steklov limit into a recoverable tangent response.

## 8. Research consequence

PF-065 should not be interpreted as saying that canonical boundary response loses the prime-gap information. It says only that **spectral compression to Steklov eigenvalues before de-embedding loses it exponentially**.

The surviving branch is now precise:

\[
\boxed{
\text{isolated prime block}
\to
\text{full DtN operator on its canonical separating geodesic}
\to
\text{exact collar stripping}
\to
\text{tangent boundary response}.
}
\]

The next serious gate is to carry (2) through the spectral parameter and identify, without extra choices, which poles/residues or boundary spectral data of the stripped operator recover the tangent's systole / weighted-gap path. That would connect the canonical boundary observable directly to PF-063/PF-051 rather than merely to the zero-frequency conformal response.
