---
title: "WP-444: Critical valuation energy drift has no measurable diagonal counterterm"
type: research-finding
status: verified
research_question: "Can the closed critical valuation energy become dilation invariant by subtracting a valuation-diagonal potential?"
claim_strength: exact_full_form_domain_dilation_cocycle_and_nonexistence_of_finite_measurable_diagonal_primitive
scope: WP-442's radial product probability and normalized valuation composition isometries; no assertion about all Bost--Connes GNS intertwiners or nonlocal completions
finding_id: WP-444
related_findings:
  - WP-442
  - WP-443
  - WP-288
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-24
updated: 2026-10-24
tags:
  - weil-positivity
  - valuation-product
  - dirichlet-form
  - dilation-cocycle
  - measurable-counterterm-obstruction
---

# WP-444: The critical energy has an uncancellable diagonal dilation drift

## Result and evidence boundary

**EXACT-DERIVED + LITERATURE+DERIVED; CLASSICAL NON-COBOUNDARY
OBSTRUCTION; NEGATIVE/OBSTRUCTION.** On the critical valuation space
of WP-442, let \(V_n\) be normalized composition by multiplication
by the integer \(n\), defined precisely below. Its closed positive
energy satisfies
\[
 \boxed{\mathcal E[V_ng]=\mathcal E[g]+\log n\,\|g\|^2.}
 \tag{1}
\]
This holds on the full form domain, which \(V_n\) preserves.

The correction in (1) has **no finite real measurable potential**:
there is no \(b:\Omega\to\mathbb R\), finite almost everywhere, with
\[
 \boxed{b(J+v(n))-b(J)=\log n\quad\text{almost everywhere for every }n.}
 \tag{2}
\]
In particular, a densely defined valuation-multiplication potential
cannot cancel this drift on the whole radial energy domain. This
excludes more than the formal divergent sum \(\sum_p J_p\log p\):
it also excludes any finite measurable tail-dependent replacement
with the same exact increments.

The Weil quadratic form is invariant under translation of the
logarithmic test variable. Thus the unmodified energy cannot be its
nonzero pullback under a map intertwining those translations with
the \(V_n\). Subtracting an ordinary valuation-diagonal potential
cannot repair that mismatch at critical temperature.

The result is specific to this action and this correction category.
The \(V_n\) are canonical partial composition operators on the
commutative valuation probability space; they are **not asserted to
be restrictions of the Bost--Connes isometries to the radial KMS
subspace**. That subspace need not be invariant under those
isometries. No nonlocal correction, interacting archimedean
completion, or full GNS construction is ruled out. No RH implication,
historical novelty, formal verification, or independent adversarial
approval is claimed.

## The action and its full-domain energy identity

Retain WP-442's definitions
\[
 \Omega=\prod_p\mathbb N_0,\qquad
 \nu=\prod_p\nu_p,\qquad \nu_p(j)=(1-p^{-1})p^{-j},
\]
\[
 \mathcal E[g]=\sum_p\sum_{j<k}(\log p)\nu_p(k)
       \|g_{p,j}-g_{p,k}\|_{L^2(\nu_{\ne p})}^2,
 \qquad D(\mathcal E)=\{g\in L^2(\nu):\mathcal E[g]<\infty\}.
 \tag{3}
\]
Here \(g_{p,j}\) is the section with coordinate \(J_p=j\).
For \(a=v(n)=(v_p(n))_p\), set
\[
 (V_ng)(J)=\sqrt n\,1_{J\ge a}\,g(J-a).
 \tag{4}
\]
The change of variables \(J=K+a\) has mass factor \(n^{-1}\).
Consequently \(V_n\) is an isometry, \(V_mV_n=V_{mn}\), and
\[
 V_nV_n^*=M_{1_{J\ge v(n)}},\qquad V_n1=\xi_n.
 \tag{5}
\]
Thus these operators implement the actual divisibility projections
and generate WP-442's divisibility form core from \(1\), without
identifying this representation with the full noncommutative source.

At one prime write \(r=p^{-1}\), \(\lambda=\log p\), and shift by
\(a\ge0\). Edges with both endpoints at least \(a\) contribute
exactly the original energy: \(\nu_p(k+a)=r^a\nu_p(k)\) cancels
the normalization \(r^{-a}\) in the squared difference. Edges with
both endpoints below \(a\) contribute zero. The remaining edges
give
\[
 \sum_{j=0}^{a-1}\sum_{k\ge a}
      \lambda\nu_p(k)r^{-a}|g(k-a)|^2
       =a\lambda\|g\|^2.
 \tag{6}
\]
The same calculation holds for sections valued in the complementary
Hilbert space. Other prime energies are unchanged by the isometry
on this coordinate. Summing the finitely many active shifts proves
(1). All terms are nonnegative, so Tonelli proves the identity even
with energy \(+\infty\); in particular
\[
 g\in D(\mathcal E)\quad\Longleftrightarrow\quad
 V_ng\in D(\mathcal E).
 \tag{7}
\]
Polarization gives the corresponding sesquilinear identity. This
is a quadratic-form compression law, not an assertion that the
operator commutator is \([A,V_n]=(\log n)V_n\).

As a normalization check, applying (1) to the divisibility core gives
\[
 \mathcal E(\xi_{nm},\xi_{nk})-
 \mathcal E(\xi_m,\xi_k)
   =\log n\,\frac{\gcd(m,k)}{\sqrt{mk}},
 \tag{8}
\]
exactly as WP-442's log-GCD kernel requires.

## Why no finite measurable diagonal primitive exists

Suppose (2) holds. It suffices to require it for each prime, with
almost-everywhere identities. All finite coordinate shifts are
nonsingular, and every value of a finite coordinate block has
positive probability. Fubini and the countability of the shifts
therefore allow iteration of these identities on a common conull
set of complementary coordinates.

For every finite prime set \(F\), this yields
\[
 b(J)=S_F(J)+b_F(J_{\ne F}),\qquad
 S_F=\sum_{p\in F}J_p\log p,
 \tag{9}
\]
where \(b_F\) is the section at \(J_p=0\) for \(p\in F\), finite
almost everywhere. The two terms in (9) are independent. Hence the
characteristic function of \(b\), requiring no moment assumptions,
satisfies
\[
 |\mathbb E e^{itb}|
 \le\prod_{p\in F}
       \left|\frac{1-p^{-1}}{1-p^{-1+it}}\right|.
 \tag{10}
\]
For fixed \(t\ne0\), the negative logarithm of the product is
\[
 D_F(t)=\sum_{p\in F}\sum_{k\ge1}
           \frac{1-\cos(kt\log p)}{k p^k}.
 \tag{11}
\]
Every summand is nonnegative. For \(\sigma>1\), the absolutely
convergent Euler product gives
\[
 D_\sigma(t):=\sum_p\sum_{k\ge1}
      \frac{1-\cos(kt\log p)}{k p^{k\sigma}}
   =\log\zeta(\sigma)-\log|\zeta(\sigma-it)|.
 \tag{12}
\]
As \(\sigma\downarrow1\), the first term tends to \(+\infty\).
The function \(\zeta\) is holomorphic near \(1-it\ne1\), so
\(|\zeta(\sigma-it)|\) is bounded above there. Thus
\(D_\sigma(t)\to+\infty\). No nonvanishing theorem on
\(\Re s=1\) is needed: a zero would only increase (12).
For each \(\sigma>1\), the full sum of (11) dominates (12).
It follows that \(D_F(t)\to+\infty\) along any exhaustion of the
primes. The right side of (10) tends to zero for every \(t\ne0\).

We would therefore have \(\mathbb E e^{itb}=0\) for every nonzero
\(t\), but \(\mathbb E e^{i0b}=1\). This contradicts continuity
at zero, which follows immediately by dominated convergence for
any finite real random variable. This proves (2) impossible.

The argument also excludes deterministic additive renormalization
of \(S_F\) to a finite limiting law: for any constants \(c_F\), the
modulus of the characteristic function of \(S_F-c_F\) has the same
zero limit away from the origin. In particular no such centered
family can have a weakly convergent subsequence along an exhaustion.
This consequence is about additive centering; rescaling changes the
problem and is not excluded.

## Relation to the Weil comparison and to diagonal subtraction

In logarithmic coordinates put
\[
 q_W(f)=W(f*\widetilde f),\qquad
 \widetilde f(x)=\overline{f(-x)},\qquad
 (\tau_a f)(x)=f(x-a).
\]
The identity
\((\tau_a f)*\widetilde{\tau_a f}=f*\widetilde f\)
gives \(q_W(\tau_a f)=q_W(f)\), without assuming positivity of
\(W\). It includes the complete distribution, with its finite,
archimedean and polar terms. WP-288 records this necessary
translation-invariance test; Connes--Consani, Appendices A--B,
fix the equivalent multiplicative convolution convention.

Suppose a map \(T\) on an admissible test class has values in
\(D(\mathcal E)\), intertwines \(\tau_{\log n}\) with \(V_n\)
for some \(n>1\), and claims \(q_W(f)=\mathcal E[Tf]\) for every
test and its translate. Then (1) forces
\[
 0=q_W(\tau_{\log n}f)-q_W(f)=\log n\,\|Tf\|^2.
 \tag{13}
\]
Thus \(T=0\). Even a one-sided translation family suffices for
this energy obstruction; no two-sided Hilbert-space intertwining
or boundedness of \(T\) is assumed.

A proposed diagonal correction has the form
\[
 \mathcal K_b[g]=\int b(J)|g(J)|^2\,d\nu(J).
\]
Where these integrals are defined absolutely, change of variables
in (4) gives
\[
 \mathcal K_b[V_ng]-\mathcal K_b[g]
   =\int\big(b(J+v(n))-b(J)\big)|g(J)|^2\,d\nu(J).
 \tag{14}
\]
In particular, if a finite real \(b\) is integrable and one requires
\(\mathcal E-\mathcal K_b\) to be \(V_n\)-invariant on **all
bounded cylinder functions** for every \(n\), those functions and
their images are in the absolute potential domain. Polarization
or cylinder indicators in (14) then force (2): the resulting
integrable difference has zero integral on every cylinder set,
which determines the measure. The contradiction above excludes
this correction. Requiring the potential on the entire original
form domain is stronger, since that domain contains \(1\) and
all bounded cylinders.

More generally (2) itself has no finite measurable solution,
irrespective of integrability or lower bounds. A multiplication
operator declared to implement the exact cocycle therefore does
not gain a solution by shrinking its domain. We do **not** infer
pointwise equality from an identity tested only on an unspecified
proper subspace, or exclude a different reduced test class.

## Controls, prior art, and remaining boundary

At a finite prime cutoff, \(b_F=S_F\) really does solve all the
shift equations for those primes. For the product law
\(\nu_{p,\beta}(j)=(1-p^{-\beta})p^{-\beta j}\), \(\beta>1\),
only finitely many coordinates are occupied almost surely because
\(\sum_p p^{-\beta}<\infty\). Then
\(b(J)=\sum_pJ_p\log p\) is finite almost everywhere and solves
(2). These controls distinguish the all-prime critical obstruction
from a purely algebraic impossibility.

The local energy calculation also works for an arbitrary geometric
law \((1-r)r^j\) and positive scale \(\lambda\), with drift
\(a\lambda\). That positivity and covariance mechanism is universal.
The critical no-primitive theorem additionally uses the specific
prime law and logarithmic increments through (12). A matched
product with summable occupation probabilities has a finite
primitive instead. Neither control is asserted to satisfy a
global Weil identity.

The logarithmic Euler-product characteristic function is classical
zeta-distribution probability. The analytic input used here is only
the Euler product for \(\Re s>1\) and the simple pole at one with
holomorphy elsewhere, as recorded in DLMF §§27.4 and 25.2. The
non-coboundary theorem itself is a corollary of known type-III
theory: in the proof of Theorem 2.1, Neshveyev explicitly identifies
the same product of geometric valuation laws and its finite-change
equivalence relation, and proves that relation has type \(\mathrm{III}_1\).
If (2) held, the equivalent sigma-finite measure
\(d\mu=e^b\,d\nu\) would satisfy
\[
 \mu(A+v(n))=n^{-1}\int_A e^{b(J+v(n))}\,d\nu(J)=\mu(A),
\]
contradicting type III. Thus this boundary is **classical prior art**,
not a new non-coboundary theorem. Equations (9)--(12) give an
elementary direct proof for the exact critical specialization and
also settle additive centering, without importing the full
ratio-set classification.

The line-local delta is a restriction on the **actual comparison
map** left missing by WP-442--WP-443: the positive energy has the
wrong dilation law under the natural radial multiplication action,
and the most direct diagonal repair is not a measurable operator
at critical probability. This is distinct from WP-443's spectral
diagonalization: diagonal in its excitation basis is not the same
as multiplication by a function of the valuation configuration.
Any surviving completion must specify a different action,
nonlocal correction, restricted comparison space, or genuinely
global coupling, and prove its sign and normalization separately.
The accepted completion clue remains unresolved.

## Validation

An exact rational audit used \(r=1/2,1/3,1/5,2/5,3/4\), scale one,
shift lengths \(1\le a\le6\), and twenty pairs of rational vectors
supported on \(0,\ldots,10\) per case (seed 444). All 600 bilinear
norm and energy shift identities passed. Infinite outgoing tails
were summed as geometric series, not discarded at the cutoff.
This checks normalization and the boundary charge; the domain,
nonexistence, and infinite-prime conclusions follow from the
proofs above rather than a finite experiment.

## References

- [WP-442](WP-442-critical-valuation-product-supports-a-closed-log-gcd-energy.md), the closed energy, divisibility core, and critical probability sector.
- [WP-443](WP-443-critical-valuation-energy-has-an-explicit-hierarchical-spectrum.md), the distinct excitation-basis diagonalization and observable boundary.
- [WP-288](WP-288-exact-cone-only-weil-quadratic-forms-linearize-to-positive-definite-distributions.md), translation invariance required of an exact Weil-square realization.
- NIST DLMF, [§27.4, equation 27.4.3](https://dlmf.nist.gov/27.4.E3) and [§25.2(i)](https://dlmf.nist.gov/25.2), the Euler product, meromorphic continuation and pole at one used in (12).
- S. Neshveyev, *Von Neumann Algebras Arising from Bost--Connes Type Systems*, IMRN **2011** (2011), 217--236; [author preprint](https://arxiv.org/pdf/0907.1456), Theorem 2.1 and its proof. The proof explicitly treats the geometric valuation product and its finite-change relation; type III already implies the no-measurable-primitive assertion.
- A. Connes and C. Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Mathematica **27** (2021), Paper 77; [author text](https://alainconnes.org/wp-content/uploads/Selecta.pdf), Appendices A--B. Multiplicative convolution and explicit-formula normalization.
