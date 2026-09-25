# VIS-433 — Chernoff-balanced Bernstein separators sharpen buffered hitting depth

## Claim

Let `(X,m)` carry a measure-preserving real flow `tau(u)`, let `Y:X->[0,1]`, and fix `0<a<b<1`. For `theta in (a,b)`, integer `d>=1`, and `M_d=ceil(d theta)`, define

`q_(d,theta)(x)=sum_(k=M_d)^d binom(d,k) x^k(1-x)^(d-k)`.

Write `D(r||p)=r log(r/p)+(1-r)log((1-r)/(1-p))` for Bernoulli relative entropy and

`I(theta;a,b)=min(D(theta||a),D(theta||b))`.

Then `0<=q_(d,theta)<=1`, and with `epsilon_(d,theta)=exp(-d I(theta;a,b))`,

`q_(d,theta)(x)<=epsilon_(d,theta)` for every `x<=a`, while

`q_(d,theta)(x)>=1-epsilon_(d,theta)` for every `x>=b`.

If `mu_b=m{Y>=b}` and `D_(d,theta)=(1-epsilon_(d,theta))mu_b-epsilon_(d,theta)>0`, then the buffered hitting argument of `VIS-430`--`VIS-432` gives

`m{H_a>rho} <= Var(L_(d,theta,rho)) / (Var(L_(d,theta,rho))+4rho^2 D_(d,theta)^2)`,

where `L_(d,theta,rho)(x)=int_(-rho)^rho q_(d,theta)(Y(x tau(u)))du`. It is enough that

`d > log((1+mu_b)/mu_b)/I(theta;a,b)`.

The best exponent in this thresholded-Bernstein family is obtained at the unique `theta_*(a,b)` satisfying `D(theta_*||a)=D(theta_*||b)`, namely

`theta_* = log((1-a)/(1-b)) / log(b(1-a)/(a(1-b)))`.

Thus

`C_Ber(a,b)=D(theta_*||a)=D(theta_*||b)`

is the Bernoulli Chernoff information, and the sufficient degree becomes

`d > log((1+mu_b)/mu_b)/C_Ber(a,b)`.

Pinsker gives `C_Ber(a,b)>=(b-a)^2/2`, so `VIS-432` is recovered as a universal quadratic lower bound while the Chernoff-balanced separator can be strictly stronger. For strict near-band Wang shells, `q_(d,theta_*)(X_N)` still has Laurent depth at most `d`, and the same estimate holds:

`Var(L_(d,theta_*,rho)) <= 4 * 9^d W_N^(4d)/(delta^*_(N,d))^2`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CHERNOFF INPUT + REPRESENTATION-CERTIFIED + QUANTITATIVE SHARPENING + NO-NOVELTY-CLAIM`.

No new general Chernoff theorem, hypothesis-testing theorem, Bernstein approximation theorem, mixing law, Wang selector anomaly, or RH consequence is claimed.

## 1. Binomial large deviations give the asymmetric separator

For `K~Bin(d,x)`, `q_(d,theta)(x)=P_x(K>=M_d)`. If `x<=a`, then `M_d/d>=theta>a>=x`. The standard binomial Chernoff bound gives

`P_x(K/d>=M_d/d)<=exp(-d D(M_d/d||x))`.

For `r>x`, `D(r||x)` increases with `r`; for fixed `r`, it decreases as `x` increases toward `r). Hence

`D(M_d/d||x)>=D(theta||a)`.

If `x>=b`, put `r_d=(M_d-1)/d<theta<b<=x`. The lower-tail Chernoff bound gives

`1-q_(d,theta)(x)<=exp(-d D(r_d||x))`.

For `r<x`, relative entropy decreases as `r` moves upward toward `x), while for fixed `r` it increases as `x` moves upward away from `r). Thus

`D(r_d||x)>=D(theta||b)`.

Taking the smaller exponent proves the separator.

## 2. The occupation and Wang reductions are unchanged

If `H_a(x)>rho`, then `Y(x tau(u))<a` for all `|u|<=rho`, so `L_(d,theta,rho)(x)<=2rho epsilon_(d,theta)`. Flow invariance gives `E[L]=2rho qbar`. On `{Y>=b}`, the separator gives `q_(d,theta)>=1-epsilon_(d,theta)`, hence

`qbar-epsilon_(d,theta)>=D_(d,theta)`.

Cantelli yields the claimed hitting bound. Positivity is equivalent to `epsilon_(d,theta)<mu_b/(1+mu_b)`, giving the stated degree requirement.

For Wang, scalar degree at most `d` means `q_(d,theta)(X_N)` contains only sums of at most `d` shell-frequency differences. The same monomial coefficient bound `<=3^d`, Wiener estimate, and `VIS-425` structural divisor therefore apply unchanged.

## 3. Balancing the two errors gives Chernoff information

For `theta in (a,b)`, `D(theta||a)` is strictly increasing from zero, whereas `D(theta||b)` is strictly decreasing to zero. Their minimum is therefore maximized uniquely at equality. Since

`D(theta||a)-D(theta||b)=theta log(b/a)+(1-theta)log((1-b)/(1-a))`,

solving for equality gives the displayed `theta_*`. The common divergence is the classical Bernoulli Chernoff information.

At the midpoint `c=(a+b)/2`, Pinsker gives

`D(c||a)>=2(c-a)^2=(b-a)^2/2`

and likewise `D(c||b)>=(b-a)^2/2`. Since `theta_*` maximizes the minimum divergence,

`C_Ber(a,b)>=I(c;a,b)>=(b-a)^2/2`.

Thus the Hoeffding exponent in `VIS-432` is a robust universal certificate, not the intrinsic exponent of this separator family.

## 4. What changes for the live Wang boundary

For `a=t^2`, `b=(t+eta)^2`, the rare-target depth remains logarithmic in `1/mu_b`, but its coefficient is now `1/C_Ber(a,b)` instead of the universal `2/(b-a)^2`. This is particularly relevant near the endpoints, where Bernoulli geometry is asymmetric and the Chernoff information can substantially exceed the quadratic floor.

The surviving source-sensitive obstruction is unchanged in kind: the actual Wang coefficient geometry must control the Wiener/small-divisor tariff at the resulting slowly growing depth. Failure of that sufficient tariff is not itself evidence of a source anomaly.

The endpoint cases `a=0` or `b=1` are excluded from the closed form only to avoid degenerate logarithms; one-sided limiting Chernoff bounds remain available.

## 5. Prior art, representation audit, and falsification

Herman Chernoff, **A Measure of Asymptotic Efficiency for Tests of a Hypothesis Based on the Sum of Observations**, *The Annals of Mathematical Statistics* 23:4 (1952), 493–507, DOI `10.1214/aoms/1177729330`, is the classical source for exponential-moment bounds and the optimal testing exponent. Hoeffding's 1963 inequalities provide the coarser bounded-sum specialization used in `VIS-432`. Bernoulli KL tail bounds and Chernoff information are classical.

No novelty is claimed for Chernoff bounds, Bernoulli relative entropy, Pinsker, Bernstein tail polynomials, Cantelli, or Wiener-algebra estimates. The Mathia delta is the quantitative audit of the existing Wang hitting certificate: optimize the already chosen thresholded Bernstein representation before charging its degree to the growing-depth arithmetic tariff.

The representation remains intrinsic to the normalized squared Wang amplitude and the actual prime-log translation flow. No image, colormap, raster scale, random surrogate, or visually tuned threshold enters this refinement.

Falsify the result by violating either binomial KL tail bound, the monotonicity comparisons, the balancing formula for `theta_*`, or the unchanged depth-`d` Wang frequency/Wiener reduction.

## Dependencies

- `VIS-425`: depth-`d` Wang structural divisor and strict near-band floor.
- `VIS-430`: occupation variance converts finite Fourier control into a hitting upper bound.
- `VIS-431`: buffered polynomial smoothing framework.
- `VIS-432`: thresholded Bernstein tail and the universal Hoeffding depth.

## Research consequence

For `0<a<b<1`, use the Chernoff-balanced threshold `theta_*(a,b)` and charge

`d > log((1+mu_b)/mu_b)/C_Ber(a,b)`.

Only after this optimized scalar separator has been priced should a growing-depth failure be attributed to the Wang Wiener mass, structural divisors, shrinking buffer, or another genuinely source-sensitive resource.
