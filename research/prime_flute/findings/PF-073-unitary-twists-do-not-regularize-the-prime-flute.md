# PF-073 — unitary twists do not regularize the prime-flute

**Status:** `DECISIVE-NEGATIVE` for unitary-character / flat-line-bundle attempts to rescue a global determinant, twisted Selberg/Ruelle zeta, or compact-resolvent spectral theory.

## 1. Motivation

A natural escape from the obstructions found in PF-035/PF-039/PF-070 is to twist the Laplacian or the dynamical zeta by a unitary character

\[
\chi:\Gamma_{\rm prime}\to U(1).
\]

For finite-type hyperbolic surfaces this can substantially change the cusp spectrum: nontrivial cusp holonomy removes the transverse zero mode, and twisted Selberg/Ruelle zeta functions are standard spectral objects. One might therefore hope that a geometrically natural unitary twist could simultaneously

1. remove the infinitely many cusp zero modes, and
2. regularize the infinitely many short primitive closed geodesics.

Neither can happen on the prime-flute.

## 2. Spectral obstruction: infinitely many cusps defeat every unitary line-bundle twist

Let \(L_\chi\) be the flat Hermitian line bundle associated with \(\chi\), and let \(\Delta_\chi\) be its nonnegative Bochner/Laplace operator.

Choose a fixed Margulis cusp neighborhood in every cusp. These neighborhoods are pairwise disjoint and mutually isometric. After a standard normalization each is

\[
C_j=\{y>Y_0\}/(x\sim x+1),
\qquad
 ds^2=\frac{dx^2+dy^2}{y^2},
\]

with the same \(Y_0>0\).

Write the holonomy of \(L_\chi\) around cusp \(j\) as

\[
\chi(P_j)=e^{2\pi i\alpha_j},
\qquad
\alpha_j\in\mathbb R/\mathbb Z.
\]

Choose a representative and an integer \(m_j\) so that

\[
\xi_j:=m_j+\alpha_j,
\qquad
|\xi_j|\le\frac12.
\]

Fix one nonzero cutoff

\[
\eta\in C_c^\infty((Y_0,2Y_0))
\]

and define on cusp \(j\)

\[
f_j(x,y)=A_j\,\eta(y)e^{2\pi i\xi_jx},
\]

where \(A_j\) normalizes \(\|f_j\|_2=1\). This satisfies the required quasi-periodicity

\[
f_j(x+1,y)=e^{2\pi i\alpha_j}f_j(x,y).
\]

Because two-dimensional Dirichlet energy is conformally invariant,

\[
q_\chi(f_j)
=
\int_{C_j}
\left(|\partial_x f_j|^2+|\partial_y f_j|^2\right)dx\,dy.
\]

The bound \(|\xi_j|\le1/2\), together with the fixed compact \(y\)-support, gives a constant \(E<\infty\), independent of \(j\) and of the character, such that

\[
\boxed{q_\chi(f_j)\le E.}
\]

The supports lie in pairwise disjoint cusps, hence \((f_j)\) is orthonormal. More generally every vector in their finite span has Rayleigh quotient bounded by \(E\) up to the same fixed constant.

Therefore for every \(M>E\),

\[
\boxed{\operatorname{rank}\mathbf 1_{[0,M]}(\Delta_\chi)=\infty.}
\]

Consequently

\[
\boxed{(\Delta_\chi+1)^{-1}\text{ is not compact}}
\]

and, for every \(t>0\),

\[
\boxed{\operatorname{Tr}(e^{-t\Delta_\chi})=\infty.}
\]

Thus no unitary flat line-bundle twist converts the prime-flute into a compact-resolvent problem or produces an ordinary spectral zeta / zeta-regularized determinant.

### Why this is stronger than the finite-cusp situation

For a finite-area surface with finitely many cusps, a nontrivial Aharonov--Bohm/flat holonomy around each cusp can remove the continuous cusp channel and may make the magnetic/twisted spectrum discrete. This is a known phenomenon in the spectral theory of magnetic Laplacians on finite-volume hyperbolic surfaces.

The prime-flute fails for a different reason: even if **every individual cusp is spectrally confining**, there are infinitely many mutually disjoint copies. The compactness of \(U(1)\) gives a uniform bounded-energy transverse mode in each copy, and infinite multiplicity survives.

## 3. Dynamical obstruction: no scalar unitary twist rescues the Ruelle Euler product

Let

\[
\gamma_j
\]

be the primitive simple closed geodesics supplied by the prime geometry with

\[
L_j:=\ell(\gamma_j)\to0.
\]

For a unitary character \(\chi\), the twisted Ruelle local factor is

\[
F_j(s)=1-\chi(\gamma_j)e^{-sL_j}.
\]

Since \(U(1)\) is compact, there is a subsequence with

\[
\chi(\gamma_{j_k})\to\xi,
\qquad |\xi|=1.
\]

For every fixed \(s\in\mathbb C\),

\[
F_{j_k}(s)\to1-\xi.
\]

But an infinite product can converge to a nonzero value only if its factors tend to \(1\). Here

\[
1-\xi\neq1
\]

because \(|\xi|=1\) and hence \(\xi\neq0\). Therefore

\[
\boxed{
\prod_{\gamma\,\mathrm{primitive}}
(1-\chi(\gamma)e^{-s\ell(\gamma)})
}
\]

has **no point of ordinary nonzero convergence for any scalar unitary character**. In particular, a spin/sign twist \(\chi\in\{\pm1\}\), a parity-compatible twist, or any other geometrically natural unitary phase cannot fix the short-orbit obstruction.

## 4. Twisted Selberg zeta has no standard half-plane of absolute convergence

The standard unitary-twisted Selberg product contains the factors

\[
\det\!\left(I-\chi(\gamma)e^{-(s+k)\ell(\gamma)}\right),
\qquad k\ge0,
\]

which in the scalar case begin with

\[
1-\chi(\gamma)e^{-s\ell(\gamma)}.
\]

For the short primitive sequence,

\[
|\chi(\gamma_j)e^{-sL_j}|
=e^{-\operatorname{Re}(s)L_j}
\to1.
\]

Hence the basic small parameter required for absolute Euler-product convergence never becomes small, no matter how far to the right \(\operatorname{Re}s\) is taken. Thus

\[
\boxed{
\text{there is no conventional right half-plane of absolute convergence
for the scalar unitary-twisted Selberg product.}
}
\]

This is a direct geometric obstruction, prior to any question of meromorphic continuation.

## 5. Relation to the distinguished cuffs

The obstruction is driven by the **multi-gap** primitive curves whose lengths approach zero, not by the individual distinguished cuffs

\[
\ell_n\sim2\log\frac{4p_n}{g_n},
\]

which themselves diverge. The cuffs remain important because their relative contrasts create the cross-ratios and necks that generate those short primitive curves, but no unitary phase attached to the global group can damp the resulting orbit family: unitary holonomies always have modulus one.

Thus a twist cannot turn the already-discarded local cuff product into a legitimate global zeta.

## 6. Interior/exterior and reflection compatibility

The original interior/exterior involution and the zero-twist reflection can at most conjugate a unitary character to its inverse/complex conjugate. The two obstructions above depend only on

\[
|\chi|=1,
\]

so they are invariant under these dualities. In particular the real twists \(\chi=\pm1\), which are the most natural ones compatible with reflection, are included.

## 7. Novelty / prior-art audit

Known ingredients:

- twisted Selberg and Ruelle zeta functions for finite-type hyperbolic surfaces/orbisurfaces with finite-dimensional unitary representations are classical and remain an active subject;
- recent work of Doll--Pohl (2026) gives a resonance-factorization theory for unitary-twisted Selberg zeta on geometrically finite infinite-area hyperbolic orbisurfaces;
- nontrivial flat/magnetic holonomy can make the magnetic Laplacian on a **finite-volume, finite-cusp** hyperbolic surface discrete (Gol\'enia--Moroianu; Morame--Truc).

Those results do not cover the present infinite-type, infinite-cusp, zero-systole geometry. Directed searches did not locate a theorem formulated for this exact combination.

The functional-analytic and infinite-product arguments above are elementary once the geometry is known, so historical novelty is **not** claimed for the abstract lemmas. The substantive conclusion for the prime-flute program is the closure of a broad and otherwise plausible regularization branch.

## 8. Research consequence

The following route is closed:

\[
\boxed{
\text{prime-flute}
\to
\text{unitary character / flat-line-bundle twist}
\to
\text{compact spectral problem or convergent twisted dynamical zeta}.
}
\]

Any twist that truly damps the short primitive sector would have to be nonunitary, with modulus changing along the problematic geodesics. Unless such a weight is forced independently by the original prime-circle geometry, that would be an externally chosen regularizer and would lose the self-adjoint spectral meaning that made the unitary route attractive.
