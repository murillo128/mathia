---
title: "WP-447: Homogeneous Maharam forms recover classical GCD Grams"
type: research-finding
status: verified
research_question: "Can excitation-sensitive positive forms preserve the Maharam dilations, and do their source-orbit kernels escape the classical GCD family?"
claim_strength: exact_classification_of_homogeneous_excitation_diagonal_forms_with_full_domain_covariance_and_orbit_kernel
scope: normalized forms diagonal in the valuation excitation basis with a common exponential real-coordinate weight; not all positive Maharam forms
finding_id: WP-447
related_findings:
  - WP-216
  - WP-443
  - WP-445
  - WP-446
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-24
updated: 2026-10-24
tags:
  - weil-positivity
  - maharam-extension
  - dilation-covariance
  - jordan-totient
  - gcd-kernel
  - positive-form
---

# WP-447: Positive covariant forms survive outside scalar filters, but their orbit kernel is classical

## Result and evidence boundary

**EXACT-DERIVED; CLASSICAL GCD FACTORIZATION; CATEGORY CLASSIFICATION.**
WP-446 excludes every nonconstant nonnegative scalar filter of the corrected
energy that preserves two source dilations. That obstruction does not extend
to forms that distinguish the valuation excitation and real coordinates.

On WP-445's fixed Maharam Hilbert space, consider the normalized class
\[
 Q[F]=\sum_{n\ge1}\int_{\mathbb R}
       d_n e^{(1-\beta)s}|h_n(s)|^2e^sds,
 \quad F=\sum_n\Psi_n\otimes h_n,
 \quad d_1=1,\quad 0\le d_n<\infty,\quad\beta\in\mathbb R.
 \tag{1}
\]
Take the full finite-integral domain. Exact covariance under every lifted
integer dilation forces, and is satisfied by, precisely
\[
 \boxed{\beta\ge0,\qquad
 d_n=d_n(\beta)=\frac{J_\beta(n)}{\varphi(n)}
 =n^{\beta-1}\prod_{p\mid n}
       \frac{1-p^{-\beta}}{1-p^{-1}}.}
 \tag{2}
\]
Here \(J_\beta(n)=n^\beta\prod_{p\mid n}(1-p^{-\beta})\) is the
generalized Jordan totient, \(\varphi=J_1\), and the empty product is one.
At \(\beta=0\), interpret \(J_0(n)=0\) for \(n>1\).
Every form in (2) is nonnegative, densely defined and closed, with
\[
 W_mD(Q_\beta)\subset D(Q_\beta),\qquad
 Q_\beta[W_mF]=Q_\beta[F].
 \tag{3}
\]
For \(\beta>0\) its kernel is zero. At \(\beta=0\) all nonvacuum
valuation excitations lie in its kernel. At \(\beta=1\) it is exactly
the original Hilbert norm squared.

The source-orbit kernel of a compactly supported real-coordinate packet
is exactly the power-GCD Gram of WP-216 multiplied by a translation
correlation, as derived below. Moreover, on a common finite-excitation,
compact-real-support core,
\[
 \left.\frac{d}{d\beta}Q_\beta[F]\right|_{\beta=1}
     =\langle F,(A\otimes I-I\otimes M_s)F\rangle.
 \tag{4}
\]
Thus WP-445's indefinite invariant energy is a tangent to positive
invariant forms. Positivity of the family does not force the sign of
that tangent.

The new local conclusion is an existence-and-classification boundary
beyond WP-446, together with its exact reduction to known positive
kernels. No new GCD positivity theorem, historical novelty, full
Bost--Connes KMS state construction, Gamma/polar term, Weil comparison,
RH consequence, formal verification or independent adversarial approval
is claimed. The common exponential weight and excitation diagonality
in (1) are explicit hypotheses, not consequences of source canonicity.

## Fixed representation and recurrence

Retain the critical valuation product
\[
 \Omega=\prod_p\mathbb N_0,\qquad
 \nu=\bigotimes_p\nu_p,\qquad \nu_p(j)=(1-p^{-1})p^{-j},
 \qquad\mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds).
\]
The complete orthonormal basis of WP-443 is
\[
 \Psi_n=\prod_{p\mid n}\psi_{p,v_p(n)},\quad \Psi_1=1,\qquad
 \psi_{p,a}=\frac{1_{J_p\ge a}-p^{-1}1_{J_p\ge a-1}}
                  {\sqrt{(1-p^{-1})p^{-a}}}\quad(a\ge1).
 \tag{5}
\]
For \(\lambda=\log p\), set
\[
 (V_pg)(J)=\sqrt p\,1_{J_p\ge1}g(J-e_p),\qquad
 (U_ch)(s)=e^{-c/2}h(s-c),\qquad W_p=V_p\otimes U_\lambda.
 \tag{6}
\]
Both the geometric mass and the real-coordinate normalization matter.
The local basis identities are
\[
 V_p\psi_{p,0}=p^{-1/2}\psi_{p,0}
                 +\sqrt{1-p^{-1}}\psi_{p,1},\qquad
 V_p\psi_{p,a}=\psi_{p,a+1}\quad(a\ge1).
 \tag{7}
\]
Images of distinct excitation vectors have disjoint excitation supports.
Changing variables in the real integral yields the multiplier
\(p^{1-\beta}\). Testing (3) on \(\Psi_n\otimes h\), where
\(h\ne0\) has bounded compact support, therefore gives
\[
 \begin{cases}
 p^{-1}d_n+(1-p^{-1})d_{np}=p^{\beta-1}d_n,&p\nmid n,\\
 d_{np}=p^{\beta-1}d_n,&p\mid n.
 \end{cases}
 \tag{8}
\]
In particular
\[
 d_p=\frac{p^\beta-1}{p-1},\qquad
 d_{p^a}=p^{(\beta-1)(a-1)}\frac{p^\beta-1}{p-1}.
 \tag{9}
\]
Nonnegativity of even one \(d_p\) requires \(\beta\ge0\).
Starting from \(d_1=1\), (8) determines every \(d_n\) by prime
factorization. The factors commute, so the recursion is consistent and
gives (2). No multiplicativity assumption was imposed in (1).
Conversely, (2) satisfies both recurrences, including their zero endpoint.

This is a classification only of (1). Allowing arbitrary measurable
weights depending on both \(n\) and \(s\), or off-diagonal excitation
couplings, is a different problem. Removing the normalization allows
nonnegative scalar multiples; if \(d_1=0\), (8) forces all weights zero.

## Closed domains and actual covariance

In excitation coordinates the nonnegative self-adjoint multiplication
operator underlying \(Q_\beta\) has symbol
\[
 q_\beta(n,s)=d_n(\beta)e^{(1-\beta)s}.
 \tag{10}
\]
It is finite everywhere. Its square-root domain is exactly (1), so the
form is closed and densely defined. Finite sums of excitation tensors
with bounded compactly supported real functions form a form core:
truncate the excitation index and the real coordinate, then truncate
the functions, in the squared form norm \(\|F\|^2+Q_\beta[F]\).
This also covers \(\beta=0\), where some weights vanish.

For arbitrary \(F\), disjointness in (7), the nonnegative sum in (1),
and the real change of variables give (8) term by term. Tonelli makes
the equality valid even if either form value is infinite. Therefore
finite energy is preserved, proving (3) on the full domain rather than
only on the algebraic core. The prime lifts commute and multiply to
\(W_m\), so prime covariance gives every integer dilation.

For \(\beta>0\), all \(d_n>0\), hence the kernel is trivial. For
\(\beta\ne1\), translating a unit vacuum packet arbitrarily far in
one real direction makes its form value tend to zero, and translating
in the opposite direction makes it diverge. Thus these forms have no
uniform positive coercivity bound and are unbounded as forms on the
original Hilbert space. At \(\beta=0\), the symbol is
\(1_{n=1}e^s\); at \(\beta=1\), it is one.

These nonconstant forms cannot be scalar functions of
\(B_C=A\otimes I-I\otimes M_s-CI\): if they were, their positivity
and full-domain covariance would invoke WP-446 and force a scalar
norm. They use the joint excitation/real-coordinate calculus, which
has more information than the spectral value \(\eta_n-s-C\) alone.
The weights are diagonal in the excitation basis, not multiplication
by a function of the original valuation configuration \(J\).

## Orbit Gram and the classical temperature parameter

Let \(D_\beta\Psi_n=d_n(\beta)\Psi_n\), and
\(\xi_m=V_m1=\sqrt m\,1_{J\ge v(m)}\).
We first compute its weighted radial pairing. At one prime write
\(r=p^{-1}\) and \(t_k=1_{J_p\ge k}-r1_{J_p\ge k-1}\).
The orthogonal expansion and norms are
\[
 1_{J_p\ge a}=r^a+\sum_{k=1}^a r^{a-k}t_k,
 \qquad \|t_k\|^2=(1-r)r^k.
\]
Using (9), their weighted pairing is
\[
 \begin{aligned}
 \langle1_{J_p\ge a},D_\beta1_{J_p\ge b}\rangle
 &=r^{a+b}\left[1+(1-r^\beta)
                  \sum_{k=1}^{\min(a,b)}r^{-\beta k}\right]\\
 &=r^{a+b-\beta\min(a,b)}.
 \end{aligned}
 \tag{11}
\]
The equality at \(\beta=0\) follows directly without division by
\(1-r^\beta\). Taking finite products yields
\[
 \langle\xi_m,D_\beta\xi_n\rangle
       =\frac{\gcd(m,n)^\beta}{\sqrt{mn}}.
 \tag{12}
\]
All these vectors have finite excitation expansions, so no infinite
product of operators is being assumed.

Take nonzero bounded compactly supported \(h\), put
\(F_h=1\otimes h\), and define
\(k_\beta(s)=e^{(1-\beta)s/2}h(s)\).
Then
\[
 e^{(1-\beta)s/2}U_ch(s)
       =e^{(1-\beta)c/2}U_ck_\beta(s).
\]
Polarization of the form, together with (12), gives the exact identity
\[
 \boxed{Q_\beta(W_mF_h,W_nF_h)
 =\left(\frac{\gcd(m,n)}{\sqrt{mn}}\right)^\beta
   \langle U_{\log m}k_\beta,U_{\log n}k_\beta\rangle_{L^2(e^sds)}.}
 \tag{13}
\]
The first factor is precisely \(G_\beta\) in WP-216. The second is
an ordinary unitary translation Gram. Both have independent elementary
positivity proofs; their entrywise product is positive by tensor-product
Gram construction. At \(\beta=0\) the first factor is identically one.

The parameter \(\beta\) is thus the exponent of the familiar GCD
kernel. Formula (13) alone does not make these forms KMS states at that
temperature: the Hilbert space and its original critical measure have
remained fixed. Nor has the freely selected packet \(h\) been shown to
produce a Gamma factor. Calling its real coordinate archimedean would
not establish the missing Weil identity.

## The corrected energy is the indefinite tangent

For \(\beta>0\), differentiate the finite product in (2):
\[
 \left.\partial_\beta\log d_n(\beta)\right|_{\beta=1}
 =\log n+\sum_{p\mid n}\frac{\log p}{p-1}=\eta_n.
 \tag{14}
\]
Since \(d_n(1)=1\), (10) has derivative \(\eta_n-s\) at one.
Finite excitation sums and bounded real support justify differentiation
under the integral, proving (4) on that common core. We assert no
unqualified differentiability on the whole parameter-dependent domain.
Multiplying the family by \(e^{-C(\beta-1)}\) similarly produces
\(B_C\) as its tangent.

For vacuum packets, (4) is \(-\int s|h(s)|^2e^sds\). Packets
supported strictly on either side of zero exhibit opposite signs.
Consequently the full positive family does not repair the sign of the
invariant tangent. The obstruction is concrete even on the common
core, without a limiting-domain argument.

## Prior art, controls, and consequence

The generalized Jordan identity
\(\sum_{d\mid n}J_\beta(d)=n^\beta\) and the associated power-GCD
factorization are classical; Hong--Loewy, Lemma 4.1, records the
factorization with weights \(J_\beta\). Aistleitner--Berkes--Seip
identify normalized GCD kernels with prime-coordinate Poisson integrals.
WP-216 already derives \(G_\beta\) from KMS-conditioned divisibility
projections. None of these positive kernels is claimed as a new result.

The delta is the exact unique realization (2) in the homogeneous
excitation-diagonal category on this fixed Maharam space, its full
closed-domain covariance, the orbit identity (13), and identification
of the existing indefinite corrected energy as its tangent. It both
prevents extending WP-446 beyond scalar filters and explains why this
particular escape returns to known positive GCD geometry.

The recurrence and positivity survive matched nonarithmetic models.
Replace a prime coordinate by any \(0<r<1\), its scale by
\(\lambda=-\log r\), and use the same geometric law and lift. The
local weights are
\[
 d_0=1,\qquad
 d_a=r^{(1-\beta)a}\frac{1-r^\beta}{1-r}\quad(a\ge1),
\]
with exactly the same positivity threshold and covariance. Thus neither
this sign nor the tangent argument requires primes, zero data, a Gamma
term or type-III ergodicity. The arithmetic labels identify the GCD
specialization, not a new sign-producing principle.

This family leaves the global completion clue unresolved. An additional
source-selected comparison or interaction would have to establish the
finite-Weil orientation and the Gamma/polar normalization. Choosing
\(\beta\), or taking the signed tangent at the critical exponent,
does not establish that implication. The result does not exclude
nonhomogeneous diagonal forms, excitation off-diagonal forms, or a
proper source-selected comparison space.

## Validation

An exact rational audit checked 240 local compression recurrences and
2,880 tail pairings using \(r=1/2,1/3,1/5,2/5,3/4\),
\(\beta=0,1,2,3\), and tail exponents zero through eleven (the
compression outputs retain excitation twelve). It used exact geometric
tail masses, without a truncated top boundary.

It also checked 2,000 mixed-index covariance identities with
\(1\le n\le100\) and primes \(2,3,5,7,11\), and 25,600 independent
divisor-sum Gram identities with \(1\le m,n\le80\). Twelve tests
at \(\beta=-1,-2,-3\) verified the negative first-excitation boundary.
All 30,732 rational checks passed. Twenty-one centered finite-difference
checks of (14) with step \(10^{-5}\), indices
\(1,2,4,6,12,30,210\), and real offsets \(-2,0,3\), had maximum
absolute error below \(1.21\cdot10^{-8}\).

These checks diagnose normalization, endpoint and tangent signs. The
all-real-parameter classification, closed domains and infinite-space
claims follow from the proofs, not the finite audit.

## References

- [WP-216](WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md), the source-conditioned GCD family and its distinction from the finite-Weil defect.
- [WP-443](WP-443-critical-valuation-energy-has-an-explicit-hierarchical-spectrum.md), the complete excitation basis and eigenvalues.
- [WP-445](WP-445-maharam-drift-cancellation-forces-an-indefinite-energy.md), the fixed Maharam representation and indefinite corrected energy.
- [WP-446](WP-446-positive-maharam-spectral-filters-collapse-under-two-dilations.md), the scalar-filter obstruction and exact source-shift formula.
- S. Hong and R. Loewy, *Asymptotic behavior of eigenvalues of greatest common divisor matrices*, Glasgow Mathematical Journal **46** (2004), 551--569, [DOI: 10.1017/S0017089504001995](https://doi.org/10.1017/S0017089504001995), Lemma 4.1. Classical generalized-Jordan factorization of power-GCD matrices.
- C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals and systems of dilated functions*, Journal of the European Mathematical Society **17** (2015), 1517--1546, [author preprint](https://arxiv.org/pdf/1210.0741), [DOI: 10.4171/JEMS/537](https://doi.org/10.4171/JEMS/537). Classical normalized GCD/Poisson kernel framework.
