---
title: "WP-448: Periodic Maharam forms have a sharp zeta-smoothing threshold"
type: research-finding
status: verified
research_question: "Can an integrable periodic modulation enlarge the positive dilation-covariant Maharam forms at the critical exponent?"
claim_strength: exact_periodic_profile_classification_with_critical_rigidity_supercritical_positive_cone_and_full_domain_covariance
scope: excitation-diagonal Maharam forms with an exponential times integrable periodic vacuum weight; not arbitrary nonperiodic or off-diagonal forms
finding_id: WP-448
related_findings:
  - WP-444
  - WP-445
  - WP-447
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-24
updated: 2026-10-24
tags:
  - weil-positivity
  - maharam-extension
  - dilation-covariance
  - periodic-profile
  - mobius-inversion
  - zeta-distribution
---

# WP-448: Critical periodic profiles are rigid; above criticality the cone is classical zeta averaging

## Result and evidence boundary

**EXACT-DERIVED; CLASSICAL MOBIUS/ZETA MECHANISM; CATEGORY CLASSIFICATION.**
WP-447 leaves nonhomogeneous excitation-diagonal forms open. Fix
\(\beta>0\), a period \(L>0\), and a real
\(g\in L^1(\mathbb R/L\mathbb Z)\). On the same Maharam Hilbert
space, prescribe the vacuum weight
\[
 q_1(s)=e^{(1-\beta)s}g(s).
 \tag{1}
\]
Seek finite almost-everywhere nonnegative measurable weights \(q_n(s)\)
whose full finite-integral form
\[
 Q[F]=\sum_{n\ge1}\int_{\mathbb R}q_n(s)|h_n(s)|^2e^sds,
 \qquad F=\sum_n\Psi_n\otimes h_n,
 \tag{2}
\]
satisfies \(W_mD(Q)\subset D(Q)\) and
\(Q[W_mF]=Q[F]\) for every positive integer \(m\).
Then the weights are unique, and existence is classified as follows:

- If \(0<\beta\le1\), existence holds exactly when \(g\) is a
  nonnegative constant almost everywhere. The form is that constant
  times WP-447's homogeneous form. In particular, at \(\beta=1\)
  it is a scalar Hilbert norm squared.
- If \(\beta>1\), existence holds exactly when
  \[
   \boxed{g=\mathcal P_\beta h,\qquad
   (\mathcal P_\beta h)(s)=\frac1{\zeta(\beta)}
          \sum_{k\ge1}k^{-\beta}h(s+\log k),
   \qquad h\in L^1(\mathbb R/L\mathbb Z),\quad h\ge0.}
   \tag{3}
  \]
  The nonnegative profile \(h\) is unique. The series converges in
  \(L^1\); for nonnegative \(h\), it is also finite almost everywhere.

Every form so obtained is densely defined and closed, and covariance
holds on its full domain. The supercritical cone contains nonconstant
smooth profiles; it is not just a positive mixture of the homogeneous
forms. Nevertheless, (3) is averaging by the classical logarithmic
Riemann zeta distribution, with a freely chosen nonnegative input.
It supplies no source-selected Weil orientation, Gamma term or polar
normalization. The exponent \(\beta\) parametrizes the form, not a
change to the underlying critical valuation measure.

This extends the homogeneous classification at the critical exponent
to all integrable periodic profiles and gives an exact contrasting
cone above that exponent. No classification of arbitrary nonperiodic
weights, excitation off-diagonal couplings or proper comparison
subspaces is asserted. There is no RH consequence, claim of historical
novelty, formal verification or independent adversarial approval.

## Source normalization and the unique recurrence

Use
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad\nu_p(j)=(1-p^{-1})p^{-j},\quad
 \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds).
\]
The complete excitation basis and source lifts of WP-443/WP-447 are
\[
 \Psi_n=\prod_{p\mid n}\psi_{p,v_p(n)},\quad\Psi_1=1,\quad\psi_{p,0}=1,
 \qquad
 \psi_{p,a}=
 \frac{1_{J_p\ge a}-p^{-1}1_{J_p\ge a-1}}
      {\sqrt{(1-p^{-1})p^{-a}}},\quad a\ge1,
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\quad
 (U_ch)(s)=e^{-c/2}h(s-c),\quad W_p=V_p\otimes U_{\log p}.
\]
The prime lifts commute; set \(W_m=\prod_pW_p^{v_p(m)}\).
Writing \(r=p^{-1}\), direct substitution gives
\[
 V_p\psi_{p,0}=\sqrt r\,\psi_{p,0}
                +\sqrt{1-r}\,\psi_{p,1},\qquad
 V_p\psi_{p,a}=\psi_{p,a+1}\quad(a\ge1).
 \tag{4}
\]
Distinct input excitations have disjoint output excitation supports.
The real-coordinate change of variables cancels the unitary mass
normalization. Thus covariance is equivalent to
\[
 \begin{cases}
 r q_n(s+\log p)+(1-r)q_{np}(s+\log p)=q_n(s),&p\nmid n,\\
 q_{np}(s+\log p)=q_n(s),&p\mid n.
 \end{cases}
 \tag{5}
\]
Necessity does not presume local boundedness of the unknown weights:
test \(\Psi_n\otimes1_E\) for arbitrary measurable subsets of
\(\{|s|\le R,q_n(s)\le R\}\). These vectors have finite form
value, and domain preservation permits the comparison. Equality of
the nonnegative integrals for every such subset gives (5); the sets
exhaust the real line up to a null set. Countably many translations
can be handled on a common conull set.

Let \(\varphi\) be Euler's totient and \(\mu\) the Mobius function.
Iterating (5) from (1) gives the unique formula
\[
 \boxed{q_n(s)=\frac{e^{(1-\beta)s}}{\varphi(n)}
   \sum_{d\mid n}\mu(d)(n/d)^\beta
                    g(s-\log(n/d)).}
 \tag{6}
\]
Indeed, the first occurrence of a prime applies the difference
\([q(s-\log p)-p^{-1}q(s)]/(1-p^{-1})\); every subsequent
occurrence shifts by \(-\log p\). These commuting differences give
(6), so consistency imposes no additional factorization hypothesis.

Write \(\tau_a g(s)=g(s+a)\), let \(F(n)\) be the set of prime
divisors of \(n\), and define
\[
 d_n(\beta)=\frac{n^\beta}{\varphi(n)}
                \prod_{p\mid n}(1-p^{-\beta})>0,
 \qquad
 \mathcal L_F=\prod_{p\in F}
            \frac{I-p^{-\beta}\tau_{\log p}}{1-p^{-\beta}}.
 \tag{7}
\]
Formula (6) becomes
\[
 q_n(s)=d_n(\beta)e^{(1-\beta)s}
                 (\mathcal L_{F(n)}g)(s-\log n).
 \tag{8}
\]
Consequently positivity for every excitation is exactly
\[
 \mathcal L_Fg\ge0\text{ almost everywhere for every finite prime set }F,
 \tag{9}
\]
including \(F=\varnothing\). Every finite prime set occurs as
\(F(n)\). In particular, prime powers alone do not test the full cone.

## All nonzero periodic frequencies disappear at and below one

Normalize circle integration by \(L^{-1}ds\), and write
\(\widehat g(k)\) for the Fourier coefficient at
\(t_k=2\pi k/L\). Each \(\mathcal L_F\) preserves the mean.
A nonnegative integrable function has every Fourier coefficient
bounded in modulus by its mean. Therefore (9) implies
\[
 |\widehat g(k)| R_F(\beta,t_k)\le\widehat g(0),\qquad
 R_F(\beta,t)=\prod_{p\in F}
       \frac{|1-p^{-\beta+it}|}{1-p^{-\beta}}.
 \tag{10}
\]
Every factor is at least one, and the convergent one-prime logarithm is
\[
 \log R_F(\beta,t)
   =\sum_{p\in F}\sum_{j\ge1}
       \frac{1-\cos(jt\log p)}{j p^{j\beta}}.
 \tag{11}
\]
For \(t\ne0\), the sum at \(\beta=1\) diverges as \(F\)
exhausts the primes. Here is the full analytic input, also used in
WP-444. For \(\sigma>1\), the absolutely convergent Euler product gives
\[
 \sum_p\sum_{j\ge1}\frac{1-\cos(jt\log p)}{j p^{j\sigma}}
       =\log\zeta(\sigma)-\log|\zeta(\sigma-it)|.
 \tag{12}
\]
As \(\sigma\downarrow1\), the pole makes the first term diverge,
whereas holomorphy near \(1-it\ne1\) bounds the zeta modulus above.
Thus (12) diverges. The full nonnegative sum at exponent one dominates
it for every \(\sigma>1\). For \(0<\beta\le1\), (11) in turn
dominates the sum at exponent one. No RH or zero-free-line theorem is
needed; a zero at \(1-it\) would only strengthen the bound.

For every nonzero integer \(k\), (10) now forces
\(\widehat g(k)=0\). Uniqueness of Fourier coefficients for
\(L^1\) periodic functions makes \(g\) constant almost everywhere;
for example, its Fejer means are constant and converge to it in
\(L^1\). Nonnegativity makes the constant nonnegative. Conversely,
constants satisfy (9), recovering exactly WP-447.

## Above one, Mobius inversion classifies the whole periodic cone

Suppose \(\beta>1\). Since \(\sum_p p^{-\beta}<\infty\),
the products in (7) converge in operator norm on the periodic
\(L^1\) space to
\[
 \mathcal L_\infty
       =\zeta(\beta)\sum_{k\ge1}\frac{\mu(k)}{k^\beta}
                          \tau_{\log k}.
 \tag{13}
\]
Indeed, each factor differs from the identity by norm at most
\(2p^{-\beta}/(1-p^{-\beta})\), a summable sequence.
Both (13) and (3) are absolutely convergent operator series.
Dirichlet convolution \(\mu*1=\delta_1\) proves
\[
 \mathcal L_\infty\mathcal P_\beta
    =\mathcal P_\beta\mathcal L_\infty=I.
 \tag{14}
\]
The same statements hold on bounded periodic functions with the
supremum norm, though \(L^1\) suffices for the theorem.

If (9) holds, its \(L^1\) limit
\(h=\mathcal L_\infty g\) is nonnegative because the positive cone
is closed. Equation (14) gives (3) and uniqueness.

Conversely, let \(h\ge0\) and \(g=\mathcal P_\beta h\).
For each finite \(F\), the prime factors cancel to give
\[
 \mathcal L_Fg=\mathcal P_{F^c}h,
 \qquad
 \mathcal P_{F^c}=
 \prod_{p\notin F}(1-p^{-\beta})
                   (I-p^{-\beta}\tau_{\log p})^{-1}.
 \tag{15}
\]
Each factor on the right is the positive probability average
\[
 (1-p^{-\beta})\sum_{a\ge0}p^{-a\beta}\tau_{a\log p}.
\]
The infinite product converges in operator norm, so (15) is positive
and proves (9). This proves both directions of the cone classification.
Equivalently, (3) averages over \(\log N\), where
\(\Pr(N=k)=k^{-\beta}/\zeta(\beta)\). The arithmetic probability
law is classical; no new sign theorem has been inserted by naming it.

## Closed forms, a sharp oscillatory control, and limits of the result

Formula (6) gives locally integrable weights because \(g\) is
integrable and periodic. When (9) holds they are nonnegative and
finite almost everywhere. The direct-sum multiplication operator with
symbol \(q_n(s)\) is nonnegative self-adjoint; (2) is its square-root
form on the full domain. Finite excitation sums of bounded compactly
supported real-coordinate functions are a form core, by truncation
in excitation index, real support and function magnitude. Thus the
form is densely defined and closed, including profiles with zeros.
Using the disjoint supports in (4), Tonelli and (5) proves covariance
for arbitrary vectors, with equality also when the energy is infinite.
This establishes actual domain preservation, not just a core identity.

For a transparent sharp control, set
\(g(s)=1+\varepsilon\cos(ts)\), where \(t\ne0\),
\(\varepsilon\in\mathbb R\), and take period \(2\pi/|t|\).
At \(\beta>1\), (13) gives
\[
 h(s)=1+\varepsilon\operatorname{Re}
       \left(\frac{\zeta(\beta)}{\zeta(\beta-it)}e^{its}\right).
\]
Hence the exact all-prime admissibility threshold is
\[
 \boxed{|\varepsilon|\le
                 \frac{|\zeta(\beta-it)|}{\zeta(\beta)}}.
 \tag{16}
\]
At \(0<\beta\le1\), only \(\varepsilon=0\) works. For a
finite prime set \(F\), the threshold is instead
\(R_F(\beta,t)^{-1}>0\). Finite-cutoff tests can therefore miss
the critical collapse. These thresholds also follow directly by
minimizing each sinusoidal weight in (8), rather than estimating
its mean alone.

Choose a strictly positive admissible \(\varepsilon\) in (16).
The vacuum weight is not a positive mixture of real exponentials:
its logarithm has second derivative
\(-\varepsilon t^2/(1+\varepsilon)<0\) at a cosine maximum,
whereas every finite-valued positive exponential mixture is log-convex
by Holder's inequality. Thus the supercritical cone genuinely exceeds
positive homogeneous mixtures. It still has the unconstrained input
\(h\); positivity does not select that input from the Weil source.

The finite-prime translation calculation survives geometric-coordinate
controls with arbitrary scales \(a_j>1\) in place of primes. The
rigidity step requires divergence of the phase-sensitive sum (11),
not merely divergence of \(\sum_j a_j^{-\beta}\). For example,
if every \(\log a_j\) is an integer multiple of a common period,
all normalized difference factors fix every function of that period.
Nonconstant nonnegative profiles then survive. Conversely, a summable
scale family has the same positive-convolution construction as (15).
The arithmetic Euler product settles the phase-divergence condition
for the actual prime scales; the supercritical positivity mechanism
itself is generic probability averaging.

The line consequence is a closed periodic escape at the critical
exponent, with a precisely classical and freely parametrized escape
above it. Neither side produces the signed finite-Weil complement of
the GCD Gram or its archimedean/polar completion. A nonperiodic
profile, off-diagonal coupling or independently selected comparison
space needs its own theorem and remains outside this classification.

## Prior art and validation

The finite difference (6) is Mobius inversion. Mattila--Haukkanen,
Theorem 4.3, give the classical criterion that an arithmetic function
has positive semidefinite GCD matrices exactly when its Mobius
convolution is nonnegative. Hong--Loewy's generalized-Jordan
factorization is the homogeneous specialization used in WP-447.
Nakamura, Section 1.1 and equation (1.4), recalls the classical zeta
distribution and its prime-power Levy measure. The Euler-product and
pole facts are recorded by DLMF. These ingredients and the zeta
probability law are prior art, not new Mathia mechanisms.

The local delta is the exact identification of the **whole integrable
periodic-profile cone** for the prescribed Maharam compression law,
including its collapse for \(0<\beta\le1\), its invertible
positive-convolution parametrization for \(\beta>1\), and full
closed-domain realization. The proof is given above without relying
on a novelty claim for any general harmonic-analysis theorem.

A coefficient-level audit compared (6) with both
compression recurrences (5) as exact rational combinations of formal
translations: 3,000 checks used \(1\le n\le120\), primes
\(2,3,5,7,11\), and integer exponents \(-1,0,1,2,3\).
The nonpositive exponents were algebraic controls, not positivity
claims. Another 1,200 numerical checks compared complex-exponent
divisor sums with their factored Jordan products and Fourier gains
for \(\beta=0.5,1,1.5,2\), \(t=0.3,1,2.7\), and
\(1\le n\le100\); the largest relative product error was below
\(1.18\cdot10^{-15}\). Twelve finite-prime threshold controls
checked the exact sinusoidal minima at amplitudes 0.99 and 1.01
times their predicted threshold. All checks passed. They diagnose
translation signs and normalization; the infinite-prime threshold,
Fourier uniqueness and domain assertions are established by the
analytic proofs, not these finite checks.

## References

- [WP-444](WP-444-critical-valuation-energy-drift-has-no-measurable-diagonal-counterterm.md), the phase-sensitive critical Euler-product divergence.
- [WP-445](WP-445-maharam-drift-cancellation-forces-an-indefinite-energy.md), the fixed Maharam source action.
- [WP-447](WP-447-homogeneous-maharam-forms-recover-classical-gcd-grams.md), the excitation basis, homogeneous weights and classical orbit Grams.
- M. Mattila and P. Haukkanen, *A notion of positive definiteness for arithmetical functions*, in **Matrices, Statistics and Big Data**, Contributions to Statistics (2019), 61--74, Theorem 4.3, [author manuscript](https://trepo.tuni.fi/bitstream/handle/10024/117105/a_notion_of_positive_definiteness_2019.pdf?sequence=2), [DOI: 10.1007/978-3-030-17519-1_5](https://doi.org/10.1007/978-3-030-17519-1_5).
- T. Nakamura, *A complete Riemann zeta distribution and the Riemann hypothesis*, **Bernoulli 21** (2015), 604--617, Section 1.1 and equation (1.4), [author reprint](https://arxiv.org/pdf/1504.03438), [DOI: 10.3150/13-BEJ581](https://doi.org/10.3150/13-BEJ581). Only its classical uncompleted zeta distribution is used here.
- NIST DLMF, [Euler product, §27.4](https://dlmf.nist.gov/27.4.E3) and [analytic continuation and the pole at one, §25.2(i)](https://dlmf.nist.gov/25.2).
