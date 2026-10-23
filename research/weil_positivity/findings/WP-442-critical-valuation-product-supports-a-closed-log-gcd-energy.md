---
title: "WP-442: The critical valuation product supports a closed log-GCD energy in a different occupation sector"
type: research-finding
status: verified
research_question: "Does the Gibbs ground-state completion survive at critical temperature on the KMS valuation probability space, and what pairing does it actually produce?"
claim_strength: exact_closed_conservative_product_form_divisibility_energy_kernel_and_representation_boundary
scope: radial valuation subspace of the critical Bost--Connes KMS Hilbert space; prescribed local jump conductances; no full noncommutative Markov extension, archimedean comparison, or Weil positivity theorem
finding_id: WP-442
related_findings:
  - WP-441
  - WP-216
  - WP-217
  - WP-395
  - WP-009
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-24
updated: 2026-10-24
tags:
  - weil-positivity
  - bost-connes
  - critical-kms
  - dirichlet-form
  - valuation-product
  - ground-state-transform
  - representation-boundary
---

# WP-442: Critical probability repairs the domain, while retaining the completion terms

## Result and evidence boundary

**EXACT-DERIVED; CLASSICAL PRODUCT JUMP FORM AND GCD POSITIVITY;
REPRESENTATION BOUNDARY.** WP-441's diagonal completion has divergent
critical Gibbs cost in the standard integer occupation representation.
That does not prevent its local critical ground-state transforms from
assembling into a densely defined, closed, conservative Dirichlet form
on the **critical valuation probability space**. We construct that form
below, including its domain and a form core.

For the canonical normalized divisibility vectors
\(\xi_n=\sqrt n\,1_{n\widehat{\mathbb Z}}\), the resulting energy is
exactly
\[
 \boxed{\mathcal E(\xi_m,\xi_n)
   =\log\gcd(m,n)\,\frac{\gcd(m,n)}{\sqrt{mn}}.}
 \tag{1}
\]
Their linear span is a form core in the radial valuation Hilbert space.
Thus (1) specifies more than a family of finite positive matrices:
it has a closed realization in the source's critical Gram norm.

In an orthonormal shell basis at a single prime, the same form is
\[
 Q_p=H_p+\frac{\log p}{p-1}I+W_p,
 \quad H_pe_j=j\log p\,e_j,\quad
 W_p(j,k)=-\log p\,p^{-|j-k|/2}\quad(j\ne k),\quad W_p(j,j)=0.
 \tag{2}
\]
So it retains the desired local off-diagonal entries **together with**
the explicit positive completion. The infinite construction uses
equilibrium reference vectors, not the integer occupation vacuum.
Finite integer configurations have measure zero in this critical
space. It is therefore not a semibounded extension or scalar
renormalization of WP-441's critical form on \(c_{00}(\mathbb N)\).

The jump rule is an additional prescription, albeit one uniquely
determined locally if the negative off-diagonal coefficients and
conservativity are imposed. KMS equilibrium alone does not select it.
The construction has no Gamma or polar term, and no identification
with the global Weil test form. It repairs a precise domain problem;
it does not establish the missing Weil sign.

## Critical source probability and the radial Hilbert space

Let \(J_p\) be independent nonnegative integer-valued coordinates with
\[
 \nu_p(j)=(1-p^{-1})p^{-j},\qquad
 (\Omega,\nu)=\prod_p(\mathbb N_0,\nu_p),\qquad
 \mathcal H_{\rm rad}=L^2(\Omega,\nu).
 \tag{3}
\]
These are the valuations of Haar-distributed elements of
\(\widehat{\mathbb Z}=\prod_p\mathbb Z_p\):
\(\Pr(J_p\ge a)=p^{-a}\). Values \(v_p(0)=\infty\) form a null
set and do not affect this realization.

Equivalently, WP-216's KMS identities already determine the law on
the divisibility algebra: for every finite prime set,
\(\phi_1(\prod_p E_{p^{a_p}})=\prod_p p^{-a_p}\).
Taking differences of these tail probabilities gives (3). This
identifies \(\mathcal H_{\rm rad}\) with the closed subspace generated
by divisibility projections acting on the critical KMS cyclic vector.
It is not the full Bost--Connes GNS space or the whole centralizer.

Write \(D_n=\{J_p\ge v_p(n)\text{ for all }p\}\). Then
\(\xi_n=\sqrt n\,1_{D_n}\) and
\[
 \langle\xi_m,\xi_n\rangle
 =\frac{\sqrt{mn}}{\operatorname{lcm}(m,n)}
 =:G(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}}.
 \tag{4}
\]
All these vectors are bounded cylinder functions. Their span contains
every finite-coordinate singleton indicator, by taking differences
\(1_{J_p\ge a}-1_{J_p\ge a+1}\) and products. In particular it is
dense in \(\mathcal H_{\rm rad}\).

## Closed conservative energy, including the infinite-prime domain

For \(j<k\), prescribe the local conductance
\[
 c_p(j,k)=(\log p)\nu_p(k).
 \tag{5}
\]
Extend it symmetrically by \(c_p(k,j)=c_p(j,k)\).
It is the ground-state transform of the off-diagonal magnitude
\((\log p)p^{-(k-j)/2}\), since
\[
 c_p(j,k)=(\log p)p^{-(k-j)/2}
                 \sqrt{\nu_p(j)\nu_p(k)}.
 \tag{6}
\]
For \(g\in\mathcal H_{\rm rad}\), let \(g_{p,j}\) denote its section
with the \(p\)-coordinate fixed at \(j\), in the complementary
product space with measure \(\nu_{\ne p}\). Set
\[
 \begin{split}
 \mathcal E_p[g]&=\sum_{j<k}c_p(j,k)
             \|g_{p,j}-g_{p,k}\|_{L^2(\nu_{\ne p})}^2,\\
 \mathcal E[g]&=\sum_p\mathcal E_p[g],\qquad
 D(\mathcal E)=\{g\in\mathcal H_{\rm rad}:\mathcal E[g]<\infty\}.
 \end{split}
 \tag{7}
\]
The sesquilinear form uses polarization, conjugate-linear in the first
argument. No finite total conductance over all primes is assumed.

For each fixed \(p\),
\[
 \sum_{j<k}c_p(j,k)
 =\log p\sum_{k\ge0}k\nu_p(k)=\frac{\log p}{p-1}<\infty.
 \tag{8}
\]
A bounded cylinder function has differences only at its finitely many
active primes. Equation (8) therefore puts every such function in
\(D(\mathcal E)\), proving density.

For fixed \(p,j\), section evaluation is bounded from
\(\mathcal H_{\rm rad}\) to \(L^2(\nu_{\ne p})\), with norm at most
\(\nu_p(j)^{-1/2}\). Consequently the operator
\[
 Tg=\big(\sqrt{c_p(j,k)}(g_{p,j}-g_{p,k})\big)_{p,j<k}
 \tag{9}
\]
into the Hilbert direct sum of those complementary spaces is closed
on its maximal domain. Indeed convergence of \(g\) and \(Tg\)
forces the limit of every component by bounded section evaluation.
Thus (7) is a closed nonnegative form. Real normal contractions
decrease each squared difference, so it is a Dirichlet form.
The constant function \(1\) belongs to the domain with zero energy;
the associated self-adjoint Markov semigroup preserves it. This is
conservativity at the semigroup level, without a claim about sample
paths of an infinite-jump process.

Here is also a core argument. Let \(P_Fg\) be conditional expectation
onto a finite set of prime coordinates. For \(p\in F\), the edge
difference of \(P_Fg\) is the corresponding conditional expectation
of the edge difference of \(g\); for \(p\notin F\) it is zero.
Hence \(P_F\) contracts the energy. Along an increasing exhaustion,
martingale convergence in each edge space and dominated summation in
(9) give \(P_Fg\to g\) in the form norm. Real and imaginary truncation
then approximate finite-energy cylinder functions by bounded ones:
the truncation remainders have edge differences dominated by those
of the original function and tending pointwise to zero. Finally,
cut a bounded cylinder function off to a finite box in its active
coordinates. Equation (8), boundedness, and dominated convergence
give convergence in form norm. Such finite-box functions are finite
linear combinations of the divisibility tails in (4). Therefore
\(\operatorname{span}\{\xi_n:n\ge1\}\) is a form core.

## Exact local matrix and the divisibility pairing

The local jump generator, with Markov sign convention, is
\[
 (L_pg)(j)=\log p\left[
   \sum_{k<j}(g(k)-g(j))+
   \sum_{k>j}p^{-(k-j)}(g(k)-g(j))\right].
 \tag{10}
\]
Its upward rate is \((\log p)p^{-(k-j)}\), its downward rate
is \(\log p\), and detailed balance is exactly (5).
On finitely supported local vectors the sums and matrix entries
are legitimate. Conjugating \(-L_p\) by
\(U_pg(j)=\sqrt{\nu_p(j)}g(j)\) gives (2): the off-diagonal entry
is \(-c_p(j,k)/\sqrt{\nu_p(j)\nu_p(k)}\), and the diagonal is
\[
 \frac{1}{\nu_p(j)}\sum_{k\ne j}c_p(j,k)
   =\log p\left(j+\frac1{p-1}\right).
 \tag{11}
\]
The equilibrium vector \(u_p(j)=\sqrt{\nu_p(j)}\) has zero energy.
If these off-diagonal entries are fixed, the equation \(Q_pu_p=0\)
forces (11); it is not another free diagonal parameter.

For a tail \(h_a(j)=1_{j\ge a}\), only edges crossing both
thresholds contribute to the bilinear pairing. Thus
\[
 \mathcal E_p(h_a,h_b)
 =\sum_{j<\min(a,b)}\sum_{k\ge\max(a,b)}(\log p)\nu_p(k)
 =(\log p)\min(a,b)p^{-\max(a,b)}.
 \tag{12}
\]
After normalizing the two tails, this is
\((\log p)\min(a,b)p^{-|a-b|/2}\).
For \(\xi_m,\xi_n\), the inactive coordinates contribute their
ordinary inner products. Summing the active local energies gives
\[
 \mathcal E(\xi_m,\xi_n)
 =G(m,n)\sum_p(\log p)\min(v_p(m),v_p(n)),
 \tag{13}
\]
which proves (1). In particular \(\mathcal E[\xi_n]=\log n\),
\(\mathcal E(\xi_1,\xi_n)=0\), and coprime labels have zero energy
pairing. These are useful normalization and orientation checks.

## Why this does not contradict the critical occupation obstruction

For finitely many primes \(F\), the orthonormal shell representation
has the exact sum
\[
 Q_F=H_F+C_FI+W_F,\qquad
 C_F=\sum_{p\in F}\frac{\log p}{p-1}.
 \tag{14}
\]
The product construction embeds it into a larger finite-prime space
by \(f\mapsto f\otimes u_p\). Since \(Q_pu_p=0\), energies are
consistent under these embeddings. It does not embed by
\(f\mapsto f\otimes e_0\), which would charge
\(\langle e_0,Q_pe_0\rangle=\log p/(p-1)\) at every new prime.
The latter charges have divergent sum. Positivity of the combined
closed form never licenses splitting (14) into three separately
defined infinite operators.

Indeed under (3), the events \(J_p\ge1\) are independent with
probability \(1/p\). Reciprocal-prime divergence and Borel--Cantelli
imply infinitely many occupied primes almost surely. The set of
finite integer configurations is null. In particular, mapping the
old occupation vectors to indicators of those exact configurations
gives zero, not an isometry.

There is no nonzero bounded intertwiner of all divisibility
projections between the standard integer occupation representation
and this radial representation. To see this, fix an integer \(n\)
and let \(R_{n,F}\) impose \(J_p=v_p(n)\) for \(p\in F\).
Each is a finite product of differences of divisibility projections.
As \(F\) exhausts the primes, it converges strongly to the rank-one
projection onto \(e_n\) in the integer representation, and to zero
in (3). An intertwiner must therefore annihilate every \(e_n\).
This is a concrete domain/observable comparison, not a claim that
the abstract separable Hilbert spaces cannot be isomorphic.

For comparison, replacing \(\nu_p(j)\) by
\((1-p^{-\beta})p^{-\beta j}\), \(\beta>1\), makes finite integer
configurations have full measure, with masses \(n^{-\beta}/\zeta(\beta)\).
The conductances
\((\log p)p^{-(k-j)/2}\sqrt{\nu_{p,\beta}(j)\nu_{p,\beta}(k)}\)
then recover WP-441 under the global ground-state isometry. At
these temperatures the total transformed edge mass is the finite
\(C_\beta\) of WP-441, so finite integer cutoffs give the same
closed-form core. At
\(\beta=1\) the local formula remains valid but that global integer
identification fails. No same-Hilbert-space Mosco or resolvent limit
is asserted here.

## Source selection, matched controls, and prior art

KMS fixes (3) and the divisibility Gram, but detailed balance alone
allows many reversible conductances. Equations (5)--(6) select one
by requiring the previously identified finite-Weil off-diagonal
magnitudes. Its positivity is an ordinary sum-of-squares theorem,
not a further consequence of KMS selecting this dynamics.

The positive construction survives the replacement of primes by
arbitrary independent coordinates with geometric laws
\((1-r_i)r_i^j\), \(0<r_i<1\), and arbitrary finite positive
scales \(\lambda_i\). Use
\(c_i(j,k)=\lambda_i(1-r_i)r_i^k\) for \(j<k\).
Every coordinate has finite total conductance
\(\lambda_ir_i/(1-r_i)\); bounded cylinders are still a dense
domain even when their sum diverges. The local matrix is
\(\lambda_i(j+r_i/(1-r_i))\) on the diagonal and
\(-\lambda_i r_i^{|j-k|/2}\) off it. Thus the existence and sign
are not arithmetic-specific. These are controls for the mechanism,
not asserted alternative global Weil models.

The product jump-form and ground-state methods are classical.
Schilling--Uemura discuss jump-form domains; Keller--Pinchover--
Pogorzelski, Proposition 4.8, supplies the ground-state-transform
comparison. The domain and core proof above is given directly
rather than imported from a theorem with different state-space
hypotheses. Bost--Connes KMS theory and Neshveyev's critical-sector
analysis supply the equilibrium background; WP-216 already derives
the exact divisibility law used here.

Even positivity of the kernel (1) alone is classical: the identity
\[
 \log\gcd(m,n)=\sum_{d\mid m,\ d\mid n}\Lambda(d)
 \tag{15}
\]
is a positive incidence Gram. Its Schur product with (4) is positive.
Kaarnioja--Haukkanen--Ilmonen--Mattila, Theorems 2.5 and 2.7,
give the general semilattice positivity/factorization framework.
No novelty is claimed for log-GCD positivity or its Schur product.

The line-local result is the closed realization and core for (1)
on the actual critical valuation law, the exact local matrix (2),
and the explanation of why it evades WP-441's domain obstruction
without giving its desired critical subtraction. WP-217 instead
differentiates the Poisson log density; WP-009 instead uses
translation jumps on the Weil test line. Neither domain is (7).
WP-395's loss of exact orbit support is consistent with the
representation boundary proved here.

The remaining comparison would have to map a global Weil test class
into this radial form and account for the extra terms in (14),
the archimedean contribution, and polar normalization. No such map
or identity is established. The result therefore narrows the
accepted completion clue without resolving it or supplying an RH
implication.

## Validation

A standard-library Python normalization audit used primes
\(2,3,5,11\), local support \(0\le j<12\), and twenty complex
random vectors per prime (independent real and imaginary uniform
coordinates in \([-1,1]\), seed 442). Infinite outgoing tails were
summed geometrically. The energy in (7) and the matrix in (2)
agreed with maximum relative error \(3.8\cdot10^{-16}\).
For tail thresholds \(0\le a,b<10\), direct sums through index
99 agreed with (12) within \(2.8\cdot10^{-17}\); shell diagonals
agreed within \(3.6\cdot10^{-15}\). The tensor pairing (13) for
all 10,000 pairs \(1\le m,n\le100\) agreed with (1) within
\(8.9\cdot10^{-16}\).

These are floating-point finite normalization checks. Closure,
the form core, conservativity, and the representation obstruction
rest on the proofs above, not on numerics. No formal verification
or independent adversarial approval is claimed.

## References

- [WP-441](WP-441-gibbs-minimal-diagonal-completion-has-divergent-critical-cost.md).
- [WP-216](WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md), [WP-217](WP-217-bost-connes-conditioned-gram-score-is-exactly-the-prime-torus-poisson-score.md).
- [WP-395](WP-395-critical-kms-centralizer-erases-exact-prime-power-orbit-support.md), [WP-009](WP-009-prime-lattice-weil-weights-fail-passive-jump-energy.md).
- J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica **1** (1995), 411--457, [DOI: 10.1007/BF01589495](https://doi.org/10.1007/BF01589495).
- S. Neshveyev, *Von Neumann Algebras Arising from Bost--Connes Type Systems*, International Mathematics Research Notices **2011** (2011), 217--236, [author preprint](https://arxiv.org/pdf/0907.1456), introduction and Section 2.
- R. L. Schilling and T. Uemura, *On the Structure of the Domain of a Symmetric Jump-type Dirichlet Form*, Publications of RIMS **48** (2012), 1--20, [DOI: 10.2977/PRIMS/58](https://ems.press/journals/prims/articles/10879).
- M. Keller, Y. Pinchover, F. Pogorzelski, *Criticality theory for Schrödinger operators on graphs*, Journal of Spectral Theory **10** (2020), 73--114, [author preprint](https://arxiv.org/pdf/1708.09664), Proposition 4.8.
- V. Kaarnioja, P. Haukkanen, P. Ilmonen, M. Mattila, *Positive definite functions on semilattices*, [arXiv:1804.03047v2](https://arxiv.org/pdf/1804.03047), Theorems 2.5 and 2.7.
