---
id: WP-347
title: Self-adjoint point scatterers show one-cusp hyperbolic realizability does not fix the scattering divisor
branch: weil_positivity
status: supported
kind: hyperbolic-point-scatterer-relative-scattering-control
claim_strength: literature-backed exact relative-scattering identity plus matched-control consequence
created: 2026-09-17
related: [WP-237, WP-345, WP-346, WP-188]
prior_art:
  - Henrik Ueberschär, The trace formula for a point scatterer on a hyperbolic surface with one cusp, arXiv:1111.6198v2 (2012)
  - Yves Colin de Verdière, Pseudo-laplaciens I, Ann. Inst. Fourier 32 (1982), 275-286
  - classical rank-one self-adjoint extension and relative scattering theory
---

# WP-347 — Self-adjoint point scatterers show one-cusp hyperbolic realizability does not fix the scattering divisor

## Claim

The source-realizability escape left after `WP-345`--`WP-346` can be narrowed substantially. One does not need to leave finite-volume one-cusp hyperbolic geometry to obtain a **genuine self-adjoint scattering system whose meromorphic scattering divisor moves while the underlying cusp geometry and Hilbert-space positivity remain**.

Let

\[
X=\Gamma\backslash\mathbb H
\tag{1}
\]

be a finite-volume hyperbolic surface with one cusp, let `z_0 in X`, and formally perturb the Laplacian by a real point interaction

\[
\Delta_{\alpha,z_0}
=\Delta+\alpha\,\delta_{z_0}(\delta_{z_0},\cdot),
\qquad \alpha\in\mathbb R\setminus\{0\}.
\tag{2}
\]

Ueberschär constructs (2) rigorously by von Neumann self-adjoint extension theory: the Laplacian restricted to functions vanishing at `z_0` has deficiency indices `(1,1)`, and real `alpha` selects a self-adjoint extension. The perturbed operator has generalized Eisenstein eigenfunctions with the same one-cusp asymptotic form

\[
E^{\alpha,z_0}(x+iy,s)
=y^s+\varphi_{\alpha,z_0}(s)y^{1-s}+O(e^{-2\pi y}).
\tag{3}
\]

Its scattering coefficient is related **exactly** to the unperturbed one by Ueberschär's equation (4.24), repeated as (6.1):

\[
\boxed{
\varphi_{\alpha,z_0}(s)
=\varphi(s)
\frac{S_{\alpha,z_0}(1-s)}{S_{\alpha,z_0}(s)}.
}
\tag{4}
\]

Here `S_{alpha,z_0}` is the meromorphic spectral function built from the regularized automorphic Green function and the coupling constant. Therefore the source-defined relative factor

\[
\Theta_{\alpha,z_0}(s)
:=\frac{\varphi_{\alpha,z_0}(s)}{\varphi(s)}
=\frac{S_{\alpha,z_0}(1-s)}{S_{\alpha,z_0}(s)}
\tag{5}
\]

satisfies the reciprocal identity

\[
\Theta_{\alpha,z_0}(1-s)=\Theta_{\alpha,z_0}(s)^{-1},
\tag{6}
\]

while its meromorphic divisor changes with the point interaction. Ueberschär's Theorem 3 identifies zeros of `S_{alpha,z_0}` in `Re s<1/2` with **perturbed resonances** and poles there with unperturbed resonances; crucially, self-adjointness rules out nonreal zeros only in the `L^2` eigenvalue region `Re s>=1/2`, while the resonance zeros in `Re s<1/2` may be nonreal.

Consequently,

\[
\boxed{
\begin{gathered}
\text{same finite-volume one-cusp hyperbolic surface}
+\text{self-adjoint source operator}
+\text{positive Hilbert norm}
+\text{Eisenstein scattering/trace framework}
\\[2mm]
\not\Rightarrow
\text{rigidity of the meromorphically continued scattering divisor}.
\end{gathered}
}
\tag{7}
\]

This is a stricter matched control than the free Robin model of `WP-346`: the divisor-changing freedom already occurs **inside the same one-cusp hyperbolic scattering category**. It does **not** show that the point-scattered operator preserves the arithmetic/Hecke/Euler structure of the unperturbed modular or congruence Laplacian. Indeed the point perturbation introduces a new spectral function and diffractive-orbit terms. Thus the surviving escape is now specifically arithmetic: any theorem intended to force a Weil sign from source realizability must use rigidity such as the unperturbed arithmetic Laplacian, Hecke symmetry, Euler-product normalization, or another comparably strong arithmetic constraint, rather than generic hyperbolic automorphy, self-adjointness, cusp geometry, or Hilbert positivity.

**Classification:** `LITERATURE-BACKED-EXACT + SELF-ADJOINT-HYPERBOLIC-POINT-SCATTERER + RELATIVE-SCATTERING-FACTOR + RESONANCE-DIVISOR-MOBILITY + MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

## 1. The point perturbation stays on the same one-cusp surface

Ueberschär works on a fixed noncompact finite-volume surface `X=Gamma\H` with one cusp. The formal delta perturbation (2) is not treated as a non-self-adjoint effective model. If `D_0` is the domain of the positive Laplacian restricted to functions vanishing at `z_0`, then the symmetric operator has deficiency indices `(1,1)`. Its deficiency vectors are automorphic Green functions, and von Neumann theory gives a one-parameter family of self-adjoint extensions. The real coupling `alpha` is in one-to-one correspondence with the extension parameter.

Hence the control preserves several pieces that the free half-line model of `WP-346` deliberately discarded:

- the same hyperbolic quotient `X`;
- the same unique cusp and continuous spectral channel;
- automorphic Green functions and Eisenstein-type generalized eigenfunctions;
- a self-adjoint operator on `L^2(X)`;
- the ordinary positive Hilbert norm and positive norms of every spatially truncated generalized eigenfunction;
- an exact Selberg-type relative trace formula.

None of these properties prevents the meromorphic scattering data from acquiring a nontrivial relative factor.

This does not mean that the *operator* is unchanged. The point interaction is precisely a rank-one domain-changing perturbation. That distinction is the point of the control: if a proposed positivity theorem uses only the broad geometric/scattering properties above, then it cannot distinguish the original arithmetic Laplacian from this self-adjoint deformation.

## 2. The relative scattering factor is source-defined, not hand-picked

For the unperturbed Eisenstein series write the cusp expansion

\[
E(x+iy,s)
=y^s+\varphi(s)y^{1-s}+O(e^{-2\pi y}).
\tag{8}
\]

Ueberschär constructs a perturbed Eisenstein series `E^{alpha,z_0}` satisfying the analogous expansion (3). The exact relation (4) then separates the old scattering coefficient from the perturbation through `S_{alpha,z_0}`.

Unlike the abstract CDD multiplier introduced as a falsification device in `WP-345`, the factor (5) is selected before any desired zero location is inspected. It is forced by a concrete self-adjoint extension specified by the geometric point `z_0` and real coupling `alpha`. Its reciprocal symmetry (6) is automatic from the ratio form.

The paper's trace formula makes the same factor divisor-sensitive. In its continuous term the difference between perturbed and unperturbed scattering logarithmic derivatives is written through the logarithmic derivative of the relative factor. Equivalently, Ueberschär introduces

\[
\theta_{\alpha,z_0}\left(\tfrac12+i\rho\right)
=
\frac{S_{\alpha,z_0}(\tfrac12-i\rho)}
{S_{\alpha,z_0}(\tfrac12+i\rho)},
\tag{9}
\]

and the relative trace formula integrates `theta' / theta`. Thus the change in meromorphic divisor is not invisible bookkeeping: it is exactly the scattering contribution seen by the trace formula.

## 3. Self-adjointness controls eigenvalues, not resonance locations

The decisive point is the separation between `L^2` spectrum and resonances. Ueberschär's Theorem 3 states that:

- in `Re s>=1/2`, zeros of `S_{alpha,z_0}` correspond to new `L^2` eigenvalues, and self-adjointness rules out nonreal such zeros;
- in `Re s<1/2`, zeros correspond to perturbed resonances, whose generalized eigenfunctions are not in `L^2(X)`, and these zeros may have nonzero imaginary part.

The same theorem identifies poles in the left half-plane with unperturbed resonances. Therefore (5) changes the continued scattering divisor by exchanging the perturbed and unperturbed resonance data. This is exactly the logical gap that a bare appeal to positive Hilbert geometry misses: positivity constrains the self-adjoint spectral measure on the physical axis, while the Weil problem is sensitive to the **meromorphic continuation** and its divisor.

On the critical line the spectral function has the source-defined imaginary part

\[
\operatorname{Im}S_{\alpha,z_0}\left(\tfrac12+it\right)
=
\frac{|E(z_0,\tfrac12+it)|^2}{4t},
\qquad t\ne0,
\tag{10}
\]

so even there positivity appears as a boundary constraint rather than as a theorem fixing the full continued divisor. A critical-line zero additionally requires a simultaneous zero of `E(z_0,s)` and a vanishing real part of `S_alpha`. The continued left-half-plane resonance divisor remains free to move under the self-adjoint perturbation.

This gives a geometric version of the `WP-345`--`WP-346` lesson: boundary positivity/unitarity and self-adjointness do not propagate by themselves into a sign or location theorem for the analytically continued divisor.

## 4. Aggressive falsification and exact scope

**The control does not preserve Hecke symmetry.** A delta interaction at a generic point singles out `z_0`. On an arithmetic quotient this generally breaks Hecke invariance. Therefore (7) does not refute a theorem whose hypotheses genuinely use the unperturbed Hecke algebra or an Euler-product characterization of the scattering coefficient. It refutes only weaker claims based on one-cusp hyperbolic geometry, automorphic Green/Eisenstein analysis, self-adjointness, trace formulas, or Hilbert positivity alone.

**The control does not preserve the original Euler product.** Equation (4) multiplies the old coefficient by a Green-function spectral factor. Ueberschär's relative trace formula correspondingly introduces combinations of diffractive orbits that visit the scatterer. Thus the perturbation is not a second arithmetic model with the same Euler factors. The conclusion is a narrowing: a viable positivity theorem must make essential use of precisely the arithmetic structure that the scatterer destroys.

**This is not an arbitrary regularization.** `S_{alpha,z_0}` is the spectral function of a fixed self-adjoint extension, and the same function governs perturbed eigenvalues, resonances, Eisenstein scattering and the relative trace formula. No zero locations or test kernels are inserted by hand.

**This is not an RH-equivalent positivity criterion.** The construction does not prove any sign for the Riemann zero functional and does not assume zero locations. It is a matched control showing that a broad proposed source category remains too flexible.

**The finding is compatible with `WP-188`.** `WP-188` excluded the exact Gamma phase as an ordinary trace-class Birman--Krein determinant. A point interaction is a singular/domain-changing self-adjoint extension, one of the categories that ordinary trace-class perturbation arguments do not cover. The present result says that entering such a self-adjoint hyperbolic extension category does not itself create the missing Weil sign.

**The finding is stronger than, but does not replace, `WP-346`.** `WP-346` realizes the exact elementary CDD factor in a free Robin problem and proves an explicit positive truncated-norm identity. `WP-347` does not claim that the Ueberschär relative factor equals that rational CDD factor, nor does it need that stronger algebraic match. Instead it moves the matched control into the one-cusp hyperbolic setting itself and proves that divisor mobility persists there under a source-defined self-adjoint perturbation.

## 5. Prior-art and novelty audit

The mathematical ingredients are prior art. Ueberschär, *The trace formula for a point scatterer on a hyperbolic surface with one cusp*, arXiv:`1111.6198v2` (2012), gives the self-adjoint point-scatterer construction, the perturbed Eisenstein series, the exact relative scattering formula (4.24)/(6.1), the classification of zeros and poles of the spectral function in Theorem 3, and the exact relative trace formula. The construction builds on the classical pseudo-Laplacian/self-adjoint-extension literature, including Colin de Verdière.

A targeted audit therefore finds no theorem-level novelty in (2)--(6) or in the resonance classification. The durable Mathia delta is the **matched-control consequence for the current Weil-positivity route**: after `WP-345` showed that boundary-square positivity is divisor-blind and `WP-346` showed that generic self-adjoint scattering realizes the CDD control, the point-scatterer literature shows that even requiring the same finite-volume one-cusp hyperbolic geometry and Eisenstein/trace architecture does not fix the continued divisor. The residual hypothesis must be arithmetic-specific.

Primary source:

- Henrik Ueberschär, *The trace formula for a point scatterer on a hyperbolic surface with one cusp*, arXiv:`1111.6198v2`, https://arxiv.org/abs/1111.6198.

## Consequence for `weil_positivity`

The surviving Maaß--Selberg route is narrower than after `WP-346`. It is no longer enough to ask whether the desired scattering normalizer has a genuine self-adjoint realization on a finite-volume one-cusp hyperbolic surface. Such realizations can carry movable resonance divisors while retaining positive Hilbert geometry and a full Eisenstein/trace formalism.

What remains genuinely untested is whether **arithmetic rigidity itself** can tie the divisor-sensitive logarithmic derivative to a source-positive form before scalar separation. Concretely, a surviving theorem must exploit structure absent from the point scatterer—for example Hecke equivariance, an Euler-product/local-global characterization, a canonical arithmetic correspondence, or a noncentral automorphic coupling that cannot be deformed by a rank-one point interaction while preserving its hypotheses.

Accordingly the route boundary becomes

\[
\boxed{
\text{generic self-adjoint one-cusp hyperbolic scattering is a matched control;}
\\
\text{only specifically arithmetic source rigidity remains a viable escape.}
}
\tag{11}
\]
