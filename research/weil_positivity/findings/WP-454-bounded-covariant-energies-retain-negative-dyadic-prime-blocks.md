---
title: "WP-454: Bounded covariant energies retain negative dyadic prime blocks"
type: research-finding
status: verified
research_question: "Can joint phase selection make infinitely many disjoint finite-prime blocks positive when separate ray orientation is not required?"
claim_strength: exact_bounded_energy_block_obstruction_with_a_variance_scale_negative_floor
scope: disjoint finite-prime sums in the fixed Maharam representation; no completed global Weil sign claim
finding_id: WP-454
related_findings:
  - WP-451
  - WP-452
  - WP-453
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-26
updated: 2026-10-26
tags:
  - weil-positivity
  - maharam-extension
  - bounded-positive-form
  - prime-blocks
  - sign-obstruction
---

# WP-454: Grouping rays into dyadic blocks does not remove the bounded-energy obstruction

## Claim and boundary

**EXACT-DERIVED; CLASSICAL PROBABILITY AND HARMONIC-ANALYSIS
INGREDIENTS; CATEGORY OBSTRUCTION.** A nonzero bounded covariant
energy cannot orient infinitely many disjoint prime blocks whose
reciprocal-prime mass tends to zero. The blocks may have unbounded
cardinality, and their individual ray defects need not be positive.
The conclusion survives a fixed small variance-scale scalar repair.

Use the source and conventions of WP-452:
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(j)=(1-p^{-1})p^{-j},\qquad
 \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds),
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\quad
 (U_ch)(s)=e^{-c/2}h(s-c),\quad W_p=V_p\otimes U_{\log p}.
 \tag{1}
\]
Let \(Q\) be a positive semidefinite sesquilinear form on
\(\mathcal K\), conjugate-linear in its first variable, with
\[
 0\le Q[f]\le C\|f\|^2,\quad C<\infty,\qquad
 Q[W_pf]=Q[f].                                           \tag{2}
\]
Covariance is required for every prime in the blocks below.
On the quotient energy completion \(\mathcal H_Q\), put
\(S_p[f]=[W_pf]\); these are commuting isometries. With
**energy-space adjoints**, define
\[
 D_{p,Q}=-(\log p)\sum_{k\ge1}p^{-k/2}(S_p^k+S_p^{*k}),
 \qquad D_{B,Q}=\sum_{p\in B}D_{p,Q}.                    \tag{3}
\]
Every operator in (3) for a finite \(B\) is bounded self-adjoint.

Let \((B_j)\) be pairwise disjoint, nonempty finite prime sets, and
write
\[
 \sigma_j=\sum_{p\in B_j}\frac1p\longrightarrow0,\qquad
 V_j=2\sum_{p\in B_j}\frac{(\log p)^2}{p-1},\qquad
 \tau=\frac1{4\sqrt6}.                                  \tag{4}
\]
Then
\[
 \boxed{D_{B_j,Q}\ge-\tau\sqrt{V_j}\,I
 \text{ for infinitely many }j\quad\Longrightarrow\quad Q=0.}
 \tag{5}
\]
Equivalently, for every nonzero \(Q\) satisfying (2),
\[
 \inf\operatorname{spec}D_{B_j,Q}<-\tau\sqrt{V_j}
 \quad\text{for all sufficiently large }j.              \tag{6}
\]
The onset may depend on \(Q\); no effective uniform onset or sharp
constant is claimed. In particular, nonnegativity, or a scalar
repair of size \(o(\sqrt{V_j})\), cannot hold on infinitely many
blocks in a single such energy.

This permits arbitrary off-diagonal and cross-prime correlations
in \(Q\). It concerns the unchanged sum (3), not a new observable
with additional mixed-prime terms. It does not address an unbounded
closable energy, overlapping blocks, or the sum completed by
archimedean and polar contributions. No RH consequence, historical
novelty, formal verification or independent adversarial approval
is claimed.

## A uniform negative tail under Haar measure

For normalized Haar measure on \(\mathbb T\), put
\[
 r_p=p^{-1/2},\quad P_r(z)=\frac{1-r^2}{|1-rz|^2},\qquad
 w_p(z)=(\log p)(1-P_{r_p}(z)).                           \tag{7}
\]
On a finite product torus let \(X_B=\sum_{p\in B}w_p(z_p)\).
The coordinates are independent under product Haar measure.
The absolutely convergent Fourier series of \(P_r\) gives
\[
 \mathbb E w_p=0,\qquad
 v_p:=\mathbb E w_p^2=\frac{2(\log p)^2r_p^2}{1-r_p^2},
 \qquad \|w_p\|_\infty\le\frac{2(\log p)r_p}{1-r_p}.
 \tag{8}
\]
For \(r_p\le1/2\),
\[
 \frac{\|w_p\|_\infty^2}{v_p}
 \le2\frac{1+r_p}{1-r_p}\le6,\qquad
 \mathbb E w_p^4\le6v_p^2.
\]
Independence and zero means therefore imply, with
\(V_B=\sum_{p\in B}v_p\),
\[
 \mathbb E X_B=0,\quad \mathbb E X_B^2=V_B,\quad
 \mathbb E X_B^4
 =\sum_p\mathbb E w_p^4+6\sum_{p<q}v_pv_q\le6V_B^2.
 \tag{9}
\]
Hölder interpolation gives
\[
 \mathbb E|X_B|\ge
 \frac{(\mathbb E X_B^2)^{3/2}}{(\mathbb E X_B^4)^{1/2}}
 \ge\sqrt{V_B/6}.
\]
For \(Y=(-X_B)_+\), zero mean implies
\(\mathbb EY=\tfrac12\mathbb E|X_B|\). Consequently
\[
 \mathbb E\big[Y1_{Y>\tau\sqrt{V_B}}\big]
 \ge\left(\frac1{2\sqrt6}-\tau\right)\sqrt{V_B}
 =\frac{\sqrt{V_B}}{4\sqrt6}.
\]
Cauchy--Schwarz, using \(\mathbb EY^2\le V_B\), proves the
dimension-free estimate
\[
 \boxed{m_B\{X_B<-\tau\sqrt{V_B}\}\ge\frac1{96}.}        \tag{10}
\]
This is a direct fourth-moment argument of Paley--Zygmund type.
It needs neither a central limit theorem nor comparable prime
weights. Disjointness ensures that only finitely many blocks
contain primes below five, so the restriction in (8) is harmless.

## Small reciprocal mass controls the actual Poisson reference

For arbitrary rotations \(\eta_p\in\mathbb T\), define
\[
 L_{B,\eta}(z)=\prod_{p\in B}P_{r_p}(z_p\eta_p).
\]
Parseval and product integration give exactly
\[
 \int L_{B,\eta}\,dm_B=1,\qquad
 \|L_{B,\eta}-1\|_2^2
 =\prod_{p\in B}\frac{1+r_p^2}{1-r_p^2}-1
 \le\exp\left(\frac83\sum_{p\in B}\frac1p\right)-1.
 \tag{11}
\]
The last bound uses
\(\log((1+t)/(1-t))\le2t/(1-t)\le8t/3\) for
\(0\le t\le1/4\). Thus for every measurable event \(A\),
\[
 \left|\int_A L_{B,\eta}\,dm_B-m_B(A)\right|
 \le\|L_{B,\eta}-1\|_1\le\|L_{B,\eta}-1\|_2.           \tag{12}
\]
The bound is uniform in all rotations, including those correlated
through the Maharam real frequency. From (4), (10)--(12), every
sufficiently late block satisfies
\[
 \sup_\eta\int_{\{X_{B_j}\ge-\tau\sqrt{V_j}\}}
       L_{B_j,\eta}\,dm_{B_j}\le\frac{191}{192}=:\rho<1.
 \tag{13}
\]
No assertion of independence after mixing the real frequency is
being made.

## Orbit-measure domination converts block signs to zero energy

For a finite prime set \(F\), bounded covariance (2) gives the
finite-torus Herglotz measures of WP-452:
\[
 c_Q(h)=Q(W^{h_-}f,W^{h_+}f)=\int z^h\,d\mu_{Q,f,F}(z),
 \qquad \mu_{Q,f,F}(\mathbb T^F)=Q[f],
 \qquad 0\le\mu_{Q,f,F}\le C\mu_{I,f,F}.                \tag{14}
\]
Here \(W^a=\prod_{p\in F}W_p^{a_p}\), and \(h_+,h_-\)
are the coordinatewise positive and negative parts. For clarity,
polarized covariance makes \(Q(W^af,W^bf)\) depend only on
\(b-a\). The resulting functions for \(Q\), the original norm
\(I\), and \(CI-Q\) are positive definite on \(\mathbb Z^F\).
Herglotz representation and uniqueness give (14).

If \(B\subset F\), then for every analytic polynomial \(P\),
\[
 \langle[P(W)f],D_{B,Q}[P(W)f]\rangle_Q
   =\int X_B(z)|P(z)|^2\,d\mu_{Q,f,F}(z).               \tag{15}
\]
This follows by expanding (3), with absolute convergence of each
prime-ray series. If \(D_{B,Q}\ge-\tau\sqrt{V_B}I\), then
\(\mu_{Q,f,F}\) is supported on
\(A_B=\{X_B\ge-\tau\sqrt{V_B}\}\): multiply Laurent
polynomials by monomials without changing their boundary modulus,
and approximate continuous square roots uniformly in (15).
This uses positivity of the **whole block**, not its summands.

Take a packet \(f\) depending on finitely many valuation
coordinates \(E\) and the real variable. After flattening the
real measure by \(f\mapsto e^{s/2}f\), use the unitary Fourier
transform with convention \(e^{-i\xi s}\). For \(F\cap E=\varnothing\),
WP-452's direct source calculation is
\[
 d\mu_{I,f,F}(z)=
 \left[\int_{\mathbb R}\|\widehat f_E(\xi)\|^2
       \prod_{p\in F}P_{r_p}(z_pe^{i\xi\log p})\,d\xi\right]dm_F(z).
 \tag{16}
\]
Indeed \(\langle V_p^a1,V_p^b1\rangle=r_p^{|a-b|}\),
and \(U_c\) becomes multiplication by \(e^{-i\xi c}\).
These determine all Fourier moments of (16); its mass is
\(\|f\|^2\).

Suppose the lower bound in (5) holds on infinitely many blocks.
Choose any \(N\) sufficiently late such blocks avoiding \(E\)
and let \(F\) be their union. Their disjointness, (13), and (16)
give, **before** the frequency mixing,
\[
 \begin{split}
 Q[f]
 &\le C\mu_{I,f,F}\left(\bigcap_{j}A_{B_j}\right)\\
 &\le C\int\|\widehat f_E(\xi)\|^2\rho^N\,d\xi
 =C\rho^N\|f\|^2.                                     \tag{17}
 \end{split}
\]
Letting \(N\to\infty\) forces \(Q[f]=0\). Such packets are
dense, and the single boundedness constant in (2) extends this to
all of \(\mathcal K\). This proves (5). Applying the same argument
to any infinite subsequence proves the eventual statement (6).

## Dyadic blocks and the scalar repair scale

For \(B_j=\{p:2^j\le p<2^{j+1}\}\), the prime number theorem
and partial summation give, writing \(x=2^j\),
\[
 \sigma_j\sim\frac{\log2}{\log x}\longrightarrow0,
 \qquad V_j\sim2(\log2)\log x.                          \tag{18}
\]
For the second formula, replace \(1/(p-1)\) by \(1/p\), with
error \(o(1)\) on the block, and integrate
\((\log t)^2/t\) against \(d\pi(t)\). The main term is
\(2\int_x^{2x}(\log t)/t\,dt
=2(\log2)\log x+(\log2)^2\); its leading asymptotic is (18).
No RH input is used. The main theorem itself needs only (4).

Thus every fixed nonzero bounded covariant energy has negative
dyadic-block spectral values of magnitude at least
\(\tau\sqrt{2(\log2)\log x}(1+o(1))\). A scalar diagonal
repair smaller than this order cannot make all late blocks
nonnegative. This is a necessary cost within (1)--(3), not an
optimal repair theorem or a statement about the Gamma term.

Finite selection remains possible: the half-circle selection form
of WP-452 for the finite union of any chosen blocks makes all
their rays, hence their block sums, positive. Its existence is
compatible with (5); no fixed nonzero bounded energy can retain
that selection on infinitely many of the blocks in (4).

## Prior art, controls and validation

Herglotz representation, positive invariant-metric factorization,
fourth-moment lower-tail bounds, and the product-density calculation
are classical. Panja's Theorem 1.2 supplies the neighboring bounded
Toeplitz-factorization framework; Nikolski--Pushnitski Section 3
supplies the multiplicative-Toeplitz/infinite-torus setting. No
Szegő limit, infinite-product absolute-continuity theorem, or
multivariable Fejér--Riesz factorization is applied here. Tao's
second-moment notes, Exercise 5, record the classical
Paley--Zygmund method; (8)--(10) give the exact buffered sign estimate
used here without citing a stronger probability theorem.

The local delta from WP-452 is the replacement of separate ray
positivity by positivity of an entire finite block, allowing growing
block cardinality and internal cancellation. The new input is that
small reciprocal-prime mass makes each actual Poisson block close
to Haar **uniformly in the real frequency**, while a fourth-moment
bound preserves a fixed negative tail. WP-453 permits unbounded
closable energies but requires separate ray signs; its weak-moment
argument is not asserted to settle block sums. The present result
does not supersede that different domain boundary.

Searches on multiplicative Toeplitz positivity, closable Toeplitz
forms, product Poisson measures, and fourth-moment sign estimates
locate these classical ingredients, not a historical novelty
certificate. The derived contribution is this explicit bounded
Maharam block obstruction. It survives matched product sources
with vacuum correlations \(r_p^{|a-b|}\), block sums
\(\sum r_p^2\to0\), arbitrary real translations and positive
ray scales. It therefore supplies no arithmetic sign selection.

A standard-library Python diagnostic outside Git checked 86
normalizations and inequalities: one-torus moments at six primes,
rotation-invariance of Poisson second moments, four two-prime
product grids, the buffered negative mass, fourth-moment bounds,
and the product-density error bound. The largest relative error
in the one-torus moment identities was below \(7\times10^{-16}\).
These are numerical diagnostics only. Equations (8)--(17) prove
the dimension-free and infinite-block claims exactly.

The surviving global question still requires an additional
source-forced operation: changed observables with mixed-prime or
archimedean coupling, a different representation/topology, or a
properly analyzed unbounded form. Simply grouping the unchanged
ray defects into disjoint dyadic blocks does not furnish that
operation within bounded covariant energies.

## References

- [WP-452](WP-452-bounded-covariant-energies-cannot-orient-infinitely-many-prime-rays.md), orbit measures, source normalization and finite selection controls.
- [WP-453](WP-453-closability-forbids-infinite-prime-ray-orientation.md), the distinct unbounded-closable separate-ray theorem.
- S. Panja, *Factorization of Toeplitz operators*, New York Journal of Mathematics **29** (2023), 848--873, Theorem 1.2, [journal text](https://nyjm.albany.edu/j/2023/29-33v.pdf).
- N. Nikolski and A. Pushnitski, *Szegő-type limit theorems for “multiplicative Toeplitz” operators and non-Følner approximations*, St. Petersburg Mathematical Journal **32** (2021), 1033--1050, Section 3, [author preprint](https://arxiv.org/pdf/2001.01474).
- T. Tao, *254A, Notes 9: second moment and entropy methods* (2019), Exercise 5, [author notes](https://terrytao.wordpress.com/2019/11/12/254a-notes-9-second-moment-and-entropy-methods/).
- NIST Digital Library of Mathematical Functions, [§27.2(i), equation 27.2.3](https://dlmf.nist.gov/27.2.E3), the prime number theorem used only for (18).
