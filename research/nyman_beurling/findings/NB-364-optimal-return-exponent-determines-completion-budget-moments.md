# NB-364 — Optimal return exponent determines completion-budget moments

- **Status:** proved (classical tools plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-356 and NB-360 for exact orbit membership and uniform full-component cost; NB-358 for the two-orbit energy exponent
- **Classification:** LITERATURE+DERIVED + EXACT-MOMENT-THRESHOLD + ENDPOINT-CONTROL

## Claim and scope

The optimal Diophantine return exponent of a fixed seed pair determines the sharp open range of power moments for its three-orbit completion budgets. At the first-moment boundary, the exponent alone is insufficient: a classical continued-fraction series decides whether a finite mean physical budget exists.

Fix real seeds \(p,q>1\), with irrational \(\alpha=\log p/\log q\). In \(H=L^2(0,1;dx)\), put
\[
e=1,\quad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\quad
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\}.
\]
Let \(\mathcal N=\overline{\operatorname{span}}\{g_v:v>1\}\), \(t=P_{\mathcal N}e\), and
\[
\delta_n=\|n\alpha\|_{\mathbb R/\mathbb Z},\qquad
\omega=\limsup_{n\to\infty}\frac{-\log\delta_n}{\log n}.
\tag{1}
\]
Assume \(1\le\omega<\infty\). This is the **optimal** exponent, not an arbitrary exponent in a known lower bound. Define
\[
s_*=
\begin{cases}
\infty,&\omega=1,\\
\displaystyle\frac{\omega}{2(\omega-1)},&\omega>1.
\end{cases}
\tag{2}
\]
A measurable budget \(K:(1,2)\to[0,\infty]\) is admissible if, for almost every \(\beta\), there exist vectors
\[
t=u_q+u_p+u_{q^\beta},\qquad u_v\in\mathcal C_v,\qquad
\|u_q\|^2+\|u_p\|^2+\|u_{q^\beta}\|^2\le K(\beta).
\tag{3}
\]
The costs throughout are **sums of squared physical norms**. Then:

1. One explicit admissible budget has finite \(s\)-moment for every \(0<s<s_*\).
2. No admissible budget has finite \(s\)-moment for any \(s>s_*\).
3. For every irrational \(\alpha\), without the finite-\(\omega\) restriction, an admissible budget with finite mean exists exactly when
   \[
   \boxed{\sum_{j\ge1}\frac{Q_{j+1}}{Q_j^2}<\infty,}
   \tag{4}
   \]
   where \(P_j/Q_j\) are the regular continued-fraction convergents, \(Q_{-1}=0,Q_0=1\).

The first two assertions leave the single endpoint \(s=s_*\) undecided. At \(\omega=2\), (4) decides that endpoint, and both outcomes occur for explicit ratios with the same exponent. No measurable choice of the component vectors, or measurability of an optimizer, is assumed.

## 1. The physical lift reduces the question to one scalar moment

Set
\[
S_\alpha(\beta)=\sum_{n\ge1}
\frac1{n^2(\delta_n^2+\|n\beta\|^2)},\qquad 1<\beta<2.
\tag{5}
\]
NB-356 and NB-360 give constants \(c,C>0\), independent of \(\beta\in[1,2]\), with the following two properties:

- Every exact decomposition in (3) has total squared norm at least \(cS_\alpha(\beta)\).
- If \(S_\alpha(\beta)<\infty\), there is an exact decomposition with total squared norm at most \(C(1+S_\alpha(\beta))\).

The upper statement is an actual construction. Briefly, in the unitary Mellin model
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\quad
\mathcal Mt=Bb/s,\quad b=B(1)>0,\quad
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})}.
\]
Remove the common inner factor \(B\) isometrically on its range. On the nonzero zero lattice \(z_\ell=1+2\pi i\ell/\log q\) of \(\Theta_q\), target squared samples are comparable to \(\ell^{-2}\), and the squared magnitudes of the other two factors sum to a quantity comparable to \(\delta_{|\ell|}^2+\||\ell|\beta\|^2\). The constants are uniform because \(q\le q^\beta\le q^2\).

Bounded lattice sampling gives the lower cost. The bounded lattice right inverse lifts the minimum-norm sample split to two Hardy vectors of squared norm sum \(H_\beta\le C S_\alpha(\beta)\). The remaining numerator vanishes on every nonzero lattice point, so division by the pure Blaschke factor \(\Theta_q\) gives the anchor component of norm at most \(b+\sqrt{2H_\beta}\). This prices all three components. The removable point \(s=1\) is not a zero.

Consequently, for every \(s>0\),
\[
\boxed{\text{an admissible }K\text{ with }\int_1^2K^s<\infty
\quad\Longleftrightarrow\quad\int_1^2S_\alpha^s<\infty.}
\tag{6}
\]
For sufficiency use the same measurable certificate \(K=C(1+S_\alpha)\) for every exponent; necessity uses \(cS_\alpha\le K\) almost everywhere. This avoids assumptions about a varying minimum-norm optimizer.

## 2. All strictly subcritical moments are finite

Two elementary estimates suffice. For \(s>1/2\) and \(0<a\le1/2\), Haar invariance gives
\[
\begin{aligned}
I_s(a)&:=\int_1^2(a^2+\|n\beta\|^2)^{-s}\,d\beta
=2\int_0^{1/2}(a^2+y^2)^{-s}\,dy,\\
2^{1-s}a^{1-2s}&\le I_s(a)\le D_sa^{1-2s},\qquad
D_s=2\int_0^\infty(1+y^2)^{-s}\,dy<\infty.
\end{aligned}
\tag{7}
\]
The lower bound integrates only over \(0\le y\le a\). No independence between different \(n\) is used.

For every \(v>\omega\), definition (1) supplies \(\gamma>0\) such that \(\delta_n\ge\gamma n^{-v}\) for all \(n\ge1\). If \(a>1\), the weighted return mass satisfies
\[
F_a(x):=\sum_{\delta_n\le x}n^{-a}
\le\zeta(a)(2x/\gamma)^{a/v},\qquad 0<x\le1/2.
\tag{8}
\]
Indeed the first return is at least \((\gamma/x)^{1/v}\), and two returns differ by at least \((\gamma/(2x))^{1/v}\), since
\(\|(n-m)\alpha\|\le2x\). The \(k\)-th return is therefore at least \(k(\gamma/(2x))^{1/v}\). This difference estimate, not just the first-return bound, proves (8).

For \(h>0\), the layer integral now yields
\[
\sum_{n\ge1}n^{-a}\delta_n^{-h}
=2^h\zeta(a)+h\int_0^{1/2}F_a(x)x^{-h-1}\,dx<\infty
\quad\text{when }h<a/v.
\tag{9}
\]

First let \(1/2<s\le1\). Concavity for finite nonnegative sums, (7), and monotone convergence give
\[
\int_1^2S_\alpha^s
\le D_s\sum_{n\ge1}n^{-2s}\delta_n^{-(2s-1)}<\infty
\quad\text{if }2s-1<2s/v.
\tag{10}
\]
For \(s\ge1\), use Minkowski on finite sums instead of the concavity inequality:
\[
\|S_\alpha\|_{L^s(1,2)}
\le D_s^{1/s}\sum_{n\ge1}n^{-2}\delta_n^{-(2-1/s)}<\infty
\quad\text{if }2-1/s<2/v.
\tag{11}
\]
Uniform bounds on the partial sums justify the infinite version by monotone convergence. Both conditions are exactly \(2s(1-1/v)<1\).

For \(1/2<s<s_*\), choose \(v>\omega\) close enough to \(\omega\) for that strict inequality. When \(\omega=1\), this works for every finite \(s>1/2\). Since \(s_*>1/2\) for finite \(\omega\), some such moment always exists; on the unit-measure interval it also implies all moments \(0<s\le1/2\). This proves assertion 1 through (6), including moments above one which NB-360 did not claim.

## 3. One phase term excludes every supercritical moment

Suppose \(s>1/2\) and \(M=\int_1^2S_\alpha^s<\infty\). For every \(n\), positivity and the lower bound in (7) give
\[
M\ge n^{-2s}I_s(\delta_n)
\ge2^{1-s}n^{-2s}\delta_n^{-(2s-1)}.
\]
Therefore
\[
\boxed{\delta_n\ge
\left(\frac{2^{1-s}}M\right)^{1/(2s-1)}
n^{-2s/(2s-1)}\quad\text{for every }n.}
\tag{12}
\]
In particular \(\omega\le2s/(2s-1)\). If \(\omega>1\), this is equivalent to \(s\le s_*\), proving assertion 2. Thus the upper threshold is forced by a necessary uniform return bound; it is not merely a limitation of the sufficient moment estimate.

For comparison, NB-358 proves that the limsup growth exponent of the two-orbit squared energy \(\mathcal E_2(\varepsilon)\) is
\[
\kappa:=\limsup_{\varepsilon\downarrow0}
\frac{\log(1+\mathcal E_2(\varepsilon))}{\log(1/\varepsilon)}
=2(\omega-1).
\]
For \(0<\kappa<\infty\), the present result reads
\[
s_*=\frac12+\frac1\kappa.
\tag{13}
\]
This relates approximation cost for two physical components to the sharp open moment range for exact completion by a third. It is not an asymptotic tail formula. When \(\kappa=0\), all positive power moments exist, but NB-363 shows that stronger exponential integrability still depends on finer information.

## 4. The mean endpoint is a classical convergent-denominator test

Tonelli and direct integration, valid also when the result is infinite, give
\[
\int_1^2S_\alpha(\beta)\,d\beta
=\sum_{n\ge1}\frac{2}{n^2\delta_n}
\arctan\frac1{2\delta_n}
\asymp\sum_{n\ge1}\frac1{n^2\delta_n}.
\tag{14}
\]
The comparison is uniform because \(0<\delta_n\le1/2\). Rivoal's Lemma 3.2, with reciprocal exponents \((2,1)\), identifies convergence of the last series with (4). The following elementary block argument also reconstructs the exact criterion needed here.

Fix \(j\ge1\), and abbreviate \(d=Q_j,D=Q_{j+1}\). The convergent at \(d\) supplies
\[
\sum_{d\le n<D}\frac1{n^2\delta_n}\ge\frac{D}{d^2},
\tag{15}
\]
since \(\delta_d<1/D\). Partition this range into blocks \(kd\le n<\min((k+1)d,D)\), \(k\ge1\). For \(d>1\), the points in one such block are pairwise separated modulo one by more than \(1/(2d)\), using best approximation for index differences below \(Q_j\). Their ordered distances \(y_1\le y_2\le\cdots\) from zero satisfy \(y_h\ge(h-1)/(4d)\) for \(h\ge2\). Also every \(n<D\) has \(\delta_n\ge\delta_d>1/(D+d)>1/(2D)\). Thus the closest point contributes at most \(2D\) to the reciprocal-distance sum, and all others contribute at most \(4dH_d\), where \(H_d=\sum_{h\le d}1/h\). When \(d=1\), there is just one point per block and the same upper estimate holds. Weighting by \(n^{-2}\le(kd)^{-2}\) and summing in \(k\) gives
\[
\sum_{d\le n<D}\frac1{n^2\delta_n}
\le\zeta(2)\left(\frac{2D}{d^2}+\frac{4H_d}{d}\right).
\tag{16}
\]
The blocks \([Q_j,Q_{j+1})\), \(j\ge1\), are disjoint. The possible duplicate initial denominator \(Q_0=Q_1=1\) is not counted twice. Fibonacci growth implies \(\sum_j H_{Q_j}/Q_j<\infty\); finitely many indices below \(Q_1\) are harmless. Equations (15)–(16) prove the claimed equivalence, and (6), (14) prove assertion 3.

Two endpoint controls show why the exponent does not decide the mean. Define separate continued fractions \(\alpha_\pm=[1;2,a_2,a_3,\ldots]\), with their own denominator recurrences:
\[
\begin{array}{ll}
\alpha_+:&a_{j+1}=Q_j,\\
\alpha_-:&a_{j+1}=\max(1,\lfloor Q_j/j^2\rfloor),
\end{array}\qquad j\ge1.
\tag{17}
\]
For \(\alpha_+\), \(Q_{j+1}/Q_j^2=1+Q_{j-1}/Q_j^2\ge1\), so the mean diverges. For \(\alpha_-\),
\[
\frac{Q_{j+1}}{Q_j^2}\le\frac1{j^2}+\frac2{Q_j},
\tag{18}
\]
so it converges. In the second case \(Q_j/j^2\to\infty\) and \(\log j/\log Q_j\to0\), by Fibonacci growth. Hence \(Q_{j+1}\sim Q_j^2/j^2\); in the first case \(Q_{j+1}\sim Q_j^2\). Both ratios have
\[
\omega=\limsup_j\frac{\log Q_{j+1}}{\log Q_j}=2.
\tag{19}
\]
For completeness the equality in (19) follows from
\((Q_{j+1}+Q_j)^{-1}<\delta_{Q_j}<Q_{j+1}^{-1}\) and \(\delta_n\ge\delta_{Q_j}\) for \(Q_j\le n<Q_{j+1}\). Thus both examples have every moment below one and no moment above one, but only \(\alpha_-\) permits finite mean completion budgets. Their third-seed completion still holds almost everywhere in both cases; an infinite mean is not a nonexistence statement.

## Prior art, mathematical delta, and limits

Rivoal, *On the convergence of Diophantine Dirichlet series*, Proc. Edinburgh Math. Soc. 55 (2012), 513–541, DOI `10.1017/S0013091510001069`, [Lemma 3.2, pp. 523–525](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0A03A2C7A347D4C9E76CF565FDE45DA5/S0013091510001069a.pdf/on-the-convergence-of-diophantine-dirichlet-series.pdf), explicitly gives the scalar continued-fraction criterion used in (14)–(16). That criterion is prior art, not a new number-theoretic result. The block proof here is a self-contained reconstruction of its special case.

Borda's [2024 reciprocal-sums paper, Introduction](https://arxiv.org/pdf/2305.07394), places these weighted sums in the older Hardy–Littlewood/Kruse literature and points to the subsequent Chamizo–Martin general theory. Beresnevich, Haynes and Velani's [Section 2.2, Theorem 2.2](https://arxiv.org/pdf/1511.06862) treats neighboring fixed-coordinate multiplicative approximation; the Euclidean denominator and moment necessity here follow directly from (7)–(12). Burnol's [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055) supply the common inner factor and target projection, already retained by NB-354–NB-360. No new general interpolation or Diophantine theorem is claimed from an absence of search matches.

The local delta is the sharp open moment threshold for **physical completion budgets**, its relation (13) to two-orbit approximation cost, and a complete finite-mean test with opposite endpoint controls. NB-360 supplied only sufficient fractional moments below one from a possibly nonoptimal type bound; NB-363 classifies exponential rather than general power moments. The present necessity also prevents another choice of physical components from evading the threshold.

- Finite \(\omega\) is essential to the positive moment-range assertion. For \(\omega=\infty\), (12) still excludes every moment above \(1/2\), but it gives no positive moment below that value; NB-361 even permits empty completion families.
- No endpoint classification for \(s_*\ne1\), sharp tail asymptotic, or largest exponential parameter is proved. A known nonoptimal logarithmic-forms bound gives only sufficient moments; it does not identify the actual \(\omega\) of a specified integer pair.
- All parameters \(p,q,b\) are fixed. The third seed varies over a real interval; no specified integer third seed is covered by an almost-everywhere statement.
- Full closed real-dilation orbit vectors are priced. There is no bound on finite generator count, dilation range, absolute coefficients, or discrete Nyman-section error.
- For every orbit sum \(w\), \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The common Burnol floor remains, and no value of \(b\), zeta-zero exclusion, or RH conclusion is obtained.

Evidence is the analytic proof and the inspected primary sources. An ephemeral exact-rational check passed the lower bound (15) and the relaxed upper bound (16) with \(\zeta(2)\) replaced by \(2\), across 108 nonterminal continued-fraction blocks and 11,173 integer indices. Those finite controls do not establish irrational limits or moment convergence. Decisive audits are the change from concavity to Minkowski at \(s=1\), use of return differences in (8), the necessary uniform bound (12), and the endpoint summability in (17)–(19). No Lean verification or independent adversarial approval is asserted.
