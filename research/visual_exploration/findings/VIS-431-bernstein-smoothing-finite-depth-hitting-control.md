# VIS-431 — Bernstein smoothing converts buffered hitting to finite-depth Laurent control

## Claim

Let `(X,m)` carry a measure-preserving real flow `tau(u)`, let `Y:X->[0,1]`, and fix

`0<=a<b<=1`.

Define the ramp

`r_(a,b)(x)=0` for `x<=a`,
`r_(a,b)(x)=(x-a)/(b-a)` for `a<x<b`,
and `r_(a,b)(x)=1` for `x>=b`.

For an integer `d>=1`, let `q_d=B_d r_(a,b)` be the degree-`d` Bernstein approximation

`q_d(x)=sum_(k=0)^d r_(a,b)(k/d) binom(d,k) x^k(1-x)^(d-k)`.

Then `0<=q_d<=1` and

`||q_d-r_(a,b)||_infinity <= epsilon_d := 1/(2(b-a)sqrt(d))`.

Put

`L_(d,rho)(x)=int_(-rho)^rho q_d(Y(x tau(u)))du`

and

`qbar_d=int_X q_d(Y)dm`.

For `rho>0`, if `qbar_d>epsilon_d`, then the hitting time

`H_a(x)=inf{|u|:Y(x tau(u))>=a}`

satisfies

`m{H_a>rho} <= Var(L_(d,rho)) / ( Var(L_(d,rho)) + [2rho(qbar_d-epsilon_d)]^2 )`.

If

`mu_b=m{Y>=b}`,

then

`qbar_d-epsilon_d >= (1-epsilon_d)mu_b-epsilon_d`.

Hence whenever

`D_d:=(1-epsilon_d)mu_b-epsilon_d>0`,

the same hitting tail is bounded by

`m{H_a>rho} <= Var(L_(d,rho)) / ( Var(L_(d,rho)) + 4rho^2 D_d^2 )`.

For the strict near-band Wang shells, take

`Y=X_N=|F_N|^2/S_N^2`,
`a=t^2`,
`b=(t+eta)^2`

with `0<=t<t+eta<=1`. Then `q_d(X_N)` is a finite Laurent polynomial of depth at most `d`. If

`W_N=(sum_a |b_(N,a)|)/S_N`

and `delta^*_(N,d)` is the structural mixed divisor from `VIS-425`, its nonconstant Fourier mass obeys

`sum_(m!=0)|c_(N,d,m)| <= 3^d W_N^(2d)`,

and therefore

`Var(L_(d,rho)) <= 4 * 9^d W_N^(4d) / (delta^*_(N,d))^2`.

Using the strict near-band arithmetic floor

`delta^*_(N,d) >= (2Y_N)^(-2d)`

gives the explicit source-independent bound

`Var(L_(d,rho)) <= 4 * 9^d W_N^(4d) (2Y_N)^(4d)`.

Thus `VIS-430`'s hard-target indicator can be replaced by a **fixed finite-depth Laurent observable** whenever the threshold buffer and higher-target Haar mass permit one fixed `d`. Conversely, the elementary Bernstein error already shows why a genuinely rare or shrinking target escapes this reduction: a sufficient condition for `D_d>0` is

`d > (1+mu_b)^2 / [4(b-a)^2 mu_b^2]`.

If `mu_b->0` or `b-a->0`, the required smoothing depth diverges, pushing the problem into the growing-moment / growing-small-divisor regime rather than closing it by fixed-depth character control.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL BERNSTEIN/CANTELLI INPUT + REPRESENTATION-CERTIFIED + QUANTITATIVE BOUNDARY + NO-NOVELTY-CLAIM`.

No new general approximation theorem, hitting-time theorem, mixing law, Wang selector anomaly, or RH consequence is claimed.

## 1. Quantitative Bernstein smoothing of a buffered threshold

The ramp `r_(a,b)` is `1/(b-a)`-Lipschitz. If `K~Bin(d,x)`, the Bernstein operator has the probabilistic representation

`q_d(x)=E[r_(a,b)(K/d)]`.

Therefore

`|q_d(x)-r_(a,b)(x)|`
` <= (1/(b-a)) E|K/d-x|`
` <= (1/(b-a)) sqrt(Var(K/d))`
` <= 1/(2(b-a)sqrt(d))`.

The Bernstein basis is nonnegative and sums to one, while the ramp takes values in `[0,1]`, so `q_d` also takes values in `[0,1]`.

This is a standard quantitative form of classical Bernstein approximation; the proof is included because the exact dependence on the buffer `b-a` and degree `d` is the load-bearing quantity for the Wang specialization.

## 2. Soft occupation controls the hard lower target

If `H_a(x)>rho`, then

`Y(x tau(u))<a`

for every `|u|<=rho`. Since the ramp is zero on `[0,a]` and `q_d` is uniformly within `epsilon_d` of the ramp,

`q_d(Y(x tau(u)))<=epsilon_d`

throughout the window. Hence

`H_a(x)>rho => L_(d,rho)(x)<=2rho epsilon_d`.

By invariance,

`E[L_(d,rho)]=2rho qbar_d`.

Cantelli's one-sided variance inequality applied to the lower tail then gives

`m{L_(d,rho)<=2rho epsilon_d}`
` <= Var(L_(d,rho)) / ( Var(L_(d,rho)) + [2rho(qbar_d-epsilon_d)]^2 )`.

Combining the two statements proves the first hitting bound.

On the upper target `{Y>=b}`, the ramp equals one, so the uniform approximation gives

`q_d>=1-epsilon_d`.

Since `q_d>=0` everywhere,

`qbar_d >= (1-epsilon_d)mu_b`.

Subtracting `epsilon_d` yields the displayed explicit denominator `D_d`.

The buffer is structural rather than cosmetic. A continuous polynomial cannot equal a nonzero hard indicator while vanishing on an interval. The price of replacing the indicator by finite polynomial depth is exactly a nonzero threshold gap plus enough target mass to dominate the approximation leakage.

## 3. Wang shells turn the smoothed target into finite Laurent depth

For the Wang shell,

`X_N=|F_N|^2/S_N^2`

is a Laurent polynomial on the base-prime torus. Its Wiener norm satisfies

`||X_N||_A <= W_N^2`.

Write the scalar Bernstein polynomial in monomials,

`q_d(x)=sum_(j=0)^d alpha_(d,j)x^j`.

Each Bernstein basis term has monomial coefficient `l^1`-norm

`binom(d,k) 2^(d-k)`.

Because every sampled ramp value lies in `[0,1]`,

`sum_(j=0)^d |alpha_(d,j)|`
` <= sum_(k=0)^d binom(d,k)2^(d-k)`
` =3^d`.

Also `W_N>=1`, because the torus supremum of `F_N` is at most its coefficient `l^1`-norm. Submultiplicativity of the Wiener algebra therefore gives

`||q_d(X_N)||_A <= 3^d W_N^(2d)`.

Every Fourier frequency occurring in `X_N^j` is a sum of at most `j<=d` shell-frequency differences. Padding with zero differences if necessary places every nonzero frequency under the `VIS-425` depth-`d` structural divisor. Hence

`|lambda_m|>=delta^*_(N,d)`

for every nonconstant character of `q_d(X_N)`.

The exact torus-translation variance identity from `VIS-430` applied to the centered polynomial gives

`Var(L_(d,rho)) =4 sum_(m!=0)|c_(N,d,m)|^2 sin^2(rho lambda_m)/lambda_m^2`.

Using `sin^2<=1`, the divisor floor, and `sum |c_m|^2<=(sum |c_m|)^2` proves

`Var(L_(d,rho)) <= 4 * 9^d W_N^(4d)/(delta^*_(N,d))^2`.

For strict near-band shells, `VIS-425` gives

`delta^*_(N,d)>=(2Y_N)^(-2d)`,

which yields the explicit arithmetic-height form in the claim.

## 4. Fixed depth closes buffered non-rare targets, not shrinking targets

For amplitude thresholds, the scalar gap is

`b-a=(t+eta)^2-t^2=eta(2t+eta)`.

If `t`, `eta`, and the higher-target mass `mu_N(t+eta)` stay uniformly away from their degenerate limits, one can choose `d` once so that

`D_d=(1-epsilon_d)mu_N(t+eta)-epsilon_d`

is uniformly positive. The hard-target hitting upper bound then depends only on a fixed-depth Laurent polynomial and the corresponding fixed-depth Wang small divisors.

This is the regime in which the apparent infinite Fourier complexity of the superlevel indicator in `VIS-430` is not an independent escape mechanism.

The situation changes when the target becomes rare or the threshold buffer shrinks. Since

`D_d>0 iff epsilon_d < mu_b/(1+mu_b)`,

the elementary error estimate gives the sufficient degree requirement

`d > (1+mu_b)^2/[4(b-a)^2 mu_b^2]`.

Thus `mu_b->0` or `b-a->0` forces the available finite-depth certificate toward larger degree. In the Wang bound, that simultaneously raises the Wiener factor `W_N^(4d)` and the structural divisor tariff `(2Y_N)^(4d)`.

The remaining shrinking-target branch is therefore not merely "the indicator has infinitely many Fourier modes." Its concrete resource is that resolving a small target mass or narrow threshold buffer requires increasing polynomial depth, exactly where the existing fixed-order moment and small-divisor machinery stops being uniform.

## 5. Prior art, representation audit, and falsification

Bernstein-polynomial approximation is classical. G. G. Lorentz's monograph *Bernstein Polynomials* gives the standard approximation-theory background. Tiangang Cui and Friedrich Pillichshammer, **Bernstein approximation and beyond: Proofs by means of elementary probability theory**, *Elemente der Mathematik* 81:1 (2026), 1--7, DOI `10.4171/EM/548`, explicitly develops the probabilistic representation and Lipschitz error estimates used here. Cantelli's one-sided Chebyshev inequality is also classical.

The Mathia content is only the exact specialization: use a buffered Bernstein ramp to replace the Wang hard superlevel indicator by a finite-depth polynomial in the intrinsic normalized squared amplitude, then combine `VIS-425`'s structural divisor with `VIS-430`'s occupation variance identity. No novelty is claimed for Bernstein approximation, Cantelli, Wiener-algebra submultiplicativity, or Fourier variance formulas separately.

The representation is intrinsic. The statistic uses the normalized squared shell amplitude and the actual prime-log translation flow. No colormap, finite raster, arbitrary embedding, random-phase surrogate, or plotted threshold enters the proof.

Falsify the result by exhibiting a failure of the Bernstein error bound, a hard-target avoidance path whose smoothed occupation exceeds `2rho epsilon_d`, a violation of Cantelli's lower-tail step, a Fourier character of `q_d(X_N)` outside depth `d`, failure of the Wiener bound `3^d W_N^(2d)`, or a strict near-band shell violating the `VIS-425` structural divisor floor.

## Dependencies

- `VIS-419`: fixed Wang shells live on the base-prime torus with Haar as the translation self-null.
- `VIS-425`: squared amplitude has Wiener norm `<=W_N^2` and depth-`d` nonzero frequencies satisfy the structural divisor bound, with the explicit strict near-band floor.
- `VIS-429`: target rarity gives the complementary lower quiet-tail control.
- `VIS-430`: occupation variance gives the hard-target upper-tail route but leaves the indicator Fourier complexity unresolved.

## Research consequence

The pre-saturation Wang branch now has a finite-depth decision boundary. For buffered targets whose higher-level Haar mass is not too small, choose a fixed Bernstein degree, compute or bound the finite Laurent variance, and compare the selected quiet interval to the resulting exact Haar upper bound. In that regime, the hard indicator itself is no longer a reason to invoke uncontrolled infinite Fourier structure.

If the required degree grows because the target mass vanishes or the threshold buffer shrinks, do not pretend that fixed-order character tariffs close the problem. That is precisely the surviving growing-moment/small-divisor regime. The next independent question would be whether the actual Wang coefficient geometry can control that growing depth; it is not needed to establish the present finite-depth boundary.
