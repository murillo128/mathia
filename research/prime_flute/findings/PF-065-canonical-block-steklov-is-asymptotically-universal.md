# PF-065 — the canonical isolated-block Steklov spectrum is asymptotically universal

**Status:** `DECISIVE-NEGATIVE` for using the ordinary Steklov spectrum of the canonically isolated prime block as a stable gap-sensitive replacement for the arbitrary cutoff in PF-064.

## 1. Canonical finite block

Let \(\Omega_j\subset X_{\rm prime}\) be one of the isolated recurrent prime-pattern blocks from PF-034/PF-064, bounded by its unique outer separating geodesic \(\beta_j\). Write

\[
\varepsilon_j:=\ell(\beta_j)\to0.
\]

The boundary is not chosen by hand: \(\beta_j\) is the unique geodesic representative of the peripheral class enclosing the block, determined by the exact orthogonal-circle/Fuchsian geometry.

The surface \(\Omega_j\) has finite area, finitely many cusps, and one totally geodesic boundary component of length \(\varepsilon_j\). Its Dirichlet-to-Neumann operator

\[
\mathcal D_j f=\partial_\nu \widetilde f,
\qquad
\Delta\widetilde f=0,
\]

is well-defined, positive, self-adjoint and has discrete spectrum

\[
0=\sigma_{0,j}<\sigma_{1,j}\le\sigma_{2,j}\le\cdots\to\infty.
\]

This remains true for finite-volume noncompact hyperbolic surfaces with cusps.

## 2. Exact half-collar geometry

The boundary collar is

\[
C_{\varepsilon}
=\{0\le r\le w(\varepsilon)\}\times\mathbb R/\mathbb Z,
\]

with

\[
ds^2=dr^2+\varepsilon^2\cosh^2r\,d\theta^2,
\qquad
w(\varepsilon)=\operatorname{arsinh}\frac1{\sinh(\varepsilon/2)}.
\]

Introduce the conformal coordinate

\[
x(r)=\frac1\varepsilon\int_0^r\frac{du}{\cosh u}
=\frac1\varepsilon\arctan(\sinh r).
\]

The full half-collar has conformal length

\[
T_\varepsilon
=\frac1\varepsilon
\arctan\frac1{\sinh(\varepsilon/2)}.
\]

Since harmonicity is conformally invariant in dimension two, the mixed Steklov-Neumann and Steklov-Dirichlet problems on the collar are exactly the flat-cylinder problems of length \(T_\varepsilon\), with the physical normal derivative carrying the factor \(1/\varepsilon\).

For Fourier mode \(m\ge1\), their eigenvalues are

\[
\sigma_m^N(C_\varepsilon)
=
\frac{2\pi m}{\varepsilon}
\tanh(2\pi mT_\varepsilon),
\]

\[
\sigma_m^D(C_\varepsilon)
=
\frac{2\pi m}{\varepsilon}
\coth(2\pi mT_\varepsilon).
\]

Dirichlet-Neumann bracketing gives, for the full block with its single boundary component,

\[
\boxed{
\frac{2\pi m}{\varepsilon_j}
\tanh(2\pi mT_{\varepsilon_j})
\le
\sigma_{2m-1,j},\sigma_{2m,j}
\le
\frac{2\pi m}{\varepsilon_j}
\coth(2\pi mT_{\varepsilon_j}).
}
\]

The same collar comparison is standard in the Steklov theory of hyperbolic surfaces with geodesic boundary; Perrin gives these explicit mixed-collar eigenvalues, and Hassannezhad-Metras-Perrin extend the Steklov framework to finite-volume hyperbolic surfaces with cusps.

## 3. Universal asymptotic spectrum

As \(\varepsilon\to0\),

\[
\arctan\frac1{\sinh(\varepsilon/2)}
=
\frac\pi2-\frac\varepsilon2+O(\varepsilon^3),
\]

so

\[
T_\varepsilon
=
\frac\pi{2\varepsilon}-\frac12+O(\varepsilon^2).
\]

Hence, for every fixed \(m\ge1\),

\[
\boxed{
\varepsilon_j\sigma_{2m-1,j}	o2\pi m,
\qquad
\varepsilon_j\sigma_{2m,j}	o2\pi m.
}
\]

More precisely the bracketing width is exponentially small:

\[
\boxed{
\varepsilon_j\sigma_{2m-1,j},
\varepsilon_j\sigma_{2m,j}
=
2\pi m
\left(1+O\!\left(e^{-4\pi mT_{\varepsilon_j}}\right)\right)
}
\]

and therefore

\[
e^{-4\pi mT_{\varepsilon}}
=
\exp\!\left[-\frac{2\pi^2m}{\varepsilon}+O(1)\right].
\]

Thus the entire fixed-index positive Steklov spectrum, after the only natural scaling by the boundary length, tends to the universal spectrum of \(|D|\) on the unit circle:

\[
\boxed{
\{\varepsilon\sigma_k\}_{k\ge1}
\leadsto
\{2\pi,2\pi,4\pi,4\pi,\ldots\}.
}
\]

The internal modulus of the prime pattern can affect the raw Steklov spectrum only inside corrections that are exponentially small in \(1/\varepsilon\).

## 4. Consequence for prime-gap information

For an isolated cluster, the outer geodesic satisfies the exact multi-gap formula from PF-004/PF-034,

\[
\varepsilon
=4\operatorname{arsinh}\sqrt{\chi_{\rm out}},
\qquad
\chi_{\rm out}\to0.
\]

The internal pattern may still have nontrivial gap ratios such as

\[
r=\frac{d_1}{d_2}
\]

which determine the four-punctured tangent modulus and, in the hierarchical regime, its unique systole/resonance data (PF-063/PF-064).

Nevertheless the ordinary canonical Steklov eigenvalues satisfy

\[
\boxed{
\varepsilon\sigma_{2m-1},\varepsilon\sigma_{2m}
=2\pi m+O\!\left(e^{-2\pi^2m/\varepsilon}\right),
}
\]

independently of that internal ratio at every algebraic order in \(\varepsilon\).

Therefore the route

\[
\boxed{
\text{canonical isolated block}
\to
\text{ordinary Steklov spectrum on its shrinking geodesic boundary}
\to
\text{robust prime-gap observable}
}
\]

is closed.

It does not repair PF-064 by simply replacing a chosen spatial cutoff with the Steklov eigenvalues of the canonical block: the increasingly long collar screens the interior too efficiently.

## 5. What survives: exponentially renormalized DtN, not Steklov eigenvalues

This negative result does **not** say that the full Dirichlet-to-Neumann operator contains no interior information. In fact, splitting \(\Omega_j\) into its canonical half-collar and the remaining core gives an exact Schur-complement factorization.

At zero spectral parameter and on the mean-zero boundary subspace, let

\[
D=2\pi|D_\theta|,
\quad
B_T=D\coth(TD),
\quad
C_T=D\operatorname{csch}(TD),
\]

and let \(A_j\) be the DtN operator of the core on the inner edge of the half-collar. Then

\[
\boxed{
\varepsilon_j\mathcal D_j
=
B_{T_j}
-
C_{T_j}(A_j+B_{T_j})^{-1}C_{T_j}.
}
\]

Consequently the interior contribution is suppressed by two factors

\[
C_T\sim2De^{-TD}.
\]

This identifies the only surviving version of the idea: strip the universal collar transfer (or equivalently exponentially renormalize the full operator) before looking for tangent scattering/DtN data. That is a boundary-control/scattering problem, not an ordinary Steklov-spectral one, and it requires a separate novelty audit.

## 6. Literature / novelty check

Known ingredients:

- the hyperbolic collar theorem and the exact warped-product collar;
- mixed Steklov-Neumann / Steklov-Dirichlet bracketing on boundary collars;
- explicit Fourier-mode formulas for the cylinder DtN map;
- discreteness of the Steklov spectrum for finite-volume hyperbolic surfaces with geodesic boundary and cusps;
- general Schur-complement/gluing formulas for DtN maps.

Relevant references include H. Perrin, *Estimates for low Steklov eigenvalues of surfaces with several boundary components* (2024), and A. Hassannezhad, A. Métras, H. Perrin, *Geometric Bounds for Low Steklov Eigenvalues of Finite Volume Hyperbolic Surfaces* (J. Geom. Anal. 35, 2025).

No novelty is claimed for the collar asymptotics themselves. The substantive conclusion for the prime-flute program is that the most canonical boundary-local spectral replacement for PF-064 is asymptotically universal and gap-blind, with all nonlocal prime-pattern information pushed into exponentially small DtN corrections.
