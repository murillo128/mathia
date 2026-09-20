# VIS-333 — Wang's summatory-remainder transfer has no real log-frequency blind mode

## Claim

Let

`A(x)=sum_(n<=x) Lambda(n)^2`

and write its summatory remainder as

`E(x)=A(x)-(x log x-x)`.

For `u>=0`, define the normalized log-scale remainder

`F(u)=e^(-u) E(e^u)`

and Wang's adjusted source-profile remainder

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`,

where

`S(x)=x^(-2) sum_(n<=x) n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`.

Then the exact transform from `VIS-332` becomes

`Q(u)`
` = - integral_0^u e^(-2(u-v)) F(v) dv`
`   +3 integral_u^infinity e^(-2(v-u)) F(v) dv`.

Extend `F` by zero to `u<0` and define

`h(s) = -e^(-2s)` for `s>=0`,
`h(s) = 3e^(2s)` for `s<0`.

Define the auxiliary full-line output

`Q_ext=h*F`.

It agrees with the physical `Q` for every `u>=0`. With the Fourier convention of `VIS-292`,

`hat h(xi)=4(1+i xi)/(4+xi^2)`.

Hence the summatory-remainder transfer has **no blind real log-frequency**:

`hat h(xi) != 0`

for every real `xi`, while

`|hat h(xi)| = 4 sqrt(1+xi^2)/(4+xi^2)`
`              ~ 4/|xi|`

as `|xi|->infinity`.

Equivalently, distributionally on the full-line continuation,

`(4-d^2/du^2) Q_ext = 4(1+d/du) F`.

Thus, relative to the normalized summatory remainder `E(x)/x`, Wang's two-tail transform is a one-order log-frequency low-pass filter. It can attenuate increasingly rapid logarithmic oscillation, but it does not annihilate any fixed real log-frequency.

For every fixed `B<infinity`, the Fourier energy in that band obeys

`||1_(|xi|<=B) hat Q_ext||_2`
` >= c_B ||1_(|xi|<=B) hat F||_2`,

where

`c_B=min_(|xi|<=B) 4 sqrt(1+xi^2)/(4+xi^2) > 0`.

Therefore Wang smoothing cannot selectively erase any fixed bounded band of log-frequency energy.

**Evidence/status:** `EXACT-DERIVED + LOG-FREQUENCY TRANSFER + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not prove a sharper pointwise bound for the actual squared-von-Mangoldt remainder, locate its logarithmic spectrum, or improve Wang's pair-correlation error term.

## 1. Exact log-scale transform

`VIS-332` gives

`S(x)-log x`
` = -x^(-2) integral_1^x E(t) dt`
`   +3x^2 integral_x^infinity E(t)t^(-4) dt`
`   -3/(4x^2)`.

Set `x=e^u`, `t=e^v`, and `F(v)=e^(-v)E(e^v)`. Then

`E(e^v)e^v dv = e^(2v) F(v) dv`,

so the lower tail becomes

`e^(-2u) integral_1^(e^u) E(t)dt`
` = integral_0^u e^(-2(u-v))F(v)dv`.

Likewise,

`e^(2u) integral_(e^u)^infinity E(t)t^(-4)dt`
` = integral_u^infinity e^(-2(v-u))F(v)dv`.

After moving the explicit endpoint term `-3e^(-2u)/4` into the definition of `Q`, the displayed two-sided exponential transform follows exactly.

The Korobov--Vinogradov envelope recorded in `VIS-291` gives

`F(u)=O(exp(-c u^(3/5)(log u)^(-1/5)))`

after weakening constants for large `u`. Thus the zero extension of the actual `F` belongs to `L^2(R)`, so ordinary Fourier/Plancherel analysis of this exact transform is legitimate.

## 2. The transfer multiplier is nonzero and only first-order smoothing

For the piecewise kernel `h`, direct integration gives

`hat h(xi)`
` = - integral_0^infinity e^(-(2+i xi)s) ds`
`   +3 integral_(-infinity)^0 e^((2-i xi)s) ds`
` = -1/(2+i xi)+3/(2-i xi)`
` = 4(1+i xi)/(4+xi^2)`.

The numerator never vanishes for real `xi`. Its magnitude is

`4 sqrt(1+xi^2)/(4+xi^2)`,

which is strictly positive at every finite real frequency, equals `1` at `xi=0`, and decays like `4/|xi|`.

A single coherent logarithmic oscillation therefore cannot disappear. For example, if on the positive half-line

`F(u)=e^(i xi u)`,

then direct evaluation gives

`Q(u)`
` = [4(1+i xi)/(4+xi^2)] e^(i xi u)`
`   + e^(-2u)/(2+i xi)`.

The second term is only the lower-end boundary transient. The persistent oscillatory mode is multiplied by the nonzero factor above.

Differentiating the integral representation gives the equivalent local identity, for `u>0`,

`(4-d^2/du^2)Q=4(F+F')`.

On the full-line extension this is

`(4-d^2/du^2)Q_ext=4(F+F')`

in the distributional sense.

The extra first-order factor is exactly why the summatory-remainder transfer attenuates high log-frequencies like `|xi|^-1`, whereas the source-measure Green kernel in `VIS-292` attenuates them like `|xi|^-2`.

## 3. Fixed frequency bands cannot be selectively erased

Let the zero-extended `F` be in `L^2(R)`. For every fixed finite `B`, Plancherel and the pointwise multiplier relation give

`||1_(|xi|<=B) hat Q_ext||_2^2`
` = integral_(|xi|<=B) |hat h(xi)|^2 |hat F(xi)|^2 dxi`
` >= c_B^2 ||1_(|xi|<=B) hat F||_2^2`

with

`c_B=min_(|xi|<=B)|hat h(xi)|>0`.

Thus no fixed bounded log-frequency band is a hidden null of the transform. More generally, for any family `F_j`, if

`||Q_ext,j||_2 / ||F_j||_2 -> 0`,

then for every fixed `B` the fraction of Fourier energy of `F_j` inside `[-B,B]` must tend to zero. Strong norm suppression by the transform therefore requires spectral mass escaping every fixed band, not merely a fixed-frequency sign oscillation.

This is only a structural control. It does not say that the actual arithmetic remainder has such high-frequency migration, nor does an `L^2` gain by itself imply the pointwise Korobov--Vinogradov improvement required by the accepted Wang clue.

## 4. Relation to the earlier Wang controls

`VIS-292` works one level earlier, on the weighted prime-power source measure

`mu=sum Lambda(n)^2/n delta_(log n)`.

Its symmetric Green kernel has multiplier

`4/(4+xi^2)`

and is exactly invertible distributionally. The present finding concerns instead the **summatory remainder** `E(x)`, the object on which classical PNT error terms are naturally stated.

The factor

`1+i xi`

in the present multiplier is the log-scale derivative converting a summatory perturbation back toward source mass. This is the same factor already visible in `VIS-332` for real powers. Indeed, a pure secondary term

`E(x)=c x^alpha`

corresponds to `F(u)=c e^((alpha-1)u)`, and the same transfer gives

`4 alpha/[(alpha+1)(3-alpha)]`,

exactly the regular-variation coefficient of `VIS-332`.

Thus `VIS-292`, `VIS-332`, and the current result describe the same resolvent at three compatible levels: source measure, real regularly varying secondary scales, and real logarithmic frequencies of the normalized summatory remainder.

## 5. Prior art and evidence boundary

The operator algebra is classical. `VIS-292` already anchors the modified-Helmholtz Green kernel `e^(-2|u|)`, its Fourier multiplier, and resolvent inversion to standard Green-function theory. The present asymmetric kernel and multiplier are obtained by the elementary change from the source measure to the summatory remainder and by direct Fourier integration. No novelty is claimed for Fourier multipliers, Plancherel, constant-coefficient resolvents, or one-sided exponential transforms.

The arithmetic input is also unchanged. Biao Wang's coefficient profile and complete pair-correlation error budget are the source of the statistic, while `VIS-291` supplies the current Korobov--Vinogradov envelope for `E(x)` and `VIS-332` supplies the exact signed two-tail representation used here.

The result does **not** prove that the actual `Lambda^2` remainder is spectrally concentrated at high log-frequency, that its low-frequency content is nonzero, or that cross-frequency cancellation cannot improve a pointwise bound. It rules out a narrower false mechanism: a fixed real log-frequency cannot be killed by Wang's summatory-remainder transfer, and a fixed bounded spectral band cannot be driven to a lower `L^2` order by the filter alone.

## Dependencies

- `VIS-291`: gives the unconditional Korobov--Vinogradov envelope for the squared-von-Mangoldt summatory remainder.
- `VIS-292`: identifies Wang's source-measure Green resolvent and its nonvanishing symmetric multiplier.
- `VIS-332`: gives the exact signed transform of the summatory remainder and the real regular-variation transfer coefficient.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose remaining branch asks for source-specific signed cancellation.

## Research consequence

The accepted Wang clue can be narrowed again. A source improvement cannot be explained by assigning the actual remainder a fixed logarithmic oscillation that happens to land in a spectral null: there is no such real-frequency null. Nor can a fixed bounded band of log-frequencies be suppressed to a smaller `L^2` order by the transform itself.

A viable cancellation mechanism must instead quantify genuinely arithmetic behavior absent from these controls: log-frequency content moving to unbounded scale, cancellation among a broad collection of modes, nonstationary phase, or another source-specific structure, and then convert that mechanism into the required **pointwise** subpower improvement. Determining whether the actual `Lambda^2` remainder has such structure is a separate research question and is not pursued further in this invocation.
