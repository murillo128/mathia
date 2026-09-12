# VIS-196 — opposite-sign prime-ratio collisions are subquadratic and same-sign crowding is a gap-lattice incidence

## Claim

Keep the notation and hypotheses of `VIS-192`--`VIS-195`. Write

`Lambda_y^+={log(q/p): p<q<=y, p,q prime}`

and `Lambda_y=Lambda_y^+ union (-Lambda_y^+)`. For `y>=4` put

`a_y=log(1+2/y)`.

Every positive prime-ratio frequency satisfies

`lambda>=a_y`.

Hence every positive/negative pair obeys

`|lambda-mu|>=2a_y`.

For each `lambda in Lambda_y`, let `delta_lambda^sg` be its nearest-neighbor spacing among frequencies of the **same sign**, with `1/delta_lambda^sg=0` if no same-sign competitor exists, and define

`D_v^sg(y,H)=sum_(lambda in Lambda_y) nu_(y,H)(lambda)/delta_lambda^sg`.

Then whenever `R_v(y,H)>0`,

`D_v^sg(y,H) <= D_v(y,H) <= D_v^sg(y,H) + [2a_y]^(-1)`.

Since

`[2a_y]^(-1)=y/4+O(1)`,

one has the exact asymptotic equivalence

`D_v(y,H)=o(y^2)`

if and only if

`D_v^sg(y,H)=o(y^2)`.

Thus **opposite-sign collisions cannot carry the quadratic obstruction** isolated in `VIS-194`--`VIS-195`. They contribute at most a linear-scale correction to the weighted dephasing resource.

The remaining same-sign near-collision geometry has a simpler arithmetic form. For two positive frequencies

`lambda=log(q/p)`, `mu=log(s/r)`,

write the additive prime gaps

`d=q-p>0`, `e=s-r>0`.

Then

`qr-ps = d r - e p`.

Consequently every fixed normalized near-collision from `VIS-195` eventually lies on a same-sign gap-balance equation

`d r - e p = +/- h`,

where `h` is one of finitely many fixed positive even integers and all four primes are `Omega_A(y)`.

If

`g=gcd(d,e)`, `d=g d_0`, `e=g e_0`, `gcd(d_0,e_0)=1`,

then necessarily

`g | h`,

and after fixing the sign and one integer solution `(p_0,r_0)` of

`d_0 r - e_0 p = +/- h/g`,

all integer solutions have the one-parameter form

`p=p_0+d_0 t`, `q=p_0+d_0(t+g)`,

`r=r_0+e_0 t`, `s=r_0+e_0(t+g)`.

So the dangerous determinant family is not an unconstrained four-prime surface after the taper has selected a prime-ratio frequency. It is a union, over gap pairs with `gcd(d,e)|h`, of **four affine prime forms in one common parameter**.

In the equal-gap subfamily `d=e`, the equation collapses further to

`d(r-p)=+/- h`.

Hence `d|h` and `|r-p|=h/d`: equal-gap worst-scale collisions are fixed finite prime constellations indexed only by divisors of `h`.

**Evidence/status:** `EXACT-DERIVED + ARITHMETIC-REDUCTION + NEGATIVE/CONTROL FRONTIER + NO-NOVELTY-CLAIM`.

No estimate for the remaining same-sign weighted incidence mass is proved here, so no improvement `D_v=o(y^2)` is claimed.

## 1. Positive prime-ratio frequencies are separated from zero at scale `1/y`

Take `lambda=log(q/p)` with primes `p<q<=y`.

If `p>=3`, both primes are odd and therefore

`q-p>=2`.

Thus

`q/p >= 1+2/p >= 1+2/y`,

so

`lambda>=a_y`.

If `p=2`, then `q>=3` and

`lambda>=log(3/2)`.

For `y>=4`,

`log(3/2) >= log(1+2/y)=a_y`,

so the same lower bound holds uniformly.

Now let `lambda>0` and `mu<0` be frequencies in the symmetric spectrum. Writing `mu=-nu` with `nu>0`,

`|lambda-mu|=lambda+nu>=2a_y`.

This is a different scale from the worst same-sign arithmetic spacing in `VIS-195`:

`2a_y ~ 4/y`,

whereas

`b_y=log(1+2/y^2) ~ 2/y^2`.

Therefore fixed multiples of the `b_y` crowding scale are eventually disjoint from the opposite-sign branch.

## 2. Removing opposite signs changes `D_v` by only `O(y)`

For a positive frequency `lambda`, let

`chi_lambda=min_(mu<0)|lambda-mu|`.

By the previous section,

`chi_lambda>=2a_y`.

The full nearest-neighbor spacing is

`delta_lambda=min(delta_lambda^sg,chi_lambda)`.

Hence

`1/delta_lambda = max(1/delta_lambda^sg,1/chi_lambda)`

and therefore

`0 <= 1/delta_lambda - 1/delta_lambda^sg <= 1/chi_lambda <= 1/(2a_y)`.

The same statement holds by reflection for negative frequencies. Averaging against the probability measure `nu_(y,H)` gives

`0 <= D_v-D_v^sg <= 1/(2a_y)`.

Since

`log(1+2/y)=2/y+O(y^-2)`,

`1/(2a_y)=y/4+O(1)`.

Dividing by `y^2` proves

`(D_v-D_v^sg)/y^2 -> 0`.

Thus the quadratic-scale problem from `VIS-195` is exactly a same-sign problem up to a lower-order correction. In particular, the opposite-sign determinant form `qs-pr` that appeared in the symmetric bookkeeping of `VIS-195` is irrelevant to the criterion `D_v=o(y^2)`.

## 3. Same-sign determinants are gap-balance equations

Take two positive frequencies

`lambda=log(q/p)`, `mu=log(s/r)`

and write

`q=p+d`, `s=r+e`.

Then

`qr-ps=(p+d)r-p(r+e)=dr-ep`.

For the fixed normalized near-collision regime of `VIS-195`, the product difference

`h=|qr-ps|`

is eventually a fixed nonzero even integer bounded in terms of the fixed crowding multiplier `A`, and all four primes are proportional to `y`. Hence none of them is `2`, so both gaps `d,e` are positive even integers.

The near-collision relation is therefore exactly

`dr-ep=+/- h`.

If `g=gcd(d,e)`, then `g` divides the left side and so

`g|h`.

This already removes all gap pairs whose common divisor is incompatible with the bounded determinant.

Now write

`d=g d_0`, `e=g e_0`, `gcd(d_0,e_0)=1`.

Dividing by `g` gives

`d_0 r-e_0 p=+/- h/g`.

For fixed `d,e,h` this is a linear Diophantine equation. If `(p_0,r_0)` is one integer solution, every integer solution is

`p=p_0+d_0 t`,

`r=r_0+e_0 t`.

Adding the prescribed prime gaps gives

`q=p+d=p_0+d_0(t+g)`,

`s=r+e=r_0+e_0(t+g)`.

Thus, after the gap pair is fixed, the four-prime incidence problem is one-dimensional: it asks for common parameter values `t` at which two parallel pairs of affine forms are simultaneously prime.

This is the useful coordinate system for any subsequent sieve or weighted-incidence estimate. The taper weights from `VIS-194` remain attached to

`kappa_v(H log(1+d/p))`

and its `e,r` analogue, so the future estimate must sum these one-parameter prime configurations with their actual gap-dependent Fourier weights rather than count determinant points indiscriminately.

## 4. Equal gaps form only fixed prime constellations

If `d=e`, then the same-sign determinant identity becomes

`d(r-p)=+/- h`.

Therefore `d|h` and

`r-p=+/- h/d`.

For a fixed crowding multiplier `A`, only finitely many `h` occur by `VIS-195`, and each has only finitely many gap divisors `d`. The corresponding four primes are

`p`, `p+d`, `p+/- h/d`, `p+/- h/d+d`,

subject to the top-scale interval restrictions.

No asymptotic count for these constellations is asserted here. The point is structural: the equal-gap branch cannot hide a new two- or three-dimensional determinant family. It is a finite collection of ordinary fixed-shift prime-pattern problems.

## Prior-art audit

The determinant-surface prior art and weighted Hilbert context were already audited in `VIS-194` and `VIS-195`. In particular, `VIS-195` records classical and current work on integer and prime points on determinant equations such as `xy-zw=h` and explicitly makes no novelty claim for the determinant form itself.

The new reductions here use only elementary facts: parity of large prime gaps, the separation between positive and negative logarithmic frequencies, and the standard one-parameter description of solutions to a two-variable linear Diophantine equation. No novelty is claimed for any of those ingredients or for affine prime tuples as a general sieve object.

A targeted literature check is therefore not being used to assert that the gap-coordinate parametrization is new. Its role is narrower: it identifies the correct remaining Mathia object after `VIS-195`, namely the taper-weighted mass of one-parameter same-sign prime-gap configurations. Any future quantitative estimate must receive its own serious sieve/prime-tuples prior-art audit.

## Boundaries and falsification

The same-sign resource `D_v^sg` is defined using the same coefficient probability measure `nu_(y,H)` as `VIS-195`. The comparison with `D_v` concerns the sufficient Montgomery--Vaughan horizon from `VIS-194`; it does not make that horizon necessary or optimal.

The `O(y)` cross-sign correction is enough only for the quadratic-scale question. It does not say opposite-sign neighbors are irrelevant to finer secondary terms, nor that every individual frequency has a same-sign nearest neighbor closer than its reflected branch.

The fixed `h` and top-scale conclusions in the gap-coordinate section are inherited from the fixed-`A` near-collision theorem of `VIS-195`. They are not asserted uniformly when the crowding multiplier `A` grows with `y`.

The affine parametrization counts integer solutions for fixed `d,e,h`; it does not by itself supply any prime-density estimate. The coefficients and taper can concentrate unevenly across gap pairs, so an unweighted count of affine prime tuples remains insufficient for the `nu_(y,H)` mass question.

Falsify the finding by exhibiting a positive prime-ratio frequency below `a_y` for `y>=4`, an opposite-sign distance below `2a_y`, an error in the comparison between `D_v` and `D_v^sg`, a same-sign determinant not equal to `dr-ep`, a gap pair with `gcd(d,e)` not dividing its determinant, or a failure of the stated linear-Diophantine parametrization.

## Research consequence

The `VIS-195` frontier can now be narrowed before any heavy determinant-surface machinery is applied.

To prove the useful sufficient bound

`D_v=o(y^2)`,

one may discard the opposite-sign branch at a total cost `O(y)` and work only with same-sign prime ratios. At the dangerous fixed normalized spacing scale, those collisions are exactly solutions of

`dr-ep=+/- h`

with fixed even `h`, top-scale primes, `gcd(d,e)|h`, and the four primes lying on a one-parameter affine system once `(d,e,h)` is fixed.

The next quantitative theorem should therefore estimate the **taper-weighted aggregate of these affine prime-gap systems**, organized by the gap pair `(d,e)`. A generic four-variable determinant count wastes structure, while reintroducing the opposite-sign surface cannot improve the quadratic dephasing question.