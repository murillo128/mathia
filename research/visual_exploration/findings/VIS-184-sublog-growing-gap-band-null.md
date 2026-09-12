# VIS-184 — every sublogarithmic growing prime-gap band is diluted in the full prime prefix

## Claim

Fix `0 <= alpha < 1/2` and put

`w_p = p^(-alpha)`,

`Q_y = sum_(p<=y) w_p^2`.

For an integer-valued cutoff `D=D(y)>=1`, define the normalized positive-gap coefficient mass

`C_D(y)`
` = Q_y^(-1) sum_(1<=d<=D) sum_(p<=y-d, p and p+d prime) w_p w_(p+d)`.

If

`D(y) = o(log y)`,

then

`C_D(y) -> 0`.

More quantitatively, for every fixed `0<=alpha<1/2`, writing `beta=1-2alpha>0`, one has for all sufficiently large `y` with `D(y)<=sqrt(y)`,

`C_D(y) <<_alpha D(y)/log y + D(y) y^(-beta/2)`.

Consequently every predeclared sublogarithmic near-diagonal band, including `D(y)=(log y)^gamma` for any fixed `0<gamma<1`, has vanishing normalized coefficient mass. Any off-diagonal quadratic channel whose pair kernel has modulus at most one therefore receives `o(1)` contribution from that whole band, uniformly in the averaging interval.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL UNIFORM SELBERG-SIEVE INPUT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not prove that the band `D(y) asymp log y` is non-negligible, and it does not close the full `alpha<1/2` linear-support variance problem. It identifies the first scale not forced to vanish by this coefficient-mass argument.

## 1. Uniform prime-pair input over a growing shift family

For even `d`, let

`S(d)=mathfrak S({0,d})`

be the two-shift prime singular series. A standard Selberg upper-bound sieve gives, uniformly for distinct shifts lying in `[-X,X]`,

`#{n<=X : n, n+d prime} << S(d) X/(log X)^2`

for fixed tuple size two. Jared Duker Lichtman and Joni Teräväinen, **On the Hardy–Littlewood–Chowla conjecture on average**, *Forum of Mathematics, Sigma* 10 (2022), e57, DOI `10.1017/fms.2022.54`, Lemma 2.3, records exactly this uniform fixed-`k` Selberg-sieve bound; their Lemmas 2.4--2.5 give the companion singular-series estimate and its averaged control.

Specialized to `{0,d}`, those lemmas imply

`S(d) << (d/phi(d))^2`

and

`sum_(d<=D) S(d) << D`.

For odd `d`, two odd primes cannot differ by `d`; apart from the isolated pair involving the prime `2`, there is no high-scale contribution. Thus the same aggregate bound applies to the positive gaps relevant below.

The crucial improvement over `VIS-182` is uniformity in the shift. `VIS-182` used a fixed-`d` sieve constant and therefore could not sum over a growing band. Here the classical uniform sieve plus average singular-series bound permits exactly that summation.

## 2. Low primes are negligible for every sublogarithmic band

Split the numerator defining `C_D(y)` at `p=sqrt(y)`.

For `p<=sqrt(y)`, there are at most `D` possible positive shifts, and because `p+d>=p`,

`p^(-alpha)(p+d)^(-alpha) <= p^(-2alpha)`.

Hence

`M_low(y) <= D sum_(p<=sqrt(y)) p^(-2alpha)`.

For fixed `alpha<1/2`, the prime number theorem and partial summation give

`sum_(p<=z) p^(-2alpha) asymp_alpha z^(1-2alpha)/log z`,

and therefore

`M_low(y)/Q_y <<_alpha D y^(-beta/2)`.

In particular this tends to zero whenever `D=o(log y)`.

## 3. Uniform sieve control on the high dyadic blocks

Now take a dyadic block

`x < p <= 2x`,

with `x >= sqrt(y)/2`. For `D=o(log y)`, eventually `D<=x`, so every shift in the band lies inside the uniform range of the Selberg-sieve bound above.

On this block,

`p^(-alpha)(p+d)^(-alpha) <= x^(-2alpha)`.

Summing the uniform prime-pair bound over `1<=d<=D` and using `sum_(d<=D)S(d)<<D` gives

`sum_(1<=d<=D) sum_(x<p<=2x, p and p+d prime) p^(-alpha)(p+d)^(-alpha)`
` <<_alpha D x^(1-2alpha)/(log x)^2`.

Because `beta=1-2alpha>0`, the dyadic sum from `sqrt(y)` to `y` is geometrically dominated by the top scales, while `log x` is comparable to `log y` throughout this range. Thus

`M_high(y) <<_alpha D y^beta/(log y)^2`.

Also

`Q_y ~ y^beta/(beta log y)`.

Consequently

`M_high(y)/Q_y <<_alpha D/log y`.

Combining the low and high pieces proves

`C_D(y) <<_alpha D/log y + D y^(-beta/2)`.

If `D=o(log y)`, both terms vanish.

## 4. Consequence for the linear-support quadratic channel

For a prime pair `p<q`, write the normalized interval kernel

`K_(H,T)(p,q)=H^(-1) int_T^(T+H) exp(it log(p/q)) dt`.

For every `H>0` and every interval start `T`,

`|K_(H,T)(p,q)| <= 1`.

Therefore the absolute normalized contribution from all pairs with

`1 <= q-p <= D(y)`

is bounded by `C_D(y)` (up to the fixed convention factor from pairing conjugate terms). It is consequently `o(1)` for every `D=o(log y)`, uniformly in `H` and `T`.

This applies in particular at the unresolved linear-support scale `H asymp y`. The conclusion needs no oscillatory cancellation from the time kernel: coefficient-mass dilution alone kills the entire sublogarithmic gap band.

## 5. Relation to VIS-182 and VIS-183

`VIS-182` proves vanishing for every fixed finite gap family but has no uniformity as the family grows. `VIS-183` uses only those fixed-band limits to diagonalize existentially, producing some nonexplicit `D(y)->infinity` whose mass still vanishes, even below any prescribed diverging envelope.

The present result supplies the first explicit rate family on that frontier:

`D(y)=o(log y)`.

Thus the unresolved `alpha<1/2` question can no longer be described merely as a growing-gap effect, nor even as an arbitrary slowly growing explicit effect. Any coefficient-mass route must reach at least the logarithmic gap scale before this particular null argument stops forcing disappearance.

The statement is one-sided. At `D(y) asymp c log y`, the bound above is only `O_alpha(c)`; that loss of a vanishing upper bound is **not evidence that a nonzero covariance survives**. Time-kernel cancellation, stronger sieve information, or other structure may still kill the logarithmic and larger bands.

## 6. Prior art and novelty boundary

The uniform prime-tuple upper bound and the averaged singular-series estimate are classical sieve machinery. The cited Lichtman--Teräväinen paper uses Selberg-sieve prime-tuple bounds and singular-series averages as auxiliary tools and traces its Lemma 2.3 to Friedlander--Iwaniec. No new sieve estimate, prime-pair asymptotic, singular-series theorem, or bounded-gap theorem is claimed here.

The dyadic weighting and normalization by `Q_y` are elementary consequences specialized to Mathia's full-prime power-weight covariance control. The mathematical value of the finding is therefore a **control boundary**: it converts the qualitative growing-window loophole left by `VIS-182`/`VIS-183` into the explicit statement that every sublogarithmic band is already null.

## 7. Boundaries and falsification

The exponent `alpha` is fixed and strictly below `1/2`. The implied constants are not asserted uniform as `alpha` approaches `1/2`. The critical case `alpha=1/2` is already closed at global quadratic order by `VIS-181` and is not needed here.

The proof uses the full prime prefix normalization. It does not apply to the sparse adversarial support of `VIS-180`, where a single close pair can carry order-one normalized mass.

Only the positive near-diagonal coefficient mass is controlled. The result does not settle larger gap bands, the complete kernel-weighted off-diagonal sum, higher moments, discrete Gram sampling, shrinking events, hybrid prime/zero observables, or source-sensitive statistics outside this additive prime-log representation.

Falsify the finding by locating an error in the uniform two-shift Selberg-sieve application, the averaged singular-series bound, the low/high split, the dyadic weighted summation, the PNT normalization of `Q_y`, or the domination of the selected covariance channel by `C_D(y)`.

## Research consequence

For fixed `0<=alpha<1/2`, **sublogarithmic prime-gap crowding is not the missing full-prefix linear-support variance mechanism**. The first rate not eliminated by coefficient-mass dilution is logarithmic: `D(y) asymp log y`.

The next coherent quadratic question is therefore to control the logarithmic-scale band or, preferably, the naturally kernel-weighted aggregate over all gaps. A surviving source-sensitive signal would still need to beat the matched deterministic crowding null; failure of the present upper bound beyond `o(log y)` is not positive evidence.