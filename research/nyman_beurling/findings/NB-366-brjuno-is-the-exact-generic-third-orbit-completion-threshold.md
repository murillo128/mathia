# NB-366 — Brjuno is the exact generic third-orbit completion threshold

- **Status:** proved (classical metric theorem plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-356 and NB-360 for exact orbit membership and physical cost; NB-362 for the Brjuno sufficient condition
- **Classification:** LITERATURE+DERIVED + EXACT-TARGET-MEMBERSHIP + NEGATIVE/OBSTRUCTION

## Claim and scope

The ordinary Brjuno condition is necessary as well as sufficient for almost-everywhere completion of a fixed irrational Nyman seed pair by one real third seed. This closes the generic-membership gap in NB-362 and decides the zero-one alternative of NB-365. It does not classify the existence of exceptional completing seeds.

Fix real seeds \(p,q>1\), with irrational \(\alpha=\log p/\log q\). Let \(P_j/Q_j\) be its regular continued-fraction convergents, with \(Q_{-1}=0,Q_0=1\), and put
\[
\mathcal B_1(\alpha)=\sum_{j\ge1}\frac{\log Q_{j+1}}{Q_j},\qquad
\delta_n=\|n\alpha\|_{\mathbb R/\mathbb Z}>0,
\]
\[
S_\alpha(\beta)=\sum_{n\ge1}
\frac1{n^2(\delta_n^2+\|n\beta\|_{\mathbb R/\mathbb Z}^2)}.
\tag{1}
\]
Then, with Lebesgue measure on any unit interval,
\[
\boxed{
S_\alpha(\beta)<\infty\text{ for almost every }\beta
\quad\Longleftrightarrow\quad \mathcal B_1(\alpha)<\infty.
}
\tag{2}
\]
More precisely, if \(\mathcal B_1(\alpha)=\infty\), then for almost every \(\beta\) there are infinitely many distinct \(n\) with
\[
n\|n\alpha\|<1,\qquad n\|n\beta\|\le1.
\tag{3}
\]
The corresponding summands in (1) are at least \(1/2\); generic divergence is witnessed by terms failing to tend to zero, not inferred from an infinite expectation.

For the physical statement, in \(H=L^2(0,1;dx)\), define
\[
e=1,\quad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a},
\]
\[
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\},\quad
\mathcal N=\overline{\operatorname{span}}\{g_v:v>1\},\quad t=P_{\mathcal N}e.
\]
Consequently,
\[
\boxed{
\begin{aligned}
\mathcal B_1(\alpha)<\infty
&\Longrightarrow t\in\mathcal C_q+\mathcal C_p+\mathcal C_{q^\beta}
\quad\text{for a.e. }\beta\in(1,2),\\
\mathcal B_1(\alpha)=\infty
&\Longrightarrow t\notin\mathcal C_q+\mathcal C_p+\mathcal C_{q^\beta}
\quad\text{for a.e. }\beta\in(1,2).
\end{aligned}}
\tag{4}
\]
The sums are algebraic sums of closed real-dilation spaces: one finite-norm vector from each space. The same full/null classification holds on every fixed nonempty open subinterval. No finite generator count or specified integer third seed is covered.

## 1. The positive implication retains its clipped-moment proof

NB-362 proves directly that
\[
\sum_{n\ge1}\min\left(\frac1n,\frac1{n^2\delta_n}\right)<\infty
\quad\Longleftrightarrow\quad \mathcal B_1(\alpha)<\infty.
\tag{5}
\]
For clarity, the upper bound needed here uses consecutive continued-fraction blocks. Write \(u=Q_j,V=Q_{j+1}\); divide \([u,V)\) into blocks \([ku,(k+1)u)\), truncating the last. Distinct fractional parts within such a block are separated by more than \(1/(2u)\). In order of distance from zero, all but the closest point have distances at least \((h-1)/(4u)\). Using \(1/n\) at the closest point and the other branch of the minimum at the rest bounds the block by
\[
\frac1{ku}+\frac{4H_u}{k^2u}.
\]
Its sum over \(k\) is \(O((1+\log V)/u)\). The finitely many initial indices and \(u=1\) are harmless. This establishes the sufficient direction of (5) without any assumptions on equidistribution.

For \(n\ge2\), Haar measure and an elementary one-variable integral give
\[
\int_0^1\min\left(1,\frac1{n^2(\delta_n^2+\|n\beta\|^2)}\right)d\beta
\asymp\min\left(\frac1n,\frac1{n^2\delta_n}\right).
\tag{6}
\]
Tonelli makes the clipped series finite almost surely under (5). There can then be only finitely many unclipped summands above one, and each is finite since \(\alpha\) is irrational. Thus (1) converges almost surely. This proof alone gives no converse; the remaining sections supply it.

## 2. Reduce the convergent-multiple blocks before charging totients

For each sufficiently large \(j\), put
\[
u=Q_j\ge2,\qquad V=Q_{j+1},\qquad
L_j=\left\lfloor\sqrt{V/u}\right\rfloor.
\]
Retain integers \(m\) with \(u\le m\le L_j\), an empty range if \(L_j<u\). Every original denominator \(n=um\) satisfies
\[
n\|n\alpha\|\le um^2\|u\alpha\|<\frac{um^2}{V}\le1.
\tag{7}
\]
For each retained \(m\), use **all** divisors \(g\mid u\) satisfying \(\gcd(m,u/g)=1\), and form the reduced denominator
\[
d=gm,\qquad n=um=\frac ug\,d.
\tag{8}
\]
These denominators have three decisive properties:

1. \(\gcd(d,u)=g\), so \(d\) determines \(g\) and \(m\) uniquely within the block. No pair is counted twice.
2. \(u\le d\le uL_j\le\sqrt{uV}<V\). Thus denominators from different convergent blocks lie in disjoint intervals \([Q_j,Q_{j+1})\).
3. The exact identity
   \[
   \boxed{\sum_{\substack{g\mid u\\\gcd(m,u/g)=1}}\varphi(gm)=u\varphi(m)}
   \tag{9}
   \]
   restores the whole weight \(u\), rather than the potentially small \(\varphi(u)\).

To prove (9), factor prime by prime. For a prime \(\ell\) with exponent \(a\) in \(u\), if \(\ell\nmid m\), all exponents \(0\le c\le a\) in \(g\) are permitted and \(\sum_{c=0}^a\varphi(\ell^c)=\ell^a\). If the exponent of \(\ell\) in \(m\) is \(b>0\), the coprimality condition forces \(c=a\), and \(\varphi(\ell^{a+b})=\ell^a\varphi(\ell^b)\). Primes outside \(u\) retain their ordinary factor in \(\varphi(m)\). Multiplying proves (9), including \(m=1\) in the general identity.

The restriction \(m\ge u\) costs only a summable logarithmic error below. It is what makes the *reduced* denominator blocks disjoint. Disjointness of the original multiples alone would not suffice after reduction.

## 3. An explicit Duffin–Schaeffer function has divergent mass

Define a nonnegative function on positive integers by
\[
\Delta(d)=\frac1{u^2m^2}\quad\text{when }d=gm\text{ is selected in (8)},
\qquad \Delta(d)=0\text{ otherwise},\qquad \psi(d)=d\Delta(d).
\tag{10}
\]
The uniqueness and disjointness above make this a single well-defined function; no supremum is silently exchanged with a sum. Since \(d\le um\), \(\psi(d)\le1/d\).

The totient-weighted contribution of block \(j\) is exactly
\[
M_j:=\sum_{d\text{ in block }j}\frac{\varphi(d)\psi(d)}d
=\frac1u\sum_{m=u}^{L_j}\frac{\varphi(m)}{m^2},
\tag{11}
\]
with an empty sum interpreted as zero. Let \(H_N=\sum_{k\le N}1/k\). The classical identity \(\sum_{d\mid k}\varphi(d)=k\) gives
\[
H_L=\sum_{d\le L}\frac{\varphi(d)}{d^2}
\sum_{k\le L/d}\frac1{k^2}
\le\zeta(2)\sum_{d\le L}\frac{\varphi(d)}{d^2}.
\tag{12}
\]
Also \(\sum_{m<u}\varphi(m)/m^2\le H_{u-1}\). When \(L_j<u\), the difference of these two initial sums is nonpositive, so the following lower bound remains valid in that case as well:
\[
M_j\ge\frac1u\left(\frac{H_{L_j}}{\zeta(2)}-H_{u-1}\right)
\ge\frac{\log V}{2\zeta(2)u}
-\left(1+\frac1{2\zeta(2)}\right)\frac{\log u}{u}-\frac1u.
\tag{13}
\]
Here \(H_{L_j}\ge\log(L_j+1)>\tfrac12\log(V/u)\), and \(H_{u-1}\le1+\log u\). Since the convergent denominators grow at least at Fibonacci rate,
\[
\sum_j\frac{1+\log Q_j}{Q_j}<\infty.
\]
Thus \(\mathcal B_1(\alpha)=\infty\) forces
\[
\boxed{\sum_{d\ge1}\frac{\varphi(d)\psi(d)}d
=\sum_jM_j=\infty.}
\tag{14}
\]
This removes the totient loss left by applying the metric theorem only to reduced fractions with the *original* denominators \(um\). It covers arbitrarily slow Brjuno divergence and denominators with many prime factors.

## 4. Infinitely many reduced approximations lift to distinct large summands

Apply the Duffin–Schaeffer theorem of Koukoulopoulos–Maynard, [Theorem 1, p. 253](https://annals.math.princeton.edu/wp-content/uploads/annals-v192-n1-p05-s.pdf), to (10)–(14). For almost every \(\beta\in[0,1]\), infinitely many coprime pairs \((a,d)\) satisfy
\[
\left|\beta-\frac ad\right|\le\frac{\psi(d)}d
=\frac1{u^2m^2}.
\tag{15}
\]
Multiplication by \(n=um\) gives
\[
\|n\beta\|\le\left|n\beta-\frac ug a\right|\le\frac1n,
\tag{16}
\]
since \((u/g)a\) is an integer. The denominators \(d\) are unbounded, and \(n\ge d\); hence infinitely many distinct original indices \(n\) occur. Reuse of one \(n\) at several divisors cannot invalidate this conclusion. Combining (7) and (16) proves (3), and then divergence of (1). Integer periodicity supplies the result on \((1,2)\) and any other unit interval.

The load-bearing metric input is a theorem for arbitrary nonnegative \(\psi\); no monotonicity, independence of return events, or unjustified converse to Tonelli is used. The proof applies a reduced-fraction theorem to deliberately constructed reduced denominators, then lifts them back to the original return indices.

## 5. Retain the physical target and every component norm

NB-356 identifies the finite-series condition with exact target membership. Its normalization is
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\qquad
\mathcal Mt=Bb/s,\qquad b=B(1)>0,
\qquad
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})},
\tag{17}
\]
where \(H^2=H^2(\Re s>1/2)\) has boundary squared norm \((2\pi)^{-1}\int|F(1/2+iy)|^2dy\). Removing the common inner factor \(B\) on its range is isometric. At the nonzero zero lattice \(z_k=1+2\pi ik/\log q\) of \(\Theta_q\),
\[
|b/z_k|^2\asymp k^{-2},\qquad
|\Theta_p(z_k)|^2+|\Theta_{q^\beta}(z_k)|^2
\asymp\delta_{|k|}^2+\||k|\beta\|^2.
\]
The sampler is bounded and onto \(\ell^2\), with an explicit bounded right inverse. Its minimum-norm split of these target samples constructs the two non-anchor components when (1) is finite. Dividing the remaining vanishing numerator by the pure Blaschke factor \(\Theta_q\) supplies the anchor component. In particular NB-360 proves, uniformly on \(\beta\in[1,2]\),
\[
cS_\alpha(\beta)\le E_3(\beta)\le C(1+S_\alpha(\beta)),
\tag{18}
\]
where \(E_3\) is the infimum of the sum of **all three squared physical component norms**, and equals infinity when no exact decomposition exists. The upper bound is constructive on the finite-series set; the anchor norm is included. The removable point \(s=1\) is not a zero. This proves (4) without discarding the target or assuming RH.

## Consequences, prior art, and boundaries

The missing converse to NB-362 is now settled for every irrational fixed pair. There are precisely two generic regimes, distinguished by the ordinary Brjuno sum. NB-361's 2-Brjuno necessary condition still addresses a different question: whether *any* third seed completes the pair. In the 2-Brjuno but non-Brjuno regime, completion has measure zero, but emptiness or existence of exceptional completing seeds remains undecided here. The classification does not add a moment or tail estimate for finite completion costs.

The metric theorem and rational-reduction principle are classical. Koukoulopoulos–Maynard's [Theorem 2 and Section 2](https://annals.math.princeton.edu/wp-content/uploads/annals-v192-n1-p05-s.pdf) give Catlin's non-reduced criterion; the construction (8)–(14) is an explicit disjoint-block way to recover the relevant mass. Their p. 254 also records Vaaler's earlier case \(\psi(d)=O(1/d)\), which includes (10). No new metric approximation theorem is claimed. The scalar delta is the full Brjuno lower bound for this fixed-coordinate reciprocal series; the Nyman delta is the resulting exact generic physical membership classification.

Lee–Marmi–Petrykiewicz–Schindler, [Section 1.1 and equation (1.4)](https://link.springer.com/article/10.1007/s00010-023-00967-w), supplies the classical Brjuno terminology. Beresnevich–Ramírez–Velani, [*Metric Diophantine Approximation: aspects of recent work*, Section 4.5](https://arxiv.org/pdf/1601.01948), supplies the neighboring simultaneous-approximation-on-fibers setting. Its general fiber questions are not being claimed solved: (3) concerns one fixed rate and a particular continued-fraction criterion. Burnol's [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055) supplies the common inner factor and target projection; the interpolation bridge is already proved in NB-356. The argument is a derived specialization of those tools. No bibliographic priority is inferred from a search failing to find this formulation.

- Positive-measure completion, on any parameter subset, is now equivalent to almost-everywhere completion and to the Brjuno condition. This does not turn a single completing seed into a positive-measure set.
- Even in the Brjuno regime, rational \(\beta\) fail the series test by the convergent-denominator obstruction on a rational sublattice. Full measure never means every seed.
- The null set depends on the fixed irrational pair. The theorem gives no conclusion for a specified arithmetic triple such as \(2,3,5\), nor a uniform statement across all fixed pairs on one common exceptional set.
- Closed real-dilation orbit vectors may require infinitely many generators. No finite-section rate, bounded dilation range, or absolute-coefficient budget follows.
- Every orbit sum \(w\) still satisfies \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The Burnol floor is unchanged; there is no zeta-zero exclusion or RH conclusion.

Evidence is the analytic proof and the inspected primary metric theorem. Ephemeral exact checks passed 24,576 instances of (9), 170 reduced-block mass identities (12,861 distinct-denominator controls), and 647 continued-fraction return controls. They test the finite arithmetic mechanism, not almost-everywhere convergence or any infinite limit. The decisive audits are the gcd uniqueness in (8), disjointness after reduction, the summable cost of excluding \(m<u\), correct metric normalization \(\psi(d)/d\), and unbounded original indices after lifting. No Lean verification or independent adversarial approval is asserted.
