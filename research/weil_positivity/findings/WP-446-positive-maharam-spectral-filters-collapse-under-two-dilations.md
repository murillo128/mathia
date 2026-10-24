---
title: "WP-446: Positive Maharam spectral filters collapse under two dilations"
type: research-finding
status: verified
research_question: "Can a nonnegative scalar function of the Maharam-corrected energy retain exact source-dilation covariance?"
claim_strength: exact_measurable_positive_spectral_filter_classification_with_nonuniform_approximate_control
scope: scalar Borel functional calculus of WP-445's corrected energy on its full spectral form domain; not arbitrary nonlocal corrections or restricted comparison spaces
finding_id: WP-446
related_findings:
  - WP-443
  - WP-444
  - WP-445
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-24
updated: 2026-10-24
tags:
  - weil-positivity
  - maharam-extension
  - spectral-filter
  - dilation-covariance
  - harmonic-recurrence
  - sign-obstruction
---

# WP-446: Two source dilations erase every nonconstant positive spectral filter

## Result and evidence boundary

**EXACT-DERIVED; CLASSICAL HARMONIC RIGIDITY; NEGATIVE/OBSTRUCTION.**
Fix \(C\in\mathbb R\). Let \(B_C=A\otimes I-I\otimes M_s-CI\) be WP-445's self-adjoint
Maharam-corrected valuation energy, with its lifted source isometries
\(W_n\). Let \(f:\mathbb R\to[0,\infty)\) be Borel and finite
Lebesgue-almost everywhere. Define its densely defined closed form by
\[
 Q_f[F]=\|f(B_C)^{1/2}F\|^2,
 \qquad D(Q_f)=D(f(B_C)^{1/2}).
 \tag{1}
\]
Then
\[
 \left.
 \begin{array}{c}
 W_pD(Q_f)\subset D(Q_f),\\
 Q_f[W_pF]=Q_f[F]\quad(F\in D(Q_f))
 \end{array}
 \right\}\quad p=2,3
 \quad\Longleftrightarrow\quad
 \boxed{f=c\ \text{a.e. for a finite constant }c\ge0.}
 \tag{2}
\]
Consequently the only such form is \(c\|F\|^2\). This rules out
arbitrary nonconstant positive scalar spectral repairs, including
discontinuous and unbounded candidates, not just the positive-part
operation tested in WP-445. The same conclusion holds for any real
spectral function with a uniform lower bound, after subtracting that bound.

The conclusion is exact, not a quantitative stability statement.
Bounded positive nonconstant filters can approach covariance in operator
norm for both generators while staying distance at least one from every scalar
operator. A single generator also admits exact nonconstant positive
filters. Both controls are proved below.

This is a classification in one prescribed functional calculus. It
does not classify all positive forms on the Maharam space, all operators
commuting with \(B_C\), or identities restricted to a proper test
subspace. A scalar Hilbert norm might acquire arithmetic information
through a separately proved comparison map; this result supplies no
such map or Weil identity. No RH implication, historical novelty,
formal verification, or independent adversarial approval is claimed.

## Source normalization and the spectral domain

Use the exact objects of WP-443--WP-445:
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(j)=(1-p^{-1})p^{-j},\quad
 \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds),
\]
\[
 A\Psi_n=\eta_n\Psi_n,\qquad
 \eta_n=\log n+\sum_{p\mid n}\frac{\log p}{p-1},\qquad
 \Psi_1=1.
 \tag{3}
\]
The \(\Psi_n\) form a complete orthonormal basis. In this basis
\(B_C\) acts on the \(n\)-th real-coordinate fibre by multiplication
by \(\eta_n-s-C\). Thus, for \(F=\sum_n\Psi_n\otimes h_n\),
\[
 Q_f[F]=\sum_n\int_{\mathbb R}
 f(\eta_n-s-C)|h_n(s)|^2e^sds.
 \tag{4}
\]
Its domain consists exactly of the vectors for which this is finite.
Each fibre's spectral measure is equivalent to Lebesgue measure.
In particular, finiteness of \(f\) almost everywhere makes (1)
densely defined; no local integrability or growth bound on \(f\)
is assumed.

At prime \(p\), set \(r=p^{-1}\), \(\lambda=\log p\), and
\[
 (V_pg)(J)=\sqrt p\,1_{J_p\ge1}g(J-e_p),\qquad
 (U_\lambda h)(s)=e^{-\lambda/2}h(s-\lambda),\qquad
 W_p=V_p\otimes U_\lambda.
 \tag{5}
\]
Here \(V_p\) is an isometry, and \(U_\lambda\) is unitary for
the measure \(e^sds\). The local normalized excitation basis is
\[
 \psi_{p,0}=1,\qquad
 \psi_{p,a}=\frac{1_{J_p\ge a}-r1_{J_p\ge a-1}}
                   {\sqrt{(1-r)r^a}}\quad(a\ge1).
\]
Direct substitution, with no operator commutator assumption, gives
\[
 V_p\psi_{p,0}=\sqrt r\,\psi_{p,0}
                   +\sqrt{1-r}\,\psi_{p,1},\qquad
 V_p\psi_{p,a}=\psi_{p,a+1}\quad(a\ge1).
 \tag{6}
\]
The local eigenvalues are zero at \(a=0\) and
\(\lambda(a+r/(1-r))\) at \(a\ge1\). Positive excitations
therefore acquire exactly \(\lambda\) under (6), cancelling the
real-coordinate shift. Only the local vacuum splits into two energies.

## Covariance becomes a centered harmonic equation

Apply (4)--(6) to \(F=1\otimes h\), and change variables
\(s=t+\lambda\). The real normalization cancels exactly, giving
\[
 Q_f[W_p(1\otimes h)]
 =\int_{\mathbb R}(T_pf)(-t-C)|h(t)|^2e^tdt,
\]
\[
 (T_pf)(x)=\frac1p f(x-\log p)
       +\frac{p-1}{p}f\left(x+\frac{\log p}{p-1}\right).
 \tag{7}
\]
To justify recovering a pointwise equation from an unbounded form,
take \(h=1_E\) for arbitrary measurable subsets of
\(\{|t|\le N,\ f(-t-C)\le N\}\). Every such vector lies in
\(D(Q_f)\). The assumed domain preservation and equality imply that
the two nonnegative integrals agree for every such subset. These sets
exhaust the real line up to a null set. Hence
\[
 f=T_2f=T_3f\quad\text{almost everywhere}.
 \tag{8}
\]
This inference would not be justified for an unspecified proper
comparison subspace, which is why the domain hypothesis in (2) matters.

The increment in (7) has mean zero and variance
\[
 \frac1p(\log p)^2+
 \frac{p-1}{p}\left(\frac{\log p}{p-1}\right)^2
 =\frac{(\log p)^2}{p-1}.
 \tag{9}
\]
Thus (8) is a classical positive-harmonic-function problem for centered
two-point random walks. Its special recurrences admit an elementary
complete proof, without importing a general recurrence theorem.

## Two elementary recurrences force a constant

Put \(a=\log2\), \(b=\tfrac12\log3\). Remove the null sets
in (8), the set where \(f\) is infinite, and all their translates
by the countable group \(a\mathbb Z+b\mathbb Z\). Work on the
resulting invariant conull set.

For a fixed remaining \(x\), the sequence \(u_k=f(x+ka)\),
\(k\in\mathbb Z\), satisfies
\[
 2u_k=u_{k-1}+u_{k+1}.
 \tag{10}
\]
Its first differences are constant, so \(u_k=\alpha+\beta k\).
Nonnegativity for both positive and negative integers forces
\(\beta=0\). Hence \(a\) is an almost-everywhere period of \(f\).

For \(v_k=f(x+kb)\), the second equation is
\[
 3v_k=v_{k-2}+2v_{k+1}.
 \tag{11}
\]
Its characteristic polynomial is
\[
 2z^3-3z^2+1=(z-1)^2(2z+1).
\]
The recurrence extends uniquely in both directions from three
consecutive values. Its three independent solutions give
\(v_k=\alpha+\beta k+\gamma(-1/2)^k\).
If \(\gamma\ne0\), the last term alternates sign and dominates
the affine part as \(k\to-\infty\), contradicting nonnegativity.
Then nonnegativity in both directions also forces \(\beta=0\).
Thus \(b\) is a second almost-everywhere period.

The ratio \(a/b=2\log2/\log3\) is irrational: a rational
relation would equate positive integer powers of 2 and 3. The period
group is therefore dense. To avoid assuming \(f\) locally
integrable, use the bounded measurable function \(g=f/(1+f)\).
It inherits both periods. Convolution with any smooth compactly
supported approximate identity is continuous and has a dense set of
periods, hence is constant. Approximate-identity convergence in
\(L^1_{\rm loc}\) makes \(g\), and therefore \(f\), constant
almost everywhere. This proves necessity in (2). Sufficiency follows
because every \(W_n\) is an isometry.

## Exact single-prime control and failure of uniform stability

For bounded Borel \(f\), let \(\Pi_{p,0}\) project onto the
zero local excitation at \(p\), with all other coordinates unchanged.
The images in (6) of distinct local basis vectors have disjoint
excitation supports. Consequently the full compression identity is
\[
 W_p^*f(B_C)W_p-f(B_C)
 =\Pi_{p,0}\big((T_pf)(B_C)-f(B_C)\big).
 \tag{12}
\]
The projection commutes with \(B_C\); this is a bounded-operator
identity, not a claimed commutator identity for the indefinite energy.

For \(p=2\), every nonnegative bounded \(a\)-periodic \(f\)
satisfies \(T_2f=f\). For example
\(f(x)=2+\cos(2\pi x/a)\) gives an exact nonconstant positive
form preserved by \(W_2\), and hence by all its powers. The second
incommensurate dilation is essential.

There is also no operator-norm stability estimate taking small
covariance errors for 2 and 3 to small distance from scalar filters.
For \(\varepsilon>0\), set
\[
 f_\varepsilon(x)=2+\cos(\varepsilon x),\qquad
 m_p(\varepsilon)=\frac1p e^{-i\varepsilon\log p}
 +\frac{p-1}{p}e^{i\varepsilon\log p/(p-1)}.
\]
The vacuum fibre has full real spectral support, so (12) implies
\[
 \|W_p^*f_\varepsilon(B_C)W_p-f_\varepsilon(B_C)\|
 =|m_p(\varepsilon)-1|
 \le\frac{\varepsilon^2(\log p)^2}{2(p-1)}.
 \tag{13}
\]
The bound follows from \(|e^{iu}-1-iu|\le u^2/2\) and the
zero mean in (9). Yet \(\sigma(B_C)=\mathbb R\), and therefore
\[
 \inf_{c\in\mathbb R}\|f_\varepsilon(B_C)-cI\|=1
 \quad\text{for every }\varepsilon>0.
 \tag{14}
\]
These filters tend strongly to \(3I\) as \(\varepsilon\to0\),
but not in operator norm. Finite-window or approximate checks cannot
replace the exact global hypothesis of (2).

## Prior art, mathematical delta, and remaining boundary

Choquet--Deny theory classically classifies convolution-harmonic
functions and measures. Deny's 1959--1960 exposition, Theorem 1,
identifies the support-generated periods in the bounded case. The
nonnegative recurrent-chain Liouville principle is recorded, with
proof, in Tamuz's *Lecture Notes on Probability*, Theorem 15.2.
The recurrence proof above establishes the needed special unbounded
case directly, and then uses only measurable dense-period rigidity.
No new general harmonic-function theorem is claimed.

The line-local delta is the exact spectral-compression dictionary
(6)--(8) for the actual valuation/Maharam source and the resulting
classification of every positive scalar spectral repair. WP-445
classified multiplication compensation and ruled out its immediate positive
spectral truncation; it did not imply that discontinuous or unbounded
positive functions of the corrected energy all collapse to constants.
The earlier WP-272 multiplier obstruction concerns a different signed
prime-power measure and is not a proof of this statement.

Only two prime coordinates and the real coordinate are needed here.
Type-III ergodicity, the tail of the prime distribution, zeta zeros,
and a Gamma factor play no role in this obstruction. The same proof
applies to an abstract pair of these local shift models with
incommensurate lattice spans. This separates the classical mechanism
from any unsupported assertion that primality itself produces a sign.

Nonlocal corrections outside scalar functional calculus, multiplicity-
sensitive operators, and a source-selected proper comparison space
remain outside the theorem. They still require their own domains,
covariance, prime/archimedean normalization and independent sign
argument. The accepted completion clue remains unresolved. Replacing
the indefinite energy by another positive scalar filter, while
retaining the full-domain source covariance, is no longer a surviving
nonconstant mechanism.

## Validation

An exact rational audit checked (6)--(7) in the unnormalized orthogonal
tail-difference basis, retaining its exact geometric masses. Parameters
were \(r\in\{1/2,1/3,1/5,2/5,3/4\}\), local energy scales
\(\lambda\in\{1,2/3,7/5\}\), input excitation indices 0 through 7,
real spectral offsets \(k/3\) for \(-4\le k\le4\), and monomial
filters of degrees 0 through 6. All 7,560 weighted compression
identities passed. Outputs retained excitation index 8, so there was
no artificial top-boundary truncation. All 123 exact checks of the
three recurrence solutions in (11), at indices -20 through 20, passed.

Twelve floating-point checks of (13), using primes 2, 3, 5, 11 and
\(\varepsilon=0.01,0.1,0.5\), also passed. These are normalization
and sign diagnostics only. The infinite-domain classification,
almost-everywhere conclusion and absence of uniform stability follow
from the proofs, not from these finite checks.

## References

- [WP-443](WP-443-critical-valuation-energy-has-an-explicit-hierarchical-spectrum.md), the complete excitation basis and exact spectrum.
- [WP-444](WP-444-critical-valuation-energy-drift-has-no-measurable-diagonal-counterterm.md), the full-domain drift and the necessary Weil translation identity.
- [WP-445](WP-445-maharam-drift-cancellation-forces-an-indefinite-energy.md), the Maharam isometries, corrected operator and positive-part obstruction.
- J. Deny, *Sur l'equation de convolution \(\mu=\mu\star\sigma\)*, Seminaire Brelot--Choquet--Deny, **4** (1959--1960), expose 5, 1--11, [original text](https://www.numdam.org/article/SBCD_1959-1960__4__A5_0.pdf), Theorem 1. Classical convolution/periodicity boundary.
- O. Tamuz, *Lecture Notes on Probability*, Caltech (2018), [author text](https://www.tamuz.caltech.edu/teaching/ma144a/lectures.pdf), Theorem 15.2. Classical nonnegative harmonic rigidity for recurrent chains.
