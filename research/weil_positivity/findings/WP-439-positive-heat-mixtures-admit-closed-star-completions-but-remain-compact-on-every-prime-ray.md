---
title: "WP-439: Positive heat mixtures admit closed star completions above a sharp logarithmic threshold but remain compact on every prime ray"
type: research-finding
status: verified
research_question: "Can infinitely many thermal output channels evade the rank-one completion obstruction while retaining a closed all-prime form and repairing the unchanged Weil prime-ray sign?"
claim_strength: exact_positive_heat_mixture_classification_closed_star_existence_threshold_and_prime_ray_compactness_obstruction
scope: positive measures on strictly positive fractional heat times with finite energy on every basis vector in the standard positive-energy Bost--Connes representation; vacuum-plus-first-prime star completion and additive corrections of the unchanged Weil ray; no global Weil or source-canonicity theorem
finding_id: WP-439
related_findings:
  - WP-438
  - WP-437
  - WP-435
  - WP-218
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-23
updated: 2026-10-23
tags:
  - weil-positivity
  - bost-connes
  - positive-heat-mixture
  - closed-quadratic-form
  - vacuum-charge
  - laplace-gram
  - essential-spectrum
---

# WP-439: Infinite thermal channels repair the star only, not the Weil ray

## Exact result and boundary

**EXACT-DERIVED; CLASSICAL LAPLACE-GRAM CONSTRUCTION; NEGATIVE/COMPLETION-CLASS OBSTRUCTION.**
WP-438 excludes a single positive-time thermal channel from simultaneously
aligning with all first-prime Weil couplings. An infinite collection of
channels changes that conclusion: a densely defined closed
positive all-prime **star** completion exists for logarithmic exponent
\(\kappa>1\). For \(0\le\kappa\le1\), no positive heat mixture in the
class below permits any finite vacuum charge, even on the algebraic star.
Nevertheless, **every** admissible positive heat mixture is compact on
each fixed prime-power ray. Thus even mixtures whose full-space energy
is unbounded cannot repair the unchanged Weil ray by addition of that
energy and a finite vacuum charge.

This separates an actual domain/positivity possibility from an invalid
Weil inference. The positive example is a freely specified classical
Laplace Gram, not an independently source-selected sign mechanism.

## Objects and admissible measures

On \(\mathcal H=\ell^2(\mathbb N)\), let
\[
 He_n=(\log n)e_n,\qquad \mu_pe_n=e_{pn},\qquad
 a_p=\frac{(\log p)^\kappa}{\sqrt p},\quad
 b_p=\frac{\log p}{\sqrt p},\quad \kappa\ge0.
\]
For fixed \(\alpha>0\), put \(y_n=(\log n)^\alpha\) and
\[
 B_t=R_\kappa e^{-tH^\alpha},\qquad
 R_\kappa e_n=\sum_{p\mid n}a_p e_{n/p},\qquad t>0.
 \tag{1}
\]
Here \(B_t\) denotes its bounded compact extension from WP-435,
not an assumed closed extension of the unsmoothed \(R_\kappa\).
In particular \(B_te_1=0\) and \(B_te_p=a_pe^{-ty_p}e_1\).

Let \(\nu\) be a nonzero positive Borel measure on **\((0,\infty)\)**
satisfying
\[
 L_\nu(2y_2):=\int_0^\infty e^{-2ty_2}\,d\nu(t)<\infty.
 \tag{2}
\]
This is exactly the condition that the mixed energy of \(e_2\) be
finite. It also makes every other basis energy finite, since
\[
 \int\|B_te_n\|^2d\nu(t)
 =\left(\sum_{p\mid n}a_p^2\right)L_\nu(2y_n),\qquad n\ge2,
 \tag{3}
\]
and \(y_n\ge y_2\). No finite-total-mass or operator-norm integrability
assumption is imposed on \(\nu\).

Define the analysis operator by its maximal integral domain:
\[
 \mathcal A_\nu f=(t\mapsto B_tf),\qquad
 D(\mathcal A_\nu)=
 \left\{f\in\mathcal H:\int\|B_tf\|^2d\nu(t)<\infty\right\},
 \quad
 \mathcal A_\nu:\mathcal H\supset D(\mathcal A_\nu)
       \longrightarrow L^2(\nu;\mathcal H).
 \tag{4}
\]
This operator is densely defined and closed. Density follows from (3).
For closedness, if \(f_j\to f\) in \(\mathcal H\) and
\(\mathcal A_\nu f_j\to F\) in \(L^2(\nu;\mathcal H)\), take a
subsequence converging pointwise \(\nu\)-almost everywhere. Boundedness
of each \(B_t\) gives \(B_tf_j\to B_tf\) for every \(t>0\), hence
\(F(t)=B_tf\) almost everywhere. Thus \(f\in D(\mathcal A_\nu)\)
and \(\mathcal A_\nu f=F\). Measurability follows from strong
continuity of \(B_t\) on positive-time intervals: the factorization
in WP-435, equation (3), gives local uniform bounds, and finite-support
vectors give the initial continuity. Condition (2) also makes \(\nu\)
sigma-finite.

Consequently
\(q_\nu(f)=\|\mathcal A_\nu f\|^2\) is a closed nonnegative form.
It need not be bounded on \(\mathcal H\).

## Every admissible mixture stays compact on a prime ray

Fix a prime \(p\), and identify
\(\mathcal H_p=\overline{\operatorname{span}}\{e_{p^j}:j\ge0\}\).
Different ray basis vectors have orthogonal \(B_t\) outputs. Hence
the restricted form is represented by the diagonal operator
\[
 K_{\nu,p}e_1=0,\qquad
 K_{\nu,p}e_{p^j}
 =a_p^2L_\nu\!\left(2(j\log p)^\alpha\right)e_{p^j},
 \quad j\ge1.
 \tag{5}
\]
For \(u\ge2y_2\), dominated convergence using (2) gives
\[
 L_\nu(u)\longrightarrow0\qquad(u\to\infty),
 \tag{6}
\]
because every heat time is strictly positive. The diagonal in (5)
is bounded and tends to zero. In particular the **whole ray** lies
in \(D(\mathcal A_\nu)\), and \(K_{\nu,p}\) is compact.
This statement is a restriction of a closed form; it does not assume
that an unbounded full-space operator \(\mathcal A_\nu^*\mathcal A_\nu\)
can be compressed on arbitrary vectors in its operator domain.

The unchanged Weil ray is
\[
 W_p=(\log p)(I-G_{1,p}),\qquad
 G_{1,p}(j,k)=p^{-|j-k|/2}.
\]
WP-218 proves, with \(r=p^{-1/2}\),
\[
 \inf\sigma_{\rm ess}(W_p)
 =-\frac{2(\log p)r}{1-r}<0.
\]
Therefore for every admissible \(\nu\) and every finite \(\gamma\ge0\),
\[
 \boxed{W_p+K_{\nu,p}+\gamma|e_1\rangle\langle e_1|
          \not\succeq0.}
 \tag{7}
\]
The correction is compact even when the ambient mixed energy is
unbounded. An infinite bath of positive heat times therefore does
not evade the essential-sign obstruction merely by losing global
boundedness or compactness.

## The sharp star-existence threshold

For finite prime support \(x=\sum_p x_pe_p\), write
\(S(x)=\sum_pb_px_p\). The vacuum-plus-first-prime star form is
\[
 Q_{\nu,\gamma}(z,x)
 =\gamma|z|^2-2\operatorname{Re}(\overline z S(x))
        +\|\mathcal A_\nu x\|^2.
 \tag{8}
\]
There are no additional Weil prime-prime entries in this specified
star model; all prime-prime entries come from the mixed heat Gram.

If (8) is nonnegative, its \(\{e_1,e_p\}\) determinant implies
\[
 b_p^2\le\gamma a_p^2L_\nu(2y_p),\quad\text{or}\quad
 (\log p)^{2-2\kappa}\le\gamma L_\nu(2y_p).
 \tag{9}
\]
The right side tends to zero along the primes by (6). For
\(0\le\kappa\le1\), the left side does not. Thus **no** measure
satisfying (2) and **no** finite charge works in that regime.
This uses neither a rank bound nor a finite number of thermal channels.

For every \(\kappa>1\), a concrete admissible measure gives the
opposite result. Set
\[
 s=\frac{\kappa-1}{\alpha}>0,\qquad c=y_2>0,\qquad
 d\nu_s(t)=t^{s-1}e^{ct}\,dt,
 \quad h(t)=\frac{e^{-ct}}{\Gamma(s)}.
 \tag{10}
\]
The measure has infinite total mass but satisfies (2), with
\(L_{\nu_s}(2c)=\Gamma(s)c^{-s}\). Euler's Gamma integral gives
\[
 L_{\nu_s}(u)=\frac{\Gamma(s)}{(u-c)^s}\quad(u>c),\qquad
 \gamma_*:=\|h\|_{L^2(\nu_s)}^2
 =\frac1{\Gamma(s)c^s}.
 \tag{11}
\]
The exact cross-channel identity is
\[
 \int h(t)a_pe^{-ty_p}\,d\nu_s(t)
 =\frac{a_p}{\Gamma(s)}\int_0^\infty t^{s-1}e^{-ty_p}dt
 =a_py_p^{-s}=b_p.
 \tag{12}
\]
The resulting prime-prime Gram is the classical shifted
Laplace/Cauchy-power kernel
\[
 K_{\nu_s}(p,q)
 =\frac{\Gamma(s)a_pa_q}{(y_p+y_q-c)^s}.
 \tag{13}
\]
It has no rank-one constraint on a multi-prime panel.

Put \(g(t)=h(t)e_1\), and for \(f\in D(\mathcal A_{\nu_s})\)
let \(z=f_1\). The explicit full-space realization
\[
 \mathcal Q_\gamma(f)
 =\|\mathcal A_{\nu_s}f-zg\|^2
       +(\gamma-\gamma_*)|z|^2,
 \qquad \gamma\ge\gamma_*,
 \tag{14}
\]
is closed and nonnegative. Indeed \(f\mapsto f_1g\) is bounded,
so subtracting it from the closed analysis operator preserves
closedness; the last term is bounded and nonnegative. On finite
support, only prime inputs to \(B_t\) can land in \(e_1\).
Thus (12) shows that (14) equals the mixed heat energy plus the
vacuum charge and **exactly** the first-prime cross terms in (8).
For general domain vectors the cross functional is the convergent
Hilbert-space pairing with \(g\); no convergence of a bare
\(\sum_pb_pf_p\) is being assumed.

The charge is sharp for this chosen measure. Since \(y_2=c\),
\[
 K_{\nu_s}(2,2)=\Gamma(s)a_2^2c^{-s},\qquad
 \frac{b_2^2}{K_{\nu_s}(2,2)}=\gamma_*.
 \tag{15}
\]
The two-state determinant is negative for \(\gamma<\gamma_*\).
At equality the explicit finite-support vector
\[
 e_1+\frac1{\Gamma(s)a_2}e_2
 \tag{16}
\]
is null for (14). This also audits the sign and normalization.

The construction is necessarily unbounded in the ambient Hilbert
norm: if \(\mathcal A_{\nu_s}\) were bounded, (12) and
Cauchy--Schwarz would make \(x\mapsto\sum_pb_px_p\) bounded on
\(\ell^2(\mathbb P)\), contradicting
\(\sum_p b_p^2=\sum_p(\log p)^2/p=\infty\).
Nevertheless (14) is a valid densely defined closed extension of
its finite-support form. No claim that finite-support vectors are
a core for its maximal integral domain is needed or made. Restricting
(14) to the closed star subspace
\(\mathbb C e_1\oplus\ell^2(\mathbb P)\) gives a densely defined
closed star form as well.

Combining (9)--(14) yields the exact existence statement:
\[
 \boxed{\begin{gathered}
 \text{Some admissible positive heat mixture and finite vacuum charge}\\
 \text{give a positive algebraic star with a closed realization}
 \end{gathered}
 \quad\Longleftrightarrow\quad\kappa>1.}
 \tag{17}
\]
This quantifies over measures; it does **not** say that every
measure works when \(\kappa>1\).

## Why the positive star is not a positive Weil completion

For the example (10), the ray correction is explicitly
\[
 K_{\nu_s,p}(j,j)
 =\frac{\Gamma(s)a_p^2}{\bigl(2(j\log p)^\alpha-c\bigr)^s},
 \quad j\ge1,
 \tag{18}
\]
and decays like \(j^{-\alpha s}=j^{-(\kappa-1)}\).
Thus (7) applies to the positive star example as well. Formula
(14) matches only the vacuum-to-first-prime coefficients; it
does not insert all the higher prime-power Toeplitz couplings of
\(W_p\). Replacing the star's truncated signed part by that full
unchanged ray destroys positivity.

There are two independent reasons to reject an RH interpretation.
First, the thermal measure and its vacuum feature in (10) were
chosen to realize (12). The source dynamics has not selected them.
The same Laplace identity works for arbitrary unbounded generator lengths
\(\ell_j\ge\ell_0>0\), with one generator attaining \(\ell_0\), amplitudes
\(a_j=\ell_j^\kappa e^{-\ell_j/2}\), and target
\(b_j=\ell_j e^{-\ell_j/2}\); the star construction and charge
threshold require no primality. Second, the full Weil ray still
has negative essential spectrum. There is no archimedean Gamma
term, polar normalization, or equality with the global Weil form
in this construction. The Euler Gamma function in (10)--(13) is
only an integration constant, not an archimedean completion.

The excluded class consists of **positive** mixtures of the fixed
\(B_t^*B_t\), finite on the canonical basis, with strictly positive
heat times, added to the unchanged ray. An atom at zero would
invoke the unsmoothed nonclosable field and lies outside (1)--(4);
signed subtraction before taking a limit, altered ray domains,
or a genuinely different source coupling are also outside this
theorem. Allowing infinite basis energy would change the test
domain rather than evade (2) within the stated class.

## Prior art, audits, and research consequence

The Hilbert-space square completion is classical Gram/Riesz
factorization, as in the range-inclusion framework already cited
for WP-438. The positive kernel (13) is an elementary Laplace
Gram; Euler's integral is NIST DLMF equation 5.2.1. Aronszajn's
1950 theory is the general positive-kernel background. Partington,
Pott and Zawiski (2020), Theorem 4.1 and its proof, explicitly
factor positive-measure Laplace/Hankel kernels through an \(L^2\)
Laplace map. Their bounded truncated Hankel operators differ from
this possibly unbounded prime-shift analysis operator. Closedness
here was proved directly in (4), and essential-sign preservation
uses the already audited WP-218 Toeplitz/Weyl result.

The line-local comparison is with WP-438's single thermal channel,
WP-435's fixed-time compact energies, and WP-437's vacuum-null
corrections. This result permits infinitely many channels, finite
vacuum charge, and unbounded full-space energies.
It supplies an explicit closed positive control, rather than
extrapolating the rank-one or nonclosability obstruction past its
hypotheses. It then closes that larger **positive heat-mixture**
route at the actual prime-ray sign gate. WP-127's positive
subordination result concerns the different archimedean Gamma
Markov multiplier and does not imply this classification.

Direct finite-panel checks with primes \(2,3,5,7,11\) verified the null
vector (16), the determinant threshold (15), and positivity of
900 sampled real quadratic values for
\((\alpha,\kappa)=(1,2),(0.7,2.4),(2,7)\), using 300 vectors per
choice with coordinates uniform in \([-1,1]\) and Python random seed 439.
Explicit constant packets on ray grades 1000--1499 retained
energy below \(-3.32\) for the same choices. These are floating-point
sanity checks only; equations (2)--(18) are the evidence for all
quantified conclusions. No historical novelty is claimed for the
general kernel, Gamma identity, closure argument, or compactness
principle, and no formal proof is claimed.

Continuum thermal mixing is more flexible than a single channel, but all admissible
positive mixtures are still too small on each ray to change the
unchanged Weil sign. A source-forced construction must change
that ray geometry or its admissible domain, not merely introduce
more positive heat scales.

## References

- research/weil_positivity/findings/WP-438-mixed-prime-vacuum-charge-rank-one-thermal-completion-obstruction.md
- research/weil_positivity/findings/WP-437-prime-ray-heat-restriction-mosco-discontinuity-and-vacuum-null-sign-obstruction.md
- research/weil_positivity/findings/WP-435-fractional-heat-prime-field-schatten-phase-transition.md
- research/weil_positivity/findings/WP-218-bost-connes-weil-defect-has-negative-essential-spectrum-stable-under-compact-completion.md
- NIST DLMF, [Euler's Gamma integral, equation 5.2.1](https://dlmf.nist.gov/5.2.E1).
- N. Aronszajn, *Theory of reproducing kernels*, Transactions of the American Mathematical Society **68** (1950), 337--404, [DOI: 10.1090/S0002-9947-1950-0051437-7](https://doi.org/10.1090/S0002-9947-1950-0051437-7).
- J. R. Partington, S. Pott and R. Zawiski, *Laplace--Carleson Embeddings on Model Spaces and Boundedness of Truncated Hankel and Toeplitz Operators*, Integral Equations and Operator Theory **92** (2020), article 37, [DOI: 10.1007/s00020-020-02594-5](https://doi.org/10.1007/s00020-020-02594-5).
