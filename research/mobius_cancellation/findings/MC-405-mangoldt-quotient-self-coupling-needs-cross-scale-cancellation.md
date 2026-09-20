# MC-405 — Mangoldt quotient retention self-couples to Mertens and needs cross-scale cancellation

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-IDENTITY` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The accepted retained-variable clue asks whether a pre-quadratic representation can keep a quotient/source variable alive instead of collapsing all divisor labels to an lcm fiber. There is a natural exact Möbius decomposition that does exactly that at the formal level, but it also gives a useful negative control: **retaining a quotient variable is not by itself enough**.

For every positive integer `n`,

\[
\boxed{
\mu(n)\log n
=
-(\mu*\Lambda)(n)
=
-\sum_{ab=n}\mu(a)\Lambda(b).
}
\tag{1}
\]

Hence, writing

\[
M(x):=\sum_{n\le x}\mu(n),
\]

one gets the exact quotient-scale identity

\[
\boxed{
\sum_{n\le x}\mu(n)\log n
=
-\sum_{b\le x}\Lambda(b)M(x/b).
}
\tag{2}
\]

Partial summation gives a second exact form:

\[
\boxed{
M(x)\log x-
\int_1^x\frac{M(t)}{t}\,dt
=
-\sum_{b\le x}\Lambda(b)M(x/b).
}
\tag{3}
\]

Thus the prime-power source variable `b` genuinely survives inside the quotient `x/b`, so this representation lies outside the pure divisor-incidence/lcm collapse of `MC-404`. But after summing over `b`, the entire source-weighted quotient family is **exactly a first-order self-coupling of `M`**. The variable has survived notation without yet supplying independent cancellation information.

More sharply, suppose for some fixed `0<theta<1` and all relevant `y` one only knows the pointwise input

\[
|M(y)|\le C y^\theta.
\tag{4}
\]

Then absolute values in `(2)` give

\[
\sum_{b\le x}\Lambda(b)|M(x/b)|
\le
C x^\theta
\sum_{b\le x}\frac{\Lambda(b)}{b^\theta}.
\tag{5}
\]

The prime number theorem and partial summation imply

\[
\sum_{b\le x}\frac{\Lambda(b)}{b^\theta}
\sim
\frac{x^{1-\theta}}{1-\theta},
\tag{6}
\]

so the triangle-inequality closure has size `O(Cx)` for **every** fixed exponent `theta<1`. In contrast, `(3)` and `(4)` force the actual signed sum to satisfy

\[
\left|\sum_{b\le x}\Lambda(b)M(x/b)\right|
=O_\theta(Cx^\theta\log x).
\tag{7}
\]

Therefore any use of this retained quotient representation at exponent `theta` must recover a signed cross-scale saving of order roughly

\[
\frac{x^{1-\theta}}{\log x}
\tag{8}
\]

relative to the natural absolute mass. At the RH scale `theta=1/2`, the missing gain is roughly `sqrt(x)/log x`.

This is not a proof that the quotient representation is useless. It isolates its exact obligation: **a successful argument must control signed interaction among the values `M(x/b)` across prime-power scales; source-variable retention plus pointwise bounds and triangle inequality cannot bootstrap any fixed power exponent below `1`.**

No estimate for `M(x)` is improved here.

## 1. Exact arithmetic derivation

Let `1(n)=1`, let `L(n)=log n`, and use Dirichlet convolution. The classical divisor identity

\[
L=1*\Lambda
\tag{9}
\]

and Möbius inversion `mu*1=epsilon` give

\[
\Lambda=\mu*L.
\tag{10}
\]

There is also the elementary convolution Leibniz rule for the logarithmic weight operator

\[
D f(n):=f(n)\log n:
\qquad
D(f*g)=Df*g+f*Dg.
\tag{11}
\]

Apply `(11)` to `mu*1=epsilon`. Since `D epsilon=0` and `D1=L`,

\[
D\mu*1+\mu*L=0.
\tag{12}
\]

By `(10)`, this is

\[
D\mu*1=-\Lambda.
\]

Convolving with `mu`, and using `1*mu=epsilon`, yields

\[
D\mu=-\Lambda*\mu,
\]

which is `(1)`.

This derivation is purely finite arithmetic. It does not use `1/zeta(s)`, analytic continuation, contour shifting, or any zero-free region.

## 2. Summation retains a real quotient variable

Sum `(1)` over `n<=x` and write `n=ab`:

\[
\begin{aligned}
\sum_{n\le x}\mu(n)\log n
&=-\sum_{ab\le x}\mu(a)\Lambda(b)\\
&=-\sum_{b\le x}\Lambda(b)
  \sum_{a\le x/b}\mu(a)\\
&=-\sum_{b\le x}\Lambda(b)M(x/b).
\end{aligned}
\tag{13}
\]

Unlike a pure divisor-incidence weight, the source label `b` now changes the downstream arithmetic object through the quotient `x/b`. Two labels with the same lcm-incidence behavior need not produce the same argument of `M`. Therefore `MC-404` does not collapse `(13)`.

This makes `(13)` a useful matched control for the current clue: it demonstrates concretely that the requested kind of variable can survive an exact arithmetic transformation while still failing to deliver a free analytic gain.

## 3. The retained family is nevertheless an exact self-coupling

Abel summation applied to the left side of `(13)` gives

\[
\sum_{n\le x}\mu(n)\log n
=
M(x)\log x-
\int_1^x\frac{M(t)}{t}\,dt,
\tag{14}
\]

which proves `(3)`.

Equation `(3)` is the important structural boundary. The full prime-power quotient family

\[
b\longmapsto M(x/b)
\]

has not produced a second independent arithmetic observable after aggregation with `Lambda(b)`: its signed weighted total is exactly determined by `M` itself.

That does **not** mean each individual scale `M(x/b)` is redundant, nor that a decomposition of the `b`-range cannot reveal useful cancellation before the final sum. It means that a proposal whose only new ingredient is “keep `b` visible and then bound the terms separately” has not escaped the original problem.

## 4. Absolute values erase every fixed power exponent below one

Assume `(4)`. Then `(5)` is immediate. To evaluate the coefficient mass, put

\[
\psi(u):=\sum_{n\le u}\Lambda(n).
\]

The prime number theorem gives `psi(u)~u`. Partial summation therefore yields, for fixed `0<theta<1`,

\[
\begin{aligned}
\sum_{b\le x}\frac{\Lambda(b)}{b^\theta}
&=x^{-\theta}\psi(x)
 +\theta\int_1^x\psi(t)t^{-\theta-1}\,dt\\
&\sim
x^{1-\theta}
+\frac{\theta}{1-\theta}x^{1-\theta}\\
&=
\frac{x^{1-\theta}}{1-\theta}.
\end{aligned}
\tag{15}
\]

Thus the unsigned transform in `(5)` is of linear scale `Cx`, irrespective of the input power `theta<1`.

On the other hand, `(14)` and `(4)` give

\[
\left|M(x)\log x-
\int_1^x\frac{M(t)}{t}\,dt\right|
\le
C x^\theta\log x
+
C\int_1^x t^{\theta-1}\,dt
=
O_\theta(Cx^\theta\log x),
\tag{16}
\]

which is `(7)`.

The gap between `(15)` and `(16)` is not a contradiction; it is exactly the cancellation that the signed values `M(x/b)` must exhibit against the positive prime-power weights `Lambda(b)` when `M` has power cancellation. A proof that discards those signs has discarded the only place the exponent can survive.

## 5. Quantitative obligation at the critical scale

At a hypothetical RH-scale input

\[
|M(y)|\le C_\varepsilon y^{1/2+\varepsilon},
\]

with fixed `epsilon<1/2`, the absolute mass in `(5)` is still `O(C_epsilon x)`, whereas the exact signed transform is only

\[
O_\varepsilon(C_\varepsilon x^{1/2+\varepsilon}\log x).
\]

So the relevant source-scale theorem would need to explain a cancellation factor essentially

\[
x^{1/2-\varepsilon}/\log x.
\]

This pinpoints what a genuine quotient-retaining bootstrap must add. It is not enough that `b` survives Cauchy, inversion, or a hyperbola decomposition. One needs an independently controlled relation among the signs and magnitudes of `M(x/b)` over many prime-power scales, or another tuple-sensitive observable that is not already an exact aggregate of `M`.

## 6. Prior art and novelty boundary

The arithmetic identities behind `(1)` are classical. The standard relations

\[
\sum_{d\mid n}\Lambda(d)=\log n,
\qquad
\Lambda(n)=\sum_{d\mid n}\mu(d)\log(n/d)
\]

are recorded, for example, in the *Encyclopedia of Mathematics* entry “Mangoldt function”, which cites Hardy and Wright, *An Introduction to the Theory of Numbers*, §17.7. The equivalent identity

\[
\sum_{d\mid n}\mu(n/d)\Lambda(d)=-\mu(n)\log n
\]

is an immediate Möbius-inversion consequence. No novelty is claimed for `(1)`--`(3)`, for Abel summation, or for the PNT asymptotic `(6)`.

A targeted mechanism-level search on 20 September 2026 found the underlying Möbius--Mangoldt convolution as standard arithmetic-function algebra. The durable contribution here is only the **frontier-level diagnostic**: the most obvious quotient/source variable outside the lcm-incidence algebra self-couples exactly to `M`, and any absolute-value treatment maps every fixed sublinear power input to linear scale. Thus “retains a quotient variable” is a necessary-looking representation property but is not a sufficient mechanism for the current Mathia retained-variable branch.

## Boundaries and falsification tests

- **No impossibility theorem for quotient methods.** Splitting the `b`-range, using cancellation between scales, coupling to another arithmetic observable, or retaining more structure before summation may escape this obstruction.
- **The triangle-inequality barrier is method-specific.** Equation `(5)` shows failure of absolute-value closure, not a lower bound for the true signed convolution.
- **The PNT is only used to price unsigned source mass.** The exact self-coupling `(3)` is elementary and finite.
- **No circular `1/zeta` input.** The derivation uses divisor identities and Möbius inversion rather than analytic continuation of the reciprocal zeta function.
- **No independence heuristic.** Nothing assumes random signs for `mu` or for the values `M(x/b)`.
- **The source weights are positive.** All cancellation in `(2)` comes from the signs of `M(x/b)`; `Lambda(b)>=0`.
- **Fixed `theta`.** The asymptotic `(6)` is stated for fixed `0<theta<1`; no uniform endpoint estimate as `theta` varies with `x` is claimed.
- **No RH conclusion.** The critical-scale calculation prices the missing signed saving conditionally; it does not establish it.

## Consequence for the research line

`MC-404` says that a useful pre-lcm variable must change arithmetic inside an lcm fiber. Equation `(13)` supplies a canonical example that passes that representation test: `b` survives by changing the quotient `x/b`. `MC-405` adds the next filter.

A retained variable must do more than survive representation. **Its downstream family must carry independently exploitable signed or phase structure.** In the Möbius--Mangoldt quotient decomposition, the aggregate family is exactly the original Mertens problem in self-coupled form, and taking absolute values destroys every fixed sublinear power exponent.

Accordingly, the alternative branch of the accepted retained-variable clue should reject quotient/source proposals that reduce after exact summation to `(3)` or another self-coupling and then use only pointwise bounds. A surviving proposal should exhibit, before claiming a gain, the specific cross-scale correlation, phase, congruence, or off-diagonal mechanism that controls the signed source sum beyond its `O(x)` absolute mass.