# PF-072 — the canonical 3D Fuchsian thickening realizes interior/exterior exactly, but its scattering is only universal functional calculus of the flute Laplacian

**Status:** `DECISIVE-NEGATIVE` for using the ambient interior/exterior duality as a new two-channel spectral mechanism; `EXACT-DERIVED` for the warped-product reduction.

PF-017 correctly showed that the original inversion across the unit circle is ambient rather than an intrinsic involution of the 2D prime-flute. There is, however, one canonical way to turn that ambient duality into a genuine connected hyperbolic object without inventing gluing data: regard the same Fuchsian group as a subgroup of `PSL(2,C)` and form the 3-dimensional quotient.

The resulting construction is natural enough that it must be audited before any further attempt to obtain an RH-like functional equation from the inside/outside pair.

## 1. Canonical Fuchsian thickening

Let

\[
X=\Gamma_{\rm prime}\backslash\mathbb H^2
\]

be the prime-flute. Embed

\[
PSL_2(\mathbb R)\subset PSL_2(\mathbb C)
\]

and let the same group act on \(\mathbb H^3\). The invariant copy of \(\mathbb H^2\) is totally geodesic, and normal exponential coordinates give an exact global warped product

\[
\boxed{
M_{\rm prime}:=\Gamma_{\rm prime}\backslash\mathbb H^3
\cong
\mathbb R_r\times X,
\qquad
g_3=dr^2+\cosh^2 r\,g_X.
}
\]

This formula is standard for Fuchsian 3-manifolds and does not depend on finite generation of the group.

In the ball/spherical-boundary picture, the limit circle is the equator. The two complementary hemispheres are exactly the two components exchanged by the original inversion/reflection. Thus the two ends

\[
r\to+\infty,
\qquad
r\to-\infty
\]

realize the interior/exterior pair as genuine opposite ends of one connected hyperbolic 3-manifold.

Moreover, every Euclidean circle on the sphere at infinity orthogonal to the equator bounds a totally geodesic plane in \(\mathbb H^3\) orthogonal to the central \(\mathbb H^2\). Hence this thickening preserves the exact orthogonal-circle geometry rather than merely doubling the abstract quotient.

## 2. Exact separation of the 3D Laplacian

Use the nonnegative Laplacian convention. For

\[
g_3=dr^2+\cosh^2r\,g_X,
\]

we have

\[
\boxed{
\Delta_M
=-\partial_r^2-2\tanh r\,\partial_r
+\operatorname{sech}^2r\,\Delta_X.
}
\]

The volume form is

\[
dV_M=\cosh^2r\,dr\,dA_X.
\]

The unitary map

\[
U:L^2(M,dV_M)\to L^2(\mathbb R,dr)\otimes L^2(X,dA_X),
\qquad
(Uf)(r,x)=\cosh r\,f(r,x),
\]

gives the exact conjugation

\[
\boxed{
U\Delta_MU^{-1}
=
-\partial_r^2+1+\operatorname{sech}^2r\,\Delta_X.
}
\]

Now apply the spectral theorem to \(\Delta_X\). If \(E_X(d\lambda)\) is its spectral resolution, then

\[
\boxed{
U\Delta_MU^{-1}
=
\int_{[0,\infty)}^{\oplus}
H_\lambda\,E_X(d\lambda),
}
\]

where

\[
\boxed{
H_\lambda
=-\frac{d^2}{dr^2}+1+\lambda\operatorname{sech}^2r.
}
\]

Thus the entire 3D problem separates into one-dimensional modified Pöschl–Teller scattering channels parameterized by the spectral values \(\lambda\) of the **original** 2D Laplacian.

No discrete eigenbasis is required; the statement applies equally to continuous and essential spectrum of the infinite-type surface.

## 3. Two-sided scattering is a universal function of `Delta_X`

At 3D energy

\[
E=1+k^2,
\]

the radial equation is

\[
\boxed{
\left[-\frac{d^2}{dr^2}
+\lambda\operatorname{sech}^2r\right]w
=k^2w.
}
\]

For every fixed \((k,\lambda)\), this is the standard exactly solvable Pöschl–Teller barrier. Let

\[
R(k;\lambda),\qquad T(k;\lambda)
\]

be its scalar reflection and transmission coefficients. Their explicit expressions in Gamma/Legendre functions are universal special-function data.

Consequently, whenever the two-ended scattering operator is defined in the appropriate spectral representation, it has the form

\[
\boxed{
S_M(k)
=
\begin{pmatrix}
R(k;\Delta_X)&T(k;\Delta_X)\\
T(k;\Delta_X)&R(k;\Delta_X)
\end{pmatrix}.
}
\]

In particular,

\[
[S_M(k),\Delta_X]=0
\]

on each boundary copy, and the full two-sided scattering family contains **no independent geometric variable beyond the spectral measure of \(\Delta_X\)**.

Every prime-gap effect already found in the 2D surface — for example a tangent-induced value

\[
\lambda_H\in\sigma_{\rm ess}(\Delta_X)\cap(0,1/4)
\]

or a local spectral ladder determined by cuff contrasts — is merely sent through the same universal scalar Pöschl–Teller response

\[
\lambda_H\mapsto
\bigl(R(k;\lambda_H),T(k;\lambda_H)\bigr).
\]

The 3D thickening does not create an additional arithmetic invariant.

## 4. The apparent functional-equation symmetry is dimensionally universal

For an asymptotically hyperbolic 3-manifold the natural spectral parameter is

\[
\Delta_M-s(2-s),
\]

and the scattering symmetry is centered on

\[
\boxed{\Re s=1.}
\]

This is the standard \(s\leftrightarrow2-s\) symmetry forced by boundary dimension \(2\). It is not a prime-specific realization of the Riemann critical line.

Thus the visually compelling chain

\[
\text{interior/exterior}
\to
\text{two 3D scattering channels}
\to
\text{functional equation}
\to
\text{RH mechanism}
\]

fails at the final step: the functional equation is universal Poincare–Einstein scattering symmetry, and after exact separation the scattering operator is only a fixed functional calculus of \(\Delta_X\).

## 5. What this does and does not rule out

This **does** close the most canonical deliberate doubling left open by PF-017:

\[
\boxed{
\text{prime-flute}
\to
\Gamma\backslash\mathbb H^3
\to
\text{inside/outside transmission spectrum}
\to
\text{new prime-gap spectral invariant}
}
\]

as a source of genuinely new information.

It does **not** invalidate the 2D results where relative cuff/gap data genuinely change \(\Delta_X\), its tangent spectra, local spectral measures, or finite-tangent scattering. Those remain the input spectral data seen by the 3D scattering.

It also does not rule out a non-Fuchsian deformation of the 3D group. But a quasi-Fuchsian/bent construction would require additional deformation data not present in the original prime-circle geometry, so it cannot be used as a canonical RH mechanism unless such data are independently forced.

## 6. Novelty / literature audit

The ingredients are standard:

- For a Fuchsian group acting on \(\mathbb H^3\), the quotient is the warped product \(dr^2+\cosh^2r\,g_X\). This exact formula appears throughout the Fuchsian 3-manifold literature; for example Datchev–Dyatlov use \(\Gamma\backslash\mathbb H^3\cong\mathbb R\times\Gamma\backslash\mathbb H^2\) with this metric, and standard Fuchsian-manifold notes describe the two boundary components explicitly.
- Scattering and resolvent theory for hyperbolic / asymptotically hyperbolic manifolds is classical; Guillarmou–Mazzeo prove meromorphic continuation in the geometrically finite setting.
- Warped-product Laplacians and their one-dimensional scattering reductions are standard, and the \(\operatorname{sech}^2\) equation is the classical Pöschl–Teller problem.

Literature anchors:

- K. Datchev and S. Dyatlov, Fuchsian example with `R x (Gamma\H^2)` and metric `dr^2+cosh^2(r)dS`: https://math.mit.edu/~dyatlov/files/2012/fwl.pdf
- S. Moroianu, notes on Fuchsian 3-manifolds and the same warped product / two-boundary compactification: https://www.imar.ro/~purice/Inst/2013/Moroianu-hab.pdf
- C. Guillarmou and R. Mazzeo, *Resolvent of the Laplacian on geometrically finite hyperbolic manifolds*: https://arxiv.org/abs/1002.2165
- General warped-product scattering literature includes Hunsicker–Roidos–Strohmaier, *Scattering theory of the p-form Laplacian on manifolds with generalized cusps*: https://arxiv.org/abs/1106.3032

No novelty is claimed for the reduction itself. Its value is a **decisive program-level negative**: the most geometrically faithful way to promote the exact inside/outside duality into a connected scattering system is spectrally redundant with the 2D prime-flute Laplacian.
