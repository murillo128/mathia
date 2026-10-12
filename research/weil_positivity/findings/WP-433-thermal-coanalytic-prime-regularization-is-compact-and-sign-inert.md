---
title: "WP-433: Thermal coanalytic prime regularization is compact but sign-inert"
type: research-finding
status: verified
research_question: "Does source-Hamiltonian heat damping turn the nonclosable critical coanalytic prime field of WP-432 into a usable positive Bost--Connes/Weil completion?"
claim_strength: exact_thermal_coanalytic_closability_compactness_and_hilbert_schmidt_threshold_with_essential_sign_no_go
scope: standard positive-energy Bost--Connes representation on l2(N); heat-preconditioned minimal coanalytic prime field; no statement about mixed cancellation before regularization, noncompact global extensions, other GNS sectors, or archimedean normalization
finding_id: WP-433
related_findings:
  - WP-432
  - WP-431
  - WP-218
  - WP-216
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-12
updated: 2026-10-12
tags:
  - weil-positivity
  - bost-connes
  - heat-regularization
  - coanalytic
  - compactness
  - hilbert-schmidt
  - closability
  - essential-spectrum
---

# WP-433: Thermal coanalytic prime regularization is compact but sign-inert

## Exact claim and evidence

**EXACT-DERIVED; NEGATIVE/OBSTRUCTION.** On \(\mathcal H=\ell^2(\mathbb N)\), let
\[
\mu_p e_n=e_{pn},\qquad H e_n=(\log n)e_n,\qquad
D_t=e^{-tH},\quad D_t e_n=n^{-t}e_n .
\]
For arbitrary complex prime coefficients \(a=(a_p)\), take the minimal coanalytic field from WP-432,
\[
R_a e_m=\sum_{p\mid m}\overline{a_p}\,e_{m/p}
\quad\text{on }c_{00}(\mathbb N),
\]
and, for a **fixed \(t>0\)**, form the densely defined, heat-preconditioned operator
\(B_{a,t}=R_aD_t|_{c_{00}}\). Set \(b_p=a_pp^{-t}\). Then the following conditions are equivalent:
\[
\boxed{\;
B_{a,t}\ \text{is closable}
\iff B_{a,t}\ \text{extends boundedly}
\iff B_{a,t}\ \text{extends compactly}
\iff \sum_p|a_p|^2p^{-2t}<\infty .\;}
\tag{1}
\]
When the sum diverges, even the positive quadratic form
\(f\mapsto\|B_{a,t}f\|^2\) on \(c_{00}\) is nonclosable.

For nonzero \(a\), the resulting compact extension is Hilbert--Schmidt **exactly** when
\[
\boxed{t>\tfrac12\quad\text{and}\quad
\sum_p|a_p|^2p^{-2t}<\infty,}
\qquad
\|B_{a,t}\|_{\mathcal S_2}^2
=\zeta(2t)\sum_p|a_p|^2p^{-2t}.
\tag{2}
\]
The zero field is Hilbert--Schmidt for every \(t>0\).

At the Bost--Connes critical half-density \(a_p=p^{-1/2}\), and also for the Weil-log-weighted field \(a_p=(\log p)/\sqrt p\), (1) holds for **every \(t>0\)**. The heat regulator thus genuinely creates a bounded compact positive energy \(K_t=B_{a,t}^*B_{a,t}\), even though the undamped field is nonclosable by WP-432. However, the regularized operators cannot remain uniformly bounded as \(t\downarrow0\), and for every fixed \(t>0\) their positive compact energies cannot correct the negative essential prime-ray spectrum of WP-218. This is a precise regularization mechanism, **not** an independently derived Weil sign.

## Derivation: a sharp prime-row bound

The coefficient action is
\[
(B_{a,t}f)(n)
=\sum_p\overline{a_p}(np)^{-t}f(np)
=n^{-t}\sum_p\overline{b_p}f(np).
\tag{3}
\]
Every sum is finite on \(c_{00}\). Suppose \(b\in\ell^2(\mathbb P)\). Cauchy--Schwarz gives
\[
\|B_{a,t}f\|_2^2
\le\|b\|_{\ell^2(\mathbb P)}^2
\sum_{n\ge1}n^{-2t}\sum_p|f(np)|^2
=\|b\|_2^2\sum_{m\ge1}|f(m)|^2
\underbrace{\sum_{p\mid m}(m/p)^{-2t}}_{Q_t(m)}.
\tag{4}
\]
If \(r=\omega(m)\) is the number of distinct prime divisors of \(m\), then for each \(p\mid m\), the integer \(m/p\) is divisible by the other \(r-1\) distinct primes and hence is at least \(2^{r-1}\). Consequently
\[
Q_t(m)\le r\,2^{-2t(r-1)}
\le C_t:=\sup_{r\ge1}r\,2^{-2t(r-1)}<\infty
\qquad(t>0).
\tag{5}
\]
Thus
\[
\boxed{\ \|B_{a,t}\|\le C_t^{1/2}\|b\|_2\ .\ }
\tag{6}
\]
This proves bounded extension without assuming that the formal analytic prime multiplier is bounded.

For any finite prime set \(F\), the truncated \(B_{a,t,F}\) is a finite sum of \(\overline{a_p}\mu_p^*D_t\). Each summand is compact: it maps \(e_{pn}\) to \((pn)^{-t}e_n\) and vanishes on integers not divisible by \(p\); its nonzero singular weights tend to zero as \(n\to\infty\). The same estimate (6) applied to the complementary coefficient family gives
\[
\|B_{a,t}-B_{a,t,F}\|
\le C_t^{1/2}\Big(\sum_{p\notin F}|b_p|^2\Big)^{1/2}
\longrightarrow0.
\tag{7}
\]
The bounded extension is therefore a norm limit of compact operators, hence compact.

Conversely, suppose \(\sum_p|b_p|^2=\infty\). For finite \(F\), put
\[
S_F=\sum_{p\in F}|b_p|^2,\qquad
x_F=S_F^{-1}\sum_{p\in F}b_p e_p .
\]
Since \(B_{a,t}e_p=\overline{b_p}e_1\),
\[
\|x_F\|_2^2=S_F^{-1},\qquad B_{a,t}x_F=e_1.
\tag{8}
\]
Choosing \(F\) with \(S_F\to\infty\) gives \(x_F\to0\) but \(B_{a,t}x_F=e_1\), so the operator is not closable. Moreover \(B_{a,t}(x_F-x_G)=0\) while \(\|B_{a,t}x_F\|^2=1\): its norm-square quadratic form is not closable. This proves the necessity in (1).

## Hilbert--Schmidt and the critical limit

For each \(m\), the images indexed by distinct divisors \(p\mid m\) are orthogonal, so
\[
\|B_{a,t}e_m\|_2^2=m^{-2t}\sum_{p\mid m}|a_p|^2.
\]
Tonelli's theorem and \(m=pn\) yield the **exact** extended-real identity
\[
\sum_{m\ge1}\|B_{a,t}e_m\|_2^2
=\Big(\sum_{n\ge1}n^{-2t}\Big)
 \Big(\sum_p|a_p|^2p^{-2t}\Big).
\tag{9}
\]
For \(a\ne0\), the first factor is finite precisely when \(t>1/2\). This proves (2); it also distinguishes compactness on the full interval \(t>0\) from the stronger trace-class condition on \(K_t\), which holds exactly when \(t>1/2\) and (1) holds.

For the thermal critical family \(a_p=p^{-1/2}\),
\[
\|B_{a,t}\|\ge\|B_{a,t}^*e_1\|_2
=\Big(\sum_p p^{-1-2t}\Big)^{1/2}
\longrightarrow\infty\quad(t\downarrow0).
\tag{10}
\]
The logarithmically amplified family also satisfies (1) for every positive \(t\), with the lower bound \((\sum_p(\log p)^2p^{-1-2t})^{1/2}\to\infty\). Equation (10) follows simply from the classical divergence of \(\sum_p1/p\); there is no appeal to RH. For each finitely supported \(f\), \(B_{a,t}f\to R_af\), but the compact extensions do **not** converge strongly on all of \(\ell^2\) to a bounded operator, by uniform boundedness.

Likewise, any scalar normalization that holds \(\|B_{a,t}/\lambda_t\|\) uniformly bounded as \(t\downarrow0\) must have \(|\lambda_t|\to\infty\). It then erases every fixed-prime matrix coefficient \(\overline{a_p}p^{-t}/\lambda_t\to0\). Merely removing the regulator or dividing out its growing norm cannot retain the original critical source amplitudes in a uniformly bounded limit.

## Why the positive energy still cannot orient Weil

For \(t>0\) satisfying (1), \(K_t=B_{a,t}^*B_{a,t}\) is bounded, positive, and compact. Let \(P_p\) project onto the closed prime-power ray
\(\mathcal H_p=\overline{\operatorname{span}}\{e_{p^k}:k\ge0\}\).
Then \(P_pK_tP_p|_{\mathcal H_p}\) is a positive compact operator. In contrast, WP-218 identifies the independently source-forced critical defect there as
\[
W_p=(\log p)\big(I-T(P_{p^{-1/2}})\big),\qquad
\inf\sigma_{\mathrm{ess}}(W_p)
=-\frac{2(\log p)p^{-1/2}}{1-p^{-1/2}}<0.
\tag{11}
\]
Weyl invariance of essential spectrum therefore gives
\[
\boxed{\quad W_p+P_pK_tP_p|_{\mathcal H_p}
\not\succeq0\quad\text{for every fixed }t>0 .\quad}
\tag{12}
\]
The same holds for any bounded compact function of these regularized positive energies that is proposed as an additive prime-ray correction. This does not rule out noncompact interacting completions, operations that destroy the standalone prime-ray channel, or singular renormalized limits outside the compact/norm topology.

## Prior art, controls, and conclusion

The Bohr--Hardy realization of prime shifts is classical (Hedenmalm--Lindqvist--Seip, 1997); Bost--Connes (1995) supplies the multiplicative Hamiltonian; Fernández Vidal--Galicer--Sevilla-Peris (2025, DOI 10.5802/aif.3658) study Hardy--Dirichlet multiplier operators; and compactness, adjoint closability, Hilbert--Schmidt ideals, and Weyl's theorem are classical. All are already anchored in the local SOURCES.md and WP-431/WP-432/WP-218. No new general operator theorem, archimedean explicit-formula identity, or RH progress is claimed. The line-specific delta is the exact **thermal escape-and-recollapse classification**: positive heat time repairs the coanalytic field in a compact category, with a sharp Hilbert--Schmidt threshold, but the zero-time limit is singular and its fixed-time energy cannot alter the wrong essential Weil orientation.

A matched free-multiplicative-generator model with generator weights uniformly bounded below by a number greater than one obeys the same prime-row estimate. The bounded/compact mechanism is therefore not arithmetic-specific positivity; it uses decay, countable orthogonal shift geometry, and the absence of accumulation of generator weights at one. It neither recovers the global Mangoldt prime-power selector nor builds the archimedean Gamma and polar counterterms. A genuine surviving Weil route requires a separately source-forced, noncompact finite--archimedean operation or a different justified operator/form category whose sign theorem comes before the arithmetic target is imposed.

## References

- research/weil_positivity/findings/WP-432-coanalytic-prime-field-is-dense-but-nonclosable-at-critical-half-density.md
- research/weil_positivity/findings/WP-431-critical-prime-coherent-semigroup-field-has-a-sharp-kms-domain-collapse.md
- research/weil_positivity/findings/WP-218-bost-connes-weil-defect-has-negative-essential-spectrum-stable-under-compact-completion.md
- research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md
- research/weil_positivity/SOURCES.md
