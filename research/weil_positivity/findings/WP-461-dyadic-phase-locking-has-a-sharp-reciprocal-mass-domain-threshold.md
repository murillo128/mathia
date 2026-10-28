---
title: "WP-461: Dyadic phase locking has a sharp reciprocal-mass domain threshold"
type: research-finding
status: verified
research_question: "Can the sparse closed phase-locking construction extend to a nonsummable family of dyadic prime blocks by changing its dense domain?"
claim_strength: exact_phase_independent_existence_classification_for_dyadic_block_locking
scope: exact scalar phase locking in the fixed Maharam representation; not arbitrary correlated energies or approximate locking
finding_id: WP-461
related_findings:
  - WP-247
  - WP-455
  - WP-459
  - WP-460
created: 2026-10-28
updated: 2026-10-28
tags:
  - weil-positivity
  - maharam-extension
  - closability
  - prime-blocks
  - phase-locking
  - infinite-tensor-product
---

# WP-461: Dense-domain freedom cannot extend exact dyadic phase locking past summable reciprocal mass

## Claim and evidence boundary

**EXACT-DERIVED; CLASSICAL PROJECTION, TENSOR-PRODUCT AND
PRIME-NUMBER-THEOREM INGREDIENTS; SHARP CATEGORY OBSTRUCTION.**
Use the fixed Maharam source defined below. Let
\(B_j=\{p:2^j\le p<2^{j+1}\}\), choose any
\(\mathcal J\subset\{3,4,\ldots\}\), and fix arbitrary
scalar phases \(\lambda_p\in\mathbb T\) for primes in these blocks.
There exists a nonzero densely defined closed nonnegative form
\(Q\) with all-prime forward-invariant domain, covariance
\(Q[W_pf]=Q[f]\), and induced energy-space relations
\[
 \lambda_p^{-1}S_p=\lambda_q^{-1}S_q
       \quad(p,q\in B_j,\ j\in\mathcal J)                 \tag{1}
\]
**if and only if**
\[
 \sum_{j\in\mathcal J}\frac1j<\infty,
 \quad\text{equivalently}\quad
 \sum_{p\in\bigcup_{j\in\mathcal J}B_j}\frac1p<\infty.   \tag{2}
\]

On the divergent side, every densely defined nonnegative
covariant form satisfying (1) has quotient map
\(T:f\mapsto[f]\in E_Q\) with
\[
 \operatorname{Dom}T^*=\{0\},\qquad
 \overline{\operatorname{Graph}T}=\mathcal K\oplus E_Q.    \tag{3}
\]
In particular, if the form is closable, it is zero.
The argument allows arbitrary dense invariant domains; it
does not assume they contain the vacuum orbit or any tensor
cylinder vectors. Those vectors are used only to test bounded
source projections, outside the form domain.

Thus WP-460's sparse-panel restriction is intrinsic to **exact
block phase locking**, rather than merely a limitation of its
common-wandering-space construction. Every choice of phases
fails on all late dyadic blocks, including its three-periodic
choice. The obstruction precedes any Weil sign calculation.
It does not classify general mixed-prime correlations, approximate
locking, shrinking relative-width blocks, different representations,
or archimedean/polar completions. No RH consequence, historical
novelty, Lean verification or independent adversarial approval
is claimed.

## Source, adjoint relations and the Hilbert representation

Keep exactly the source of WP-455 and WP-460:
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(a)=(1-p^{-1})p^{-a},
 \qquad\mathcal K=L^2(\Omega,\nu)\otimes L^2(\mathbb R,e^sds),
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\quad
 (U_ch)(s)=e^{-c/2}h(s-c),\quad W_p=V_p\otimes U_{\log p}.
                                                               \tag{4}
\]
Covariance and polarization give commuting isometries
\(S_pTf=TW_pf\) on \(E_Q\), without assuming closability.
Equation (1) implies
\[
 T(W_p-(\lambda_p/\lambda_q)W_q)f=0
                   \quad(f\in\operatorname{Dom}Q).
\]
For \(u\in\operatorname{Dom}T^*\), density of
\(\operatorname{Dom}Q\) in the source therefore gives
\[
 (W_p^*-(\overline{\lambda_p}/\overline{\lambda_q})W_q^*)T^*u=0.
                                                               \tag{5}
\]
No density of \(\operatorname{Dom}T^*\) is used at this
stage. We will show that the simultaneous source kernel in
(5) is zero when (2) diverges.

The local unitary
\[
 L^2(\mathbb N_0,\nu_p)\longrightarrow\ell^2(\mathbb N_0),
 \qquad f(a)\longmapsto\sqrt{(1-p^{-1})p^{-a}}f(a)
\]
sends \(V_p\) to the unilateral shift \(L_p\) and the
constant function to the unit vector
\[
 \kappa_p=\sqrt{1-r_p^2}\sum_{a\ge0}r_p^ae_a,
 \qquad r_p=p^{-1/2}.
\]
Consequently \(L^2(\Omega,\nu)\) is the incomplete tensor
product with reference vectors \(\kappa_p\): finite changes
of those reference vectors span a dense subspace. This follows
directly from density of finite-coordinate cylinder functions.
It is not the tensor sector with all local vacua \(e_0\).

Multiplication by \(e^{s/2}\), followed by the Fourier transform
with kernel \(e^{-its}\), sends \(U_c\) to multiplication
by \(e^{-itc}\). Hence in the direct integral over real \(t\),
\[
 W_p(t)=e^{-it\log p}L_p,
 \qquad\gamma_p(t)=\lambda_pe^{it\log p}.                \tag{6}
\]
The fibrewise version of (5) is
\(\gamma_p(t)L_p^*v=\gamma_q(t)L_q^*v\).
The real translations have thus been retained exactly.

## Every full dyadic block loses a definite amount of reference mass

Fix a finite block \(B=B_j\), of size \(d\). In its local
tensor space define
\[
 R_B(t)=\bigcap_{p,q\in B}\ker(\gamma_p(t)L_p^*-
                                      \gamma_q(t)L_q^*),
\]
and let \(P_B(t)\) be its orthogonal projection. The space
is graded by total occupation. In degree \(n\) its vectors
are exactly
\[
 v_\alpha=c_n\overline{\gamma(t)^\alpha},
                         \qquad |\alpha|=n.             \tag{7}
\]
Indeed the adjoint equations equate coefficients after moving
one occupation from one coordinate to another; these moves
connect every pair of degree-\(n\) multiindices. Conversely,
(7) satisfies every equation. This also constructs a measurable
projection field, degree by degree.

Let \(\kappa_B=\bigotimes_{p\in B}\kappa_p\) and
\(c_B^2=\prod_{p\in B}(1-p^{-1})\). Its degree-one
coefficient vector is \(c_B(r_p)_{p\in B}\). Projection
onto (7) in that degree loses exactly
\[
 c_B^2\left(\sum_{p\in B}r_p^2-
           \frac1d\left|\sum_{p\in B}\gamma_p(t)r_p\right|^2\right).
\]
Losses in every other degree are nonnegative. The triangle
inequality therefore gives the uniform, phase-independent bound
\[
 1-\|P_B(t)\kappa_B\|^2\ \ge\ a_j,
 \qquad
 a_j:=c_B^2\left(\sum_{p\in B}\frac1p-
              \frac{(\sum_{p\in B}p^{-1/2})^2}{d}\right).
                                                               \tag{8}
\]
This is a radial variance, rather than a phase-cancellation
estimate. Even optimally aligned phases cannot remove it.

For \(x=2^j\), the prime number theorem and partial summation give
\[
 d\sim\frac{x}{\log x},\qquad
 \sum_{x\le p<2x}p^{-1/2}\sim
      2(\sqrt2-1)\frac{\sqrt x}{\log x},\qquad
 \sum_{x\le p<2x}\frac1p\sim\frac{\log2}{\log x}.
                                                               \tag{9}
\]
Also \(c_B^2\to1\), since
\(1-c_B^2\le\sum_{p\in B}1/p\to0\). Thus
\[
 a_j\sim\frac{c_*}{j\log2},\qquad
 c_*:=\log2-4(\sqrt2-1)^2>0.                            \tag{10}
\]
Strict positivity is exact: on \([1,2]\), strict
Cauchy--Schwarz for the nonconstant function \(u^{-1/2}\)
says
\(\int_1^2u^{-1}du>(\int_1^2u^{-1/2}du)^2\).
No numerical approximation is needed for the sign of \(c_*\).
Equations (9) also establish the equivalence in (2).

## Divergent block loss annihilates the simultaneous source kernel

For disjoint blocks the projections \(P_{B_j}(t)\) commute
and act on different local tensor factors. Suppose
\(\sum_{j\in\mathcal J}1/j=\infty\). For a finite tensor
cylinder supported on a finite prime set \(F_0\), all but
finitely many selected blocks miss \(F_0\). On any finite
collection \(A\) of those blocks, (8) gives
\[
 \left\|\prod_{j\in A}P_{B_j}(t)v\right\|^2
 \le\|v\|^2\prod_{j\in A}(1-a_j)
 \le\|v\|^2\exp\!\left(-\sum_{j\in A}a_j\right).        \tag{11}
\]
This remains true for a cylinder multiplied by an arbitrary
square-integrable function of \(t\), after integration,
because the bound is uniform in \(t\). Such vectors span
a dense subspace of the actual source Hilbert space.

The right side tends to zero along the selected tail by (10).
If \(v_0\) belongs to every source kernel in (5), its Fourier
fibres belong to every \(R_{B_j}(t)\). Therefore, for any
test cylinder \(v\),
\[
 \langle v_0,v\rangle
   =\left\langle v_0,\prod_{j\in A}P_{B_j}v\right\rangle
   \longrightarrow0.
\]
Density proves \(v_0=0\). We have proved a zero intersection
of bounded source kernels, without any form-domain approximation.

Apply this to (5): \(T^*u=0\) for every
\(u\in\operatorname{Dom}T^*\). Since \(T\) has dense
range in its energy completion, such \(u\) must itself be
zero. Hence \(\operatorname{Dom}T^*=\{0\}\). The
orthogonal complement of its graph is
\(\{(-T^*u,u):u\in\operatorname{Dom}T^*\}\), proving
(3). If \(T\) is closable, its adjoint domain is dense,
so \(E_Q=\{0\}\). A nonnegative form is closable exactly
when its quotient map is closable, by the graph-sequence
definitions. This proves the necessary half of (2).

## Summable reciprocal mass gives an exact closed realization

For completeness, the sufficient half is the domain construction
of WP-460, which does not depend on its special phases or
exponentially sparse choice of indices. Put
\(F=\bigcup_{j\in\mathcal J}B_j\). When (2) converges,
\[
 \nu\{J_p=0\text{ for every }p\in F\}
      =\prod_{p\in F}(1-p^{-1})>0.
\]
Its supported subspace \(\mathcal E_F\subset\mathcal K\)
is nonzero. Almost every selected occupation has finite support,
since the tail probability of any nonzero selected coordinate
is at most the corresponding tail of \(\sum_{p\in F}1/p\).
The orthogonal shells \(W^\alpha\mathcal E_F\) exhaust
\(\mathcal K\), identifying it with
\(\ell^2(\mathbb N_0^{(F)};\mathcal E_F)\).

Group a source multiindex by block totals
\(\pi(\alpha)_j=\sum_{p\in B_j}\alpha_p\), and define
\[
 (Af)_\beta=\sum_{\pi(\alpha)=\beta}\lambda^\alpha f_\alpha,
 \qquad
 \operatorname{Dom}A=
 \{f:\sum_\beta\|(Af)_\beta\|^2<\infty\}.              \tag{12}
\]
Every fibre is finite. Coordinate convergence proves closedness;
finite arrays give density and a graph core, by truncating whole
fibres. Choosing one source multiindex in each fibre gives an
isometric right inverse, so the range is the entire target
coefficient space. Thus \(Q[f]=\|Af\|^2\), transported
back to \(\mathcal K\), is a nonzero densely defined closed
form. The coefficient formula gives
\(AL_p=\lambda_pL_jA\) for \(p\in B_j\). Primes outside
\(F\) act isometrically on \(\mathcal E_F\) and commute
with (12). These identities on the graph core extend to its
full closed domain and establish all-prime covariance and (1).
This proves sufficiency for every prescribed phase family.

## Controls, prior art and consequence

The fixed-width dyadic geometry is essential to (10). A family
of much thinner blocks can have smaller radial variance; merely
diverging reciprocal-prime mass is not asserted to obstruct
every arbitrary partition. Scalar phases can be arbitrary and
may differ in every block. The proof is uniform in them and in
the real Fourier parameter. Exact locking is essential: a small
error in (1) does not give the exact adjoint kernel (5).

WP-460 remains valid in its summable regime. Its three-phase
norm suppression cannot be extended to all late dyadic blocks
by changing only the dense form domain while preserving exact
locking. WP-459's vacuum-orbit and strict-margin hypotheses are
unneeded here because the new hypothesis is an exact operator
relation, rather than its block sign inequality. The present
result therefore does not close its general arbitrary-domain
sign question. Singularity of a joint measure alone is still
insufficient to prove nonclosability, as WP-455 demonstrates.

The infinite-product loss mechanism is classical, in the
incomplete-tensor framework of von Neumann; the degreewise
diagonal projection is the same elementary coefficient geometry
underlying Rudin's diagonal restriction. Teschl's dense-adjoint
criterion supplies the final domain bridge. All needed special
cases are proved above. WP-247 already records a related
reference-sector obstruction for product deformations; it does
not establish the simultaneous adjoint-kernel obstruction for
arbitrary dense-domain intertwiners proved here.

The derived local contribution is the sharp dyadic threshold
(2), with the positive radial-variance constant (10), for the
actual Maharam source and arbitrary phases. Targeted literature
checks on infinite tensor products, diagonal Hardy restrictions,
quotient modules and closable intertwiners support classification
as an application of classical tools, not a historical novelty
claim. The same projection argument applies to nonarithmetic
product-shift controls whenever their block radial variances have
a divergent sum. It is not an arithmetic sign theorem.

A standard-library diagnostic in scratch passed 201 checks:
the homogeneous adjoint-kernel coefficients for two to four
coordinates through degree four; randomized-phase projection
loss bounds; and strictly positive radial losses on the sixteen
blocks \(3\le j\le18\). These are finite consistency checks.
The infinite intersection, sharp threshold and arbitrary-domain
conclusions rely on the proofs, not on numerical extrapolation.

## References

- [WP-460](WP-460-sparse-closed-diagonal-traces-admit-summable-prime-block-repairs.md), sparse closed trace and selected-block norm suppression.
- [WP-455](WP-455-closed-diagonal-trace-energies-lock-prime-phases-but-retain-both-weil-signs.md), finite diagonal trace and its sign boundary.
- [WP-459](WP-459-analytic-exponential-separators-rule-out-orbit-domain-block-orientation.md), the distinct sign-margin obstruction.
- [WP-247](WP-247-critical-all-prime-nonspherical-deformations-leave-the-canonical-restricted-tensor-sector.md), neighboring reference-sector product-deformation obstruction.
- J. von Neumann, *On infinite direct products*, Compositio Mathematica **6** (1939), 1--77, Part II, [original paper](https://www.numdam.org/article/CM_1939__6__1_0.pdf).
- O. F. Brevig, J. Gómez-Serrano, J. Ortega-Cerdà and K. Seip, *Contractivity of Rudin's diagonal restriction operator for H^p of the polydisc*, arXiv:2610.16227v1 (2026), equation (1.2), [author preprint](https://arxiv.org/pdf/2610.16227v1).
- G. Teschl, *Mathematical Methods in Quantum Mechanics*, second edition, AMS (2014), Lemma 2.4(ii), [author text](https://radon.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
- NIST Digital Library of Mathematical Functions, [equation 27.2.3](https://dlmf.nist.gov/27.2.E3), the prime number theorem used in (9).
