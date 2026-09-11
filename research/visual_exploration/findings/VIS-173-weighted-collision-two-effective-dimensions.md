# VIS-173 — weighted collision bulk has distinct concentration and shape dimensions

## Claim

Consider the independent-Haar collision geometry of `VIS-169`--`VIS-172` with an arbitrary finite positive weight family `w_{n,j}`. Let

`W_n = sum_j w_{n,j}`,

`Q_n = sum_j w_{n,j}^2`,

`R_n = sum_j w_{n,j}^4`,

and define two effective dimensions

`D_2(n) = W_n^2/Q_n`,

`D_4(n) = Q_n^2/R_n`.

Let `X_{n,j}` and `Y_n` be independent Haar-uniform variables on the circle,

`U_{n,j}=sin^2(pi X_{n,j})`,

`A_n = W_n^(-1) sum_j w_{n,j} U_{n,j}`,

`N_n = |sin(pi Y_n)|`,

`C_n = N_n / sqrt(sum_j w_{n,j} U_{n,j})`.

Then `D_2` and `D_4` control two genuinely different parts of the weighted Haar null.

If `D_2(n)->infinity`, then

`A_n -> 1/2`

in probability and

`sqrt(W_n) C_n -> sqrt(2) N_n`

in distribution. Thus `D_2` controls concentration of the weighted denominator and hence the leading collision-bulk scale.

For the first relative correction, put

`H_n=(2A_n)^(-1/2)`

and

`Z_n=sqrt(D_2(n))(H_n-1)`.

If `D_2(n)->infinity`, then

`Z_n = - [sum_j w_{n,j}(U_{n,j}-1/2)] / sqrt(Q_n) + o_P(1)`.

The leading term has exact variance

`Var(Z_n)=1/8+o(1)`

and exact fourth-cumulant asymptotic

`kappa_4(Z_n) = -3/(128 D_4(n)) + o(1)`.

Equivalently, after standardizing to variance one, the excess kurtosis is

`-3/(2 D_4(n)) + o(1)`.

Moreover,

`D_4(n)->infinity`

if and only if

`max_j w_{n,j}/sqrt(Q_n) -> 0`.

Because the centered coordinate variable `U-1/2` is bounded, this is exactly the Lindeberg negligibility condition for the weighted triangular array. Therefore:

- if `D_4(n)->infinity`, then `Z_n` converges to `N(0,1/8)`;
- if `D_4` stays bounded along a subsequence, the standardized fourth cumulant stays bounded away from zero there, so a Gaussian first-correction limit is impossible along that subsequence.

Thus **concentration and Gaussianity are controlled by different effective dimensions**. A weighting may have `D_2->infinity` while `D_4` remains finite: the bulk then concentrates perfectly well around its leading scale but keeps a persistent non-Gaussian representation fingerprint.

For prime-power tapers `w_p=p^(-alpha)` over `p<=x`, this gives an exact phase boundary for the concentrated regime:

- `0<=alpha<=1/2`: `D_2(x)->infinity` and `D_4(x)->infinity`; the first relative correction is Gaussian;
- `1/2<alpha<=1`: `D_2(x)->infinity` but `D_4(x)` tends the finite constant `P(2alpha)^2/P(4alpha)`; the first relative correction retains non-Gaussian low-prime memory;
- `alpha>1`: even `W_x=sum_{p<=x}p^(-alpha)` converges, so the denominator no longer enters the concentrated-bulk regime above.

The `alpha=1` critical-line amplitude-squared weighting of `VIS-172` is therefore not an isolated anomaly. It lies inside the whole non-Gaussian concentrated phase `1/2<alpha<=1`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-LINDEBERG-FELLER SPECIALIZATION + WEIGHTED-HAAR-NULL + NEGATIVE-CONTROL + NO-NOVELTY-CLAIM`.

This is a representation/null theorem. It is not a deterministic prime-log equidistribution theorem in growing dimension, a zeta-versus-control separation, or an RH consequence.

## 1. `D_2` controls concentration

Write

`V_{n,j}=U_{n,j}-1/2`.

For one Haar coordinate,

`E[V_{n,j}]=0`,

`E[V_{n,j}^2]=1/8`.

Hence

`A_n-1/2 = W_n^(-1) sum_j w_{n,j} V_{n,j}`

and

`Var(A_n)=Q_n/(8W_n^2)=1/(8D_2(n))`.

Therefore `D_2->infinity` implies `A_n->1/2` in `L^2` and in probability. Since

`sqrt(W_n) C_n = N_n/sqrt(A_n)`,

Slutsky's theorem gives the leading bulk law

`sqrt(W_n) C_n -> sqrt(2)N_n`.

This recovers equal weights (`D_2=d`) and the `1/p` taper of `VIS-172` (`D_2~(log log x)^2/P(2)`) as special cases.

## 2. The first correction reduces to a normalized weighted sum

Let

`S_n=sum_j w_{n,j}V_{n,j}`.

For

`h(a)=(2a)^(-1/2)`,

one has `h(1/2)=1` and `h'(1/2)=-1`. Since `A_n=1/2+S_n/W_n`, Taylor expansion on any fixed neighborhood of `1/2` gives

`h(A_n)-1 = -S_n/W_n + O(S_n^2/W_n^2)`.

Also `S_n=O_P(sqrt(Q_n))`. Multiplying by

`sqrt(D_2)=W_n/sqrt(Q_n)`

yields

`sqrt(D_2)(h(A_n)-1)`
` = -S_n/sqrt(Q_n) + O_P(sqrt(Q_n)/W_n)`
` = -S_n/sqrt(Q_n) + o_P(1)`

whenever `D_2->infinity`.

The first relative bulk correction is therefore governed entirely by the normalized weighted sum, independently of the leading concentration calculation.

## 3. `D_4` is the shape dimension

The centered Haar coordinate has

`E[V^4]=3/128`

and fourth cumulant

`kappa_4(V)=3/128-3(1/8)^2=-3/128`.

Cumulants add under independence, so for

`T_n=-S_n/sqrt(Q_n)`

one has exactly

`Var(T_n)=1/8`

and

`kappa_4(T_n)`
` = -(3/128) R_n/Q_n^2`
` = -3/(128D_4(n))`.

After standardizing by variance `1/8`, the exact excess kurtosis is

`-3/(2D_4(n))`.

Thus `D_4` is an inverse-participation dimension for the shape of the first correction. Large `D_2` alone says only that the weighted average concentrates; it says nothing about whether the remaining normalized fluctuation is Gaussian.

## 4. `D_4` is exactly the Lindeberg boundary here

Set

`a_{n,j}=w_{n,j}/sqrt(Q_n)`.

Then `sum_j a_{n,j}^2=1` and

`1/D_4(n)=sum_j a_{n,j}^4`.

The inequalities

`max_j a_{n,j}^4 <= sum_j a_{n,j}^4 <= max_j a_{n,j}^2`

show that

`D_4(n)->infinity`

is equivalent to

`max_j |a_{n,j}|->0`.

Because `V_{n,j}` is uniformly bounded, this maximal-coefficient condition is precisely the Lindeberg negligibility condition. Classical Lindeberg--Feller therefore gives

`T_n => N(0,1/8)`

when `D_4->infinity`, and the same limit holds for `Z_n` by the Taylor reduction.

Conversely, if `D_4` is bounded along a subsequence, the fourth cumulant of `T_n` is bounded away from zero on that subsequence. The fourth moments are uniformly bounded, so Gaussian convergence would force the fourth cumulant to vanish, a contradiction. This does not assert that a unique non-Gaussian limit always exists; it says that the Gaussian null is invalid unless `D_4` diverges.

## 5. Prime-power taper phase diagram

Take

`w_p=p^(-alpha)`

for primes `p<=x`.

The reciprocal-prime divergence and comparison with the ordinary zeta series give the required sum boundaries without any delicate prime asymptotic:

- `sum_p p^(-beta)` diverges for `beta<=1` because it dominates the reciprocal-prime series when `beta<=1`;
- it converges for `beta>1` by comparison with `sum_n n^(-beta)`.

Hence for `0<=alpha<=1/2`, `Q_x=sum p^(-2alpha)` diverges. Since the largest weight is fixed while `Q_x->infinity`, the Lindeberg condition holds and `D_4->infinity`. Also `W_x->infinity` and `Q_x<=w_max W_x`, so `D_2>=W_x/w_max->infinity`. The concentrated bulk has a Gaussian first correction.

For `1/2<alpha<=1`, `W_x->infinity` while

`Q_x -> P(2alpha)<infinity`,

`R_x -> P(4alpha)<infinity`.

Therefore `D_2->infinity` but

`D_4 -> P(2alpha)^2/P(4alpha)<infinity`.

The centered weighted sum converges in `L^2` to an infinite low-prime series with nonzero negative fourth cumulant. This is exactly the mechanism exhibited explicitly at `alpha=1` in `VIS-172`.

For `alpha>1`, `W_x` itself converges and the mean-normalized denominator does not concentrate by increasing support; this lies outside the `D_2->infinity` regime.

Thus the taper family has two separate thresholds: `alpha=1/2` separates Gaussian from persistent low-prime first-correction shape, while `alpha=1` separates concentrated from leading-order low-prime-dominated bulk.

## 6. Prior art and novelty boundary

The normal-limit statement is a direct specialization of classical Lindeberg--Feller theory to bounded weighted Haar coordinates. The reciprocal-prime convergence/divergence inputs are classical and already anchored for this line, and `VIS-172` records the same historical Lindeberg/Feller boundary used here.

No new general central-limit theorem, prime-sum theorem, or weighted-probability theorem is claimed. The Mathia-specific content is the decomposition of the collision-null calibration into the two effective dimensions `D_2` and `D_4`, plus the resulting prime-power taper phase diagram for visual-representation controls.

## 7. Boundaries and falsification

The theorem concerns independent Haar phases. It does not prove that a deterministic prime-log orbit with growing support inherits the weighted Haar law.

`D_4->infinity` is a Gaussian criterion for the first relative correction after `D_2->infinity`; it does not calibrate rare collision tails, uncapped high moments, or decoder approximation error. Those remain separate controls from `VIS-164`--`VIS-168`.

A zeta-facing representation may use weights outside the prime-power family. The general `D_2`/`D_4` statement is the relevant gate there; the `alpha` diagram is only a transparent specialization.

Falsify the finding by finding an error in the variance reduction, Taylor scaling, Haar fourth cumulant, the equivalence between `D_4->infinity` and maximal-weight negligibility, or the prime-power convergence boundaries.

## Research consequence

A weighted collision visualization should report at least two null diagnostics before any source-sensitive interpretation:

`D_2=W^2/Q` for concentration and leading bulk scale, and `D_4=Q^2/R` for the Gaussian/non-Gaussian shape of the first relative correction.

Using only `D_2`, an apparent increase in effective dimension can be misleading: the bulk may become sharply concentrated while a finite set of coordinates still controls standardized shape. Any prewhitening, low-prime removal, or taper comparison intended to expose zeta-specific structure should therefore be matched on both diagnostics, or else use the exact non-Gaussian weighted null instead of a Gaussian surrogate.