---
title: "WP-449: Nonperiodic Maharam positive forms from coprime counting"
type: research-finding
status: verified
research_question: "Does critical periodic-profile rigidity extend to bounded smooth nonperiodic vacuum weights?"
claim_strength: exact_counterexample_with_closed_domain_covariance_kernel_and_classical_incidence_gram
scope: an explicit nonperiodic excitation-diagonal family on the fixed critical Maharam space; not a classification of all covariant forms
finding_id: WP-449
related_findings:
  - WP-447
  - WP-448
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-24
updated: 2026-10-24
tags:
  - weil-positivity
  - maharam-extension
  - dilation-covariance
  - coprime-counting
  - gcd-kernel
  - domain-boundary
---

# WP-449: Bounded nonperiodic profiles escape critical rigidity through classical counting

## Result and evidence boundary

**EXACT-DERIVED; CLASSICAL SIEVE/INCIDENCE POSITIVITY; CATEGORY BOUNDARY.**
WP-448 proves that an integrable periodic vacuum profile at exponent one
must be constant. Boundedness, even combined with smoothness and strict
positivity, cannot replace periodicity in that statement.

On the same fixed critical Maharam space, let
\[
 C_n(X)=\#\{k\in\mathbb N: k\le X,\ (k,n)=1\},\qquad X\ge0,
\]
and prescribe excitation weights
\[
 \boxed{q_n(s)=\frac{e^s}{\varphi(n)}C_n(ne^{-s}).}                 \tag{1}
\]
Here \(\varphi(1)=1\), so the vacuum profile is
\[
 q_1(s)=g(s)=e^s\lfloor e^{-s}\rfloor,\qquad 0\le g\le1.          \tag{2}
\]
The full finite-integral form with weights (1) is densely defined,
closed, nonnegative and invariant under every source integer dilation.
It is unbounded on the ambient Hilbert space, despite its bounded
vacuum profile. Its kernel is exactly the vectors whose \(n\)-th
excitation component is supported in \(s>\log n\), up to null sets.

Positive compactly supported smooth averaging of the real translations
of (1) gives bounded smooth nonconstant vacuum profiles with the same
full-domain covariance. Adding any positive multiple of the Hilbert
norm gives strictly positive bounded smooth vacuum profiles and a
coercive, still unbounded, form. Thus the escape is not an artifact of
a discontinuous vacuum profile or a nontrivial kernel.

The positive radial pairing is explicitly a floor-GCD incidence Gram.
Its sign comes from counting coprime integers, a classical sieve
mechanism. Neither the cutoff nor its smoothing is selected uniquely
by source covariance. No finite-Weil sign, Gamma contribution, polar
normalization, RH consequence, historical novelty, formal verification
or independent adversarial approval is asserted.

## Fixed source and the counting recurrence

Retain the normalization of WP-447--WP-448:
\[
 \Omega=\prod_p\mathbb N_0,\quad
 \nu=\bigotimes_p\nu_p,\quad \nu_p(j)=(1-p^{-1})p^{-j},\quad
 \mathcal K=L^2(\Omega\times\mathbb R,d\nu\,e^sds).
\]
The complete orthonormal excitation basis is
\[
 \Psi_n=\prod_{p\mid n}\psi_{p,v_p(n)},\quad \Psi_1=1,\qquad
 \psi_{p,a}=\frac{1_{J_p\ge a}-p^{-1}1_{J_p\ge a-1}}
                  {\sqrt{(1-p^{-1})p^{-a}}}\quad(a\ge1).
\]
Set
\[
 (V_pf)(J)=\sqrt p\,1_{J_p\ge1}f(J-e_p),\qquad
 (U_ch)(s)=e^{-c/2}h(s-c),\qquad W_p=V_p\otimes U_{\log p}.
\]
The \(W_p\) commute and are isometries. For \(r=p^{-1}\),
\[
 V_p\psi_{p,0}=\sqrt r\,\psi_{p,0}+\sqrt{1-r}\,\psi_{p,1},
 \qquad V_p\psi_{p,a}=\psi_{p,a+1}\quad(a\ge1).                 \tag{3}
\]
Distinct input excitation vectors have disjoint output excitation
supports. Consequently the diagonal form
\[
 Q[F]=\sum_{n\ge1}\int q_n(s)|h_n(s)|^2e^sds,
 \qquad F=\sum_n\Psi_n\otimes h_n,\qquad D(Q)=\{F\in\mathcal K:Q[F]<\infty\}
                                                                    \tag{4}
\]
has dilation covariance if its weights obey
\[
 \begin{cases}
 p^{-1}q_n(s+\log p)+(1-p^{-1})q_{np}(s+\log p)=q_n(s),&p\nmid n,\\
 q_{np}(s+\log p)=q_n(s),&p\mid n.
 \end{cases}                                                       \tag{5}
\]
The real-coordinate change of variables cancels the mass factor in
\(U_c\); it contributes exactly the translations displayed in (5).

For \(p\nmid n\), splitting the integers coprime to \(n\) into
those divisible by \(p\) and those not divisible by \(p\) gives
\[
 C_n(X)=C_n(X/p)+C_{np}(X).                                        \tag{6}
\]
For \(p\mid n\), simply \(C_{np}(X)=C_n(X)\). Together with
\(\varphi(np)=(p-1)\varphi(n)\) or \(p\varphi(n)\), respectively,
these identities prove (5) for (1), at every real \(s\). In
particular the argument includes prime powers and every mixed-prime
excitation, not just one-prime tests.

Equivalently, the standard coprimality indicator gives
\[
 C_n(X)=\sum_{d\mid n}\mu(d)\lfloor X/d\rfloor,\qquad
 q_n(s)=\frac1{\varphi(n)}\sum_{d\mid n}\mu(d)\frac nd
                         g\bigl(s-\log(n/d)\bigr).                \tag{7}
\]
This is exactly the exponent-one recurrence of WP-448 with a
nonperiodic input. It also proves uniqueness of these weights for the
specified vacuum profile. The sign in (7) is justified by the count
in (1), not by an assumption that a Mobius difference preserves
arbitrary positive functions.

## Full domain, kernel and unavoidable operator unboundedness

For every fixed excitation,
\[
 0\le q_n(s)\le\frac n{\varphi(n)}<\infty.                         \tag{8}
\]
Thus (4) is the square-root form of a nonnegative self-adjoint
direct-sum multiplication operator. Finite excitation sums with
bounded compactly supported real-coordinate components form a core:
truncate excitation index, real support and component magnitude in
the squared form norm. This proves density and closedness.

Disjointness in (3), nonnegativity and Tonelli extend the calculation
of (5) to every \(F\in\mathcal K\), allowing infinite energy.
Therefore
\[
 W_mD(Q)\subset D(Q),\qquad Q[W_mF]=Q[F] \quad(m\ge1).             \tag{9}
\]
No limiting finite-prime operator or unproved domain passage is used.

Since the integer one is coprime to every \(n\),
\(C_n(ne^{-s})=0\) exactly when \(s>\log n\). This proves the
kernel assertion, with the endpoints immaterial in \(L^2\).
On the interval \(\log n-\log2<s<\log n\), only the integer one
is counted, so
\[
 q_n(s)=\frac{e^s}{\varphi(n)}>\frac n{2\varphi(n)}.               \tag{10}
\]
For primorials \(n_R=\prod_{p\le R}p\),
\[
 \frac{n_R}{\varphi(n_R)}=\prod_{p\le R}(1-p^{-1})^{-1}
       \ge\sum_{k\le R}\frac1k\longrightarrow\infty.             \tag{11}
\]
The inequality follows by expanding the finite Euler product, which
contains all integers up to \(R\). Unit vectors supported on the
intervals in (10) prove unboundedness. A bounded vacuum profile is
therefore not a bounded-operator certificate.

For each fixed \(n\), elementary periodic counting modulo \(n\)
gives \(C_n(X)=X\varphi(n)/n+O_n(1)\), hence
\(q_n(s)\to1\) as \(s\to-\infty\). This convergence is not
uniform in the excitation index, as (10)--(11) demonstrate.

## Smoothness and strict positivity do not restore rigidity

Choose \(\kappa\in C_c^\infty(\mathbb R)\), \(\kappa\ge0\),
\(\int\kappa=1\), and define
\[
 q_n^\kappa(s)=\int\kappa(u)q_n(s-u)\,du.                         \tag{12}
\]
Translation commutes with (5), so (12) satisfies the same recurrence.
Each weight is smooth, nonnegative and bounded by (8). The full
form is closed and covariant by the same multiplication/Tonelli
argument. Its vacuum weight obeys
\[
 0\le g_\kappa\le1,\qquad
 g_\kappa(s)\to1\ (s\to-\infty),\qquad
 g_\kappa(s)=0\ (s>\sup\operatorname{supp}\kappa).                \tag{13}
\]
It is therefore nonconstant and nonperiodic. Its derivatives are
bounded by \(\|\kappa^{(j)}\|_1\).

Unboundedness of the full form also survives smoothing. Choose an
interval \(I\) of length less than \(\log2\) with
\(\int_I\kappa>0\), and \(c\) such that
\(0<u-c<\log2\) throughout \(I\). At \(s=\log n+c\),
the contribution of this interval to (12) is
\[
 q_n^\kappa(\log n+c)\ge
 \frac n{\varphi(n)}\int_I e^{c-u}\kappa(u)\,du.                  \tag{14}
\]
The integral is a fixed positive constant, and continuity gives
positive-measure neighborhoods of these lower bounds. Equation (11)
again proves unboundedness.

For any \(\varepsilon>0\), add \(\varepsilon\|F\|^2\).
The weights become \(\varepsilon+q_n^\kappa\); their form has the
same domain, covariance and unboundedness, and is bounded below by
\(\varepsilon\|F\|^2\). Its vacuum is bounded, smooth and strictly
positive, with different limits \(1+\varepsilon\) and
\(\varepsilon\) at the two ends of the real line.

These profiles are not positive mixtures of WP-447's homogeneous
vacuum weights. A positive mixture of real exponentials that is
bounded on the entire real line can have mass only at exponent zero:
any positive mass on positive or negative exponents forces growth
at one end. Such a mixture is constant. This does not classify the
nonperiodic cone; it proves that the cone is larger than positive
homogeneous mixtures, even at bounded smooth vacuum regularity.

Subtracting the limiting unit weight does not inherit positivity.
The difference \(Q^\kappa[F]-\|F\|^2\) is negative on nonzero
vacuum packets supported above \(\sup\operatorname{supp}\kappa\),
and positive on suitable primorial-excitation packets by (14).
Both packets lie in the common finite-excitation core. This is an
explicit two-sign obstruction to that particular baseline subtraction;
no identification of this difference with the Weil functional is made.

## The pairing is classical floor-GCD incidence positivity

Write \(\xi_m=V_m1\). The tail expansion in the excitation basis is
\[
 \xi_m=\frac1{\sqrt m}\sum_{d\mid m}\sqrt{\varphi(d)}\,\Psi_d.
\]
At fixed \(s\), let \(D_s\Psi_d=q_d(s)\Psi_d\). If
\(a=\gcd(m,n)\), then
\[
 \langle\xi_m,D_s\xi_n\rangle
 =\frac{e^s}{\sqrt{mn}}\sum_{d\mid a}C_d(de^{-s})
 =\boxed{\frac{e^s}{\sqrt{mn}}\lfloor ae^{-s}\rfloor}.            \tag{15}
\]
Indeed, partition the positive integers \(k\le ax\) by
\(b=\gcd(k,a)\), write \(d=a/b\), \(k=b\ell\), and obtain
\(\ell\le dx\), \((\ell,d)=1\). This proves
\(\sum_{d\mid a}C_d(dx)=\lfloor ax\rfloor\).

For bounded compactly supported \(h\), the complete source-orbit
pairing is therefore
\[
 Q(W_m(1\otimes h),W_n(1\otimes h))
 =\int_{\mathbb R}\frac{e^s\lfloor\gcd(m,n)e^{-s}\rfloor}{\sqrt{mn}}
       \overline{U_{\log m}h(s)}U_{\log n}h(s)\,e^sds.           \tag{16}
\]
All source vectors here have finite excitation expansions. Formula
(15) is the ordinary incidence factorization of the GCD matrix for
\(f_x(a)=\lfloor ax\rfloor\), whose Mobius convolution is the
nonnegative count \(C_a(ax)\). Its positivity is classical and
also immediate from the displayed Gram. Smoothing averages these
Grams; adding the norm adds the original positive GCD pairing.

## Controls, prior art and consequence for the line

The floor profile has different limits at the two ends of the real
axis and is not integrable there. It lies outside WP-448's finite
periodic measure space; its existence does not contradict that
finding's Fourier argument. The weights are excitation diagonal,
not multiplication by a function of the original valuation
configuration. No ergodicity claim about invariant scalar functions
on the Maharam space can silently be applied to them.

The construction uses no zeros or RH. It does use the ordinary
integer lattice and its coprimality partition. Its algebraic
positivity is the general meet-matrix incidence mechanism, not a
Riemann-specific sign law. Mixed-prime excitations retain positive
weight whenever \(s<\log n\); they have not been turned into a
prime-power selector. Replacing \(s\) by \(s-c\), choosing a
different positive smoothing kernel, or adding a scalar norm leaves
covariance intact. Thus covariance alone selects none of those
choices or a privileged sign comparison.

Oliveira e Silva's Section II-B gives the classical partial-sieve
recurrence; (6) is that same split for an arbitrary finite prime
set. Kaarnioja--Haukkanen--Ilmonen--Mattila, Theorem 2.5 and
Corollary 2.6, give the general incidence/Mobius criterion behind
(15). No new sieve identity or general positive-GCD theorem is
claimed. The local delta is the exact realization on the fixed
Maharam source, with full closed-domain covariance, its unbounded
excitation cost, and the counterexample to replacing periodicity by
bounded smooth vacuum regularity. Searches by sieve recurrence,
floor-GCD matrices, incidence positivity and Maharam forms do not
justify a historical novelty claim.

This answers the bounded nonperiodic existence question while
classicalizing its sign. It leaves the global completion clue open:
an independent source-selection theorem and the exact signed
finite-Weil, archimedean and polar comparison are still missing.
Neither a general nonperiodic classification nor an obstruction to
all such completions follows.

## Validation

An exact rational audit made 42,688 checks: 1,980 Mobius-count
identities, 9,900 normalized prime-compression identities, 1,980
kernel-boundary checks, 28,800 incidence-pairing identities, and 28
primorial-window checks. The first three used \(1\le n\le180\),
eight fixed positive rational values of \(x=e^{-s}\), and the
moving points \(x=1/n,999/(1000n),1001/(1000n)\); compression
used primes \(2,3,5,7,11\). Pairings used
\(1\le m,n\le60\) and the eight fixed values
\(1/97,1/13,1/2,999/1000,1,1001/1000,7/3,5\).
The primorial test used primes through 17 and
\(nx=1,5/4,3/2,7/4\). All checks passed.

The audit compares direct coprimality counting against divisor sums
and the independently normalized recurrences. It diagnoses floor
endpoints, prime-repeat cases and translation direction. Infinite
covariance, domain closure, smoothing and unboundedness are proved
above, not inferred from finite checks. The elementary counting
certificate is not proposed as a separate Lean handoff: the live
boundary here is its analytic domain realization, and no additional
structural ambiguity in the finite identity requires formalization.

## References

- [WP-447](WP-447-homogeneous-maharam-forms-recover-classical-gcd-grams.md), fixed excitation basis, source normalization and homogeneous forms.
- [WP-448](WP-448-periodic-maharam-forms-have-a-sharp-zeta-smoothing-threshold.md), periodic rigidity and the arbitrary-profile finite recurrence.
- T. Oliveira e Silva, *Computing pi(x): the combinatorial method*, Revista do DETUA **4**, no. 6 (2006), 759--768, Section II-B, [author text](https://sweet.ua.pt/tos/bib/5.4.pdf).
- V. Kaarnioja, P. Haukkanen, P. Ilmonen and M. Mattila, *Positive definite functions on semilattices*, Theorem 2.5 and Corollary 2.6, [author preprint](https://arxiv.org/pdf/1804.03047).
