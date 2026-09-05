# MC-075 — Symmetric fractional Dirichlet gauge has a near-linear Selberg–Delange mean

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-074` shows that the normalized factorization space

\[
\mathcal F_\mu=\{(a,k):a(1)=k(1)=1,\ a*k=\mu\}
\]

is a torsor for the Dirichlet-convolution unit group, so a useful factor statistic needs an independently justified gauge fixing. The most intrinsic gauge condition available from the factorization alone is **exchange symmetry**:

\[
\boxed{a=k.}
\tag{1}
\]

There is exactly one normalized arithmetic function satisfying

\[
\boxed{r*r=\mu.}
\tag{2}
\]

It is multiplicative and is the generalized divisor function

\[
\boxed{r=d_{-1/2},}
\qquad
\sum_{n\ge1}\frac{r(n)}{n^s}=\zeta(s)^{-1/2}
\quad(\operatorname{Re}s>1),
\tag{3}
\]

with the branch positive for real `s>1`. At every prime,

\[
\sum_{j\ge0}r(p^j)z^j=(1-z)^{1/2},
\qquad
r(p^j)=(-1)^j\binom{1/2}{j}.
\tag{4}
\]

Thus exchange symmetry really does fix the convolution gauge. But it fixes it in an analytically hostile way. Classical Selberg–Delange theory gives

\[
\boxed{
R(x):=\sum_{n\le x}r(n)
=\frac{x(\log x)^{-3/2}}{\Gamma(-1/2)}
+O\!\left(x(\log x)^{-5/2}\right)
}
\tag{5}
\]

and hence

\[
\boxed{
R(x)\sim -\frac{x}{2\sqrt\pi\,(\log x)^{3/2}}.
}
\tag{6}
\]

So the unique symmetric factor has **no fixed power saving at all**: for every fixed `delta>0`,

\[
|R(x)|\not=O(x^{1-\delta}).
\tag{7}
\]

Its absolute Dirichlet series likewise has abscissa exactly `1`.

The obstruction is not peculiar to the midpoint. For every fixed real

\[
0<\theta<1,
\]

the generalized divisor functions give an exact fractional factorization

\[
\boxed{
\mu=d_{-\theta}*d_{-(1-\theta)}.
}
\tag{8}
\]

Both factors have nonzero Selberg–Delange main terms of near-linear size:

\[
\sum_{n\le x}d_{-\theta}(n)
\sim
\frac{x(\log x)^{-1-\theta}}{\Gamma(-\theta)},
\tag{9}
\]

and

\[
\sum_{n\le x}d_{-(1-\theta)}(n)
\sim
\frac{x(\log x)^{-2+\theta}}{\Gamma(\theta-1)}.
\tag{10}
\]

The symmetric choice `theta=1/2` is exactly the point where the two logarithmic exponents balance, but the common scale remains `x/(log x)^(3/2)` rather than a power-cancellative scale.

Therefore **splitting Möbius symmetrically, or more generally by a fixed fractional power of its reciprocal-zeta Dirichlet series, does not distribute the Mertens cancellation burden into two milder one-factor cancellation problems.** It does the opposite: every nontrivial interior fractional split produces factors with explicit near-linear means, and the strong cancellation of `mu` reappears only after their signed Dirichlet convolution recombines.

No improved bound for `M(x)` is claimed.

## 1. Exchange symmetry has a unique normalized fixed point

The swap involution on the factorization torsor is

\[
(a,k)\longmapsto(k,a).
\]

A fixed point is exactly a normalized solution of `(2)`.

Uniqueness can be seen without multiplicativity. Suppose `r(1)=1` and the coefficients `r(m)` are known for `m<n`. The `n`-th coefficient of `r*r` is

\[
(r*r)(n)
=2r(n)
+\sum_{\substack{d\mid n\\1<d<n}}r(d)r(n/d).
\tag{11}
\]

Requiring `(r*r)(n)=mu(n)` determines `r(n)` uniquely from proper divisors. Starting from `r(1)=1`, this recursively gives a unique normalized square root of `mu` under Dirichlet convolution.

Now define `d_z` by the classical generalized-divisor Dirichlet series

\[
\sum_{n\ge1}\frac{d_z(n)}{n^s}=\zeta(s)^z
\qquad(\operatorname{Re}s>1),
\tag{12}
\]

using the real logarithm of `zeta(s)` on the real axis `s>1`. Absolute convergence gives the coefficient identity

\[
d_z*d_w=d_{z+w}.
\tag{13}
\]

Since `d_{-1}=mu`, equation `(13)` with `z=w=-1/2` shows

\[
d_{-1/2}*d_{-1/2}=d_{-1}=\mu.
\]

By uniqueness, this is the fixed point from `(11)`. Its Euler factor is `(4)`, so multiplicativity follows as well.

This is a genuine gauge fixing in the narrow sense relevant to `MC-074`: no external character, conductor, support choice, optimization functional, or arbitrary comparator remains. The negative conclusion below is therefore not caused by residual factorization nonuniqueness.

## 2. The symmetric factor has an unconditional near-linear main term

The generalized divisor asymptotic is classical Selberg–Delange prior art. `MC-S14` records a modern theorem for multiplicative `f` whose prime values have a sufficiently accurate mean `alpha`, with main term

\[
x\,\widetilde c_0\frac{(\log x)^{\alpha-1}}{\Gamma(\alpha)}
\]

and arbitrarily strong logarithmic remainder when the prime-average error is correspondingly strong.

For

\[
r=d_{-1/2},
\]

one has exactly

\[
r(p)=-\frac12
\]

for every prime. The required prime-value average is therefore just `-1/2` times the classical prime number theorem, whose zero-free-region error is stronger than every fixed inverse power of `log x`. Also `|r(n)|<=1`, so the divisor-bound hypothesis is harmless.

The leading Euler constant in `MC-S14` is exactly one here:

\[
\begin{aligned}
\widetilde c_0
&=\prod_p
\left(\sum_{j\ge0}\frac{r(p^j)}{p^j}\right)
(1-p^{-1})^{-1/2}\\
&=\prod_p
(1-p^{-1})^{1/2}(1-p^{-1})^{-1/2}\\
&=1.
\end{aligned}
\tag{14}
\]

Taking enough logarithmic accuracy in the theorem gives `(5)`. Since

\[
\Gamma(-1/2)=-2\sqrt\pi,
\]

we obtain `(6)`.

This is stronger than merely observing that a hypothetical power bound for `r` would carry zeta-zero information. The actual unconditional asymptotic already says that the symmetric factor is far too biased for any fixed power-saving comparator strategy.

## 3. Every interior fractional zeta-power split has the same defect

Equation `(13)` gives `(8)` immediately because

\[
-\theta-(1-\theta)=-1.
\]

For fixed `0<theta<1`, neither `-theta` nor `theta-1` is a nonpositive integer. Their Gamma values are finite and nonzero. Applying the same generalized-divisor asymptotic yields `(9)` and `(10)`, with nonzero leading constants.

Thus each factor is of the form

\[
x(\log x)^{-c}
\]

for a fixed positive `c`, not `x^(1-delta)` for any fixed `delta>0`. The only exceptional points of this one-parameter family are the endpoints `theta=0,1`, where one factor becomes `d_0=epsilon` and the other becomes `d_{-1}=mu`; the Gamma leading coefficient vanishes there because `1/Gamma(z)` vanishes at nonpositive integers. Those endpoints do not split the original problem—they return the trivial factorization.

This exposes a sharp structural discontinuity. The Möbius coefficient sequence sits at the integer exponent `z=-1`, where the generic Selberg–Delange main term disappears. Moving even to a fixed fractional convolution power restores a nonzero near-linear main term. The cancellation one hoped to distribute is therefore not stable under this natural fractional interpolation.

## 4. Absolute convolution control also fails below exponent one

From `(4)`, all nonconstant coefficients of `(1-z)^(1/2)` are negative. Hence

\[
1+\sum_{j\ge1}|r(p^j)|z^j
=2-(1-z)^{1/2}.
\tag{15}
\]

For real `sigma>0`, the logarithm of the absolute local factor at `z=p^{-sigma}` satisfies

\[
\log\bigl(2-(1-p^{-\sigma})^{1/2}\bigr)
=\frac{1}{2p^\sigma}+O(p^{-2\sigma}).
\tag{16}
\]

Therefore

\[
\sum_{n\ge1}\frac{|r(n)|}{n^\sigma}
\]

converges exactly for `sigma>1` and diverges for `sigma<=1`. So the exact recovery

\[
\mu=r*r
\tag{17}
\]

cannot be combined with a coefficientwise absolute inverse norm at any fixed target exponent below `1`. This mirrors the absolute-inversion barriers already found for other comparators, but here it occurs in the unique exchange-symmetric gauge itself.

For the general factor `d_{-theta}` with `0<theta<1`, the prime coefficient is `-theta`, so the prime terms alone again force absolute abscissa `1`.

## 5. Relation to the current factorization frontier

`MC-073` proves that complete comparator/inverse cancellation is algebraically forced for every normalized gauge. `MC-074` then shows that even a proper one-factor statistic is non-identifiable until the gauge is fixed independently.

Exchange symmetry is the cleanest attempt to meet that requirement without importing any extra arithmetic object: it selects the unique fixed point of the swap involution. The present calculation shows that **canonicality is not enough**. The internally selected factor is a classical generalized divisor sequence with a deterministic near-linear mean.

The broader family `(8)` makes the failure harder to dismiss as an unlucky midpoint. Any fixed fractional division of the exponent `-1` between two zeta-power factors produces two near-linear Selberg–Delange means. The exact smallness of Möbius cannot be assigned proportionally to the factors by this functional calculus; it resides in cancellation created by the full convolution.

A surviving gauge-fixing route therefore needs structure not supplied by the factorization group or by fractional powers of `zeta`. It may still use a source-natural arithmetic subclass, as `MC-074` permits, or a genuinely coupled statistic whose estimate exploits a relation between the factors before absolute values or standalone partial-sum bounds are imposed. But "choose the symmetric/canonical square root and split the difficulty" is now decisively closed.

## 6. Prior art and novelty boundary

The generalized divisor functions `d_z`, the identity `(12)`, and their Selberg–Delange asymptotics are classical. `MC-S14` is the retained primary theorem-level anchor for the asymptotic machinery and explicitly allows complex prime-average parameter `alpha`; the specialization `alpha=-1/2` is within its ordinary nonintegral regime. The convolution law `(13)` is immediate from multiplication of absolutely convergent Dirichlet series in `Re(s)>1`.

A targeted literature audit of generalized divisor functions, fractional powers of `zeta`, and Dirichlet-convolution square roots found no basis for treating `d_{-1/2}` or its summatory asymptotic as a new number-theoretic object. No such novelty is claimed.

The durable Mathia contribution is the **frontier obstruction relative to `MC-074`**: the most intrinsic swap-symmetric gauge fixing does exist and is unique, but established generalized-divisor theory proves that its factor has near-linear mean. The same obstruction holds across the natural interior fractional-power interpolation `(8)`. This removes a specific apparently canonical escape from the torsor degeneracy without claiming a new theorem about generalized divisor functions.

## 7. Boundaries and falsification tests

The claim is exact but deliberately limited.

- Exchange symmetry is a natural internal gauge condition, not a theorem that every useful gauge must respect it. An externally motivated arithmetic gauge may behave differently.
- The family `(8)` covers fixed fractional powers of the Riemann-zeta Euler product. It does not classify all restricted comparator families or all coupled statistics on `mathcal F_mu`.
- The Selberg–Delange asymptotics concern ordinary partial sums of the individual factors. They do not rule out a useful bilinear or weighted coupled statistic that cancels their main terms before estimation.
- The argument uses fixed `theta`. A scale-dependent `theta=theta(x)` is not covered by simply substituting into the fixed-parameter asymptotic; such a route would require its own uniform theorem and must also avoid collapsing to a moving-gauge version of the non-identifiability in `MC-074`.
- The absolute-abscissa statement concerns coefficientwise absolute recovery. Signed convolution can of course cancel strongly—indeed `(17)` is the point.
- No statement is made about pointwise sizes of individual `r(n)` beyond the elementary Euler coefficients needed above.

The finding is falsified if the normalized Dirichlet square root of `mu` is not unique, if `d_{-1/2}*d_{-1/2}` fails to equal `mu`, if the `MC-S14` Selberg–Delange theorem does not apply to `d_{-1/2}`, if its leading Euler constant is not one, or if `Gamma(-1/2)` does not give the main term `(6)`. These reduce to exact convolution algebra and a direct specialization of retained classical prior art.

## Consequence for the active frontier

`MC-074` asks the next comparator route to state its gauge fixing as part of the mathematics. The most immediate answer—**fix the gauge by requiring the two factors to be identical**—is now fully audited and fails for a stronger reason than zero-hardness: the selected factor is unconditionally known to have a near-linear Selberg–Delange mean.

The next productive coupled-comparator candidate should therefore not search for another purely algebraic notion of balance unless it comes with an independent arithmetic estimate. It must either justify a restricted gauge from arithmetic structure external to `a*k=mu`, or identify a coupled functional for which the large one-factor Selberg–Delange modes cancel by a theorem that is genuinely cheaper than the Mertens target.