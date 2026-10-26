# WI-466 — full Euler sampling bias changes sign on increasing tests

**Status:** EXACT-DERIVED + LITERATURE-TRANSPORT + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-464](WI-464-full-euler-correction-has-an-integrable-threshold-primitive.md), for the integrable cumulative coefficient; [WI-465](WI-465-analytic-euler-observables-have-a-full-first-zero-sampling-correction.md), for polynomial arithmetic transport and the negative correction to each fixed positive moment.

## Claim and scope

The negative corrections to all fixed positive moments of the coherent
Euler response do **not** extend to every increasing observable. For
each fixed width `r>0`, and all sufficiently large safe-line parameters
`sigma=1+epsilon`, an explicit increasing quintic has a **strictly
positive** first zero-sampling correction. The full infinite Euler
series, with its original normalization, is used. A sufficient concrete
regime is `r=1, sigma>=100`.

Consequently WI-464's cumulative coefficient `C` has both positive and
negative sets of positive Lebesgue measure in this regime. For each
such fixed pair of parameters, the actual zero-sampled response law and
its Haar law are incomparable in usual stochastic order for every
sufficiently large height. The witnesses are two fixed increasing
polynomials with opposite first corrections, not a conjectured
indicator asymptotic.

This is a counterexample within the actual source family to a uniform
downward-bias interpretation. It does not determine a first correction
at any preselected threshold, prove bounded variation of `C`, cover the
near-pole regime, or exclude an off-critical zero.

## Response, coefficient functional, and normalization

Write `sigma=1+epsilon>1`, and put

\[
 A=\sum_{n\ge2}\Lambda(n)n^{-\sigma},\qquad
 a_n=\Lambda(n)n^{-\sigma}/A,\qquad
 G(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r}.
 \tag{1}
\]

Only prime powers have nonzero coefficients. On the prime torus with
probability Haar measure `m`, let `chi_u=prod_p z_p^{nu_p(u)}` and

\[
 Q=\sum_{n,m\ge2}a_na_mG(n,m)\chi_{n/m},\qquad
 \mu=\int Q\,dm=\sum_n a_n^2G(n,n),\qquad
 b=2a_2a_3G(2,3)>0.
 \tag{2}
\]

For an absolutely convergent rational-character series
`H=sum_u d_u chi_u`, define

\[
 \|H\|_{\mathrm W}=\sum_u|d_u|,\qquad
 \mathfrak L(H)=-\sum_u d_u\kappa(u),
 \quad
 \kappa(u)=
 \begin{cases}
  (\log p)p^{-j/2},&u=p^j\text{ or }p^{-j},\ j\ge1,\\
  0,&\text{otherwise}.
 \end{cases}
 \tag{3}
\]

This coefficient norm is submultiplicative. Also
`sup_u kappa(u)<=sup_(x>1) (log x)/sqrt(x)=2/e<1`, so
`|mathfrak L(H)|<=||H||_W`. This bound concerns coefficients; it does
not assert a finite signed measure on the infinite torus.

For each fixed polynomial `F`, WI-465 proves unconditionally

\[
 \log T\left[\frac1{D_T}\sum_{T<\gamma\le2T}F(Q(\gamma))
                 -\int F(Q)\,dm\right]
 \longrightarrow\mathfrak L(F(Q))
 =-\int_0^1 F'(x)C(x)\,dx.
 \tag{4}
\]

Here `z_p(gamma)=exp(-i gamma log p)` and `D_T=N(2T)-N(T)` counts
all nontrivial zeros with multiplicity, including different real parts
at the same ordinate. The parameters and polynomial are fixed before
the height limit. The proof below uses (3) to control the *full* series
and then (4); a finite-prime approximation is not silently passed
through an order-`1/log T` sampling limit.

## The first prime square supplies a perturbation with the opposite sign

Set `u=arg z_2`, `v=arg z_2-arg z_3`, and

\[
 Y=\frac{Q-\mu}{b},\qquad Y_0=\cos v,\qquad
 t_\sigma=\frac{a_4G(2,4)}{a_3G(2,3)}
 =\frac{\log2}{\log3}\frac{G(2,4)}{G(2,3)}
    \left(\frac34\right)^\sigma>0.
 \tag{5}
\]

For fixed `r>0`, the exact expansion is

\[
 Y=Y_0+t_\sigma\cos u+R_\sigma,\qquad
 \|R_\sigma\|_{\mathrm W}
 =O_r\left(2^{-\sigma}+(3/5)^\sigma\right)=o_r(t_\sigma).
 \tag{6}
\]

To verify the infinite tail, write
`U_sigma=sum_(n>=5) Lambda(n)n^(-sigma)`. For `sigma>=2`, integer-sum
comparison gives

\[
 U_\sigma\le5^{2-\sigma}\sum_{n\ge5}\frac{\log n}{n^2}
 \le5^{2-\sigma}\frac{\log4+1}{4}<15\,5^{-\sigma},
 \qquad A<4\,2^{-\sigma}.
 \tag{7}
\]

For the latter inequality, separate `2,3,4`, apply the former to the
tail, and bound each ratio to `2^(-sigma)` by its value at `sigma=2`.
The off-diagonal coefficient mass involving any `n>=5` is at most
`2 U_sigma/A`, since `sum a_n=1` and `0<=G<=1`. After division by `b`,
this is at most

\[
 \frac{60}{(\log2)(\log3)G(2,3)}(3/5)^\sigma.
 \tag{8}
\]

Among `2,3,4`, the unretained off-diagonal term is
`(a_4/a_2)[G(3,4)/G(2,3)] cos(u+v)`, of norm
`2^(-sigma)G(3,4)/G(2,3)`. All diagonal terms have already been removed
by the *full* mean `mu`. These facts prove (6), even after equal
rational characters have been collected.

Choose the fixed quintic shape

\[
 f(y)=-\frac15(1-y)^5,\qquad f'(y)=(1-y)^4\ge0,
 \qquad F_\sigma(x)=f\left(\frac{x-\mu}{b}\right).
 \tag{9}
\]

Thus `F_sigma` is increasing on the whole real line, with
`F_sigma'(x)=b^(-1)(1-(x-mu)/b)^4`. It may be shifted by a constant
to be nonnegative on the response interval without changing any
correction.

Every nonconstant character of `f(Y_0)` is `(2/3)^j`, so
`mathfrak L(f(Y_0))=0`. To compute the first perturbation, abbreviate
`A_p=(log p)/sqrt(p)` and `w(v)=(1-cos v)^4`. Only the axis characters
`2,2^(-1),3,3^(-1)` survive in `w(v) cos u`. Equivalently, on the
two-prime torus use the classical correction densities

\[
 h_p(\theta_p)=-2\log p\sum_{j\ge1}p^{-j/2}\cos(j\theta_p).
\]

Integrating in `u`, with `theta_3=u-v`, yields

\[
 \int\cos u\,[h_2(u)+h_3(u-v)]\,\frac{du}{2\pi}
 =-A_2-A_3\cos v.
 \tag{10}
\]

The exact circle moments are
`int w=35/8` and `int w cos v=-7/2`; hence

\[
 K:=\mathfrak L(w(v)\cos u)
 =\frac72\frac{\log3}{\sqrt3}
  -\frac{35}{8}\frac{\log2}{\sqrt2}>0.
 \tag{11}
\]

The sign is rigorous, not inferred from a numerical integral. For
example `log3>1.098`, `log2<0.694`, `sqrt3<1.733`, and
`sqrt2>1.414` imply
`K>98389/1400264>0.07`. The logarithm bounds follow from the
geometric remainder for
`log x=2 sum_(j>=0) ((x-1)/(x+1))^(2j+1)/(2j+1)`; the square-root
bounds follow by squaring rational numbers.

Polynomial expansion in the coefficient algebra now gives

\[
 \boxed{\mathfrak L(F_\sigma(Q))
       =t_\sigma K+O_r(t_\sigma^2+\|R_\sigma\|_{\mathrm W})
       =t_\sigma\{K+O_r((4/5)^\sigma)\}>0}
 \tag{12}
\]

for all sufficiently large `sigma`, at each fixed `r>0`. In detail, if
`delta=t_sigma cos u+R_sigma` has norm at most one, expansion of (9)
around `Y_0` bounds its quadratic and higher terms by
`27 ||delta||_W^2`, while `||f'(Y_0)||_W<=16`. Therefore

\[
 |\mathfrak L(F_\sigma(Q))-t_\sigma K|
 \le16\|R_\sigma\|_{\mathrm W}
       +27(t_\sigma+\|R_\sigma\|_{\mathrm W})^2.
 \tag{13}
\]

This uses a bounded functional on coefficient space, not a bound on
the total variation of the divergent sum of prime-axis densities.

## An explicit full-series sign certificate

At `r=1`, the three Gram entries are
`G(2,3)=1/2`, `G(2,4)=3/8`, and `G(3,4)=2/3`. The previous estimates
give, for `sigma>=2`,

\[
 \frac25(3/4)^\sigma<t_\sigma<\frac12(3/4)^\sigma,\qquad
 \|R_\sigma\|_{\mathrm W}\le
 E_\sigma:=\frac43\,2^{-\sigma}+160(3/5)^\sigma.
 \tag{14}
\]

For every real `sigma>=100`,

\[
 \frac{E_\sigma}{(2/5)(3/4)^\sigma}<10^{-6},\qquad
 \frac12(3/4)^\sigma<10^{-12}.
 \tag{15}
\]

Each left side decreases with `sigma`; its value at `100` is a rational
number. Exact rational arithmetic verifies (15), as well as the rational
logarithm bounds used in (11), (14), and (7). In particular
`||delta||_W<1`, and (13) implies

\[
 \mathfrak L(F_\sigma(Q))
 >t_\sigma\bigl[0.07-16\cdot10^{-6}
                     -27(1+10^{-6})^2\cdot10^{-12}\bigr]>0.
 \tag{16}
\]

No phase quadrature, finite zero table, model assumption, or unbounded
numerical truncation is an input to this certificate. The threshold
`100` is deliberately nonoptimal.

## Consequences for cumulative signs and stochastic order

WI-464 gives `int C=B_epsilon(r)>0`, while (4), (9), and (12) give

\[
 \int_0^1 F_\sigma'(x)C(x)\,dx<0,
 \qquad F_\sigma'(x)\ge0.
 \tag{17}
\]

Since `C` is integrable, (17) forces `{C<0}` to have positive measure;
its positive integral forces `{C>0}` to have positive measure as well.
This statement is well-defined for its `L^1` equivalence class and
requires neither pointwise cutoff convergence nor a signed density on
the infinite torus.

For each fixed admissible `sigma,r`, (4) implies, for all sufficiently
large `T`,

\[
 \frac1{D_T}\sum F_\sigma(Q(\gamma))>\int F_\sigma(Q)\,dm,
 \qquad
 \frac1{D_T}\sum Q(\gamma)<\int Q\,dm.
 \tag{18}
\]

Usual stochastic dominance in either direction would order the
expectations of *both* increasing functions in that direction,
contradicting (18). This elementary implication also follows by
integrating their derivatives against the distribution functions.
Thus the finite-height distribution functions must cross. Their
crossing thresholds may depend on height; (18) establishes no limit
of a scaled indicator error at a prescribed threshold.

WI-465's negative correction for **each fixed** positive moment and
positive-exponential test remains valid. No common height uniform in
moment order is inferred. The quintic has alternating coefficients,
so it is outside that finding's nonnegative-coefficient sign cone.
For the prime-only control every polynomial correction remains zero
by common-rotation invariance. The term `2,4`, representing the first
coherent prime square, is the leading source of the opposite sign.

## Prior art, audit boundary, and significance

The prime-axis functional is classical: Ford–Zaharescu, *On the
distribution of imaginary parts of zeros of the Riemann zeta function*,
**J. reine angew. Math. 579** (2005), 145–158,
[Corollary 2 and §3](https://ford126.web.illinois.edu/wwwpapers/fz.pdf).
Ford–Meng–Zaharescu, *Simultaneous distribution of the fractional parts
of Riemann zeta zeros*, **BLMS 49** (2017), 1–9,
[Lemmas 1–2](https://arxiv.org/pdf/1511.06814), supply the unconditional
uniform arithmetic inputs underlying WI-465's full-series polynomial
transport. They are not cited as a theorem about the present quintic.
The classical distinction between moments and stochastic order is not
new. The substantive delta is an explicit opposite-sign increasing
test for the actual full Euler response, including a controlled tail,
and the resulting sign change of its candidate cumulative coefficient.
No literature-priority claim is made.

Ford–Soundararajan–Zaharescu,
[§1 of *On the distribution … II*](https://arxiv.org/pdf/0805.2745),
separate smooth corrections from interval indicators. Nothing in this
argument bypasses that distinction or WI-463's bracket obstruction.

The load-bearing checks are the full-mean subtraction in (6), the
`2,4` versus `3,4` scales, the `theta_3=u-v` sign in (10), the
coefficient-norm rather than total-variation remainder in (13), and
fixing `sigma,r,F_sigma` before the arithmetic height limit. The
large-`sigma` argument selects a parameter regime; it is not a joint
`sigma,T` limit. It proves neither sign change near `sigma=1` nor any
uniformity as `r` varies. It also does not settle the finite-signed-
measure regularity question left by WI-464.

This closes the proposed uniform monotone-bias interpretation with a
source-family counterexample. It calibrates a statistical observable,
not an individual off-line defect. No improved simple-critical
proportion, off-line-zero exclusion, Lean verification, or RH conclusion
is claimed. The finite algebra is routine; the substantive arithmetic
input remains the existing analytic transport theorem, with no separate
formalization-fertility handoff identified here.
