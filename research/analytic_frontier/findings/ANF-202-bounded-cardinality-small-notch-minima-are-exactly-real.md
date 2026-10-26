# ANF-202 — Bounded-cardinality small-notch minima are exactly real

**Status:** EXACT-DERIVED + FIXED-CARDINALITY + PROFILE-UNIFORM-LOCAL-AMPLITUDE + STRICT-VERTICAL-COST + EXACT-REAL-REDUCTION. For every fixed cardinality cap, a common positive amplitude interval makes the complex and real Montgomery--Taylor notch minima identical, uniformly over all dominated even notch profiles. Near equality, real-part collapse preserves the affine denominator and strictly decreases the perturbed energy of every nonreal configuration. For the positive-Fourier inverse-square-tail profiles of ANF-200, an actual real two-site configuration therefore attains the complex capped minimum throughout an initial amplitude interval. No interval uniform in cardinality, unrestricted complex certificate, or zeta-zero improvement is established.

## Statement

Use the Fourier convention \(\widehat f(x)=\int f(u)e^{-2\pi iux}\,du\) and
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad
J_0=g*g,\qquad K=\widehat g,\qquad F=\widehat J_0=K^2.
\tag{1}
\]
Here \(g>0\) on its support, \(\int g=\int J_0=1\), and the
positive zeros \(r_j\) of \(K\) are the simple roots from ANF-087.
For a nonempty finite conjugation-invariant multiset \(W\), count
every entry with its positive integer multiplicity and put
\[
N=|W|,\quad L(W)=2N-\sigma(W),\quad
S_W(u)=\sum_{z\in W}e^{-2\pi iuz},\quad
E_f(W)=\int f(u)|S_W(u)|^2\,du,
\]
\[
e(W)=E_{J_0}(W)/L(W)-1\ge0,\qquad
H(W)=\max_{z\in W}|\Im z|.
\tag{2}
\]
The count \(\sigma\) includes distinct **simple real** sites only.
Let \(V=\Re W\) denote the multiset obtained by replacing every
entry by its real part, retaining all repetitions.

For every fixed integer \(m\ge2\), there is \(t_m>0\) such that,
simultaneously for every integrable real even profile \(0\le\phi\le J_0\),
\[
\boxed{
\inf_{\substack{W=\overline W\\1\le |W|\le m}}
\frac{E_{J_0-t\phi}(W)}{L(W)}
=
\inf_{\substack{V\subset\mathbb R\\1\le |V|\le m}}
\frac{E_{J_0-t\phi}(V)}{L(V)}
\qquad(0\le t\le t_m).
}
\tag{3}
\]
Every attaining configuration on the left is real. No Fourier-sign,
Fourier-tail, or Sobolev assumption on \(\phi\) is needed for (3).
The cap is on total multiplicity, not the number of distinct sites.

The load-bearing local assertion is stronger than the limiting
exposure identity of ANF-201. There are \(\varepsilon_m>0\), an
absolute \(d>0\) depending only on (1), and \(B_m<\infty\) such that
\(N\le m\) and \(e(W)\le\varepsilon_m\) imply the following.
Every nonreal orbit is a simple pair \(x_j\pm iy_j\), \(y_j>0\),
whose center is distinct from every other orbit center and real site;
\(L(V)=L(W)\); and, with \(Q=\sum_jy_j^2\),
\[
\boxed{
E_{J_0}(W)-E_{J_0}(V)\ge dQ,\qquad
|E_\phi(W)-E_\phi(V)|\le B_mQ.
}
\tag{4}
\]
The second estimate is uniform over \(0\le\phi\le J_0\). In particular,
\[
H(W)^2\le Q\le\frac{L(W)e(W)}d\le\frac{2m}d e(W).
\tag{5}
\]
Thus maximum-height collapse has a square-root rate at each fixed cap,
although the admissible excess threshold is not uniform in \(m\).

## A strict curvature gap at every source zero

Write
\[
A=-F''(0)=8\pi^2\int u^2g(u)\,du>0.
\]
At a real zero \(r\) of \(K\),
\[
F''(r)=2K'(r)^2,
\qquad K'(r)=-2\pi\int ug(u)\sin(2\pi ru)\,du.
\]
Cauchy--Schwarz gives
\[
F''(r)\le A\int g(u)\sin^2(2\pi ru)\,du<A.
\tag{6}
\]
Strictness follows from \(g>0\) on an interval and
\(\int g=1\): the sine square cannot equal one almost everywhere.
Moreover \(K'(x)\to0\) as \(|x|\to\infty\), by the
Riemann--Lebesgue lemma applied to \(ug(u)\). Since the source zeros
are discrete and tend to infinity, the strict gap is uniform over them:
\[
d:=A-\sup_{j\ge1}F''(r_j)>0.
\tag{7}
\]
This is a source-specific curvature margin, not an asserted convexity
of \(F\) on the real line.

Consider an equality configuration of ANF-087 containing a double
site at \(x\). There is at most one other site; its multiplicity
\(b\) is one or two and its separation is a source zero. Therefore
\[
\sum_{v\in V}F''(x-v)
=2F''(0)+bF''(r_j)\le-2d.
\tag{8}
\]
For a single double site the sum is \(-2A\le-2d\). The factor two
at the distinguished site is essential: a collapsing nonreal pair
creates a double site, never a simple one.

## Transfer the gap to all sufficiently small excess at a fixed cap

ANF-201 supplies the precise compactness input. Every sequence with
\(|W_n|\le m\) and \(e(W_n)\to0\) has a subsequence splitting into
finitely many horizontally separating clusters. After a separate real
translation, each cluster converges to an ANF-087 equality multiset;
all heights tend to zero; and its limiting denominator equals its
prelimit denominator. This conclusion includes multiplicity collisions.

These facts imply that, for sufficiently small excess, each nonreal
orbit has multiplicity one and no projected center coincides with
another orbit center or a real site. Otherwise choose a sequence of
violations with excess tending to zero and apply that compactness
statement. A repeated nonreal orbit would give at least four entries
at one limit site. A center collision with another orbit or a real
site would give at least three. Both contradict the equality
multiplicity bound of two. Replacing each simple nonreal pair by its
double real center consequently preserves \(L\) exactly.

For each such pair center define, using the entire flattened multiset,
\[
P_j(V):=\sum_{v\in V}F''(x_j-v).
\]
Uniformly over all sufficiently small-excess configurations at this cap,
\[
P_j(V)\le-d\quad\hbox{for every nonreal pair center }x_j.
\tag{9}
\]
To prove this uniform assertion, a contrary sequence has a selected
violating orbit; the finite label set permits passage to a fixed one.
Its limit site has multiplicity exactly two. Its own cluster's
potential converges to (8). Every other cluster contributes zero in
the limit, because
\(F''(x)=-4\pi^2\widehat{u^2J_0}(x)\to0\) at horizontal infinity
and there are at most \(m\) summands. This contradicts failure of (9).

This argument does not assume global compactness modulo one translation,
separation of the original sites, or continuity of \(L\) through an
arbitrary collision. It uses exactly the collision-safe cluster result
of ANF-201. Shrinking the excess threshold further makes \(H\) as
small as required below.

## Uniform expansion in the actual conjugate heights

For \(|u|\le1\) and \(H\le1\), the source difference is
\[
D(u):=S_W(u)-S_V(u)
=2\sum_j e^{-2\pi iux_j}\{\cosh(2\pi uy_j)-1\}
=4\pi^2u^2\sum_j y_j^2e^{-2\pi iux_j}+R(u).
\tag{10}
\]
Taylor's theorem and \(|S_V|\le m\) give
\[
|D(u)|\le C_2Q,\qquad |R(u)|\le C_4H^2Q,
\]
\[
C_2=4\pi^2\cosh(2\pi),\qquad
C_4=\frac{(2\pi)^4\cosh(2\pi)}{12}.
\tag{11}
\]
Expanding the energy, the leading cross term has the exact sign
\[
2\Re\int J_0\overline{S_V}
\left(4\pi^2u^2\sum_j y_j^2e^{-2\pi iux_j}\right)du
=-2\sum_j y_j^2P_j(V).
\tag{12}
\]
The remaining square \(\int J_0|D|^2\) is nonnegative. Therefore
(9)--(12), \(\int J_0=1\), and
\(2mC_4H^2\le d\) imply
\[
E_{J_0}(W)-E_{J_0}(V)
\ge2dQ-2mC_4H^2Q\ge dQ.
\tag{13}
\]
The required height restriction holds after decreasing
\(\varepsilon_m\), by ANF-201's uniform fixed-cap height collapse.
No rate from that finding is assumed to prove this step.

For every dominated notch, \(\int\phi\le1\), so
\[
|E_\phi(W)-E_\phi(V)|
\le2mC_2Q+C_2^2Q^2
\le B_mQ,\qquad
B_m=2mC_2+\frac m2C_2^2.
\tag{14}
\]
Here the number of nonreal orbits is at most \(m/2\), and hence
\(Q\le m/2\) when \(H\le1\). This proves (4).
Lamzouri's inequality on the real multiset \(V\), together with
\(L(V)=L(W)\), then proves (5).

## From local collapse to the exact global capped minimum

Take
\[
0<t_m\le\min\left\{\frac12,\frac{d}{2B_m},
\frac{\varepsilon_m}{2(1+\varepsilon_m)}\right\}.
\tag{15}
\]
For \(e(W)\le\varepsilon_m\), (4) yields
\[
E_{J_0-t\phi}(W)-E_{J_0-t\phi}(V)
\ge(d-tB_m)Q\ge\frac d2Q.
\tag{16}
\]
The denominators agree, and the inequality is strict whenever
\(W\) is nonreal. For \(e(W)>\varepsilon_m\), domination instead gives
\[
\frac{E_{J_0-t\phi}(W)}{L(W)}
\ge(1-t)(1+e(W))>1+\frac{\varepsilon_m}{2}>1.
\tag{17}
\]
A simple real singleton has value
\(1-t\widehat\phi(0)\le1\). Thus no configuration in (17) can
attain or lower the real infimum. Every remaining complex configuration
has the real competitor (16) with the same cardinality and denominator.
The reverse infimum inequality follows by inclusion, proving (3)
and the assertion about all attaining configurations. At \(t=0\)
these assertions follow also directly from ANF-087.

For \(m=1\), conjugation invariance already forces a real singleton,
so the conclusion is immediate without the constants above.

## Exact two-site minimum for the regular positive-Fourier profiles

Now additionally assume the ANF-200 profile conditions:
\[
\Phi=\widehat\phi\ge0,\qquad
\sup_x(1+x^2)\Phi(x)<\infty,\qquad
M=\max_j\Phi(r_j)>0.
\tag{18}
\]
ANF-200 proves that the unrestricted finite-real minimum is attained
by a simple pair for \(0<t\le t_\phi\). The same pair belongs to
every capped real class with \(m\ge2\). Combining that theorem with
(3) therefore gives
\[
\boxed{
\inf_{\substack{W=\overline W\\1\le|W|\le m}}
\frac{E_{J_0-t\phi}(W)}{L(W)}
=1-t\Phi(0)+\min_{x>0}\{F(x)-t\Phi(x)\}
\quad(0<t\le\min(t_m,t_\phi)).
}
\tag{19}
\]
This is an attained identity, not just a first-order envelope. In
particular the sharp expansion from ANF-200 transfers unchanged:
\[
q_{m,\phi}^{\mathbb C}(t)=1-(\Phi(0)+M)t-\kappa t^2+O_\phi(t^3),
\quad
\kappa=\max_{\substack{r>0:K(r)=0\\\Phi(r)=M}}
\frac{\Phi'(r)^2}{4K'(r)^2}.
\tag{20}
\]
When \(\kappa=0\), ANF-200 gives an exactly affine floor near zero.
The elementary real pair deformation already accounts for all
small-amplitude gain at any prescribed finite cardinality.

## Prior art, falsification checks and boundary

The source inequality is classical input from
[Lamzouri, Proposition 2.1, v2](https://arxiv.org/html/2609.02882v2#S2).
The explicit source extremizer is recorded in
[Carneiro--Chandee--Littmann--Milinovich, Corollary 14](https://arxiv.org/pdf/1406.5462).
No RH-conditional zero statistic is imported. ANF-087 supplies its
equality classification; ANF-201 supplies the height confinement,
horizontal cluster extraction and denominator bookkeeping; ANF-200
supplies only the final real two-site minimization in (19)--(20).
These are existing SOURCES anchors.

Strict Cauchy--Schwarz, Fourier decay, Taylor expansion, and persistence
of a positive transverse quadratic cost under a smaller perturbation
are classical mechanisms. The local mathematical delta is (7)--(16):
the equality clusters give a uniform negative real curvature potential
at every possible collapsed pair center, and the actual conjugate
source expansion turns that into a positive height cost, with a notch
cost uniform over the whole domination interval. ANF-201 establishes
only a limiting exposure equality and does not imply exact equality
of positive-amplitude minima without this extra curvature argument.
Targeted searches on Montgomery--Taylor/Lamzouri stability, complex
perturbations and positive-type pair-potential ground states did not
identify (3) or (19). This is a derived specialization, not a claim
of a new general perturbation theorem or an exhaustive novelty audit.

Decisive audit points are the strict **uniform** root gap in (7),
the double-site multiplicity in (8), the preservation of \(L\),
the sign and factor in (12), and the two different uses of smallness:
small excess allows collapse, while small amplitude excludes all
remaining configurations by (17). A collapsing pair plus an existing
real site would change the multiplicity and denominator; the cluster
argument explicitly excludes this case before (4). Arbitrary real
collapse is not claimed to decrease source energy. Known higher-order
collapse reversals away from near equality are compatible with (17).
No numerical experiment, validated numerical amplitude or Lean proof
is used here.

The common \(t_m\) is independent of the dominated profile, but the
cardinality cap is fixed before the excess and amplitude limits.
The proof does not bound \(\varepsilon_m\) as \(m\to\infty\).
The extra real two-site interval \(t_\phi\) in (19) can also shrink
with profile variation, as permitted by ANF-198 and ANF-200. Nothing
here allows either limit to be interchanged. In particular (3) does
not combine with ANF-106's finite-resolution boxes to close the
unrestricted envelope: their cardinality bound grows when the
localization error tends to zero. The accepted ANF-099 notch-exposure
question remains open, and no all-configuration zero-counting
certificate or RH conclusion follows.
