---
title: "WP-441: The Gibbs-minimal diagonal completion is unique and has divergent critical cost"
type: research-finding
status: verified
research_question: "Does minimizing Gibbs expectation select a positive diagonal completion of the all-prime defect that survives the critical-temperature limit?"
claim_strength: exact_unique_weighted_trace_minimizer_closed_form_realization_and_critical_subtraction_obstruction
scope: diagonal additions to the algebraic all-prime Weil defect on c00(N) in the standard positive-energy representation, with normal Gibbs weight beta>1; no critical KMS completion or global Weil positivity theorem
finding_id: WP-441
related_findings:
  - WP-440
  - WP-148
  - WP-265
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-23
updated: 2026-10-23
tags:
  - weil-positivity
  - bost-connes
  - diagonal-completion
  - gibbs-cost
  - ground-state-transform
  - critical-renormalization
---

# WP-441: Minimizing the thermal cost fixes the bath but does not preserve its critical sign

## Claim and evidence boundary

**EXACT-DERIVED; CLASSICAL GROUND-STATE TRANSFORM; CRITICAL OBSTRUCTION.**
WP-440 supplies freely chosen growing diagonal completions. Here a
specific variational rule removes that freedom: minimize the Gibbs
expectation of the added diagonal, subject to positivity and preservation
of every off-diagonal prime-power coefficient. For every fixed
\(\beta>1\), this optimization has a unique minimizer, explicitly
\[
 d_\beta(n)=C_\beta+
       \sum_{d\mid n}\Lambda(d)d^{(\beta-1)/2},\qquad
 C_\beta=-\frac{\zeta'}{\zeta}\left(\frac{\beta+1}{2}\right).
 \tag{1}
\]
Its minimum normalized Gibbs cost is exactly \(2C_\beta\). The
completed algebraic form is closable and nonnegative; its closure has
the Gibbs square-root vector as a zero-energy vector.

Nevertheless,
\[
 C_\beta=\frac{2}{\beta-1}-\gamma+O(\beta-1),\qquad
 \min\operatorname{Tr}(\rho_\beta D)=
       \frac{4}{\beta-1}-2\gamma+O(\beta-1).
 \tag{2}
\]
Subtracting the exact vacuum charge \(C_\beta I\) gives, on the
fixed finite-support core, the critical limit \(H+W\). That form
is unbounded below. Any scalar subtraction leaving a finite vacuum
value gives the same limit up to a scalar, and so cannot retain
semiboundedness. Scalar normalization that keeps the vacuum finite
instead erases every fixed off-diagonal coefficient.

These conclusions concern the specified diagonal optimization and scalar
renormalizations. The rule of minimizing this cost is an additional
choice, not a proved consequence of the Bost--Connes source. Neither
the positive completion nor the zeta expression for its cost supplies
the archimedean term, polar normalization, Weil test-space bridge, or RH.

## Exact object and optimization class

Use \(\mathcal H=\ell^2(\mathbb N)\), \(He_n=(\log n)e_n\),
and WP-440's algebraic form
\[
 w[f]=-2\operatorname{Re}\sum_{m\ge1,d\ge2}
       \frac{\Lambda(d)}{\sqrt d}\overline{f_m}f_{md},
       \qquad f\in c_{00}(\mathbb N).
 \tag{3}
\]
Every such sum is finite. Write \(a_{m,md}=\Lambda(d)/\sqrt d\)
for the nonnegative weight of an undirected edge; each nonzero edge
is counted once by \((m,d)\). The zero-diagonal matrix \(A\) of
these weights is notation for the form, not an assertion that its
columns belong to \(\ell^2\).

Fix \(\beta>1\) and set
\[
 Z_\beta=\zeta(\beta),\quad
 \pi_\beta(n)=\frac{n^{-\beta}}{Z_\beta},\quad
 u_n=\sqrt{\pi_\beta(n)},\quad
 \rho_\beta=\operatorname{diag}(\pi_\beta(n)).
 \tag{4}
\]
Admissible diagonals are real finite-valued sequences \(v_n\) for
which
\[
 q_v[f]=\sum_n v_n|f_n|^2+w[f]\ge0
             \quad(f\in c_{00}).
 \tag{5}
\]
Testing \(e_n\) forces \(v_n\ge0\). Their cost is the extended
nonnegative number
\[
 J_\beta(v)=\sum_n\pi_\beta(n)v_n.
 \tag{6}
\]
Thus the minimization ranges over all diagonal positive completions
on this core, even ones for which no closed realization was initially
specified. It does not range over arbitrary off-diagonal corrections.

The total weighted edge mass is finite:
\[
 S_\beta:=\sum_{m,d}a_{m,md}u_mu_{md}
   =\frac1{Z_\beta}\sum_m m^{-\beta}
       \sum_{d\ge2}\Lambda(d)d^{-(\beta+1)/2}
   =C_\beta<\infty.
 \tag{7}
\]
Only the absolutely convergent Dirichlet series in \(\Re s>1\)
is used here; no zero information or analytic continuation is needed.

## Minimum and equality rigidity

Let \(P_N\) project onto labels \(1,\ldots,N\). For every
admissible \(v\), (5) gives
\[
 \sum_{n\le N}v_nu_n^2\ \ge\
       2\sum_{md\le N}a_{m,md}u_mu_{md}.
 \tag{8}
\]
Monotone convergence of both nonnegative sums proves
\(J_\beta(v)\ge2C_\beta\), also when the left side is infinite.

Define the weighted degree
\[
 v_n^*=\frac1{u_n}\sum_{j\ne n}a_{nj}u_j.
 \tag{9}
\]
Splitting into multiples and divisors gives exactly
\[
 v_n^*=\sum_{d\ge2}\Lambda(d)d^{-(\beta+1)/2}
       +\sum_{d\mid n}\Lambda(d)d^{(\beta-1)/2}
       =d_\beta(n).
 \tag{10}
\]
The first sum converges and the second is finite. Expanding squares,
with all terms absolutely summable for finite-support \(f\), gives
\[
 q_{d_\beta}[f]
 =\sum_{m,d}a_{m,md}u_mu_{md}
       \left|\frac{f_m}{u_m}-\frac{f_{md}}{u_{md}}\right|^2
 \ge0.
 \tag{11}
\]
Each edge contributes to two diagonal entries, so Tonelli and (7)
give \(J_\beta(d_\beta)=2C_\beta\).

For uniqueness, suppose \(J_\beta(v)=2C_\beta\). Then (8)
implies \(q_v[P_Nu]\to0\). The Cauchy--Schwarz inequality for
the positive sesquilinear form on \(c_{00}\) yields, for fixed \(n\),
\[
 |q_v(e_n,P_Nu)|^2\le v_n q_v[P_Nu]\longrightarrow0.
 \tag{12}
\]
The weighted row \(\sum_j a_{nj}u_j\) is absolutely convergent
by (10). Taking its limit in (12) gives
\[
 v_nu_n-\sum_j a_{nj}u_j=0.
 \tag{13}
\]
Because \(u_n>0\), every entry is forced to equal (9). No
compactness of the optimization class, existence assumption, or
unproved infinite-dimensional trace duality is being used.

## Closed form and its zero-energy vector

Let \(c_{m,md}=a_{m,md}u_mu_{md}\). Map \(c_{00}\) into
\(\ell^2\) of the countable edge set by
\[
 (T_0f)_{m,md}=\sqrt{c_{m,md}}
       (f_m/u_m-f_{md}/u_{md}).
 \tag{14}
\]
This map is well-defined by (10)--(11) and is closable. Indeed,
if \(f_k\to0\) in vertex \(\ell^2\) and \(T_0f_k\to g\)
in edge \(\ell^2\), each fixed edge coordinate converges to zero,
so \(g=0\). Consequently \(\|\overline T_0f\|^2\) is a
closed nonnegative form whose core is \(c_{00}\) and which
agrees with (11) there.

Moreover \(P_Nu\to u\) in \(\ell^2\), and
\[
 \|T_0P_Nu\|^2=
       \sum_{m\le N<md}c_{m,md}\longrightarrow0
 \tag{15}
\]
by dominated convergence and \(\sum c=C_\beta<\infty\).
Thus \(u\in D(\overline T_0)\) and \(\overline T_0u=0\).
The associated self-adjoint nonnegative operator has \(u\) in its
kernel. This does not assert that the basis vectors lie in its
operator domain: the unchanged off-diagonal columns are not square
summable. They do lie in its form domain.

Equation (11) is the classical ground-state transform. In the weighted
vertex space \(\ell^2(\pi_\beta)\), the substitution \(f=ug\)
turns it into the ordinary graph energy \(\sum c_{ij}|g_i-g_j|^2\).
We established the summability and closure directly; applying a graph
theorem to the raw, infinite-degree matrix \(A\) without that step
would be invalid.

## Critical subtraction destroys the sign

The Laurent expansion of \(\zeta\) at one gives (2). For each
fixed label \(n\), the divisor sum in (1) is finite and hence
\[
 d_\beta(n)-C_\beta\longrightarrow
           \sum_{d\mid n}\Lambda(d)=\log n.
 \tag{16}
\]
It follows for every fixed \(f\in c_{00}\) that
\[
 q_{d_\beta}[f]-C_\beta\|f\|^2
       \longrightarrow\langle f,Hf\rangle+w[f].
 \tag{17}
\]
This is a statement of convergence on the common algebraic core;
no Mosco, resolvent, or operator-domain limit is inferred from it.

Here is a direct lower-bound obstruction, independent of that caveat.
For any \(M\ge0\), choose finitely many primes \(F\) and set
\[
 f=e_1+\sum_{p\in F}
       \frac{\log p}{\sqrt p(\log p+M)}e_p.
\]
Distinct primes have no mutual edge. Completing the leaf squares gives
\[
 \langle f,Hf\rangle+w[f]+M\|f\|^2
       =M-\sum_{p\in F}\frac{(\log p)^2}{p(\log p+M)}.
 \tag{18}
\]
The sum diverges as \(F\) exhausts the primes: for sufficiently
large \(p\), its summand is at least \((\log p)/(2p)\), and
even \(\sum_p1/p\) diverges. Therefore (18) becomes negative
for every proposed lower bound \(-M\). The limit form in (17)
is unbounded below, in agreement with WP-440's subcritical diagonal
growth obstruction.

More generally, subtract a real scalar \(r_\beta I\). Since
\(d_\beta(1)=C_\beta\), a finite vacuum limit means
\(C_\beta-r_\beta\to\ell\in\mathbb R\). The core limit
is then \(H+W+\ell I\), still unbounded below. Subtracting only
\(2/(\beta-1)\) is included, with \(\ell=-\gamma\).

Alternatively, if nonnegative scalars \(a_\beta\) keep
\(a_\beta d_\beta(1)\) bounded, then \(a_\beta\to0\).
Every fixed off-diagonal entry becomes
\(-a_\beta\Lambda(d)/\sqrt d\to0\). For example,
\(q_{d_\beta}[f]/C_\beta\to\|f\|^2\) on \(c_{00}\).
Scalar subtraction and scalar normalization therefore fail for
different explicit reasons; this does not classify non-scalar or
finite--archimedean renormalizations.

## Source, matched-control, and prior-art audit

The optimization is unique **after** its objective, admissible diagonal
class, and negative off-diagonal kernel have been fixed. No independent
source principle has been proved to impose that optimization. A Gibbs
square-root vector here is a device for the weighted trace inequality,
not an assertion that the mixed Gibbs state is that pure state.

The positivity mechanism is universal. For any countable undirected
nonnegative edge system \(a_{ij}\) and strictly positive unit vector
\(u\) with \(\sum_{i<j}a_{ij}u_iu_j<\infty\), the same proof
gives the unique minimum-cost diagonal (9), the minimum twice the edge
mass, and the closed energy (11). It works on nonarithmetic graphs.
Arithmetic supplies the explicit divisor sum and cost in (1), not a
new sign theorem. No claim is made that those control graphs are Weil
models.

Keller--Pinchover--Pogorzelski, Proposition 4.8, is the direct classical
ground-state-transform comparison; their Section 3 treats closed graph
forms. NIST DLMF (27.4.12) and (25.2.4) supply the Dirichlet series and
Laurent expansion used here. Weighted graph energies, diagonal
majorization, and the elementary positivity/equality argument are not
claimed as new general theorems. Searches by ground-state transforms,
weighted-trace diagonal majorization, and Bost--Connes/Mangoldt Gibbs
completions did not identify this exact arithmetic optimization; absence
from those searches is not a historical novelty claim.

The line-local delta is the unique all-label Gibbs-cost minimizer and
its exact critical failure. WP-440 classified a freely specified
Hamiltonian growth family, not this optimization. WP-148 treated the
different cyclotomic-resultant graph with a constant conserving vector
and an infinite-degree collapse; here the Gibbs-weighted completion
exists for each \(\beta>1\). WP-265 compared finite parts of another
incidence Gram, not the unchanged defect (3).

The critical temperature has no normal trace density (4) in this
representation. Nothing above says that Bost--Connes has no critical
KMS state, or excludes a different GNS sector, mixed correction,
source-fixed non-diagonal geometry, or global Weil test class. The
Gamma and polar sectors remain absent. This closes this variational
diagonal route to a finite critical sign, not the whole accepted
Bost--Connes completion clue.

## Validation

A standard-library Python audit on labels \(1\le n\le250\)
used all 652 prime-power edges, \(\beta=1.1,1.5,2,3\), and 20
complex random vectors per temperature (independent real and imaginary
coordinates uniform in \([-1,1]\), seed 441). For the induced finite
graph it checked the multiple/divisor weighted-degree identity, (11),
the twice-edge-mass cost, and the ground-state equation for \(u\).
Maximum relative discrepancies were respectively
\(5.2\cdot10^{-16}\), \(2.2\cdot10^{-16}\), and
\(1.9\cdot10^{-16}\); the maximum absolute null residual was
\(1.6\cdot10^{-15}\). The explicit star in (18), using the 1229
primes below 10000 and \(M=3\), had shifted value
\(-1.5973791639980854\), agreeing with the square-completion formula.
These are finite floating-point normalization checks. The preceding
proofs establish infinite summability, uniqueness, closure, and
unboundedness; neither formal verification nor independent adversarial
approval is claimed.

## References

- [WP-440](WP-440-hamiltonian-diagonal-completion-has-sharp-loglog-threshold.md).
- [WP-148](WP-148-canonical-resultant-graph-laplacian-has-infinite-critical-degree-and-trivial-l2-domain.md).
- [WP-265](WP-265-sharp-and-gibbs-minimal-subtractions-give-opposite-critical-incidence-inertia.md).
- M. Keller, Y. Pinchover, F. Pogorzelski, *Criticality theory for Schrödinger operators on graphs*, Journal of Spectral Theory **10** (2020), 73--114, [DOI: 10.4171/JST/286](https://doi.org/10.4171/JST/286); [author preprint](https://arxiv.org/pdf/1708.09664), Proposition 4.8 and Section 3.
- NIST DLMF, [27.4.12](https://dlmf.nist.gov/27.4.E12), logarithmic derivative of zeta; [25.2.4](https://dlmf.nist.gov/25.2.E4), Laurent expansion at one.
