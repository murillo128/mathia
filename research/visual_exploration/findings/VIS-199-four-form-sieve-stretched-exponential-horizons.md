# VIS-199 — the four-form sieve extends weighted dephasing into a subpolynomial horizon corridor

## Claim

Keep the notation and hypotheses of `VIS-192`--`VIS-198`. In particular, let `H=H(y)` satisfy

`H -> infinity`

and

`H log y / y -> 0`,

let `D_v(y,H)` be the coefficient-weighted inverse prime-ratio spacing from `VIS-194`, and let

`C_(y,H)(A)=nu_(y,H){lambda : delta_lambda <= A b_y}`

be the fixed normalized near-collision energy from `VIS-195`, where

`b_y=log(1+2/y^2)`.

Assume in addition that

`(1+log log(3+y)) sqrt(log y) = o(log(H/log y))`.

Then

`D_v(y,H)=o(y^2)`.

More quantitatively, for every fixed `A>1`,

`C_(y,H)(A)`
` <<_(A,alpha,v)`
`    (1+log log(3+y))^4 (log y)^2 / [log(H/log y)]^4`
`    + 1/log y`
`    + H/(y log y)`.

Hence every term on the right tends to zero, and the layer-cake equivalence of `VIS-195` gives the claimed subquadratic weighted dephasing horizon.

A simple sufficient subpolynomial regime is: for any fixed `eta>0`,

`H >= exp((log y)^(1/2+eta))`

and

`H log y/y -> 0`.

Thus the polynomial lower bound `H>=y^epsilon` in `VIS-198` is not a structural threshold. It was the point at which a three-form sieve already supplied enough logarithmic saving. Keeping the fourth primality condition gains one additional logarithm and pushes the same collision argument into a genuinely subpolynomial observation corridor.

**Evidence/status:** `LITERATURE+DERIVED + FOUR-FORM UPPER-BOUND-SIEVE EXTENSION + ASYMPTOTIC POSITIVE RESULT + NO-NOVELTY-CLAIM`.

The result still does not reach polylogarithmic or arbitrarily slowly growing `H`, does not prove the sufficient resource `D_v` is necessary, and does not resolve the transition all the way to the critical scale.

## 1. The slow-horizon loss in VIS-198 is exactly a sieve-length loss

Fix `A>1`. By `VIS-195` and `VIS-196`, every frequency counted by `C_(y,H)(A)` is eventually a same-sign top-scale collision with

`d r-e p=+/- h`,

where `h` belongs to a finite `A`-dependent set of nonzero even integers, all four primes are `Theta_A(y)`, and for fixed gaps `(d,e)` the prime points lie on the common-parameter affine system of `VIS-196`.

`VIS-197` writes the nondegenerate system as four affine forms

`L_1(t), L_2(t), L_3(t), L_4(t)`

with finite conductor

`Q=d_0 e_0 g m (m^2-g^2 d_0^2 e_0^2) != 0`,

and proves the uniform local-product estimate

`S_4(L) <<_A (1+log log(3+y))^4`.

The polynomial hypothesis in `VIS-198` entered only when the parameter interval was required to have polynomial length so that a three-form upper-bound sieve produced a denominator comparable with `(log y)^3`. For slower `H`, the natural gap scale is

`Y=y/H`,

and a typical relevant gap `d~Y` leaves only

`y/d ~ H`

parameter values. The available sieve logarithm is therefore `log H`, not `log y`.

The fourth prime condition is precisely one more source of logarithmic sparsity. Retaining it changes the useful fiber majorant from dimension three to dimension four.

## 2. Choose the sieve/tail boundary from the actual horizon

Put

`M=H/log y`

and

`X=y/M = y log y/H`.

The hypothesis on `log(H/log y)` implies in particular that `M->infinity`. Also

`X/Y=log y`,

so the sieve region extends a logarithmic factor beyond the taper transition `Y=y/H`.

For every gap `d<=X`, enlarge the actual top-scale parameter interval, if necessary, to an integer interval of span comparable to `y/d`, exactly as in `VIS-198`. The enlarged interval still majorizes the prime parameters relevant to the collision, and its span satisfies

`N_d asymp_A y/d >= c_A M`.

All target prime values are `Omega_A(y)`, much larger than the sieve levels associated with `N_d`. Translation of the parameter interval changes the affine intercepts but not the local root-count structure.

For `d>X`, no sieve estimate will be needed; taper decay alone will control the tail.

## 3. Four-form Selberg/large-sieve upper bounds give the extra logarithm

Consider first a nondegenerate `VIS-197` fiber. Every dangerous parameter makes all four affine forms prime. Apply the same fixed-dimensional Selberg/large-sieve upper-bound mechanism used in `VIS-198`, but retain all four primality conditions.

The residue system is admissible by `VIS-197`, and its local product is `S_4(L)`. The standard dimension-four upper-bound sieve therefore gives, on the enlarged interval,

`# {dangerous prime parameters on the fiber}`
` <<_A S_4(L) N_d/(log N_d)^4`.

Using `N_d <<_A y/d`, `N_d >= c_A M`, and the local-product bound from `VIS-197`,

`# {dangerous prime parameters}`
` <<_A (1+log log(3+y))^4 y/[d (log M)^4]`.

This is the only new analytic input relative to `VIS-198`: the same upper-bound-sieve framework is used at dimension four instead of deliberately dropping `L_4` and working at dimension three.

No prime-tuple asymptotic is required. Only an upper bound for the sifted parameter set is used.

## 4. The taper-weighted four-form sum is subquadratic under the stated logarithmic condition

For the coefficient attached to

`lambda=log((p+d)/p)`,

`VIS-194` and `VIS-198` give on a fixed-`A` top-scale collision

`|c_lambda|^2`
` <<_(A,alpha) (log y)^2/y^2 * w_d`,

where

`w_d=min(1,(Y/d)^4)`

and `Y=y/H`.

For each fixed `d`, the top-scale relation gives only `O_A(d)` possible positive gaps `e`; this is the same elementary geometry used in `VIS-198`. Multiplying the fiberwise four-form sieve bound by these `O_A(d)` choices cancels the `1/d` parameter-length factor. Therefore the total unnormalized coefficient mass of nondegenerate dangerous collisions with `d<=X` is

`<<_(A,alpha,v)`
`  (log y)^2/y^2`
`  * [(1+log log(3+y))^4 y/(log M)^4]`
`  * sum_(d<=X) w_d`.

Since `X/Y=log y` and

`sum_(d>=1) min(1,(Y/d)^4) << Y`,

this becomes

`<<_(A,alpha,v)`
`  (1+log log(3+y))^4 (log y)^2`
`  / [H (log M)^4]`.

In the strictly subcritical regime, `VIS-192` gives

`R_v(y,H) asymp_(alpha,v) 1/H`.

After division by `R_v`, the nondegenerate sieve region contributes

`<<_(A,alpha,v)`
`  (1+log log(3+y))^4 (log y)^2/(log M)^4`

to `C_(y,H)(A)`.

The stated hypothesis is exactly what forces this term to zero.

## 5. Beyond the sieve boundary, taper decay costs only `1/log y`

For `d>X`, use the same trivial top-scale fiber count as `VIS-198`. There are `O_A(d)` possible gaps `e`, and each fixed fiber contains at most `O_A(y/d)` integer parameters, so the number of candidate parameters at one gap `d` is `O_A(y)`.

Hence the unnormalized large-gap mass is

`<<_(A,alpha,v) (log y)^2/y * sum_(d>X) (Y/d)^4`

`<<_(A,alpha,v) (log y)^2 Y^4/(y X^3)`.

After division by `R_v asymp 1/H`, this is

`<< (log y)^2 y^3/(H^3 X^3)`.

Because `X=y/M` and `M=H/log y`,

`(log y)^2 y^3/(H^3 X^3)`
` = (log y)^2 (M/H)^3`
` = 1/log y`.

Thus the price of extending the sieve region from the taper scale `Y` out to `Y log y` is exactly enough to make the unsieved tail negligible without any polynomial lower bound on `H`.

## 6. The conductor-zero branch remains negligible

The degenerate branch `Q=0` is unchanged from `VIS-197`--`VIS-198`. For fixed `A`, it reduces to finitely many fixed-shift three-prime progressions

`p, p+g, p+2g`

or their reflections, with `h=g^2`.

A dimension-three upper-bound sieve on a parameter interval of length `Theta_A(y)` gives

`O_A(y/(log y)^3)`

such prime triples. With the same coefficient normalization, their unnormalized mass is

`O_(A,alpha,v)(1/[y log y])`.

After division by `R_v asymp 1/H`, the normalized contribution is

`O_(A,alpha,v)(H/[y log y])`,

which tends to zero because `H log y/y ->0`.

Combining Sections 4--6 proves the quantitative bound in the claim.

## 7. Consequence for the dephasing resource

For each fixed `A>1`, the three terms

`(1+log log(3+y))^4 (log y)^2/[log(H/log y)]^4`,

`1/log y`,

and

`H/(y log y)`

all tend to zero under the hypotheses. Therefore

`C_(y,H)(A)->0`.

`VIS-195` proves that fixed-`A` vanishing for every `A>1` is equivalent to

`D_v(y,H)=o(y^2)`.

Thus deterministic finite-start dephasing admits a subquadratic sufficient horizon throughout this stretched-exponential/subpolynomial corridor.

For example, if

`H=exp((log y)^(1/2+eta))`

with fixed `eta>0`, then

`log(H/log y)~(log y)^(1/2+eta)`,

so the four-form sieve term is

`O((1+log log y)^4/(log y)^(4 eta))=o(1)`.

This example is genuinely below every fixed power `y^epsilon` while still lying far above the polylogarithmic regime.

## Prior-art audit

The sieve ingredient is classical. `VIS-197` already anchored the local-density/singular-series framework and `VIS-198` already audited the fixed-dimensional Selberg/large-sieve upper-bound mechanism used to count affine prime tuples from their excluded residue classes. The present argument changes only the sieve dimension from three to four and keeps the same coefficient-varying affine family and local-product control.

Henryk Iwaniec and Emmanuel Kowalski, **Analytic Number Theory**, AMS Colloquium Publications 53 (2004), remains the standard general reference for Selberg and upper-bound sieve machinery used in the preceding findings.

Thomas Dubbe, **Explicit bounds for prime k-tuplets**, arXiv `2409.04261` (revised March 22, 2026), gives an explicit modern large-sieve treatment for fixed-dimensional affine prime-tuple upper bounds. The argument here uses only the qualitative upper-bound-sieve consequence; it does not import a prime-tuple asymptotic and makes no novelty claim for dimension-four sieving.

A targeted literature check of Selberg upper-bound sieve and affine prime-tuple formulations confirms that the extra inverse logarithm from retaining a fourth independent prime condition is standard sieve dimension, not a new sieve theorem. The Mathia-specific content is the way `VIS-195`--`VIS-197` reduce the weighted prime-ratio collision problem to these coefficient-dependent one-parameter fibers and the horizon-dependent choice `X=y log y/H` that balances the four-form sieve region against taper decay.

## Boundaries and falsification

The statement concerns the sufficient Montgomery--Vaughan resource `D_v`; it does not prove that `D_v` is the optimal or necessary deterministic observation horizon.

The fixed normalized crowding multiplier `A` is essential. The finite determinant set, `g|h`, top-scale prime restriction, and uniform conductor bounds are inherited from `VIS-195`--`VIS-197` for fixed `A`. No uniform theorem for `A=A(y)->infinity` is asserted.

The argument also uses the endpoint-zero taper decay

`|kappa_v(theta)| <<_v min(1,|theta|^-2)`

from `VIS-192`. A weaker taper would change the unsieved-tail exponent and therefore the balancing scale.

The four-form sieve applies only to nondegenerate fibers. The exact `Q=0` classification is separated before sieving and remains a three-form problem.

The logarithmic condition is sufficient, not claimed sharp. In particular this method still loses control when `log H` is only of order `sqrt(log y)` up to the local-factor logarithms, and it gives no result for polylogarithmic `H`. Improving that frontier would require an average local-factor bound, a stronger aggregate incidence estimate, a different use of the fourth prime condition, or a different dephasing resource; simply repeating the present worst-case singular-series majorant cannot remove the displayed threshold.

Falsify the finding by finding a failure of the dimension-four upper-bound sieve uniformly for the `VIS-197` admissible affine fibers at span `N_d`, an incorrect use of the `S_4(L)` bound, an error in the `O_A(d)` gap count, a failure of the taper sum or tail estimate, a degenerate `Q=0` contribution larger than stated, or a regime satisfying the hypotheses in which a fixed `C_(y,H)(A)` does not tend to zero.

## Research consequence

`VIS-198` showed that polynomially growing subcritical horizons are enough. The present result moves the live boundary substantially: the weighted-crowding obstruction is also absent for a broad subpolynomial corridor, including every stretched-exponential scale

`H >= exp((log y)^(1/2+eta))`

with fixed `eta>0` and `H log y/y ->0`.

The remaining difficult regime is now below this four-form sieve threshold. The next useful question is not another fixed-power refinement. It is whether one can control the aggregate singular-series/fiber mass strongly enough to reach `log H=O(sqrt(log y) log log y)`, or whether a different deterministic dephasing resource is needed before the polylogarithmic and slower horizons become accessible.