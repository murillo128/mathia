# MC-053 — Conjugate-square positivity closes the fixed complex square-free comparator escape

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
f:\mathbb N\to\mathbb C
\]

be multiplicative and supported on the square-free integers, with

\[
f(p^m)=0\quad(m\ge2),
\qquad |f(p)|\le1
\]

for every prime `p`. Suppose that for some fixed

\[
0<\alpha<1
\]

its partial sums satisfy

\[
S_f(x):=\sum_{n\le x}f(n)\ll x^\alpha,
\tag{1}
\]

and that its Dirichlet series

\[
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s}
\]

satisfies

\[
F(1)=0.
\tag{2}
\]

Then

\[
\boxed{\zeta(s)\ne0\qquad(\operatorname{Re}s>\alpha).}
\tag{3}
\]

Thus the loss of coefficientwise positivity identified in `MC-052` does **not** leave a fixed complex square-free comparator escape from the matching zeta zero-free burden. Positivity can be restored after tensoring the zeta quotient with its conjugate reflection.

In particular, the full hypotheses of `MC-052` already imply `(2)`: finite global ordinary pretentious distance from Möbius together with `(1)` forces a simple zero of `F` at `1`. Therefore a fixed complex square-free-supported comparator that is globally ordinarily Möbius-close and independently satisfies a power bound `S_f(x)<<x^alpha` already forces the matching zero-free half-plane `(3)`.

At the RH scale, if one fixed such comparator satisfies finite global ordinary distance from Möbius and

\[
S_f(x)=O_\varepsilon(x^{1/2+\varepsilon})
\qquad\text{for every }\varepsilon>0,
\tag{4}
\]

then RH follows by applying `(3)` with every `alpha=1/2+eta`, `eta>0`, and using the functional-equation symmetry.

The mechanism is an exact line-specific synthesis of the classical Landau nonnegative-Dirichlet-series argument. No standalone novelty claim is made.

## 1. The zeta quotient is holomorphic throughout the comparator half-plane

From `(1)` and partial summation,

\[
F(s)=s\int_1^\infty S_f(x)x^{-s-1}\,dx
\tag{5}
\]

is holomorphic throughout

\[
\operatorname{Re}s>\alpha.
\]

Set

\[
h=1*f,
\qquad
H(s)=\sum_{n\ge1}\frac{h(n)}{n^s}.
\]

For `Re(s)>1`,

\[
H(s)=\zeta(s)F(s).
\tag{6}
\]

Because `(2)` cancels the simple pole of `zeta` at `1`, the right side of `(6)` extends holomorphically to the entire half-plane `Re(s)>alpha`.

Square-free support gives a particularly rigid local quotient. If

\[
c_p:=1+f(p),
\]

then for every `m>=1`,

\[
h(p^m)=c_p,
\tag{7}
\]

and in `Re(s)>1` the local factor is

\[
H_p(s)=\frac{1+f(p)p^{-s}}{1-p^{-s}}.
\tag{8}
\]

For real `f`, `MC-051` used `c_p>=0` directly. For complex `f`, that sign is unavailable; the next step recovers positivity without discarding the phase information needed to define the quotient.

## 2. Conjugate reflection restores a nonnegative Dirichlet series

Define the holomorphic conjugate reflection

\[
H^*(s):=\overline{H(\overline{s})}
\]

and the product

\[
Q(s):=H(s)H^*(s).
\tag{9}
\]

Both factors are holomorphic in `Re(s)>alpha`, so `Q` is holomorphic there.

In `Re(s)>1`, both Dirichlet series converge absolutely and

\[
Q(s)=\sum_{n\ge1}\frac{q(n)}{n^s},
\qquad
q=h*\overline h.
\tag{10}
\]

The coefficients are multiplicative. Using `(7)`, for every prime `p` and `m>=1`,

\[
\begin{aligned}
q(p^m)
&=\sum_{j=0}^m h(p^j)\overline{h(p^{m-j})}\\
&=c_p+\overline{c_p}+(m-1)|c_p|^2\\
&=2(1+\operatorname{Re}f(p))+(m-1)|1+f(p)|^2.
\end{aligned}
\tag{11}
\]

Since `|f(p)|<=1` implies `Re f(p)>=-1`, every term on the last line is nonnegative. Hence

\[
\boxed{q(n)\ge0\qquad\text{for every }n.}
\tag{12}
\]

This is the decisive structural repair: the complex quotient itself need not have nonnegative coefficients, but its ordinary Dirichlet product with the conjugate-reflected quotient does.

The series in `(10)` has finite abscissa of convergence because it converges absolutely for `Re(s)>1`. Since its represented function `Q` is holomorphic throughout `Re(s)>alpha`, Landau's theorem for Dirichlet series with nonnegative coefficients forces the abscissa of convergence to be at most `alpha`. Therefore

\[
\boxed{
\sum_{n\ge1}\frac{q(n)}{n^\sigma}<\infty
\qquad(\sigma>\alpha).
}
\tag{13}
\]

This is the same classical positivity-to-convergence principle used in the real setting by Aymone (`MC-S33`), but the positive series here is the conjugate square `(9)` rather than the original quotient.

## 3. The positive tensor quotient is zero-free

For `Re(s)>1`, equation `(8)` gives the Euler factor

\[
Q_p(s)
=
\frac{(1+f(p)p^{-s})(1+\overline{f(p)}p^{-s})}
     {(1-p^{-s})^2}.
\tag{14}
\]

By `(13)`, the multiplicative Dirichlet series for `Q` converges absolutely throughout `Re(s)>alpha`, hence so does its Euler product there.

Every local factor in `(14)` is nonzero in that half-plane. Indeed `alpha>0` gives `|p^{-s}|<1`; with `|f(p)|<=1`, neither numerator factor can vanish, and the denominator cannot vanish either. Absolute Euler-product convergence then gives

\[
\boxed{Q(s)\ne0\qquad(\operatorname{Re}s>\alpha).}
\tag{15}
\]

Now suppose that `rho` were a zero of `zeta` with `Re(rho)>alpha`. The function `F` is holomorphic at `rho` by `(5)`, so `(6)` gives

\[
H(\rho)=\zeta(\rho)F(\rho)=0.
\]

Equation `(9)` would then imply `Q(rho)=0`, contradicting `(15)`. This proves `(3)`.

No zero-free region for zeta is used in the derivation. The only analytic inputs are the comparator power bound, the zero `(2)` at the zeta pole, and the classical Landau theorem applied after positivity has been restored by conjugation.

## 4. The same construction upgrades the quadratic phase budget, but not enough for direct Cauchy transfer

The tensor series also sharpens the quantitative boundary recorded in `MC-052`. From `(11)`,

\[
q(p)=2(1+\operatorname{Re}f(p))
\ge |1+f(p)|^2,
\tag{16}
\]

where the inequality is the elementary identity already used in `MC-052`. For `m>=2`, `(11)` also gives

\[
q(p^m)\ge |1+f(p)|^2.
\tag{17}
\]

Consequently `(13)` implies, for every `sigma>alpha`,

\[
\sum_p\frac{|1+f(p)|^2}{p^\sigma}<\infty.
\tag{18}
\]

Let `k=h^{-1}`. As in `MC-052`,

\[
k(p^m)=-(1+f(p))(-f(p))^{m-1},
\qquad m\ge1,
\]

so

\[
|k(p^m)|^2\le |1+f(p)|^2\le q(p^m).
\tag{19}
\]

Multiplicativity gives `|k(n)|^2<=q(n)`, and hence

\[
\boxed{
\sum_{n\ge1}\frac{|k(n)|^2}{n^\sigma}<\infty
\qquad(\sigma>\alpha).
}
\tag{20}
\]

Thus the comparator's cancellation plus the boundary zero upgrades the automatic quadratic norm from the single weight `1/n` in `MC-052` to every weight `n^{-sigma}` with `sigma>alpha`.

This still does not make the naive Cauchy inversion exponent-preserving. The calculation in `MC-052` requires a quadratic weight exponent `beta<2alpha-1` to transfer `x^alpha` directly through absolute Cauchy. The new theorem only forces such norms for `beta>alpha`; since `alpha<1`, one always has

\[
\alpha>2\alpha-1.
\]

Choosing `beta=alpha+epsilon` in that Cauchy estimate gives only the weaker power `x^{(1+alpha+epsilon)/2}`. The zero-free conclusion `(3)` therefore comes from **nonvanishing of the positive tensor quotient**, not from repairing the absolute inverse-convolution route.

This distinction matters: `MC-052` correctly located a real quantitative loss in direct inversion. The present result shows that this loss is not a genuine escape from the zeta zero-free obstruction because a different positivity carrier bypasses the Cauchy step altogether.

## 5. Matched controls identify the load-bearing hypotheses

The zero `(2)` is essential. Take the multiplicative square-free-supported function

\[
f(1)=1,
\qquad f(n)=0\quad(n>1).
\]

Then `S_f(x)=1`, so it satisfies arbitrarily strong power cancellation, but `F(s)=1` and `F(1)\ne0`. Here `H=\zeta` and `Q=\zeta^2`; the pole at `1` prevents the Landau argument from pushing convergence left of `1`. Excellent cancellation of an unrelated comparator alone therefore says nothing about zeta zeros.

Conversely, the phase-block comparator constructed in `MC-052` has finite ordinary Möbius distance and a well-behaved boundary Euler quotient, but no independent power bound was asserted. Without `(1)`, `F` is not known to be holomorphic in `Re(s)>alpha`, so `Q` is not known to be holomorphic there and Landau cannot be invoked. This prevents the current theorem from silently upgrading that control into a contradiction.

The fixed-comparator hypothesis is also substantive. The scale-dependent terminal-prime families of `MC-045`--`MC-048` do not define one global `F` with one half-plane of analytic continuation and one fixed positive tensor quotient. Their nonuniformity therefore remains outside the claim.

Finally, exact square-free support is used in `(7)` and hence in the positive local formula `(11)`. A complex comparator with nonzero prime-square data can produce different, sign-indefinite tensor coefficients. The theorem does not classify that larger multiplicative class.

## 6. Prior art and novelty boundary

The Landau step itself is classical. Aymone's Theorem 1.1 (`MC-S33`) is the closest source already audited in this line: for a real completely multiplicative `f`, it obtains a matching zeta zero-free region by constructing nonnegative convolution coefficients and applying Landau. The source also uses a square-free-supported companion series to complete its zero-free argument. `MC-050` and `MC-051` adapted the same positivity philosophy to fixed real square-free Möbius comparators.

Using a self-dual or conjugate product to recover positivity is also a classical general pattern in analytic number theory; Rankin--Selberg self-convolutions are a prominent neighboring example. A targeted literature search for complex square-free Möbius comparators, Landau-positive auxiliary products, and globally pretentious Helson characters found Aymone's real-valued results and the already-retained Helson-zeta flexibility literature, but did not establish the exact local identity `(11)` and implication `(3)` as a named theorem. Absence from that search is not evidence of novelty.

The Helson literature summarized in `research/prior_art/incremental/PA-helson-zeta-divisor-and-continuation-flexibility.md` remains an important boundary: unrestricted prime-phase Euler products can have highly flexible zero/pole divisors. The present theorem does not contradict that flexibility because it imposes the much stronger combination of square-free reciprocal coefficients, an independently proved power bound, and a zero at the zeta pole.

Accordingly, the durable result is classified as an exact Mathia-specific obstruction built from classical mechanisms, with `NO-NOVELTY-CLAIM`.

## 7. Consequence for the comparator frontier

`MC-049` closed fixed real completely multiplicative Liouville-like comparators at matching power scale. `MC-050` and `MC-051` closed fixed real square-free-supported Möbius-like comparators and identified coefficientwise positivity of `1*f` as their load-bearing carrier. `MC-052` showed that complex phases destroy that first-order positivity and leave only an ordinary quadratic phase budget under the naive inversion analysis.

The present result closes that apparent escape for the same fixed square-free-supported class. Complex phases can make `1*f` sign-indefinite, but the conjugate product

\[
(\zeta F)(s)\,\overline{(\zeta F)(\overline{s})}
\]

has nonnegative Dirichlet coefficients by `(11)`, and that is already enough to force the matching zeta zero-free half-plane.

A genuinely different fixed-comparator route must therefore break at least one load-bearing input: the boundary zero `F(1)=0`, exact square-free prime-power support, the unit-disk bound `|f(p)|<=1`, or reduction to a single auxiliary Dirichlet series with a fixed power exponent. Complexifying the prime values alone is no longer an open escape hatch.