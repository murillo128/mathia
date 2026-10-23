---
title: "WP-443: The critical valuation energy has an explicit hierarchical spectrum"
type: research-finding
status: verified
research_question: "What spectrum and observable representation does the closed critical valuation completion actually carry?"
claim_strength: exact_complete_eigenbasis_operator_domain_simple_spectrum_and_heat_trace_threshold
scope: WP-442's radial critical valuation form with its prescribed conductances; no full Bost--Connes Markov extension or identification with the Weil test form
finding_id: WP-443
related_findings:
  - WP-442
  - WP-441
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-24
updated: 2026-10-24
tags:
  - weil-positivity
  - critical-kms
  - valuation-product
  - hierarchical-laplacian
  - spectral-classification
  - representation-boundary
---

# WP-443: The critical completion diagonalizes into integer excitation modes

## Result and evidence boundary

**EXACT-DERIVED; CLASSICAL HIERARCHICAL DIAGONALIZATION.** Let \(A\ge0\)
be the self-adjoint operator of WP-442's closed critical valuation
energy. It has a complete orthonormal basis \((\Psi_n)_{n\ge1}\) with
\[
 A\Psi_n=\eta_n\Psi_n,\qquad
 \boxed{\eta_n=\log n+\sum_{p\mid n}\frac{\log p}{p-1}.}
 \tag{1}
\]
The eigenvalues are all distinct; \(\eta_1=0\), the spectral gap is
\(2\log2\), and the resolvent is compact. The heat operator is compact
for every \(t>0\), but is trace class **exactly when \(t>1\)**.

Thus the critical probability space supports a perfectly well-defined
positive operator while still having a divergent heat trace at time one.
Its spectrum is an explicit additive occupation spectrum, not a spectrum
of zeta zeros. The diagonalizing unitary does not intertwine the source
range projections with the usual integer divisibility projections.
Consequently this classification does not undo WP-442's representation
boundary or WP-441's critical subtraction obstruction.

The local diagonalization is a specialization of classical hierarchical
Laplacian theory. The line-local delta is the complete spectral and
operator-domain classification of this particular closed completion,
including the precise thermodynamic and observable boundaries. No
historical novelty, independent adversarial approval, formal verification,
Gamma/polar completion, or RH implication is claimed.

## Fixed form and local eigenfunctions

Retain WP-442's probability space and conductances:
\[
 \nu=\prod_p\nu_p,\qquad \nu_p(j)=(1-p^{-1})p^{-j},\qquad
 c_p(j,k)=(\log p)\nu_p(k)\quad(j<k).
 \tag{2}
\]
The Hilbert space is \(\mathcal H=L^2(\nu)\), and
\[
 \mathcal E[g]=\sum_p\sum_{j<k}c_p(j,k)
       \|g_{p,j}-g_{p,k}\|_{L^2(\nu_{\ne p})}^2,
 \quad D(\mathcal E)=\{g\in\mathcal H:\mathcal E[g]<\infty\}.
 \tag{3}
\]
WP-442 proves closure and that finite linear combinations of divisibility
tails are a form core. The present argument uses that exact realization;
it does not assign a spectrum to a formal matrix with an unspecified
extension.

First work at one coordinate with arbitrary \(0<r<1\), scale \(\lambda>0\),
measure \(\nu_r(j)=(1-r)r^j\), and conductance
\(c(j,k)=\lambda\nu_r(k)\) for \(j<k\). Set
\[
 h_a(j)=1_{j\ge a},\qquad
 \psi_0=1,\qquad
 \psi_a=\frac{h_a-rh_{a-1}}{\sqrt{(1-r)r^a}}\quad(a\ge1).
 \tag{4}
\]
Since \(\int h_a\,d\nu_r=r^a\), each numerator has mean zero and
squared norm \((1-r)r^a\). For \(b>a\), \(\psi_a\) is constant on
the support of \(\psi_b\), proving orthogonality. Conversely,
\[
 h_a=rh_{a-1}+\sqrt{(1-r)r^a}\,\psi_a
 \tag{5}
\]
puts every tail in their algebraic span. Tail differences give all
singleton indicators, so (4) is a complete orthonormal basis.

The nonnegative generator is
\[
 (A_{r,\lambda}g)(j)=\lambda\left[
    \sum_{k<j}(g(j)-g(k))+
    \sum_{k>j}r^{k-j}(g(j)-g(k))\right].
 \tag{6}
\]
For \(w_a=h_a-rh_{a-1}\), consider the three regions
\(j<a-1\), \(j=a-1\), and \(j\ge a\). In the first, the weighted
mean of the later values is zero. In the second, the lower coordinates
contribute \(-\lambda(a-1)r\), and the upper coordinates contribute
\(-\lambda r/(1-r)\). In the third, the lower-coordinate contribution
is \(\lambda((a-1)(1-r)+1)\), and all later differences vanish.
Therefore
\[
 A_{r,\lambda}\psi_0=0,\qquad
 A_{r,\lambda}\psi_a=
       \lambda\left(a+\frac r{1-r}\right)\psi_a\quad(a\ge1).
 \tag{7}
\]

This is also an operator-domain assertion. The \(\psi_a\) are bounded
finite-energy functions. Summation by parts against finitely supported
functions gives
\(\mathcal E(\psi_a,g)=\lambda(a+r/(1-r))\langle\psi_a,g\rangle\).
The sums converge absolutely: a fixed row has finite outgoing rate,
and the total local conductance is \(\lambda r/(1-r)<\infty\).
The identity extends from the local form core to every form-domain
vector by form-norm continuity. The representation theorem for a closed
form then places \(\psi_a\) in \(D(A_{r,\lambda})\) and proves (7).

## Exact hierarchical interpretation and prior art

Let \(T_b=\{b,b+1,\ldots\}\), with mass \(r^b\), and let
\(\operatorname{av}_{T_b}g=r^{-b}\int_{T_b}g\,d\nu_r\). Then
\[
 A_{r,\lambda}g(j)=\sum_{b=0}^{j}C_b
             \big(g(j)-\operatorname{av}_{T_b}g\big),\qquad
 C_0=\frac\lambda{1-r},\quad C_b=\lambda\ (b\ge1).
 \tag{8}
\]
Indeed, the off-diagonal rate from \(j\) to \(k\) on the right is
\[
 \nu_r(k)\sum_{b\le\min(j,k)}C_b r^{-b}
 =\nu_r(k)\frac{\lambda r^{-\min(j,k)}}{1-r},
 \tag{9}
\]
which is \(\lambda\) if \(k<j\) and \(\lambda r^{k-j}\) if
\(k>j\). Conservativity fixes the diagonal as well.

This is a hierarchical Laplacian for the nested tails. One can add a
zero-mass point at infinity and use the compact ultrametric
\(d(j,k)=r^{\min(j,k)}\) for distinct finite points and
\(d(j,\infty)=r^j\); the nonsingleton balls are the tails with that
point appended. Bendikov--Krupski, equations (1.3)--(1.5) and Section 3,
give the standard tail-average operator, differences of normalized
nested indicators, and cumulative ancestor eigenvalues. Here the
cumulative sum is explicitly
\(C_0+\cdots+C_{a-1}=\lambda(a+r/(1-r))\).
Equations (4)--(9) supply the specialization directly, including its
probability-space domain. No new general wavelet or hierarchy theorem
is asserted.

## Infinite product, exact domains, and simple spectrum

Use (4) at prime \(p\) with \(r=p^{-1}\), \(\lambda=\log p\), and
write the functions as \(\psi_{p,a}\). For each integer \(n\ge1\), define
\[
 \Psi_n(J)=\prod_{p\mid n}\psi_{p,v_p(n)}(J_p),\qquad \Psi_1=1.
 \tag{10}
\]
Finite tensor products of complete local bases are complete in the
product probability space: cylinder functions are dense, and each
finite-coordinate tensor space has this product basis. Moreover (5)
shows that the algebraic span of (10) equals the algebraic span of the
divisibility tails used as WP-442's form core. There is no missing
infinite-excitation sector in this Hilbert basis, although almost every
valuation configuration itself has infinitely many occupied primes.

Product polarization of (3) and (7) gives, on that common core,
\[
 \mathcal E(\Psi_m,\Psi_n)=\delta_{mn}\eta_n.
 \tag{11}
\]
Closure now determines the full domains. For \(g=\sum_n b_n\Psi_n\),
\[
 \begin{split}
 D(\mathcal E)&=\left\{g:\sum_n\eta_n|b_n|^2<\infty\right\},
 &\mathcal E[g]&=\sum_n\eta_n|b_n|^2,\\
 D(A)&=\left\{g:\sum_n\eta_n^2|b_n|^2<\infty\right\},
 &Ag&=\sum_n\eta_n b_n\Psi_n.
 \end{split}
 \tag{12}
\]
This proves (1) without exchanging an uncontrolled infinite operator sum.

If \(\eta_n=\eta_m\), their difference is a finite rational linear
combination of \(\log p\). Clearing denominators and unique
factorization force every coefficient to vanish. For each fixed prime,
the coefficient is \(0\) at exponent zero and
\(a+1/(p-1)\) at exponent \(a\ge1\), a strictly increasing function.
Hence \(n=m\). Since \(\eta_n\ge\log n\), there are only finitely
many eigenvalues below any fixed bound, proving compact resolvent and
compactness of \(e^{-tA}\) for every \(t>0\).

The smallest nonzero local eigenvalue is
\(p\log p/(p-1)\). The function \(x\log x/(x-1)\) is strictly
increasing for \(x>1\), since its derivative has numerator
\(x-1-\log x>0\). Thus the unique first excitation is \(n=2\),
and the sharp Poincare inequality is
\[
 \mathcal E[g]\ge2\log2\,\|g-\langle1,g\rangle1\|^2.
 \tag{13}
\]
Equality holds precisely in \(\operatorname{span}\{1,\Psi_2\}\).

## Heat trace and the critical boundary

For \(t>1\), comparison with \(\sum_n n^{-t}\) and the product
basis give
\[
 \begin{split}
 Z_A(t):=\operatorname{Tr}(e^{-tA})
 &=\prod_p\left(1+\frac{p^{-t/(p-1)}p^{-t}}{1-p^{-t}}\right)\\
 &=\zeta(t) B(t),\qquad
 B(t)=\prod_p\left[1-p^{-t}\left(1-p^{-t/(p-1)}\right)\right].
 \end{split}
 \tag{14}
\]
For \(0<t\le1\), the single-prime excitations alone have divergent
sum: their weights are \(p^{-t}e^{-t\log p/(p-1)}\), whose ratio to
\(p^{-t}\) is uniformly bounded below by a positive constant.
Reciprocal-prime divergence therefore proves the exact threshold.

The factors of \(B(t)\) are positive for real \(t>0\). Near \(t=1\),
\(1-B_p(t)\le t p^{-t}\log p/(p-1)\), a uniformly summable
majorant on any sufficiently small closed neighborhood of one. Hence
\[
 \lim_{t\downarrow1}(t-1)Z_A(t)
 =B(1)=\prod_p\left[1-\frac1p\left(1-p^{-1/(p-1)}\right)\right]
 \in(0,1).
 \tag{15}
\]
This pole is an ordinary positive-state-counting effect. In particular,
the conserved probability vector \(1\) at the critical KMS law does
not imply a finite heat trace at time one. The heat parameter in (14)
belongs to the prescribed Markov operator; it is not being identified
with the original Bost--Connes time evolution.

## Why diagonalization does not repair the Weil comparison

Let \(U:\ell^2(\mathbb N)\to\mathcal H\) send \(e_n\) to \(\Psi_n\).
Then
\[
 U^*AU=H+D_{\rm rad},\quad
 He_n=(\log n)e_n,\quad
 D_{\rm rad}e_n=\left(\sum_{p\mid n}\frac{\log p}{p-1}\right)e_n.
 \tag{16}
\]
This is an operator identity with the diagonal domains in (12).
But if \(M_p\) is the actual radial source projection multiplying by
\(1_{J_p\ge1}\), (4) gives
\[
 U^*M_pUe_1=\frac1p e_1+\frac{\sqrt{p-1}}p e_p.
 \tag{17}
\]
The standard integer projection \(E_pe_n=1_{p\mid n}e_n\) instead
annihilates \(e_1\). Thus (16) is not a unitary equivalence of the
pairs consisting of energy and source observables. It is consistent
with WP-442's stronger no-intertwiner statement for all divisibility
projections.

Subtracting \(D_{\rm rad}\) in these spectral coordinates would leave
\(H\ge0\), but it would be a different correction in a different
observable representation. It is not the scalar critical subtraction
on the old occupation core and does not preserve that core's
finite-Weil matrix. Nor does (14) supply a Weil explicit formula.
WP-442's actual shell matrix still contains its positive diagonal
completion alongside the desired off-diagonal entries.

All of (4)--(9) persists for arbitrary geometric parameters and positive
scales. Product eigenvalues are then sums over the active indices \(a_i\ge1\) of
\(\lambda_i(a_i+r_i/(1-r_i))\); simplicity and the particular heat
threshold require extra data and are not universal. This matched
nonarithmetic family explains the positivity and diagonalization while
separating the arithmetic contributions to (1) and (14). It does not
provide an alternative model satisfying a global Weil identity.

The remaining unsupported step is still a source-forced comparison
with the global Weil test form, including the completion terms, Gamma
contribution and polar normalization. The accepted completion clue
therefore remains open. This result closes the spectral classification
of the prescribed radial energy; it does not close every possible
critical completion or justify a further spectral reformulation as an
RH mechanism.

## Validation

An exact rational audit used \(r=1/2,1/3,1/5,2/5,3/4\), scale one,
and the finite partition \(\{0\},\ldots,\{13\},T_{14}\). The tail
bucket has its exact mass \(r^{14}\); upward rates into it are summed
geometrically, so this is an invariant finite quotient, not a zero
boundary truncation. All 75 constant/excitation eigenvectors satisfied
(7) exactly. Weighted orthogonality, norms, detailed balance, and every
pairing \(\mathcal E(h_a,h_b)=\min(a,b)r^{\max(a,b)}\) for
\(0\le a,b\le14\) also passed exactly.

A floating-point product audit used primes \(2,3,5,11\), local
excitation indices \(0\le a\le6\), and heat times
\(0.25,1,1.1,2,4\). Direct summation over the 2401 product modes
agreed with the product of local finite traces to maximum relative
error \(2.21\cdot10^{-16}\). These are normalization checks only;
completeness, the operator domains, simplicity, and the infinite heat
threshold follow from the proofs above.

## References

- [WP-442](WP-442-critical-valuation-product-supports-a-closed-log-gcd-energy.md), the closed form, divisibility core, local shell matrix, and representation boundary used here.
- [WP-441](WP-441-gibbs-minimal-diagonal-completion-has-divergent-critical-cost.md), the distinct Gibbs-cost and critical scalar-subtraction obstruction.
- A. Bendikov and P. Krupski, *On the spectrum of the hierarchical Laplacian*, Potential Analysis **41** (2014), 1247--1266, [DOI: 10.1007/s11118-014-9409-6](https://doi.org/10.1007/s11118-014-9409-6); [author preprint](https://arxiv.org/pdf/1308.4883), equations (1.3)--(1.5) and Section 3. Classical hierarchical operator and eigenfunction framework; the exact valuation specialization and its all-prime consequences are derived above.
