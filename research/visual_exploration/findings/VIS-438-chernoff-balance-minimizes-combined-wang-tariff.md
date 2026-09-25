# VIS-438 — Chernoff balance also minimizes the combined exponential Wang tariff

## Claim

Fix `0<a<b<1`. Write `D_p(theta)=D(theta||p)` for Bernoulli relative entropy,

`I_(a,b)(theta)=min(D_a(theta),D_b(theta))`,  `a<theta<b`,

and let `theta_*` be the unique balance point `D_a(theta_*)=D_b(theta_*)`, equivalently

`theta_* = log((1-a)/(1-b)) / log(b(1-a)/(a(1-b)))`.

For `z>=1` and `kappa>=0`, define

`C_(z,kappa)(theta)=Psi_z(theta)+kappa`,

where the exact Wiener-rate function from `VIS-437` is

`Psi_z(theta)=H(theta)+theta log z+(1-theta)log(1+z)`.

Then

`R_(z,kappa)(theta)=C_(z,kappa)(theta)/I_(a,b)(theta)`

is strictly decreasing on `(a,theta_*]` and strictly increasing on `[theta_*,b)`. Hence its unique global minimum is `theta_*`, independently of `z>=1` and every nonnegative `theta`-independent per-depth charge `kappa`.

For the rare-target separator of `VIS-433`, put `L_mu=log((1+mu_b)/mu_b)`. The continuous depth condition is `d I_(a,b)(theta)>L_mu`. With fixed `a,b,z` and fixed `Y>=1`, `VIS-437` and the strict near-band divisor floor give

`limsup_(mu_b->0) [1/L_mu] log Var(L_(d,theta,rho)) <= [2 Psi_z(theta)+4 log(2Y)]/I_(a,b)(theta)`

for asymptotically minimal admissible depth, up to vanishing integer-depth and strict-inequality slack. The right-hand side is uniquely minimized at `theta_*`.

Thus the threshold-specific Wiener sharpening in `VIS-437` does not create an exponential-rate optimum away from the Chernoff balance point.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FRACTIONAL-PROGRAMMING BACKGROUND + ASYMPTOTIC TARIFF OPTIMIZATION + REPRESENTATION-CERTIFIED + NO-NOVELTY-CLAIM`.

No exact finite-degree optimizer, uniform changing-shell asymptotic, new fractional-programming theorem, new Chernoff theorem, improved Wang small-divisor bound, selector anomaly, or RH consequence is claimed.

## 1. Chernoff branch structure

The difference

`D_a(theta)-D_b(theta)=theta log(b/a)+(1-theta)log((1-b)/(1-a))`

is affine, negative at `a`, positive at `b`, and vanishes uniquely at `theta_*`. Therefore `I_(a,b)=D_a` on the left branch and `I_(a,b)=D_b` on the right branch. `D_a` is positive, strictly increasing and strictly convex for `theta>a` with `D_a(a)=0`; `D_b` is positive, strictly decreasing and strictly convex for `theta<b` with `D_b(b)=0`.

## 2. Concave/convex ratio lemma

Let `f` be positive and concave on `[a,b]`, and let `g` be positive and convex on `(a,b]` with `g(a)=0`. Then

`f'(x) <= [f(x)-f(a)]/(x-a) < f(x)/(x-a)`

while

`g'(x) >= g(x)/(x-a)`.

Hence `f'/f<g'/g`, so `(f/g)'<0`. Reflecting the interval gives the symmetric statement: if `g` is positive and convex on `[a,b)` with `g(b)=0`, then `f/g` is strictly increasing.

Apply the left statement with `f=C_(z,kappa)` and `g=D_a`, and the reflected statement with `g=D_b`. Since `H` is strictly concave and the remaining terms in `Psi_z` are affine, `C_(z,kappa)` is concave. For `z>=1`, `0<theta<1`, and `kappa>=0`, it is positive. This proves the unique minimum at `theta_*`.

## 3. Wang specialization

`VIS-433` gives separator leakage `epsilon_(d,theta)=exp(-d I_(a,b)(theta))` and sufficient positivity `d I_(a,b)(theta)>L_mu`. `VIS-437` gives, for `M_d/d->theta` and fixed `z>0`,

`log A_(d,M_d)(z)=d Psi_z(theta)+o(d)`.

For a strict near-band shell with `z=W^2>=1`,

`Var(L) <= 4 A_(d,M_d)(z)^2 (2Y)^(4d)`.

Hence `log Var(L) <= 2d[Psi_z(theta)+2 log(2Y)]+o(d)`. When `mu_b->0` with fixed `a,b,z,Y`, asymptotically minimal depth is `d=L_mu/I_(a,b)(theta)+o(L_mu)`, yielding the normalized exponent in the claim with `kappa=2 log(2Y)`.

Any additional positive exponential per-depth penalty independent of the threshold fraction only increases `kappa` and cannot move the minimizer.

## 4. Boundary

The result closes only the exponential-rate tradeoff left open by `VIS-437`. It is not an exact discrete optimization theorem for finite `d`: the ceiling `M=ceil(d theta)`, the exact finite `A_(d,M)(z)`, strict positivity slack, and other nonexponential terms can move a finite-degree optimum. If `z=W_N^2`, `Y_N`, the buffer, or target law vary jointly with `N`, the fixed-parameter asymptotic is not automatically uniform.

A different optimum can therefore arise only from information not represented by this positive concave per-depth certificate: a `theta`-dependent source-specific divisor improvement, cancellation inside actual Fourier coefficients beyond the Wiener majorant, finite-depth discrete effects, a changing endpoint regime, or another separator family.

## 5. Prior art, representation audit, and falsification

Optimization of ratios involving convex and concave functions belongs to classical fractional programming. Siegfried Schaible, **Fractional Programming. I, Duality**, *Management Science* 22:8 (1976), 858–867, DOI `10.1287/mnsc.22.8.858`, develops the classical concave-convex fractional-programming framework.

No general fractional-programming novelty is claimed. The Mathia step is the elementary one-dimensional endpoint lemma above, specialized to the persisted Chernoff leakage denominator and Bernstein/Wiener exponential numerator. Bernoulli KL and Chernoff are classical; the thresholded Bernstein coefficient rate is the internal input from `VIS-437`.

No plot, colormap, finite raster, sampled parameter search, or post-hoc threshold choice enters the derivation.

Falsify the finding by violating the KL branch decomposition, the ratio monotonicity inequalities, positivity/concavity of the charged per-depth tariff, or the substitution of the `VIS-437` rate and `VIS-425` divisor factor into the rare-target depth requirement.

## Dependencies

- `VIS-425`: strict near-band depth-`d` structural divisor floor.
- `VIS-433`: Chernoff-balanced separator and rarity-depth coefficient.
- `VIS-437`: exact threshold-specific Bernstein/Wiener majorant and exponential rate.

## Research consequence

Within the current thresholded-Bernstein Wang hitting certificate, keep the Chernoff-balanced threshold `theta_*` when minimizing the combined exponential rarity, Wiener, and theta-independent structural-divisor tariff. Re-optimizing the scalar threshold after `VIS-437` does not buy an exponential improvement.

The next independent question must therefore attack source-sensitive structure omitted by the positive Wiener majorant or elementary divisor floor, or move to a regime where the fixed-parameter exponential reduction is no longer valid.