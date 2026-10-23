---
title: "WP-440: Hamiltonian diagonal completion has a sharp log-log threshold for the all-prime Weil defect"
type: research-finding
status: verified
research_question: "Can a growing Hamiltonian diagonal, outside the ray-compact heat-mixture class, define a closed semibounded completion retaining every finite-prime off-diagonal coefficient?"
claim_strength: exact_diagonal_growth_threshold_relative_form_compactness_and_universal_positive_completion_control
scope: algebraic all-prime defect on c00(N) in the standard positive-energy representation, completed by a specified unbounded Hamiltonian diagonal; no source-selection, archimedean, polar, or global Weil positivity theorem
finding_id: WP-440
related_findings:
  - WP-439
  - WP-438
  - WP-437
  - WP-223
  - WP-218
  - WP-216
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-23
updated: 2026-10-23
tags:
  - weil-positivity
  - bost-connes
  - hamiltonian
  - diagonal-completion
  - closed-quadratic-form
  - schur-test
  - sharp-threshold
---

# WP-440: A noncompact diagonal can complete the defect, at an exact growth cost

## Result and evidence boundary

**EXACT-DERIVED; CLASSICAL SCHUR/FORM METHODS; POSITIVE MATCHED CONTROL.**
The strictly positive heat mixtures of WP-439 remain compact on each
prime ray. A growing diagonal is a different operation and can change
that conclusion. For the full algebraic prime-power defect defined below,
put
\[
 H e_n=(\log n)e_n,\qquad
 D_\eta=(1+H)^2[\log(e+H)]^\eta,\qquad \eta\in\mathbb R.
 \tag{1}
\]
Then the sharp assertion is
\[
 \boxed{\ cD_\eta+W\text{ has a semibounded closed form extension
 from }c_{00}(\mathbb N),\quad c>0,
 \quad\Longleftrightarrow\quad\eta>1.\ }
 \tag{2}
\]
This holds for **every** fixed finite coefficient \(c>0\). For
\(\eta>1\), the extension has form domain \(D(D_\eta^{1/2})\),
finite-support vectors are a form core, and its associated self-adjoint
operator has compact resolvent. For sufficiently large finite \(c\),
no scalar shift is needed: the completed form is nonnegative.
For arbitrary \(c>0\), a finite scalar shift makes it nonnegative.
For \(\eta\le1\), the algebraic form is unbounded below, so neither
a bounded correction nor any extension retaining all its finite tests
can repair semiboundedness.

The theorem retains all off-diagonal prime-power coefficients, including
those between mixed-prime labels. Its positive conclusion uses a
**freely specified unbounded diagonal**, not a source-forced completion.
It supplies no archimedean term, polar subtraction, identification with
the Weil test space, or RH implication. It identifies exactly why
noncompact completion is possible without making positivity explanatory.

## The fixed algebraic object

On \(\mathcal H=\ell^2(\mathbb N)\), with the original orthonormal basis
unchanged, define for finite-support \(f\)
\[
 w[f]=-2\operatorname{Re}
   \sum_{m\ge1}\sum_{d\ge2}
       \frac{\Lambda(d)}{\sqrt d}\,\overline{f_m}f_{md}.
 \tag{3}
\]
Every such sum is finite. Here \(\Lambda(p^k)=\log p\), and
\(\Lambda(d)=0\) otherwise. Thus the Hermitian matrix has zero diagonal
and entry \(-\Lambda(d)/\sqrt d\) between \(m\) and \(md\).
This is precisely the algebraic union of the finite-prime coordinate
sums \(\sum_p(\log p)(I-G_p)\) in WP-223. On the ray \(p^j\),
(3) restricts to WP-216/218's
\[
 W_p(j,k)=\begin{cases}
  -\log p\,p^{-|j-k|/2},&j\ne k,\\0,&j=k.
 \end{cases}
 \tag{4}
\]
No assertion that the bare matrix acts on \(c_{00}\) as an
\(\ell^2\)-valued operator is made: its vacuum column is not square
summable. All completions below are **form** completions.

Write
\[
 L_n=1+\log n,\quad J_n=\log(e+\log n),\quad
 d_\eta(n)=L_n^2J_n^\eta,\qquad
 d_\eta[f]=\sum_n d_\eta(n)|f_n|^2.
 \tag{5}
\]
In particular \(L_1=J_1=d_\eta(1)=1\). Every basis vector has finite
energy, and \(d_\eta(n)\to\infty\) for every fixed real \(\eta\).

## Necessity: the first-prime star already forces \(\eta>1\)

Suppose \(c d_\eta+w\ge -M\|\cdot\|^2\) on \(c_{00}\), taking
\(M\ge0\). Distinct primes have no edge between them in (3). On
\(e_1+\sum_{p\in F}x_pe_p\), put
\[
 b_p=\frac{\log p}{\sqrt p},\qquad
 x_p=\frac{b_p}{c d_\eta(p)+M}.
\]
Completing the independent leaf squares gives the necessary inequality
\[
 0\le c+M-\sum_{p\in F}
             \frac{b_p^2}{c d_\eta(p)+M}
 \quad\text{for every finite prime set }F.
 \tag{6}
\]
As \(p\to\infty\), the summand is asymptotic to
\[
 \frac{1}{c\,p(\log\log p)^\eta}.
 \tag{7}
\]
Mertens' theorem and partial summation show
\[
 \sum_{p\text{ sufficiently large}}
       \frac1{p(\log\log p)^\eta}<\infty
 \quad\Longleftrightarrow\quad\eta>1.
 \tag{8}
\]
For example, in the coordinate \(u=\log\log x\), the reciprocal-prime
counting measure has cumulative mass \(u+O(1)\); integration by parts
reduces convergence to \(\int^\infty u^{-\eta}du\).
For \(\eta\le0\), ordinary reciprocal-prime divergence also suffices.
Thus (6) fails for any \(c>0,M\ge0\) when \(\eta\le1\).
This proves unboundedness below, not merely failure of one norm estimate.
A bounded Hermitian correction cannot alter that conclusion, since its
quadratic value is bounded by a constant times \(\|f\|^2\).

## Sufficiency: a weighted Schur estimate controls every mixed-prime edge

Assume \(\eta>1\). Let \(A=-W\) denote the **entrywise** nonnegative
symmetric matrix from (3); this notation does not claim operator
positivity of \(A\). Define the normalized matrix
\[
 K_\eta(m,n)=\frac{A(m,n)}{\sqrt{d_\eta(m)d_\eta(n)}},
 \qquad h_n=\frac1{\sqrt{nJ_n}},
 \quad \beta=\frac{\eta-1}{2}>0,\quad \tau=\beta+1>1.
 \tag{9}
\]
The Schur weight \(h\) need not belong to \(\ell^2\).
Splitting the \(m\)-th weighted row into multiples and divisors yields
exactly
\[
 \frac1{h_m}\sum_n K_\eta(m,n)h_n
 =\frac1{L_mJ_m^\beta}
 \left[
 \sum_{d\ge2}\frac{\Lambda(d)}{dL_{md}J_{md}^\tau}
 +\sum_{\substack{d\mid m\\d\ge2}}
       \frac{\Lambda(d)}{L_{m/d}J_{m/d}^\tau}
 \right].
 \tag{10}
\]
The critical half-density is essential to this identity: it combines
with \(h_{md}/h_m\) to give \(1/d\) on the upward edges, and cancels
on the downward ones.

The classical estimate \(\psi(x)=\sum_{d\le x}\Lambda(d)=O(x)\)
and partial summation imply
\[
 C_\tau:=\sum_{d\ge2}
       \frac{\Lambda(d)}{dL_dJ_d^\tau}<\infty,
 \tag{11}
\]
since the corresponding integral at infinity is
\(\int dx/[x\log x(\log\log x)^\tau]\).
The numerator of the divisor sum satisfies the exact identity
\(\sum_{d\mid m}\Lambda(d)=\log m\).
Since \(L_{m/d},J_{m/d}\ge1\), while \(L_{md}\ge L_d\) and
\(J_{md}\ge J_d\), (10) gives
\[
 R_m:=\frac1{h_m}\sum_n K_\eta(m,n)h_n
 \le J_m^{-\beta}\left(1+\frac{C_\tau}{L_m}\right)
 \longrightarrow0\quad(m\to\infty).
 \tag{12}
\]
In particular \(\sup_m R_m\le1+C_\tau\).
For finite-support \(u\), the elementary weighted inequality
\[
 2|u_mu_n|\le\frac{h_n}{h_m}|u_m|^2+
                    \frac{h_m}{h_n}|u_n|^2
\]
proves the Schur bound directly. Therefore \(K_\eta\) extends to a
bounded self-adjoint operator, with
\[
 \|K_\eta\|\le1+C_\tau.
 \tag{13}
\]
If \(P_N\) projects onto \(e_1,\ldots,e_N\), the same estimate on
both tail indices gives
\[
 \|(I-P_N)K_\eta(I-P_N)\|\le\sup_{m>N}R_m\longrightarrow0.
 \tag{14}
\]
The difference from this tail has finite rank, because \(K_\eta\)
is bounded. Hence \(K_\eta\) is **compact**.

This is relative form compactness of the signed defect with respect to
an unbounded confining diagonal. It is not compactness of the added
correction to \(W_p\), and does not fall under WP-218/439's obstruction.

## Closed realization, positivity, and compact resolvent

On
\[
 \mathcal Q_\eta=D(D_\eta^{1/2})
 =\{f:\sum_n d_\eta(n)|f_n|^2<\infty\},
\]
define the unique extension continuous in the diagonal form norm by
\[
 w[f]=-\langle D_\eta^{1/2}f,
                   K_\eta D_\eta^{1/2}f\rangle.
 \tag{15}
\]
This agrees with (3) on \(c_{00}\), which is dense in that norm.
Compactness also gives, for every \(\varepsilon>0\),
\[
 |w[f]|\le\varepsilon d_\eta[f]+C_\varepsilon\|f\|^2.
 \tag{16}
\]
Indeed approximate \(K_\eta\) in norm by \(P_NK_\eta P_N\);
the residual contributes \(\varepsilon d_\eta[f]\), while the
finite compression contributes at most
\(\|K_\eta\|\max_{n\le N}d_\eta(n)\|f\|^2\).

For each \(c>0\), choose \(\varepsilon<c\) in (16). The KLMN theorem,
or directly equivalence of the shifted form norms, shows that
\(c d_\eta+w\) is closed and bounded below on \(\mathcal Q_\eta\),
with \(c_{00}\) a form core. Since \(d_\eta(n)\to\infty\), this
form domain embeds compactly into \(\ell^2\); its tail norm is bounded
by \((\inf_{n>N}d_\eta(n))^{-1/2}\) on the diagonal form unit ball.
The equivalent completed form norm therefore gives compact resolvent.

For \(c>1+C_\tau\), (13) gives the explicit positive control
\[
 c d_\eta[f]+w[f]\ge(c-1-C_\tau)d_\eta[f]\ge0.
 \tag{17}
\]
The strict inequality on \(c\) avoids any inference about closedness
at an unexamined norm-bound equality. For smaller \(c>0\), (16)
still supplies a finite scalar shift making the form nonnegative.
No claim of an optimal completion coefficient is made.

As an immediate consequence within the same growth question,
\(c(1+H)^q+W\) is semibounded for \(q>2\), and is unbounded below
for \(0\le q\le2\). For sufficiency use
\(d_\eta(n)=o((1+\log n)^q)\) with any fixed \(\eta>1\) in
(16); necessity follows again from (6). The log-log scale resolves
the critical \(q=2\) boundary rather than hiding it in a strict
power inequality.

## Source and matched-control audit

The diagonal in (1) is positive, time-invariant, finite on the canonical
basis, and unbounded along every prime ray. It charges the vacuum and
therefore lies outside WP-437's vacuum-null class as well. It is an
**additive** correction, not a diagonal congruence or compression of
\(W\); WP-223 explicitly leaves such additions outside its no-go.
No Hilbert metric or critical off-diagonal normalization has changed.

However, neither \(\eta\), \(c\), nor this diagonal functional calculus
has been selected by an independent arithmetic or geometric law. The
same upper bounds and positive completion hold if each edge of \(W\)
is multiplied by an arbitrary complex phase, with conjugate phase on
the reverse edge; they also hold for arbitrary Hermitian edge weights
whose absolute values do not exceed the original ones. The normalized
absolute matrix is dominated in (10)--(14), so even the compactness
and closed-form argument persist. This is a matched **orientation
control**, not a claim that those phase models are global Weil forms.
It proves that the sufficient positivity mechanism cannot distinguish
the required arithmetic orientation from arbitrary edge phases.

The construction therefore evades ray compactness by real confinement,
while remaining a generic stabilizing bath. No finite total trace,
critical Gibbs expectation, canonical diagonal counterterm, or agreement
with the Gamma/polar contribution is asserted. Nor does (2) classify all
possible noncompact corrections or domains. Any global test class that
excludes these algebraic star tests requires a different argument.

## Prior art and validation

The analytic tools are classical: Mertens' reciprocal-prime theorem,
Chebyshev's upper estimate, the Mangoldt divisor identity, the weighted
Schur test, and the KLMN closed-form theorem. Teschl's second edition,
Theorem 6.24 and Lemma 6.26, gives the standard perturbation framework;
(10)--(16) establish its hypotheses here rather than assuming a bare
critical field is a densely defined operator. Mertens' 1874 theorem,
with Villarino's explicit modern reconstruction, supplies (8).

Multiplicative Toeplitz matrices are established objects. Hilberdink's
2017 article and author conference abstract place ratio-indexed
arithmetic matrices in that literature. The present weighted matrix
is a nonmultiplicative logarithmic normalization of a prime-power
adjacency; no tensor-product spectral theorem is imported from that
work. Searches by weighted multiplicative Toeplitz forms, Mangoldt
couplings, and relative form bounds did not identify this precise
threshold. That search is not a historical novelty claim. The durable
line-local delta is the sharp **all-prime, all-prime-power** diagonal
completion criterion, beyond WP-438's finite star and WP-439's
ray-compact thermal class.

A pure-Python finite audit on labels \(1\le n\le1000\) included all
2877 undirected prime-power edges. For \(\eta=1.25,2,4\), the two
expressions in (10) agreed to below \(6\cdot10^{-16}\), and (12)
held with the finite version of \(C_\tau\). Twenty real random vectors
per exponent, coordinates uniform in \([-1,1]\), passed the finite
Schur quadratic bound both for the original edges and independent
random sign controls (Python random seed 440). Direct star evaluations
also verified (6)'s square-completion identity for
\(\eta=-1,0,1\), \(c=1.3\), \(M=0.7\).
These are floating-point normalization checks; no infinite convergence,
endpoint divergence, or proof is inferred from them. The derivations
above establish the quantified conclusions. No formal verification or
independent adversarial approval is claimed.

## References

- research/weil_positivity/findings/WP-439-positive-heat-mixtures-admit-closed-star-completions-but-remain-compact-on-every-prime-ray.md
- research/weil_positivity/findings/WP-438-mixed-prime-vacuum-charge-rank-one-thermal-completion-obstruction.md
- research/weil_positivity/findings/WP-437-prime-ray-heat-restriction-mosco-discontinuity-and-vacuum-null-sign-obstruction.md
- research/weil_positivity/findings/WP-223-state-hamiltonian-diagonal-selection-cannot-make-bost-connes-weil-defect-positive-without-annihilating-it.md
- research/weil_positivity/findings/WP-218-bost-connes-weil-defect-has-negative-essential-spectrum-stable-under-compact-completion.md
- research/weil_positivity/findings/WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md
- F. Mertens, *Ein Beitrag zur analytischen Zahlentheorie*, Journal fuer die reine und angewandte Mathematik **78** (1874), 46--62, [DOI: 10.1515/crll.1874.78.46](https://doi.org/10.1515/crll.1874.78.46).
- M. B. Villarino, *Mertens' Proof of Mertens' Theorem* (2005), [arXiv:math/0504289v3](https://arxiv.org/html/math/0504289v3), Theorems 2--6 and partial summation.
- G. Teschl, *Mathematical Methods in Quantum Mechanics*, second edition, Graduate Studies in Mathematics **157**, AMS (2014), [author's authorized text](https://radon.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), Theorem 6.24 and Lemma 6.26.
- T. Hilberdink, *Matrices with multiplicative entries are tensor products*, Linear Algebra and its Applications **532** (2017), 179--197, [DOI: 10.1016/j.laa.2017.06.037](https://doi.org/10.1016/j.laa.2017.06.037); [author's conference abstract](https://conf.lmno.cnrs.fr/Ja2017/resumpdf/hilberdink.pdf).
