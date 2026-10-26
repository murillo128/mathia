# MC-536 — Stratified random starts reduce the Möbius variance sample exponent

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. Probability concerns the observation locations only.
No Möbius energy ceiling or improved bound for \(M(x)\) is proved.

## Claim and probability quantifiers

For every sufficiently large integer \(X\), put
\[
 I_X=\{X,\ldots,2X-1\},\quad q_X=\lceil X^{1/3}\rceil,
 \quad H_X=\lfloor X/20\rfloor,\quad
 L_1=H_X,\quad L_2=\lfloor\sqrt2H_X\rfloor.
\tag{1}
\]
Partition \(I_X\) into \(q_X\) consecutive nonempty cells
\[
 B_{X,b}=\{X+\lfloor(b-1)X/q_X\rfloor,\ldots,
                  X+\lfloor bX/q_X\rfloor-1\},\quad 1\le b\le q_X.
\tag{2}
\]
For each channel \(i\), choose one uniform integer \(R_{i,X,b}\)
in each cell. Take all choices independent across cells, channels
and scales, under the resulting product law. The sampling law does
not depend on Möbius values or any zeta zero. Define
\[
 S_L(j)=M(j+L)-M(j),\qquad
 Q_i(X)=\min_{c\in\mathbb R}\sum_{b=1}^{q_X}
                     |S_{L_i}(R_{i,X,b})-c|^2.
\tag{3}
\]
The minimizer is the ordinary sample mean.

**Almost-sure criterion.** There is a set of sampling outcomes of
probability one such that, for each outcome in this set, RH is
equivalent to the following property: there exists one unbounded set
\(\mathcal X\) of integer scales for which
\[
 \boxed{Q_i(X)/q_X\ll_\varepsilon X^{1+\varepsilon}
       \quad(i=1,2;\ X\in\mathcal X),\qquad
       \text{for every }\varepsilon>0.}
\tag{4}
\]
The set \(\mathcal X\) may depend on the realized observations, but
must be the same for both channels and fixed before epsilon varies.
The implicit constants may depend on the outcome and epsilon, and
must be uniform along \(\mathcal X\).

More quantitatively, if zeta has a zero \(\rho=\beta+i\gamma\),
\(\beta>1/2\), of multiplicity \(m\), then with probability one,
for every sufficiently large integer \(X\),
\[
 \boxed{\sum_{i=1}^2\sqrt{Q_i(X)/q_X}
                  +\sqrt{X\log X}
       \gg_\rho X^\beta(\log X)^{m-1}.}
\tag{5}
\]
The onset may depend on the sampling outcome. Constants in the
analytic tests depend on the full hypothetical zero set, as in
[MC-532](MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md).

The change from [MC-533](MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.md)
is from a deterministic square-root-sized grid to cube-root-many
random observations per channel. This changes the guarantee: the
source is fixed before sampling, and an exceptional set of sampling
outcomes is allowed. It is not a uniform guarantee for all bounded
coefficient sequences after their observations have been chosen.

## 1. A discrete quadrature that removes every constant exactly

Let \(u_j\in\mathbb R\), \(j\in I_X\), be fixed, with
\(|u_{j+1}-u_j|\le A\). For \(f\in C^1([1,2];\mathbb C)\)
with \(\int_1^2f=0\), write
\[
 F=\|f\|_\infty,\quad D=\|f'\|_\infty,\quad
 w_j=\int_j^{j+1}f(y/X)\,dy.
\tag{6}
\]
Then \(|w_j|\le F\), \(|w_j-w_k|\le D|j-k|/X\), and
\(\sum_jw_j=0\). For any consecutive partition into cells \(B_b\)
of sizes \(d_b\), set \(W_b=\sum_{j\in B_b}w_j\). Independently
sample \(R_b\) uniformly in \(B_b\), and, for a normalization
\(L>0\), define
\[
 P=L^{-1}\sum_jw_ju_j,\qquad
 \widehat P=L^{-1}\sum_bW_bu_{R_b}.
\tag{7}
\]
Both expressions are unchanged if any one constant is subtracted
from every \(u_j\). For \(\widehat P\), that constant may even
be chosen after seeing the samples: \(\sum_bW_b=0\) identically.
Thus, with \(Q=\min_c\sum_b|u_{R_b}-c|^2\),
\[
 |\widehat P|\le\frac{\sqrt{\sum_b|W_b|^2}}{L}\sqrt Q
       \le\frac{F\sqrt{\sum_bd_b^2}}{L}\sqrt Q.
\tag{8}
\]
Replacing \(W_b\) by \(d_bf(R_b/X)\) would lose this exact
constant cancellation. The weights in (7) are deterministic
integrals of the test, not additional observations of \(u\).

## 2. Bias, independent fluctuations and all-scale control

Put \(\bar u_b=d_b^{-1}\sum_{j\in B_b}u_j\).
The exact within-cell covariance identity gives
\[
 P-\mathbb E\widehat P
 =\frac1L\sum_b\frac1{2d_b}
       \sum_{j,k\in B_b}(u_j-u_k)(w_j-w_k).
\tag{9}
\]
Since \(\sum_{j,k\in B_b}(j-k)^2=d_b^2(d_b^2-1)/6\),
\[
 |P-\mathbb E\widehat P|
       \le\frac{AD}{12LX}\sum_bd_b(d_b^2-1).
\tag{10}
\]
This estimator is generally biased. Equation (10) is needed even
though the samples are uniform inside their cells.

Independence between cells, with no independence assumption on the
values of \(u\), gives
\[
 \mathbb E|\widehat P-\mathbb E\widehat P|^2
 =L^{-2}\sum_b|W_b|^2\operatorname{Var}(u_{R_b})
 \le\frac{A^2}{12L^2}\sum_b|W_b|^2(d_b^2-1).
\tag{11}
\]
The last bound follows by applying the jump bound in
\(\operatorname{Var}(u_{R_b})=(2d_b^2)^{-1}
\sum_{j,k\in B_b}(u_j-u_k)^2\).

For the almost-sure assertion, retain a tail bound rather than using
only this second moment. Define
\[
 R^2=\frac{A^2}{L^2}\sum_b|W_b|^2(d_b-1)^2.
\tag{12}
\]
The range length of either real coordinate of the \(b\)-th
summand in (7) is at most \(A|W_b|(d_b-1)/L\).
Hoeffding's bounded-independent-sum inequality, applied to real and
imaginary parts at threshold \(t/\sqrt2\), therefore gives
\[
 \Pr\{|\widehat P-\mathbb E\widehat P|\ge t\}
       \le4\exp(-t^2/R^2)\qquad(t>0).
\tag{13}
\]
If \(R=0\), the fluctuation is identically zero.

For the balanced partition (2) with any \(1\le q\le X\),
\(\max_bd_b\le2X/q\), \(\sum_bd_b=X\), and
\(\sum_bd_b^2\le2X^2/q\). If \(L\asymp X\), (8),
(10) and (12) imply
\[
 |\widehat P|\ll F\sqrt{Q/q},\quad
 |P-\mathbb E\widehat P|\ll AD\,X/q^2,\quad
 R^2\ll A^2F^2X^2/q^3.
\tag{14}
\]
The constants here depend only on a lower bound for \(L/X\).
At \(q=\lceil X^{1/3}\rceil\), the bias is \(O(X^{1/3})\)
and \(R^2=O(X)\), for uniformly bounded \(A,F,D\).
Choose a sufficiently large fixed \(C\) and
\(t=C\sqrt{X\log X}\) in (13). The failure probabilities are
\(O(X^{-3})\), summable over **all integer scales**. The first
Borel–Cantelli lemma yields
\[
 |P-\widehat P|=O(\sqrt{X\log X})
 \quad\text{almost surely for all sufficiently large }X.
\tag{15}
\]
This works for any deterministic sequence of tests having uniform
\(C^1\) bounds. Independence across scales is unnecessary for
this step. Neither a random fitted center nor subsequent selection
of an unbounded subset of scales alters (15).

## 3. Apply the bound to the complete paired Möbius pole test

Fix one hypothetical zero as in (5), and let \(h=H_X/X\).
MC-532, Sections 1–3, supplies deterministic tests \(f_{i,h}\)
supported in one fixed compact subset of \((1,2)\), with
\[
 \int f_{i,h}=0,\qquad
 \sup_{0<h\le1/20}(\|f_{i,h}\|_\infty+
                         \|f'_{i,h}\|_\infty)<\infty,
\tag{16}
\]
and complete pairings
\[
 P_i(X)=\frac1{L_i}\int_X^{2X}S_{L_i}(y)f_{i,h}(y/X)\,dy,
 \qquad |P_1(X)+P_2(X)|
       \gg_\rho X^\beta(\log X)^{m-1}.
\tag{17}
\]
Its finite-order distributional inverse gives (16) for every fixed
derivative order. Its integer rounding error is \(O(1)\) in the
coefficient sum. The full-multiplicity annihilator of
[MC-528](MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md)
retains the selected principal part and cancels its conjugate, so
(17) holds on every large block, not just near favorable phases.
These are inherited arithmetic/analytic inputs, not consequences of
random sampling.

For integer \(L_i\), \(S_{L_i}(y)\) is constant on
\([j,j+1)\) and
\[
 |S_{L_i}(j+1)-S_{L_i}(j)|
 =|\mu(j+L_i+1)-\mu(j+1)|\le2.
\tag{18}
\]
Thus (7) is exactly (17)'s integral, with \(A=2\), including
windows crossing \(2X\). Apply (8) and (15) separately to the two
channels and use the triangle inequality in (17). This proves (5).
The sample centers in (3) need not approximate the complete means;
their disappearance is an algebraic identity before concentration.

If (4) holds, choose \(0<\varepsilon<2\beta-1\). Its contribution
to the left side of (5) is \(O(X^{1/2+\varepsilon/2})\), and
\(\sqrt{X\log X}=o(X^\beta)\). This contradicts (5) on the
same unbounded set, even if that set was selected after observation.
Functional-equation symmetry then gives RH. For this implication it
suffices to fix one off-critical zero before sampling. Alternatively,
the zero set is countable, so one may intersect the probability-one
events for one chosen test construction per zero.

Conversely, under RH the classical Mertens bound gives
\(M(t)\ll_\delta t^{1/2+\delta}\). All queried endpoints lie
below \(3X\), so every sampling outcome satisfies
\[
 Q_i(X)/q_X\le\max_{j\in I_X}|S_{L_i}(j)|^2
                  \ll_\delta X^{1+2\delta}.
\tag{19}
\]
Take \(\delta=\varepsilon/2\) and all sufficiently large integer
scales. This proves the converse for every outcome, not merely
almost every outcome.

## Prior art, controls and consequence

The randomized improvement is classical stratified quadrature.
[Chopin–Gerber, Section 2.1](https://arxiv.org/html/2210.01554v2#S2.SS1)
(MC-S90) restates Haber's one-point-per-cell rule and its
one-dimensional \(q^{-3/2}\) root-mean-square rate. Hoeffding's
inequality (MC-S75) supplies (13). Equations (9)–(15) derive the
discrete, exactly mean-removing specialization needed here; no new
Monte Carlo rate or concentration theorem is claimed.
[Verjovsky, Sections 4 and 5.4](https://arxiv.org/html/2607.25002v2)
(MC-S86, preprint) also retains deterministic Möbius coefficients and
randomizes evaluation points, but uses moments on Fourier arcs.
The observation here is a finite stratified sample of physical
window starts, followed by an almost-sure all-scale assertion.
Neither comparison establishes external novelty.

- **Order of quantifiers.** MC-534 and MC-535 construct controls after
  fixing the queried locations. They remain valid for every realized
  partition sample. Equations (13)–(15) instead hold for a fixed
  source before its random observations; they are not simultaneous
  over all possible sources selected after the draws. Thus this
  result does not contradict either matched-control obstruction.
- **No randomized Möbius model.** Only the observation locations are
  independent. No signs, prime factors, or overlapping window sums
  are asserted to be independent. Sampling accuracy does not prove
  the energy premise (4).
- **Centers and bias.** Ordinary pointwise test weights do not remove
  a fitted mean exactly. Cell-integrated weights do, but introduce
  the explicit covariance bias (10). Omitting either issue would
  invalidate the transfer. Constant signals give zero in (7) exactly;
  singleton cells give exact recovery with zero bias and fluctuation.
- **Scope.** No conclusion is asserted for every deterministic seed,
  adaptive sampling laws, arbitrary clustered samples, or a source
  chosen in response to the draws. The sample exponent \(1/3\) is
  sufficient; optimality for Möbius or its centered energy criterion
  is not proved. The statement gives no finite RH decision procedure,
  no effective zero-uniform onset, and no conclusion about simplicity.

Exact rational checks covered 7,108 configurations and 42,643 joint
sample outcomes: all lengths \(1\le X\le7\), all balanced cell
counts, and every increment string in \(\{-2,0,2\}^{X-1}\).
The test weights had centered linear real part and centered quadratic
imaginary part. The checks verified the exact expectation/covariance
identity (9), independent variance identity (11), their stated upper
bounds, the summand range bounds, (8), and exact removal of the
sample-dependent empirical mean. Unequal and singleton cells were
included. These are finite bookkeeping checks, not evidence for an
arithmetic energy estimate, the asymptotic probability statement, or
zero location. The proofs establish those implications; no Lean
verification or independent adversarial approval is asserted.

The mathematical delta is a smaller admissible observation count
under a different, explicit probability guarantee. The remaining
source problem is still an independently proved joint energy ceiling
on common scales. It cannot be supplied by the quadrature theorem,
qualitative almost-all cancellation, or the probability-one statement
about recovery. The elementary covariance/concentration assembly does
not present a separate high-value Lean fertility target.
