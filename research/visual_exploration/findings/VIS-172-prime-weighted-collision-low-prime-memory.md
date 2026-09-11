# VIS-172 — critical-line amplitude weighting preserves non-Gaussian low-prime memory in the Haar collision null

## Claim

Consider the held-out-phase collision geometry of `VIS-164`--`VIS-171`, but replace the equal coordinate weights by the square of the first-order critical-line Euler amplitude. For primes `p<=x`, let

`w_p = 1/p`,

let `X_p` and `Y` be independent Haar-uniform variables on `T`, and put

`U_p = sin^2(pi X_p)`,

`W_x = sum_(p<=x) w_p`,

`Q_x = sum_(p<=x) w_p^2`,

`A_x = W_x^(-1) sum_(p<=x) w_p U_p`,

`N = |sin(pi Y)|`,

`C_x = N / sqrt(sum_(p<=x) w_p U_p)`.

Then the weighted Haar null has a different bulk-fluctuation regime from the equal-weight null.

First,

`sqrt(W_x) C_x = N / sqrt(A_x) -> sqrt(2) N`

in probability, so the raw weighted collision bulk contracts at scale `W_x^(-1/2)`. By Mertens' reciprocal-prime asymptotic,

`W_x = log log x + B_1 + o(1)`,

hence the bulk scale is only `(log log x)^(-1/2)`.

Second, define

`S_x = sum_(p<=x) p^(-1) (U_p-1/2)`.

Because

`sum_p p^(-2) < infinity`,

the partial sums `S_x` converge in `L^2` to a non-degenerate random variable

`S_infinity = sum_p p^(-1)(U_p-1/2)`.

With

`h(a) = 1/sqrt(2a)`,

one has the sharper relative limit

`W_x (h(A_x)-1) -> -S_infinity`

in probability. Equivalently, if

`d_eff(x) = W_x^2 / Q_x`,

then

`sqrt(d_eff(x)) (h(A_x)-1) -> R := -S_infinity/sqrt(P(2))`,

where

`P(2)=sum_p p^(-2)`.

The limit `R` is **not Gaussian**. Its characteristic function is

`E[e^(itR)] = product_p J_0(t / (2 p sqrt(P(2))))`,

where `J_0` is the ordinary Bessel function. It has

`Var(R)=1/8`,

but fourth cumulant

`kappa_4(R) = - 3 P(4) / (128 P(2)^2) != 0`,

with `P(4)=sum_p p^(-4)`.

Thus a prime-amplitude-weighted collision plot can display a persistent non-Gaussian standardized bulk even under completely independent Haar phases. The effect is not source information: it is forced by the square-summable `1/p` taper, which leaves a permanent low-prime contribution after normalization.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-MERTENS/LINDEBERG-BOUNDARY + WEIGHTED-HAAR-NULL + NEGATIVE-CONTROL + NO-NOVELTY-CLAIM`.

This is a representation/null theorem. It is not a convergence statement for the critical-line Euler product, a deterministic prime-log equidistribution theorem in growing dimension, a zeta-versus-control separation, or an RH consequence.

## 1. Why `1/p` is the relevant test weight

For a finite prime truncation on `Re(s)=1/2`, the first prime harmonic has amplitude proportional to `p^(-1/2)`. A Euclidean phase perturbation weighted by squared first-order amplitude therefore assigns coordinate weight `p^(-1)`.

The present finding studies exactly that finite-dimensional representation choice. It does not assert that this weighted metric is canonical, and it does not use the divergent critical-line Euler product as an analytic identity. The point is adversarial: if a visual statistic chooses this natural-looking amplitude taper, its null must be calibrated with the same taper rather than with the equal-weight law of `VIS-169`--`VIS-171`.

## 2. Weighted concentration still produces a stable bulk

Since `E[U_p]=1/2`,

`A_x-1/2 = S_x/W_x`.

Also

`E[S_x^2] = (1/8) Q_x`.

The reciprocal-prime series diverges, while `Q_x` converges to the finite constant `P(2)`. Therefore

`E[(A_x-1/2)^2] = Q_x/(8W_x^2) -> 0`,

so `A_x -> 1/2` in `L^2` and in probability. Consequently

`sqrt(W_x) C_x = N/sqrt(A_x) -> sqrt(2)N`

in probability.

There is also an exact weighted Hoeffding envelope. Since each summand `w_p U_p/W_x` has range length `w_p/W_x`,

`P(|A_x-1/2| >= delta)`
` <= 2 exp(-2 delta^2 W_x^2/Q_x)`
` = 2 exp(-2 delta^2 d_eff(x))`.

Thus `d_eff=W_x^2/Q_x` really is the concentration dimension of this weighted average.

## 3. The first relative fluctuation is an infinite low-prime series

The centered partial sums `S_x` are Cauchy in `L^2`, because for `y>x`,

`E[|S_y-S_x|^2] = (1/8) sum_(x<p<=y) p^(-2) -> 0`.

Hence `S_x -> S_infinity` in `L^2`.

Now

`A_x = 1/2 + S_x/W_x`.

The map `h(a)=(2a)^(-1/2)` satisfies

`h(1/2)=1`,

`h'(1/2)=-1`.

On any fixed neighborhood of `1/2`, Taylor's theorem gives

`h(1/2+u)-1 = -u + O(u^2)`.

Since `S_x=O_P(1)` and `W_x->infinity`,

`W_x(h(A_x)-1)`
` = -S_x + O_P(S_x^2/W_x)`
` -> -S_infinity`.

This identifies the actual first correction to the bulk law. Equal weights produced a central-limit fluctuation of order `d^(-1/2)` in `VIS-170`; the `1/p` taper instead freezes the centered numerator into a convergent random series and pushes the relative correction down to order `W_x^(-1)`.

## 4. Effective dimension grows but Gaussianity fails

Because `Q_x -> P(2)>0`,

`d_eff(x) = W_x^2/Q_x`

satisfies

`d_eff(x) ~ (log log x)^2/P(2)`.

If one looked only at this diverging effective dimension and the Hoeffding envelope, a Gaussian standardized null might look plausible. The triangular-array negligibility condition fails, however:

`max_(p<=x) w_p / sqrt(Q_x)`
` = (1/2)/sqrt(Q_x)`
` -> 1/(2 sqrt(P(2))) > 0`.

The smallest primes never become negligible relative to the total quadratic weight. This is exactly the regime excluded by the asymptotic-negligibility side of the classical Lindeberg--Feller theory.

The normalized relative fluctuation therefore converges not to a fresh Gaussian, but to

`R = -S_infinity/sqrt(P(2))`.

Its variance is still `1/8`, so variance alone cannot detect the failure of the Gaussian null.

## 5. The limit law is explicitly non-Gaussian

Write

`X_p = U_p-1/2 = -(1/2) cos(2 pi X_p)`.

For one Haar coordinate,

`E[X_p]=0`,

`E[X_p^2]=1/8`,

`E[X_p^4]=3/128`,

so its fourth cumulant is

`3/128 - 3(1/8)^2 = -3/128`.

Independence and absolute fourth-power summability give

`kappa_4(S_infinity) = -(3/128) sum_p p^(-4)`.

After normalization by `sqrt(P(2))`,

`kappa_4(R) = -3P(4)/(128P(2)^2)`,

which is strictly negative. Therefore `R` is not Gaussian.

The full characteristic function is also explicit. Since the characteristic function of `-(a/2) cos(theta)` with uniform `theta` is `J_0(at/2)`, finite independence gives a product over primes, and the `L^2` limit yields

`phi_R(t) = product_p J_0(t/(2p sqrt(P(2))))`.

The product is well defined near the origin, and the nonzero fourth cumulant already suffices to separate it from the normal law.

## 6. Prior art and novelty boundary

The reciprocal-prime asymptotic is classical Mertens theory; the repository already records Franz Mertens, **Ein Beitrag zur analytischen Zahlentheorie** (1874), as the reciprocal-prime source anchor. The facts `sum_p p^(-2)<infinity` and `sum_p p^(-4)<infinity` are immediate from comparison with the corresponding integer zeta series.

The general normal-versus-non-negligible triangular-array boundary is classical Lindeberg--Feller theory. J. W. Lindeberg, **Eine neue Herleitung des Exponentialgesetzes in der Wahrscheinlichkeitsrechnung**, *Mathematische Zeitschrift* 15 (1922), 211--225, and W. Feller, **Ueber den zentralen Grenzwertsatz der Wahrscheinlichkeitsrechnung**, *Mathematische Zeitschrift* 40 (1935), 521--559, are standard historical anchors. No new limit theorem is claimed here.

The Mathia-specific content is the specialization of these elementary probability facts to the prime-phase collision geometry and the observation that the visually natural squared critical-line amplitude taper `1/p` lands on the non-negligible side of the Gaussian boundary.

## 7. Boundaries and falsification

The independent Haar phases are a matched null, not the deterministic prime-log orbit. The result does not prove that deterministic prime phases have this same weighted limit at growing support.

The `1/p` weight is tied only to a finite first-order critical-line amplitude metric. Other visual constructions may use different weights. In particular, a taper whose quadratic mass grows and whose largest normalized weight vanishes can return to the Lindeberg Gaussian regime.

The theorem concerns the ordinary bulk and its first relative correction. It does not replace the rare-collision small-ball and sample-complexity controls of `VIS-164`--`VIS-168`.

Falsify the finding by exhibiting an error in the reciprocal-prime growth, square-summability, the `L^2` convergence of `S_x`, the Taylor reduction, the Haar moments, or the fourth-cumulant calculation. The non-Gaussian conclusion does not depend on visual inspection.

## Research consequence

The equal-weight Gaussian calibration of `VIS-170`--`VIS-171` is not representation-invariant. If a zeta-facing visualization weights prime-phase coordinates by squared first-order critical-line amplitude, its matched Haar null retains a permanent low-prime fingerprint after standardization.

Accordingly, a persistent skew/kurtosis profile or non-Gaussian standardized bulk in such a view is not arithmetic evidence by itself. A source-sensitive comparison must either use the explicit weighted null above, remove/prewhiten the low-prime taper under a frozen rule, or choose a weighting regime that satisfies an asymptotic-negligibility condition. Only a residual that survives that representation-matched control can be interpreted as information beyond the amplitude geometry.