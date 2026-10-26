---
title: "WP-456: Closed singular arc traces can select either finite Weil sign"
type: research-finding
status: verified
research_question: "Does closability prevent a singular diagonal phase trace from selecting a favorable finite Weil block?"
claim_strength: exact_closed_unbounded_singular_arc_construction_with_both_strict_sign_controls
scope: arbitrary fixed finite prime panel and phase locking in the Maharam representation; no infinite-block or global sign theorem
finding_id: WP-456
related_findings:
  - WP-452
  - WP-453
  - WP-454
  - WP-455
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-26
updated: 2026-10-26
tags:
  - weil-positivity
  - maharam-extension
  - closed-form
  - diagonal-restriction
  - singular-orbit-measure
  - sign-selection
---

# WP-456: Closedness permits target-selected arcs even in a singular joint phase measure

## Claim and boundary

**EXACT-DERIVED; CLASSICAL RESTRICTION AND ADJOINT-DOMAIN
INGREDIENTS; MATCHED SIGN CONTROL.** Fix a finite prime panel
\(F=\{p_1,\ldots,p_d\}\), \(d\ge2\), phases
\(\lambda_j\in\mathbb T\), and a nonempty \(B\subset F\).
There are two nonzero densely defined **closed unbounded**
positive forms \(Q_+\) and \(Q_-\) on the same Maharam source
such that:

- their domains are invariant under every integer source isometry
  \(W_m\), and \(Q_\pm[W_mf]=Q_\pm[f]\);
- their energy spaces have the same phase-locking relation
  \(\lambda_i^{-1}S_{p_i}=\lambda_j^{-1}S_{p_j}\);
- at any unit common wandering vector \(e\), both have
  \(Q_\pm[e]=1\), and their joint orbit measures are singular
  relative to the original product-Haar orbit measure;
- for the unchanged finite block, using **energy-space adjoints**,
  \[
  D_{B,Q}= -\sum_{p_j\in B}(\log p_j)
        \sum_{k\ge1}p_j^{-k/2}(S_{p_j}^k+S_{p_j}^{*k}),
  \qquad
  D_{B,Q_+}\ge\epsilon_+ I,\quad
  D_{B,Q_-}\le-\epsilon_- I
  \tag{1}
  \]
  for some \(\epsilon_\pm>0\).

The only sign-selecting change is the choice of an arc in the
common diagonal phase variable. The result settles the arc-restriction
test explicitly excluded in WP-455: closedness, singular phase
locking, all-prime covariance and fixed vacuum normalization do
not independently select the finite sign. Unlike the full-circle
trace, these energies have unitary selected shifts.

The arcs are chosen **after inspecting the block symbol**. This is
a counterexample to a canonicity inference, not a source-forced
positive Weil construction. The panel is finite; no uniform
infinite-panel limit, infinite-block orientation, Gamma/polar
completion, RH consequence, historical novelty, formal verification
or independent adversarial approval is claimed.

## Fixed source and the polynomial trace

Retain the normalization of WP-452--WP-455:
\[
 \Omega=\prod_p\mathbb N_0,\qquad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(a)=(1-p^{-1})p^{-a},
 \qquad \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds),
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\quad
 (U_ch)(s)=e^{-c/2}h(s-c),\quad W_p=V_p\otimes U_{\log p}.
 \tag{2}
\]
Let \(\mathcal E_F\ne0\) be the common wandering space supported
on \(J_{p_j}=0\) for every \(p_j\in F\). The valuation-shell
decomposition gives a unitary
\[
 \mathcal U_F:\mathcal K\longrightarrow
       H^2(\mathbb D^d;\mathcal E_F),\qquad
 W_{p_j}\longmapsto M_{z_j},\qquad
 W_q\longmapsto I\otimes R_q\quad(q\notin F),
 \tag{3}
\]
where each \(R_q\) is an isometry. Indeed the orthogonal shell
\(W^\alpha\mathcal E_F\) is precisely \(J_F=\alpha\);
the real translation is invertible within that shell. The
unselected isometries preserve the wandering space and doubly
commute with the selected ones, proving the last identity.

Choose a nonempty open arc \(A\subset\mathbb T\), with closure
so short that for some \(z_0\in\mathbb T\)
\[
 \sup_{z\in\overline A}|z-z_0|<1.
 \tag{4}
\]
Write \(d\mu_A=1_A\,dm/m(A)\), with normalized circle Haar
measure \(m\). On the dense space \(\mathcal P\) of finite
\(\mathcal E_F\)-valued polynomials define
\[
 T_A:\mathcal P\subset H^2(\mathbb D^d;\mathcal E_F)
       \longrightarrow L^2(A,\mu_A;\mathcal E_F),\qquad
 T_A f(z)=\sum_\alpha\lambda^\alpha f_\alpha z^{|\alpha|}.
 \tag{5}
\]
This polynomial definition does not presume boundary values for
arbitrary Hardy functions on a product-null curve.

## Exact adjoint domain and closability

For \(h\in L^2(A,\mu_A;\mathcal E_F)\), set
\[
 \widehat h_A(n)=\int_A z^{-n}h(z)\,d\mu_A(z),\qquad
 N_{n,d}=\binom{n+d-1}{d-1}.
\]
Testing (5) coefficient by coefficient, with inner products
conjugate-linear in the first argument, gives exactly
\[
 \operatorname{Dom}T_A^*
 =\left\{h:\sum_{n\ge0}N_{n,d}
                  \|\widehat h_A(n)\|^2<\infty\right\},
 \qquad (T_A^*h)_\alpha
       =\overline{\lambda^\alpha}\widehat h_A(|\alpha|).
 \tag{6}
\]
Necessity follows by testing arbitrary finite coefficient arrays;
sufficiency follows by Cauchy--Schwarz in their square-summable
coefficient space. Each degree has exactly \(N_{n,d}\) indices.

Finite sums \(h(z)=\sum_l\phi_l(z)e_l\), with
\(\phi_l\in C_c^\infty(A)\) and \(e_l\in\mathcal E_F\),
belong to (6). Their zero extensions to the circle are smooth, so
integration by parts gives Fourier decay of every polynomial
order, while \(N_{n,d}=O((n+1)^{d-1})\). These finite sums are
dense in the target \(L^2\) space. The dense-adjoint-domain
criterion therefore proves that \(T_A\) is closable.

Let \(\overline T_A=T_A^{**}\), and define on
\(\mathcal U_F^{-1}\operatorname{Dom}\overline T_A\)
\[
 Q_A(f,g)=\langle\overline T_A\mathcal U_F f,
                    \overline T_A\mathcal U_F g\rangle.
 \tag{7}
\]
This specifies the domain by the closure of an explicit densely
defined operator, with the adjoint domain fully characterized in
(6). The graph norm makes (7) a closed positive form. Polynomials
are a form core by construction. Bounded restriction of the
full-circle trace alone would not justify this closure step:
composition with a bounded map need not preserve closability.

On polynomials,
\[
 T_A M_{z_j}=\lambda_j M_zT_A,
 \qquad T_A(I\otimes R_q)=(I\otimes R_q)T_A.
 \tag{8}
\]
Both sides' source and target shifts are bounded. Passing along
graph-convergent polynomial sequences proves (8) on the entire
closed domain, its forward invariance, and all-prime covariance
of (7). No backward invariance of the original form domain is
asserted or needed.

## Energy completion, unboundedness and singularity

The energy completion is the entire
\(L^2(A,\mu_A;\mathcal E_F)\). To verify dense range without
assuming it, (5) already contains every one-variable polynomial
with coefficients in \(\mathcal E_F\). On \(\overline A\),
\[
 z^{-1}=z_0^{-1}\sum_{k\ge0}
                \left(-\frac{z-z_0}{z_0}\right)^k
 \tag{9}
\]
converges uniformly by (4). Hence the uniform closure of analytic
polynomials contains Laurent polynomials and therefore all
continuous functions on the arc, by Stone--Weierstrass.
Continuous functions are dense in \(L^2(A,\mu_A)\); finite
vector-valued sums prove the range assertion.

Consequently the induced selected shifts and their adjoints are
\[
 S_{p_j}=\lambda_j M_z,\qquad
 S_{p_j}^*=\overline{\lambda_j}M_{\bar z}.
 \tag{10}
\]
They are unitaries on this energy completion, although the source
operators in (3) are pure isometries.

For a unit \(e\in\mathcal E_F\), take
\[
 f_n=N_{n,d}^{-1/2}\sum_{|\alpha|=n}
          \overline{\lambda^\alpha}\,e z^\alpha.
 \qquad \|f_n\|^2=1,
 \qquad Q_A[\mathcal U_F^{-1}f_n]=N_{n,d}\longrightarrow\infty.
 \tag{11}
\]
Thus every such form is unbounded for \(d\ge2\), independently
of arc length after the chosen normalization.

At the constant vector \(e\), the original orbit has product-Haar
measure, whereas the new orbit satisfies
\[
 Q_A(W^\alpha e,W^\beta e)
 =\overline{\lambda^\alpha}\lambda^\beta
       \int_A z^{|\beta|-|\alpha|}\,d\mu_A(z).
 \tag{12}
\]
Here and below \(e\) also denotes its inverse image under (3).
The new measure is the pushforward of \(\mu_A\) by
\(z\mapsto(\lambda_1z,\ldots,\lambda_dz)\). It has mass
one and is supported on a product-Haar-null curve. Thus it is
singular, but every one-coordinate marginal remains absolutely
continuous. There is no conflict with one-variable Toeplitz
closability.

## Choosing either strict block sign

Equations (1) and (10) identify the block with multiplication by
the real continuous function
\[
 w_{B,\lambda}(z)=\sum_{p_j\in B}(\log p_j)
   \left(1-\frac{1-p_j^{-1}}
                    {|1-\lambda_jz/\sqrt{p_j}|^2}\right).
 \tag{13}
\]
The series defining each ray converges in norm. Its full-circle
mean is zero. It is nonzero for every choice of phases: putting
\(t_j=\lambda_j/\sqrt{p_j}\), the analytic Fourier coefficients
are \(-c_k\), where
\(c_k=\sum_{p_j\in B}(\log p_j)t_j^k\).
The nonzero \(t_j\) have distinct moduli, and the Vandermonde
matrix \((t_j^k)_{1\le k\le |B|,\ p_j\in B}\) is invertible.
Thus \(c_1,\ldots,c_{|B|}\) cannot all vanish.

A nonzero real continuous function of mean zero has both strict
signs. Choose short open arcs \(A_+\) and \(A_-\), satisfying
(4), whose closures lie respectively in its positive and negative
sets. Compactness gives
\[
 \epsilon_+=\min_{\overline A_+}w_{B,\lambda}>0,
 \qquad \epsilon_-=-\max_{\overline A_-}w_{B,\lambda}>0.
\]
Applying (5)--(12) to these arcs proves (1). Both choices preserve
the source, panel, phases, covariance and normalization. Their
strict signs are selected by the chosen output arc measures.
If all phases equal one, arcs near \(-1\) and \(1\)
even give the two opposite strict signs for every ray in the
fixed panel simultaneously.

## Controls, prior art and consequence

Three boundaries prevent a false extrapolation.

1. For the full circle, analytic polynomials close to \(H^2\),
   not \(L^2\); the selected shifts are unilateral. WP-455's
   finite two-sign witnesses then apply. The proper-arc change
   in (9)--(10) is mathematically material.
2. For \(d=1\), arc restriction is bounded and its measure is
   absolutely continuous. The joint singularity and growth (11)
   require \(d\ge2\).
3. Replacing an arc by a point does not give another closed form.
   At \(z_0\), the polynomial
   \(g_n=N_{n,d}^{-1}\sum_{|\alpha|=n}
   \overline{\lambda^\alpha z_0^n}e z^\alpha\)
   has original squared norm \(1/N_{n,d}\to0\) and point trace
   exactly \(e\). Its trace differences vanish, violating
   closability. Positive arc length and the dense smooth adjoint
   tests cannot be replaced by an atomic character.

Rudin's diagonal restriction is classical; the coefficient count
and the bidisc Hardy-to-Bergman identity are recorded in
Brevig--Gómez-Serrano--Ortega-Cerdà--Seip, equation (1.2).
Teschl's Lemma 2.4(ii) supplies the adjoint criterion used in (6).
Panja's Theorem 1.2 concerns bounded invariant metrics;
Yafaev's Theorem 1.3 concerns a single Toeplitz coordinate.
Neither theorem asserts joint absolute continuity here.
The smooth Fourier-decay and short-arc approximation arguments
are classical and have been written out rather than imported as
a new restriction theorem. Targeted searches on diagonal
restriction, closable Toeplitz forms and Bergman boundary traces
do not certify historical novelty.

The local delta is the verified **closed singular** sign-selection
control excluded from WP-455. WP-452 already permits bounded
finite-panel sign selection; this construction shows that moving
to a singular closed trace category does not supply the missing
source selection either. It works for any doubly commuting pure
finite isometry panel with nonzero common wandering space, and
the sign proof needs only distinct radii in \((0,1)\) and nonzero
real weights. No zero data or prime-specific sign principle enters.

A standard-library scratch diagnostic passed 4,710 finite
coefficient, arc-covariance, norm-growth, Fourier-sign and
inverse-approximation checks for panels of two to four primes,
with aligned and random phases. The largest relative discrepancy
was below \(2.5\times10^{-10}\), from arc quadrature. These
checks do not establish closability or an infinite-dimensional
limit; (6)--(10) supply those analytic arguments exactly.

The infinite separate-ray obstruction of WP-453 and the bounded
block obstruction of WP-454 remain intact. A general unbounded
infinite-block theorem, or a genuine arithmetic positive
completion, still requires additional input. Closedness alone
cannot promote a chosen singular phase arc to an intrinsic
geometric sign law.

## References

- [WP-452](WP-452-bounded-covariant-energies-cannot-orient-infinitely-many-prime-rays.md), the fixed finite-panel model and bounded arc controls.
- [WP-453](WP-453-closability-forbids-infinite-prime-ray-orientation.md), the separate-ray obstruction for arbitrary dense closable domains.
- [WP-454](WP-454-bounded-covariant-energies-retain-negative-dyadic-prime-blocks.md), the bounded infinite-block result.
- [WP-455](WP-455-closed-diagonal-trace-energies-lock-prime-phases-but-retain-both-weil-signs.md), the full-circle trace and phase-independent sign certificate.
- O. F. Brevig, J. Gómez-Serrano, J. Ortega-Cerdà and K. Seip, *Contractivity of Rudin's diagonal restriction operator for H^p of the polydisc*, arXiv:2610.16227v1 (2026), equation (1.2), [author preprint](https://arxiv.org/pdf/2610.16227v1).
- G. Teschl, *Mathematical Methods in Quantum Mechanics*, second edition, Graduate Studies in Mathematics **157**, AMS (2014), Lemma 2.4(ii), [authorized author text](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
- S. Panja, *Factorization of Toeplitz operators*, New York Journal of Mathematics **29** (2023), 848--873, Theorem 1.2, [journal text](https://nyjm.albany.edu/j/2023/29-33v.pdf).
- D. R. Yafaev, *On semibounded Toeplitz operators*, Journal of Operator Theory **77** (2017), no. 1, 205--216, Theorem 1.3, [journal text](https://jot.theta.ro/jot/archive/2017-077-001/2017-077-001-012.pdf).
