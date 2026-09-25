# VIS-437 — thresholded Bernstein tails have an exact weighted Wiener majorant

## Claim

For integers `1<=M<=d`, define the thresholded Bernstein tail

`q_(d,M)(x)=sum_(k=M)^d binom(d,k)x^k(1-x)^(d-k)`.

Its power-basis expansion is exactly

`q_(d,M)(x)=sum_(j=M)^d (-1)^(j-M) binom(d,j) binom(j-1,M-1) x^j`.

Hence for every `z>=0` the weighted power-coefficient majorant

`A_(d,M)(z):=sum_(j=M)^d binom(d,j)binom(j-1,M-1)z^j`

has the exact representations

`A_(d,M)(z)=binom(d,M) z^M sum_(r=0)^(d-M) [M/(M+r)] binom(d-M,r) z^r`

and

`A_(d,M)(z)=M binom(d,M) z^M int_0^1 u^(M-1)(1+zu)^(d-M)du`.

For `z>0`,

`(M/d) binom(d,M) z^M(1+z)^(d-M) <= A_(d,M)(z) <= binom(d,M) z^M(1+z)^(d-M) <= (1+2z)^d`.

If `M_d/d -> theta in (0,1)` and `z>0` is fixed, then

`lim_(d->infinity) (1/d)log A_(d,M_d)(z)=Psi_z(theta)`

with

`Psi_z(theta)=H(theta)+theta log z+(1-theta)log(1+z)=log(1+2z)-D(theta || z/(1+2z))`.

Thus the worst exponential rate over threshold fractions occurs at `theta=z/(1+2z)`.

For the strict near-band Wang shells, let

`X_N=|F_N|^2/S_N^2`,  `W_N=(sum_a |b_(N,a)|)/S_N`.

Since `||X_N||_A<=W_N^2`, the thresholded Bernstein observable obeys

`||q_(d,M)(X_N)||_A <= A_(d,M)(W_N^2)`.

Consequently the occupation variance used in `VIS-430`--`VIS-436` satisfies

`Var(L_(d,M,rho)) <= 4 A_(d,M)(W_N^2)^2/(delta^*_(N,d))^2`.

Using the strict near-band divisor floor from `VIS-425`,

`delta^*_(N,d)>=(2Y_N)^(-2d)`,

gives

`Var(L_(d,M,rho)) <=4 A_(d,M)(W_N^2)^2 (2Y_N)^(4d)`.

In particular,

`A_(d,M)(W_N^2) <= (1+2W_N^2)^d <= (3W_N^2)^d`

because `W_N>=1`. This uniformly improves the earlier `3^d W_N^(2d)` bound whenever `W_N>1`. Even at `W_N=1`, a fixed threshold fraction has exponential rate

`Psi_1(theta)=log 3-D(theta||1/3)`,

so the old `3^d` coefficient tariff is exponentially sharp only at `theta=1/3` and exponentially loose for every fixed `theta!=1/3`.

For the Chernoff-balanced separator of `VIS-433`, `M_d=ceil(d theta_*(a,b))`. Therefore, whenever `W_N^2` has a fixed limiting value `z`, its scalar/Wiener exponential tariff is `Psi_z(theta_*)`, not the previously charged `log 3+log z`. For changing `W_N`, the finite exact quantity `A_(d,M)(W_N^2)` remains the valid certificate without any fixed-`z` asymptotic assumption.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL BERNSTEIN BASIS CONVERSION + REPRESENTATION-TARIFF SHARPENING + ASYMPTOTIC RATE + NO-NOVELTY-CLAIM`.

No new general Bernstein-basis theorem, binomial-tail theorem, Chernoff theorem, Wang selector anomaly, small-divisor estimate, or RH consequence is claimed.

## 1. Exact power coefficients of a Bernstein tail

The coefficient of `x^j` in `q_(d,M)`, for `j>=M`, is

`sum_(k=M)^j binom(d,k) binom(d-k,j-k)(-1)^(j-k)`.

Using

`binom(d,k)binom(d-k,j-k)=binom(d,j)binom(j,k)`,

this becomes

`binom(d,j) sum_(k=M)^j binom(j,k)(-1)^(j-k)`.

The alternating partial-binomial identity gives

`sum_(k=M)^j binom(j,k)(-1)^(j-k)=(-1)^(j-M)binom(j-1,M-1)`,

which proves the claimed coefficient formula. In particular, the nonzero monomial coefficients alternate in sign and their absolute values are explicit.

This matters because `VIS-431`--`VIS-436` bounded every thresholded Bernstein polynomial by summing the absolute monomial coefficients of all Bernstein basis terms separately. That triangle inequality produced the convenient but coarse `3^d` factor before the actual threshold `M` was used.

## 2. The exact weighted coefficient tariff

Set `j=M+r`. The binomial identity

`binom(d,M+r)binom(M+r-1,M-1)=binom(d,M) [M/(M+r)] binom(d-M,r)`

gives the weighted-sum representation of `A_(d,M)(z)`.

Since

`M/(M+r)=M int_0^1 u^(M+r-1)du`,

finite interchange yields the integral representation in the claim.

For `0<=r<=d-M`,

`M/d <= M/(M+r) <=1`.

Multiplying the binomial sum by these endpoint bounds proves the two-sided estimate with

`binom(d,M)z^M(1+z)^(d-M)`.

Finally that upper term is one summand of

`[z+(1+z)]^d=(1+2z)^d`,

so the uniform bound follows.

## 3. Threshold fraction determines the exponential price

For fixed `z>0` and `M_d/d->theta in (0,1)`, the lower and upper bounds differ only by the nonexponential factor `M_d/d`. Stirling's formula therefore gives

`(1/d)log A_(d,M_d)(z) -> H(theta)+theta log z+(1-theta)log(1+z)`.

Writing `p_z=z/(1+2z)` turns this into

`Psi_z(theta)=log(1+2z)-D(theta||p_z)`.

Thus the exact threshold-specific coefficient tariff has an information-geometric penalty away from `p_z`. At `z=1`, the universal `3^d` rate occurs only at `theta=1/3`; every other fixed threshold fraction saves the exponential factor `exp[-dD(theta||1/3)+o(d)]`.

This is a coefficient-space statement, not a probabilistic approximation statement. The relative entropy appears because the exact absolute power coefficients form a binomially weighted profile, not because a new hypothesis-testing argument has been introduced.

## 4. Wang specialization

The normalized squared shell amplitude satisfies `||X_N||_A<=W_N^2`. By Wiener-algebra submultiplicativity and the exact power coefficients,

`||q_(d,M)(X_N)||_A <=sum_(j=M)^d |c_j| ||X_N||_A^j <=A_(d,M)(W_N^2)`.

Every nonconstant character of `q_(d,M)(X_N)` still has mixed depth at most `d`, so the same structural divisor `delta^*_(N,d)` from `VIS-425` applies. In the exact occupation-variance identity of `VIS-430`,

`Var(L)=4 sum_(m!=0)|chat_m|^2 sin^2(rho lambda_m)/lambda_m^2`,

use `sin^2<=1`, `|lambda_m|>=delta^*_(N,d)`, and

`sum_(m!=0)|chat_m|^2 <= (sum_(m!=0)|chat_m|)^2 <= ||q_(d,M)(X_N)||_A^2`.

This proves the Wang variance bounds in the claim.

The new estimate changes only the Wiener/coefficient side of the tariff. It does not improve `VIS-425`'s structural small-divisor floor, which still contributes `(2Y_N)^(4d)` in the elementary strict near-band certificate.

## 5. Prior art, representation audit, and falsification

Bernstein/power-basis conversion is classical. Weikang Qian, Marc D. Riedel, and Ivo Rosenberg, **Uniform approximation and Bernstein polynomials with coefficients in the unit interval**, *European Journal of Combinatorics* 32:3 (2011), 448--463, DOI `10.1016/j.ejc.2010.11.004`, explicitly records the relation between power-form and Bernstein-form coefficients. Lorentz's monograph and the Bernstein sources already recorded for `VIS-431`--`VIS-432` delimit the broader approximation-theory background.

No novelty is claimed for basis conversion, alternating binomial identities, Stirling asymptotics, Bernoulli relative entropy, Wiener-algebra submultiplicativity, or Bernstein tail polynomials. The Mathia delta is the exact threshold-tail specialization and its use to remove avoidable coefficient inflation from the live Wang growing-depth certificate.

The representation is intrinsic to the already chosen thresholded Bernstein separator and normalized squared Wang amplitude. No raster, color map, sampling window, or visually tuned parameter enters the derivation.

Falsify the result by violating the exact power coefficient formula, the weighted-sum/integral identity for `A_(d,M)`, either two-sided bound, the asymptotic rate `Psi_z`, the Wiener substitution `z=W_N^2`, or the unchanged depth-`d` structural-divisor step.

## Dependencies

- `VIS-425`: depth-`d` Wang structural divisor and strict near-band floor.
- `VIS-430`: occupation variance converts finite Fourier control into a hitting upper bound.
- `VIS-432`: thresholded Bernstein tail and the earlier uniform `3^d` coefficient tariff.
- `VIS-433`: Chernoff-balanced threshold fraction.
- `VIS-436`: closes large scalar gains from merely optimizing the Chernoff/Bhattacharyya exponent.

## Research consequence

The `3^d W_N^(2d)` Wiener factor used through `VIS-431`--`VIS-436` is not the intrinsic growing-depth price of a thresholded Bernstein separator. Replace it by the exact finite tariff `A_(d,M)(W_N^2)`; for fixed threshold fraction and fixed Wiener scale its exponential rate is `Psi_z(theta)`.

This materially narrows the surviving Wang obstruction: part of the apparent exponential growth came from an avoidable basis-level triangle inequality, while the structural small-divisor factor remains untouched. A separate next question is whether one should optimize the combined separator-leakage and Wiener tariffs rather than the Chernoff leakage exponent alone; that question is not needed for the present result and is left outside this invocation.
