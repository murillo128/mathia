# PF-033 — no absolute or standard Selberg-style Laplacian determinant exists for the prime flute

**Status:** `DECISIVE-NEGATIVE` for the standard heat-zeta / absolute Laplacian-determinant branch, and for the usual finite-type Selberg heat-trace regularization without an additional prime-specific subtraction.

This note does **not** claim a new theorem in spectral geometry. The point is that several previously established features of the exact prime flute combine to rule out a major remaining candidate: a natural global zeta-regularized determinant obtained from the ordinary Laplacian heat trace, or from the standard identity/cusp-subtracted Selberg heat trace.

## 1. Infinite hyperbolic area already kills the absolute heat trace

The zero-twist prime flute is a chain of countably many hyperbolic pairs of pants. Each pair of pants has one cusp and two geodesic boundary components, hence Euler characteristic `-1` and area

\[
\operatorname{Area}(P)=2\pi
\]

by Gauss-Bonnet. The interiors are disjoint in the pants decomposition, so

\[
\boxed{\operatorname{Area}(X_{\rm prime})=\infty.}
\]

Let `K_X(t;x,y)` be the heat kernel of the non-negative Laplacian on

\[
X_{\rm prime}=\Gamma_{\rm prime}\backslash\mathbb H.
\]

For a hyperbolic quotient,

\[
K_X(t;x,y)
=
\sum_{\gamma\in\Gamma_{\rm prime}}
K_{\mathbb H}(t;\tilde x,\gamma\tilde y).
\]

The hyperbolic-plane heat kernel is strictly positive. On the diagonal, retaining only the identity term gives the uniform lower bound

\[
\boxed{
K_X(t;x,x)\ge K_{\mathbb H}(t;0)>0
\qquad(t>0).
}
\]

Therefore

\[
\operatorname{Tr}(e^{-t\Delta_X})
=
\int_XK_X(t;x,x)\,dA(x)
=\infty
\]

for every `t>0`.

Consequently

\[
\boxed{e^{-t\Delta_X}\text{ is not trace class for any }t>0.}
\]

The same remains true after any constant spectral shift:

\[
\operatorname{Tr}(e^{-t(\Delta_X+\mu)})
=e^{-\mu t}\operatorname{Tr}(e^{-t\Delta_X})=\infty.
\]

Thus the ordinary heat-zeta definition

\[
\zeta_{\Delta}(w)
=\frac1{\Gamma(w)}
\int_0^\infty t^{w-1}
\operatorname{Tr}(e^{-t\Delta})\,dt
\]

never has an initial half-plane of convergence, and the absolute zeta determinant

\[
\det_\zeta(\Delta+\mu)
\]

is not available.

This obstruction is independent of the prime gaps: it follows already from the infinite chain geometry.

## 2. Subtracting the universal volume term is still not enough

For finite-volume or geometrically finite surfaces, one can replace the divergent absolute trace by a Selberg/regularized trace: remove the identity contribution and treat finitely many cusps separately. That does **not** repair the prime flute.

PF-005/PF-007/PF-020 established that the exact cross-ratio geometry produces infinitely many distinct primitive closed geodesics

\[
L_j\longrightarrow0.
\]

The hyperbolic contribution to the standard heat trace has the form

\[
H(t)
= C(t)
\sum_{\gamma\ {m primitive}}
\sum_{k\ge1}
\frac{\ell_\gamma}
{2\sinh(k\ell_\gamma/2)}
\exp\!\left(-\frac{k^2\ell_\gamma^2}{4t}\right),
\]

where `C(t)>0` is the universal heat prefactor (the harmless convention-dependent factor of `2` does not matter here).

For the primitive `k=1` terms of the short-orbit sequence,

\[
\frac{L_j}{2\sinh(L_j/2)}
\exp\!\left(-\frac{L_j^2}{4t}\right)
\longrightarrow 1
\qquad(j\to\infty)
\]

for every fixed `t>0`.

All summands are non-negative. Hence

\[
\boxed{H(t)=+\infty\qquad\text{for every }t>0.}
\]

So even after formally removing the infinite identity/area term, the ordinary hyperbolic orbital part of the Selberg heat trace diverges at **every positive time**.

This strengthens the local-finiteness obstruction of PF-020 from compactly supported wave/trace test functions to the heat kernel itself.

## 3. Infinite cusp subtraction also does not provide the missing background

The prime flute has infinitely many cusps. Standard finite-area Selberg heat-trace regularization subtracts/parses a **finite** parabolic contribution. In our surface there is no finite parabolic sector to remove.

More importantly, PF-019 showed that after normalizing each cusp to width `1`, cross-cusp scattering entries stay bounded away from zero along infinitely many prime-cluster channels. In the natural `\ell^2` cusp basis the scattering operator cannot be a compact perturbation of the independent-cusp background; in particular `\Phi(s)-I` is not compact in the naive model.

Therefore the two most obvious relative backgrounds both fail:

\[
\boxed{
\text{hyperbolic plane / volume background}
\quad\text{and}\quad
\text{independent normalized cusps}.
}
\]

The first leaves an infinite short-orbit heat contribution; the second leaves a non-compact cross-cusp coupling.

## 4. Known determinant theories do not cover this geometry

This conclusion is consistent with the hypotheses of the standard literature rather than contradicting it.

- Borthwick-Judge-Perry, *Determinants of Laplacians and isopolar metrics on surfaces of infinite area* (Duke Math. J. 118, 2003), construct determinants for surfaces hyperbolic near infinity in a geometrically finite / convex-cocompact framework and explicitly use **relative** heat operators that are trace class. Their headline infinite-area construction is for surfaces without cusps; it does not cover an infinitely generated surface with infinitely many cusp channels and primitive lengths accumulating at `0`.
- Jorgenson-Lundelius regularized heat traces for degenerating finite-volume hyperbolic surfaces handle a finite collection of degenerating collars/cusps. They do not provide a subtraction for infinitely many primitive lengths accumulating at zero with non-decaying heat weights.
- Recent large-volume determinant-limit results likewise impose short-geodesic control (for example, hypotheses excluding an extensive/uncontrolled contribution of reciprocal very-short lengths). The prime flute lies deliberately outside this regime.

Thus there is no conflict with existing determinant theory: the exact prime geometry violates the trace-class/local-finiteness hypotheses that make those determinants possible.

## 5. Consequence for the RH search

The branch

\[
\boxed{
X_{\rm prime}
\longrightarrow
\operatorname{Tr}(e^{-t\Delta})
\longrightarrow
\zeta_\Delta(w)
\longrightarrow
\det_\zeta\Delta
}
\]

is closed.

So is the minimally regularized variant in which one only subtracts the universal area and ordinary cusp terms.

Any determinant-like object that survives must be genuinely **relative/renormalized with respect to a new non-compact background which already contains the infinite family of short multi-gap channels and their cross-cusp coupling**. Choosing such a background arbitrarily would merely manufacture a zeta. To count as a substantive candidate it must be forced by the exact prime-circle/flute geometry itself.

This is compatible with PF-027: the singular factor of any *finite* pinching event can be removed canonically, but here there are infinitely many such events, and PF-020 shows that their aggregate is not locally finite.

## 6. What remains open

This negative does **not** rule out:

1. a relative determinant between two prime-derived surfaces whose heat-kernel difference can be proved trace class;
2. a new renormalized trace obtained from a canonical prime-derived background rather than the hyperbolic plane or independent cusps;
3. local determinants/scattering determinants of finite tangent surfaces such as the candidate of PF-029, provided their geometric-limit status is first proved;
4. non-trace spectral observables such as spectral shift densities, provided the comparison pair is canonical.

But it rules out treating the global prime flute as though it possessed the ordinary Laplacian determinant of a compact/finite-type hyperbolic surface.
