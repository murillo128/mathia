# VIS-183 — fixed-band dilution diagonalizes to a diverging gap-window null

## Claim

Keep the full-prime power weights and normalization of `VIS-182`:

`w_p=p^(-alpha)`,

`Q_y=sum_(p<=y) w_p^2`,

with fixed `0<=alpha<=1/2`. For an integer `K>=1`, define the normalized positive-gap coefficient mass

`C_K(y)`
` = Q_y^(-1) sum_(1<=d<=K) sum_(p<=y-d, p and p+d prime) w_p w_(p+d)`.

Then there exists a nondecreasing integer-valued function

`D(y) -> infinity`

such that

`C_(D(y))(y) -> 0`.

In fact `D` may be chosen below **any prescribed diverging envelope** `R(y)->infinity`: there is a nondecreasing `D(y)->infinity` with `D(y)<=R(y)` eventually and

`C_(D(y))(y) <= 1/D(y)`

for all sufficiently large `y`.

Consequently, if the off-diagonal variance expansion is restricted to prime pairs with

`1<=q-p<=D(y)`,

its normalized contribution is `o(1)` in absolute value for every averaging interval, because the time kernel has modulus at most one. Thus the remaining `alpha<1/2` linear-support problem cannot be formulated merely as “allow a gap cutoff that tends to infinity.” There are always sufficiently slowly expanding near-diagonal windows whose entire coefficient mass, and hence their possible covariance contribution, still vanishes.

**Evidence/status:** `EXACT DIAGONAL CONSEQUENCE OF VIS-182 + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This result is deliberately non-quantitative. It does not prove that `D(y)=log y`, `D(y)=y^epsilon`, or any other explicit growing cutoff is negligible, and it does not close the full `alpha<1/2` variance problem.

## 1. Every fixed finite band already vanishes

For fixed `K`, apply `VIS-182` with

`Delta={1,2,...,K}`.

That finding gives

`C_K(y)->0`

for every fixed `K` and every fixed `0<=alpha<=1/2`.

The quantities are nonnegative and monotone in the band width:

`0<=C_1(y)<=C_2(y)<=...`.

No uniformity in `K` is asserted here. The only input is pointwise convergence for each finite band.

## 2. Diagonal extraction produces a growing null band

Choose thresholds `Y_K` recursively so that

- `Y_K>Y_(K-1)`;
- for every `y>=Y_K`, `C_K(y)<=1/K`.

Such a threshold exists because `C_K(y)->0` for fixed `K`.

If a diverging envelope `R(y)->infinity` has been prescribed, enlarge `Y_K` further so that

`R(y)>=K`

for every `y>=Y_K`. This is possible from the definition of `R(y)->infinity`.

Now define

`D(y)=max{K : Y_K<=y}`

once the set is nonempty, and keep any harmless fixed value below the first threshold. Then `D(y)` is nondecreasing and tends to infinity. If `D(y)=K`, one has `y>=Y_K`, hence

`C_(D(y))(y)=C_K(y)<=1/K=1/D(y)`.

The additional choice of the thresholds also gives `D(y)<=R(y)` for all sufficiently large `y`.

Therefore

`C_(D(y))(y)->0`.

The argument is a standard diagonalization; it introduces no new sieve estimate and uses no conjectural prime-pair asymptotic.

## 3. The same diagonal band is a variance null

For a prime pair `p<q`, write the normalized interval kernel

`K_(H,T)(p,q)=H^(-1) int_T^(T+H) exp(it log(p/q)) dt`.

For every `H>0` and every interval start `T`,

`|K_(H,T)(p,q)|<=1`.

Hence the absolute normalized off-diagonal contribution from the extracted band satisfies

`| Q_y^(-1) sum_(1<=q-p<=D(y)) w_p w_q K_(H,T)(p,q) |`
` <= C_(D(y))(y)`
` -> 0`.

This is uniform in `H` and `T`; in particular it applies at the linear-support scale `H asymp y` that remains open below `alpha=1/2`.

The conclusion uses only coefficient-mass dilution. Any additional oscillatory cancellation in the time kernel can only make this particular band smaller.

## 4. What this changes in the active boundary

`VIS-182` ruled out every **fixed** bounded-gap family. The present diagonal consequence rules out a stronger but still qualitative escape: saying only that the band width `D(y)` grows does not produce a candidate mechanism.

A genuine remaining question must specify a quantitative growth law or kernel-weighted aggregate. For example, one must ask whether a predeclared explicit band such as a polylogarithmic or power-scale window can accumulate enough singular-series-weighted pair mass and time-kernel coherence to survive normalization, or prove that all such bands are negligible in some stated range.

Equivalently, the unresolved information is now a **rate question**. Pointwise finite-gap dilution already implies the existence of an expanding null window; what is missing is uniform control strong enough to locate an explicit transition scale.

## 5. Prior art and novelty boundary

The arithmetic input is exactly `VIS-182`, which in turn uses the classical Brun–Selberg upper-bound sieve and prime asymptotics recorded there. No additional analytic-number-theory theorem is imported.

The passage from the family of limits `C_K(y)->0` for each fixed `K` to a slowly growing `D(y)` is the elementary diagonal principle used throughout analysis. No novelty is claimed for that principle. The line-specific content is only the consequence for the active normalized prime-gap covariance control.

## 6. Boundaries and falsification

The extracted `D(y)` is not explicit and may grow extremely slowly. Nothing here justifies substituting a convenient formula for it.

The proof gives an existential null window below any chosen diverging envelope; it does **not** say that every `D(y)->infinity` is negligible. In particular a polynomial, polylogarithmic, or even slower explicit band may require genuinely uniform prime-pair estimates not contained in `VIS-182`.

The finding controls only the near-diagonal pair contribution to the global continuous quadratic channel. It says nothing new about higher moments, discrete sampling, shrinking events, hybrid prime/zero observables, or source-sensitive statistics outside this representation.

Falsify the finding by finding an error in the application of `VIS-182` to each finite set `{1,...,K}`, the threshold/diagonal construction, or the absolute domination of the time-kernel contribution by `C_(D(y))(y)`.

## Research consequence

The next useful quadratic calculation should no longer ask merely whether an expanding prime-gap band matters. **Expansion without a rate is already compatible with a complete null.**

The live problem is to obtain a uniform, quantitative estimate for a predeclared explicit `D(y)`—or for the naturally kernel-weighted sum over all gaps—and determine where that estimate stops being `o(1)`. Only a non-vanishing contribution beyond such a crowding-aware control could reopen the full-prime `alpha<1/2` variance channel.