# NB-363 — Logarithmic orbit cost is equivalent to exponential completion budgets

- **Status:** proved (classical tools plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-356 for exact orbit membership; NB-357 and NB-359 for the two-cutoff physical-energy comparison; NB-360 for the uniform three-component budget comparison
- **Classification:** EXACT-DERIVED + LITERATURE+DERIVED + QUANTITATIVE-TARGET-CLASSIFICATION

## Claim and scope

The rate of two-orbit approximation determines a precise tail-integrability class for exact completion by a varying third real seed. In particular, logarithmic two-orbit squared energy is equivalent to an exponentially integrable three-orbit squared-energy budget. Almost-everywhere completion alone does not imply this stronger budget property.

Fix real seeds \(p,q>1\) with irrational \(\alpha=\log p/\log q\). In \(H=L^2(0,1;dx)\), set
\[
e=1,\qquad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\qquad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},
\]
\[
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\},
\qquad \mathcal N=\overline{\operatorname{span}}\{g_v:v>1\},
\qquad t=P_{\mathcal N}e.
\]
Write
\[
\delta_n=\|n\alpha\|_{\mathbb R/\mathbb Z},\qquad
W(N)=\sum_{n\le N}\frac1{n^2\delta_n^2},\qquad
S(\beta)=\sum_{n\ge1}\frac1{n^2(\delta_n^2+\|n\beta\|^2)}.
\tag{1}
\]
The parameter \(\beta\) varies with Lebesgue measure on \((1,2)\), and the third seed is \(q^\beta\). All seeds other than this third seed are fixed before any limit or integration.

Let \(\mathcal E_2(\varepsilon)\) be the infimum of \(\|u_q\|^2+\|u_p\|^2\) over \(u_v\in\mathcal C_v\) with \(\|t-u_q-u_p\|\le\varepsilon\). For every fixed \(\kappa>0\), the following are equivalent:

1. \(W(N)=O((\log(eN))^\kappa)\).
2. For some \(\lambda>0\), \(\int_1^2\exp(\lambda S(\beta)^{1/\kappa})\,d\beta<\infty\).
3. \(\mathcal E_2(\varepsilon)=O((\log(1/\varepsilon))^\kappa)\) as \(\varepsilon\downarrow0\).
4. There is a measurable budget \(K:(1,2)\to[0,\infty]\) and \(\lambda>0\) with \(\int_1^2\exp(\lambda K(\beta)^{1/\kappa})d\beta<\infty\), such that for almost every \(\beta\) there is an exact decomposition
   \[
   t=u_q+u_p+u_{q^\beta},\qquad
   u_v\in\mathcal C_v,\qquad
   \|u_q\|^2+\|u_p\|^2+\|u_{q^\beta}\|^2\le K(\beta).
   \tag{2}
   \]

No measurable choice of the component vectors or regularity of a varying optimizer is assumed. Condition 4 concerns a measurable upper budget for the existence of such vectors. When these conditions hold, one may choose \(K\) with
\[
\operatorname{meas}\{K>R\}\le C\exp(-cR^{1/\kappa})\quad(R\ge1).
\tag{3}
\]
Constants and the admissible exponent \(\lambda\) may depend on the fixed pair and \(\kappa\). No sharp tail constant is asserted.

At \(\kappa=1\), NB-359 identifies the equivalent arithmetic condition
\[
\boxed{\sup_{m\ge1}\frac1m\sum_{j=1}^m a_j^2<\infty,
\qquad \alpha=[a_0;a_1,a_2,\ldots].}
\tag{4}
\]
Thus bounded quadratic mean of the digits characterizes exponential physical completion budgets, not merely a sufficient fractional moment. For \(0<\kappa<1\), none of the four conditions holds for an irrational ratio, by the universal \(W(N)\gg\log N\) return bound in NB-355.

## 1. Physical comparisons retain the target and all components

The two-cutoff bracket of NB-357, reconstructed in NB-359, is
\[
c_1W(c_2/\varepsilon)\le\mathcal E_2(\varepsilon)
\le C_1\bigl(1+W(\lceil C_2/\varepsilon^2\rceil)\bigr).
\tag{5}
\]
Here and below \(W(X)=W(\lfloor X\rfloor)\) for real cutoffs. Since taking either fixed positive power of \(\varepsilon^{-1}\) changes \((\log(1/\varepsilon))^\kappa\) by only a constant factor, (5) proves \(1\Longleftrightarrow3\). Necessity uses \(\varepsilon=c_2/N\); sufficiency uses the upper cutoff. The distinct cutoffs are not identified for arbitrary growth laws.

Let \(E_3(\beta)\) be the infimum of the sum of all three squared component norms in (2), taking value \(+\infty\) when there is no decomposition. The explicit lattice interpolation in NB-356 and NB-360 gives, uniformly on \([1,2]\),
\[
cS(\beta)\le E_3(\beta)\le C(1+S(\beta)).
\tag{6}
\]
The upper bound comes with an actual decomposition when \(S\) is finite, not just an infimum estimate.

In brief, the unitary Mellin model has
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\qquad
\mathcal Mt=Bb/s,\qquad b=B(1)>0,
\qquad \Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})}.
\]
Removing the common inner factor \(B\) is isometric on its range. At the nonzero zeros \(1+2\pi i\ell/\log q\) of \(\Theta_q\), the squared target sample is comparable to \(\ell^{-2}\), and the sum of the other squared factors is comparable to \(\delta_{|\ell|}^2+\||\ell|\beta\|^2\). Bounded lattice sampling gives the lower bound in (6); the bounded right inverse lifts the minimum-norm sample split. Division of the remaining numerator by the pure Blaschke factor \(\Theta_q\) supplies the anchor component with norm at most \(b+\sqrt{2H}\), where \(H\) is the squared norm sum of the two lifted components. This prices all three vectors. The point \(s=1\) is removable and is not a zero.

Consequently \(2\Longrightarrow4\) follows with the measurable explicit certificate \(K=C(1+S)\), decreasing \(\lambda\) as needed. Conversely, any budget in 4 obeys \(cS\le K\) almost everywhere, so \(4\Longrightarrow2\). This argument does not need measurability of \(E_3\) itself.

## 2. A logarithmic prefix bound gives a stretched-exponential tail

Assume \(W(N)\le A(\log(eN))^\kappa\) for all integers \(N\ge1\), enlarging \(A>0\) to include initial terms. Put
\[
S_{\le N}(\beta)=\sum_{n\le N}\frac1{n^2(\delta_n^2+\|n\beta\|^2)},
\qquad T_N=S-S_{\le N}.
\]
Pointwise \(S_{\le N}\le W(N)\). Haar invariance under multiplication by \(n\) and Tonelli give
\[
\begin{aligned}
\int_1^2T_N(\beta)d\beta
&=\sum_{n>N}\frac{2}{n^2\delta_n}\arctan\frac1{2\delta_n}\\
&\le\pi\sum_{n>N}\frac1{n^2\delta_n}.
\end{aligned}
\tag{7}
\]
The initially extended-valued integrals are legitimate by positivity. For each dyadic block \(M<n\le2M\), Cauchy--Schwarz yields
\[
\begin{aligned}
\sum_{M<n\le2M}\frac1{n^2\delta_n}
&\le\left(\sum_{M<n\le2M}\frac1{n^2\delta_n^2}\right)^{1/2}
\left(\sum_{M<n\le2M}\frac1{n^2}\right)^{1/2}\\
&\le\sqrt{\frac{A}{M}}(\log(2eM))^{\kappa/2}.
\end{aligned}
\tag{8}
\]
Summing at \(M=2^jN\) proves
\[
\int_1^2T_N\le C_\kappa\sqrt A\,
\frac{(\log(eN))^{\kappa/2}}{\sqrt N}.
\tag{9}
\]
Indeed \(\log(2e2^jN)\le(1+(j+1)\log2)\log(eN)\), and the remaining series is bounded by a constant times \(\sum_{j\ge0}2^{-j/2}(j+2)^{\kappa/2}<\infty\).

For sufficiently large \(R\), set
\[
x=(R/(2A))^{1/\kappa},\qquad N=\lfloor e^{x-1}\rfloor.
\]
Then \(W(N)\le R/2\) and \(N\ge\tfrac12e^{x-1}\). If \(S>R\), necessarily \(T_N>R/2\). Markov and (9) imply
\[
\operatorname{meas}\{S>R\}
\le C_{A,\kappa}R^{-1/2}
\exp\left(-\tfrac12(R/(2A))^{1/\kappa}\right).
\tag{10}
\]
In particular \(S<\infty\) almost everywhere. With \(Y=S^{1/\kappa}\), (10) bounds \(\operatorname{meas}\{Y>y\}\) by \(Ce^{-cy}\) for large \(y\). The layer integral
\[
\int_1^2e^{\lambda Y}d\beta
=1+\lambda\int_0^\infty e^{\lambda y}\operatorname{meas}\{Y>y\}dy
\]
is finite for sufficiently small positive \(\lambda\). This proves \(1\Longrightarrow2\), and (3) follows from the explicit budget in (6). No phase independence, cancellation, or metric divergence theorem is used.

## 3. Near one, all prefix obstructions align

The converse must retain simultaneous alignment of the entire prefix. A lower bound from one unusually good convergent alone would miss cumulative cost.

Fix \(N\ge1\) and abbreviate \(W=W(N)\). Since \(\delta_1\le1/2\), \(W\ge4\). Every \(n\le N\) satisfies
\[
\delta_n\ge\frac1{n\sqrt W}.
\]
Put \(h_N=1/(N^2\sqrt W)\le1/2\). If \(\beta=1+u\) with \(0<u<h_N\), then
\[
\|n\beta\|=\|nu\|\le nu
\le\frac{n}{N^2\sqrt W}
\le\frac1{n\sqrt W}\le\delta_n\qquad(n\le N).
\]
Hence, for **every irrational** \(\alpha\),
\[
\boxed{S(\beta)\ge\tfrac12W(N)\text{ on }(1,1+h_N),\qquad
\operatorname{meas}\{S\ge W(N)/2\}\ge\frac1{N^2\sqrt{W(N)}}.}
\tag{11}
\]
No Diophantine-type assumption or equidistribution input is needed. This is a positive-measure obstruction even though the exactly repeated seed at \(\beta=1\) lies outside the integration interval.

Suppose condition 2 holds, and denote its finite integral by \(M\). Applying (11) gives
\[
M\ge\frac1{N^2\sqrt W}
\exp\bigl(\lambda(W/2)^{1/\kappa}\bigr),
\]
so
\[
\lambda2^{-1/\kappa}W^{1/\kappa}
\le\log M+2\log N+\tfrac12\log W.
\tag{12}
\]
For fixed \(\lambda,\kappa>0\), \(\log W=o(W^{1/\kappa})\). Absorbing half of the left side in (12), and handling bounded \(W\) by increasing a constant, proves
\[
W(N)^{1/\kappa}\le C(1+\log N).
\]
This is condition 1 and completes the equivalence. In particular, no measurable alternative construction of the physical components can evade the lower bound by improving the interpolation certificate: the lower comparison in (6) applies to every decomposition.

## 4. Endpoint and strict controls

NB-359's continued-fraction block estimates identify \(W(N)=O(\log N)\) with (4). Its unbounded-digit example
\[
a_j=2^k\text{ if }j=4^k\ (k\ge1),\qquad a_j=1\text{ otherwise}
\]
has \(\sum_{j\le m}a_j^2\le7m/3\). Thus exponential completion budgets extend beyond bounded partial quotients.

For the other explicit ratio \(\alpha_*=[0;1,2,3,\ldots]\), NB-359 proves
\[
W(N)\asymp\left(\frac{\log N}{\log\log N}\right)^3.
\tag{13}
\]
It follows that \(S\) admits a finite moment \(\int\exp(\lambda S^{1/3})\) for some \(\lambda>0\), but admits none of the form \(\int\exp(\lambda S^r)\) with \(r>1/3\) and \(\lambda>0\). The same existence/impossibility statement holds for physical budgets in (2). Indeed apply the equivalence with \(\kappa=1/r\); (13) is bounded by \((\log N)^3\), but not by any smaller positive power. This specifies the sharp **power exponent** in this example, not a sharp logarithmic refinement or tail constant.

These controls separate mere finite-energy completion from its quantitative budget distribution. NB-360 supplies a finite positive power moment for every fixed finite-type pair; NB-362 admits still more pairs through Brjuno summability. Neither implies the exponential endpoint characterized here. Conversely, the theorem does not classify all fixed ratios admitting almost-everywhere completion.

## Prior art, mathematical delta, and limits

Borda, *Optimal and typical L2 discrepancy of 2-dimensional lattices*, Ann. Mat. Pura Appl. 203 (2024), 2157–2184, [Theorem 1 and Section 2.2](https://link.springer.com/article/10.1007/s10231-024-01440-4), gives the established bounded-quadratic-mean criterion in discrepancy theory. His *On the theorem of Davenport and generalized Dedekind sums*, [Section 4 and Theorem 3](https://arxiv.org/pdf/1606.07946), treats the reciprocal-power sums behind it. The scalar digit boundary is prior art and was already transferred to two-orbit physical cost in NB-359.

Beresnevich, Haynes and Velani, *Sums of reciprocals of fractional parts and multiplicative Diophantine approximation*, [Section 2.2, Theorem 2.2](https://arxiv.org/pdf/1511.06862), is neighboring fixed-coordinate metric prior art. Its convergence result concerns multiplicative inequalities. The present Euclidean-denominator exponential moment and its converse are proved directly in (7)–(12); neither that metric theorem nor an independence assumption supplies them.

The mathematical delta is the two-way conversion between logarithmic-power approximation cost and stretched-exponential **physical completion budgets**, including the necessity forced by a common near-rational interval. The exact membership test, Hardy lift, classical digit criterion, and elementary probability inequalities are reused tools. This is a derived quantitative consequence for the Nyman family, with no claim of a new general interpolation or Diophantine theory based on absence of a search match.

- All costs are sums of squared norms of full closed real-dilation orbit vectors. No finite generator count, dilation range, absolute-coefficient bound, or discrete Nyman-section rate is obtained.
- With \(b=B(1)\), every admissible sum \(w\) satisfies \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The Burnol floor and its unknown zero information remain. There is no RH or zero-exclusion conclusion.
- No digit criterion is proved for a specified integer log ratio, and no completion statement is proved for a specified integer third seed. Countable arithmetic choices can belong to the exceptional set.
- The exponential conclusion concerns the whole unit interval of third-seed ratios. Its converse uses intervals adjacent to \(1\); restricting the parameter to an arbitrary smaller set requires a separate argument.
- The existence of a positive exponential parameter is classified; its largest value and the exact distribution of the minimum physical energy are not computed. Dense rational cost blowup from NB-360 remains compatible with (3).

Evidence is the analytic proof and the inspected primary literature. An ephemeral exact-rational stress check passed 210 prefix-alignment cases and 42 dyadic Cauchy–Schwarz cases across six rational controls with no vanishing sampled phase. Those checks validate only finite inequalities, not irrational limits or moment convergence. Decisive audits are the squared-norm convention, the whole-prefix interval in (11), absorption of its logarithmic width in (12), and pricing the anchor component in (6). No Lean verification or independent adversarial approval is asserted.
