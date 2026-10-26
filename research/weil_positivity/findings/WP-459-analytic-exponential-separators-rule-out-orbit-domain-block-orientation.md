---
title: "WP-459: Analytic exponential separators rule out orbit-domain block orientation"
type: research-finding
status: verified
research_question: "Can correlations or a different energy readout repair variance-scale dyadic sign selection while retaining the natural Maharam orbit domain?"
claim_strength: exact_orbit_domain_nonclosability_without_product_measure_or_moment_assumptions
scope: uniform variance-scale margins on all late dyadic blocks and domains containing the vacuum orbit; not arbitrary dense domains
finding_id: WP-459
related_findings:
  - WP-453
  - WP-454
  - WP-456
  - WP-457
  - WP-458
created: 2026-10-26
updated: 2026-10-26
tags:
  - weil-positivity
  - maharam-extension
  - prime-blocks
  - closability
  - analytic-separation
---

# WP-459: Correlating the blocks does not repair a sign-oriented orbit energy

## Claim and evidence boundary

**EXACT-DERIVED; CLASSICAL EXPONENTIAL-MOMENT AND CLOSED-GRAPH
INGREDIENTS; DOMAIN OBSTRUCTION.** On the fixed Maharam source
below, let a nonnegative sesquilinear form \(Q\) have a domain
\(\mathcal D\) containing the algebraic vacuum orbit
\(\mathcal D_0\). Assume all-prime forward invariance and covariance
\(Q[W_pf]=Q[f]\). Let \(S_p\) be the induced commuting
isometries on its energy completion \(E_Q\), and put
\[
 B_j=\{p:2^j\le p<2^{j+1}\},\qquad
 V_j=2\sum_{p\in B_j}\frac{(\log p)^2}{p-1},
\]
\[
 D_{B_j,Q}=-\sum_{p\in B_j}(\log p)
             \sum_{k\ge1}p^{-k/2}(S_p^k+S_p^{*k}).       \tag{1}
\]
Adjoints here and throughout are **energy-space adjoints**.
Suppose there are \(c>0\), \(j_0\), and one fixed
\(\varepsilon\in\{1,-1\}\) such that
\[
 \varepsilon D_{B_j,Q}\ge c\sqrt{V_j}\,I
                  \quad(j\ge j_0).                    \tag{2}
\]
Then:

1. if \(Q\) is closable in the original source norm, \(Q=0\);
2. if \(\mathcal D=\mathcal D_0\), the quotient map
   \(T:f\mapsto[f]\in E_Q\) satisfies
   \(\overline{\operatorname{Graph}T}=\mathcal K\oplus E_Q\);
   every nonnegative closable form on \(\mathcal D_0\) dominated
   by \(Q\) is zero.

There is no product-measure, independence-between-blocks,
uniform-energy-moment, phase-invariance, or energy-unitarity
assumption. In particular, arbitrary couplings of WP-457's
conditioned block marginals cannot repair WP-458's natural orbit
realization. More generally, any finite nonzero measure supported
where all the late block inequalities (2) hold has the same
entirely singular natural orbit form.

The material change from WP-458 is an operator-level separator
uniform over the sign-oriented energy space, replacing its
product-law averaging argument. The **domain inclusion** and
**strict variance-scale margin** remain hypotheses. This does
not settle arbitrary dense invariant domains that omit the
vacuum packets, mere block nonnegativity, or a Weil form completed
by mixed-prime, archimedean and polar terms. No RH consequence,
historical novelty, Lean verification or independent adversarial
approval is claimed.

## Source and domain

Use normalized critical valuation measure and the real Maharam
coordinate:
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(a)=(1-p^{-1})p^{-a},
\]
\[
 H_{\mathbb R}=L^2(\mathbb R,e^sds),\quad
 \mathcal K=L^2(\Omega,\nu)\otimes H_{\mathbb R},
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\quad
 (U_ch)(s)=e^{-c/2}h(s-c),\quad W_p=V_p\otimes U_{\log p}.
                                                               \tag{3}
\]
These are commuting isometries. For \(n\ge1\), write
\(V_n=\prod_pV_p^{v_p(n)}\), \(W_n=V_n\otimes U_{\log n}\),
\(e_n=V_n1\), and \(f_h=1\otimes h\). The domain is
\[
 \mathcal D_0=\operatorname{span}\{e_n\otimes h:
                   n\ge1,\ h\in H_{\mathbb R}\}
 =\operatorname{span}\{W_nf_h:n\ge1,\ h\in H_{\mathbb R}\}.
                                                               \tag{4}
\]
It is dense and invariant: valuation-threshold indicators generate
the finite-coordinate cylinder functions, and the real translations
are onto. Finite families \(e_n\) are linearly independent by the
triangular divisibility-incidence matrix on a finite divisor
closure, as in WP-458.

Covariance and polarization make \(S_pTf=TW_pf\) isometric
on the quotient, without requiring \(Q\) to be closable. For a
closable \(Q\), its quotient map \(T\) is closable because the
two graph-sequence definitions coincide.

## From the whole ray to a first-harmonic half-plane

For a tuple of isometries \(Z=(Z_p)\), set
\[
 a_j(Z)=-\sum_{p\in B_j}b_pZ_p,\qquad
 b_p=\frac{2\log p}{\sqrt{pV_j}}.
                                                               \tag{5}
\]
The coefficients depend on the unique block containing \(p\).
The geometric tail of (1), using only \(\|S_p^k\|=1\), gives
\[
 \left\|D_{B_j,Q}/\sqrt{V_j}-\operatorname{Re}a_j(S)\right\|
 \le\delta_j:=\frac2{\sqrt{V_j}}
       \sum_{p\in B_j}\frac{\log p}{p(1-p^{-1/2})}.
                                                               \tag{6}
\]
The prime number theorem and partial summation yield
\[
 V_j\sim2(\log2)^2j,\quad
 \sum_{p\in B_j}\frac{\log p}{p}\longrightarrow\log2,
 \quad\delta_j=O(j^{-1/2}).                               \tag{7}
\]
These are the same unconditional estimates as WP-457--WP-458.
For example, the two leading integrals are
\(2\int_{2^j}^{2^{j+1}}(\log t)/t\,dt\) and
\(\int_{2^j}^{2^{j+1}}dt/t\). The errors from replacing
\(p-1\) by \(p\) tend to zero. Also
\[
 \sum_{p\in B_j}b_p^2\le2,\qquad
 L_j:=\sum_{p\in B_j}\frac{b_p}{\sqrt p}=O(j^{-1/2}).     \tag{8}
\]
Increase \(j_0\) so that \(\delta_j\le c/2\). Hypothesis
(2) then implies the operator inequality
\[
 \operatorname{Re}(\varepsilon a_j(S))\ge(c/2)I
                 \quad(j\ge j_0).                      \tag{9}
\]
No joint spectral measure is used in this step.

## Exponential tests are small on the actual source vacuum

We first prove a finite coefficient estimate, retaining the real
translations. For a finite prime set \(F\), numbers \(d_p\ge0\),
and \(\varepsilon=\pm1\), define
\[
 C(W)=\sum_{p\in F}d_pW_p,\quad
 L=\sum_{p\in F}d_pp^{-1/2},\quad K=\sum_{p\in F}d_p^2.
\]
Then
\[
 \|(e^{\varepsilon C(W)}-I)f_h\|^2
 \le\bigl(e^{2L+2K}-2e^L+1\bigr)\|h\|^2.              \tag{10}
\]
To see this, for multiindices \(\alpha,\beta\) on \(F\),
put \(n_\alpha=\prod p^{\alpha_p}\). Directly from (3),
\[
 \langle W^{\alpha}f_h,W^{\beta}f_h\rangle
 =\prod_{p\in F}p^{-|\alpha_p-\beta_p|/2}
   \langle U_{\log n_\alpha}h,U_{\log n_\beta}h\rangle.
                                                               \tag{11}
\]
Taking absolute values bounds the second factor by \(\|h\|^2\).
The absolute Taylor coefficients of \(e^{\varepsilon C}-1\)
are exactly those of \(e^C-1\). The resulting nonnegative
double sum is
\[
 \|h\|^2\int\left|e^{\sum d_pz_p}-1\right|^2d\rho_F(z),
 \quad
 d\rho_F=\prod_{p\in F}
       \frac{1-p^{-1}}{|1-z_p/\sqrt p|^2}\,dm(z_p).       \tag{12}
\]
Here \(m\) is normalized Haar measure. All series converge
absolutely, since \(F\) is finite. The auxiliary Poisson law
is a **source upper bound**, not an assertion about the energy
measure or the real-coordinate correlations.

Its analytic moments give
\(\int e^{\sum d_pz_p}\,d\rho_F=e^L\). The variables
\(X_p=\operatorname{Re}z_p\) are independent under \(\rho_F\),
lie in \([-1,1]\), and have mean \(p^{-1/2}\). Hoeffding's
bounded-variable exponential estimate gives
\[
 \int e^{2\sum d_pX_p}\,d\rho_F\le e^{2L+2K}.
\]
For completeness, if \(X\in[-1,1]\),
\(F(t)=\log\mathbb E e^{t(X-\mathbb EX)}\) has
\(F(0)=F'(0)=0\) and \(F''(t)\le1\): its second derivative
is a variance under exponential tilt, still supported on
\([-1,1]\). Thus \(F(t)\le t^2/2\); apply this at
\(t=2d_p\) and multiply. Expanding (12) now proves (10).

For the consecutive blocks \(j_0\le j<j_0+N\), take
\[
 t_N=N^{-3/4},\quad d_p=t_Nb_p,\quad
 A_N(Z)=\varepsilon t_N\sum_{j=j_0}^{j_0+N-1}a_j(Z).
                                                               \tag{13}
\]
Thus \(-A_N(W)=\varepsilon C(W)\). By (8),
\[
 L=O(t_N\sqrt N)=O(N^{-1/4}),\qquad
 K\le2Nt_N^2=2N^{-1/2}.
\]
Since
\(e^{2L+2K}-2e^L+1=(e^L-1)^2+e^{2L}(e^{2K}-1)\),
(10) gives
\[
 \|(I-e^{-A_N(W)})f_h\|^2
           =O(N^{-1/2})\|h\|^2\longrightarrow0.         \tag{14}
\]

## The same tests converge to the identity in every oriented energy

By (9),
\[
 \operatorname{Re}A_N(S)\ge(c/2)Nt_NI.
\]
If a bounded operator \(A\) satisfies \(\operatorname{Re}A\ge\gamma I\),
differentiating \(\|e^{-uA}v\|^2\) gives a derivative at most
\(-2\gamma\|e^{-uA}v\|^2\). Hence
\(\|e^{-A}\|\le e^{-\gamma}\), with no normality assumption.
Consequently
\[
 \|e^{-A_N(S)}\|\le e^{-(c/2)N^{1/4}}\longrightarrow0.  \tag{15}
\]

Exponential images need not lie in the original algebraic domain,
so replace them by polynomials **before** testing closability.
For each fixed \(N\), choose a Taylor degree \(k_N\) so large
that the absolute exponential tail at
\(M_N=\sum_{p\in\cup_{j=j_0}^{j_0+N-1}B_j}d_p<\infty\)
is at most \(N^{-1}\). Let \(P_N\) be one minus this Taylor
polynomial for \(e^{-A_N(z)}\). Since every source and energy
shift has norm one, the same coefficient-tail estimate bounds
both operator errors by \(N^{-1}\). Therefore
\[
 P_N(W)f_h\longrightarrow0\quad\hbox{in }\mathcal K,
 \qquad \|P_N(S)-I\|\longrightarrow0.                   \tag{16}
\]
Each \(P_N(W)\) preserves \(\mathcal D\), and
\(TP_N(W)=P_N(S)T\). Thus
\[
 (P_N(W)f_h,TP_N(W)f_h)\longrightarrow(0,Tf_h).          \tag{17}
\]

If \(T\) is closable, (17) forces \(Tf_h=0\) for every
\(h\). Covariance then forces \(T\mathcal D_0=0\).
The kernel of the closed operator \(\overline T\) is closed
in \(\mathcal K\) and contains the dense space
\(\mathcal D_0\). It is therefore all of \(\mathcal K\),
so \(T=0\) on its full original domain. This proves item 1;
\(\mathcal D_0\) need not have been a form core.

When \(\mathcal D=\mathcal D_0\), multiply (17) by any fixed
polynomial in the commuting source and energy shifts. Equation
(16) then puts \((0,TR(W)f_h)\) in the graph closure. Those
target vectors have dense span in \(E_Q\). The graph closure
contains \(\{0\}\oplus E_Q\); subtracting vertical vectors
from the original graph, and using source-domain density, gives
\(\overline{\operatorname{Graph}T}=\mathcal K\oplus E_Q\).

If a closable nonnegative form \(q\le Q\) on \(\mathcal D_0\)
were nonzero, for any \(f\in\mathcal D_0\) this graph identity
would provide \(u_n\to0\) with \(Tu_n\to Tf\). Then
\(q[u_n-u_m]\le\|Tu_n-Tu_m\|^2\to0\), so closability
gives \(q[u_n]\to0\); also \(q[f-u_n]\to0\). The seminorm
triangle inequality implies \(q[f]=0\), proving item 2.

## Correlated measures, controls and the remaining boundary

For a finite nonzero measure \(\mu\) on the prime torus,
use the natural map
\[
 T_\mu(e_n\otimes h)=z^{v(n)}\otimes U_{-\log n}h
 \quad\hbox{on }\mathcal D_0,
 \qquad E_\mu=H^2(\mu)\otimes H_{\mathbb R}.
\]
Linear independence in (4) makes it well defined; covariance
follows by cancellation of the translations. If \(\mu\) is
supported on
\(\varepsilon X_j(z)\ge c\sqrt{V_j}\) for all late \(j\),
where \(X_j\) is the symbol in WP-457, compression of its
multiplication quadratic form gives (2), even when
\(H^2(\mu)\ne L^2(\mu)\). Item 2 applies. It requires
neither WP-457's conditional marginals nor any independence.

Three limitations are essential:

- The source norms in (14) are vacuum-vector estimates, not
  uniform bounds on \(P_N(W)\). They cannot be extended to an
  arbitrary dense invariant domain by an appeal to density.
  Omitting the natural orbit remains a genuinely different question.
- The fixed \(c>0\) drives (15). This proof does not exclude
  \(D_{B_j,Q}\ge0\) with no variance-scale buffer or margins
  tending to zero at an unspecified rate.
- Infinitely many late blocks are essential. WP-456's closed
  singular finite-panel arc energies are consistent with this
  theorem, as are tests of the full completed Weil form instead
  of the unchanged finite blocks (1).

The source estimate uses only the Poisson Gram bound, the two
coefficient bounds in (8), and the decaying ray tail. Comparable
product-shift controls satisfy the same argument; it is not a
Riemann-specific sign law. Arbitrary target correlations cannot
repair this domain, while a different source-selected domain or
a changed global comparison still needs an independent theorem.

## Prior art and validation

Hoeffding's 1963 equation (4.16) is the classical exponential
estimate used in (10); the required special case is proved above.
Simon's Section 2 provides the general maximal-closable-part
framework; here the zero-part conclusion follows directly from
the graph calculation. Yafaev's Theorem 1.3 is a one-variable
Toeplitz closability theorem and is not being extended by
assertion to this source. WP-456 supplies the local warning that
singular joint measures alone do not imply nonclosability.
Searches on closable Toeplitz forms, analytic restrictions,
singular product measures and unbounded shift intertwiners do
not support a historical novelty claim.

The derived contribution is the analytic separator (13)--(16)
and its correlation-independent, orbit-domain obstruction.
Unlike WP-458's normalized averages, these tests converge in
operator norm on the target without assuming target moment
bounds. All limiting claims are proved by (6)--(17), including
both signs, higher prime powers, actual real translations,
non-normal energy operators, and polynomial-domain preservation.
No finite numerical extrapolation is evidence for the theorem.

## References

- [WP-458](WP-458-conditioned-block-orbit-forms-have-no-nonzero-closable-part.md), product-conditioned predecessor and natural orbit map.
- [WP-457](WP-457-dyadic-sign-conditioning-preserves-all-bounded-support-weak-prime-moments.md), block normalization and abstract sign-selected controls.
- [WP-453](WP-453-closability-forbids-infinite-prime-ray-orientation.md), separate-ray obstruction on arbitrary dense domains.
- [WP-456](WP-456-closed-singular-arc-traces-can-select-either-finite-weil-sign.md), closed singular finite-panel controls.
- W. Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*, Journal of the American Statistical Association **58** (1963), no. 301, 13--30, equation (4.16), [original-paper scan](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf), [DOI](https://doi.org/10.1080/01621459.1963.10500830).
- B. Simon, *A canonical decomposition for quadratic forms with applications to monotone convergence theorems*, Journal of Functional Analysis **28** (1978), 377--385, Section 2, [original-paper scan](https://www.tu-chemnitz.de/mathematik/analysis/kalmes/DAAD_Tunesien_2014_Simon.pdf).
- D. R. Yafaev, *On semibounded Toeplitz operators*, Journal of Operator Theory **77** (2017), 205--216, Theorem 1.3, [journal text](https://jot.theta.ro/jot/archive/2017-077-001/2017-077-001-012.pdf).
- NIST Digital Library of Mathematical Functions, [equation 27.2.3](https://dlmf.nist.gov/27.2.E3), the prime number theorem used in (7).
