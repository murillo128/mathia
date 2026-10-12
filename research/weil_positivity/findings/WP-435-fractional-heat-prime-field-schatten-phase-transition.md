---
title: "WP-435: Fractional-Hamiltonian heat regularizes the critical prime field with a sharp Schatten phase transition"
type: research-finding
status: verified
research_question: "Does fractional heat smoothing of the nonclosable coanalytic Bost--Connes prime field yield a noncompact or Schatten-finite positive completion that can change the Weil sign?"
claim_strength: exact_fractional_heat_compactness_all_positive_orders_and_schatten_trichotomy
scope: standard positive-energy Bost--Connes representation on l2(N); coanalytic prime field with logarithmic half-density coefficients; positive fractional Hamiltonian heat; no conclusion about genuinely noncompact relative completions, cancellations before smoothing, other representations, or global archimedean normalization
finding_id: WP-435
related_findings:
  - WP-434
  - WP-433
  - WP-432
  - WP-218
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-12
updated: 2026-10-12
tags:
  - weil-positivity
  - bost-connes
  - fractional-heat
  - coanalytic
  - compactness
  - schatten
  - spectral-counting
  - essential-spectrum
---

# WP-435: Fractional-Hamiltonian heat gives a sharp Schatten phase transition without a Weil sign

## Exact claim and evidence

**EXACT-DERIVED; NEGATIVE/OPERATOR-CATEGORY CLASSIFICATION.** In the standard positive-energy representation \(\mathcal H=\ell^2(\mathbb N)\), set
\[
\mu_p e_n=e_{pn},\qquad He_n=(\log n)e_n,\qquad
R_a e_m=\sum_{p\mid m}\overline{a_p}\,e_{m/p}
\quad(m\in\mathbb N)
\]
on \(c_{00}(\mathbb N)\). For \(\kappa\geq0\), let
\[
a_{\kappa,p}=(\log p)^\kappa p^{-1/2},\qquad
B_{\kappa,\alpha,t}
=R_{a_\kappa}e^{-tH^\alpha}\big|_{c_{00}},
\quad\alpha,t>0.
\tag{1}
\]
Every \(B_{\kappa,\alpha,t}\) has a **bounded compact extension**, for every positive \(\alpha,t\). For each finite Schatten order \(q>0\), its precise membership is
\[
\boxed{
B_{\kappa,\alpha,t}\in\mathcal S_q
\iff
\begin{cases}
\text{never},&0<\alpha<1,\\
qt>1,&\alpha=1,\\
\text{always},&\alpha>1.
\end{cases}}
\tag{2}
\]
Here "never" and "always" mean for every fixed \(q\in(0,\infty)\); there is no dependence on \(\kappa\) in this phase boundary. In particular, fractional orders \(0<\alpha<1\) furnish compact operators outside **every finite Schatten class**. For the positive energy \(K=B^*B\), the same trichotomy holds with \(q\) replaced by \(2q\) in the middle threshold: \(K\in\mathcal S_q\iff B\in\mathcal S_{2q}\).

As \(t\downarrow0\), \(\|B_{\kappa,\alpha,t}\|\to\infty\) for every fixed \(\alpha>0\). At each fixed positive \(t\), its compact positive energy does not remove the negative essential Weil prime-ray interval from WP-218. Thus neither stronger heat nor a fractional weakening supplies an independently oriented global Weil sign.

## Compactness from the logarithmic power theorem

Choose \(s>\max\{1,2\kappa\}\). WP-434 proves that
\[
C_{\kappa,s}:=
R_{a_\kappa}(1+H)^{-s/2}\big|_{c_{00}}
\]
extends to a bounded compact operator on \(\mathcal H\). On basis vectors, the exact factorization is
\[
B_{\kappa,\alpha,t}
=C_{\kappa,s}\,A_{\alpha,t,s},\qquad
A_{\alpha,t,s}=(1+H)^{s/2}e^{-tH^\alpha},
\tag{3}
\]
initially on \(c_{00}\). The diagonal entries of \(A\) are
\[
d_n=(1+\log n)^{s/2}\exp[-t(\log n)^\alpha].
\tag{4}
\]
For each \(\alpha,t>0\), \(d_n\) is bounded and tends to zero because every positive power of \(\log n\) is dominated by \(\exp[t(\log n)^\alpha]\). Thus \(A\) is bounded (indeed compact) and (3) supplies the claimed compact extension, with no unlicensed exchange of infinite prime sums.

## Schatten sufficiency and necessity

The diagonal operator \(A\) belongs to \(\mathcal S_q\) precisely when
\[
\sum_{n\ge1}(1+\log n)^{sq/2}
                e^{-qt(\log n)^\alpha}<\infty.
\tag{5}
\]
For \(\alpha=1\), this is \(\sum_n n^{-qt}(1+\log n)^{sq/2}\), convergent exactly for \(qt>1\). For \(\alpha>1\), it converges for every finite \(q>0\) because its terms are eventually bounded by \(n^{-2}\); for \(0<\alpha<1\) the diagonal series itself diverges for every finite \(q\). The two-sided ideal property of the Schatten classes, including their quasi-ideal range \(0<q<1\), and (3) establish sufficiency in the first two convergent regimes.

To see that there is no cancellation loophole in the necessity, fix any prime \(p\) and let \(P_p^{\mathrm{in}}\) project onto the span of \(e_{pn}\) with \((n,p)=1\), while \(P_p^{\mathrm{out}}\) projects onto the span of \(e_n\) with \((n,p)=1\). For \(n\) coprime to \(p\), only the \(p\)-divisor term survives this compression: any term from a prime \(r\mid n\) still contains \(p\). Consequently
\[
P_p^{\mathrm{out}}B_{\kappa,\alpha,t}P_p^{\mathrm{in}}
(e_{pn})
=\overline{a_{\kappa,p}}\,
e^{-t(\log(pn))^\alpha}e_n,
\quad (n,p)=1.
\tag{6}
\]
Its nonzero singular values are therefore **exactly**
\[
|a_{\kappa,p}|e^{-t(\log(pn))^\alpha},
\quad n\ge1,\ (n,p)=1.
\tag{7}
\]
Since the integers coprime to \(p\) have positive density, the series of their \(q\)th powers diverges if \(0<\alpha<1\) (the summands eventually dominate a positive multiple of \(n^{-1}\)) and if \(\alpha=1,\ qt\le1\) (harmonic or slower). Any compression of an \(\mathcal S_q\) operator must belong to \(\mathcal S_q\), including for \(q<1\). Equations (5)--(7) prove the sharp classification (2). The case \(\alpha=1,\ q=2\) agrees with the exact Hilbert--Schmidt threshold in WP-433.

## Critical limit and essential-sign obstruction

The vacuum row already gives
\[
\|B_{\kappa,\alpha,t}\|
\geq\|B_{\kappa,\alpha,t}^*e_1\|
=\left(\sum_p\frac{(\log p)^{2\kappa}}p
             e^{-2t(\log p)^\alpha}\right)^{1/2}.
\tag{8}
\]
The series is finite for each \(t>0\) and increases monotonically to
\(\sum_p(\log p)^{2\kappa}/p=\infty\) as \(t\downarrow0\), by the prime number theorem (the \(\kappa=0\) endpoint is the familiar reciprocal-prime divergence). A scalar rescaling that kept the family uniformly bounded would consequently suppress each fixed-prime coefficient.

For each fixed \(\alpha,t>0\), \(K_{\kappa,\alpha,t}=B^*B\) is positive compact. If \(P_p\) denotes projection onto the prime-power ray, then \(P_pKP_p\) is compact, whereas WP-218 proves that the unchanged self-adjoint Weil defect
\[
W_p=(\log p)\bigl(I-T(P_{p^{-1/2}})\bigr)
\]
has negative essential spectrum, with
\[
\inf\sigma_{\rm ess}(W_p)
=-\frac{2(\log p)p^{-1/2}}{1-p^{-1/2}}<0.
\tag{9}
\]
Weyl invariance therefore gives \(W_p+P_pKP_p\not\succeq0\). This argument excludes **additive compact positive-energy repairs of the unchanged ray**. It does not exclude a noncompact, cancellation-bearing, differently represented, or coupled finite--archimedean construction that changes the operator before the ray reduction.

## Novelty, controls, and consequence

The underlying prime shifts/Hamiltonian come from Bost--Connes (1995), and the Dirichlet-series Hilbert model is classical (Hedenmalm--Lindqvist--Seip, 1997). Schatten ideal theory is standard (Simon, *Trace Ideals and Their Applications*, 2nd ed., 2005); Bayart--Kouroupis (2024) investigate Schatten composition operators on Hardy--Dirichlet space, a **different operator family**, not this coanalytic field. These sources and their respective roles are recorded in the local SOURCES.md. The argument is an elementary consequence of the compact logarithmic-power bound in WP-434, two-sided Schatten ideal properties, and a single-prime compression; it claims neither a new general operator theorem nor RH progress.

The mathematical delta is the exact **three-phase Schatten boundary** for the surviving fractional-heat regularization question: all positive powers regularize into compactness, sublinear heat power remains in no finite Schatten class, ordinary heat has the sharp \(qt=1\) boundary, and superlinear heat belongs to all finite classes. The failure for \(0<\alpha<1\) is controlled by the ambient integer spectral-counting density on a fixed nonzero prime channel, not by zeta-zero data or a special Weil sign. The matched-control warning is therefore explicit: compactness and trace-ideal thresholds alone cannot certify source-selective arithmetic positivity.

The required global ingredients remain unconstructed: canonical all-prime Mangoldt weights, an archimedean Gamma term, polar normalization, and a nonnegative form whose sign is forced independently of the Weil target. This closes a regulator-regularity branch of the accepted Bost--Connes completion clue, not that clue's remaining noncompact/cross-sector possibilities.

## References

- research/weil_positivity/findings/WP-434-logarithmic-coanalytic-prime-smoothing-compactness-without-schatten-gain.md
- research/weil_positivity/findings/WP-433-thermal-coanalytic-prime-regularization-is-compact-and-sign-inert.md
- research/weil_positivity/findings/WP-432-coanalytic-prime-field-is-dense-but-nonclosable-at-critical-half-density.md
- research/weil_positivity/findings/WP-218-bost-connes-weil-defect-has-negative-essential-spectrum-stable-under-compact-completion.md
- research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md
- research/weil_positivity/SOURCES.md
