# VIS-195 — weighted prime-ratio crowding is equivalent to top-scale bounded-determinant mass

## Claim

Keep the notation and hypotheses of `VIS-192`--`VIS-194`. Thus

`Lambda_y={+/-log(q/p): p<q<=y, p,q prime}`

and, when `R_v(y,H)>0`,

`D_v(y,H)=sum_(lambda in Lambda_y) nu_(y,H)(lambda)/delta_lambda`,

where

`nu_(y,H)(lambda)=|c_lambda|^2/R_v(y,H)`

is a probability measure on the symmetric prime-ratio spectrum and

`delta_lambda=min_(mu!=lambda)|lambda-mu|`.

For `y>=4` put

`b_y=log(1+2/y^2)`.

Then every two distinct frequencies in `Lambda_y` are separated by at least `b_y`. Consequently

`D_v(y,H) <= b_y^(-1) = y^2/2 + O(1)`.

This improves the universal `y^2+1` fallback in `VIS-194` by the parity forced by prime products, but the more important consequence is a scale decomposition of the weighted crowding.

For `A>=1`, define the normalized near-collision energy

`C_(y,H)(A)=nu_(y,H){lambda: delta_lambda <= A b_y}`.

Then one has the exact identity

`b_y D_v(y,H) = integral_1^infinity C_(y,H)(A) A^(-2) dA`,

and for every `A>=1`,

`C_(y,H)(A)/A <= b_y D_v(y,H) <= C_(y,H)(A)+1/A`.

Hence along any asymptotic regime `y->infinity` for which `R_v(y,H)>0`,

`D_v(y,H)=o(y^2)`

if and only if

`C_(y,H)(A)->0`

for every fixed `A>1`.

The near-collision event has an exact arithmetic form. If

`lambda=epsilon log(q/p)`, `mu=eta log(s/r)`

with `epsilon,eta in {+1,-1}`, then

`|lambda-mu|=|log(U/V)|`,

where, up to swapping `U,V`,

`(U,V)=(qr,ps)` when `epsilon=eta`, and

`(U,V)=(qs,pr)` when `epsilon!=eta`.

Thus `U,V` are distinct products of two primes, each at most `y^2`. For every fixed `A`, once `y` is sufficiently large, membership in `C_(y,H)(A)` forces all relevant products to be odd and

`h=|U-V| in {2,4,...,2 floor(A)}`,

while

`min(U,V) >= (h/(2A)+o_A(1)) y^2`.

In particular every participating prime is `Omega_A(y)`: normalized crowding at the worst spacing scale can only come from **top-scale prime points on finitely many fixed determinant surfaces**.

More intrinsically, for fixed `K>=1` and `c>0`, let `J_(K,c)(y,H)` be the `nu_(y,H)`-mass of frequencies `lambda` for which there exists a distinct `mu` whose associated products satisfy

`1 <= |U-V| <= K`,

`min(U,V) >= c y^2`.

Then

`D_v(y,H)=o(y^2)`

if and only if

`J_(K,c)(y,H)->0`

for every fixed `K` and `c>0`.

So the live `VIS-194` problem is no longer merely a vague request for a weighted multiplicative-energy estimate. It is exactly a weighted **bounded-determinant incidence** problem at the top prime-product scale.

**Evidence/status:** `EXACT-DERIVED + ARITHMETIC-REDUCTION + NEGATIVE/CONTROL FRONTIER + NO-NOVELTY-CLAIM`.

No estimate for the required determinant-incidence mass is proved here, and therefore no subquadratic deterministic dephasing horizon is claimed.

## 1. Prime parity improves the universal spacing floor

Take distinct frequencies

`lambda=epsilon log(q/p)`, `mu=eta log(s/r)`

from `Lambda_y`, with `p<q<=y` and `r<s<=y` prime. Unique factorization gives distinct positive integers `U,V<=y^2` as above such that

`|lambda-mu|=log(max(U,V)/min(U,V))`.

If `U` and `V` have the same parity, then they are distinct integers of the same parity, so

`|U-V|>=2`.

Therefore

`|lambda-mu| >= log(1+2/y^2)=b_y`.

If they have opposite parity, the even product must contain the prime `2`. In the same-sign case the only possible factors `2` are `p` or `r`; in the opposite-sign case `qs` is odd and a factor `2` can occur only in `pr`. In every case the even product is at most `2y`. Hence

`|lambda-mu| >= log(1+1/(2y))`.

For `y>=4`,

`1/(2y) >= 2/y^2`,

so this is again at least `b_y`.

Thus

`delta_lambda>=b_y`

for every frequency. Averaging inverse spacings against `nu_(y,H)` yields

`D_v<=b_y^(-1)`.

The improvement is only a constant factor asymptotically; it does not by itself solve the `o(y^2)` problem.

## 2. `D_v` is the mean of a bounded normalized-crowding variable

Define

`X_lambda=b_y/delta_lambda`.

The spacing floor gives

`0<X_lambda<=1`,

and by definition

`b_y D_v=sum_lambda nu(lambda) X_lambda`.

For a random variable `X in [0,1]`, the layer-cake identity gives

`E[X]=integral_0^1 P(X>=t) dt`.

Substitute `t=1/A`. Since

`X_lambda>=1/A`

is exactly

`delta_lambda<=A b_y`,

one obtains

`b_y D_v=integral_1^infinity C_(y,H)(A) A^(-2) dA`.

For a fixed `A`, on the event defining `C(A)` one has `X>=1/A`, while outside it one has `X<1/A`. Hence

`C(A)/A <= E[X] <= C(A)+1/A`.

Because

`b_y ~ 2/y^2`,

`D_v=o(y^2)` is equivalent to `E[X]->0`. The lower inequality shows this forces `C(A)->0` for every fixed `A`. Conversely, if every fixed `C(A)` tends to zero, choose `A` large enough that `1/A` is arbitrarily small and use the upper inequality. This proves the near-collision criterion.

The criterion is stronger conceptually than a single worst-gap bound: it asks whether the coefficient-energy measure places asymptotically vanishing mass at every fixed multiple of the arithmetic minimum-spacing scale.

## 3. Fixed normalized crowding becomes a bounded even determinant

Suppose `A` is fixed and

`|lambda-mu|<=A b_y`.

If one of the products `U,V` contains a factor `2`, the parity argument above gives a spacing at least `log(1+1/(2y))`, which is larger than `A log(1+2/y^2)` for all sufficiently large `y`. Therefore every fixed-`A` near-collision eventually uses only odd prime products.

Put

`h=|U-V|`.

Then `h` is a positive even integer and

`h/min(U,V)`
` <= exp(A b_y)-1`
` = (1+2/y^2)^A-1`.

Since `min(U,V)<=y^2`,

`h <= y^2[(1+2/y^2)^A-1]`
`   = 2A+O_A(y^(-2))`.

Because `h` is even, for all sufficiently large `y`,

`h in {2,4,...,2 floor(A)}`.

The same inequality in the other direction gives

`min(U,V)`
` >= h/[(1+2/y^2)^A-1]`
` = (h/(2A)+o_A(1)) y^2`.

Thus the products are not merely close; they both live at macroscopic scale `Theta_A(y^2)`. Since each factor is at most `y`, every prime appearing in either product is bounded below by a positive `A`-dependent multiple of `y`.

This is the arithmetic content hidden by the abstract nearest-neighbor notation in `VIS-194`: the dangerous frequencies are produced by prime quadruples lying near the top of the box on one of finitely many surfaces

`qr-ps=h`

or

`qs-pr=h`,

with fixed small nonzero even `h`.

## 4. Equivalence with top-scale bounded-determinant energy

Fix `K` and `c>0`. If a frequency belongs to `J_(K,c)`, then for some competitor

`|lambda-mu|`
` <= log(1+K/(c y^2))`.

Since

`log(1+K/(c y^2))/b_y -> K/(2c)`,

there is a fixed `A=A(K,c)` such that, for all sufficiently large `y`,

`J_(K,c) subset C(A)`.

Therefore `D_v=o(y^2)` implies

`J_(K,c)->0`

for every fixed `K,c`.

Conversely, fix `A>1`. Section 3 shows that for all sufficiently large `y`, every frequency counted by `C(A)` participates in a determinant relation with

`|U-V|<=2 floor(A)`

and, because `h>=2`,

`min(U,V)>=(1/A+o_A(1))y^2`.

Hence, for example, eventually

`C(A) <= J_(2 floor(A),1/(2A))`.

If every fixed `J_(K,c)` tends to zero, then every fixed `C(A)` does too, and Section 2 gives

`D_v=o(y^2)`.

This proves the stated equivalence.

## Prior-art audit

The weighted Hilbert inequality behind `D_v` is classical and was already audited in `VIS-194`: H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`.

Determinant surfaces are also an established analytic-number-theory object. Satadal Ganguly and Rachita Guria, **Distribution of integer points on determinant surfaces and a mod-p analogue**, *Mathematika* 72 (2026), DOI `10.1112/mtk.70093`, obtain asymptotic formulas with smooth weights for integer solutions of `xy-zw=r`. Rachita Guria's preprint **An asymptotic formula with power-saving error term for counting prime solutions to a binary additive problem**, arXiv `2410.10856`, treats the same determinant equation with two entries restricted to primes. Étienne Fouvry and Igor E. Shparlinski, **On character sums with determinants**, *Science China Mathematics* (2024), DOI `10.1007/s11425-022-2122-0`, study weighted determinant character sums modulo a prime.

These sources make clear that neither the determinant form nor the general strategy of counting points on determinant surfaces is novel. A targeted audit did not identify a theorem in these sources that directly controls the present object: all four entries are prime, the entries are at top scale, `h` is fixed and small, and the quantity to be killed is the `VIS-194` coefficient-energy mass rather than an unweighted point count. Absence from this targeted audit is not evidence of novelty, and no novelty claim is made for the reduction.

The Mathia-specific value of the finding is to convert the abstract weighted-spacing frontier into the exact arithmetic incidence class that a subsequent theorem would have to control.

## Boundaries and falsification

The coefficient measure `nu_(y,H)` is defined only when `R_v(y,H)>0`. If `R_v=0`, the prime-ratio polynomial vanishes and finite-start dephasing is already trivial as in `VIS-194`.

The equivalence concerns the sufficient Hilbert resource `D_v`; `VIS-194` does not prove that `D_v` is the necessary optimal observation horizon. Therefore even a complete estimate of the determinant-incidence mass would sharpen this sufficient route, not establish an optimal lower bound on `L`.

The determinant criterion is weighted by the actual coefficients `|c_lambda|^2`. An unweighted count of prime quadruples can be much larger than the relevant energy and is not by itself the desired theorem. Conversely, proving few unweighted incidences would be a sufficient but potentially wasteful route.

The fixed-`A` reduction uses the full symmetric spectrum, including positive/negative competitors. The two displayed product forms cover both sign configurations and repeated prime entries are allowed when they arise from the two frequency pairs.

Falsify the finding by exhibiting a pair of distinct signed prime-ratio frequencies violating the parity spacing floor, an error in the layer-cake identity or its normalization, a fixed-`A` near-collision not representable by the stated bounded determinant forms, or a failure of either inclusion used in the `J_(K,c)` equivalence.

## Research consequence

The coarse `y^2` barrier has now been decomposed into a precise arithmetic statement. To prove

`D_v=o(y^2)`,

it is necessary and sufficient to show that the tapered coefficient measure places asymptotically vanishing mass on every fixed bounded-determinant collision family at macroscopic prime-product scale.

This supplies a clean next boundary for future work: estimate the weighted prime solutions of

`qr-ps=h` and `qs-pr=h`

for fixed even `h`, with all entries proportional to `y` and with the `VIS-192` taper weights. A generic reuse of the global minimum spacing, or an unweighted determinant count detached from the coefficient profile, would not address the remaining frontier.