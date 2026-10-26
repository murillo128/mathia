# MC-537 — Small sampled energy permits quarter-power Möbius observations

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. Randomness belongs only to observation locations.
No arithmetic energy ceiling or improved estimate for \(M(x)\) is proved.

## Claim and quantifiers

For every sufficiently large integer \(X\), put
\[
 I_X=\{X,\ldots,2X-1\},\quad q_X=\lceil X^{1/4}\rceil,
 \quad L_1=\lfloor X/20\rfloor,\quad L_2=\lfloor\sqrt2L_1\rfloor.
\tag{1}
\]
For each channel draw \(2q_X\) independent uniform starts
\(R_{i,X,a}\) in \(I_X\), **with replacement**, and define
\[
 S_L(j)=M(j+L)-M(j),\qquad
 V_i(X)=\min_{c\in\mathbb R}\frac1{2q_X}
       \sum_{a=1}^{2q_X}|S_{L_i}(R_{i,X,a})-c|^2.
\tag{2}
\]
Repeated observations retain their multiplicities. The minimizer is
the sample mean. Use the product sampling law across channels and
integer scales, independently of the fixed Möbius sequence.

There is an event of probability one on which RH is equivalent to:
there exists one unbounded integer scale set \(\mathcal X\), fixed
before epsilon varies, such that for every \(\varepsilon>0\),
\[
 \boxed{V_i(X)\ll_\varepsilon X^{1+\varepsilon}
       \quad(i=1,2;\ X\in\mathcal X).}
\tag{3}
\]
The set and constants may depend on the sampling outcome. More
precisely, if zeta has a zero \(\rho=\beta+i\gamma\),
\(\beta>1/2\), of multiplicity \(m\), then on that event, at
every sufficiently large integer scale,
\[
 \boxed{\sqrt{V_1(X)}+\sqrt{V_2(X)}+\sqrt X(\log X)^2
       \gg_\rho X^\beta(\log X)^{m-1}.}
\tag{4}
\]
The analytic constants inherit dependence on the full hypothetical
zero set from [MC-532](MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md).
The almost-sure onset may depend on the sampling outcome.

[MC-536](MC-536-stratified-random-starts-reduce-the-mobius-variance-sample-exponent.md)
uses cube-root-many stratified samples and controls quadrature error
without exploiting a small observed energy. Here pairwise differences
and a range bound use that energy directly. The recovered quantity is
population **mean absolute dispersion**, sufficient for the complete
pole test; a full population second moment is not recovered. The
sampling law is also different.

## 1. A finite sampling lemma with an observable center

Let \(u_1,\ldots,u_X\) be a fixed real sequence with
\(|u_{j+1}-u_j|\le A\). Draw \(2q\) independent uniform
indices \(R_a\), write \(Y_a=u_{R_a}\), and put
\[
 V=\min_c\frac1{2q}\sum_a(Y_a-c)^2,\quad
 D=\frac1{X^2}\sum_{j,k}|u_j-u_k|,\quad
 B=\max_j u_j-\min_j u_j.
\tag{5}
\]
For every \(t>0\), set
\(r=\min\{X,\lceil Xt/(2q)\rceil\}\). With probability at
least \(1-3e^{-t}\),
\[
 \boxed{D\le\left(4+\frac{16t}{\sqrt q}\right)\sqrt V
                 +\frac{16Art}{q}.}
\tag{6}
\]
In particular the last term is at most
\(8AXt^2/q^2+16At/q\). The statement is valid for constant
signals, singleton populations, repeated draws and endpoint extrema.

Pair the observations and define
\[
 Z_b=|Y_{2b-1}-Y_{2b}|,\quad
 \bar Z=q^{-1}\sum_{b=1}^q Z_b.
\]
These are independent nonnegative variables bounded by the fixed
population range \(B\), with \(\mathbb E Z_b=D\).
For \(B>0\), the elementary Chernoff argument gives
\[
 \Pr\{\bar Z\le D/2\}\le \exp(-qD/(8B)).
\tag{7}
\]
Indeed convexity on \([0,1]\) gives
\(e^{-z}\le1-(1-e^{-1})z\). Applying exponential Markov
to \(\sum_b Z_b/B\) yields the stronger exponent
\(-(1/2-e^{-1})qD/B\), and \(1/2-e^{-1}>1/8\).
Consequently, with probability at least \(1-e^{-t}\),
\[
 D\le2\bar Z+8Bt/q.
\tag{8}
\]
If \(D\le8Bt/q\) this is automatic; otherwise failure implies
the event in (7). If \(B=0\), all these quantities vanish.

Fix one minimizing and one maximizing population index before drawing
the samples. Around each choose a consecutive set of \(r\) indices
containing it. Every point in this set lies within distance \(r-1\)
of the extremum. If \(r<X\), the probability of missing either
specified set is at most
\[
 2(1-r/X)^{2q}\le2e^{-t};
\]
if \(r=X\), neither set can be missed. On the two-hit event,
\[
 B\le (\max_aY_a-\min_aY_a)+2Ar.
\tag{9}
\]
For the empirical mean \(\bar Y\), deterministic inequalities give
\[
 \bar Z\le q^{-1}\sum_a|Y_a-\bar Y|\le2\sqrt V,
 \qquad \max_aY_a-\min_aY_a\le2\sqrt{qV}.
\tag{10}
\]
For the second inequality, square the difference of the two extreme
sample values and bound it by twice the total squared deviation.
Intersect the events in (8) and (9), substitute (10), and use a union
bound to obtain (6). Independence of these two events is not needed.
The range is bounded on the same event **after** applying (8) with
its fixed true range; no random bound was substituted inside a
concentration theorem.

## 2. Recover every bounded mean-zero pairing on the same event

Write \(\bar u=X^{-1}\sum_j u_j\). Jensen's inequality gives
\[
 X^{-1}\sum_j|u_j-\bar u|\le D.
\tag{11}
\]
Thus for any complex weights with \(\sum_jw_j=0\) and
\(|w_j|\le F\), and any \(L>0\),
\[
 \left|L^{-1}\sum_jw_ju_j\right|\le FXD/L.
\tag{12}
\]
This is simultaneous over all such weights. Neither the empirical
mean nor an estimate for the population mean enters the pairing.
Pairwise differences eliminated the fitted center before the
probabilistic step. The sample energy is translation invariant.

For a fixed family of bounded-jump populations, take
\(q=\lceil X^{1/4}\rceil\), \(t=4\log X\), and a fixed
bound on \(A\). Equation (6) becomes
\[
 D\ll\sqrt V+\sqrt X(\log X)^2
\tag{13}
\]
outside events of probability at most \(3X^{-4}\), for all large
\(X\). The coefficient \(t/\sqrt q\) is eventually bounded.
The first Borel–Cantelli lemma makes (13) hold almost surely on all
large integer scales. Independence across scales is unnecessary for
this conclusion. For two families, take their intersection.

## 3. Transfer to the paired Möbius pole test

MC-532, Sections 1–3, gives deterministic compactly supported
mean-zero tests \(f_{i,h}\), \(h=L_1/X\), with uniformly bounded
sup norms, and complete pairings
\[
 P_i(X)=L_i^{-1}\int_X^{2X}S_{L_i}(y)f_{i,h}(y/X)\,dy,
 \qquad |P_1(X)+P_2(X)|\gg_\rho
                       X^\beta(\log X)^{m-1}.
\tag{14}
\]
That theorem includes integer rounding and windows crossing \(2X\).
Its full-multiplicity reciprocal-zeta annihilator cancels the
conjugate pole, so the lower bound holds on every large block. These
are inherited analytic inputs, not consequences of sampling.

For integer \(L_i\), \(S_{L_i}(y)\) is constant on
\([j,j+1)\) and
\[
 |S_{L_i}(j+1)-S_{L_i}(j)|
 =|\mu(j+L_i+1)-\mu(j+1)|\le2.
\]
Set \(w_j=\int_j^{j+1}f_{i,h}(y/X)\,dy\). These weights have
zero sum and uniformly bounded magnitude, and (12) is exactly the
integral in (14). Since \(L_i\asymp X\), (13) bounds each
\(|P_i(X)|\) by a constant times
\(\sqrt{V_i(X)}+\sqrt X(\log X)^2\). This proves (4).

The probability-one event controls dispersion of the two fixed Möbius
populations. It is independent of which zero or mean-zero test is
subsequently used; there is no uncountable union over tests. If (3)
holds, choose \(0<\varepsilon<2\beta-1\). Both square-root
energy terms and the logarithmic remainder in (4) are
\(o(X^\beta)\), contradicting (4) on the same unbounded set.
Functional-equation symmetry then yields RH.

Conversely, under RH the classical bound
\(M(y)\ll_\delta y^{1/2+\delta}\) bounds every queried window
sum by \(O_\delta(X^{1/2+\delta})\). Hence (3) holds on all
sufficiently large integer scales for **every** sampling outcome,
with \(\delta=\varepsilon/2\). The forward implication allows
the common unbounded scale set to be chosen after the observations,
because its exceptional events have already been removed on all
large integer scales.

## 4. The quarter-power boundary for this generic sampling guarantee

The exponent cannot be lowered using only bounded jumps and small
sampled variance for arbitrary fixed signal families under this
uniform sampling law. Fix \(0\le\alpha<1/4\) and choose
\(3/4<\kappa<1-\alpha\). On each large block let
\[
 j_0=\lfloor3X/2\rfloor,\quad a_X=\lfloor X^\kappa\rfloor,
 \qquad u_j=(a_X-|j-j_0|)_+.
\tag{15}
\]
This deterministic population is chosen before the draws and has
jumps at most one. Its mass is exactly \(a_X^2\). Choose one
fixed smooth mean-zero function \(f\) on \((1,2)\) equal to
one near \(3/2\); subtract a disjoint smooth bump to arrange
zero integral. For the cell-integrated weights, eventually
\[
 X^{-1}\sum_jw_ju_j=a_X^2/X\asymp X^{2\kappa-1},
 \qquad 2\kappa-1>1/2.
\tag{16}
\]
With \(2\lceil X^\alpha\rceil\) uniform observations, the
probability of hitting the tent is at most
\[
 2\lceil X^\alpha\rceil(2a_X-1)/X
             =O(X^{\alpha+\kappa-1})=o(1).
\tag{17}
\]
On a miss, all observed values and their centered variance are zero.
Along dyadic scales the probabilities in (17) are summable, so
almost surely all sufficiently large dyadic samples miss this
fixed family despite (16). The counterexample is to a generic
bounded-jump inference at a smaller sampling exponent. It is not a
Möbius sequence, a common coefficient/window realization, a statement
about every sampling design, or a lower bound for Möbius itself.
No optimal logarithmic factor at exponent \(1/4\) is claimed.

## Prior art, validation and consequence

The concentration step is the classical exponential-moment method
of Hoeffding (MC-S75); (7) supplies the needed specialization in full.
[Maurer–Pontil, Theorem 4](https://www.cs.mcgill.ca/~colt2009/papers/012.pdf)
(MC-S91) provides adjacent primary prior art for confidence bounds
that exploit small empirical variance. Its theorem is not imported
with a data-dependent range; (8)–(10) handle that range explicitly.
[Baran–Demaine–Katz](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf)
(MC-S85), Section 2 and the randomized-analysis section, treats
Lipschitz envelopes, hidden area and sampling cost. The tent control
is an elementary specialization of that familiar obstruction.
Haber's stratified quadrature rate, as presented by
[Chopin–Gerber, Section 2.1](https://arxiv.org/html/2210.01554v2#S2.SS1)
(MC-S90), remains the comparison for MC-536. No new concentration
principle, general quadrature rate or external novelty is claimed.

Exact integer/rational checks covered all 121 sequences of lengths
one through five starting at zero with increments in \(\{-1,0,1\}\),
and all 60,866 ordered sample outcomes for \(q=1,2\). They verified
(10)–(11) and 295,178 conditional range checks underlying (9),
including repeated draws and endpoint extrema. Exact lower-tail
probabilities in (7) were enumerated and compared numerically with
its exponential upper bound. Separate integer checks verified the
tent mass and zero-mean weighted pairing at lengths 80, 160, 320 and
640. These are bookkeeping audits; the proofs establish the
unbounded-scale implications. No Lean verification or independent
adversarial approval is asserted.

The mathematical delta is that the small-energy premise itself
allows a stronger observation theorem than unrestricted quadrature
accuracy: quarter-power-many independent starts per channel suffice.
MC-534/535's controls chosen after fixing observations do not
contradict a fixed-source probability guarantee. The new tent control
also closes a smaller-exponent escape for the generic law here.
Neither random sampling nor mean absolute recovery supplies the
unproved energy premise (3), restores the full uncentered variance,
or bounds the actual Möbius function more strongly. The elementary
sampling assembly gives no separate high-value Lean fertility target.
