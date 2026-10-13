---
title: "WP-438: Vacuum charging cannot make the rank-one thermal mixed-prime Weil star positive except at a sharp alignment"
type: research-finding
status: verified
research_question: "Can a finite positive vacuum charge complete the first-step Weil vacuum-to-prime couplings together with the mixed-prime Gram supplied by one heat-regularized coanalytic Bost--Connes field?"
claim_strength: exact_rank_one_finite_prime_alignment_classification_sharp_prime_count_and_nonclosable_zero_heat_exception
scope: finite vacuum-plus-first-prime star built from the source-fixed WP-216 Weil first-step couplings, zero additional Weil prime-prime terms, one WP-435 heat-regularized coanalytic Gram and a freely allowed positive vacuum charge; not a theorem for a canonical global Weil completion with extra mixed-prime, archimedean or polar terms
finding_id: WP-438
related_findings:
  - WP-437
  - WP-436
  - WP-435
  - WP-433
  - WP-432
  - WP-218
  - WP-216
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-13
updated: 2026-10-13
tags:
  - weil-positivity
  - bost-connes
  - mixed-prime
  - rank-one
  - thermal-regularization
  - vacuum-charge
  - positive-block-matrix
  - sharp-alignment
  - nonclosability
---

# WP-438: The finite mixed-prime rank-one completion has a sharp alignment obstruction

## Precise claim and evidence

**EXACT-DERIVED; NEGATIVE/OBSTRUCTION; CLASSICAL RANGE-FACTORING LEMMA SPECIALIZED TO THE MATHIA FIELD.**
On the standard positive-energy Bost--Connes representation
\(\mathcal H=\ell^2(\mathbb N)\), take the shifts
\(\mu_p e_n=e_{pn}\) and \(He_n=(\log n)e_n\). For
\(\alpha>0,\ \kappa\ge0,\ t>0\), let
\[
R_\kappa e_m=\sum_{p\mid m}\overline{a_{\kappa,p}}e_{m/p},
\quad a_{\kappa,p}=\frac{(\log p)^\kappa}{\sqrt p},\qquad
B_t=R_\kappa e^{-tH^\alpha}.
\]
WP-435 proves that the heat-regularized \(B_t\) extends to a
bounded compact operator for every \(t>0\).

Fix a nonempty finite set of distinct primes \(F\). On the subspace
\(E_F=\operatorname{span}\{e_1\}\oplus
 \operatorname{span}\{e_p:p\in F\}\), retain precisely the first-step
vacuum-to-prime entries of the WP-216 critical Weil-ray defects,
\[
W_F(e_1,e_p)=W_F(e_p,e_1)
=-b_p,\qquad b_p=\frac{\log p}{\sqrt p},
\]
and put zero on the diagonal and between distinct prime states
**before** the heat correction. This specifies a *finite star test
model*, not a claim that the unknown completed global Weil operator
has no mixed-prime or archimedean entries. Add the genuine compressed
positive heat energy \(P_{E_F}B_t^*B_tP_{E_F}\) and an arbitrary
nonnegative vacuum charge \(\gamma|e_1\rangle\langle e_1|\).
Because \(B_te_1=0\) and
\(B_te_p=\overline{c_{t,p}}e_1\), with
\[
c_{t,p}=\frac{(\log p)^\kappa}{\sqrt p}
        \exp[-t(\log p)^\alpha]>0,
\]
the resulting Hermitian matrix is
\[
M_{F,t,\gamma}
=\begin{pmatrix}\gamma&-b_F^*\\-b_F&c_t c_t^*\end{pmatrix}.
\tag{1}
\]

The **complete finite classification**, for any nonzero \(c_t\),
is
\[
\boxed{M_{F,t,\gamma}\succeq0
\quad\Longleftrightarrow\quad
b_F=\lambda c_t\text{ for some }\lambda\in\mathbb C
\quad\text{and}\quad\gamma\ge|\lambda|^2.}
\tag{2}
\]
For the positive real coefficients just defined this implies:

1. If \(0\le\kappa\le1\) and \(t>0\), every set with **two
   distinct primes** violates (2), however large the finite charge
   \(\gamma\) is.
2. If \(\kappa>1\) and \(t>0\), every set with **three distinct
   primes** violates (2). This prime count is sharp: for any
   \(p<q\), one special \(t>0\) aligns those two coordinates, and
   sufficiently large \(\gamma\) makes their entire \(3\times3\)
   block positive.
3. In the formal \(t=0\) limit, sets of at least two primes align
   **only when \(\kappa=1\)**, where \(c_0=b\) and the finite matrix
   is positive precisely for \(\gamma\ge1\). However the
   all-prime form obtained on the canonical finite-support domain
   is **not closable**, even when \(\gamma\ge1\).

This extends the vacuum-null two-state obstruction of WP-437:
charging the vacuum can repair one local \(2\times2\) block, but
a single coanalytic output channel cannot generally align
simultaneously with the source-fixed Weil couplings across primes.
The conclusion applies only to the specified finite star and one
thermal rank-one Gram, **not** to arbitrary mixed-prime,
finite--archimedean or domain-constrained global Weil forms.

## Exact block proof

For any \(c\ne0\), the quadratic form of
\(\begin{psmallmatrix}\gamma&-b^*\\-b&cc^*\end{psmallmatrix}\)
on \((z,x)\in\mathbb C\oplus\mathbb C^F\) equals
\[
\gamma|z|^2-2\operatorname{Re}(\overline z\,b^*x)
                  +|c^*x|^2.                       \tag{3}
\]
If \(b\notin\operatorname{span}\{c\}\), choose
\(x\in\ker c^*\) with \(b^*x\ne0\). Varying an arbitrarily
small \(z\) with the favorable phase makes (3) negative,
for every finite \(\gamma\ge0\). Thus positivity forces
\(b=\lambda c\). Conversely, under that condition (3) is
\[
|c^*x-\lambda z|^2+(\gamma-|\lambda|^2)|z|^2.
\tag{4}
\]
Taking \(c^*x=\lambda z\), possible because \(c\ne0\),
proves necessity of the charge threshold. Equation (4)
also proves sufficiency. This is the elementary finite-dimensional
rank-one instance of the classical Douglas range/factorization
criterion, not a new general operator theorem.

The coanalytic compression in (1) contains a **genuine
mixed-prime term**:
for \(p,q\in F\), including \(p\ne q\),
\[
\langle B_te_p,B_te_q\rangle
=\overline{c_{t,p}}c_{t,q}
=c_{t,p}c_{t,q}.                                    \tag{5}
\]
All such terms come from the same output vector \(e_1\),
so the whole prime-prime block has rank one.
This feature is stronger than testing each prime ray separately;
yet it is exactly what creates the range-alignment condition.

## Sharp thermal prime-count analysis

Since \(b_p,c_{t,p}>0\), the alignment is equivalent to
constancy over the chosen primes of
\[
\frac{c_{t,p}}{b_p}
=(\log p)^{\kappa-1}e^{-t(\log p)^\alpha}.
\tag{6}
\]
Writing \(x=\log p>0\), take the logarithm
\[
g_t(x)=(\kappa-1)\log x-tx^\alpha,
\qquad
g_t'(x)=\frac{\kappa-1-\alpha t x^\alpha}{x}.
\tag{7}
\]
For \(\kappa\le1\), \(g_t\) is strictly decreasing, so
two different primes cannot share the same ratio. For
\(\kappa>1\), \(g_t\) increases to a unique maximum at
\(x=((\kappa-1)/(\alpha t))^{1/\alpha}\), then decreases.
Every horizontal level consequently has at most two
positive preimages; three distinct primes cannot align.
For a chosen pair \(p<q\), the unique positive alignment time is
\[
\boxed{t_{p,q}=
\frac{(\kappa-1)
       \log\!\bigl((\log q)/(\log p)\bigr)}
     {(\log q)^\alpha-(\log p)^\alpha}>0.}
\tag{8}
\]
At this time \(\lambda=b_p/c_{t,p}=b_q/c_{t,q}\);
choosing \(\gamma\ge\lambda^2\) produces a positive
two-prime star. This exact exceptional construction proves
that the three-prime bound for \(\kappa>1\) cannot be
replaced by a universal two-prime bound.

At \(t=0\), (6) becomes \(x^{\kappa-1}\).
For any \(F\) of size at least two this is constant exactly
when \(\kappa=1\). In that case \(c_0=b\) and (4)
reduces to
\[
Q_{\gamma,F}(z,x)
=|b_F^*x-z|^2+(\gamma-1)|z|^2,
\tag{9}
\]
which is nonnegative exactly for \(\gamma\ge1\).
For fixed finite \(F\), the matrices in (1) depend
continuously on \(t\), even though the all-prime
critical operator has no well-behaved zero-heat extension.

## The aligned critical limit is not a closed Hilbert energy

On the canonical dense algebraic subspace
\[
D=\operatorname{span}\{e_1\}\oplus
       c_{00}(\mathbb P)
\subset \mathbb C e_1\oplus\ell^2(\mathbb P),
\]
put \(S(x)=\sum_p b_px_p\), a finite sum on \(D\).
At \(t=0,\ \kappa=1\), the formal all-prime form is
\[
Q_\gamma(z,x)=|S(x)-z|^2+(\gamma-1)|z|^2,\qquad\gamma\ge1.
\tag{10}
\]
It is nonnegative on \(D\), but it is not closable.
Indeed, \(\sum_p b_p^2=\sum_p(\log p)^2/p=\infty\)
(by the divergence of \(\sum_p 1/p\)).
For expanding finite prime sets \(F_n\), let
\[
A_n=\sum_{p\in F_n}b_p^2\to\infty,\qquad
x_n=A_n^{-1}\sum_{p\in F_n}b_p e_p.
\tag{11}
\]
Then \(\|x_n\|_2^2=A_n^{-1}\to0\) but
\(S(x_n)=1\). The vectors \(u_n=(0,x_n)\)
satisfy
\[
u_n\to0,\qquad Q_\gamma(u_n-u_m)=0,\qquad
Q_\gamma(u_n)=1.                                    \tag{12}
\]
This contradicts the defining closability criterion for
nonnegative quadratic forms. Therefore finite-panel
positivity at the unique aligned endpoint does not yield
a closed positive all-prime Hilbert form.

## Audits, prior art and mathematical boundary

The ratio proof checks **all** \(\alpha>0\), \(\kappa\ge0\),
and finite \(\gamma\ge0\), without assuming monotonicity
of the full prime-field operator family. Its exceptional
two-prime case was checked directly using (8);
its zero-heat claim is only finite-panel algebra until
the closability test (11)--(12) is imposed.
The full \(W_p\) has nonzero couplings along higher
prime powers and negative essential Toeplitz spectrum
(WP-216/218); those channels make positivity harder,
not easier, but this result does **not** identify the
star model with their globally assembled Weil operator.

The range constraint and square completion are classical
finite-dimensional operator theory (Douglas, 1966).
The singular critical-form obstruction is likewise
standard nonclosable-form theory; the closest
general framework is Hassi--Sebestyén--de Snoo (2009),
already recorded in SOURCES.md.
The Mathia-local contribution is their *sharp application*
to the actual \(B_te_p\) outputs and prescribed
\(-(\log p)/\sqrt p\) Weil first-step couplings.
No broad novelty or RH implication is claimed.

The same proof works for a matched nonarithmetic
free-generator semigroup with distinct positive log-weights:
hence the rank-one failure is not by itself
arithmetic-selective. It excludes neither several
independently selected coherent output channels,
nor nonadditive cancellation before Gram formation,
nor an independently source-forced global mixed-prime
term, altered test domain, archimedean Gamma contribution,
or polar normalization. A successful global Weil form
must supply these extra structures and establish its sign
*before* being identified with the arithmetic target.

## References

- research/weil_positivity/findings/WP-437-prime-ray-heat-restriction-mosco-discontinuity-and-vacuum-null-sign-obstruction.md
- research/weil_positivity/findings/WP-435-fractional-heat-prime-field-schatten-phase-transition.md
- research/weil_positivity/findings/WP-432-coanalytic-prime-field-is-dense-but-nonclosable-at-critical-half-density.md
- research/weil_positivity/findings/WP-218-bost-connes-weil-defect-has-negative-essential-spectrum-stable-under-compact-completion.md
- research/weil_positivity/findings/WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md
- research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md
- research/weil_positivity/SOURCES.md
