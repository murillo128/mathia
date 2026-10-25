---
title: "WP-453: Closability forbids infinite prime-ray orientation"
type: research-finding
status: verified
research_question: "Can an unbounded closable covariant Maharam energy orient infinitely many separate critical prime rays?"
claim_strength: exact_closable_form_obstruction_with_a_nonclosable_all_ray_control
scope: separate critical prime-ray defects in the fixed Maharam representation; not the globally completed Weil form
finding_id: WP-453
related_findings:
  - WP-451
  - WP-452
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-25
updated: 2026-10-25
tags:
  - weil-positivity
  - maharam-extension
  - closable-form
  - weak-convergence
  - sign-obstruction
---

# WP-453: Unbounded energy does not evade the infinite-ray obstruction if it is closable

## Claim and boundary

**EXACT-DERIVED; CLASSICAL OPERATOR-THEORETIC INGREDIENTS;
CATEGORY OBSTRUCTION.** WP-452's boundedness assumption can be
replaced by closability on an arbitrary dense invariant domain.
No phase-modulation invariance or excitation-diagonal structure
is needed.

Use the same fixed source:
\[
 \Omega=\prod_p\mathbb N_0,\qquad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(j)=(1-p^{-1})p^{-j},\qquad
 \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds),
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\qquad
 (U_ch)(s)=e^{-c/2}h(s-c),\qquad
 W_p=V_p\otimes U_{\log p}.
 \tag{1}
\]
Write \(W_m=\prod_pW_p^{v_p(m)}\) for the integer semigroup action.
Let \(\mathcal D\subset\mathcal K\) be dense, and let \(Q\) be
positive semidefinite, sesquilinear, conjugate-linear in its first
variable, and **closable relative to the original norm of
\(\mathcal K\)**. For a set of primes \(P\), suppose
\[
 W_p\mathcal D\subset\mathcal D,\qquad Q[W_pf]=Q[f]
       \quad(p\in P,\ f\in\mathcal D).                    \tag{2}
\]
The energy completion
\(\mathcal H_Q=\overline{\mathcal D/\ker Q}^{\,Q}\) carries
isometries \(S_p[f]=[W_pf]\). Define, with energy-space adjoints,
\[
 D_{p,Q}=-(\log p)\sum_{k\ge1}r_p^k(S_p^k+S_p^{*k}),
 \qquad r_p=p^{-1/2}.                                    \tag{3}
\]
The series converges in operator norm for each prime. Then
\[
 \boxed{P\text{ infinite and }D_{p,Q}\ge0\ (p\in P)
        \quad\Longrightarrow\quad Q=0.}                 \tag{4}
\]
In particular, a nonzero densely defined closable covariant
energy can orient only finitely many separate critical rays.
Covariance is needed only for those primes, not every integer.
There is no boundedness, coercivity, faithfulness, domain-core,
backward-shift-invariance or modulation hypothesis.

The finite boundary remains WP-452's nonzero bounded arc-selection
forms. Conversely, an explicit dense-domain **nonclosable** form
below makes every ray strictly positive. Thus an algebraic positive
completion alone is not enough: its relation to the original
Hilbert topology is essential.

No claim is made about the sign of a sum completed by mixed-prime,
archimedean and polar terms. No RH consequence, historical novelty,
formal verification or independent adversarial approval is claimed.

## Weak limits survive a closable intertwiner

The load-bearing lemma is elementary but replaces the bounded
measure-domination step of WP-452.

Let \(T:\mathcal D\subset H\to E\) be densely defined and
closable with dense range. Suppose bounded operators \(A_j\) on
\(H\) and \(B_j\) on \(E\) satisfy
\[
 A_j\mathcal D\subset\mathcal D,\qquad TA_j=B_jT,
 \qquad A_j\longrightarrow0\text{ weakly},\qquad
 \sup_j\|B_j\|<\infty.                                  \tag{5}
\]
Then \(B_j\to0\) weakly. Indeed, \(\operatorname{Dom}T^*\)
is dense by closability. For \(u\) in this adjoint domain and
\(f\in\mathcal D\),
\[
 \langle u,B_jTf\rangle_E
  =\langle T^*u,A_jf\rangle_H\longrightarrow0.            \tag{6}
\]
The uniform bound on \(B_j\) first extends (6) to every \(u\in E\)
and then, using density of \(T\mathcal D\), to every second
argument in \(E\). No assertion that an arbitrary unbounded
operator preserves weak convergence is used.

Apply this to the quotient map \(Tf=[f]\). Its range is dense
by construction. It is closable precisely when \(Q\) is:
\(\|Tf\|^2=Q[f]\), so the graph-sequence criterion for \(T\)
is exactly the criterion that \(f_n\to0\) and
\(Q[f_n-f_m]\to0\) imply \(Q[f_n]\to0\). Nullspaces cause
no problem. Positivity and polarization of (2) make each \(S_p\)
a well-defined isometry on the completion.

For every fixed \(k\ge1\), the actual source satisfies
\[
 W_p^k\longrightarrow0\quad\text{in the weak operator topology
 as }p\to\infty.                                        \tag{7}
\]
To verify this, take two packets \(f,g\) depending on finitely
many valuation coordinates, say those in \(E\), and on \(s\).
For a prime outside \(E\), integration over its fresh coordinate
in (1) gives exactly
\[
 \langle g,W_p^kf\rangle
   =p^{-k/2}\langle g,(I\otimes U_{k\log p})f\rangle,
 \qquad
 |\langle g,W_p^kf\rangle|
   \le p^{-k/2}\|g\|\|f\|.                              \tag{8}
\]
These packets are dense in \(\mathcal K\), and \(\|W_p^k\|=1\),
which proves (7). The packets need **not** belong to
\(\mathcal D\); they prove a statement in the original space
before (5) is applied on the actual domain.

Equations (2), (5)--(8), with \(A_j=W_{p_j}^k\) and
\(B_j=S_{p_j}^k\), show for any sequence of distinct primes in
\(P\) that
\[
 S_{p_j}\longrightarrow0,\qquad S_{p_j}^2\longrightarrow0
        \quad\text{weakly on }\mathcal H_Q.              \tag{9}
\]
Only these first two powers will be needed. The second assertion
is proved separately; weak convergence of operators does not in
general pass to their squares.

## Ray positivity forces a uniform quadratic separator

First, if \(D_{p,Q}\ge0\), the isometry \(S=S_p\) must be
unitary. Otherwise choose a unit vector \(v\in\ker S^*\).
The vectors \(S^nv\), \(n\ge0\), are orthonormal. For
\(x=v+Sv\),
\[
 \langle x,Sx\rangle=1,\qquad
 \langle x,S^kx\rangle=0\ (k\ge2),\qquad
 \langle x,D_{p,Q}x\rangle=-2(\log p)r_p<0,             \tag{10}
\]
a contradiction. An isometry has closed range, so
\(\ker S^*=0\) indeed makes it surjective.

For a unitary \(S\), (3) is the continuous functional calculus
of the Poisson-defect symbol
\[
 w_p(z)=(\log p)\left(1-\frac{1-r_p^2}{|1-r_pz|^2}\right).
 \tag{11}
\]
Thus positivity confines its spectrum to
\(\{z\in\mathbb T:\operatorname{Re}z\le r_p\}\).
Writing \(X=\operatorname{Re}S\), we have
\(-I\le X\le r_pI\).

Consider the same polynomial at every prime,
\[
 h(z)=-z-\tfrac12z^2.
\]
Unitarity implies \(\operatorname{Re}S^2=2X^2-I\), hence
\[
 \operatorname{Re}h(S)=\tfrac12I-X-X^2.
\]
For \(-1\le x\le1/4\), the exact certificate is
\[
 \tfrac12-x-x^2-\tfrac3{16}
       =(\tfrac14-x)(x+\tfrac54)\ge0.                  \tag{12}
\]
Therefore every oriented prime \(p\ge17\) satisfies
\[
 \boxed{\operatorname{Re}h(S_p)\ge\tfrac3{16}I,\qquad
        \|h(S_p)\|\le\tfrac32.}                        \tag{13}
\]
If infinitely many rays were oriented in a nonzero energy space,
(9) would make \(h(S_{p_j})\to0\) weakly along them. On any
nonzero vector this contradicts (13). This proves (4).

The argument uses neither prime density nor divergence of a prime
sum. Arbitrarily sparse infinite prime sets are excluded. It also
avoids an infinite-torus absolute-continuity assertion or an
unjustified multivariable extension of a one-variable theorem.

## A nonclosable control realizes all favorable phases

The excluded category is nonempty even on this very source. Put
\(e_n=V_n1\), where \(V_n=\prod_pV_p^{v_p(n)}\), and set
\(\epsilon(n)=(-1)^{\sum_pv_p(n)}\). The functions
\(e_n=\sqrt n\,1_{J_p\ge v_p(n)\ \forall p}\) are finitely
linearly independent: after taking a finite divisor closure this
is the triangular divisibility-incidence matrix, on cylinder
sets of positive measure. Their span is dense, since differences
of successive valuation thresholds generate finite-coordinate
cylinder functions.

On the dense algebraic domain
\[
 \mathcal D_0=\operatorname{span}\{
 e_n(J)e^{-s/2}\phi(s): n\ge1,\ \phi\in C_c^\infty(\mathbb R)\},
\]
define the well-defined linear functional
\[
 L\left(\sum_n e_n e^{-s/2}\phi_n\right)
      =\sum_n\epsilon(n)\int_{\mathbb R}\phi_n(s)\,ds,
 \qquad Q_0(f,g)=\overline{L(f)}L(g).                    \tag{14}
\]
Flattening the real measure by multiplication by \(e^{s/2}\)
turns \(U_c\) into ordinary translation. Consequently
\(LW_m=\epsilon(m)L\). The domain is invariant and \(Q_0\)
is dilation covariant for every integer. Its energy space is
\(\mathbb C\), with \(S_p=-I\) for every prime, so
\[
 D_{p,Q_0}=\frac{2(\log p)r_p}{1+r_p}I>0.                \tag{15}
\]
But choose \(\phi\in C_c^\infty\) with \(\int\phi=1\), and
put \(\phi_R(s)=R^{-1}\phi(s/R)\),
\(f_R=e_1e^{-s/2}\phi_R(s)\). Then
\[
 \|f_R\|^2=R^{-1}\|\phi\|_2^2\longrightarrow0,
 \qquad L(f_R)=1,\qquad Q_0[f_R-f_T]=0.                 \tag{16}
\]
This explicitly violates closability. The chosen character selects
favorable phases and is not a source-forced sign law. The control
shows exactly why purely algebraic covariance and positivity do
not imply the analytic result.

## Prior art, validation and consequence

The adjoint-domain characterization of closability is classical;
Teschl's Lemma 2.4(ii) records it. The short proof (6) is the only
weak-limit transport used. Panja's Theorem 1.2 treats the bounded
positive invariant-metric factorization through isometries. Here
that quotient map may be unbounded, and its closability replaces
bounded domination. The spectral calculus and the elementary
wandering-vector test (10) are also classical.

Yafaev's Theorem 1.3 characterizes closable one-variable
semibounded Toeplitz forms by absolute continuity of their
representing measure. It is relevant neighboring prior art, but
is not being applied to an arbitrary Maharam form or infinitely
many coordinates. Our proof needs only the two weak moments (9)
and the explicit polynomial (12). Searches by closable Toeplitz
forms, unbounded intertwiners and multiplicative Toeplitz operators
do not establish historical novelty.

The local delta from WP-452 is the removal of its global bounded
energy constant while allowing arbitrary dense invariant domains,
including domains without cylinder vectors. WP-451 allowed general
energies but needed phase modulation; the present theorem does
not. It excludes the concrete unbounded-closable escape left by
those two results, rather than merely restating the bounded
support argument.

A scratch diagnostic checked four exact unilateral-orbit pairings
in (10), 1,001 rational values of (12), and 4,004 Fourier/arc
values for radii \(0.05,0.1,0.2,0.24\). All 5,009 checks passed.
The identity (12) and the analytic proof above, not the samples,
establish the uniform bound and infinite-prime assertion. The
nonclosable control (14)--(16) is exact and needs no numerical
limit extrapolation.

The obstruction survives product controls with fresh-coordinate
vacuum moments tending to zero, arbitrary real translation
frequencies, ray radii tending to zero, and positive ray scales.
It therefore does not detect
Riemann-specific arithmetic. A surviving global sign mechanism
must change the unchanged separate-ray comparison, its isometric
source relation, the original topology/representation, or the
admissible domain/covariance requirements. A nonclosable positive
algebraic form supplies no closed energy in the declared norm.
Active global coupling remains outside this theorem; its exact
Gamma/polar comparison and independent sign theorem remain missing.

## References

- [WP-452](WP-452-bounded-covariant-energies-cannot-orient-infinitely-many-prime-rays.md), bounded predecessor and finite-panel positive controls.
- [WP-451](WP-451-phase-invariant-maharam-forms-retain-the-full-finite-weil-sign-defect.md), the distinct modulation-invariant obstruction.
- G. Teschl, *Mathematical Methods in Quantum Mechanics*, second edition, Graduate Studies in Mathematics **157**, AMS (2014), Lemma 2.4(ii), [authorized author text](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
- S. Panja, *Factorization of Toeplitz operators*, New York Journal of Mathematics **29** (2023), 848--873, Theorem 1.2, [journal text](https://nyjm.albany.edu/j/2023/29-33v.pdf).
- D. R. Yafaev, *On semibounded Toeplitz operators*, Journal of Operator Theory **77** (2017), no. 1, 205--216, Theorem 1.3, [journal text](https://jot.theta.ro/jot/archive/2017-077-001/2017-077-001-012.pdf), [DOI](https://doi.org/10.7900/jot.2016mar20.2095).
