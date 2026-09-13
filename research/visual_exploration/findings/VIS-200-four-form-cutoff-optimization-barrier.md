# VIS-200 — cutoff tuning cannot beat the four-form worst-case local-factor threshold

## Claim

Keep the fixed-`A` strictly subcritical weighted-dephasing setting and notation of `VIS-192`--`VIS-199`. In particular,

`H=H(y) -> infinity`,

`H log y/y -> 0`,

`Y=y/H`,

and `C_(y,H)(A)` denotes the fixed normalized near-collision energy from `VIS-195`.

Let

`B(y)=(1+log log(3+y))^4`.

Instead of the specific sieve/taper boundary `X=Y log y` used in `VIS-199`, choose an arbitrary cutoff factor `L=L(y)` and put

`X=Y L = yL/H`,

subject to

`L>=1`

and

`H/L -> infinity`.

Then the same pointwise four-form upper-bound-sieve argument of `VIS-199`, with no new arithmetic input, gives

`C_(y,H)(A)`
` <<_(A,alpha,v)`
`    B(y) (log y)^2/[log(H/L)]^4`
`    + (log y)^2/L^3`
`    + H/(y log y)`.

Consequently, within the proof template that combines

1. the pointwise worst-case local-factor bound `S_4(L) <<_A B(y)` from `VIS-197`,
2. a dimension-four upper-bound sieve on every fiber with `d<=X`, and
3. only taper decay plus trivial fiber counting for `d>X`,

**changing the cutoff alone cannot push the argument through the scale**

`log H = O((1+log log y) sqrt(log y))`.

Indeed, making the tail term vanish requires

`L^3/(log y)^2 -> infinity`,

whereas making the sieve term vanish requires

`log(H/L)/[(1+log log(3+y)) sqrt(log y)] -> infinity`.

Since `log(H/L)<=log H`, the latter is impossible to obtain from this bound when `log H` is only of the displayed threshold order or smaller. Thus the `sqrt(log y)`-times-local-factor threshold in `VIS-199` is not an artifact of the convenient choice `L=log y`; it is the limit of this **pointwise singular-series + separate tail** argument.

A near-minimal tail-safe cutoff is

`L=(log y)^(2/3) omega(y)`,

with any `omega(y)->infinity` slow enough that `L=o(H)`. This improves the crude tail from `1/log y` to `1/omega(y)^3`, while changing the sieve logarithm only from `log(H/log y)` to

`log H-(2/3)log log y-log omega(y)`.

That `O(log log y)` recovery is negligible compared with the current `(1+log log y)sqrt(log y)` sieve barrier. Therefore a genuine advance below the `VIS-199` corridor must improve an ingredient other than the scalar cutoff: for example average the local-factor/fiber mass instead of using its pointwise maximum, count the dangerous fibers in a coupled way, exploit cancellation or extra structure across fibers, or replace the sufficient resource `D_v`.

**Evidence/status:** `EXACT-DERIVED + METHOD-OBSTRUCTION + NO-NOVELTY-CLAIM`.

This is an obstruction to the present proof architecture, not an obstruction to `D_v=o(y^2)` itself. It does not assert that the true dephasing threshold is of order `exp(sqrt(log y) log log y)` or that a different sieve aggregation cannot go lower.

## 1. Generalize the VIS-199 cutoff

For a fixed crowding multiplier `A>1`, `VIS-195`--`VIS-197` reduce every relevant nondegenerate near-collision to a same-sign affine four-prime fiber indexed by its first gap `d`, with only `O_A(d)` possible second gaps `e` for a fixed `d`.

`VIS-194` and `VIS-198` give the coefficient bound

`|c_lambda|^2`
` <<_(A,alpha) (log y)^2/y^2 * w_d`,

where

`w_d=min(1,(Y/d)^4)`

and `Y=y/H`.

Choose now

`X=Y L`.

For `d<=X`, the top-scale parameter interval on one fiber has span comparable, after the same harmless enlargement used in `VIS-198`--`VIS-199`, to

`N_d asymp_A y/d`.

Hence throughout the sieve region

`N_d >= c_A y/X = c_A H/L`.

Write

`M=H/L`.

The assumption `M->infinity` is exactly what is needed here to retain a growing sieve logarithm.

## 2. The four-form sieve region depends on `L` only through `log(H/L)`

For every nondegenerate fiber, `VIS-197` supplies the pointwise local-product estimate

`S_4(L_fiber) <<_A B(y)`

with

`B(y)=(1+log log(3+y))^4`.

Applying the same fixed-dimensional four-form Selberg/large-sieve upper bound as in `VIS-199` on the enlarged parameter interval gives

`# {dangerous prime parameters on one fiber}`
` <<_A B(y) N_d/(log N_d)^4`
` <<_A B(y) y/[d (log M)^4]`.

For a fixed first gap `d`, the `O_A(d)` possible second gaps cancel the factor `1/d` from the parameter length. Multiplying by the coefficient bound and summing over the sieve region therefore gives unnormalized dangerous coefficient mass

`<<_(A,alpha,v)`
`  (log y)^2/y^2`
`  * B(y) y/(log M)^4`
`  * sum_(d<=X) w_d`.

Since

`sum_(d>=1) min(1,(Y/d)^4) << Y`,

this is

`<<_(A,alpha,v)`
`  B(y) (log y)^2/[H (log M)^4]`.

The strictly subcritical normalization from `VIS-192` is

`R_v(y,H) asymp_(alpha,v) 1/H`.

After division by `R_v`, the entire nondegenerate sieve region contributes

`<<_(A,alpha,v)`
`  B(y) (log y)^2/[log(H/L)]^4`.

No other dependence on the cutoff remains in this part of the argument.

## 3. The unsieved tail costs exactly `(log y)^2/L^3`

For `d>X`, retain only the trivial top-scale count from `VIS-198`--`VIS-199`: there are `O_A(d)` possible second gaps, and every corresponding fiber has at most `O_A(y/d)` integer parameters. Thus the total number of candidate parameters at one first-gap value `d` is `O_A(y)`.

Because `X=YL>=Y`, the taper is already in its decaying regime throughout the tail, so

`sum_(d>X) w_d`
` << Y^4/X^3`
` = Y/L^3`.

The unnormalized tail mass is therefore

`<<_(A,alpha,v)`
`  (log y)^2/y * Y/L^3`
` = (log y)^2/[H L^3]`.

Dividing again by `R_v asymp 1/H` gives

`<<_(A,alpha,v) (log y)^2/L^3`.

This calculation isolates the exact tradeoff hidden by the special choice `L=log y` in `VIS-199`: increasing `L` improves the taper tail cubically but shortens the smallest sieve interval from `H` to `H/L`.

## 4. The degenerate conductor-zero branch is independent of the cutoff

The `Q=0` branch remains the finite collection of fixed-shift three-prime progressions classified in `VIS-197`. The dimension-three upper-bound sieve used in `VIS-198`--`VIS-199` gives normalized contribution

`O_(A,alpha,v)(H/[y log y])`.

This estimate does not depend on the choice of `X=YL`, because that branch has parameter span `Theta_A(y)` and is separated before the nondegenerate gap-fiber summation.

Combining Sections 2--4 proves

`C_(y,H)(A)`
` <<_(A,alpha,v)`
`    B(y) (log y)^2/[log(H/L)]^4`
`    + (log y)^2/L^3`
`    + H/(y log y)`.

## 5. Optimizing the cutoff does not move the leading threshold

For the crude unsieved tail to vanish one needs

`(log y)^2/L^3 ->0`,

or equivalently

`L/(log y)^(2/3) -> infinity`.

Thus the smallest admissible tail-safe cutoff has the form

`L=(log y)^(2/3) omega(y)`

with `omega(y)->infinity` arbitrarily slowly.

At such a cutoff,

`log(H/L)`
` = log H-(2/3)log log y-log omega(y)`.

The nondegenerate sieve term vanishes only if

`B(y) (log y)^2/[log(H/L)]^4 ->0`,

which is equivalent to

`log(H/L)/[(1+log log(3+y)) sqrt(log y)] -> infinity`.

The tail optimization recovers at most an `O(log log y)` amount relative to the choice `L=log y`. But

`log log y = o(sqrt(log y) log log y)`.

Hence it cannot alter the leading threshold imposed by the pointwise four-form local-factor majorant.

More directly, for every admissible cutoff,

`log(H/L)<=log H`.

Therefore if

`log H = O((1+log log y) sqrt(log y))`,

the displayed sieve majorant cannot tend to zero by cutoff choice alone. This does **not** show that the actual collision energy stays large; it shows only that this proof template has exhausted the information supplied by its present pointwise ingredients.

## Prior-art audit

No new sieve theorem is asserted here. The analytic inputs are exactly those already audited in `VIS-197`--`VIS-199`: classical fixed-dimensional Selberg/large-sieve upper bounds for affine prime tuples and the corresponding local-density/singular-series framework, with Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (AMS Colloquium Publications 53, 2004), as the standard general reference and Thomas Dubbe, *Explicit bounds for prime k-tuplets*, arXiv `2409.04261` (revised March 22, 2026), as an explicit modern fixed-dimensional affine-tuple upper-bound reference.

The present result is an elementary optimization and limitation analysis of the already-persisted Mathia-specific inequalities. No novelty is claimed for cutoff balancing, Selberg sieve, singular-series bounds, or prime-tuple counting.

## Boundaries and falsification

The obstruction is conditional on the **proof architecture**, not on the underlying arithmetic truth. It assumes the same fixed-`A` reduction, coefficient envelope, pointwise worst-case local-factor bound, separate fiberwise four-form sieve, `O_A(d)` second-gap count, trivial unsieved-tail counting, and endpoint-zero taper decay used in `VIS-199`.

A better average estimate for the local products, cancellation or packing across fibers, a sieve applied jointly before taking the worst local factor, a stronger use of the fourth prime condition, or a different deterministic dephasing resource can evade the obstruction without contradicting this finding.

The cutoff factor must satisfy `H/L->infinity` for the present sieve interval to grow. If `L` is so large that `H/L` stays bounded, the logarithmic four-form sieve estimate used here no longer supplies the claimed term and the proof template fails even earlier.

The exponent `3` in the tail tradeoff comes from the squared endpoint-zero taper decay `w_d~(Y/d)^4`; a different taper with a different decay exponent changes the cutoff optimization. This finding does not claim universality across taper classes.

Falsify the derivation by finding an error in the generalized sieve-region summation, a failure of `N_d >= c_A H/L`, an incorrect tail identity `sum_(d>YL)(Y/d)^4 << Y/L^3`, a missing cutoff-dependent contribution in the conductor-zero branch, or an admissible choice of `L` for which the displayed three-term bound does not follow from the exact ingredients of `VIS-197`--`VIS-199`.

## Research consequence

The remaining frontier is now sharper than the informal boundary recorded after `VIS-199`. **Cutoff engineering is closed as an independent escape route** for this proof architecture. Choosing `X=Y log y` was convenient rather than optimal, but optimizing it only changes lower-order logarithms.

To enter the regime

`log H = O((1+log log y) sqrt(log y))`

while keeping the same dephasing resource, the next useful mathematical question is whether the dangerous affine fibers have substantially smaller **aggregate** local-factor mass than the pointwise `B(y)` majorant suggests, or whether their weighted incidences admit a coupled estimate not visible fiber by fiber. If neither route works, the remaining escape is to replace `D_v` by a resource that does not pay for inverse local spacing in the same way.