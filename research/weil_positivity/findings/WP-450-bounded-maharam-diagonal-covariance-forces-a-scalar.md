---
title: "WP-450: Bounded Maharam diagonal covariance forces a scalar"
type: research-finding
status: verified
research_question: "Can an arbitrary nonperiodic vacuum profile produce a bounded excitation-diagonal covariant Maharam form?"
claim_strength: exact_bounded_diagonal_classification_via_uniform_inverse_sieve_bounds
scope: all bounded real excitation-diagonal multiplication operators on the fixed critical Maharam space; not off-diagonal operators or unbounded forms
finding_id: WP-450
related_findings:
  - WP-447
  - WP-448
  - WP-449
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-24
updated: 2026-10-24
tags:
  - weil-positivity
  - maharam-extension
  - dilation-covariance
  - bounded-operator
  - mobius-inversion
  - zeta-distribution
---

# WP-450: Every bounded diagonal covariant form is a scalar norm

## Result and evidence boundary

**EXACT-DERIVED; CLASSICAL CONVOLUTION INGREDIENTS; CATEGORY OBSTRUCTION.**
On the fixed critical Maharam space of WP-447--WP-449, suppose
\(A\) is a bounded self-adjoint operator which, in excitation
coordinates, acts by
\[
 (AF)_n(s)=q_n(s)h_n(s),\qquad
 q_n:\mathbb R\longrightarrow\mathbb R\text{ measurable},\qquad
 \sup_n\|q_n\|_\infty\le M<\infty.
 \tag{1}
\]
If
\[
 W_m^*AW_m=A\quad\text{for every positive integer }m,
 \tag{2}
\]
then
\[
 \boxed{A=cI,\qquad q_n(s)=c\text{ almost everywhere for every }n.}
 \tag{3}
\]
Conversely every real scalar satisfies (2). In particular, bounded
nonnegative forms in this diagonal category are precisely
\(c\|F\|^2\), \(c\ge0\).

There is no periodicity, continuity, integrability over the real
line, prescribed asymptotic profile, or sign assumption in the
rigidity proof. The essential hypothesis is the **single uniform
bound over all excitations and all real positions**. Boundedness of
the vacuum alone does not suffice: WP-449 supplies nonconstant
bounded smooth vacuum profiles whose full positive forms are
unbounded. Here unboundedness is forced for every nonscalar positive
form in the diagonal covariant category, rather than just proved for
that example.

The proof below is an elementary inverse-sieve Liouville argument.
It uses the ordinary uncompleted zeta probability law only above
one, and the divergence of the harmonic series. It uses no RH,
zero-free line, prime number theorem, modular ergodicity theorem,
Gamma term or zero data. No historical novelty, formal verification,
independent adversarial approval, global Weil positivity or RH
consequence is claimed.

## Exact source and reduction to uniformly bounded sieve transforms

Use
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad\nu_p(j)=(1-p^{-1})p^{-j},\quad
 \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds).
\]
The complete orthonormal excitation basis and source lifts are
\[
 \Psi_n=\prod_{p\mid n}\psi_{p,v_p(n)},\quad \Psi_1=1,\quad
 \psi_{p,a}=
 \frac{1_{J_p\ge a}-p^{-1}1_{J_p\ge a-1}}
      {\sqrt{(1-p^{-1})p^{-a}}},\quad a\ge1,
\]
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\qquad
 (U_ch)(s)=e^{-c/2}h(s-c),\qquad W_p=V_p\otimes U_{\log p}.
\]
Set \(W_m=\prod_pW_p^{v_p(m)}\). These are commuting isometries.
Writing \(\psi_{p,0}=1\), direct substitution gives
\[
 V_p\psi_{p,0}=p^{-1/2}\psi_{p,0}
                 +\sqrt{1-p^{-1}}\psi_{p,1},\qquad
 V_p\psi_{p,a}=\psi_{p,a+1}\quad(a\ge1).
 \tag{4}
\]
Distinct input excitations have disjoint output excitation supports.
Testing (2) on single excitation packets, and changing the real
integration variable, gives
\[
 \begin{cases}
 p^{-1}q_n(s+\log p)+(1-p^{-1})q_{np}(s+\log p)=q_n(s),&p\nmid n,\\
 q_{np}(s+\log p)=q_n(s),&p\mid n.
 \end{cases}
 \tag{5}
\]
All operators are bounded, so there is no core-to-domain extension
problem here. The measures \(ds\) and \(e^sds\) have identical
null sets; the essential bounds may be used in either measure.

Put \(g=q_1\), \(\tau_a f(s)=f(s+a)\), and, for a finite prime
set \(E\), define
\[
 L_{E,\beta}=\prod_{p\in E}
       \frac{I-p^{-\beta}\tau_{\log p}}{1-p^{-\beta}}
       \quad(\beta>0),\qquad L_{\varnothing,\beta}=I.
 \tag{6}
\]
Solving (5) by successive prime factors gives the same finite
recurrence as WP-448 at exponent one:
\[
 q_n(s)=(L_{E(n),1}g)(s-\log n),\qquad E(n)=\{p:p\mid n\}.
 \tag{7}
\]
For example, a first occurrence of \(p\) applies
\([q(s-\log p)-p^{-1}q(s)]/(1-p^{-1})\); every repeat just
shifts by \(-\log p\). The factors commute. Every finite prime
set occurs as \(E(n)\), so (1) implies
\[
 \boxed{\sup_{E\text{ finite}}\|L_{E,1}g\|_\infty\le M.}
 \tag{8}
\]
This uniform estimate, not positivity of individual finite
differences, is the extra information used below.

## Convex interpolation to the absolutely convergent side

Fix \(\sigma>1\). For every prime,
\[
 \frac{I-p^{-\sigma}\tau_{\log p}}{1-p^{-\sigma}}
  =(1-a_{p,\sigma})I
     +a_{p,\sigma}\frac{I-p^{-1}\tau_{\log p}}{1-p^{-1}},
 \qquad a_{p,\sigma}=\frac{p-1}{p^\sigma-1}\in(0,1).
 \tag{9}
\]
Expanding a finite product expresses \(L_{F,\sigma}g\) as a
convex combination of \(L_{E,1}g\), \(E\subset F\):
\[
 L_{F,\sigma}g=
 \sum_{E\subset F}
   \left(\prod_{p\in E}a_{p,\sigma}
         \prod_{p\in F\setminus E}(1-a_{p,\sigma})\right)L_{E,1}g.
 \tag{10}
\]
Consequently \(\|L_{F,\sigma}g\|_\infty\le M\), independently
of \(F\) and \(\sigma>1\). This remains true for signed \(g\).

For fixed \(\sigma>1\), the products converge in operator norm on
\(L^\infty(\mathbb R)\), since the norm distance of each factor
from the identity is at most \(2p^{-\sigma}/(1-p^{-\sigma})\),
whose sum is finite. The limit and its inverse are
\[
 L_{\infty,\sigma}
   =\zeta(\sigma)\sum_{k\ge1}\frac{\mu(k)}{k^\sigma}\tau_{\log k},
 \qquad
 P_\sigma=\frac1{\zeta(\sigma)}
             \sum_{k\ge1}k^{-\sigma}\tau_{\log k}.
 \tag{11}
\]
Both series converge absolutely in operator norm. Multiplying them
and using \(\sum_{d\mid k}\mu(d)=1_{k=1}\) proves
\(P_\sigma L_{\infty,\sigma}=I\), without any critical-line
continuation. Thus
\[
 h_\sigma=L_{\infty,\sigma}g,\qquad
 \|h_\sigma\|_\infty\le M,\qquad g=P_\sigma h_\sigma.
 \tag{12}
\]
The inputs \(h_\sigma\) can vary with \(\sigma\); a weak limit
of the zeta laws alone would not justify the next step.

## A uniform derivative estimate makes the vacuum constant

Use the ordinary Lebesgue duality between \(L^\infty\) and
\(L^1\). For \(\phi\in C_c^\infty(\mathbb R)\), the adjoint
of \(P_\sigma\) is
\[
 P_\sigma^*\phi(s)=\frac1{\zeta(\sigma)}
             \sum_{k\ge1}k^{-\sigma}\phi(s-\log k).
\]
We prove the quantitative estimate
\[
 \boxed{\|P_\sigma^*\phi'\|_1
  \le\frac{2\|\phi\|_1+\|\phi'\|_1+
                          \sigma^{-1}\|\phi''\|_1}{\zeta(\sigma)}.}
 \tag{13}
\]
Let \(f_x(s)=x^{-\sigma}\phi'(s-\log x)\), \(x\ge1\).
This is differentiable as an \(L^1\)-valued function, with
\[
 \|\partial_x f_x\|_1
  \le x^{-\sigma-1}
             (\sigma\|\phi'\|_1+\|\phi''\|_1).
\]
On each unit interval compare its left endpoint with its integral.
The fundamental theorem of calculus and Minkowski's inequality give
\[
 \left\|\sum_{k\ge1}f_k-\int_1^\infty f_x\,dx\right\|_1
 \le\sum_{k\ge1}\int_k^{k+1}\int_k^x
                         \|\partial_u f_u\|_1\,du\,dx
 \le\|\phi'\|_1+\sigma^{-1}\|\phi''\|_1.
 \tag{14}
\]
The series and integrals converge in \(L^1\) for every
\(\sigma>1\). With \(\epsilon=\sigma-1\), integration by
parts yields
\[
 \int_1^\infty x^{-\sigma}\phi'(s-\log x)\,dx
 =\int_0^\infty e^{-\epsilon t}\phi'(s-t)\,dt
 =\phi(s)-\epsilon\int_0^\infty e^{-\epsilon t}\phi(s-t)\,dt.
 \tag{15}
\]
Its \(L^1\) norm is at most \(2\|\phi\|_1\), since the
last convolution has probability mass one after multiplication by
\(\epsilon\). Equations (14)--(15) prove (13).

Now (12), duality and (13) imply
\[
 \left|\int g(s)\phi'(s)\,ds\right|
 =\left|\int h_\sigma(s)(P_\sigma^*\phi')(s)\,ds\right|
 \le\frac{M(2\|\phi\|_1+\|\phi'\|_1+
                         \sigma^{-1}\|\phi''\|_1)}{\zeta(\sigma)}.
 \tag{16}
\]
As \(\sigma\downarrow1\), \(\zeta(\sigma)\to\infty\)
by monotone convergence to the harmonic series. Hence the
distributional derivative of \(g\) is zero. A locally integrable
function on the connected real line with zero distributional
derivative is constant almost everywhere (equivalently, mollify on
compact intervals and then remove the mollifier). Finally
\(L_{E,1}1=1\), so (7) proves (3).

## Sharp boundaries and consequence for positive completion

The nonconstant WP-449 counting weights satisfy covariance and are
bounded for each fixed \(n\), but their supremum over \(n\) is
infinite. Its smooth coercive variants have the same defect. They
therefore test exactly the hypothesis (8), rather than contradicting
this theorem. No periodic Fourier expansion has been used.

Nor may all-prime covariance be replaced by a finite collection of
source dilations. For one prime \(p\), take any bounded
nonnegative nonconstant \(\log p\)-periodic function \(g\) and
put \(q_n(s)=g(s)\) for every \(n\). This gives a bounded
positive nonscalar operator satisfying (5) for that prime and all
its powers. The hypothesis controlling every finite prime set is
material.

For an unbounded positive diagonal covariant operator \(A\), a
bounded positive spectral cap \(f(A)\), such as
\(\min(A,R)\) or \(A(I+A)^{-1}\), stays in the diagonal
category. If it is nonscalar, it cannot retain all of (2).
Compression covariance by isometries does not commute with arbitrary
spectral calculus. This closes the proposed repair of retaining a
nonperiodic positive Maharam form while making it bounded by a
nonlinear spectral cap. It also makes the Hilbert norm ray extreme
within this diagonal covariant positive-form cone: if two such
nonnegative forms sum to \(c\|F\|^2\) on the whole Hilbert
space, each is bounded and hence scalar.

The theorem concerns multiplication in the **excitation coordinates**
and the real variable. It neither follows by treating these weights
as invariant multiplication functions of the valuation configuration
nor classifies off-diagonal couplings, nonlocal real-coordinate
operators, unbounded forms or restrictions to a different test
space. These are genuine exclusions from its hypotheses.

Bounded diagonal covariance therefore contributes only the original
Hilbert sign, with no new orientation of the signed finite-Weil
defect. A nonconstant positive completion in this category must
accept an unbounded form and supply its domain theorem. The
source-selection, finite-Weil comparison, Gamma and polar gates
remain separate and unresolved.

## Prior art and validation

The logarithmic zeta probability law in (11) is classical; Nakamura,
Section 1.1 and equation (1.4), records its Euler-product description.
Deny's Theorem 1 is the classical neighboring rigidity result for a
bounded function or measure fixed by one probability convolution.
Here (12) has a varying input \(h_\sigma\), not a fixed-point
identity \(g=P_\sigma g\), so that theorem is not being applied
without its hypothesis. Takanobu, Section 1.1, Claim 1, records the
classical exponential scaling limit of logarithmic zeta laws.
That weak convergence likewise does not supply the uniform
\(L^1\) estimate needed for varying bounded inputs; (13)--(16)
give that estimate directly.

The local mathematical delta is the full bounded diagonal
classification without periodicity, and the resulting obstruction
to nonscalar bounded covariant truncations of WP-449. Finite Mobius
inversion, convex interpolation, sum-integral comparison and
distributional differentiation are classical ingredients. Literature
checks by convolution Liouville theory, zeta distributions and
Maharam/Bost--Connes covariance do not establish historical novelty.

An exact rational coefficient audit passed 728 checks. It expanded
(10) for all 32 subsets of \(\{2,3,5,7,11\}\) at
\(\sigma=2,3,4,5\), checking equality of every formal translation
coefficient and nonnegative convex weights summing to one (128
checks). Independently, it checked (5) for the formula (7) with
\(1\le n\le120\) and those five primes (600 checks), including
prime repeats. These finite checks diagnose interpolation constants
and translation directions; the operator-norm limit, derivative
estimate and rigidity are the analytic proofs above. No finite
computation is treated as evidence for an infinite-prime limit.

## References

- [WP-447](WP-447-homogeneous-maharam-forms-recover-classical-gcd-grams.md), fixed source and homogeneous closed forms.
- [WP-448](WP-448-periodic-maharam-forms-have-a-sharp-zeta-smoothing-threshold.md), finite excitation recurrence and periodic classification.
- [WP-449](WP-449-nonperiodic-maharam-positive-forms-from-coprime-counting.md), bounded nonperiodic vacuum profiles with unbounded full forms.
- T. Nakamura, *A complete Riemann zeta distribution and the Riemann hypothesis*, **Bernoulli 21** (2015), 604--617, Section 1.1 and equation (1.4), [author reprint](https://arxiv.org/pdf/1504.03438), [DOI](https://doi.org/10.3150/13-BEJ581). Only the uncompleted law for real parameter above one is used.
- J. Deny, *Sur l'equation de convolution mu = mu star sigma*, **Seminaire Brelot--Choquet--Deny 4** (1959--1960), expose 5, 1--11, Theorem 1, [original text](https://www.numdam.org/article/SBCD_1959-1960__4__A5_0.pdf).
- S. Takanobu, *A generalization of functional limit theorems on the Riemann zeta process*, **Osaka Journal of Mathematics 56** (2019), 843--882, Section 1.1, Claim 1, [institutional text](https://ir.library.osaka-u.ac.jp/repo/ouka/all/73631/ojm56_04_843.pdf), [DOI](https://doi.org/10.18910/73631).
