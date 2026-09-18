---
id: WP-365
title: The canonical finite-times-archimedean Rankin--Selberg tensor Gram is positive before continuation but still loses projective positivity at critical zeros
branch: weil_positivity
status: supported
kind: completed-rankin-selberg-tensor-gram-critical-obstruction
claim_strength: exact local-global Gram derivation with unconditional critical-line-zero falsification
created: 2026-09-18
related: [WP-356, WP-361, WP-362, WP-363, WP-364]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - A. Erdelyi, W. Magnus, F. Oberhettinger, and F. G. Tricomi, Tables of Integral Transforms, Vol. II, McGraw-Hill, 1954, formula 6.8.48
  - Michael Woodbury, On the Triple Product Formula: Real Local Calculations, preprint dated 16 June 2017, equation 2.10
  - NIST Digital Library of Mathematical Functions, Section 10.32(iii), equation 10.32.19
  - E. C. Titchmarsh, The Theory of the Riemann Zeta-function, 2nd ed. revised by D. R. Heath-Brown, Oxford University Press, 1986
---

# WP-365 — The canonical finite-times-archimedean Rankin--Selberg tensor Gram is positive before continuation but still loses projective positivity at critical zeros

## Claim

`WP-364` rules out repairing the Eisenstein coefficient Gram by scalar completion or projectivization, but deliberately leaves open a stronger possibility: enlarge the feature geometry by a **genuinely nonseparable positive archimedean sector before critical specialization**. The most canonical Rankin--Selberg version of that repair can be tested exactly, and it also fails.

For real spectral parameters `r,u` and `s>0`, define the archimedean Whittaker/Bessel Gram

\[
H_s(r,u)
:=
\int_0^\infty K_{ir}(x)K_{iu}(x)x^{s-1}\,dx.
\tag{1}
\]

Because `K_{it}(x)` is real for `x>0`, `t in R`, equation (1) is an ordinary Hilbert Gram on
`L^2((0,infinity),x^{s-1}dx)` and is positive semidefinite independently of zeta or RH. The integral converges for every `s>0`: exponential decay controls infinity, while the small-`x` behavior of `K_{it}` (and the logarithmic `K_0` limit) is integrable against `x^{s-1}dx`.

The classical Mellin product identity gives

\[
\boxed{
H_s(r,u)
=
\frac{2^{s-3}}{\Gamma(s)}
\prod_{\epsilon,\delta\in\{\pm1\}\atop \epsilon\delta=1\;\text{or}\;-1}
\Gamma\!\left(\frac{s+i(\epsilon r+\delta u)}2\right),
}
\tag{2}
\]

where the product means the four factors

\[
\Gamma\!\left(\frac{s+i(r+u)}2\right)
\Gamma\!\left(\frac{s-i(r+u)}2\right)
\Gamma\!\left(\frac{s+i(r-u)}2\right)
\Gamma\!\left(\frac{s-i(r-u)}2\right).
\tag{3}
\]

For `s>1`, combine this with the positive Hecke-coefficient Gram from `WP-363`--`WP-364`,

\[
K_s^{\rm fin}(r,u)
=
\sum_{n\ge1}\frac{\lambda_r(n)\lambda_u(n)}{n^s}
=
\frac{A_s(r+u)A_s(r-u)}{\zeta(2s)},
\qquad
A_s(t)=|\zeta(s+it)|^2.
\tag{4}
\]

The pointwise product

\[
J_s(r,u):=K_s^{\rm fin}(r,u)H_s(r,u)
\tag{5}
\]

is again positive semidefinite by the Schur product theorem; more intrinsically it is the Gram of the tensor features

\[
v_r^{\rm fin}\otimes w_r^\infty,
\qquad
w_r^\infty(x)=K_{ir}(x).
\tag{6}
\]

Thus the finite and infinite places have now been assembled **before** taking any scalar readout, and the new Gamma dependence is nonseparable in `(r,u)`. This is not the scalar gauge excluded by `WP-364`.

Let

\[
\Gamma_{\mathbb R}(z)=\pi^{-z/2}\Gamma(z/2),
\qquad
\Lambda(z)=\Gamma_{\mathbb R}(z)\zeta(z),
\qquad
B_s(t)=|\Lambda(s+it)|^2.
\tag{7}
\]

Multiplying (2) and (4) gives the exact completed factorization

\[
\boxed{
J_s(r,u)
=
2^{s-3}\pi^s
\frac{B_s(r+u)B_s(r-u)}{\Lambda(2s)},
\qquad s>1.
}
\tag{8}
\]

This is the canonical local-global completion one would hope could preserve positivity at the Weil half-density: the finite Hecke Gram supplies the Euler factors, the independent Bessel Gram supplies the archimedean Gamma factors, and positivity before continuation is a theorem of Hilbert/tensor geometry.

Nevertheless its intrinsic projective geometry fails at `s=1/2`. Normalize

\[
\widehat C_s(r,u)
:=
\frac{J_s(r,u)}{\sqrt{J_s(r,r)J_s(u,u)}}.
\tag{9}
\]

All common scalar factors in (8), including `1/Lambda(2s)`, cancel, leaving

\[
\boxed{
\widehat C_s(r,u)
=
\frac{B_s(r+u)B_s(r-u)}
{B_s(0)\sqrt{B_s(2r)B_s(2u)}}.
}
\tag{10}
\]

At the critical exponent put

\[
B_*(t):=\left|\Lambda\!\left(\frac12+it\right)\right|^2.
\tag{11}
\]

If `gamma` is the ordinate of any zero of zeta on the critical line, then the Gamma factor in (7) is finite and nonzero at `1/2+i gamma`, so `B_*(gamma)=0` with exactly the same zero order as `|zeta(1/2+i t)|^2`. Choose generic real `u` for which

\[
B_*(\gamma/2+u)B_*(\gamma/2-u)B_*(2u)>0.
\tag{12}
\]

Then, as `r -> gamma/2` through regular values,

\[
\boxed{
|\widehat C_*(r,u)|\longrightarrow\infty.
}
\tag{13}
\]

But every normalized positive-semidefinite Gram with unit diagonal satisfies `|C(r,u)|<=1`. Hence the canonical finite-times-archimedean tensor Gram has **no critical projective continuation preserving its own Hilbert positivity**.

The infinitesimal version is equally sharp. For `s>1`, the Fubini--Study pullback of the tensor-feature ray is

\[
\widehat g_s(r)
=
\left.\partial_r\partial_u\log J_s(r,u)\right|_{u=r}
=
(\log B_s)''(2r)-(\log B_s)''(0)
\ge0.
\tag{14}
\]

If the critical zero at `gamma` has multiplicity `m>=1`, then locally

\[
B_*(t)=|t-\gamma|^{2m}G(t),
\qquad G(\gamma)>0,
\tag{15}
\]

with `G` smooth and positive. Therefore

\[
(\log B_*)''(t)
=-\frac{2m}{(t-\gamma)^2}+O(1),
\tag{16}
\]

and

\[
\boxed{
\widehat g_*(r)\longrightarrow-\infty
\quad\text{as}\quad r\to\gamma/2.
}
\tag{17}
\]

The archimedean Gamma contribution is smooth at every such real critical zero and cannot cancel this negative pole. Thus even the canonical nonseparable Bessel completion does not rescue the Rankin--Selberg route.

**Classification:** `CLASSICAL-K-BESSEL-MELLIN + CLASSICAL-RANKIN-SELBERG + EXACT-DERIVED + INDEPENDENT-TENSOR-GRAM-POSITIVITY + FINITE-ARCHIMEDEAN-COMPLETION + NONSEPARABLE-GAMMA-COUPLING + CRITICAL-OVERLAP-UNBOUNDED + CRITICAL-METRIC-NEGATIVE + HARDY-ZERO-CONTROL + DECISIVE-NARROWING + NO-NOVELTY-CLAIM-FOR-CLASSICAL-INGREDIENTS`.

## 1. The archimedean factor is an independent positive geometry

The important distinction from a scalar completion is structural. Replacing `v_r` by `a(r)v_r` only multiplies a Gram kernel by a separated factor `a(r) conjugate(a(u))`; projectivization removes it identically. Equation (1) instead introduces a new feature vector `w_r^infty` in its own Hilbert space. Its mixed Gram entry depends on both `r+u` and `r-u` through four Gamma factors, so it cannot be absorbed into a scalar gauge of the finite vector family.

For a finite set `r_1,...,r_N` and coefficients `c_1,...,c_N`,

\[
\sum_{j,k}\overline{c_j}c_k H_s(r_j,r_k)
=
\int_0^\infty
\left|\sum_j c_j K_{ir_j}(x)\right|^2x^{s-1}\,dx
\ge0.
\tag{18}
\]

Likewise `K_s^fin` is a coefficient Gram for `s>1`. Therefore

\[
\sum_{j,k}\overline{c_j}c_k J_s(r_j,r_k)\ge0
\tag{19}
\]

without using the factorized zeta expression. The positivity theorem exists before any appeal to the divisor of zeta.

The exact Gamma product (2) is classical. In Woodbury's normalization, equation (2.10) states the equivalent identity for `K_nu(y/2)K_mu(y/2)y^s d^x y`, citing Erdelyi--Magnus--Oberhettinger--Tricomi formula 6.8.48. DLMF 10.32.19 gives the corresponding Mellin--Barnes product representation. Setting `mu=ir`, `nu=iu` yields (2) after the elementary change of variables.

## 2. The tensor Gram supplies the completed zeta factors automatically

Equation (8) is not obtained by inserting `Gamma_R` by hand. The four zeta factors are forced by the Hecke coefficient identity in (4), while the four Gamma factors with the same spectral combinations are forced by the independent Bessel Gram (2). Since the four arguments

\[
s\pm i(r+u),\qquad s\pm i(r-u)
\tag{20}
\]

sum to `4s`, their powers of `pi` combine exactly into the scalar `pi^s` in (8), and

\[
\Gamma(s)\zeta(2s)=\pi^s\Lambda(2s).
\tag{21}
\]

Thus the finite and archimedean factors close into completed zeta functions without a fitted counterterm. Standard changes of Whittaker normalization or the scale `x -> 2 pi x` only contribute positive scalar or separated factors; they cancel from (9) and do not affect the obstruction.

This makes (5) a stricter control than the scalar Gamma completions dismissed in `WP-364`: a source-defined infinite-place Hilbert space has genuinely changed the cross-parameter geometry, yet the result remains exactly computable.

## 3. Critical zeros destroy the completed projective Gram

For `s>1`, positivity of `J_s` makes (9) a normalized Hilbert overlap. Therefore every `2 x 2` principal minor requires

\[
1-|\widehat C_s(r,u)|^2\ge0.
\tag{22}
\]

Equation (10) is the unique pointwise continuation furnished by the exact local-global factorization wherever the denominator is nonzero. At `s=1/2`, `Gamma_R(1/2+it)` has neither zeros nor poles for real `t`; consequently the zero set of `B_*` is precisely the critical-line zero set of zeta, with unchanged multiplicities.

Hardy's theorem supplies infinitely many such zeros unconditionally. For each one, the exceptional `u` excluded by (12) belongs to a discrete set. Hence (13) holds for generic `u`, not merely at a singular diagonal point. Deleting the exact zero ray cannot restore positivity: regular points arbitrarily close to it already violate (22), and in fact the violation becomes unbounded.

The metric calculation (14)--(17) is independent confirmation. The Gamma factor contributes a real-analytic bounded term to `(log B_*)''` near each critical zero; the arithmetic zero contributes the negative double pole in (16). Therefore no smooth archimedean normalization of the same local Bessel sector can reverse the sign.

## 4. Matched controls and attempted repairs

**Archimedean sector alone.** `H_{1/2}` is still an honest positive Bessel Gram. The target exponent is not singular for the infinite-place Hilbert geometry itself. The failure appears only after the arithmetic finite factor is analytically continued and its critical divisor is combined with that geometry.

**Finite sector without Gamma.** This is `WP-364`: the normalized zeta-only overlap already blows up near critical zeros. The present test asks whether the strongest canonical nonseparable Gamma coupling changes that conclusion. It does not, because the Gamma factor is smooth and nonzero at the arithmetic zeros.

**Standard Whittaker renormalization.** Multiplying `K_{ir}` by any nonzero normalization `a(r)` changes `H_s(r,u)` by the separated factor `a(r)conjugate(a(u))`; the normalized overlap and Fubini--Study metric are invariant. Changing the positive scale in the Bessel argument contributes only an `s`-dependent scalar. Thus ordinary representation-theoretic normalization conventions cannot repair (13) or (17).

**Insert a zeros-cancelling factor.** A factor that cancels the denominator zero in (10) must itself know the arithmetic divisor or otherwise introduce a singular nonlocal coupling at precisely those spectral parameters. Such a repair is no longer supplied by the local archimedean Whittaker geometry; absent an independent source theorem it is exactly the zero-coded or hand-picked regularization excluded by the research mandate.

**Use an operator-valued rather than tensor/Schur completion.** This remains open. The finding rules out the canonical local-product completion, not every possible finite--archimedean interaction. A surviving route must mix the local sectors before scalarization in a way that changes the normalized divisor geometry, rather than merely multiply independent positive local Gram kernels.

## 5. Prior-art and novelty audit

Every analytic ingredient is classical. The Bessel-product Mellin identity is tabulated by Erdelyi--Magnus--Oberhettinger--Tricomi and used explicitly in archimedean Whittaker calculations such as Woodbury's equation (2.10). Rankin--Selberg local factors, completed zeta functions, and critical-line zeros are standard automorphic/analytic-number-theory objects. The Schur/tensor-product positivity statement is elementary Hilbert-space theory.

A targeted literature audit for combinations of Rankin--Selberg positive-definite/Gram kernels, Eisenstein K-Bessel or Whittaker Grams, completed-zeta projective kernels, and Fubini--Study geometry did not locate a source asserting that this particular tensor Gram yields a positive continuation at the critical half-density. The search instead surfaced standard work on Eisenstein K-Bessel expansions, local Rankin--Selberg integrals, and completed automorphic L-factors. This is not a historical novelty proof, and no novelty is claimed for those ingredients.

The Mathia-specific result is the **falsification of a precise surviving construction**: after `WP-364` says scalar Gamma completion is projectively invisible, promote the archimedean factor to its own positive Whittaker Hilbert geometry, tensor it canonically with the positive finite Hecke feature space, and test the inherited projective sign. The completion now genuinely contains both finite and infinite local factors, but the target critical continuation still violates the positivity theorem that generated it.

## Representation audit

The candidate is defined from source-side automorphic features: Hecke coefficient vectors at the finite places and K-Bessel/Whittaker functions at the real place. Neither feature space is defined from zeta zeros. Positivity for `s>1` is established directly by squared norms and tensor products, while equation (8) is a derived arithmetic bridge.

Critical zeros are introduced only after the construction is fixed, as an adversarial falsifier. The test therefore does not assume RH, reconstruct a spectrum from zeros, or define a kernel by the desired Weil functional. The Gamma sector is retained explicitly rather than absorbed into a scalar completion, so the failure cannot be attributed to having omitted the archimedean local geometry.

What remains beyond this obstruction is narrower than after `WP-364`: a successful construction must be **more than the canonical tensor product of independently positive finite and archimedean Rankin--Selberg local features**. It needs a source-forced operator, boundary, correspondence, or cohomological coupling that changes finite--archimedean cross-correlations before the critical specialization and proves its sign independently of the zeta divisor.

## Verdict

**Supported exact negative.** The canonical Bessel/Whittaker archimedean Gram supplies exactly the Gamma factors missing from the positive finite Hecke Rankin--Selberg Gram, and their tensor product is independently positive for `s>1`. This is a genuine nonseparable finite--archimedean completion, not a scalar gauge. Yet after projective normalization its critical continuation is controlled by `|Lambda(1/2+it)|^2`; every unconditional critical-line zero forces unbounded normalized overlaps and a negatively divergent Fubini--Study metric on nearby regular points.

Therefore the natural local-product Rankin--Selberg completion does not furnish Mathia's sought global Weil positivity. Any surviving Maaß--Selberg/Hecke route must introduce a genuinely noncentral finite--archimedean mixing mechanism rather than multiplying positive local Gram factors and analytically continuing the result.