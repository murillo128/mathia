# VIS-207 — growing prime-ratio collision windows remain dilute below an explicit scale

## Claim

Keep the notation and hypotheses of `VIS-192`, `VIS-195`, `VIS-203`--`VIS-206`. Fix

`0 <= alpha < 1/2`,

let `v` be the fixed real endpoint-zero taper from `VIS-192`, and suppose

`H=H(y)->infinity`,

`H log y / y -> 0`.

Write

`b_y=log(1+2/y^2)`

and let `A=A(y)>=1` be allowed to grow. For the coefficient-energy probability measure

`nu(lambda)=|c_lambda|^2/R_v(y,H)`

on

`Lambda_y={+/-log(q/p): p<q<=y, p,q prime}`,

define

`Q_(y,H)(A)`
` = sum_(lambda!=mu, 0<|lambda-mu|<=A b_y) nu(lambda)nu(mu)`.

If

`H A^(2+4alpha) (log y)^2 / y^2 -> 0`,

then

`Q_(y,H)(A)`
` <<_(alpha,v) H A^(2+4alpha) (log y)^2 / y^2`
` -> 0`.

More precisely, throughout this regime the close-pair graph at radius `A b_y` has maximum degree `O(A^2)` on its non-isolated vertices, while every non-isolated frequency has

`nu(lambda) <<_(alpha,v) H A^(4alpha) (log y)^2/y^2`.

The hypothesis itself forces `A=o(y/log y)`, so the growing collision window remains below the one-cancellation prime/prime shell scale. Hence, for the autocorrelation-taper subclass of `VIS-203`, every nonzero exact shell in the same window still has multiplicity at most four and the `VIS-205` comparison extends to this growing regime:

`Q_(y,H)(A)`
` <= S_(y,H)(A)/R_v(y,H)^2`
` <= 4 Q_(y,H)(A)`.

Consequently

`S_(y,H)(A)/R_v(y,H)^2 -> 0`

under the same condition.

Thus `VIS-206` is not confined to fixed normalized width. Its elementary local-degree mechanism survives a widening family of determinant shells up to the scale allowed by

`H A^(2+4alpha) (log y)^2 << y^2`.

For `alpha=0`, this includes every

`A=o(y/(sqrt(H) log y))`.

**Evidence/status:** `EXACT-DERIVED + GROWING-WINDOW INCIDENCE BOUND + PNT NORMALIZATION + STRUCTURAL EXTENSION + NO-NOVELTY-CLAIM`.

No claim is made at the limiting scale where the displayed upper bound is order one, at the prime/prime cancellation scale `A asymp y`, or for the full sinc-weighted intermediate-shell sum.

## 1. The vanishing condition keeps the window below prime/prime cancellation

Since `A>=1` and `alpha>=0`,

`A^2 <= A^(2+4alpha)`.

Therefore

`H A^(2+4alpha) (log y)^2/y^2 ->0`

with `H->infinity` implies

`A log y/y ->0`.

In particular

`A=o(y/log y)=o(y)`.

Now

`A b_y <= 2A/y^2 = o(1/y)`.

On the other hand, `VIS-204` showed that every nonzero one-cancellation shell is a ratio of two distinct primes and therefore has magnitude at least

`log(1+1/y) asymp 1/y`.

Hence, for all sufficiently large `y`, no one-cancellation shell can enter

`0<|lambda-mu|<=A b_y`.

Every close pair is therefore in the noncancelling determinant regime of `VIS-195`: after choosing the relative frequency signs, its two associated products `U,V` are odd products of two primes and

`h=|U-V|`

is a positive even integer.

This observation also makes the exact-shell multiplicity statement uniform over the present growing window. The proof of `VIS-204` gives multiplicity at most four for every noncancelling shell; fixed `A` was used there only to keep the window below the prime/prime cancellation scale. The present hypothesis supplies that separation directly.

## 2. A growing normalized window allows only `O(A)` determinant levels

Put

`E_y(A)=exp(A b_y)-1=(1+2/y^2)^A-1`.

Because `A=o(y)`, in particular `A/y^2->0`. Thus, for all sufficiently large `y`,

`E_y(A) <= 4A/y^2`.

For a close pair, after swapping `U,V` if needed,

`log(U/V) <= A b_y`,

so

`h/min(U,V) <= E_y(A)`.

Since `min(U,V)<=y^2`,

`h <= E_y(A)y^2 <= 4A`.

Thus only `O(A)` positive even determinant values are possible.

The same inequality gives a lower bound in the opposite direction. Since `h>=2`,

`min(U,V) >= h/E_y(A) >= y^2/(2A)`

for all sufficiently large `y` after harmless adjustment of the absolute constant.

Both products are at least this large. Every prime factor occurring in either product is at most `y`, so every one of the four participating primes is at least

`y/(2A)`

up to another fixed absolute constant.

The fixed-`A` statement `p,q,r,s=Omega_A(y)` from `VIS-195` has therefore become the uniform growing-window localization

`p,q,r,s >> y/A`.

The loss of one factor of `A` in the endpoint localization is exactly the geometric price of widening the normalized collision window.

## 3. The near-collision graph has degree `O(A^2)`

Fix a signed frequency represented by one prime pair `p<q`. If it has any neighbor in the radius-`A b_y` graph, Section 2 gives

`p,q >> y/A`.

For each possible determinant level `h=O(A)`, relative sign choice and determinant orientation, the neighboring prime pair `r,s` lies on one of the linear Diophantine fibers

`q r-p s=+/-h`

or

`q s-p r=+/-h`.

For the first equation, once one integer solution `(r_0,s_0)` is chosen, all integer solutions have the form

`r=r_0+p t`,

`s=s_0+q t`,

with `t in Z`.

Because `p,q >> y/A`, only `O(A)` values of `t` can place both coordinates in `(0,y]`. Requiring `r,s` to be prime and to define an admissible signed frequency can only reduce this count. The second determinant form has the same conclusion, with the roles of `p,q` in the progression interchanged.

There are `O(A)` possible determinant values and only constantly many sign/orientation cases. Hence every non-isolated vertex has

`deg_A(lambda) << A^2`.

This is the uniform version of the bounded-degree argument in `VIS-206`. No four-prime sieve is used: after one frequency is fixed, the determinant surface becomes a one-dimensional lattice, and the widening window enlarges both the number of determinant levels and the number of lattice positions by at most one factor of `A` each.

## 4. Dangerous vertex mass costs only `A^(4alpha)`

For a signed frequency represented by `p<q`, `VIS-192` and the notation inherited by `VIS-206` give

`|c_lambda|^2`
` = Q_y^(-2) p^(-2alpha) q^(-2alpha)`
`   |kappa_v(H log(q/p))|^2`,

where

`Q_y=sum_(p<=y) p^(-2alpha)`.

The fixed taper gives the uniform bound

`|kappa_v(theta)| <<_v 1`.

If `lambda` is non-isolated in the present close-pair graph, Section 2 gives

`p,q >> y/A`.

Therefore

`p^(-2alpha)q^(-2alpha) <<_alpha A^(4alpha)y^(-4alpha)`.

The prime number theorem with partial summation gives, for fixed `0<=alpha<1/2`,

`Q_y asymp_alpha y^(1-2alpha)/log y`.

Consequently

`|c_lambda|^2`
` <<_(alpha,v) A^(4alpha) (log y)^2/y^2`.

The strictly subcritical assumption `H log y/y->0` gives the matching normalization from `VIS-192`,

`R_v(y,H) asymp_(alpha,v) 1/H`.

Thus every non-isolated frequency satisfies

`nu(lambda)`
` = |c_lambda|^2/R_v(y,H)`
` <<_(alpha,v) H A^(4alpha) (log y)^2/y^2`.

The weight penalty depends on `alpha`: widening the collision window permits smaller primes into the dangerous set, and the coefficient profile increasingly favors those smaller primes as `alpha` grows.

## 5. Degree times maximal vertex mass controls the two-sample energy

Let

`N_A(lambda)={mu!=lambda: |lambda-mu|<=A b_y}`

and let `m_A` be the maximum `nu`-mass of a non-isolated vertex, with `m_A=0` if the graph has no edges.

By Section 3,

`#N_A(lambda) << A^2`,

so

`sum_(mu in N_A(lambda)) nu(mu) << A^2 m_A`.

Averaging against the probability measure `nu` gives

`Q_(y,H)(A)`
` = sum_lambda nu(lambda) sum_(mu in N_A(lambda)) nu(mu)`
` << A^2 m_A`.

Section 4 therefore yields

`Q_(y,H)(A)`
` <<_(alpha,v) H A^(2+4alpha) (log y)^2/y^2`.

This tends to zero by hypothesis.

For autocorrelation tapers, Section 1 keeps all shells in the window noncancelling, so their exact representation multiplicity remains at most four. Repeating the shell-by-shell Cauchy argument of `VIS-205` gives

`Q_(y,H)(A)`
` <= S_(y,H)(A)/R_v(y,H)^2`
` <= 4 Q_(y,H)(A)`

without requiring `A` to be fixed. Hence the normalized noncancelling shell energy vanishes throughout the same widening regime.

## 6. What scale this actually reaches

The condition can be written as

`A = o((y^2/(H (log y)^2))^(1/(2+4alpha)))`.

At `alpha=0`, this is

`A=o(y/(sqrt(H) log y))`.

As `alpha` approaches `1/2`, the admissible power of `A` shrinks because dangerous lower-end primes carry more coefficient energy.

The result still operates well below the one-cancellation scale `A asymp y`. Its value is different: it shows that the first failure of the fixed-scale proof is not immediate. A nontrivial growing family of determinant shells can be absorbed purely by local incidence geometry and coefficient dilution.

This does not yet sum the full finite-start error. The sinc weight sees every shell, and the region beyond this widening window may contain many more determinant levels before ordinary dephasing becomes strong. The live question is therefore no longer whether *any* growth of `A` destroys the `VIS-206` mechanism, but how to bridge from this explicit dilute window to the larger intermediate scales.

## Prior-art audit

The load-bearing Diophantine fact is classical: fixing one coprime coefficient pair in a linear equation leaves a one-dimensional lattice of integer solutions. The prime-number-theorem normalization is also classical. No novelty is claimed for either ingredient or for the elementary estimate that a box of length `y` intersects a progression of step `>>y/A` in `O(A)` points.

The closest determinant-surface literature remains the material already audited in `VIS-195` and `VIS-206`. Satadal Ganguly and Rachita Guria, **Distribution of integer points on determinant surfaces and a mod-p analogue**, *Mathematika* 72 (2026), DOI `10.1112/mtk.70093`, gives asymptotics for smoothly weighted integer points on `xy-zw=r` with dependence on the determinant parameter. Rachita Guria, **An asymptotic formula with power-saving error term for counting prime solutions to a binary additive problem**, arXiv `2410.10856`, treats the determinant equation with two entries restricted to primes. These works study global determinant-surface counts rather than the present fixed-vertex local-degree estimate.

A targeted current literature check confirms that determinant-surface counting itself is established prior art and supplies no basis for a novelty claim here. The proof above does not invoke or improve those asymptotic counting theorems; it uses the much cheaper geometry available after one prime-ratio vertex is fixed.

The Mathia-specific content is the uniform bookkeeping that combines the widening determinant range, the induced `y/A` localization of participating primes, the resulting `O(A^2)` local degree, and the actual `VIS-192` coefficient-energy normalization to produce the explicit vanishing corridor for `Q(A)` and the associated autocorrelation shell energy.

## Boundaries and falsification

The exponent `alpha` and taper `v` are fixed. Constants are not uniform as `alpha->1/2` or over varying taper families.

The hypothesis is sufficient, not claimed sharp. The `O(A^2)` degree bound deliberately multiplies the number of determinant levels by a worst-case lattice occupancy. Arithmetic restrictions on simultaneous primality may make the true degree much smaller, but no such saving is used.

The result does not control the one-sided crowding mass `C(A)` or imply `D_v=o(y^2)`. As in `VIS-205`--`VIS-206`, the quadratic pair energy can vanish while a stronger nearest-neighbor resource remains unresolved.

The shell-energy conclusion uses the autocorrelation-taper nonnegativity of `VIS-203`. For a general sign-changing taper, within-shell cancellation changes the relevant decomposition.

The argument depends on the window remaining below prime/prime one-cancellation shells. The displayed vanishing condition guarantees this. It gives no statement once `A` approaches order `y`, where shared-anchor shell multiplicities can grow.

Falsify the finding by exhibiting, within the stated regime, a close pair whose determinant difference exceeds `O(A)`, a participating prime below `c y/A` for every absolute `c>0`, a fixed frequency with more than `O(A^2)` neighbors, a failure of the coefficient-mass bound, or a noncancelling shell with more than four ordered representations.

## Research consequence

The positive-shell route now has an explicit growing-width safe zone. Fixed normalized scale was not a singular accident: local determinant fibers and coefficient dilution control a widening family of exact shells as long as

`H A^(2+4alpha) (log y)^2/y^2 ->0`.

The next coherent boundary is the gap between this corridor and the ordinary dephasing region. A useful continuation must either improve the `O(A^2)` local-degree accounting using arithmetic information, exploit the sinc decay while summing successive widening shells, or change the sign/interference class. Reopening the already closed fixed-`A` problem would not address the remaining obstruction.
