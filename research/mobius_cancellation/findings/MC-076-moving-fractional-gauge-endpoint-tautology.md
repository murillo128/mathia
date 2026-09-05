# MC-076 — Polynomially moving fractional gauges trivialize one factor and leave the other Mertens-equivalent

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-075` closes every **fixed** interior fractional factorization

\[
\mu=d_{-\theta}*d_{-(1-\theta)},
\qquad 0<\theta<1,
\]

because both factors have near-linear Selberg–Delange means. It leaves open a natural endpoint escape: let the fractional exponent move with the cutoff so that one factor approaches the convolution identity while the other approaches Möbius.

That escape has an exact quantitative obstruction before any uniform Selberg–Delange theorem is needed.

For `0<eta<=1`, define

\[
u_\eta:=d_{-\eta},
\qquad
v_\eta:=d_{-1+\eta}.
\]

The classical generalized-divisor convolution law gives

\[
\boxed{u_\eta*v_\eta=\mu.}
\tag{1}
\]

Let

\[
U_\eta(X)=\sum_{n\le X}u_\eta(n),
\qquad
V_\eta(X)=\sum_{n\le X}v_\eta(n).
\]

Then the local Euler coefficients imply the elementary uniform bounds

\[
\boxed{|U_\eta(X)-1|\le \eta X,}
\tag{2}
\]

and, without using any zero-free region beyond the trivial bound `|M(y)|<=y`,

\[
\boxed{|V_\eta(X)-M(X)|\le \eta X(1+\log X).}
\tag{3}
\]

Consequently, fix any `delta in (0,1)` and allow a **diagonal moving gauge**

\[
\eta=\eta(X)=X^{-\delta+o(1)}.
\tag{4}
\]

Then

\[
U_{\eta(X)}(X)=1+O\!\left(X^{1-\delta+o(1)}\right),
\tag{5}
\]

while

\[
\boxed{
V_{\eta(X)}(X)
=M(X)+O\!\left(X^{1-\delta+o(1)}\right).
}
\tag{6}
\]

Hence, at the level of fixed power exponents,

\[
\boxed{
V_{\eta(X)}(X)=O_\varepsilon\!\left(X^{1-\delta+\varepsilon}\right)
\quad\Longleftrightarrow\quad
M(X)=O_\varepsilon\!\left(X^{1-\delta+\varepsilon}\right).
}
\tag{7}
\]

In particular, the apparently balanced choice needed to make the near-identity factor automatically live at the RH power scale,

\[
\eta(X)=X^{-1/2+o(1)},
\]

gives

\[
|U_{\eta(X)}(X)-1|=X^{1/2+o(1)}
\]

as a **pure coefficient-amplitude bound**, while

\[
V_{\eta(X)}(X)=M(X)+X^{1/2+o(1)}.
\]

Thus proving the matching square-root-scale bound for the companion factor is already equivalent to proving the Mertens RH criterion. The moving gauge has not split the cancellation burden: it has made one factor small by collapsing it toward the convolution identity and left the other factor equal to Möbius up to an error of exactly the target power scale.

More generally, any polynomial endpoint motion capable of manufacturing a fixed power saving `delta` by coefficient dilution produces the same `X^(1-delta+o(1))` approximation of the companion factor to `M(X)`. No improved estimate for `M(X)` is claimed.

## 1. Uniform prime-power bounds near the identity

For the generalized divisor function,

\[
\sum_{j\ge0}d_z(p^j)t^j=(1-t)^{-z}.
\]

For `0<eta<=1` and `j>=1`,

\[
\begin{aligned}
|d_{-\eta}(p^j)|
&=
\frac{\eta(1-\eta)(2-\eta)\cdots(j-1-\eta)}{j!}\\
&=
\frac{\eta}{j}
\prod_{m=1}^{j-1}\left(1-\frac{\eta}{m}\right)\\
&\le \frac{\eta}{j}
\le \eta.
\end{aligned}
\tag{8}
\]

Similarly,

\[
\begin{aligned}
d_{\eta}(p^j)
&=
\frac{\eta(1+\eta)(2+\eta)\cdots(j-1+\eta)}{j!}\\
&=
\frac{\eta}{j}
\prod_{m=1}^{j-1}\left(1+\frac{\eta}{m}\right)\\
&\le
\frac{\eta}{j}
\prod_{m=1}^{j-1}\left(1+\frac1m\right)\\
&=\eta.
\end{aligned}
\tag{9}
\]

The coefficients `d_eta(n)` are nonnegative. Both functions are multiplicative, so for every `n>1`, multiplying the local estimates over the distinct prime divisors gives

\[
\boxed{|d_{-\eta}(n)|\le \eta,\qquad 0\le d_\eta(n)\le\eta.}
\tag{10}
\]

Equation `(2)` now follows immediately:

\[
|U_\eta(X)-1|
\le
\sum_{2\le n\le X}|d_{-\eta}(n)|
\le \eta(X-1).
\]

This bound is deliberately crude. Its role is to expose why a moving endpoint can create an apparent power saving without any cancellation theorem: the nonconstant coefficients themselves are being scaled toward zero.

## 2. The companion factor is Möbius plus a controlled endpoint perturbation

The same classical convolution semigroup used in `MC-075` gives

\[
v_\eta=d_{-1+\eta}=d_{-1}*d_\eta=\mu*d_\eta.
\tag{11}
\]

Summing through `X`,

\[
\begin{aligned}
V_\eta(X)
&=
\sum_{d\le X}d_\eta(d)
\sum_{m\le X/d}\mu(m)\\
&=
M(X)+
\sum_{2\le d\le X}d_\eta(d)M(X/d).
\end{aligned}
\tag{12}
\]

Using only `|M(y)|<=y` and `(10)`,

\[
\begin{aligned}
|V_\eta(X)-M(X)|
&\le
\eta X\sum_{2\le d\le X}\frac1d\\
&\le
\eta X(1+\log X),
\end{aligned}
\]

which proves `(3)`.

This is stronger for the present purpose than trying to push a fixed-parameter Selberg–Delange expansion uniformly all the way into the endpoint. The estimate is finite, coefficient-level, and valid for every `0<eta<=1`; it does not pass through analytic continuation of `1/zeta(s)` or any Mertens estimate.

## 3. Exponent-equivalence on a polynomially moving diagonal

Assume `(4)`. For every fixed `epsilon>0`, eventually

\[
\eta(X)\le X^{-\delta+\varepsilon/2},
\qquad
1+\log X\le X^{\varepsilon/2}.
\]

Equations `(2)` and `(3)` then give

\[
|U_{\eta(X)}(X)-1|
\le X^{1-\delta+\varepsilon}
\]

and

\[
|V_{\eta(X)}(X)-M(X)|
\le X^{1-\delta+\varepsilon}.
\tag{13}
\]

If `M(X)=O_epsilon(X^(1-delta+epsilon))`, equation `(13)` gives the same bound for `V`. Conversely, if `V` has that bound, the triangle inequality and `(13)` give it for `M`. Replacing `epsilon` by a smaller fixed value when combining terms proves `(7)` in the usual `O_epsilon` exponent sense.

The important point is the **matching scale**. The same endpoint parameter that makes the first factor automatically `X^(1-delta+o(1))`-small also makes the second factor only `X^(1-delta+o(1))`-different from Möbius. There is no exponent slack from which a bootstrap can start.

At `delta=1/2`, `(7)` is exactly the RH-equivalent Mertens exponent. Choosing `eta` even smaller makes the first factor still more degenerate but makes the second factor correspondingly closer to Möbius; it does not create a cheaper square-root estimate.

## 4. What remains between fixed and polynomial endpoint motion

`MC-075` and the present finding close complementary regimes relevant to a **fixed power-saving** strategy.

- For fixed interior `theta`, both fractional factors have explicit near-linear Selberg–Delange means.
- To obtain a nontrivial fixed power saving merely by moving toward an endpoint, the distance from the endpoint must itself become polynomially small up to subpolynomial factors. In that regime `(2)`--`(7)` show that the small factor is being amplitude-diluted and the companion factor retains the target Mertens burden.
- Subpolynomial motions such as powers of `1/log X` may require uniform Selberg–Delange analysis for precise asymptotics, but they cannot by coefficient dilution alone manufacture a fixed power exponent below one: the elementary bound `(2)` is still `X^(1-o(1))`.

Thus a scale-dependent fractional exponent does not reopen the specific idea ruled out by `MC-075`: distribute a fixed fraction of the Mertens power-cancellation burden between two zeta-power factors. Any useful moving-parameter construction would need an additional coupled theorem that is not explained by endpoint amplitude dilution or by the exact convolution identity.

## 5. Prior art and novelty boundary

The generalized divisor functions `d_z`, the Euler factors, the identity

\[
d_z*d_w=d_{z+w},
\]

and fixed-parameter Selberg–Delange theory are classical prior art already anchored by `MC-S14` and audited in `MC-075`. A targeted search of generalized-divisor and Selberg–Delange literature also found the standard treatment of `d_z` and of the special case `d_{-1}=mu`; no novelty claim is made for those objects or for their convolution semigroup.

The inequalities `(8)`--`(13)` are elementary consequences of those classical coefficients. The durable Mathia result is the **frontier obstruction** they give when the fractional gauge is allowed to depend on the cutoff: the polynomial endpoint motion needed to make one factor look power-cancellative automatically leaves its companion Mertens-equivalent at the same exponent. This is recorded as an exact negative control, not as a claimed new theorem of analytic number theory.

## 6. Boundaries and falsification tests

- The parameter `eta(X)` defines a diagonal family of arithmetic functions; there is no claim that one fixed sequence simultaneously realizes all cutoffs. That moving-gauge freedom is precisely what is being stress-tested.
- Equation `(2)` is an upper bound, not an asymptotic. The near-identity factor may cancel further, but no such extra cancellation is needed to obtain the stated exponent obstruction.
- Equation `(3)` uses only the trivial `|M(y)|<=y`; it does not assume RH, a zero-free region, or the prime number theorem.
- The exponent-equivalence `(7)` concerns polynomial scales with the usual arbitrary `epsilon` loss. It does not classify logarithmic improvements inside the same power exponent.
- Subpolynomial endpoint motion is not proved to have a particular Selberg–Delange asymptotic here. It is excluded only as a mechanism for generating a **fixed power saving by coefficient dilution alone**.
- A genuinely coupled statistic of `u_eta` and `v_eta`, controlled uniformly in a moving parameter by new arithmetic input, is not ruled out. It must show a gain beyond `(2)`--`(3)` and avoid reducing to the exact factorization torsor of `MC-073`--`MC-074`.

The finding is falsified if the generalized-divisor convolution law fails, if the local bounds `(8)` or `(9)` fail for some `0<eta<=1`, if multiplicativity does not imply `(10)`, or if the finite convolution identity `(12)` does not hold. All of these are exact coefficient checks.

## Consequence for the active frontier

`MC-075` left scale-dependent fractional gauge as an explicit boundary. The polynomial version of that escape is now closed: **moving far enough toward the endpoint to manufacture any fixed power saving necessarily makes the complementary factor equal to Möbius up to an error of the same power scale.**

The comparator program therefore still needs what `MC-073`--`MC-075` demanded: an externally justified arithmetic gauge or a genuinely coupled, gauge-sensitive functional with an estimate independently cheaper than the Mertens target. Letting the exponent of `zeta(s)` vary with `X` does not by itself supply that missing information.