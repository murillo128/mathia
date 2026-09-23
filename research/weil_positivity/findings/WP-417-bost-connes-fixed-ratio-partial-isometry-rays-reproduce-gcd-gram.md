---
id: WP-417
title: Bost-Connes fixed-ratio partial-isometry rays reproduce the critical GCD Gram
branch: weil_positivity
status: supported
kind: bost-connes-varying-range-ratio-ray-obstruction
claim_strength: exact RH-independent classification for the canonical Bost-Connes semigroup partial isometries mu_m mu_n^* under KMS scalarization; different multiplicative ratios are thermodynamically orthogonal, while every fixed-ratio block with genuinely varying source and range support is exactly the same normalized GCD Gram already found in WP-216, so the most canonical varying-range escape left by WP-416 adds no new sign mechanism
created: 2026-09-23
related: [WP-216, WP-412, WP-415, WP-416]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
  - O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics II, 2nd ed., Springer, 1997
  - M. Laca, S. Neshveyev and M. Trifkovic, Bost-Connes systems, Hecke algebras, and induction, J. Noncommut. Geom. 7 (2013), 525-546; arXiv:1010.4766
---

# WP-417 — Bost-Connes fixed-ratio partial-isometry rays reproduce the critical GCD Gram

## Claim

`WP-416` leaves one concrete correspondence escape open: allow both the canonical source projection and the generalized range projection to vary, rather than imposing a common range. The most canonical Bost--Connes realization of that escape can be classified exactly, and it collapses back to the same divisibility Gram already isolated in `WP-216`.

Let `(A_BC,sigma)` be the rational Bost--Connes system, let `phi_beta` be any `KMS_beta` state with `beta>0`, and define the canonical semigroup partial isometries

\[
v_{m,n}:=\mu_m\mu_n^*,\qquad m,n\ge 1.
\tag{1}
\]

They have source and range projections

\[
v_{m,n}^*v_{m,n}=E_n,\qquad v_{m,n}v_{m,n}^*=E_m,
\tag{2}
\]

and homogeneous thermodynamic frequency

\[
\sigma_t(v_{m,n})=(m/n)^{it}v_{m,n}.
\tag{3}
\]

For the KMS scalar Gram

\[
K_\beta((m,n),(m',n'))
:=\phi_\beta(v_{m,n}^*v_{m',n'}),
\tag{4}
\]

KMS invariance first gives the exact ratio gate

\[
\boxed{
\frac mn\ne\frac{m'}{n'}
\Longrightarrow
K_\beta((m,n),(m',n'))=0.
}
\tag{5}
\]

Now fix a reduced ratio `a/b` with `(a,b)=1`. Every pair on that ray is uniquely `(m,n)=(ak,bk)`. Then

\[
v_{ak,bk}=\mu_aE_k\mu_b^*,
\tag{6}
\]

so the sources `E_{bk}` and ranges `E_{ak}` both vary with `k`. Nevertheless their inner products satisfy the exact identity

\[
\boxed{
v_{ak,bk}^*v_{a\ell,b\ell}
=E_{b\operatorname{lcm}(k,\ell)}.
}
\tag{7}
\]

Using `phi_beta(E_n)=n^{-beta}`, the unnormalized scalar Gram on that ray is therefore

\[
K_\beta^{a/b}(k,\ell)
=\bigl(b\operatorname{lcm}(k,\ell)\bigr)^{-\beta}.
\tag{8}
\]

After normalizing each vector by its KMS norm, all dependence on the ratio `a/b` disappears:

\[
\boxed{
\widetilde K_\beta^{a/b}(k,\ell)
=\left(\frac{\gcd(k,\ell)}{\sqrt{k\ell}}\right)^\beta.
}
\tag{9}
\]

At the source-selected critical inverse temperature `beta=1`, every fixed-ratio varying-source/varying-range block is exactly the critical GCD/Poisson Gram of `WP-216`:

\[
\widetilde K_1^{a/b}(k,\ell)
=\frac{\gcd(k,\ell)}{\sqrt{k\ell}}.
\tag{10}
\]

Thus the full canonical family `mu_m mu_n^*`, after KMS scalarization and normalization, is block diagonal by the rational ratio `m/n`, and every nonzero ratio block is an identical copy of the already-audited divisibility Gram. The range label is genuine before scalarization but does not generate a new sign-relevant kernel. The direct semigroup varying-range escape therefore does not supply the missing Weil orientation, Gamma term, or polar sector.

**Classification:** `EXACT-DERIVED + BOST-CONNES-KMS + CANONICAL-SEMIGROUP-PARTIAL-ISOMETRIES + VARYING-SOURCE-AND-RANGE + RATIO-FREQUENCY-BLOCKING + FIXED-RATIO-LCM-GRAM + NORMALIZED-GCD-GRAM-COLLAPSE + CRITICAL-WP216-RECOVERY + MATCHED-POISSON-CONTROL + DECISIVE-NARROWING + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Canonical semigroup edges vary both supports

The partial-isometry identities in (2) are immediate from `mu_n^*mu_n=1`:

\[
\begin{aligned}
v_{m,n}^*v_{m,n}
&=\mu_n\mu_m^*\mu_m\mu_n^*=E_n,\\
v_{m,n}v_{m,n}^*
&=\mu_m\mu_n^*\mu_n\mu_m^*=E_m.
\end{aligned}
\tag{11}
\]

In the standard right module `A_BC`, the generalized rank-one support of `v_{m,n}` is left multiplication by `E_m`, while its module source norm is `E_n`. Hence the family genuinely leaves the common-range hypothesis of `WP-416` whenever `m` varies.

The dynamics is equally rigid. Since `sigma_t(mu_r)=r^{it}mu_r`, equation (3) follows. The thermodynamic degree remembers only the multiplicative ratio `m/n`, not the common factor of the pair.

This separates two pieces of information that were locked together under the common-range hypothesis of `WP-416`: the ratio fixes frequency, while the common multiplier can still move source and range supports inside one frequency sector.

## 2. KMS invariance splits the family into rational-ratio blocks

The Gram coefficient in (4) is homogeneous of frequency

\[
\omega
=\log\frac{m'/n'}{m/n}.
\tag{12}
\]

Every KMS state is invariant under the time evolution. Therefore the expectation of a homogeneous element of nonzero frequency vanishes. This proves (5).

The important point is that varying support is not completely killed now. Equal ratio permits distinct pairs. Writing a ratio in lowest terms as `a/b`, every surviving pair has the form `(ak,bk)`. Thus the only possible nontrivial incidence left by the KMS spectral gate lives along these fixed-ratio rays.

This is precisely the regime not covered by `WP-416`: source and range may both change while the frequency remains fixed.

## 3. Fixed-ratio rays reduce exactly to sandwiched divisibility projections

For `(a,b)=1`, semigroup commutativity gives

\[
\begin{aligned}
v_{ak,bk}
&=\mu_{ak}\mu_{bk}^*\\
&=\mu_a\mu_k\mu_k^*\mu_b^*\\
&=\boxed{\mu_aE_k\mu_b^*}.
\end{aligned}
\tag{13}
\]

Hence for any `k,l>=1`,

\[
\begin{aligned}
v_{ak,bk}^*v_{a\ell,b\ell}
&=\mu_bE_k\mu_a^*\mu_aE_\ell\mu_b^*\\
&=\mu_bE_kE_\ell\mu_b^*\\
&=\mu_bE_{\operatorname{lcm}(k,\ell)}\mu_b^*\\
&=\boxed{E_{b\operatorname{lcm}(k,\ell)}}.
\end{aligned}
\tag{14}
\]

No KMS input is used in this algebraic identity. It is a direct consequence of the semigroup isometries and the divisibility projection law `E_kE_l=E_lcm(k,l)`.

The diagonal case gives

\[
\|v_{ak,bk}\|_{\phi_\beta}^2
=\phi_\beta(E_{bk})
=(bk)^{-\beta}.
\tag{15}
\]

Combining (14) with the same exact KMS mass law proves (8).

## 4. Normalization erases the range ratio and restores the WP-216 kernel

Normalize the GNS vectors by

\[
\eta_{a/b,k}
:=(bk)^{\beta/2}\,\pi_\beta(v_{ak,bk})\Omega_\beta.
\tag{16}
\]

Then

\[
\begin{aligned}
\langle\eta_{a/b,k},\eta_{a/b,\ell}\rangle
&=(bk)^{\beta/2}(b\ell)^{\beta/2}
\bigl(b\operatorname{lcm}(k,\ell)\bigr)^{-\beta}\\
&=\left(\frac{\sqrt{k\ell}}{\operatorname{lcm}(k,\ell)}\right)^\beta\\
&=\boxed{\left(\frac{\gcd(k,\ell)}{\sqrt{k\ell}}\right)^\beta}.
\end{aligned}
\tag{17}
\]

The reduced numerator `a` disappeared already in (14). The reduced denominator `b` survives only as an overall unnormalized mass and cancels in (17). Thus all fixed-ratio blocks are unitarily indistinguishable at the level of their normalized scalar Gram.

At `beta=1`, restricting `k,l` to one prime axis gives

\[
\widetilde K_1(p^r,p^s)=p^{-|r-s|/2},
\tag{18}
\]

the same Poisson kernel that `WP-216` identified as the positive object whose local finite-Weil ray is the indefinite defect `log p (I-G_{1,p})`. Varying both correspondence supports has therefore not changed the sign bottleneck; it has reproduced it blockwise.

## 5. What information survives the equilibrium scalarization

Before scalarization, the canonical edge `v_{ak,bk}` knows three pieces of source data: the thermodynamic ratio `a/b`, the source support `E_{bk}`, and the range support `E_{ak}`. Equations (5) and (17) show exactly what the ordinary KMS Gram retains:

- different ratios survive only as mutually orthogonal blocks;
- inside a ratio block, the common multiplier survives only through the universal divisibility distance `gcd(k,l)/sqrt(kl)`;
- the normalized kernel forgets the reduced ratio itself.

This is a concrete instance of the source-collapse warning recorded after `WP-416`: genuine algebraic variation can remain present in the source category while the destination scalarization retains only a universal equilibrium quotient.

The result does not show that all varying-range Bost--Connes correspondences collapse this way. It classifies the most direct source-native family supplied by the semigroup generators themselves.

## 6. Matched control and relation to the Weil target

The normalized kernel in (17) needs no Riemann-specific interpretation. It is the standard positive-definite multiplicative GCD kernel, equivalently the product over primes of one-dimensional Poisson kernels

\[
\prod_p p^{-\frac\beta2|v_p(k)-v_p(\ell)|}.
\tag{19}
\]

Therefore an abstract product of independent Poisson/AR(1) Gram factors reproduces every normalized fixed-ratio block without the Bost--Connes phase algebra, the zeta partition function, Gamma data, or any Weil sign law. The Bost--Connes system source-forces this kernel, but its positivity remains generic Gram positivity.

More decisively, `WP-216` already computed the destination mismatch at the critical point. The desired finite-prime Weil Toeplitz ray is `log p(I-G_{1,p})`, not `G_{1,p}` itself, and that defect is indefinite. Taking a direct orthogonal sum of copies of `G_1` cannot reverse that orientation or manufacture the archimedean and polar terms.

Thus this finding is not another argument that the GCD kernel is positive. Its new content is that the canonical **varying-range and varying-source** semigroup path category left open by `WP-416` scalarizes to orthogonal copies of exactly that old kernel.

## 7. Prior-art and novelty audit

The ingredients are classical. Bost--Connes supplies the isometries, the time evolution, the divisibility projections and the KMS structure; standard KMS theory supplies invariance and the spectral vanishing of nonzero-frequency expectations. The monomial/partial-isometry structure generated by `mu_m` and `mu_n^*` is part of the ordinary semigroup-crossed-product description of the system. No originality is claimed for those identities, for the GCD kernel, or for its positive definiteness.

The external audit checked Bost--Connes/KMS expositions and searches for the semigroup monomials `mu_m mu_n^*`, KMS matrix coefficients, least-common-multiple projection products and GCD kernels. The standard relations and KMS phase structure are documented, but no source located in that audit stated the Mathia-specific conclusion needed here: **the complete canonical semigroup partial-isometry Gram decomposes by multiplicative ratio, and every surviving varying-source/varying-range ratio block normalizes to the same GCD kernel independently of the ratio.** The durable novelty claim is restricted to applying these elementary identities as an exact falsification theorem for this particular Weil-positivity escape.

Internally, `WP-216` derives the GCD Gram from conditioned divisibility projections but does not analyze varying-range semigroup edges. `WP-415` proves universal Hilbert-module Gram positivity and common-support reductions. `WP-416` proves that common-range canonical varying-source paths are forced into distinct frequencies and hence orthogonal. None classifies the equal-frequency family in which source and range both vary. Equations (13)--(17) close exactly that direct survivor without claiming a classification of arbitrary correspondences.

## 8. Adversarial boundary and next surviving mechanisms

The theorem is deliberately category-specific. It can fail to describe a proposal if the path vectors include nontrivial phase-algebra insertions between the semigroup isometries, if the correspondence is not the canonical coefficient module, if the dynamics is actively changed rather than inherited from `sigma`, if the readout is operator-valued or genuinely two-sided instead of the ordinary positive KMS Gram, or if source/range incidence is not proportional along a fixed thermodynamic ratio.

Those are now the meaningful places to look. In particular, a candidate using phase insertions must show that the phase data force the completed finite coefficients rather than merely decorating a positive Gram; an operator-valued or two-sided readout must retain orientation-sensitive range information after equilibrium; and any active correspondence dynamics must be source-derived rather than chosen to encode the desired sign.

Nothing here supplies the Gamma factor, polar terms, finite Weil orientation, coercivity, or an RH-independent completed sign theorem. The finding only removes the most canonical varying-range semigroup family from the live escape set. A further Bost--Connes advance must preserve source dependence that the ratio-block KMS scalarization in (5)--(17) demonstrably erases.