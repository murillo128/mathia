# FD-350 — Rational probe plateaus have a sharp spatial sampling cost

**Status:** EXACT-DERIVED + SHARP-RELAXATION-OBSTRUCTION.

The genuine Farey half-arc function is locally constant at every
eligible rational probe. Even retaining its **entire actual partition
into constant intervals** does not justify the proposed spatial-to-probe
transfer: the sharp positive sampling constant on that partition is
asymptotic to \(Qt/2\), not of order \(t^2\).

The probe-containing intervals have total length asymptotic to
\(6t/(\pi^2Q)\). Their indicator has spatial integral \(O(1/t)\) in the
small-product range but takes value one at \(\Theta(t^2)\) probes.
This refutes transfer based only on the genuine partition, boundedness,
symmetry and small spatial mass. It does **not** refute the transfer for
the actual triangular function of the integer rank defect: the control
does not preserve equal values on distinct intervals with equal defect.
That arithmetic linkage remains essential.

## 1. Exact interval and sampling theorem

Let \(Q,t\) be integers with \(t\ge2\) and \(Q>3t\), and put
\(m=\lfloor t/2\rfloor\). Use the cyclic Farey set \(F_Q\subset\mathbb R/\mathbb Z\),
including zero and excluding one, with \(N_Q=|F_Q|\). Define
\[
D_Q(u)=\#(F_Q\cap(u,u+1/2])-N_Q/2,\qquad
\tau(u)=u+1/2\pmod1,
\]
\[
E_t=\{u:q(u)\le t,\ q(\tau u)\le t\}.
\]
Here \(q(u)\) is the reduced denominator, with \(q(0)=1\).
Let \(\mathcal B_Q\) be the set of nonzero jumps of \(D_Q\), after
cancelling simultaneous entrance and exit events. For \(u\in E_t\),
let \(J_Q(u)\) be the connected component of
\((\mathbb R/\mathbb Z)\setminus\mathcal B_Q\) containing \(u\).
It is the maximal open interval of local constancy containing that probe.
Set
\[
s(u)=\max(q(u),q(\tau u)).
\]
The probe is not a jump, the intervals \(J_Q(u)\) are pairwise disjoint,
and their left and right radii \(\ell_-(u),\ell_+(u)\) satisfy
\[
\boxed{\frac1{s(u)Q}\le\ell_\pm(u)
 \le\frac1{s(u)(Q-s(u))}.}\tag{1}
\]

Write \(U_{Q,t}=\bigcup_{u\in E_t}J_Q(u)\), and
\[
A(m)=\sum_{d\le m}\frac{\varphi(d)}d,\qquad
N_m=\sum_{d\le m}\varphi(d).
\]
Then
\[
|E_t|=2N_m,\qquad
\boxed{\frac{2A(m)}Q\le |U_{Q,t}|
 \le\frac{2A(m)}{Q-2m}.}\tag{2}
\]
In particular, if \(t\to\infty\) and \(t=o(Q)\),
\[
|U_{Q,t}|=\frac{12m}{\pi^2Q}
 \left(1+O\left(\frac{\log(2m)}m+\frac tQ\right)\right)
 \sim\frac{6t}{\pi^2Q}.\tag{3}
\]
Lengths and integrals are with respect to normalized Lebesgue measure.

Let \(\mathcal A_Q\) consist of nonnegative functions constant on each
component of the complement of \(\mathcal B_Q\); values at jump points
are irrelevant. The best constant in
\[
\sum_{u\in E_t}f(u)\le B_{Q,t}\int_0^1 f(v)\,dv
\qquad(f\in\mathcal A_Q)
\]
is exactly
\[
\boxed{
B_{Q,t}=\max_{u\in E_t}|J_Q(u)|^{-1},\qquad
m(Q-2m)\le B_{Q,t}\le mQ.}\tag{4}
\]
Thus \(B_{Q,t}\sim Qt/2\) in the same growing regime. This is an
optimal bound for a specified relaxation, not an optimal estimate for
functions of \(D_Q\) alone.

## 2. Why the full plateaus have these widths

For any reduced \(v=a/d\), its two inverse images under doubling are
\(v/2\) and \((v+1)/2\). If \(d\) is odd their reduced denominators
are \(d,2d\); if \(d\) is even both denominators are \(2d\).
Consequently
\[
E_t=\{v/2,(v+1)/2:v\in F_m\},\qquad s(u)=2q(2u).\tag{5}
\]
This also proves the cardinality in (2).

At a point \(x\), the jump of the right-continuous function is
\[
D_Q(x)-D_Q(x-)
=\mathbf1_{F_Q}(x+1/2)-\mathbf1_{F_Q}(x).\tag{6}
\]
Both indicators equal one at every probe, so its jump cancels.
Every possible nonzero jump is a Farey point or the half translate of
one. Rational separation, applied respectively to \(u\) or \(\tau u\),
places every such point at circular distance at least \(1/(s(u)Q)\).
This proves the lower bound in (1).

For the upper bound, choose whichever of \(u,\tau u\) has denominator
\(s=s(u)\). This denominator is even. Its two immediate order-\(Q\)
Farey neighbors have denominators \(b_-,b_+\) with
\[
Q-s<b_\pm\le Q,\qquad (b_\pm,s)=1,
\]
and their distances from the vertex are \(1/(sb_\pm)\).
These are the classical determinant-one and denominator-sum properties
of consecutive Farey fractions, with the cyclic lift at the seam.
Both \(b_\pm\) are odd, and \(Q>3t\) gives \(b_\pm>Q/2\).
The half translate of either neighbor has reduced denominator \(2b_\pm>Q\).
Thus each neighbor is an **uncancelled** event in (6). If the chosen
vertex was \(\tau u\), translate those events back by one half.
On each side of \(u\), an actual jump occurs no farther away than
\(1/[s(Q-s)]\). Other jumps can only shorten the interval, proving (1).
This uses no estimate on the integer value \(D_Q(u)\).

For two distinct probes with denominators \(q,q'\le t\), their circular
separation is at least \(1/(qq')\). The sum of their interval radii
toward each other is at most
\[
\frac{1/q+1/q'}{Q-t}
=\frac{q+q'}{qq'(Q-t)}
<\frac1{qq'},
\]
because \(Q>3t\). Hence their full plateaus are disjoint.

Summing both sides of (1) over (5) gives (2): for each denominator
\(d\le m\), there are \(2\varphi(d)\) probes with \(s=2d\).
The classical estimate
\[
A(m)=\frac6{\pi^2}m+O(\log(2m))
\]
follows directly by substituting
\(\varphi(n)/n=\sum_{d\mid n}\mu(d)/d\), summing the resulting floors,
and using the absolutely convergent series
\(\sum_d\mu(d)/d^2=1/\zeta(2)\). Together with (2) it proves (3).
No Möbius cancellation estimate is required.

For (4), integration over the disjoint probe cells proves the upper
sampling bound with \(\max |J_Q(u)|^{-1}\). The indicator of a maximizing
cell attains it. By (1), each cell has length at least \(1/(mQ)\).
Conversely there is a probe coming from a reduced point of denominator
exactly \(m\); its cell has length at most \(1/[m(Q-2m)]\).
This proves both finite bounds.

## 3. A small spatial mass with quadratic probe mass

Take the explicitly defined control
\[
f_{Q,t}=\mathbf1_{U_{Q,t}}.
\]
It lies in \(\mathcal A_Q\), is bounded by one, and is unchanged by
half translation and reflection. Indeed, both the nonzero-jump
partition and \(E_t\) are preserved by those operations; using open
cells makes the indicator zero at all their boundary points.
It follows exactly that
\[
\int f_{Q,t}=|U_{Q,t}|,\quad
\sum_{u\in E_t}f_{Q,t}(u)=2N_m,\quad
\sum_{u\in E_t}f_{Q,t}(u)-|E_t|\int f_{Q,t}
=2N_m(1-|U_{Q,t}|).\tag{7}
\]
The elementary totient asymptotic gives
\(N_m=3m^2/\pi^2+O(m\log(2m))\). Choose any sequence of prime orders
\(Q\to\infty\) and \(t=\lfloor\sqrt{Q/8}\rfloor\).
Then (3) and (7) yield
\[
\int f_{Q,t}=O(1/t),\qquad
\frac{\sum_{u\in E_t}f_{Q,t}(u)-|E_t|\int f_{Q,t}}t
\sim\frac{3t}{2\pi^2}\longrightarrow\infty.\tag{8}
\]
For every fixed rank offset \(r\), these orders eventually also satisfy
FD-348's strict condition
\(2t^2[2/Q+(|r|+1)/N_Q]<1\).
Thus the positive discrepancy in (8) occurs on an admissible panel,
without moving probes onto discontinuities or changing the genuine
Farey partition.

The precise lost hypothesis is equally important. Generally
\(f_{Q,t}\) is not a function of \(D_Q\): two disjoint cells with the
same integer defect need not both meet \(E_t\). For an exact example,
at \(Q=31,t=2\), both zero and \(187/1748\) have defect zero, but only
the former belongs to \(U_{31,2}\); the latter lies in the distinct
cell \((2/19,5/46)\). In particular, (8)
is not a counterexample to either the absolute or the one-sided bound
for \(w_r(D_Q)\), where \(w_r(z)=\max(0,2-|r-z|)\).
Those bounds, and the separate spatial small-window estimate, remain
open in the [sampling clue](../clues/CLUE-half-arc-rational-probe-sampling-discrepancy.md).

For the actual function one obtains only the valid positive estimate
\[
C_{Q,r}(t,t)
=\sum_{u\in E_t}w_r(D_Q(u))
\le mQ\int_0^1w_r(D_Q(v))\,dv,\tag{9}
\]
when FD-348's strict condition is also imposed.
Even a spatial integral \(O(1/t)\) makes the right side \(O(Q)\),
which does not reach the desired \(O_r(t)\) count.
The sharpness assertion (4) explains why a proof using only this
partition and positivity cannot remove that loss.

## 4. Prior art, validation and consequence

Consecutive Farey determinant identities, rational separation and the
totient estimates are classical. François Dress, *Discrépance des suites
de Farey*, J. Théor. Nombres Bordeaux **11**(2) (1999), 345–367
([primary paper](https://www.numdam.org/article/JTNB_1999__11_2_345_0.pdf)),
already discusses the large neighboring gaps at small-denominator
vertices. The local difference here is that simultaneous half-arc
events cancel at the probe, but the odd-denominator neighbors of its
even-denominator representative cannot cancel. This identifies the
scale of its full constant interval rather than just a guaranteed
small neighborhood.

Christoph Aistleitner and Josef Dick, *Functions of bounded variation,
signed measures, and a general Koksma–Hlawka inequality*,
[arXiv:1406.0230v2](https://arxiv.org/pdf/1406.0230), equation (2),
retains a variation factor in quadrature. Equation (8) is consistent
with that theorem: no uniform variation bound is imposed here.
The generic identity between the optimal positive sampling norm and
reciprocal cell length is elementary, not a new quadrature principle.
A targeted comparison with Farey quadrature and rational sampling
did not supply this particular half-arc specialization; no general
novelty claim is made.

An exact-fraction scratch audit built \(F_Q\) by sorting reduced
rationals, constructed all jumps independently from (6), and evaluated
half-arc counts directly by rank searches. It checked every integer
\(7\le Q\le100\) and \(2\le t\le\lfloor(Q-1)/3\rfloor\), plus
\(Q=127,251\) with
\(t\in\{2,3,4,5,8,11,16,\lfloor Q/4\rfloor\}\).
Across 1,536 panels and 51,290 probe cells, both radius bounds,
disjointness, the doubling identity, total-length bounds, and the
optimal-norm bounds passed in exact arithmetic.
For each panel and \(-2\le r\le2\), exact integration over the jump
intervals also verified the positive sampling inequality and the
restricted spatial contribution: 7,680 weighted panels.
These finite checks validate conventions and algebra, not the
asymptotic rate or an estimate on actual rank-level coincidences.
No Lean verification or independent adversarial approval is claimed.

The resulting obstruction is specific: genuine local constancy and a
small spatial window mass cannot alone give the rational count
estimate. Further progress must use how the integer defect values are
shared across separated cells, or supply another input that excludes
this relaxation. There is no new cancellation estimate, half-period
sector law, Franel bound or RH improvement. The elementary sampling
norm itself does not warrant a formalization handoff; the missing
analytic value-distribution statement remains the load-bearing target.
