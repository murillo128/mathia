# WI-472 — log-distance decay enlarges the Euler sampling test class

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-FUNCTIONAL-CALCULUS-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-469](WI-469-gevrey-cutoffs-admit-the-full-first-euler-sampling-correction.md), for the fourth-logarithmic-moment arithmetic interface; [WI-464](WI-464-full-euler-correction-has-an-integrable-threshold-primitive.md), for identification of the scalar correction. [WI-471](WI-471-full-euler-response-has-no-unrestricted-smooth-wiener-calculus.md) supplies the separate obstruction to unrestricted smooth composition.

## Claim and mathematical delta

Fix `sigma>1` and `r>0`, and put

\[
 D=\min\{\sigma+r,\,2\sigma-1\}>\sigma.
 \tag{1}
\]

Every fixed periodic Gevrey scalar test of order `1<s<D` has the full
first Euler zero-sampling correction, with error `O(T/log T)`. In
particular the preceding sufficient restriction `s<sigma` is not sharp.
The gain uses the response kernel's actual decay in log-distance,
rather than treating all its entries as bounded by one.

More precisely, for `U=2+|t|` define

\[
 \Phi(U)=
 \begin{cases}
 U^{1/D},&r\ne\sigma-1,\\
 (U\log U)^{1/D},&r=\sigma-1.
 \end{cases}
 \tag{2}
\]

The full response and its original-normalization cutoff panels satisfy

\[
 \boxed{\|e^{itQ}\|_{[4]},\quad
       \sup_{M\ge2}\|e^{itQ_M}\|_{[4]}
       \le \exp\{K_{\sigma,r}\Phi(2+|t|)\}.}
 \tag{3}
\]

This also gives a sufficient endpoint Fourier-decay condition, stated
below. Neither `D` nor the logarithm on the separating parameter line
is claimed to be optimal for the full exponential norm. All source and
test parameters are fixed before the sampling height tends to infinity.
This is an enlargement of a coefficient certificate and its fixed-test
arithmetic consequence, not a hard-threshold or individual-zero theorem.

## Object and norms

On the product prime torus with probability Haar measure `m`, set

\[
 A=\sum_{n\ge2}\Lambda(n)n^{-\sigma},\qquad
 a_n=\Lambda(n)n^{-\sigma}/A,\qquad
 G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r},
\]
\[
 Q(z)=\sum_{n,m\ge2}a_na_mG_r(n,m)\chi_{n/m}(z),\qquad
 \chi_u(z)=\prod_p z_p^{\nu_p(u)}.
 \tag{4}
\]

Only prime powers occur. The Gram realization gives `0<=Q<=q_*=Q(1)<=1`.
Let `Q_M` retain `n,m<=M` without renormalizing `a_n`. Coefficients of
both `Q_M` and `Q-Q_M` are nonnegative after equal characters are
collected. For a reduced positive rational `u=a/b`, write `H(u)=ab` and

\[
 \|F\|_{\mathcal A}=\sum_u|\widehat F(u)|,\qquad
 \|F\|_{[4]}=\sum_u|\widehat F(u)|(1+\log H(u))^4.
 \tag{5}
\]

Here `mathcal A` denotes the unweighted Wiener algebra, not the scalar
normalization `A`. The height inequality `H(uv)<=H(u)H(v)` makes (5)
Banach algebra norms. Both `Q` and its panels belong to the weighted
algebra, and `Q_M->Q` there: dominate the double sum by the product of
the convergent sums `sum_n a_n(1+log n)^4`. No conditional rearrangement
is needed.

## The kernel changes the omitted coefficient mass

The classical bounds `psi(x)=sum_(n<=x) Lambda(n)=O(x)` and
`pi(x)=O(x/log x)` suffice. For `n>=m`,

\[
 0<G_r(n,m)=(m/n)^r[1-m^{-2r}]\le(m/n)^r.
 \tag{6}
\]

Hence the unweighted tail mass `b_M=||Q-Q_M||_mathcal A` obeys

\[
 b_M\le\frac2{A^2}\sum_{n>M}\Lambda(n)n^{-\sigma-r}
               \sum_{2\le m\le n}\Lambda(m)m^{r-\sigma}.
 \tag{7}
\]

This covers both ordered halves, including the diagonal. Partial
summation with `psi(x)=O(x)` gives

\[
 \sum_{m\le n}\Lambda(m)m^{r-\sigma}\ll_{\sigma,r}
 \begin{cases}
 1,&r<\sigma-1,\\
 \log(2n),&r=\sigma-1,\\
 n^{r-\sigma+1},&r>\sigma-1.
 \end{cases}
 \tag{8}
\]

For the first case the infinite sum converges; in the last case the
exponent `r-sigma` is greater than `-1`, so the Stieltjes integral is
bounded by the displayed power even when that exponent is negative.
Applying partial summation again to the outer tail gives

\[
 \boxed{b_M\ll_{\sigma,r}
 \begin{cases}
 M^{1-D},&r\ne\sigma-1,\\
 M^{1-D}\log(2M),&r=\sigma-1.
 \end{cases}}
 \tag{9}
\]

The two regimes have different causes. When `r<sigma-1`, bounded
inner mass leaves the distant-pair exponent `sigma+r`. When
`r>sigma-1`, the growing inner sum leaves the two-tail exponent
`2sigma-1`. The harmonic inner sum at equality must not be replaced by
a bounded one. No prime number theorem, zero-density hypothesis or
short-interval prime estimate is used.

## A polynomial logarithmic weight need not enter the exponential cost

Let `B` be any element of (5), and put `b=||B||_mathcal A`,
`w=||B||_[4]`. For integers `k>=1`,

\[
 \|B^k\|_{[4]}\le k^4w b^{k-1}.
 \tag{10}
\]

Indeed, for a product of `k` characters with logarithmic heights
`ell_1,...,ell_k>=0`,

\[
 (1+\log H(u_1\cdots u_k))^4
 \le\Big(\sum_{i=1}^k(1+\ell_i)\Big)^4
 \le k^3\sum_{i=1}^k(1+\ell_i)^4.
 \tag{11}
\]

Sum against the absolute coefficient products and then use the triangle
inequality after collection. Expanding the exponential, for `x=|t|b`,

\[
 \|e^{itB}\|_{[4]}
 \le1+|t|w e^x(1+7x+6x^2+x^3).
 \tag{12}
\]

The identity follows by summing `sum_(k>=1) k^4 x^(k-1)/k!`;
it also holds at `b=0`, when `B=0`. In particular, for every tail
`B=Q-Q_M`, both `b,w` are bounded by source-dependent constants, so

\[
 \|e^{it(Q-Q_M)}\|_{[4]}
 \le C_{\sigma,r}(1+|t|)^4 e^{|t|b_M}.
 \tag{13}
\]

Thus the fourth logarithmic moment costs a polynomial factor. Using
`exp(|t| ||Q-Q_M||_[4])` would unnecessarily put its logarithmic tail
losses into the leading exponent.

## Counting prime coordinates and balancing the two costs

For completeness retain the dimension dependence of the finite-panel
complex-strip estimate. Put `d=pi(M)`. For some fixed `rho_0>0`,

\[
 |\operatorname{Im}Q_M(\theta+iy)|\le C_{\sigma,r}\rho
 \quad\text{when }\max_p|y_p|\le\rho\le\rho_0.
 \tag{14}
\]

To check this uniformly in `M`, the exponent vector of `n/m` has
length at most `(log n+log m)/log 2`. Take
`rho_0< (sigma-1)log 2`. The difference from the real-angle polynomial
is at most

\[
 \frac{\rho}{\log2}\sum_{n,m}a_na_m
    (\log n+\log m)(nm)^{\rho_0/\log2}<C_{\sigma,r}\rho.
 \tag{15}
\]

This uses the holomorphic Laurent extension, not a squared Hilbert
norm evaluated off the torus. Set `rho=min(rho_0,1/U)`. Moving the
Fourier contours by the signs of their exponent coordinates gives
`|widehat(exp(it Q_M))(k)|<=C exp(-rho |k|_1)`. Since
`log H(chi_k)<=|k|_1 log M`, product geometric sums give

\[
 \|e^{itQ_M}\|_{[4]}
 \le C(CU)^d(1+C dU\log M)^4.
 \tag{16}
\]

For example, the geometric normalizing mass is at most `(C/rho)^d`;
the fourth moment of `|k|_1` under its normalized product law is at
most `C d^4 rho^(-4)`. Constants in (14)–(16) do not depend on `d`.
The dimension factor itself has not been suppressed.

Choose an integer `M_0` comparable to `Phi(U)`, with `M_0>=3`.
Then `log M_0` is comparable to `log U`, with fixed source-dependent
constants. The Chebyshev bound `d<=C M_0/log M_0` makes the logarithm
of (16) at `M_0` at most `C M_0`. Equation (9) gives

\[
 |t|b_{M_0}\le C M_0
 \tag{17}
\]

in both cases of (2). At equality, the factor `log M_0` is paid by
`M_0^D` being comparable to `U log U`.

In the commutative coefficient algebra,
`exp(itQ)=exp(itQ_(M_0)) exp(it(Q-Q_(M_0)))`. Combining (13),
(16) and (17), and absorbing `O(log U)` polynomial costs into
`C Phi(U)`, proves the full-series bound (3).

For a cutoff panel `Q_M`, use the same split if `M>=M_0`; its tail
coefficient masses in both norms are bounded by those of `Q-Q_(M_0)`.
If `M<M_0`, use (16) directly and bound its dimension and `log M`
by the corresponding quantities at `M_0`. This proves the uniform
panel statement in (3). Neither the contour argument nor the tail
estimate has a hidden constant depending on the panel.

## Scalar test class and arithmetic conclusion

Write a four-periodic test as
`f(x)=sum_(j in Z) c_j exp(i pi jx/2)`. A sufficient condition is

\[
 \sum_j |c_j|\exp\{K_{\sigma,r}\Phi(2+\pi|j|/2)\}<\infty,
 \tag{18}
\]

with `K` chosen for (3). It follows that `f(Q)` belongs to (5), and
`f(Q_M)->f(Q)` there by dominated summation and algebra continuity.
In particular (18) holds whenever

\[
 |c_j|\le C_f e^{-c_f|j|^{1/s}},\qquad 1<s<D.
 \tag{19}
\]

The strict power gap absorbs the logarithm in (2). If `r!=sigma-1`,
(18) also holds at `s=D` when the Fourier-decay constant is sufficiently
large relative to the fixed source constant and period. Thus every
Gevrey-Beurling test of order `D` is covered off that parameter line;
no claim for all Gevrey-Roumieu tests at the endpoint follows. On the
line itself (18) retains the extra logarithm.

Let `D_T=N(2T)-N(T)` count all nontrivial zero ordinates with
multiplicity, and evaluate the response along `z_p(t)=exp(-it log p)`.
WI-469's fourth-logarithmic-moment interface now gives

\[
 \boxed{\sum_{T<\gamma\le2T}f(Q(\gamma))
 =D_T\int f(Q)\,dm+\frac{T}{2\pi}\mathcal L(f)
       +O_{f,\sigma,r}(T/\log T),}
 \tag{20}
\]

where `mathcal L(f)=-integral_0^(q_*) f'(x)C(x)dx` uses WI-464's
integrable cumulative coefficient. To check the inherited arithmetic
gate, truncate reduced rational characters at
`H<=exp(sqrt(log T))`. Ford–Meng–Zaharescu's Lemmas 1–2 apply in that
range. Their individual ordinate-comparison errors cost
`(log H)^2/log T`; the weighted tail has mass `O((log T)^(-2))`,
which remains `O(1/log T)` after multiplying by `D_T/T=O(log T)`.
Rational separation bounds the nonresonant Landau terms. This is the
same arithmetic theorem as WI-469, with an enlarged composition class.

The correction equals the continuous coefficient functional
`-sum_u widehat(f(Q))(u) kappa(u)`, where `kappa(p^j)=kappa(p^(-j))`
`=(log p)p^(-j/2)` and `kappa` is zero elsewhere. This bounded
functional passes through the weighted panel limit. At each finite
panel Haar orthogonality identifies it with
`-integral f'(x)C_M(x)dx`; WI-464's `L^1` convergence identifies the
limit. The Haar mean in (20) can also be replaced by
`T^(-1) integral_T^(2T) f(Q(t))dt`, using WI-469's mean error
`O(||f(Q)||_[4]/(log T)^2)`.

## Prior art, controls and remaining boundary

Rosser–Schoenfeld, *Approximate formulas for some functions of prime
numbers*, **Illinois J. Math. 6** (1962), 64–94,
[Corollary 1, (3.6), and Theorem 12, (3.35)](https://doi.org/10.1215/ijm/1255631807),
give stronger explicit forms of the two classical Chebyshev bounds
used in (8) and (16). No improvement in prime counting is asserted.

Dasgupta–Ruzhansky, *Gevrey functions and ultradistributions on compact
Lie groups and homogeneous spaces*, **Bull. Sci. Math. 138** (2014),
756–782, [Theorem 2.3](https://arxiv.org/pdf/1208.1883), supplies the
classical Fourier characterizations of the Roumieu and Beurling
classes. The arithmetic input remains Ford–Meng–Zaharescu,
*Simultaneous distribution of the fractional parts of Riemann zeta
zeros*, **Bull. London Math. Soc. 49** (2017), 1–9,
[Lemmas 1–2](https://arxiv.org/pdf/1511.06814).

Nonanalytic calculus in weighted group algebras is established
background, as recorded in WI-469. The convolution-moment inequality
(10) is elementary weighted-algebra calculus; finite-coordinate
contour bounds and head/tail balancing are also classical methods.
The local contribution is retaining this response's log-distance
kernel in (7), paying the logarithmic coefficient weight outside the
tail exponential, and obtaining (3) and the larger range (1).
No general functional-calculus theorem or literature priority is claimed.

The self-audit boundaries are:

- The exponent is a sufficient upper bound. WI-471's superpolynomial
  lower bound remains compatible with it and still excludes an
  unrestricted smooth Wiener calculus. There is no matching
  stretched-exponential lower bound here.
- The diagonal is included in (7); positivity and collection of equal
  rational characters justify domination of every omitted panel.
  Cutting prime powers and then renormalizing would change the object.
- Constants are fixed in `sigma,r`. The constants for the strict
  regimes in (8) can diverge as `r` approaches `sigma-1`. Limits toward `sigma=1` or `r=0`
  are not uniform, and `r=0` itself makes the response zero.
- Prime-only responses retain the improved norm bounds but their
  prime-axis correction is zero by common-rotation invariance.
  Diagonal-only responses are constant. Better composition estimates
  do not manufacture an arithmetic bias.
- Exact-plateau Gevrey cutoffs with fixed transition widths are
  covered, but (18) need not remain bounded as a width shrinks.
  No indicator limit, moving-test theorem, or scalar total-variation
  bound on the actual zero-sampling residual has been established.
- The sampling statistic counts all zero ordinates with multiplicity.
  This enlargement of its test class supplies no observable isolating
  a fixed off-critical mirror block and no RH or simplicity conclusion.

The investigation closes at a source-sensitive sufficient test class.
The kernel and convolution estimates were derived analytically and the
external theorem hypotheses were checked; no numerical zero experiment,
Lean proof or independent adversarial certification is claimed. No
separate bounded formalization target with a material verification or
fertility advantage is selected from this estimate.
