# VIS-198 — a three-form sieve closes polynomial subcritical prime-ratio crowding

## Claim

Keep the notation and hypotheses of `VIS-192`--`VIS-197`. Fix `0<epsilon<1` and let `H=H(y)` satisfy

`H >= y^epsilon`

and

`H log y / y -> 0`.

Then the weighted prime-ratio dephasing resource from `VIS-194` satisfies

`D_v(y,H)=o(y^2)`.

More precisely, let

`b_y=log(1+2/y^2)`

and, for fixed `A>1`, let

`C_(y,H)(A)=nu_(y,H){lambda : delta_lambda <= A b_y}`

be the normalized near-collision energy from `VIS-195`. Then

`C_(y,H)(A)`
` <<_(A,alpha,v,epsilon) (1+log log(3+y))^3/log y`
`    + (log y)^2 y^(-3 epsilon/2)`
`    + H/(y log y)`.

In particular `C_(y,H)(A)->0` for every fixed `A>1`, and the exact layer-cake equivalence of `VIS-195` yields `D_v=o(y^2)`.

The key point is that the remaining `VIS-197` four-prime fiber does **not** require a four-prime upper-bound sieve for this purpose. To upper-bound the coefficient mass of dangerous collisions, one may forget the fourth primality condition and sieve only three affine forms. The missing logarithmic density from those three prime conditions is already enough, after the taper localization and the `Q_y` normalization, to force the fixed-`A` collision energy to zero whenever the observation scale is polynomially large but still strictly subcritical.

**Evidence/status:** `LITERATURE+DERIVED + UPPER-BOUND-SIEVE CLOSURE + ASYMPTOTIC POSITIVE RESULT + NO-NOVELTY-CLAIM`.

The result does not cover arbitrary slowly growing `H`, does not give an optimal rate for `D_v/y^2`, and does not prove that the sufficient horizon `D_v` from `VIS-194` is necessary.

## 1. Fixed normalized crowding lives on top-scale one-parameter fibers

Fix `A>1`. By `VIS-195`, every frequency counted by `C_(y,H)(A)` has, for all sufficiently large `y`, a same-scale competitor whose associated prime products differ by one of finitely many fixed nonzero even integers

`h in {2,4,...,2 floor(A)}`,

and all four participating primes are at least `c_A y` for some constant `c_A>0` depending only on `A`.

By `VIS-196`, opposite-sign pairs are eventually absent at this `b_y` scale, so it is enough to treat positive frequencies and double by reflection. Write

`lambda=log(q/p)`, `mu=log(s/r)`,

`d=q-p`, `e=s-r`.

Then every dangerous positive pair satisfies

`d r-e p=+/- h`.

Let

`g=gcd(d,e)`, `d=g d_0`, `e=g e_0`, `m=+/- h/g`.

Since `g|h`, both `g` and `m` range over finite `A`-dependent sets. For fixed `(d,e,h)` the integer points lie on the one-parameter family

`L_1(t)=p_0+d_0 t`,
`L_2(t)=p_0+d_0(t+g)`,
`L_3(t)=r_0+e_0 t`,
`L_4(t)=r_0+e_0(t+g)`.

The top-scale restriction alone gives two useful counting facts.

First, from

`e p=d r+O_A(1)`

and `p,r in [c_A y,y]`, one has

`e <<_A d`.

Thus, for a fixed gap `d`, there are only `O_A(d)` possible positive integer gaps `e` that can participate in a top-scale dangerous fiber.

Second, the admissible `t` values are contained in an interval of length

`T_(d,e,h) <<_A y/d`.

Indeed `L_1(t)=p` already ranges inside an interval of length `O_A(y)` with step `d_0=d/g`, and `g=O_A(1)`.

These two elementary bounds are the global geometry needed to sum the fiberwise sieve estimates.

## 2. Three of the four forms have a uniformly controlled sieve product

For a nondegenerate `VIS-197` fiber put

`D=d_0 e_0`

and

`Q=d_0 e_0 g m (m^2-g^2 D^2) != 0`.

Consider only the first three forms `L_1,L_2,L_3`. Let `nu_ell^(3)` be the number of residue classes `t mod ell` on which at least one of those three forms vanishes.

`VIS-197` proves more than is needed here: for every prime `ell` not dividing `Q`, all four local roots are distinct. Hence

`nu_ell^(3)=3`

for every `ell` not dividing `Q`.

The same prime-realization argument from `VIS-197` also gives local admissibility,

`nu_ell^(3)<ell`

for every prime `ell`.

Define the usual dimension-three local product

`S_3(L)=prod_ell (1-nu_ell^(3)/ell)(1-1/ell)^(-3)`.

For `ell>=5` outside `Q`, the factor is the generic three-root factor. Comparing each exceptional factor with that generic product exactly as in the four-form argument of `VIS-197` gives

`S_3(L) << (|Q|/phi(|Q|))^3`.

The finitely many small-prime factors are harmless because of admissibility. In the fixed-`A` regime, `g,m=O_A(1)` and `d_0,e_0<=y`, so

`|Q| <<_A y^6`.

The classical maximal-order estimate for `n/phi(n)` therefore yields

`S_3(L) <<_A (1+log log(3+y))^3`.

Thus the exceptional local arithmetic can inflate the three-form sieve only polylogarithmically in `log y`; it cannot consume the logarithmic saving below.

## 3. A standard dimension-three upper-bound sieve supplies the missing logarithm

For each nondegenerate fiber, every dangerous collision parameter makes all four `L_i(t)` prime. It is therefore enough for an upper bound to retain only the conditions

`L_1(t), L_2(t), L_3(t) are prime`.

Let

`X=y^(1-epsilon/2)`.

For `d<=X`, the top-scale parameter interval is contained in an integer interval of span

`N_d <<_A y/d`,

and we may enlarge it, if necessary, to an interval with span comparable to `y/d`. Hence

`N_d >>_A y^(epsilon/2)`

for the purpose of the sieve majorant. Translation of the parameter interval changes only the intercepts, not the local root counts.

Apply the standard dimension-three Selberg/large-sieve upper bound to the root sets of `L_1 L_2 L_3`. Since the target prime values are all `Omega_A(y)`, they exceed the sieve level for sufficiently large `y`, so every target parameter belongs to the corresponding sifted set. The fixed-dimensional upper-bound sieve gives

`# {dangerous prime parameters on the fiber}`
` <<_(A,epsilon) S_3(L) N_d/(log N_d)^3`
` <<_(A,epsilon) (1+log log(3+y))^3 y/[d (log y)^3]`.

Only an upper bound is used; no prime-tuple asymptotic or unproved Hardy--Littlewood statement enters.

A modern explicit formulation of exactly this large-sieve mechanism is Thomas Dubbe, **Explicit bounds for prime k-tuplets**, arXiv `2409.04261`, revised March 22, 2026. Its generic sifted-set theorem treats sieve dimension `kappa=3` by the number of excluded residue classes and gives an `N/(log N)^3` upper bound times the corresponding local product; Section 5 specializes the framework to affine prime tuples. Classical Selberg-sieve treatments give the same qualitative bound. The theorem is used here only as standard upper-bound-sieve input, not as evidence of novelty for the Mathia reduction.

## 4. The taper makes the fiber sum one-dimensional in the gap scale

For the coefficient attached to `lambda=log(q/p)`, `VIS-194` gives

`|c_lambda|^2`
` = Q_y^(-2) p^(-2alpha) q^(-2alpha)`
`   |kappa_v(H log(q/p))|^2`.

On a fixed-`A` dangerous collision all primes are `Theta_A(y)`. The prime number theorem therefore gives

`Q_y^(-2) p^(-2alpha)q^(-2alpha) <<_(A,alpha) (log y)^2/y^2`.

Because `q=p+d<=y`,

`log(q/p)>=d/q>=d/y`.

The endpoint-zero taper estimate from `VIS-192`,

`|kappa_v(theta)| <<_v min(1,|theta|^(-2))`,

thus gives

`|kappa_v(H log(q/p))|^2`
` <<_v w_d`,

where

`w_d=min(1,(y/(H d))^4)`.

Put `Y=y/H`. Since `H<=y` eventually,

`sum_(d>=1) w_d << Y`.

Now sum the three-form sieve bound over the finitely many `h` and signs, then over `e`. Section 1 gives `O_A(d)` possible `e` for each `d`. Therefore the unnormalized coefficient mass of nondegenerate dangerous collisions with `d<=X` is

`<< (log y)^2/y^2`
`   * [(1+log log(3+y))^3 y/(log y)^3]`
`   * sum_(d<=X) w_d`

`<<_(A,alpha,v,epsilon)`
`   (1+log log(3+y))^3/[H log y]`.

The apparent two-gap sum has collapsed to the single summable taper profile because the `O_A(d)` choices of `e` cancel the `1/d` parameter length of each fiber.

## 5. Large gaps can be discarded without sieving

For `d>X`, use only the trivial parameter count. There are `O_A(d)` possible `e`, and each fiber contains at most `O_A(y/d)` top-scale integer parameters, so the total number of candidate parameters at gap `d` is `O_A(y)`.

Because

`H>=y^epsilon`,

one has

`Y=y/H <= y^(1-epsilon)`

and therefore `X/Y>=y^(epsilon/2)`. Hence the taper tail satisfies

`sum_(d>X) w_d`
` << Y^4/X^3`.

After inserting the same coefficient normalization, the unnormalized large-gap collision mass is

`<<_(A,alpha,v) (log y)^2 Y^4/(y X^3)`.

In the strictly subcritical regime `VIS-192` gives

`R_v(y,H) asymp_(alpha,v) 1/H`.

Dividing the large-gap bound by `R_v` gives

`<< (log y)^2 H Y^4/(y X^3)`
` = (log y)^2 y^3/(H^3 X^3)`
` <= (log y)^2 y^(-3 epsilon/2)`.

Thus the region where the parameter interval becomes too short to supply a polynomial-size sieve interval is already negligible from taper decay alone.

## 6. The zero-conductor branch is smaller still

`VIS-197` classifies `Q=0` completely. At a prime realization it forces

`d_0=e_0=1`, `d=e=g`, `h=g^2`,

and the distinct primes form a fixed-shift three-term progression

`p, p+g, p+2g`

or its reflection. For fixed `A`, only finitely many such `g` can occur.

The same dimension-three upper-bound sieve now has parameter span `Theta_A(y)` and a fixed local product, so the number of such top-scale prime triples is

`O_A(y/(log y)^3)`.

Their total unnormalized coefficient mass is therefore

`O_(A,alpha,v)(1/[y log y])`.

After division by `R_v asymp 1/H`, their contribution to `C_(y,H)(A)` is

`O_(A,alpha,v)(H/[y log y])=o(1)`

under `H log y/y->0`.

## 7. Fixed-`A` crowding vanishes, hence `D_v=o(y^2)`

A dangerous frequency needs only one dangerous partner. Charging its coefficient mass to all ordered collision pairs can only enlarge the union mass, so Sections 4--6 give the valid upper bound

`C_(y,H)(A)`
` <<_(A,alpha,v,epsilon) (1+log log(3+y))^3/log y`
`    + (log y)^2 y^(-3 epsilon/2)`
`    + H/(y log y)`.

Every term tends to zero. Since `A>1` was arbitrary and fixed, `VIS-195` now applies directly:

`C_(y,H)(A)->0 for every fixed A>1`

is equivalent to

`D_v(y,H)=o(y^2)`.

This closes the quadratic weighted-crowding obstruction throughout every polynomially growing, strictly subcritical observation corridor.

## Prior-art audit

The sieve input is classical rather than Mathia-specific. Selberg upper-bound sieves and large-sieve formulations bound prime tuples of affine forms by the appropriate singular/local product times the expected logarithmic upper-bound scale. Henryk Iwaniec and Emmanuel Kowalski, **Analytic Number Theory**, AMS Colloquium Publications 53 (2004), is a standard reference for this machinery and was already used as a sieve reference in `VIS-197`.

For an explicit current affine-tuple formulation, Thomas Dubbe, **Explicit bounds for prime k-tuplets**, arXiv `2409.04261` (revised March 22, 2026), proves large-sieve upper bounds in arbitrary fixed dimension under the same local root-count/admissibility structure. The present finding needs only the dimension-three qualitative consequence.

The prior findings already separate the Mathia-specific reductions from classical ingredients: Montgomery--Vaughan weighted Hilbert theory in `VIS-194`, bounded-determinant reduction in `VIS-195`, one-parameter gap fibers in `VIS-196`, and finite local conductor control in `VIS-197`. No novelty is claimed for Selberg's sieve, affine prime-tuple upper bounds, singular series, or the estimate `n/phi(n)<<log log n`.

The new content is the combination of those established pieces with the actual taper coefficient profile: **three**, not four, prime conditions suffice to win the remaining logarithm after summing all relevant fibers, provided `H` supplies a polynomial parameter scale. A targeted literature search found general affine prime-tuple upper bounds but no reason to regard that Mathia-specific bookkeeping consequence as an independent new sieve theorem.

## Boundaries and falsification

The lower condition `H>=y^epsilon` is load-bearing in this proof. It guarantees that the gap region carrying essentially all taper mass has parameter span polynomial in `y`, so `log N_d` is comparable to `log y`. The argument does not show `D_v=o(y^2)` for `H` growing more slowly than every power of `y`.

The upper condition `H log y/y->0` is also load-bearing because it supplies the matching lower bound `R_v asymp 1/H` from `VIS-192`. At or above the critical scale, the numerator estimates remain useful but this proof does not provide the denominator comparison needed for `C_(y,H)(A)`.

The three-form sieve intentionally discards `L_4` primality. This weakens the count and is therefore safe only for an upper bound. No four-prime asymptotic is inferred.

The dimension-three local-product estimate uses the nondegenerate conductor from `VIS-197`. The branch `Q=0` must remain separate because two of the original four forms coincide at prime realizations there.

The argument bounds dangerous-frequency mass by ordered collision-pair mass and therefore permits overcounting. That direction is safe for the desired upper bound but should not be reversed or interpreted as an asymptotic count.

Falsify the finding by finding a fixed-`A` dangerous collision outside the `VIS-196` same-sign fibers, a nondegenerate triple whose local root count is not three outside the `VIS-197` conductor, a failure of the dimension-three upper-bound sieve under the stated affine/admissibility conditions, an error in the `O_A(d)` gap-pair count or `O_A(y/d)` parameter span, an incorrect taper-tail exponent, or a normalization error when passing from unnormalized collision mass to `C_(y,H)(A)`.

## Research consequence

The `VIS-197` frontier has split cleanly.

For every fixed `epsilon>0`, the polynomial strictly subcritical corridor no longer needs a new coefficient-uniform four-prime theorem: classical dimension-three upper-bound sieve machinery, together with the existing local conductor control, already proves the weighted crowding required by `VIS-194`.

The genuinely unresolved dephasing regime is now the **subpolynomial start-scale corridor**

`H->infinity`, `H log y/y->0`, but `H<y^epsilon` for every fixed `epsilon>0` along some sequence.

There the significant gap fibers may have only subpolynomial parameter length, so a generic `N/(log N)^3` sieve no longer supplies enough powers of `log y` after the global prime normalization. Progress requires either a sieve/short-interval input that prices primality at the ambient prime scale `y`, a sharper use of the fourth prime condition and coefficient structure, or a different cancellation mechanism. That is a narrower and more concrete frontier than the coefficient-uniform four-prime problem left by `VIS-197`.