# VIS-444 — occupation-moment hierarchy reconstructs hitting tails; a fourth-order witness

## Exact claim and status

For a measure-preserving flow, the full hierarchy of integrated target correlations reconstructs the probability that a finite flow window has **zero occupation**. For finite-union circle-arc targets, this is the symmetric first-hit avoidance law, with an explicit geometric error bound at finite correlation order. The two equal-three-deck targets of VIS-443 have identical integrated occupation moments of orders 1–3 but **different fourth-order integrated moments** at one common window.

**Evidence/status:** EXACT-DERIVED + CLASSICAL HAUSDORFF-MOMENT PRINCIPLE + EXACT RATIONAL VIS-443 SPECIALIZATION. Neither moment determinacy, inclusion-exclusion, nor the underlying cyclic three-deck nonuniqueness is claimed new. The line-specific contribution is the exact integrated fourth-order separation and the stated arc-geometry error certificate.

## The correlation hierarchy

Let \((X,m,\tau_u)\) be a measure-preserving real flow, \(E\) a measurable target and \(\rho>0\). Put \(L=2\rho\), and define

\[
Z_\rho(x)=L^{-1}\int_{-\rho}^\rho\mathbf1_E(\tau_u x)\,du\in[0,1],
\quad A_n(\rho)=\int_X(1-Z_\rho)^n\,dm\quad(n\ge1).
\]

For \(j\ge1\), write \(C_j(u_1,\ldots,u_j)=\int_X\prod_{k=1}^j\mathbf1_E(\tau_{u_k}x)\,dm(x)\), and set \(C_0=1\). Expanding the binomial and using Tonelli gives an **exact finite-order identity**

\[
A_n(\rho)=\sum_{j=0}^{n}(-1)^j\binom nj L^{-j}
\int_{[-\rho,\rho]^j}C_j(u_1,\ldots,u_j)\,du_1\cdots du_j.
\]

Since \(0\le1-Z_\rho\le1\), monotone pointwise convergence and bounded convergence give

\[
\boxed{A_n(\rho)\downarrow m\{Z_\rho=0\}.}
\]

For the unit-speed circle flow with a target that is a finite union of nondegenerate closed arcs, \(m_H\{Z_\rho=0\}=m_H\{H_E>\rho\}\), where \(H_E(\theta)=\inf\{|u|:\theta+u\in E\}\): discrepancies are confined to finitely many endpoint-only tangencies. Hence **all orders together** recover the Haar first-hit law. Finite orders need not.

## A quantitative bound for finite arc targets

Suppose \(E\subset\mathbb R/2\pi\mathbb Z\) is a union of \(K\) disjoint arcs of respective lengths \(\delta_i>0\), with \(0<L=2\rho<2\pi\) and \(L+\delta_i\le2\pi\). Define \(a_i=\min(L,\delta_i)\), \(q_i=1-a_i/L\in[0,1)\). Then for every integer \(n\ge1\),

\[
\boxed{0\le A_n(\rho)-m_H\{H_E>\rho\}\le
\frac1{2\pi}\sum_{i=1}^K
\left[\frac{2L}{n+1}(1-q_i^{n+1})
+|L-\delta_i|q_i^n\right].}
\]

In particular the error is at most

\[
\frac{KL}{\pi(n+1)}
+\frac1{2\pi}\sum_i |L-\delta_i|e^{-na_i/L}.
\]

**Derivation.** Write \(Z_\rho=\sum_i Z_{\rho,i}\), where \(Z_{\rho,i}\) is the normalized overlap between the window and arc \(i\). On \(\{Z_\rho>0\}\), at least one \(Z_{\rho,i}>0\), and \(Z_\rho\ge Z_{\rho,i}\); therefore the positive-occupation residue \((1-Z_\rho)^n\) is bounded by \(\sum_i\mathbf1_{\{Z_{\rho,i}>0\}}(1-Z_{\rho,i})^n\). Sliding one interval of length \(L\) over an arc of length \(\delta_i\) yields two linear overlap ramps from \(0\) to \(a_i\), and one plateau of width \(|L-\delta_i|\). Direct integration gives \(2L(1-q_i^{n+1})/(n+1)+|L-\delta_i|q_i^n\); division by the circumference and summation prove the first bound. Use \(q_i^n\le e^{-na_i/L}\) for the second. These are sufficient bounds, not claimed optimal.

## An integrated fourth-order separation of VIS-443

Retain VIS-443's two ten-site cyclic sets,

\[
S_E=\{0,1,3,4,12,15,19,22,24,27\},\qquad
S_F=\{0,3,4,7,12,15,22,24,25,27\}.
\]

Set \(\omega=2\pi/36\), \(\delta=\omega/2\), and \(E_S=\bigcup_{a\in S}[a\omega,a\omega+\delta]\) on the circle. VIS-443 proves that these are superlevel targets of normalized analytic polynomials of exact degree ten at one common regular threshold, with **all** target correlations of orders at most three equal. At \(\rho=3\omega\), \(L=6\omega\), the identity above therefore forces \(A_1,A_2,A_3\) to agree. Exact rational evaluation also gives

\[
A_1(E)=A_1(F)=31/36,\qquad
A_2(E)=A_2(F)=11641/15552,\qquad
A_3(E)=A_3(F)=13613/20736,
\]

but

\[
\boxed{A_4(E)=\frac{433477}{746496},\qquad
A_4(F)=\frac{433453}{746496},\qquad
A_4(E)-A_4(F)=\frac1{31104}>0.}
\]

Thus the order-four difference from VIS-443 survives **integration over all four observation offsets**, not merely one chosen four-point lag. The exact first-hit avoidance probabilities are \(1/9\) and \(1/12\), difference \(1/36\), so the moment limit retains a larger distinction.

To reproduce the finite computation, use the circle coordinate \(x=\theta/\omega\pmod{36}\). Target arcs become \([a,a+1/2]\), and the observation window is \([x-3,x+3]\). Partition \(x\in[0,36]\) at all \(a\pm3,\ a+1/2\pm3\pmod{36}\). On any consecutive segment \([u,v]\), its normalized window occupation \(Z(x)\) is affine and its endpoint values \(z_u,z_v\) are rational. The exact segment contribution is

\[
\frac{v-u}{36(n+1)}\sum_{j=0}^n
(1-z_u)^j(1-z_v)^{n-j}.
\]

Summing these fractions establishes every displayed value. An independent aligned-grid convolution agreed numerically with the exact expressions; neither discretization nor a rendered image is needed for the proof. Continuity of the integrated moments in arc width extends the strict fourth-order inequality to an open neighbourhood of \(\delta=\omega/2\), without claiming it for every width.

## Prior art, limitations, and consequence

Compact-interval moment determinacy is classical: F. Hausdorff, *Summationsmethoden und Momentfolgen*, I and II, *Mathematische Zeitschrift* 9 (1921); J. A. Shohat and J. D. Tamarkin, *The Problem of Moments*, American Mathematical Society Mathematical Surveys 1 (1943). The displayed reconstruction of the **atom at zero** follows more directly from bounded convergence, so no new Hausdorff theorem is asserted. VIS-443 already supplies the classical cyclic three-deck pair, its continuous transfer, and Fejér–Riesz polynomial realization (based on Keleti–Kolountzakis 2006).

For general measurable flow targets, \(\{Z_\rho=0\}\) need not equal literal no-hit if trajectories touch a measure-zero target for zero occupation time; the regular circle-arc assumption removes this issue up to Haar-null endpoint contacts. The explicit rate additionally requires \(L+\delta_i\le2\pi\), and is not a uniform bound for shrinking targets or growing Wang shells.

This sharpens the VIS-430 information audit: complete second- and third-order target statistics can give identical occupation certificates while the exact pre-saturation first-hit tails differ; order-four *integrated* information can already distinguish the VIS-443 construction. Higher-order correlation tariffs for actual arithmetic Wang source coefficients and selected-height comparisons remain unproved. No Gram/Haar anomaly, distinguished-height selector, zeta-zero exclusion, or RH progress follows from these abstract circle controls.

## Dependencies

- VIS-430: occupation autocorrelation/second-moment upper certificate.
- VIS-441: circle complementary-gap erosion formula.
- VIS-442: complete second-order homometric control.
- VIS-443: full third-order nonidentifiability and common analytic superlevel realization.
