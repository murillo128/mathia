# VIS-185 — the linear-window kernel nulls every subpolynomial prime-gap band

## Claim

Fix `0 <= alpha < 1/2`, put

`w_p = p^(-alpha)`,

`Q_y = sum_(p<=y) w_p^2`,

and write `beta=1-2alpha>0`. For an averaging interval `[T,T+H]`, define the normalized interval kernel

`K_(H,T)(p,q)=H^(-1) int_T^(T+H) exp(it log(p/q)) dt`.

For an integer cutoff `D=D(y)>=1`, let

`R_D(y;H,T)`
` = Q_y^(-1) | sum_(1<=d<=D) sum_(p<=y-d, p and p+d prime) w_p w_(p+d) K_(H,T)(p,p+d) |`.

For every fixed `alpha<1/2`, uniformly in `T`, one has for sufficiently large `y` and `D<=sqrt(y)/4`,

`R_D(y;H,T) <<_alpha D y^(-beta/2) + (y/H) log(2D)/log y`.

Consequently, if `H>=c y` for any fixed `c>0` and

`D(y)=y^(o(1))`

(equivalently `log(2D(y))=o(log y)`), then

`R_D(y;H,T) -> 0`

uniformly in `T`.

Thus at the unresolved linear-support scale `H asymp y`, **every subpolynomial near-diagonal prime-gap band is asymptotically negligible after the actual interval kernel is included**. This strictly strengthens the coefficient-mass control of `VIS-184`, which required `D=o(log y)` because it discarded all kernel oscillation.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL UNIFORM SELBERG-SIEVE INPUT + EXACT KERNEL BOUND + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

The result does not show that polynomial gap bands contribute nontrivially. It only moves the first scale not killed by this particular upper-bound mechanism from logarithmic to polynomial size.

## 1. Exact interval-kernel decay off the diagonal

Let

`u=log(q/p)`.

Direct integration gives

`K_(H,T)(p,q)=exp(i(T+H/2)u) * 2 sin(Hu/2)/(Hu)`,

so

`|K_(H,T)(p,q)| <= min(1, 2/(H|u|))`.

For `q=p+d` with `p in (x,2x]` and `1<=d<=x`,

`log(1+d/p) >= d/(p+d) >= d/(3x)`.

Hence

`|K_(H,T)(p,p+d)| << x/(H d)`.

The phase depending on `T` has disappeared from the bound, which is why the final estimate is uniform in the interval start.

## 2. Classical uniform prime-pair input

Use the same sieve input already audited in `VIS-184`. For the two-shift singular series

`S(d)=mathfrak S({0,d})`,

a uniform Selberg upper-bound sieve gives on a dyadic scale `x`

`#{p in (x,2x] : p and p+d prime} << S(d) x/(log x)^2`

for shifts in the present range. Jared Duker Lichtman and Joni Teräväinen, **On the Hardy–Littlewood–Chowla conjecture on average**, *Forum of Mathematics, Sigma* 10 (2022), e57, DOI `10.1017/fms.2022.54`, Lemmas 2.3--2.5, provide the fixed-tuple uniform sieve bound and the corresponding singular-series control used in `VIS-184`.

In particular,

`A(U)=sum_(d<=U) S(d) << U`.

Partial summation therefore gives the harmonic-weighted aggregate needed by the interval kernel:

`sum_(d<=D) S(d)/d`
` = A(D)/D + int_1^D A(t)/t^2 dt`
` << log(2D)`.

This logarithm, rather than the factor `D` in `VIS-184`, is the decisive gain.

The classical nature of both ingredients was checked against the earlier literature as well: Gallagher's 1976 paper **On the distribution of primes in short intervals** records that the prime-tuple singular series averages to one and explicitly invokes the Selberg-sieve upper bound for prime tuples. No new sieve or singular-series theorem is claimed here.

## 3. Low primes remain negligible for subpolynomial bands

Split the pair sum at `p=sqrt(y)`. On the low part use only `|K|<=1`. There are at most `D` positive shifts for each `p`, and

`p^(-alpha)(p+d)^(-alpha) <= p^(-2alpha)`.

Therefore

`M_low <= D sum_(p<=sqrt(y)) p^(-2alpha)`.

For fixed `alpha<1/2`, the prime number theorem and partial summation give

`sum_(p<=z) p^(-2alpha) asymp_alpha z^beta/log z`

and

`Q_y asymp_alpha y^beta/log y`.

Hence

`M_low/Q_y <<_alpha D y^(-beta/2)`.

If `D=y^(o(1))`, this tends to zero for every fixed `beta>0`.

## 4. Kernel-weighted high dyadic blocks

Now take a dyadic block `x<p<=2x` with `x>=sqrt(y)/2`. For a subpolynomial cutoff, eventually `D<=sqrt(y)/4<=x`, so the kernel estimate and the uniform sieve bound apply throughout the band.

Using

`w_p w_(p+d) <= x^(-2alpha)`

and the bounds above, the absolute contribution of this block is

`<< x^(-2alpha) sum_(d<=D) [S(d) x/(log x)^2] [x/(H d)]`

`<< x^(2-2alpha)/(H (log x)^2) * log(2D)`

` = x^(1+beta)/(H (log x)^2) * log(2D)`.

Because `1+beta>0`, summing the dyadic blocks from `sqrt(y)` to `y` is dominated geometrically by the top scale; throughout this range `log x` is comparable with `log y`. Thus

`M_high <<_alpha y^(1+beta) log(2D)/(H (log y)^2)`.

After division by

`Q_y asymp_alpha y^beta/log y`, 

this becomes

`M_high/Q_y <<_alpha (y/H) log(2D)/log y`.

Combining the low and high pieces proves the claimed quantitative bound.

## 5. Why the new cutoff is genuinely larger than VIS-184

`VIS-184` deliberately used only `|K|<=1`. Its high-range estimate therefore contained

`sum_(d<=D) S(d) << D`,

which forced the explicit condition `D=o(log y)` after normalization.

The actual linear-window kernel contributes approximately `1/d` on a fixed high dyadic block. The same singular-series input then costs only

`sum_(d<=D) S(d)/d << log(2D)`.

At `H asymp y`, the normalized high contribution is consequently `O(log(2D)/log y)`. Any cutoff with `log D=o(log y)` is therefore null, including for example

`D=exp((log y)^gamma)` for every fixed `0<gamma<1`,

far beyond all powers of `log y`.

The improvement does not assume cancellation among different gaps or different prime pairs; it comes solely from the exact interval-average kernel and absolute-value bounds.

## 6. Prior-art and novelty boundary

The prime-pair sieve estimate and singular-series average are classical. The interval integral bound

`|H^(-1) int_T^(T+H) exp(itu) dt| <= min(1,2/(H|u|))`

is elementary Fourier analysis. Partial summation of `sum_(d<=U)S(d)<<U` is also elementary.

The literature audit found classical treatments of both sieve ingredients, including Gallagher's 1976 use of averaged singular series and Selberg-sieve prime-tuple upper bounds, and the modern uniform formulation already cited in `VIS-184`. No claim is made that the resulting subpolynomial cutoff is a new theorem of prime-gap theory. Its value here is as a Mathia-specific **negative control** for the normalized full-prime covariance channel.

## 7. Boundaries and falsification

The exponent `alpha` is fixed below `1/2`; constants are not claimed uniform as `alpha -> 1/2`. The critical case `alpha=1/2` is already globally null at quadratic order in `VIS-181`.

The proof uses full-prefix normalization. It does not apply to the sparse adversarial supports of `VIS-180`, where a few selected pairs can retain order-one normalized weight.

The linear-window assumption enters only when turning the quantitative bound into a null statement. More generally the high contribution is controlled by `(y/H) log(2D)/log y`; shorter windows may therefore require a smaller gap range.

For a fixed polynomial cutoff `D=y^delta`, the high bound is only `O(delta y/H)` and does not vanish when `H asymp y`. That failure is **not evidence** for a surviving polynomial-gap covariance. Stronger cancellation, a sharper prime-pair input, or the full all-gap structure may still remove it.

Falsify this finding by locating an error in the exact interval-kernel bound, the reduction `log(1+d/p) >= d/(p+d)`, the uniform two-shift sieve range, the harmonic singular-series estimate, the low/high split, the dyadic summation, or the normalization by `Q_y`.

## Research consequence

For fixed `0<=alpha<1/2` at `H asymp y`, **subpolynomial prime-gap crowding cannot be the missing full-prefix off-diagonal variance mechanism**. The natural local-gap frontier is no longer logarithmic: every band `D=y^(o(1))` is already null once the actual interval kernel is respected.

The next coherent question is therefore not to widen the modulus-one envelope again. It is to understand the kernel-weighted contribution from genuinely polynomial and larger separations, preferably as part of the full all-gap off-diagonal sum. A nonvanishing result at such a scale would still need to distinguish arithmetic structure from a matched deterministic or randomized crowding null.