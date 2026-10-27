---
title: "WP-460: Sparse closed diagonal traces admit summable prime-block repairs"
type: research-finding
status: verified
research_question: "Does WP-454's variance-scale negative floor survive for arbitrary closed unbounded covariant energies?"
claim_strength: exact_counterexample_on_a_sparse_infinite_family_of_dyadic_blocks
scope: chosen phase-correlated closed domains and selected blocks only; no source-forced or all-prime Weil positivity
finding_id: WP-460
related_findings:
  - WP-453
  - WP-454
  - WP-455
  - WP-456
  - WP-459
created: 2026-10-27
updated: 2026-10-27
tags:
  - weil-positivity
  - maharam-extension
  - closed-form
  - diagonal-restriction
  - prime-blocks
  - matched-control
---

# WP-460: Closed domains can suppress infinitely many block defects at summable cost

## Claim and evidence boundary

**EXACT-DERIVED; CLASSICAL RESTRICTION AND SUMMATION-BY-PARTS
INGREDIENTS; MATCHED CATEGORY COUNTEREXAMPLE.** On the same
Maharam source as WP-453--WP-459, for every \(\eta>0\) there
exist a nonzero densely defined closed unbounded nonnegative
form \(Q\), an infinite set of dyadic indices \(\mathcal J\),
and positive numbers \(\epsilon_j\), such that:

- the full form domain is invariant under every prime source
  isometry \(W_p\), and \(Q[W_pf]=Q[f]\);
- on its energy completion, with induced isometries \(S_p\)
  and **energy-space adjoints**, the unchanged finite defects
  \[
  D_{B_j,Q}=-\sum_{p\in B_j}(\log p)
                  \sum_{k\ge1}p^{-k/2}(S_p^k+S_p^{*k}),
  \qquad B_j=\{p:2^j\le p<2^{j+1}\},                    \tag{1}
  \]
  satisfy
  \[
  \|D_{B_j,Q}\|\le\epsilon_j=O(j2^{-j/2}),\qquad
  \sum_{j\in\mathcal J}\epsilon_j<\eta;                 \tag{2}
  \]
- every uncorrected selected block still has both signs.

Consequently \(D_{B_j,Q}+\epsilon_j I\ge0\), and the
**block-grouped** sum
\[
 D_{\mathcal J,Q}:=\sum_{j\in\mathcal J}D_{B_j,Q}
 \quad\hbox{converges in operator norm},\qquad
 D_{\mathcal J,Q}+\Bigl(\sum_{j\in\mathcal J}\epsilon_j\Bigr)I\ge0.
                                                               \tag{3}
\]
The form is normalized by \(Q[e]=1\) at any unit common
wandering vector \(e\). Smallness in (2) is not achieved by
rescaling \(Q\).

This disproves extending WP-454's bounded-energy variance-scale
floor to every closed covariant energy: for
\(V_j=2\sum_{p\in B_j}(\log p)^2/(p-1)\sim2(\log2)^2j\),
the same nonzero \(Q\) has
\(\|D_{B_j,Q}\|/\sqrt{V_j}\to0\) along infinitely many
blocks. It also shows why a summable scalar repair on a selected
infinite subfamily need not be evidence of arithmetic structure.

The domain and phase correlations are explicitly chosen. The
construction neither makes the uncorrected blocks nonnegative
nor covers all late dyadic blocks. No inclusion of the full
natural vacuum orbit in the form domain is asserted. No
source-selection theorem, archimedean/polar completion, RH
consequence, historical novelty, Lean verification or independent
adversarial approval is claimed.

## A sparse infinite panel has a nonzero common wandering space

Keep the source, including its real translations:
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
Choose \(j_m=J+2^m\), \(m\ge1\), with \(J\) large, and set
\(\mathcal J=\{j_m:m\ge1\}\),
\(F=\bigcup_mB_{j_m}\). The prime number theorem gives
\[
 \sum_{p\in B_j}\frac1p=O(j^{-1}),\qquad
 \sum_{p\in F}\frac1p<\infty.                           \tag{5}
\]
For the first estimate it suffices to bound the number of primes
in \([2^j,2^{j+1})\) by \(O(2^j/j)\).

Let \(\mathcal E_F\) be the subspace supported where
\(J_p=0\) for all \(p\in F\). Its support has positive
measure \(\prod_{p\in F}(1-p^{-1})>0\), so
\(\mathcal E_F\ne0\). Since
\(\sum_{p\in F}\nu\{J_p\ge1\}<\infty\), the elementary
union bound on tails shows that almost every selected occupation
has finite support. The mutually orthogonal shells
\(W^\alpha\mathcal E_F\), indexed by finite-support
\(\alpha\in\mathbb N_0^{(F)}\), therefore cover \(\mathcal K\).
Each shift maps onto the corresponding shell: the valuation
scaling is isometric, and the real translation is invertible.
Thus there is a unitary coefficient identification
\[
 \mathcal U_F:\mathcal K\longrightarrow
       \ell^2(\mathbb N_0^{(F)};\mathcal E_F),\qquad
 W_p\longmapsto M_{z_p}\quad(p\in F).                  \tag{6}
\]
Here \(M_{z_p}\) just increments the \(p\)-coordinate; the
Hardy notation is optional. For \(q\notin F\), the isometry
\(W_q\) preserves \(\mathcal E_F\) and doubly commutes with
the selected shifts. It becomes \(I\otimes R_q\), with
\(R_q\) an isometry of \(\mathcal E_F\).

This is a direct shell proof of the countable version needed
here, not an unsupported extension of a finite Wold theorem.
If \(F\) were all primes, its common zero-occupation event
would have measure zero. That change invalidates (6).

## A closed trace with finite coefficient fibres

Write \(d_m=|B_{j_m}|\), and choose phases \(\lambda_p\in\mathbb T\)
below. For a source multiindex \(\alpha\), let
\(\pi(\alpha)_m=\sum_{p\in B_{j_m}}\alpha_p\). For each
finite-support target multiindex \(\beta\), the fibre
\(A_\beta=\{\alpha:\pi(\alpha)=\beta\}\) is finite, with
\[
 N_\beta=|A_\beta|=
          \prod_m\binom{\beta_m+d_m-1}{d_m-1}.          \tag{7}
\]
On source coefficient arrays define
\[
 (Tf)_\beta=\sum_{\alpha\in A_\beta}\lambda^\alpha f_\alpha,
 \quad \lambda^\alpha=\prod_{p\in F}\lambda_p^{\alpha_p},
\]
\[
 \operatorname{Dom}T=
 \left\{f\in\ell^2(\mathbb N_0^{(F)};\mathcal E_F):
       \sum_\beta\left\|\sum_{\alpha\in A_\beta}
                         \lambda^\alpha f_\alpha\right\|^2<\infty\right\}.
                                                               \tag{8}
\]
The target is \(\mathcal H=\ell^2(\mathbb N_0^{(\mathbb N)};
\mathcal E_F)\). On polynomials, (8) substitutes
\(z_p=\lambda_p u_m\) for \(p\in B_{j_m}\).

Every output coordinate in (8) is a continuous finite sum of
source coefficients. If \(f_n\to f\) and \(Tf_n\to g\)
in their respective Hilbert spaces, coordinate convergence gives
\(g_\beta=(Tf)_\beta\) for every \(\beta\). This proves
closedness on the stated maximal domain. Finite-support arrays
are dense and are a graph core: truncate by finitely many entire
fibres \(A_\beta\), which partitions both squared-norm sums.
The operator is onto. Choose one \(\alpha(\beta)\) in each
fibre and lift \(g_\beta\) to
\(f_{\alpha(\beta)}=\overline{\lambda^{\alpha(\beta)}}g_\beta\),
with all other coefficients zero. This lift preserves norm.

Let
\[
 Q(f,g)=\langle T\mathcal U_F f,T\mathcal U_F g\rangle,
 \qquad \operatorname{Dom}Q=\mathcal U_F^{-1}\operatorname{Dom}T.
                                                               \tag{9}
\]
Its graph norm makes it a densely defined closed nonnegative
form, and surjectivity identifies its energy completion with
\(\mathcal H\). On the graph core, and then by closedness,
\[
 TM_{z_p}=\lambda_p L_mT\ (p\in B_{j_m}),\qquad
 T(I\otimes R_q)=(I\otimes R_q)T\ (q\notin F),          \tag{10}
\]
where \(L_m\) increments the \(m\)-th target coordinate.
These bounded source and target isometries preserve the full
closed domain by graph approximation. Hence \(Q\) has
all-prime covariance, with \(S_p=\lambda_p L_m\) for
selected primes.

For a unit \(e\in\mathcal E_F\), the zero-degree vector
has \(Q[e]=1\). On a fibre \(A_\beta\), take
\(f_\alpha=\overline{\lambda^\alpha}e/\sqrt{N_\beta}\).
Then \(\|f\|=1\), but \(\|Tf\|^2=N_\beta\). Holding
one block with \(d_m\ge2\) fixed and letting \(\beta_m\to\infty\)
proves unboundedness. Such blocks exist for sufficiently large
\(J\) by the prime number theorem.

## Three periodic phases suppress both leading harmonics

In each selected block list the primes increasingly as
\(p_0<\cdots<p_{d-1}\), and set
\[
 \omega=e^{2\pi i/3},\qquad \lambda_{p_l}=\omega^l,
 \qquad c_{j,k}=\sum_{l=0}^{d-1}
                 (\log p_l)p_l^{-k/2}\omega^{lk}.       \tag{11}
\]
The individual coefficients in (1) have not been altered.
Rather, the imposed energy relations in (10) combine them:
\[
 D_{B_j,Q}=-\sum_{k\ge1}
                  (c_{j,k}L_m^k+\overline{c_{j,k}}L_m^{*k}).
                                                               \tag{12}
\]
For \(k=1,2\), every partial sum of \(\omega^{lk}\)
has absolute value at most one. If \(a_l\ge0\) decreases,
Abel summation therefore gives
\[
 \left|\sum_{l=0}^{d-1}a_l\omega^{lk}\right|
 \le a_{d-1}+\sum_{l=0}^{d-2}(a_l-a_{l+1})=a_0.
                                                               \tag{13}
\]
For \(x=2^j\ge8\), the functions
\((\log t)t^{-k/2}\), \(k=1,2\), decrease for \(t\ge x\).
Consequently
\[
 |c_{j,1}|\le\frac{\log x}{\sqrt x},\qquad
 |c_{j,2}|\le\frac{\log x}{x}.                          \tag{14}
\]
No cancellation estimate is needed for the remaining powers:
there are at most \(x\) integers in the block, so
\[
 \sum_{k\ge3}|c_{j,k}|
 \le\sum_{p\in B_j}\frac{(\log p)p^{-3/2}}{1-p^{-1/2}}
 \le\frac{\log(2x)}{\sqrt x(1-x^{-1/2})}.               \tag{15}
\]
Equations (12)--(15) prove (2) with the explicit choice
\[
 \boxed{\epsilon_j=2\left[
   (\log x)(x^{-1/2}+x^{-1})+
   \frac{\log(2x)}{\sqrt x(1-x^{-1/2})}\right],\quad x=2^j.}
                                                               \tag{16}
\]
The bound is summable even over all \(j\ge3\). Choose \(J\)
so that its full tail is less than \(\eta\); the selected
subfamily then satisfies (2). Absolute convergence of the
**block operator norms** proves (3). Neither arbitrary primewise
rearrangements nor absolute convergence of the individual prime
operator norms is inferred.

Every block still has both signs. Its one-coordinate continuous
Toeplitz symbol is
\[
 w_j(z)=-2\operatorname{Re}\sum_{k\ge1}c_{j,k}z^k,
                                                               \tag{17}
\]
which has zero circle mean. It is nonzero: the distinct nonzero
numbers \(t_p=\lambda_p/\sqrt p\) have distinct moduli, and
the Vandermonde matrix \((t_p^k)_{1\le k\le d,\ p\in B_j}\)
is invertible. Thus \(c_{j,1},\ldots,c_{j,d}\) cannot all
vanish. A nonzero continuous zero-mean real symbol has both
strict signs. Normalized Hardy reproducing kernels approaching
either sign arc have quadratic expectation tending to that
symbol value, because their squared boundary modulus is the
Poisson kernel. Tensoring with any unit vector in the remaining
coordinates gives both signs for (12).

## Adversarial controls and the boundary this changes

The construction passes the actual-source, dense-domain,
closedness, all-prime-covariance and exact finite-coefficient
checks. Its small repair is an operator bound on the entire
energy space, not a test at one vector or a finite matrix limit.
Nevertheless it deliberately fails the source-selection gate:
the ordered three-phase pattern and diagonal identifications
are chosen to suppress the target harmonics. Determinism of
that choice supplies no geometric theorem forcing it.

The same root-of-unity estimate works for any ordered positive
weights whose first two harmonic amplitudes decrease and whose
remaining tail obeys (15). The suppression is therefore a
generic correlation mechanism, not an arithmetic positivity law.
All-equal phases remove (13); their first coefficient is instead
\(\sum_{p\in B_j}(\log p)/\sqrt p\asymp\sqrt{2^j}\).
The small bound depends materially on the chosen correlations.

The sparse panel is equally material. Equation (5) provides the
nonzero infinite wandering space. The all-prime or all-late-block
panel has divergent reciprocal-prime mass and no such wandering
space. No replacement representation in that regime has been
constructed. Covariance under the omitted primes does not give
a bound on their defects. Equation (3) is thus not a finite-cost
completion of the full prime sum.

WP-453 remains valid because no individual prime ray is oriented.
WP-454 remains valid because \(Q\) is unbounded. WP-455's
finite trace still retains both signs, as does every block here;
the additional fact is their summably small size in a single
closed infinite-panel realization. WP-459 remains valid because
there is no strict variance-scale margin on the uncorrected
blocks and no claim about its vacuum-orbit domain hypothesis.

The surviving general question is exact nonnegativity of the
unchanged blocks, or a genuinely source-selected all-prime/global
completion. The bounded theorem cannot settle it by replacing
boundedness with closability while retaining the same quantitative
negative floor. Conversely, success after freely chosen
correlations and a small scalar repair is too weak a test.

## Prior art and validation

Rudin's diagonal restriction and its coefficient grouping are
classical; Brevig--Gómez-Serrano--Ortega-Cerdà--Seip record the
bidisc coefficient identity in equation (1.2). Sarkar provides
the finite doubly commuting Wold framework. Here the countable
shell decomposition and the maximal closed finite-fibre trace
are proved directly in (5)--(10). Abel summation with bounded
root-of-unity partial sums is classical and is explicitly (13).
The prime number theorem is used only for the sparse-panel
realization and the comparison with WP-454's variance scale;
the defect estimate (14)--(16) even bounds primes by integers.

Targeted searches on infinite-polydisc diagonal restrictions,
closed Toeplitz forms and phase-correlated multiplicative blocks
do not establish historical novelty. The derived local result
is the counterexample to a specific strengthening of WP-454,
with an exact domain and summable repairs, rather than a new
restriction theorem or a Weil sign mechanism.

A standard-library scratch diagnostic checked the first two
Fourier coefficient bounds and exact rational symbols on 12
dyadic blocks, \(3\le j\le14\), at 128 phases per block;
it also checked finite two-block trace covariance and fibre norm
growth. All 1,763 checks passed; the largest sampled
\(|w_j|/\epsilon_j\) was below 0.470. These finite checks are
only diagnostics. Closedness, density, the infinite panel,
summability and both signs follow from the proofs above, not
from numerical extrapolation.

## References

- [WP-454](WP-454-bounded-covariant-energies-retain-negative-dyadic-prime-blocks.md), the bounded-energy floor whose unbounded extension is disproved.
- [WP-455](WP-455-closed-diagonal-trace-energies-lock-prime-phases-but-retain-both-weil-signs.md), finite diagonal trace and phase-independent two-sign control.
- [WP-459](WP-459-analytic-exponential-separators-rule-out-orbit-domain-block-orientation.md), strict-margin orbit-domain obstruction and its stated boundaries.
- O. F. Brevig, J. Gómez-Serrano, J. Ortega-Cerdà and K. Seip, *Contractivity of Rudin's diagonal restriction operator for H^p of the polydisc*, arXiv:2610.16227v1 (2026), equation (1.2), [author preprint](https://arxiv.org/pdf/2610.16227v1).
- J. Sarkar, *Wold decomposition for doubly commuting isometries*, Linear Algebra and its Applications **445** (2014), 289--301, [author text](https://www.isibang.ac.in/~jay/papers/wold_n_var.pdf).
- NIST Digital Library of Mathematical Functions, [equation 27.2.3](https://dlmf.nist.gov/27.2.E3), the prime number theorem.
