# MC-043 — Growing-order Möbius Riesz smoothing has a normalization-vacuity threshold

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

For `tau>=0` and any coefficient sequence `a_n` with `|a_n|<=1`, define the normalized Riesz mean

\[
R_{\tau,a}(x)
=
\frac1{\Gamma(\tau+1)}
\sum_{n\le x}a_n\left(1-\frac nx\right)^\tau,
\qquad x\ge1.
\tag{1}
\]

Then the kernel mass alone gives the exact universal bound

\[
\boxed{
|R_{\tau,a}(x)|\le \frac{x}{\Gamma(\tau+2)}.
}
\tag{2}
\]

No cancellation, multiplicativity, Möbius structure, or zeta information is used in `(2)`. In particular it applies to the Möbius Riesz mean `M_tau(x)` of `MC-042`.

Moreover the all-positive matched control essentially saturates this scale. For every integer `X>=1` and `tau>0`, if

\[
R_{\tau,+}(X)
=
\frac1{\Gamma(\tau+1)}
\sum_{n=1}^{X}\left(1-\frac nX\right)^\tau,
\tag{3}
\]

then

\[
\boxed{
\frac{X}{\Gamma(\tau+2)}-
\frac1{\Gamma(\tau+1)}
\le
R_{\tau,+}(X)
\le
\frac{X}{\Gamma(\tau+2)}.
}
\tag{4}
\]

Hence whenever `tau=o(X)`,

\[
R_{\tau,+}(X)
=
\frac{X}{\Gamma(\tau+2)}
\left(1+O\left(\frac{\tau+1}{X}\right)\right).
\tag{5}
\]

The consequence for growing smoothing order is sharp at the power-exponent level. If

\[
\tau(x)=c\frac{\log x}{\log\log x},
\qquad c>0,
\tag{6}
\]

then Stirling's formula gives

\[
\log\Gamma(\tau(x)+2)
=(c+o(1))\log x,
\tag{7}
\]

and therefore

\[
\boxed{
\frac{x}{\Gamma(\tau(x)+2)}
=x^{1-c+o(1)}.
}
\tag{8}
\]

Thus for every fixed `delta>0`, taking

\[
\tau(x)\ge
\left(\frac12+\delta\right)
\frac{\log x}{\log\log x}
\tag{9}
\]

through a regime where the left side tends to infinity is already enough for the **trivial coefficient bound** to imply, eventually,

\[
|M_{\tau(x)}(x)|
\le x^{1/2-\delta/2}.
\tag{10}
\]

Conversely, for fixed `0<c<1/2`, the all-positive control in `(5)` has size

\[
R_{\tau,+}(X)=X^{1-c+o(1)},
\tag{11}
\]

so the normalized kernel itself does not force square-root scale there. At `c=1/2` the transition is `X^{1/2+o(1)}`; lower-order `log log log` terms decide which side of a literal `X^{1/2}` inequality one lies on.

Therefore **growing the normalized Riesz order is not automatically a stronger cancellation probe**. At order about `(1/2) log x / log log x` on the first asymptotic scale, the normalization alone crosses the square-root exponent even for arbitrary bounded coefficients. Any variable-order continuation of the smoothing route after `MC-042` must remain quantitatively below this vacuity boundary, renormalize away the kernel-mass decay, or prove a signed gain beyond the total kernel mass.

## 1. Universal kernel-mass bound

For fixed `x` and `tau>=0`, the function

\[
f(t)=\left(1-\frac tx\right)^\tau
\]

is nonnegative and decreasing on `[0,x]` (with the evident constant interpretation at `tau=0`). Therefore for every integer `n<=x`,

\[
f(n)\le \int_{n-1}^{n} f(t)\,dt.
\tag{12}
\]

Summing and then extending the integral to all of `[0,x]` gives

\[
\sum_{n\le x}\left(1-\frac nx\right)^\tau
\le
\int_0^x\left(1-\frac tx\right)^\tau dt
=
\frac{x}{\tau+1}.
\tag{13}
\]

Taking absolute values in `(1)` and using

\[
(\tau+1)\Gamma(\tau+1)=\Gamma(\tau+2)
\]

proves `(2)`.

This argument deliberately forgets every sign. It therefore identifies an information floor: once `(2)` itself reaches the desired exponent, observing the same exponent for Möbius no longer certifies any cancellation.

## 2. The all-positive control saturates the same scale

Take integer `X` and `tau>0`. Since `f` is decreasing,

\[
\int_1^X f(t)\,dt
\le
\sum_{n=1}^{X-1}f(n)
=
\sum_{n=1}^{X}f(n),
\tag{14}
\]

because `f(X)=0`. Also

\[
\int_1^X f(t)\,dt
=
\frac{X}{\tau+1}-\int_0^1 f(t)\,dt
\ge
\frac{X}{\tau+1}-1.
\tag{15}
\]

Combining `(13)` and `(15)` and dividing by `Gamma(tau+1)` proves `(4)`. Relative to the main kernel mass `X/Gamma(tau+2)`, the additive error in `(4)` is at most `(tau+1)/X`, proving `(5)`.

The control is intentionally non-arithmetic. It shows that the normalization threshold is not an artifact of a loose triangle inequality: a coefficient sequence with **no sign cancellation at all** occupies the same leading kernel-mass scale whenever `tau=o(X)`.

## 3. Stirling places the power transition at one half

Let `tau` satisfy `(6)`. Since

\[
\log\tau
=
\log\log x-
\log\log\log x+O_c(1),
\tag{16}
\]

standard Stirling asymptotics give

\[
\begin{aligned}
\log\Gamma(\tau+2)
&=(\tau+3/2)\log\tau-\tau+O(\log\tau)\\
&=c\log x+o(\log x),
\end{aligned}
\tag{17}
\]

which is `(7)` and `(8)`.

For `c=1/2+delta`, `(8)` is `x^(1/2-delta+o(1))`; absorbing the `o(1)` into `delta/2` yields `(10)` eventually. For `c<1/2`, `(5)` and `(8)` give the all-positive lower comparator `(11)` because `tau=o(X)`.

This is an exponent threshold, not an optimized finite-`x` cutoff. The convergence in `(7)` is slowed by the `log log log x / log log x` correction, so a finite numerical crossing can occur far from the first-order expression `(1/2) log x/log log x`. The durable statement is asymptotic.

## 4. Relation to the fixed-order obstruction and growing-order prior art

`MC-042` proved that every **fixed** Riesz order has a zero-free Mellin multiplier and that its square-root bound is RH-equivalent. That finding left growing order `tau=tau(x)` as a mathematically distinct escape because there is then no single fixed Mellin multiplier to continue.

The present finding does not close that escape, but it places an upper information boundary on it. As `tau` grows, two effects coexist:

1. the zero-smoothing kernel changes with scale, which may genuinely alter what can be proved;
2. the explicit normalization `1/Gamma(tau+1)` rapidly shrinks the entire coefficient mass, independently of cancellation.

Equation `(2)` isolates the second effect exactly. A proposed variable-order theorem must therefore show that its gain comes from the first effect rather than merely moving into a range where the second has already made the target small.

The primary prior-art anchor remains Inoue (`MC-S31`), who studies this same normalized Möbius Riesz family at both fixed and growing order. In particular, his RH-conditional growing-order theorem works at a scale of order

\[
\frac{\log\log x}{\log\log\log\log x},
\]

which is `o(log x/log log x)`. The trivial normalization barrier derived here is therefore **far above** that literature scale and does not explain or classicalize Inoue's RH-conditional result. Instead it marks where a future growing-order converse or cancellation claim would become information-theoretically uninformative unless its normalization is changed.

A targeted search around generalized Möbius Riesz means and growing order found the Inoue line as the directly relevant prior art but no basis for claiming novelty for the elementary kernel-mass/Stirling observation. The integral comparison, Gamma recursion, and Stirling asymptotics are classical. The durable contribution is the Mathia information audit: the currently live variable-order escape from `MC-042` has a concrete matched-control vacuity threshold.

## 5. Falsification boundary and what remains live

This finding does **not** prove that every useful growing-order choice must satisfy a literal hard inequality `tau<(1/2)log x/log log x`, nor that all information is lost above that value. A statistic can remain useful above the threshold if one rescales it, studies a signed ratio, retains another jointly controlled observable, or proves an inverse theorem that uses more than the raw normalized magnitude.

What is ruled out is narrower and exact: a claim of the form

\[
|M_{\tau(x)}(x)|\le x^{1/2+o(1)}
\]

cannot by itself be interpreted as Möbius cancellation evidence once the same exponent follows from `(2)` for **every** bounded coefficient sequence.

Likewise, a proposed inverse transfer from a large `tau` must account for the Gamma normalization explicitly. Writing the unnormalized Riesz sum as

\[
S_{\tau,a}(x)
=
\Gamma(\tau+1)R_{\tau,a}(x),
\tag{18}
\]

one always has

\[
|S_{\tau,a}(x)|\le \frac{x}{\tau+1}.
\tag{19}
\]

Thus a normalized square-root estimate at growing order is equivalent to

\[
|S_{\tau,\mu}(x)|
\le
\Gamma(\tau+1)x^{1/2},
\tag{20}
\]

and the right side becomes progressively weaker in the unnormalized information scale. Any claimed Tauberian recovery must demonstrate where a compensating signed gain enters rather than silently spending this Gamma factor.

The live smoothing window after `MC-042` is therefore narrower but nonempty: variable order well below the normalization-vacuity scale, nonlinear or jointly normalized multiscale carriers, and inverse estimates whose hypotheses are independently weaker than Mertens-scale cancellation remain legitimate targets. The decisive matched-control test for any such candidate is now immediate: compare it first with the all-positive bounded sequence and other support/multiplicativity controls after removing the raw kernel-mass normalization. If the claimed critical exponent survives solely because `Gamma(tau+2)` is already of square-root size, the route has not produced arithmetic cancellation.

## Consequence for the active transfer problem

The accepted mean-absolute/coarse-mode transfer clue had narrowed after `MC-042` to a genuinely scale-dependent or nonlinear carrier. This finding sharpens that remaining branch: **scale dependence by increasing the Riesz order is useful only while it changes the carrier faster than the normalization trivializes its size**.

A next candidate should therefore specify a quantitative order regime, measure its signed gain relative to `x/Gamma(tau+2)`, and exhibit an inverse transfer that does not simply multiply the gain back by `Gamma(tau+1)`. This converts “try growing Riesz order” into a falsifiable information-budget question rather than an open-ended smoothing direction.