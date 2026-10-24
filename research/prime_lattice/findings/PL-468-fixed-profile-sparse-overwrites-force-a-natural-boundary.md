# PL-468 — Fixed-profile sparse overwrites force a natural boundary

**Evidence/status:** EXACT-DERIVED + CLASSICAL LACUNARY-SERIES INPUT;
RESTRICTED COUNTERMODEL OBSTRUCTION; NO EXTERNAL NOVELTY CLAIM.

## Claim and scope

The sparse-block overwrite suggested by the local
[[research/prime_lattice/clues/CLUE-density-one-dyadic-variance-arithmetic-recovery|density-one variance clue]]
has a concrete analytic obstruction. Fix
\(0<\theta<1\), \(1-\theta/2<\beta<1\), \(c>0\), and a nonzero
nonnegative \(\phi\in C_c^1((1,3/2))\). Put
\[
 N_k=2^{3^k},\qquad
 G=\mathbb N_{\ge1}\setminus\{3^k-1,3^k:k\ge2\}.
\]
For sufficiently large fixed \(k_0\ge2\), define one coefficient source
\[
 b_n=\begin{cases}
 0,&5\mid n,\\
 \displaystyle\frac54-5c\sum_{k\ge k_0}
 N_k^{\beta-1}\phi(n/N_k),&n\equiv1\pmod5,\\
 \frac54,&n\equiv2,3,4\pmod5.
 \end{cases}
 \tag{1}
\]
The supports in the sum are disjoint. This source is bounded and
nonnegative, and each nonzero residue has leading mass \(x/4+o(x)\).
At every retained dyadic block \(X=2^j\), \(j\in G\), its complete
empirical window variance satisfies, for every integer \(1\le H\le X\),
\[
 P_1(y;H)=\sum_{\substack{y<n\le y+H\\n\equiv1(5)}}b_n,
 \quad \overline P_1=X^{-1}\int_X^{2X}P_1(y;H)\,dy,
 \quad
 \int_X^{2X}|P_1-\overline P_1|^2dy\le\frac{25}{16}X.
 \tag{2}
\]
Nevertheless the identity-residue Dirichlet series, and each of its
four character transforms, has \(\Re s=\beta\) as a natural boundary,
including for **meromorphic** continuation. It cannot satisfy the
clue's meromorphic sparse-pole hypotheses.

This statement rules out the entire recipe (1), for any such fixed
nonzero profile and parameters. It does **not** rule out all possible
scale-dependent overwrites or prove the clue's actual-prime implication.
The source passes the retained variance, positivity, integer support,
residue bookkeeping and leading-mass tests; it fails analytic
continuation before any pole-count or residue-sign test is available.

## 1. Positivity, counting and invisible retained windows

Choose \(k_0\) so that
\(5cN_{k_0}^{\beta-1}\|\phi\|_\infty\le5/8\).
Then \(5/8\le b_n\le5/4\) on integers coprime to 5. Each complete
overwrite has total absolute mass \(O(N_k^\beta)\). Since
\(N_{k+1}=N_k^3\), summing earlier overwrites and, when present, the
current partial overwrite gives
\[
 \sum_{\substack{n\le x\\n\equiv a(5)}}b_n
 =x/4+O_{\beta,c,\phi}(1+x^\beta),\qquad a\in\{1,2,3,4\}.
 \tag{3}
\]
For the unchanged residues the error is just \(O(1)\).

Fix an overwrite scale \(N_k=2^{3^k}\) and a retained \(j\).
If \(j\le3^k-2\), then \(3X\le3N_k/4<N_k\). If
\(j\ge3^k+1\), then \(X\ge2N_k>3N_k/2\). These exhaust the
retained possibilities. Hence every window with \(X\le y\le2X\)
and \(H\le X\) misses every overwrite: its entire support lies in
\((X,3X]\). On such a window
\[
 P_1(y;H)=\frac54\#\{n\equiv1\pmod5:y<n\le y+H\},
 \qquad |P_1(y;H)-H/4|\le5/4.
\]
The empirical mean minimizes the integral of squared distance to a
constant. Comparing it with \(H/4\) proves (2). In particular (2)
implies the clue's \(O(XH(\log X)^A)\) ceiling for every fixed
\(A\ge0\), with no exceptional starting points or window lengths.

## 2. Integer sampling preserves the lacunary Mellin term

Write
\[
 A_1(s)=\sum_{n\equiv1(5)}n^{-s}=5^{-s}\zeta(s,1/5),
 \qquad
 \Phi(s)=\int_1^{3/2}\phi(u)u^{-s}\,du.
\]
The function \(\Phi\) is entire and is positive on the real axis.
The classical Hurwitz continuation makes \(A_1\) meromorphic with
only a simple pole at 1, of residue \(1/5\) (source 130).

For each compact \(K\subset\mathbb C\), progression quadrature gives
\[
 \sum_{n\equiv1(5)}\phi(n/N)n^{-s}
 =\frac15N^{1-s}\Phi(s)+e_N(s),
 \qquad |e_N(s)|\ll_K N^{-\Re s}.
 \tag{4}
\]
To check the uniform error, apply the bounded-discrepancy counting
measure for the progression to
\(f(x)=\phi(x/N)x^{-s}\). Its compact support and vanishing endpoints
leave an error bounded by a constant times
\(\int|f'(x)|dx=O_K(N^{-\Re s})\). Each \(e_N\) is entire.
This estimate includes the atomic discretization; a continuous-density
calculation alone would not suffice.

Let
\[
 \mathcal D_1^{\rm res}(s)=\sum_{n\equiv1(5)}b_nn^{-s},
 \qquad h(z)=\sum_{k\ge k_0}z^{3^k}.
\]
Initially for \(\Re s>1\), substitution of (4) into (1) gives
\[
 \boxed{
 \mathcal D_1^{\rm res}(s)
 =\frac54 A_1(s)-c\Phi(s)h(2^{\beta-s})+E(s),
 \qquad E\text{ holomorphic on }\Re s>\beta-1.
 }
 \tag{5}
\]
Indeed \(E=-5c\sum_{k\ge k_0}N_k^{\beta-1}e_{N_k}\), whose terms
are \(O_K(N_k^{\beta-1-\Re s})\); they converge normally on that
half-plane. Formula (5) therefore continues the original series to
\(\Re s>\beta\), with its expected pole at 1. Its singular boundary
at \(\beta\) cannot be blamed on quadrature error.

For a character \(\chi\bmod5\), define
\(\mathcal D_\chi(s)=\sum_n b_n\chi(n)n^{-s}\).
Every modified integer has \(\chi(n)=\chi(1)=1\), so the same argument
gives
\[
 \mathcal D_\chi(s)=\frac54L(s,\chi)
       -c\Phi(s)h(2^{\beta-s})+E(s).
 \tag{6}
\]
The unmodified term is meromorphic, as is also seen by its finite
Hurwitz progression decomposition. The exact identity
\(\mathcal D_1^{\rm res}=\frac14\sum_\chi\mathcal D_\chi\) is preserved.
These transforms are not asserted to be genuine Dirichlet
logarithmic derivatives.

## 3. A dense set of nonmeromorphic boundary singularities

The exponents \(3^k\) satisfy the classical Hadamard gap condition;
the Fabry formulation in source 132 also applies. For this particular
series there is a direct proof, including the meromorphic assertion.

Let \(\zeta\) be any root of unity of order a power of three. All
sufficiently late terms of \(h(r\zeta)\), \(0<r<1\), equal
\(r^{3^k}\). With \(t=-\log r\), the number of indices with
\(t3^k\le1\) is \(\log(1/t)/\log3+O(1)\), each contributing at
least \(e^{-1}\). The remaining sum is bounded by a constant, since
its terms are bounded by \(e^{-3^\ell}\) after an index shift.
Consequently
\[
 \Re h(r\zeta)\longrightarrow+\infty,
 \qquad |h(r\zeta)|=O\!\left(1+\log\frac1{1-r}\right).
 \tag{7}
\]
Finite initial terms do not change these conclusions. Holomorphic
extension at \(\zeta\) would imply bounded radial values. A pole of
positive integer order would instead have power-law radial growth,
contradicting (7). There is thus no meromorphic extension at any of
these roots. They are dense on the unit circle, so there is no
meromorphic extension through **any** point of that circle.

The map \(s\mapsto2^{\beta-s}\) is locally biholomorphic and maps
\(\Re s=\beta\) onto the unit circle. Equations (5)--(6) now prove
the claimed natural boundary wherever \(\Phi(s)\ne0\). Zeros of
\(\Phi\) cannot open a continuation corridor: they are isolated,
and any neighborhood of such a zero contains boundary points at
which \(\Phi\ne0\). A meromorphic extension through that neighborhood
would contradict the already established obstruction at those points.
Adding the holomorphic error or the baseline Hurwitz terms cannot
remove it either, since \(\beta<1\).

## 4. The omitted blocks carry genuinely excessive variance

This source does not accidentally satisfy the every-block hypothesis
of PL-466. Take \(X=N_k\), \(H=\lfloor X^\theta\rfloor\).
Let \(V_k=\int_X^{2X}|P_1(y;H)-\overline P_1|^2dy\), with the
empirical mean taken over this same block.
Progression quadrature for the short window, and the bounded derivative
of the zero-extended \(\phi\), give uniformly for \(1\le u\le2\),
\[
 P_1(Xu;H)=H/4-cHX^{\beta-1}\phi(u)
             +O(1+H^2X^{\beta-2}).
 \tag{8}
\]
Other overwrite blocks are outside these windows. Since
\(\theta>2(1-\beta)>1-\beta\), division of the error by
\(HX^{\beta-1}\) tends to zero. Subtracting the empirical mean in
(8) and integrating proves
\[
 \frac{V_k}{H^2X^{2\beta-1}}
 \longrightarrow c^2\left\{\int_1^2\phi(u)^2du
                    -\left(\int_1^2\phi(u)du\right)^2\right\}>0.
 \tag{9}
\]
The last strict inequality follows because the nonzero profile vanishes
on an interval of positive length, so it is not constant on \([1,2]\).
Thus \(V_k/(XH(\log X)^A)\to\infty\) for every finite fixed
\(A\ge0\), by \(\theta+2\beta-2>0\).

## Prior art, audit and remaining implication

Lacunary natural boundaries are classical, not a new arithmetic
mechanism. Bell--Lagarias, Section 2.1 (source 132), gives the standard
gap theorem; Costin--Huang (source 133) studies boundary behavior of
lacunary exponential series. The Hurwitz continuation in source 130
and bounded-discrepancy progression quadrature are classical as well.
The elementary argument (7) establishes the exact special case used
here without an unverified extension of a gap theorem to variable
analytic coefficients.

The local contribution is the joint atomic realization and obstruction:
the same fixed source has positive coefficients, correct residue masses,
uniformly tiny retained-block variance, large omitted-block variance,
and an unavoidable natural boundary at the prescribed supercritical
abscissa. This makes explicit why replacing the generic sparse overwrite
in the authorized MC-523 comparison by a fixed smooth density bump
cannot deliver the meromorphic countermodel requested in the clue.
It is not a theorem about MC-523's own random-sign transform, and does
not strengthen or refute that finding.

Exact rational checks of an example profile
\(4096(u-9/8)^2(11/8-u)^2\) on \([9/8,11/8]\), zero elsewhere,
give \(\int\phi=2/15\) and centered variance \(44/525\); the endpoints
and first derivatives vanish. Finite exact checks also verified the
retained-window support inequalities. These are auxiliary algebra and
geometry checks; (3)--(9) supply the infinite-scale proof. No numerical
singularity plot, formal proof, or independent adversarial approval is
claimed.

The actual-prime density-one recovery question remains open here.
For the general omitted-block term in PL-466's decomposition, the
profiles \(R_j(s)\) depend on \(s\) and need not factor as a common
\(\Phi(s)\) times scalar coefficients. Its density-zero index support
is therefore **not** a license to apply the scalar gap theorem above.
A countermodel must evade this fixed-profile obstruction while retaining
meromorphic continuation and the stipulated sparse real-residue pole
structure; a positive proof must control that genuinely variable-profile
remainder from actual arithmetic input. Neither obligation is settled.
No RH/GRH claim or external novelty claim follows.
