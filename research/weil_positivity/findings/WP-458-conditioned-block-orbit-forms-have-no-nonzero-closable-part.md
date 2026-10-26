---
title: "WP-458: Conditioned block orbit forms have no nonzero closable part"
type: research-finding
status: verified
research_question: "Can WP-457's conditioned block measures be realized as closable energies on the natural Maharam vacuum orbit domain?"
claim_strength: exact_nonclosability_and_zero_closable_minorant_for_the_specified_orbit_form
scope: product-conditioned dyadic models on the algebraic vacuum orbit domain; not arbitrary dense invariant domains
finding_id: WP-458
related_findings:
  - WP-453
  - WP-454
  - WP-456
  - WP-457
created: 2026-10-26
updated: 2026-10-26
tags:
  - weil-positivity
  - maharam-extension
  - prime-blocks
  - closability
  - singular-form
---

# WP-458: Block averaging detects a domain failure invisible to fixed prime moments

## Claim and evidence boundary

**EXACT-DERIVED; CLASSICAL FORM AND PROBABILITY INGREDIENTS;
OBSTRUCTION TO THE NATURAL ORBIT REALIZATION.** Fix \(c>0\) and
either of WP-457's product-conditioned dyadic prime measures
\(\mu^+\) or \(\mu^-\). The explicit vacuum-orbit map below
defines a nonzero positive covariant form on a dense invariant
domain in the fixed Maharam source. Its energy shifts retain the
chosen strict sign of every sufficiently late dyadic Weil block.
Nevertheless:

1. the orbit map is not closable;
2. its graph closure is the entire product of source and energy
   Hilbert spaces;
3. the only nonnegative closable form on this domain dominated
   by the constructed form is zero. In particular its maximal
   closable part is zero, and no closed extension can preserve
   its values on the domain.

The proof gives explicit finite analytic block averages whose
source norms vanish while their energy images converge to the
constant vector. They use only first prime powers, with growing
prime support. All bounded-support weak character tests of
WP-457 still pass in the joint unitary extension.

This answers the **specified orbit-domain realization** question,
not the existence of an arbitrary closable dense-range
intertwiner into WP-457's abstract unitary model. A different
domain need not contain the vacuum packets used here, and a
different map need not give them the conditioned product orbit
law. No general unbounded-block theorem, source-forced sign,
archimedean/polar completion or RH consequence is established.

## The conditioned blocks and an analytic first-harmonic test

Use WP-457's normalization, with normalized circle Haar measure:
\[
 B_j=\{p:2^j\le p<2^{j+1}\},\quad r_p=p^{-1/2},\quad
 V_j=2\sum_{p\in B_j}\frac{(\log p)^2}{p-1},
\]
\[
 X_j(z)=-\sum_{p\in B_j}(\log p)
                  \sum_{k\ge1}r_p^k(z_p^k+\bar z_p^k).
 \tag{1}
\]
For \(\varepsilon\in\{+1,-1\}\), let
\[
 A_j^\varepsilon=\{\varepsilon X_j\ge c\sqrt{V_j}\},\quad
 \pi_j^\varepsilon=m_{B_j}(A_j^\varepsilon),\quad
 d\mu_j^\varepsilon=\frac{1_{A_j^\varepsilon}}
                                  {\pi_j^\varepsilon}\,dm_{B_j}.
 \tag{2}
\]
WP-457's Berry--Esseen estimate gives
\(\pi_j^\varepsilon\to a_c=1-\Phi(c)>0\). Choose \(j_0\)
large enough that both probabilities are bounded below by a
fixed \(\pi_0>0\), and put
\[
 \mu^\varepsilon=m_{\{p<2^{j_0}\}}\otimes
                     \bigotimes_{j\ge j_0}\mu_j^\varepsilon.
 \tag{3}
\]
Increasing \(j_0\) below is harmless.

Define the analytic polynomial
\[
 a_j(z)=-\sum_{p\in B_j}b_pz_p,\qquad
 b_p=\frac{2\log p}{\sqrt{pV_j}}.
 \tag{4}
\]
The higher prime powers in (1) satisfy the uniform bound
\[
 \left|\frac{X_j}{\sqrt{V_j}}-\operatorname{Re}a_j\right|
 \le \delta_j:=\frac2{\sqrt{V_j}}
       \sum_{p\in B_j}\frac{\log p}{p(1-p^{-1/2})}.
 \tag{5}
\]
The prime number theorem and partial summation give
\[
 V_j\sim2(\log2)^2j,\qquad
 \sum_{p\in B_j}\frac{\log p}{p}\to\log2,\qquad
 \delta_j=O(j^{-1/2})\to0.
 \tag{6}
\]
For the middle relation, integrate \((\log t)/t\) against
\(d\pi(t)\) on \([2^j,2^{j+1})\); the main integral is
\(\int dt/t=\log2\). Replacing \(p\) by \(p-1\) in the
variance causes a vanishing error. No RH estimate is used.

Fix one sign and suppress it from \(\mu\). The numbers
\[
 m_j=\int a_j\,d\mu
 \tag{7}
\]
are real because (2) is invariant under simultaneous complex
conjugation. Equations (2) and (5) imply, for late enough \(j_0\),
\[
 \varepsilon m_j\ge c-\delta_j\ge c/2.
 \tag{8}
\]
Haar orthogonality and (2) also give
\[
 \int|a_j|^2\,d\mu
 \le\frac1{\pi_0}\sum_{p\in B_j}b_p^2
 =\frac4{\pi_0V_j}\sum_{p\in B_j}\frac{(\log p)^2}{p}
 \le\frac2{\pi_0}.
 \tag{9}
\]
Set
\[
 M_N=\sum_{j=j_0}^{j_0+N-1}m_j,\qquad
 P_N(z)=\frac1{M_N}\sum_{j=j_0}^{j_0+N-1}a_j(z).
 \tag{10}
\]
Here \(|M_N|\ge cN/2\). Distinct blocks are independent under
(3), although primes within a conditioned block are not. Thus
\[
 \|P_N-1\|_{L^2(\mu)}^2
 =\frac{\sum_j\int|a_j-m_j|^2\,d\mu}{|M_N|^2}
 \le\frac8{\pi_0c^2N}\to0.
 \tag{11}
\]
No asymptotic formula for the conditional means \(m_j\) is
required. Both signs give the limit one after normalization
by their own \(M_N\).

## The actual Maharam source sees the same averages vanish

Let
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(a)=(1-p^{-1})p^{-a},
\]
\[
 H_{\mathbb R}=L^2(\mathbb R,e^sds),\qquad
 \mathcal K=L^2(\Omega,\nu)\otimes H_{\mathbb R},
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\quad
 (U_ch)(s)=e^{-c/2}h(s-c),\quad W_p=V_p\otimes U_{\log p}.
 \tag{12}
\]
For \(h\in H_{\mathbb R}\), put \(f_h=1\otimes h\).
Distinct primes satisfy the exact pairing and its bound
\[
 \langle W_pf_h,W_qf_h\rangle
   =\frac1{\sqrt{pq}}\langle U_{\log p}h,U_{\log q}h\rangle,
 \qquad
 |\langle W_pf_h,W_qf_h\rangle|
   \le\frac{\|h\|^2}{\sqrt{pq}},
 \tag{13}
\]
whereas \(\|W_pf_h\|=\|h\|\). Define
\[
 L_j=\sum_{p\in B_j}\frac{b_p}{\sqrt p}
 =\frac2{\sqrt{V_j}}\sum_{p\in B_j}\frac{\log p}{p}
 =O(j^{-1/2}).
 \tag{14}
\]
All primes in (10) are distinct across blocks. Expanding the
source squared norm and using \(\sum_{p\in B_j}b_p^2\le2\),
(13), and (14) yields
\[
 \|P_N(W)f_h\|^2
 \le \frac{\|h\|^2}{|M_N|^2}
        \left(2N+\bigl(\sum_{j=j_0}^{j_0+N-1}L_j\bigr)^2\right)
 =O_{c,j_0}(N^{-1})\|h\|^2\to0.
 \tag{15}
\]
The squared sum overestimates the off-diagonal terms. This is an
upper bound, not orthogonality: the real translations have not
been discarded or declared independent.

## The dense orbit form and its complete graph collapse

Write \(V_n=\prod_pV_p^{v_p(n)}\) and
\[
 e_n=V_n1=\sqrt n\,1_{\{J_p\ge v_p(n)\ \forall p\}}.
\]
Finite families \(e_n\) are linearly independent: enlarge their
labels to a finite divisor-closed set and evaluate on the
positive-measure cylinders \(J_p=v_p(d)\) for primes appearing
in that set. The resulting divisibility-incidence matrix is
triangular with nonzero diagonal. Their span is dense since
differences of valuation-threshold indicators generate all
finite-coordinate cylinder functions.

On the dense invariant algebraic domain
\[
 \mathcal D_0=\operatorname{span}\{e_n\otimes h:
                       n\ge1,\ h\in H_{\mathbb R}\},
\]
define the well-defined linear map
\[
 T_\mu(e_n\otimes h)=z^{v(n)}\otimes U_{-\log n}h,\qquad
 Q_\mu(f,g)=\langle T_\mu f,T_\mu g\rangle.
 \tag{16}
\]
Its energy space is
\[
 E_\mu=\overline{\operatorname{Ran}T_\mu}
       =H^2(\mu)\otimes H_{\mathbb R},
 \tag{17}
\]
where \(H^2(\mu)\) is the \(L^2(\mu)\)-closure of analytic
polynomials on finitely many prime coordinates. It is not assumed
to be the full \(L^2(\mu)\). Directly,
\[
 T_\mu W_m=M_{z^{v(m)}}T_\mu,\qquad Q_\mu[W_mf]=Q_\mu[f].
 \tag{18}
\]
Indeed \(W_m(e_n\otimes h)=e_{mn}\otimes U_{\log m}h\), and
the real translations in (16) cancel exactly.
The energy shifts \(S_p\) are restrictions of \(M_{z_p}\), hence
commuting isometries. Define
\[
 D_{B,Q_\mu}=-\sum_{p\in B}(\log p)
                  \sum_{k\ge1}r_p^k(S_p^k+S_p^{*k}).
\]
With these **energy-space adjoints**, the norm-convergent ray
series obey, for every \(F\in E_\mu\),
\[
 \langle F,D_{B_j,Q_\mu}F\rangle
 =\int X_j(z)\|F(z)\|_{H_{\mathbb R}}^2\,d\mu(z),
 \qquad \varepsilon D_{B_j,Q_\mu}\ge c\sqrt{V_j}I.
 \tag{19}
\]
This needs only compression of the multiplication quadratic form;
it does not identify the energy adjoint with an unrestricted
multiplier.

But (11), (15), and (18) give, for every nonzero \(h\),
\[
 g_N=P_N(W)f_h\to0\quad\hbox{in }\mathcal K,\qquad
 T_\mu g_N=P_N\otimes h\to1\otimes h\ne0
                       \quad\hbox{in }E_\mu.
 \tag{20}
\]
Thus \(Q_\mu[g_N-g_M]\to0\) while \(Q_\mu[g_N]\to\|h\|^2>0\):
an explicit violation of the graph-sequence definition of
closability.

For a fixed analytic polynomial \(R\), both \(R(W)\) on the
source and \(M_R\) on the target are bounded. Multiplying (20)
by them puts every pair \((0,R\otimes h)\) in the graph
closure. These target vectors span a dense subspace of (17), so
the graph closure contains \(\{0\}\oplus E_\mu\). Subtracting
such vertical pairs from \((f,T_\mu f)\), then using density of
\(\mathcal D_0\), proves
\[
 \boxed{\overline{\operatorname{Graph}T_\mu}
                      =\mathcal K\oplus E_\mu.}
 \tag{21}
\]

The zero-minorant statement requires no decomposition theorem.
Suppose a nonnegative closable form \(q\) on \(\mathcal D_0\)
satisfies \(q\le Q_\mu\). By (21), for each \(f\in\mathcal D_0\)
there are \(u_N\in\mathcal D_0\) with \(u_N\to0\) in the
source and \(T_\mu u_N\to T_\mu f\). Then
\(q[u_N-u_M]\le Q_\mu[u_N-u_M]\to0\), so closability implies
\(q[u_N]\to0\). Also \(q[f-u_N]\to0\), whence the seminorm
triangle inequality gives \(q[f]=0\). The regular, closable
part on the stated domain is therefore zero.

## Audit, prior art and the remaining boundary

The construction preserves the exact finite Weil coefficients,
the source isometries and all-prime covariance. The joint
unitary extension is multiplication on \(L^2(\mu)\otimes
H_{\mathbb R}\), so WP-457's bounded-support weak character
limits remain valid there; weak convergence of analytic powers
also passes to the invariant energy subspace. These necessary
limits coexist with the complete graph failure (21).

No uniform bound on \(P_N(W)\) is asserted. Equation (15) is a
vector estimate on vacuum packets. It cannot be substituted into
WP-453's weak-intertwiner lemma on an arbitrary domain as an
operator convergence theorem. Product independence across
infinitely many blocks and the uniform second-moment bound (9)
are essential to (11). Finite-panel arc energies from WP-456
have no such sequence of independent escaping blocks and are
not contradicted. Global singularity of a measure alone would
not prove (21): WP-456 already supplies singular joint measures
in closed forms. The analytic averages are the additional
domain argument.

Yafaev's Theorem 1.3 treats one-variable Toeplitz forms, and
Proposition 3.1 with its following discussion separates
vanishing Fourier coefficients from closability. This is the
closest classical warning behind the weak-moment failure; no
infinite-variable extension of his theorem is used here.
Simon's Section 2 supplies the classical maximal-closable-part
framework; the zero-part assertion above is proved directly.
Block variance addition, the graph-sequence criterion and the
prime number theorem are standard. Searches on closable
multiplicative Toeplitz forms, product measures and singular
quadratic forms do not establish historical novelty.

The local delta from WP-457 is an actual dense-domain realization
of its block signs together with a proof that this natural
realization is entirely singular as an energy form. The failure
uses generic fresh-coordinate correlations and independent
conditioned blocks; it is not a Riemann-specific sign principle.
It closes the attempt to obtain a closed form merely by
completing this algebraic orbit construction, or by retaining
a nonzero closable part below it. A different source-derived
domain or correlated completion still needs its own theorem.

Validation is the exact argument (4)--(21), including both signs,
the omitted higher powers, actual real translations, and the
possibly proper analytic energy subspace. No finite numerical
sample is used to infer an infinite-dimensional limit. No Lean
formalization or independent adversarial approval is claimed.

## References

- [WP-457](WP-457-dyadic-sign-conditioning-preserves-all-bounded-support-weak-prime-moments.md), conditioned block measures, their nonvanishing probabilities and weak character limits.
- [WP-453](WP-453-closability-forbids-infinite-prime-ray-orientation.md), fixed Maharam source, closable-intertwiner boundary and the separate-ray obstruction.
- [WP-454](WP-454-bounded-covariant-energies-retain-negative-dyadic-prime-blocks.md), bounded-energy obstruction and the same block normalization.
- [WP-456](WP-456-closed-singular-arc-traces-can-select-either-finite-weil-sign.md), closed singular finite-panel controls.
- D. R. Yafaev, *On semibounded Toeplitz operators*, Journal of Operator Theory **77** (2017), 205--216, Theorem 1.3 and Proposition 3.1, [journal text](https://jot.theta.ro/jot/archive/2017-077-001/2017-077-001-012.pdf).
- B. Simon, *A canonical decomposition for quadratic forms with applications to monotone convergence theorems*, Journal of Functional Analysis **28** (1978), 377--385, Section 2, [DOI](https://doi.org/10.1016/0022-1236(78)90094-0), [original-paper scan](https://www.tu-chemnitz.de/mathematik/analysis/kalmes/DAAD_Tunesien_2014_Simon.pdf).
- NIST Digital Library of Mathematical Functions, [equation 27.2.3](https://dlmf.nist.gov/27.2.E3), the prime number theorem used in (6).
