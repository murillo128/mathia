---
title: "WP-455: Closed diagonal-trace energies lock prime phases but retain both Weil signs"
type: research-finding
status: verified
research_question: "Can a singular joint orbit measure from a closed covariant energy orient a finite Weil block by locking its prime phases?"
claim_strength: exact_closed_unbounded_phase_locking_construction_and_finite_sign_certificate
scope: full-circle diagonal restrictions on finite prime panels in the fixed Maharam representation; no general unbounded-block theorem
finding_id: WP-455
related_findings:
  - WP-452
  - WP-453
  - WP-454
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
  - sign-obstruction
---

# WP-455: Singular phase locking is compatible with closed energy, but does not fix the block sign

## Claim and boundary

**EXACT-DERIVED; CLASSICAL DIAGONAL-RESTRICTION CONSTRUCTION;
CATEGORY AND SIGN BOUNDARY.** For every finite prime set
\(F=\{p_1,\ldots,p_d\}\), \(d\ge2\), and arbitrary phases
\(\lambda_j\in\mathbb T\), there is a nonzero densely defined
**closed**, unbounded positive form \(Q_{F,\lambda}\) on the
Maharam space of WP-452. Its domain is invariant under every
integer source isometry and
\[
 Q_{F,\lambda}[W_m f]=Q_{F,\lambda}[f]\qquad(m\ge1).
 \tag{1}
\]
In its quotient energy space the selected prime isometries satisfy
\[
 S_{p_j}=\lambda_j M_z\otimes I,\qquad
 \lambda_i^{-1}S_{p_i}=\lambda_j^{-1}S_{p_j}.
 \tag{2}
\]
Their joint orbit measure at a wandering vector is supported on
the one-dimensional torus
\(\{(\lambda_1z,\ldots,\lambda_dz):z\in\mathbb T\}\).
It is singular relative to the original orbit measure, despite
closedness of the form in the original Hilbert norm.

Nevertheless, for every nonempty \(B\subset F\), the unchanged
critical Weil block, with **energy-space adjoints**,
\[
 D_{B,Q}=-\sum_{p_j\in B}(\log p_j)
       \sum_{k\ge1}p_j^{-k/2}(S_{p_j}^k+S_{p_j}^{*k}),
 \tag{3}
\]
has strictly positive and strictly negative quadratic values.
For any phases, a witness uses only the vacuum and one shift of
degree at most \(|B|\).

This answers a particular unbounded completion test left outside
WP-454. Closability does not supply its bounded orbit-measure
domination, even at a finite panel. The explicit singular
completion here still fails the sign test. The theorem does not
extend WP-454 to all closable forms, settle infinitely many block
signs, or cover restrictions of the output to selected phase arcs.
No Gamma/polar completion, RH consequence, historical novelty,
formal verification or independent adversarial approval is claimed.

## Actual source and finite-panel model

Keep the source normalization explicit:
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(a)=(1-p^{-1})p^{-a},\qquad
 \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds),
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\quad
 (U_ch)(s)=e^{-c/2}h(s-c),\quad W_p=V_p\otimes U_{\log p}.
 \tag{4}
\]
These are doubly commuting isometries. Let \(\mathcal E_F\)
be the nonzero subspace supported on \(J_{p_j}=0\) for every
\(p_j\in F\). The subspaces \(W^\alpha\mathcal E_F\) are
exactly the valuation shells \(J_F=\alpha\); the real translation
is invertible within each shell. Consequently
\[
 \mathcal K=\bigoplus_{\alpha\in\mathbb N_0^d}
                 W^\alpha\mathcal E_F
 \xrightarrow{\ \mathcal U_F\ }
 H^2(\mathbb D^d;\mathcal E_F),\qquad
 W_{p_j}\longmapsto M_{z_j}.
 \tag{5}
\]
For \(q\notin F\), \(W_q\) preserves \(\mathcal E_F\) and
commutes with all selected shifts and their adjoints. Thus it
becomes \(I\otimes R_q\), with \(R_q\) an isometry on
\(\mathcal E_F\). This is the concrete Wold decomposition already
proved in WP-452, not an assumption about the new energy adjoints.

## Closed diagonal trace and its exact domain

For \(f(z)=\sum_\alpha f_\alpha z^\alpha\) in the Hardy space
in (5), define
\[
 b_n(f)=\sum_{|\alpha|=n}\lambda^\alpha f_\alpha,\qquad
 \mathcal D_\lambda=
 \left\{f:\sum_{n\ge0}\|b_n(f)\|_{\mathcal E_F}^2<\infty\right\},
\]
\[
 T_\lambda f=\sum_{n\ge0}b_n(f)z^n
       \in H^2(\mathbb D;\mathcal E_F).
 \tag{6}
\]
On polynomials this is exactly
\(f(z_1,\ldots,z_d)\mapsto f(\lambda_1z,\ldots,\lambda_dz)\).
Equation (6), rather than a pointwise boundary trace of an arbitrary
Hardy function, defines the unbounded operator.

Each fixed degree has only finitely many multiindices. Hence
\(b_n\) is a bounded coefficient map on the original Hardy space.
If \(f_l\to f\) there and \(T_\lambda f_l\to g\) in the
one-variable Hardy space, coefficient convergence forces
\(g_n=b_n(f)\) for every \(n\). Thus \(f\in\mathcal D_\lambda\)
and \(T_\lambda f=g\): the operator is closed. Polynomials with
\(\mathcal E_F\)-valued coefficients are dense. Truncation by
total degree converges in both the original norm and the output
norm, so they are a graph core as well.

The operator is onto: for \(g(z)=\sum_n g_nz^n\), the input
\(f(z_1,\ldots,z_d)=\sum_n\lambda_1^{-n}g_nz_1^n\)
has the same norm and satisfies \(T_\lambda f=g\).

Define the form on \(\mathcal U_F^{-1}\mathcal D_\lambda\) by
\[
 Q_{F,\lambda}(f,g)=
 \langle T_\lambda\mathcal U_F f,
         T_\lambda\mathcal U_F g\rangle,
 \tag{7}
\]
with conjugate-linearity in the first argument. It is closed because
its form norm is the graph norm of the closed operator in (6).
Its quotient energy completion identifies with the entire output
Hardy space by surjectivity.

The coefficient formulas give, on the full domain,
\[
 T_\lambda M_{z_j}=\lambda_j M_zT_\lambda,
 \qquad
 T_\lambda(I\otimes R_q)=(I\otimes R_q)T_\lambda.
 \tag{8}
\]
They prove domain invariance, (1), and (2). In particular the
construction has covariance for all primes, including the
unselected spectators.

To see unboundedness, let \(e\in\mathcal E_F\) be a unit vector,
put \(N_{n,d}=\binom{n+d-1}{d-1}\), and set
\[
 f_n=N_{n,d}^{-1/2}
       \sum_{|\alpha|=n}\overline{\lambda^\alpha}\,e z^\alpha.
 \qquad
 \|f_n\|^2=1,\quad \|T_\lambda f_n\|^2=N_{n,d}\longrightarrow\infty.
 \tag{9}
\]
This is unbounded growth along finite-degree vectors, not a
nonclosability sequence: their outputs escape to increasing degree.

## A singular joint measure in a closed energy

Choose a unit vector \(e\in\mathcal E_F\), viewed as a constant
in (5). Its original source orbit has
\(\langle W^\alpha e,W^\beta e\rangle=\delta_{\alpha,\beta}\),
so its finite-torus Herglotz measure is product Haar measure.
Its new orbit instead satisfies
\[
 Q(W^\alpha e,W^\beta e)
 =\overline{\lambda^\alpha}\lambda^\beta
       1_{|\alpha|=|\beta|}.
 \tag{10}
\]
These are exactly the moments of the pushforward of circle Haar
measure under \(z\mapsto(\lambda_1z,\ldots,\lambda_dz)\).
For \(d\ge2\) that torus curve has product Haar measure zero:
already its first two coordinates satisfy
\(z_2=(\lambda_2/\lambda_1)z_1\), a product-null condition.

Thus no finite constant can dominate this new orbit measure by
the original one. Replacing boundedness by closability in WP-454's
domination step is invalid without a new argument. Yafaev's
one-variable closability/absolute-continuity theorem is not a
multivariable joint-measure theorem. Each single coordinate of
(10) still has Haar marginal, consistent with the one-variable
boundary and with WP-453.

## Every phase-locked finite block still has both signs

Write \(S=M_z\otimes I\) on the energy space. For a nonempty
\(B\subset F\), let
\[
 t_j=\lambda_j/\sqrt{p_j},\qquad
 c_k=\sum_{p_j\in B}(\log p_j)t_j^k.
\]
Then (3) becomes the norm-convergent series
\[
 D_{B,Q}=-\sum_{k\ge1}(c_kS^k+\overline{c_k}S^{*k}).
 \tag{11}
\]
If \(b=|B|\), at least one of \(c_1,\ldots,c_b\) is nonzero.
Indeed the \(t_j\) are nonzero and distinct, since distinct primes
give different moduli. The matrix \((t_j^k)_{1\le k,j\le b}\)
has determinant
\(\big(\prod_jt_j\big)\prod_{i<j}(t_j-t_i)\ne0\).
Vanishing of all these coefficients would therefore force every
\(\log p_j\) to vanish, a contradiction.

Choose such a \(k\), a unit wandering vector
\(v=1\otimes e\in\ker S^*\), and
\(\eta=c_k/|c_k|\). Orthogonality of its unilateral orbit gives
\[
 x_\pm=v\pm\eta S^kv,\qquad \|x_\pm\|^2=2,\qquad
 \boxed{\langle x_\pm,D_{B,Q}x_\pm\rangle=\mp2|c_k|.}
 \tag{12}
\]
Only the \(k\)-th term in (11) contributes. The witnesses have
polynomial preimages under (6), so both signs occur on actual
finite source vectors in the form domain.

Equivalently, the block has continuous Toeplitz symbol
\[
 w_{B,\lambda}(z)=\sum_{p_j\in B}(\log p_j)
 \left(1-\frac{1-p_j^{-1}}{|1-\lambda_j z/\sqrt{p_j}|^2}\right).
 \tag{13}
\]
It has mean zero and is nonconstant by the same Vandermonde
argument. Formula (12) supplies an exact finite sign certificate
without numerical boundary localization. Arbitrary phase choices
can change the coefficients, but cannot make this block positive.

## Prior art, controls and consequence

Diagonal restriction on polydisc Hardy spaces is classical. In
the bidisc, Rudin's coefficient argument maps \(H^2(\mathbb D^2)\)
contractively to the **Bergman** space of the disc; the squared
target norm there is \(\sum_n\|b_n\|^2/(n+1)\).
Brevig--Gómez-Serrano--Ortega-Cerdà--Seip reproduce this identity
in equation (1.2) of their 2026 preprint and attribute the
\(p=2\) case to Rudin, Exercise 3.4.4(e). Here the target is
\(H^2\), whose stronger norm gives the closed unbounded domain
(6). No new general diagonal-restriction theorem is claimed.

Panja's Theorem 1.2 concerns bounded positive invariant metrics
and bounded intertwiners. Equations (6)--(10) exhibit why its
bounded category and WP-454's measure domination cannot simply
be inferred from closedness. Yafaev's Theorem 1.3 concerns one
shift; (10) identifies the distinct joint-measure issue explicitly.
Targeted literature searches for diagonal restriction, polydisc
Toeplitz forms and closable intertwiners support this classical
classification, not a historical novelty claim.

The local contribution is the exact source realization of this
singular closed completion, together with the phase-independent
finite Weil sign certificate (12). The selected finite panel and
its phases are freely chosen data; covariance and closedness do
not make their correlation arithmetic or canonical. The same
construction works for any finite family of doubly commuting
pure isometries with nonzero common wandering space. The sign
argument needs only distinct radii in \((0,1)\) and nonzero real
ray weights, not primes or zeta zeros.

A standard-library diagnostic outside Git passed 445 coefficient,
covariance, shell-norm, Fourier and finite-sign checks for panels
of two to four primes and aligned/random phases. The largest
relative discrepancy was below \(4.2\times10^{-15}\). These finite
checks validate formulas and conventions only; the closed-domain,
singularity and all-phase statements follow from (6)--(12).

WP-453's separate-ray obstruction and WP-454's bounded-block
obstruction remain unchanged. A more general unbounded block
theorem needs information beyond joint-measure domination. A
positive result would need a different source-forced operation,
such as a justified phase restriction or active global coupling,
and still an exact archimedean/polar comparison. Full-circle
diagonal phase locking supplies neither that sign nor those terms.

## References

- [WP-452](WP-452-bounded-covariant-energies-cannot-orient-infinitely-many-prime-rays.md), the actual finite-panel Wold model, bounded orbit domination and finite arc-selection controls.
- [WP-453](WP-453-closability-forbids-infinite-prime-ray-orientation.md), the separate-ray closability theorem.
- [WP-454](WP-454-bounded-covariant-energies-retain-negative-dyadic-prime-blocks.md), the bounded block theorem whose domination step is tested here.
- O. F. Brevig, J. Gómez-Serrano, J. Ortega-Cerdà and K. Seip, *Contractivity of Rudin's diagonal restriction operator for \(H^p\) of the polydisc*, arXiv:2610.16227v1 (2026), introduction and equation (1.2), [author preprint](https://arxiv.org/pdf/2610.16227v1).
- S. Panja, *Factorization of Toeplitz operators*, New York Journal of Mathematics **29** (2023), 848--873, Theorem 1.2, [journal text](https://nyjm.albany.edu/j/2023/29-33v.pdf).
- D. R. Yafaev, *On semibounded Toeplitz operators*, Journal of Operator Theory **77** (2017), no. 1, 205--216, Theorem 1.3, [journal text](https://jot.theta.ro/jot/archive/2017-077-001/2017-077-001-012.pdf).
