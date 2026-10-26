# MC-533 — Geometric start coverage recovers sparsely sampled Möbius variance

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. No arithmetic variance upper bound is proved.

## Claim and observation boundary

Let \(X\) be a positive integer, \(I_X=\{X,\ldots,2X-1\}\),
\(1\le H\le X/20\) an integer, \(L_1=H\), \(L_2=\lfloor\sqrt2H\rfloor\), and
\(S_L(j)=M(j+L)-M(j)\). For each channel independently, choose a
**nonempty** retained set \(R_i\subset I_X\). Map every start to a
nearest retained start, breaking ties toward the smaller index:
\[
 \pi_i(j)\in\operatorname*{argmin}_{r\in R_i}|j-r|,
 \quad w_{i,r}=|\pi_i^{-1}(r)|,
 \quad D_i=\sum_{j\in I_X}|j-\pi_i(j)|.
\tag{1}
\]
The weights count represented starts, so \(\sum_{r\in R_i}w_{i,r}=X\).
For any one constant \(c_i\in\mathbb C\), put
\[
 W_i(c_i)=\sum_{r\in R_i}w_{i,r}|S_{L_i}(r)-c_i|^2.
\tag{2}
\]
If zeta has a zero \(\rho_0=\beta+i\gamma\), \(\beta>1/2\), of
multiplicity \(m\), then there are \(C>0,X_0\) such that
\[
 \boxed{\sum_{i=1}^2
   \frac{\sqrt{XW_i(c_i)}+D_i}{L_i}
   \ge C X^\beta(\log X)^{m-1}}
\tag{3}
\]
for all integer \(X\ge X_0\), uniformly in \(H,R_i,c_i\) in the
stated ranges. Constants may depend on the selected zero and the full
hypothetical zero set. There is **no restriction on the number of
omitted starts** apart from retaining at least one.

For a concrete consequence fix, independently of Möbius,
\[
 g_X=\lfloor\sqrt X\rfloor,\qquad
 R_X=\{X+kg_X:0\le k\le\lfloor(X-1)/g_X\rfloor\},
 \qquad q_X=|R_X|\asymp\sqrt X,
\tag{4}
\]
and \(H_X=\lfloor X/20\rfloor\), for sufficiently large \(X\).
For \(L_1=H_X,L_2=\lfloor\sqrt2H_X\rfloor\), define the ordinary
sample-centered energy
\[
 Q_i(X)=\min_{c\in\mathbb C}\sum_{r\in R_X}|S_{L_i}(r)-c|^2.
\tag{5}
\]
Then RH is equivalent to the existence of **one unbounded set of integer
scales** \(\mathcal X\), fixed before epsilon varies, on which
\[
 \frac{Q_i(X)}{q_X}\ll_\varepsilon X^{1+\varepsilon},
 \qquad i=1,2,\qquad\text{for every }\varepsilon>0.
\tag{6}
\]
The same scale set must serve both channels. The minimizers in (5) are
the separate empirical means and do not depend on epsilon.

[MC-531](MC-531-bounded-jumps-recover-trimmed-mobius-variance.md) and
[MC-532](MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md)
pay a location-free quadratic bill for the deleted count and retain
more than half the starts. Here the bill is the actual sum of distances
to retained data, paired with the correct coverage weights. The fixed
grid (4) retains a vanishing fraction of starts. This is a larger
admissible observation regime, not an independently weaker arithmetic
hypothesis: (6) is still RH-equivalent, and is not proved here.

## 1. Coverage-weighted recovery from bounded jumps

Let \(u_1,\ldots,u_N\in\mathbb C\) satisfy
\(|u_{j+1}-u_j|\le A\), and let \(R\ne\varnothing\) be retained.
For the nearest map, weights and distance sum in (1), telescoping gives
\[
 |u_j|\le |u_{\pi(j)}|+A|j-\pi(j)|.
\]
Summing, then applying weighted Cauchy–Schwarz, proves
\[
 \boxed{\sum_{j=1}^N|u_j|
 \le\sum_{r\in R}w_r|u_r|+AD
 \le\sqrt{N\sum_{r\in R}w_r|u_r|^2}+AD.}
\tag{7}
\]
This proof also works for any assignment of starts to retained points;
nearest assignment minimizes the distance sum. It need not minimize
the entire right side, whose energy weights also change.

For \(u_j=S_L(j)-c\), the exact arithmetic identity
\[
 u_{j+1}-u_j=\mu(j+L+1)-\mu(j+1)
\tag{8}
\]
gives \(A=2\), independently of the chosen constant. Thus
\[
 \sum_{j\in I_X}|S_L(j)-c|\le\sqrt{XW(c)}+2D.
\tag{9}
\]
A small unweighted energy cannot replace \(W\) on arbitrary irregular
sets. An isolated observed value may represent a large part of the
block. One sufficient conversion is \(W(c)\le w_{\max}
\sum_{r\in R}|S_L(r)-c|^2\), with the actual largest weight paid.

## 2. The complete analytic pair is preserved

The load-bearing arithmetic input is precisely MC-532, Sections 1–3.
Under the hypothetical zero above, it constructs complex smooth tests
\(f_{i,h}\), \(h=H/X\), supported in a fixed compact subset of \((1,2)\),
with
\[
 \int f_{i,h}=0,\qquad\sup_{0<h\le1/20}\|f_{i,h}\|_\infty<C_\rho,
\tag{10}
\]
such that the **complete** pairings
\[
 \mathcal L_i=\frac1{L_i}\int_X^{2X}
       (M(y+L_i)-M(y)-c_i)f_{i,h}(y/X)\,dy
\tag{11}
\]
satisfy
\[
 |\mathcal L_1+\mathcal L_2|
 \gg X^\beta(\log X)^{m-1}.
\tag{12}
\]
For clarity, that result cancels all unwanted reciprocal-zeta poles with
full multiplicities using MC-528's compact Mellin test. A compact
finite-order two-box inverse at ratio \(\sqrt2\) reconstructs the test.
Integer rounding of the second length costs \(O(1)\) in the coefficient
sum. The surviving pole contributes
\(X^{\rho_0}Q_{m-1}(\log X)\), with nonzero leading coefficient; its
conjugate is cancelled. Hence (12) holds on every sufficiently large
block, including arbitrarily selected unbounded scale sets. There is no
assumption of a rightmost zero, simplicity, or a nonzero ordinary residue.

Equation (10) removes each constant in (11) exactly. Integer window
sums are constant on each unit start cell, so (9) gives
\[
 |\mathcal L_i|
 \le\frac{\|f_{i,h}\|_\infty}{L_i}
       \sum_{j\in I_X}|S_{L_i}(j)-c_i|
 \ll_\rho\frac{\sqrt{XW_i(c_i)}+D_i}{L_i}.
\tag{13}
\]
Combine (12) and (13) to obtain (3). Neither test is cut by a retained-set
indicator, and no assertion that a sampled test has zero mean is needed.
Windows crossing \(2X\) remain included in the complete pairing.

## 3. A fixed square-root-sized grid

For (4), every integer start is within \(g_X\) of a sample and each
nearest-point cell has at most \(2g_X\) starts, including the two
endpoint cells. Also \(g_Xq_X\le X+g_X\le2X\). Consequently
\[
 D_i\le Xg_X\le X^{3/2},\qquad
 W_i(c_i)\le2g_X Q_i(X)
\tag{14}
\]
when \(c_i\) is the minimizer in (5). Under (6), (14) gives
\(W_i(c_i)\ll_\varepsilon X^{2+\varepsilon}\). Since both
lengths are comparable to \(X\), the left side of (3) is at most
\[
 O_\varepsilon(X^{1/2+\varepsilon/2}+X^{1/2}).
\tag{15}
\]
For any zero with \(\beta>1/2\), fix
\(0<\varepsilon<2\beta-1\). Equation (15) is \(o(X^\beta)\),
contradicting (3) along the unbounded set. Functional-equation symmetry
excludes left-of-line nontrivial zeros as well, proving RH.

Conversely, RH implies the classical Mertens bound
\(M(t)\ll_\delta t^{1/2+\delta}\) for every \(\delta>0\)
(MC-S67). For \(r\in I_X\) and either macroscopic length,
\(r+L_i<3X\). Taking \(c=0\) in (5) gives
\[
 Q_i(X)/q_X\le\max_{r\in R_X}|S_{L_i}(r)|^2
 \ll_\delta X^{1+2\delta}.
\]
Choose \(\delta=\varepsilon/2\). This proves (6) on all large integer
scales. No transfer from a complete mean square to a sparse sample is
assumed in this converse; it uses the RH-conditional pointwise bound.

## 4. What the geometric cost does and does not optimize

For ordered retained points \(r_1<\cdots<r_q\) in
\(\{1,\ldots,N\}\), put \(a=r_1-1\), \(b=N-r_q\).
The distance sum has the exact formula
\[
 D=\frac{a(a+1)}2+\frac{b(b+1)}2
     +\sum_{k=1}^{q-1}\left\lfloor\frac{(r_{k+1}-r_k)^2}{4}\right\rfloor.
\tag{16}
\]
The endpoint terms are sums of consecutive distances. Within a gap of
length \(d\), summing \(\min(j,d-j)\), \(1\le j<d\), gives
\(\lfloor d^2/4\rfloor\). This makes clustered omissions and well-spaced
observations quantitatively distinct even when their counts agree.

Each nearest-point cell of size \(w\) has total distance at least
\(\lfloor w^2/4\rfloor\), the minimum attained by centering the cell.
Cauchy–Schwarz therefore gives
\[
 D\ge\frac{\sum_r w_r^2-q}{4}
   \ge\frac{N^2/q-q}{4}.
\tag{17}
\]
For example, if \(q\mid N\) and \(N/q\) is odd, equally sized cells
with midpoint samples attain the last bound. Moreover,
\(u_j=A\,\operatorname{dist}(j,R)\) is an \(A\)-Lipschitz sequence,
vanishes on every retained point, and has total absolute mass exactly
\(AD\). Thus the distance bill is unavoidable for absolute-mass recovery
from these samples under **only** the jump constraint.

For large \(N\) and \(q\le\sqrt N\), (17) is of order at least \(N^2/q\).
At macroscopic lengths the resulting normalized recovery cost is at
least of order \(N/q\). The grid with \(q\asymp\sqrt N\) therefore reaches
the square-root cost with the correct worst-case sample-count exponent
for this generic recovery method. This is not an information lower
bound for Möbius: the distance sequence need not be multiplicative or
even a compatible pair of sliding sums, and signed analytic pairings
can cancel its mass. Fewer samples might suffice with new arithmetic
or phase-sensitive information. No such improvement is established.

## Prior art, validation and consequence

The interpolation argument is classical Lipschitz recovery, not a new
sampling principle. [Baran–Demaine–Katz, Section 2](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf)
(MC-S85) derives integral uncertainty between observations from the
Lipschitz envelope; equal observed values give the familiar quadratic
gap cost. Equations (7), (16), and (17) are elementary discrete
specializations with a weighted second-moment bound added explicitly.

RH-equivalent smoothing and moment criteria also have extensive prior
art. [Verjovsky, Sections 4 and 9–11](https://arxiv.org/html/2607.25002v2)
(MC-S86, preprint) treats local moments of Möbius Fourier polynomials on
arcs of scale \(1/N\), using a derivative bound to recover the value at
the center. Those observations are Fourier-variable local moments,
whereas (6) concerns centered second moments at sparse physical starts
of two macroscopic windows. Neither that comparison nor the targeted
literature search establishes external novelty. The canonical
reciprocal-pole and two-box inputs remain MC-528 and MC-532; no new
analytic continuation argument is asserted here.

Exact integer checks tested (7) in 332,643 cases for all nonempty masks at lengths
\(1\le N\le7\), all increments in \(\{-2,0,2\}\), and centers
in \(\{-3,0,3\}\), comparing squared nonnegative residuals without
floating point. The 247-mask geometry enumeration checked (16), (17), and the
distance-envelope equality. Grid weights, endpoint coverage and (14)
were checked for all integers \(1\le X\le2000\). These finite controls
audit the elementary recovery and indexing; they do not validate zero
location, the full-zero-set certificate, or any arithmetic ceiling.
The proofs above establish the general statements. No Lean check or
independent adversarial approval is asserted.

The result changes the source requirement from a small count of arbitrary
deletions to adequate geometric coverage with a correctly weighted
sample energy. In particular, omitting \(X-O(\sqrt X)\) starts need
not weaken the RH strength of the paired variance criterion. Raw sample
count without coverage, unweighted energy without cell control, bounds
on unrelated scales, and qualitative almost-all cancellation do not
supply (3) or (6). Constants in the analytic test remain dependent on
the full hypothetical zero set, with no effective acquisition bound.
The unresolved arithmetic task is still to prove the sample energy
ceiling; there is no unconditional improvement for \(M(x)\).
