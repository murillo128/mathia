# PF-061 — Schulze does not close the full physical-scattering remainder gate

**Status:** `DECISIVE-CORRECTION / PF-053-DOWNGRADED`.

PF-053 promoted the polar-part scaling candidate of PF-052 to the stronger statement

\[
\frac{\varepsilon}{\pi}\,
\Phi_\varepsilon^{\rm mark}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
(G_a-zI)^{-1}
\]

for the **full physical marked scattering block** of a fixed-shape pinching family.  The only extra step was the assertion that, after subtracting the cluster of residual poles converging to \(s=1\), the remaining holomorphic part is uniformly \(O(1)\) in a fixed neighbourhood of \(s=1\).  The cited degeneration theory of Schulze does not establish that assertion.  The full-entry statement must therefore be downgraded to an open analytic gate.

## 1. What remains valid from PF-052/PF-053

Let

\[
L_i(\varepsilon)=\varepsilon a_i+o(\varepsilon),\qquad a_i>0,
\]

and let \(G_a\) be Burger's weighted dual-path Laplacian.  Assume the standard small-eigenvalue asymptotics

\[
1-s_{j,\varepsilon}
=\frac{\varepsilon}{2\pi^2}\mu_j+o(\varepsilon)
\]

and the residue-projector limit

\[
2\pi R_{j,\varepsilon}\longrightarrow v_jv_j^*.
\]

Then the finite polar cluster

\[
\Phi_{\varepsilon}^{\rm pol}(s)
:=
\sum_{j=0}^{N-1}
\frac{R_{j,\varepsilon}}{s-s_{j,\varepsilon}}
\]

satisfies, purely algebraically,

\[
\boxed{
\frac{\varepsilon}{\pi}
\Phi_{\varepsilon}^{\rm pol}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
(G_a-zI)^{-1}.
}
\]

Thus the **polar-part scaling law** of PF-052 remains the correct candidate, subject to the residue-projector convergence already stated there.  The correction concerns only the further claim that the same limit automatically holds for the unmodified physical scattering block.

## 2. What Schulze actually controls

Schulze studies degenerating geometrically finite hyperbolic surfaces by meromorphic Fredholm theory.  His central resolvent convergence is away from the essential spectrum / at spectral parameters for which the limiting operator is in the resolvent set.  He then introduces **approximate Eisenstein functions and approximate scattering matrices** adapted to the degeneration.

This distinction is structural.  When geodesics pinch, the limiting object acquires new cusp channels.  The approximate scattering formalism contains additional matrices (usually denoted \(C(\lambda,s)\) and \(D(\lambda,s)\)), and the combinations used for continuation/convergence are renormalized relative to those degeneration channels.  Consequently, continuity of the approximate/renormalized scattering data away from singular spectral parameters cannot simply be read as a uniform bound for the raw physical scattering matrix through a cluster of poles that itself approaches \(s=1\).

In the PF-053 family there are precisely \(N-1\) positive residual eigenvalues tending to zero, hence scattering poles

\[
s_{j,\varepsilon}\to1.
\]

Therefore no fixed neighbourhood of \(s=1\) remains uniformly inside the resolvent set of the degenerating family.  The regime needed by PF-053 is a **singular double scaling**:

\[
s=1-O(\varepsilon)
\]

while the poles themselves move by \(O(\varepsilon)\).  This is not the ordinary fixed-\(s\) degeneration regime.

## 3. The unsupported step in PF-053

PF-053 defined

\[
H_\varepsilon(s)
=
\Phi_\varepsilon^{\rm mark}(s)
-
\sum_{j=0}^{N-1}
\frac{R_{j,\varepsilon}}{s-s_{j,\varepsilon}}
\]

and asserted

\[
\sup_{s\in D'}\|H_\varepsilon(s)\|=O(1)
\]

for a fixed disk \(D'\) about \(s=1\).

The available degeneration results do **not** imply this estimate as stated.  Meromorphic convergence away from the moving pole set does not by itself control the pole-subtracted regular parts uniformly when poles coalesce.  A scalar model already shows the logical gap: a meromorphic family may have prescribed converging principal parts while its holomorphic remainder grows like \(\varepsilon^{-1}A(z)\).  Such a term is invisible to pole-location and residue convergence but survives exactly under the PF-053 scaling.

Hence it is currently possible that

\[
\frac{\varepsilon}{\pi}
H_\varepsilon
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow A(z)
\]

for a nonzero holomorphic matrix \(A(z)\).  If that happens, the full scaling limit would be

\[
(G_a-zI)^{-1}+A(z),
\]

not the bare graph resolvent.

## 4. Consequence for the inverse-scattering claim

The following implication is therefore **not yet proved**:

\[
\boxed{
\text{raw physical marked scattering block near }s=1
\Longrightarrow
\text{weighted prime-gap path by direct blow-up}.
}
\]

What remains justified is the weaker but still substantive statement

\[
\boxed{
\text{coalescing residual pole positions + residue matrices}
\Longrightarrow
\text{weighted path / relative gap profile}.
}
\]

Equivalently, PF-051 and the polar-part formulation of PF-052 survive; the `ANALYTIC-GATE-OF-PF-052-CLOSED` status of PF-053 does not.

This correction matters because the appeal of PF-053 was precisely that **no pole extraction or counterterm was needed**.  Until the uniform regular-remainder estimate is independently proved, that stronger claim must not be used downstream.

## 5. What would close the gate

Any one of the following would be sufficient:

1. a uniform meromorphic-normal-family theorem for the **physical persistent-cusp scattering block after subtracting the entire coalescing residual pole cluster**, valid in an \(O(\varepsilon)\) neighbourhood of \(s=1\);
2. an explicit Neumann-to-Dirichlet / boundary-triple reduction showing that the only \(\varepsilon^{-1}\) singular part is the finite-dimensional Burger graph block;
3. a direct Feshbach/Grushin reduction of the Laplacian separating the componentwise-constant small-mode space from a uniformly invertible complement and propagating that decomposition to cusp scattering amplitudes.

The third route is likely the cleanest.  The uniform complement spectral gap used by Burger controls the interior resolvent on the orthogonal complement, but one still has to prove that the cusp boundary maps do not introduce an additional \(\varepsilon^{-1}\) amplification.

## 6. Serious literature check

- Schulze, *On the resolvent of the Laplacian on functions for degenerating surfaces of finite geometry* (JFA 236, 2006), proves resolvent convergence in the non-singular regime and explicitly introduces approximate Eisenstein functions and approximate scattering matrices for degeneration.  The paper does not state the PF-053 pole-subtracted physical-block estimate in the coalescing \(s=1-O(\varepsilon)\) regime.
- Levitin--Strohmaier express the physical scattering matrix in terms of the Neumann-to-Dirichlet map on a compact core, but this formula alone does not provide the needed uniform pinching estimate.
- Standard Maaß--Selberg theory does validate the residue identity used in PF-051/PF-052: residues of the scattering matrix are Gram matrices of residual Eisenstein eigenfunctions.  The correction is not a normalization issue in the residues.
- Directed searches for `pole-subtracted scattering matrix pinching hyperbolic surfaces`, `coalescing residual poles scattering s=1`, and `uniform regular remainder degenerating hyperbolic scattering` found the standard degeneration and scattering frameworks but not the required theorem.

No novelty is claimed for the analytic warning itself.  The substantive result for this program is a **correction of scope**: the graph-resolvent limit is presently established only for the extracted residual pole cluster, not for the entire raw physical scattering block.

## 7. Research consequence

Do not use PF-053 as evidence that the unmodified scattering matrix automatically provides a canonical gap-resolvent scaling law.  Keep the scattering-residue route alive, because it remains standard spectral data and still encodes the graph modes.  The next useful calculation is a genuine Feshbach/Schur-complement derivation of the physical scattering block at \(s=1-O(\varepsilon)\); it should either prove the missing \(O(1)\) remainder or exhibit an additional holomorphic effective term.
