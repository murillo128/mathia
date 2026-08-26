# PF-039 — infinitely many canonical cusp collars kill the pseudo-Laplacian determinant

**Status:** `DECISIVE-NEGATIVE` for the natural zero-cusp-mode / pseudo-Laplacian route to a discrete determinant.

## Motivation

PF-038 left one apparently legitimate escape hatch.  For a finite-area surface with finitely many cusps, the classical Colin-de-Verdiere pseudo-Laplacian removes the zero Fourier coefficient in each cusp above a fixed height.  This is not an ad hoc trick: it is a standard way to replace the continuous cusp spectrum by a self-adjoint operator with compact resolvent.  One could therefore ask whether the prime flute admits a canonical "cuspidal" or pseudo-Laplacian determinant after removing all zeroth cusp modes.

For the prime flute the answer is no, for a reason independent of the short-geodesic accumulation.

## 1. Uniform cusp collars exist in every cusp

The cusp collar theorem gives, around every cusp of any complete hyperbolic surface, a standard embedded neighborhood isometric to

\[
C=\{y>1\}/(x\sim x+2),
\qquad
 ds^2=\frac{dx^2+dy^2}{y^2}.
\]

The boundary horocycle has length 2, and the standard collars of distinct cusps are pairwise disjoint.  The prime flute has infinitely many cusps, so it contains infinitely many pairwise disjoint isometric copies \(C_j\) of this same standard collar.

This uniformity is important: no cusp-dependent rescaling or choice of a shrinking neighborhood is needed.

## 2. Canonical zero-mode removal

Let \(f_{j,0}(y)\) denote the zeroth Fourier coefficient of \(f\) in the standard coordinates of the \(j\)-th cusp,

\[
f_{j,0}(y)=\frac12\int_0^2 f_j(x,y)\,dx.
\]

Define the closed form domain

\[
\mathcal H^1_0
=
\left\{
 f\in H^1(X_{\rm prime}):
 f_{j,0}(y)=0
 \text{ for a.e. }y>1\text{ and every cusp }j
\right\}.
\]

Let \(\Delta_{\rm ps}\) be the nonnegative self-adjoint operator obtained from the Dirichlet form

\[
q(f)=\int_X |\nabla f|^2\,dA
\]

restricted to \(\mathcal H^1_0\) by the Friedrichs construction.  This is the direct infinite-cusp analogue of the standard pseudo-Laplacian / pseudo-cuspform construction.

## 3. Infinite replication of a nonzero Fourier bump

Choose a nonzero \(\eta\in C_c^\infty((1,2))\) and on the model cusp put

\[
\phi(x,y)=A\,\eta(y)\sin(\pi x),
\]

with \(A\) chosen so that \(\|\phi\|_{L^2(C)}=1\).

The zeroth Fourier coefficient of \(\phi\) is identically zero.  Its support is compactly contained in the standard cusp collar, so it defines an admissible smooth vector for the pseudo-Laplacian form.

Copy \(\phi\) to the \(j\)-th cusp and call the resulting function \(\phi_j\).  Because the standard cusp collars are pairwise disjoint,

\[
\langle\phi_i,\phi_j\rangle=0\qquad(i\ne j).
\]

Moreover all copies have exactly the same Dirichlet energy.  In cusp coordinates

\[
|\nabla f|_g^2\,dA_g
=
\bigl(|\partial_x f|^2+|\partial_y f|^2\bigr)\,dx\,dy,
\]

so for some finite constant \(E>0\),

\[
q(\phi_j)=E
\qquad\text{for every }j.
\]

Therefore every finite linear combination satisfies

\[
\boxed{
q\!\left(\sum_j c_j\phi_j\right)
=
E\left\|\sum_j c_j\phi_j\right\|^2.
}
\]

Thus the form domain contains an infinite-dimensional subspace on which the Rayleigh quotient is uniformly equal to \(E\).

## 4. Consequence: no compact resolvent, and the heat trace is infinite

Fix any \(M>E\).  If the spectral projection

\[
\mathbf 1_{[0,M]}(\Delta_{\rm ps})
\]

had finite rank, then the infinite-dimensional span of the \(\phi_j\) would contain a nonzero vector orthogonal to that spectral subspace.  By the spectral theorem such a vector would have Rayleigh quotient at least \(M\), contradicting the exact value \(E\).

Hence

\[
\boxed{
\operatorname{rank}\mathbf 1_{[0,M]}(\Delta_{\rm ps})=\infty
\qquad\forall M>E.
}
\]

In particular,

\[
\boxed{
(\Delta_{\rm ps}+1)^{-1}
\text{ is not compact}.
}
\]

More strongly, for every \(t>0\),

\[
\operatorname{Tr}(e^{-t\Delta_{\rm ps}})
\ge
 e^{-tM}\,
 \operatorname{rank}\mathbf 1_{[0,M]}(\Delta_{\rm ps})
=\infty.
\]

So

\[
\boxed{
 e^{-t\Delta_{\rm ps}}
 \text{ is not trace class for any }t>0.
}
\]

There is therefore no ordinary spectral zeta or zeta-regularized determinant attached to this canonical zero-mode-removed pseudo-Laplacian.

## 5. Why this matters for the prime-flute program

For finite-area surfaces with finitely many cusps, removing the zeroth cusp modes is precisely a classical way to recover compact resolvent and discrete pseudo-spectrum.  The prime flute violates the conclusion for a genuinely new global reason: there are infinitely many mutually disjoint, uniformly sized standard cusp collars, so the nonzero Fourier sector itself replicates infinitely often at bounded energy.

This obstruction is independent of the distinguished cuff lengths

\[
\ell_n\sim 2\log(4p_n/g_n)
\]

and independent of the primitive short-orbit accumulation used in PF-020/PF-035/PF-036.  Even a hypothetical renormalization that perfectly removed all zeroth cusp channels and all short-orbit divergences would still not turn the absolute pseudo-Laplacian into a compact-resolvent operator.

Thus the natural chain

\[
\boxed{
\text{prime flute}
\to
\text{remove every zero cusp mode}
\to
\text{discrete pseudo-Laplacian}
\to
\zeta_{\rm ps}/\det\Delta_{\rm ps}
}
\]

fails at the second arrow.

This does **not** by itself rule out a carefully defined *relative* determinant between two noncompact operators whose repeated nonzero cusp sectors cancel exactly.  In particular it does not fully settle the projected even/odd relative problem left open in PF-038.  It does rule out the more basic and very natural hope that the infinite-cusp pseudo-Laplacian itself provides a canonical discrete spectral replacement for the ordinary Laplacian.

## Literature / novelty check

- Yves Colin de Verdiere's pseudo-Laplacian construction (1980s) removes the constant Fourier term in cusp tails and yields compact-resolvent operators in the classical finite-area / finitely many cusp setting.
- Modern treatments of pseudo-Laplacians continue to assume finitely many hyperbolic cusps and use their compact resolvent as a basic input.
- The cusp collar theorem supplies pairwise disjoint standard horocyclic neighborhoods of universal size; the noncompactness argument above is then elementary functional analysis.
- Directed searches did not locate a dedicated theorem formulated for infinitely many cusps in exactly this pseudo-Laplacian language.  No historical novelty is claimed for the abstract mechanism; the useful result is the decisive application to this infinite-cusp prime-flute determinant program.

## Research consequence

Any viable determinant attached to the prime flute must be **relative from the outset** and must cancel not only the zeroth cusp modes but also the infinitely replicated nonzero cusp sectors, in addition to handling the short-orbit accumulation.  A subtraction chosen only to force trace class would be artificial; the reference operator would have to be dictated canonically by the exact prime geometry.
