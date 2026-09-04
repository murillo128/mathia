# MC-048 — Beta-pretentious transfer overpays terminal-prime mass by a half exponent

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

The earlier Jung--Lemke Oliver `beta`-pretentious framework does not provide a cheaper square-root-scale escape from the obstruction isolated by `MC-045`--`MC-047`. Its characteristic Cauchy--Schwarz loss forces a much stronger prime-weight budget than the strong power-aware carrier audited in `MC-047`.

Use the terminal-prime control from `MC-045`. Fix

\[
\frac{17}{30}<\theta<\frac34,
\qquad
H=\lfloor X^\theta\rfloor,
\qquad
F_X=\{p:X-H<p\le X\},
\]

and let

\[
\nu_X(n)=\mu(n)\chi_{F_X}(n),
\]

where `chi_{F_X}(p)=-1` on `F_X` and `+1` on all other primes. If

\[
P_X=|F_X|,
\]

then `MC-045` gives

\[
P_X\sim \frac{X^\theta}{\log X},
\qquad
\sum_{n\le X}\nu_X(n)-M(X)=2P_X.
\tag{1}
\]

For the Jung--Lemke Oliver prime-only `beta`-distance,

\[
\mathbb D_\beta(f,g)^2
:=\sum_p\frac{1-\Re(f(p)\overline{g(p)})}{p^\beta},
\]

the exact terminal-slab cost is

\[
\boxed{
\mathbb D_\beta(\mu,\nu_X;X)^2
=2\sum_{p\in F_X}p^{-\beta}
=(2+o(1))\frac{X^{\theta-\beta}}{\log X}.
}
\tag{2}
\]

Jung--Lemke Oliver Theorem 1.1 detects cancellation through the exponent `(1+beta)/2` in the completely multiplicative case. Thus a hypothetical route using only this `beta`-pretentious mechanism to reach a target exponent

\[
\frac12+\varepsilon
\]

would require

\[
\beta\le 2\varepsilon.
\tag{3}
\]

For every `0<epsilon<1/2` and every terminal slab capable of producing a super-target endpoint discrepancy, namely

\[
\theta>\frac12+\varepsilon,
\tag{4}
\]

one has `theta>2 epsilon`. Hence every `beta` allowed by `(3)` gives

\[
\mathbb D_\beta(\mu,\nu_X;X)^2
\gg \frac{X^{\theta-2\varepsilon}}{\log X},
\tag{5}
\]

which grows polynomially. The terminal slab that is invisible to the ordinary `1/p` distance is therefore emphatically **not** invisible to a `beta`-distance strong enough to feed a square-root-scale Cauchy transfer.

There is an additional restriction for actual Möbius. The completely multiplicative conclusion of Theorem 1.1 does not apply to `mu` or `nu_X`, because both vanish on prime squares. For general multiplicative functions the same theorem requires an output exponent `sigma>3/4`, together with an auxiliary convergence hypothesis. Therefore Theorem 1.1 itself cannot reach `1/2+epsilon` for `epsilon<1/4` in the Möbius setting.

That `3/4` theorem-level restriction can be bypassed for this **explicit** comparator by going one layer deeper to Jung--Lemke Oliver Proposition 2.1 and using the exact convolution kernel. The bypass still does not give a uniform square-root transfer across the terminal-slab family. Writing

\[
\nu_X=\mu*h_X,
\]

`MC-047` gives

\[
h_X(p^k)=2\qquad(p\in F_X,\ k\ge1),
\]

and `h_X` is trivial at all other primes. Consequently

\[
\boxed{
\mathcal H_X(\sigma)
:=\sum_{n\ge1}\frac{|h_X(n)|^2}{n^\sigma}
=\prod_{p\in F_X}
\frac{1+3p^{-\sigma}}{1-p^{-\sigma}}.
}
\tag{6}
\]

The reverse convolution kernel from `nu_X` back to `mu` has the same absolute squares, so `(6)` is symmetric for the present purpose.

For fixed `sigma>0`, all primes in `F_X` are `X(1+o(1))`, and therefore

\[
\boxed{
\log \mathcal H_X(\sigma)^{1/2}
=(2+o(1))\frac{X^{\theta-\sigma}}{\log X}.
}
\tag{7}
\]

Proposition 2.1 is the elementary Cauchy--Schwarz transfer: if `S_f(x) << x^alpha` and `sum |h(n)|^2/n^sigma` converges, then

\[
S_{f*h}(x)
\ll
\mathcal H(\sigma)^{1/2}
 x^{\max\{\alpha,(1+\sigma)/2\}}
\tag{8}
\]

up to the harmless endpoint/logarithmic case in the elementary partial-sum estimate. To keep the exponent in `(8)` at most `1/2+epsilon`, one again needs

\[
\sigma\le 2\varepsilon.
\tag{9}
\]

Under `(4)` and `0<epsilon<1/2`, every such `sigma` satisfies `sigma<theta`. Equation `(7)` then gives

\[
\boxed{
\mathcal H_X(\sigma)^{1/2}
=
\exp\!\left((2+o(1))
\frac{X^{\theta-\sigma}}{\log X}
\right),
}
\tag{10}
\]

so the implicit transfer constant deteriorates faster than every fixed power of `X`. The fixed-function proposition remains correct for every frozen finite set `F_X`; what fails is the **uniformity in the scale-dependent matched-control family** required to turn it into an endpoint estimate at scale `X`.

This identifies the half-exponent information cost precisely. At target exponent `1/2+epsilon`, the prime-only `beta` route must inspect changed primes with weight roughly

\[
p^{-2\varepsilon},
\]

whereas the strong power-aware carrier in `MC-047` uses

\[
p^{-1/2-\varepsilon}.
\]

For the same slab, `MC-047` proved

\[
H_{1/2+\varepsilon}(\mu,\nu_X)
\asymp
\frac{P_X}{X^{1/2+\varepsilon}}
\asymp
\frac{\sum_{n\le X}\nu_X(n)-M(X)}{X^{1/2+\varepsilon}}.
\tag{11}
\]

By contrast, from `(2)` at `beta=2 epsilon`,

\[
\mathbb D_{2\varepsilon}(\mu,\nu_X;X)^2
\asymp
X^{1/2-\varepsilon}
\frac{P_X}{X^{1/2+\varepsilon}}.
\tag{12}
\]

Thus the prime-only route pays an extra polynomial factor `X^(1/2-epsilon)` on this exact control. That extra cost is the finite-scale shadow of the `(1+beta)/2` Cauchy--Schwarz exponent in the classical theorem.

## 1. Exact beta-distance of the terminal slab

At every prime outside `F_X`, `mu(p)=nu_X(p)=-1`. At every prime in `F_X`,

\[
\mu(p)=-1,
\qquad
\nu_X(p)=+1,
\]

so

\[
1-\Re(\mu(p)\overline{\nu_X(p)})=2.
\]

This proves the first equality in `(2)`. The short-interval prime asymptotic already audited in `MC-045` gives `P_X~X^theta/log X`, and `p=X(1+o(1))` uniformly across the slab, giving the second equality.

For `beta=1`, equation `(2)` reduces to the ordinary pretentious cost in `MC-045`, namely `X^(theta-1+o(1))`, which tends to zero. Lowering `beta` increases the cost of terminal primes. The exponent demanded by the power-cancellation theorem is not arbitrary: `(1+beta)/2` is exactly the transfer exponent in the completely multiplicative branch of Jung--Lemke Oliver Theorem 1.1, with optimality examples in that class. Solving `(1+beta)/2 <= 1/2+epsilon` gives `(3)`.

This is already enough to kill a proposed argument of the form "ordinary pretentiousness misses the endpoint, so use the same prime-only distance with a mildly stronger weight." At RH scale the theorem requires a radically stronger weight, approaching `p^0` as `epsilon` tends to zero.

## 2. Exact L2 convolution budget

For completeness, the direct Proposition-2.1 route can be audited without relying on the general Theorem-1.1 hypotheses. From `MC-047`, the local Dirichlet convolution quotient at a changed prime is

\[
1+2z+2z^2+\cdots.
\]

Squaring the absolute coefficients gives the local weighted `L2` factor

\[
1+4\sum_{k\ge1}p^{-k\sigma}
=
1+\frac{4p^{-\sigma}}{1-p^{-\sigma}}
=
\frac{1+3p^{-\sigma}}{1-p^{-\sigma}},
\]

which proves `(6)`.

If `u=p^{-sigma}`, then

\[
\log\frac{1+3u}{1-u}=4u+O(u^2).
\]

Since every changed prime is asymptotic to `X`, summing over `P_X` primes and dividing by two for the square root gives `(7)`.

The Cauchy step behind `(8)` is transparent. From `g=f*h`,

\[
|S_g(x)|
\ll
x^\alpha
\sum_{m\le x}\frac{|h(m)|}{m^\alpha}.
\]

Then

\[
\sum_{m\le x}\frac{|h(m)|}{m^\alpha}
\le
\left(\sum_m\frac{|h(m)|^2}{m^\sigma}\right)^{1/2}
\left(\sum_{m\le x}m^{\sigma-2\alpha}\right)^{1/2}.
\]

The second factor is bounded when `2 alpha>1+sigma` and otherwise contributes exactly the exponent `(1+sigma)/2`. This is the structural source of both `(8)` and the target condition `(9)`.

For each fixed finite `F_X`, `mathcal H_X(sigma)` is finite for every `sigma>0`, so no contradiction with Proposition 2.1 occurs. The issue is that a scale-dependent comparison needs constants controlled as `X` varies. Equation `(10)` shows that the required norm is catastrophically non-uniform in precisely the range capable of returning a square-root-scale exponent.

## 3. Relation to strong power-aware pretentiousness

Jung and Lemke Oliver introduced the stronger prime-power-sensitive framework precisely because the first `beta`-pretentious theory has a Cauchy barrier and because general multiplicative functions require control beyond prime values. Their Theorems 1.3--1.4 replace the `(1+beta)/2` target by `max(alpha,beta)` under stronger local hypotheses.

`MC-003` already showed, for Möbius versus Liouville, that this stronger framework reaches the square-layer threshold `beta=1/2` but does not create an independently easier comparator. `MC-047` then applied the strong carrier to the later terminal-prime matched control and found exact scale matching with the normalized endpoint defect.

The present finding closes the remaining temptation to retreat from that strong carrier to the apparently cheaper prime-only `beta` metric. On the terminal slab the prime-only theorem is not cheaper at all: to ask it for exponent `1/2+epsilon`, one must pay prime weight `p^(-2 epsilon)`, and the exact Cauchy kernel norm exposes the same failure as an exploding uniform constant. Strong power-aware pretentiousness asks for richer prime-power information, but its target exponent uses the natural target weight `p^(-1/2-epsilon)` and therefore matches the endpoint defect rather than overpaying it by a half exponent.

## 4. Prior art and novelty boundary

The source is Jung and Lemke Oliver, *Pretentiously detecting power cancellation* (`MC-S7`). The paper itself proves Theorem 1.1, its `(1+beta)/2` transfer exponent and optimality in the completely multiplicative class, Proposition 2.1 and its weighted `L2` Cauchy mechanism, and the later strong-pretentious Theorems 1.3--1.4. It explicitly motivates the strong theory by the limitations of the first `beta`-pretentious framework. None of those results is new here.

A targeted literature check around `beta`-pretentious power cancellation and Möbius found the Jung--Lemke Oliver paper as the directly adjacent primary source and no later theorem that removes the half-exponent transfer loss while retaining only the same prime-only `beta` datum. No novelty is claimed for the general obstruction.

The durable line-specific contribution is the exact **matched-control calibration** against `MC-045`--`MC-047`: equations `(2)`, `(7)`, `(10)`, and `(12)` quantify how the terminal-prime perturbation is seen by the first `beta`-pretentious framework, where the scale-dependent Proposition-2.1 constant fails, and why the strong power-aware carrier has the correct target normalization on the same control.

## 5. Boundaries and consequences

This finding is not a new bound for `M(x)` and is not a counterexample to Jung--Lemke Oliver. Their results concern fixed multiplicative functions; the terminal slab is a deliberately scale-dependent adversarial family. The family is used only to audit whether a proposed transfer theorem has the uniform information budget needed to explain an endpoint estimate at the same scale.

It also does not prove that every `L2` or quadratic convolution method is doomed. The obstruction applies to the direct absolute weighted-kernel Cauchy transfer. A method exploiting cancellation **inside** the convolution kernel, correlations between the kernel and the base summatory function, bilinear structure, or another non-Cauchy mechanism is outside the claim.

The consequence is a sharper hierarchy of surviving pretentious routes:

- ordinary `1/p` pretentiousness is too weak and misses coherent terminal-prime mass (`MC-045`);
- prime-only `beta`-pretentious power transfer detects that mass only by paying the classical half-exponent Cauchy cost quantified here;
- strong power-aware pretentiousness repairs that particular information mismatch (`MC-047`) but still needs an independently cancellative comparator or signed/multiscale structure.

Therefore the next useful pretentious-style question is not whether a different scalar prime weight can be tuned to the endpoint. The known frameworks already identify that tradeoff. A genuinely new route must reduce the transfer loss through signed/bilinear structure or find an arithmetic comparator whose strong power-aware relation to Möbius is independently controllable without carrying the same RH-scale cancellation hypothesis.