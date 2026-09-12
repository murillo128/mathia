# VIS-192 — start averaging turns the subcritical signed off-diagonal into `H^-1` energy

## Claim

Keep the notation of `VIS-189`--`VIS-191`. Fix `0 <= alpha < 1/2`, put

`a_p=p^(-alpha)`, `Q_y=sum_(p<=y) a_p^2`, `beta=1-2alpha>0`,

and let `v in C^2([0,1])` be real-valued with

`v(0)=v(1)=0`, `V=int_0^1 v(u) du != 0`.

Write

`kappa_v(theta)=V^(-1) int_0^1 v(u) exp(i theta u) du`

and let `M_v(y;H,T)` be the normalized tapered mean square from `VIS-189`. Define its long-start Cesaro variance by

`R_v(y,H)=lim_(R->infinity) R^(-1) int_0^R |M_v(y;H,T)-1|^2 dT`.

Then the limit exists and one has the exact identity

`R_v(y,H)`
` = 2 Q_y^(-2) sum_(p<q<=y) p^(-2alpha) q^(-2alpha) |kappa_v(H log(q/p))|^2`.

Consequently, whenever `H=H(y)->infinity` and `H<=y`,

`R_v(y,H) <<_(alpha,v) 1/H`.

If in addition

`H log y / y -> 0`,

then the bound is order-sharp:

`R_v(y,H) asymp_(alpha,v) 1/H`.

Thus throughout every diverging strictly subcritical observation scale, including scales far below the absolute-envelope threshold `y/log y`, the signed quadratic off-diagonal has root-mean-square size

`|M_v-1|_start-rms asymp H^(-1/2)`

under long Cesaro averaging of the interval start `T`.

At the critical absolute-envelope scale `H asymp y/log y`, the upper bound alone gives

`R_v(y,H) << log y / y -> 0`.

So `VIS-191` and the present result separate two genuinely different statements: the absolute pair mass remains order one below `y/log y`, while the signed off-diagonal is nevertheless small for a density-one set of interval starts as soon as `H->infinity`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FOURIER/DIRICHLET-POLYNOMIAL ORTHOGONALITY + AUDITED PRIME-PAIR SIEVE INPUT + PNT LOWER CONTROL + NO-NOVELTY-CLAIM`.

This is a statement about long averaging in the **start variable**. It is not a uniform-in-`T` estimate and does not control a start interval whose length is tied to `y`.

## 1. The signed off-diagonal is a finite positive-frequency polynomial in the start

Changing variables in the observation kernel gives

`K^v_(H,T)(p,q)`
` = exp(i T log(q/p)) kappa_v(H log(q/p))`.

Because `v` is real, the two off-diagonal orientations are conjugates. Hence

`M_v(y;H,T)-1 = 2 Re S_v(y;H,T)`,

where

`S_v(y;H,T)`
` = Q_y^(-1) sum_(p<q<=y) a_p a_q kappa_v(H log(q/p)) exp(i T log(q/p))`.

For prime pairs `p<q`, every frequency

`lambda_(p,q)=log(q/p)`

is positive. It is also unique: if

`q/p=q'/p'`

for primes `p<q` and `p'<q'`, both fractions are already reduced, so unique factorization forces `p=p'` and `q=q'`.

Therefore ordinary finite-frequency Cesaro orthogonality gives

`lim_(R->infinity) R^(-1) int_0^R |S_v(T)|^2 dT`
` = Q_y^(-2) sum_(p<q<=y) a_p^2 a_q^2 |kappa_v(H lambda_(p,q))|^2`.

Meanwhile every frequency occurring in `S_v(T)^2` is a positive sum `lambda_(p,q)+lambda_(r,s)`, so its Cesaro mean is zero. Since

`(2 Re S)^2 = S^2 + conjugate(S)^2 + 2|S|^2`,

the displayed exact formula for `R_v` follows.

This step is only Parseval/orthogonality for a finite exponential polynomial. It does not invoke random phases, independence, a probabilistic model of the primes, or an unproved prime-pair asymptotic.

## 2. Squaring the taper kernel makes the start energy summable at scale `1/H`

`VIS-188` gives the endpoint-zero Fourier decay

`|kappa_v(theta)| <<_v min(1,|theta|^(-2))`.

Hence

`|kappa_v(theta)|^2 <<_v min(1,|theta|^(-4))`.

For a dyadic near-pair block

`x<p<=2x`, `p<q<3p/2`, `d=q-p`,

one has as in `VIS-189`--`VIS-190`

`log(q/p) >= d/(3x)`.

The source-audited Selberg upper-bound sieve and singular-series average used there give

`#{p in (x,2x] : p and p+d prime} << S(d) x/(log x)^2`,

`A(U)=sum_(d<=U) S(d) << U`.

Put `D=x/H`. The squared-kernel gap aggregate is

`G_4(D)=sum_(d<=x) S(d) min(1,(D/d)^4)`.

Partial summation from `A(U)<<U` gives

`G_4(D) << D` when `D>=1`,

and

`G_4(D) << D^4` when `D<1`.

Because the squared coefficient product on the block is

`a_p^2 a_q^2 << x^(-4alpha)`,

the near-pair start-energy contribution from one block is

`<<_(alpha,v) x^(1-4alpha)/(log x)^2 G_4(x/H)`.

For `x>=H` this is

`<<_(alpha,v) x^(2-4alpha)/(H (log x)^2)`,

while for `x<H` it is

`<<_(alpha,v) x^(5-4alpha)/(H^4 (log x)^2)`.

Since `2-4alpha>0` and `5-4alpha>0`, the corresponding dyadic sums are controlled by their upper scales. Using

`Q_y asymp_alpha y^(1-2alpha)/log y`,

one obtains, for `H->infinity` with `H<=y`,

`Q_y^(-2) E_near <<_(alpha,v) 1/H`.

For the far multiplicative region `q>=3p/2`, the fixed separation gives

`|kappa_v(H log(q/p))|^2 <<_v H^(-4)`,

so simply

`Q_y^(-2) E_far`
` << H^(-4) Q_y^(-2) (sum_(p<=y) p^(-2alpha))^2`
` << H^(-4)`.

Combining near and far pairs proves

`R_v(y,H) <<_(alpha,v) 1/H`.

The gain relative to the absolute envelope is structural: start averaging squares the pair coefficients before they are summed, while exact frequency orthogonality removes all cross terms between distinct prime ratios.

## 3. In the strictly subcritical regime the `1/H` scale is also unavoidable

The upper bound could in principle be much smaller. It is not when

`H log y / y -> 0`.

Since `kappa_v(0)=1`, continuity supplies constants `eta_v>0` and `c_v>0` such that

`|kappa_v(theta)| >= c_v`

for `|theta|<=eta_v`.

Consider only primes in `(y/2,y]`. The prime number theorem gives

`m=pi(y)-pi(y/2)=(1/2+o(1)) y/log y`.

Partition `(y/2,y]` into intervals of length

`ell=eta_v y/(8H)`.

There are `J<<_v H` such intervals. If their prime occupancies are `n_1,...,n_J`, Cauchy gives

`sum_j binom(n_j,2)`
` = (sum_j n_j^2-m)/2`
` >= (m^2/J-m)/2`.

The subcritical assumption implies

`m/J asymp_v y/(H log y) -> infinity`,

so the number of same-bin prime pairs is

`>>_v y^2/(H (log y)^2)`.

For every such pair,

`0<q-p<=ell`, `p>y/2`,

and therefore

`H log(q/p) <= H (q-p)/p <= eta_v/4`.

Thus the squared kernel is bounded below by a positive constant. Also

`p^(-2alpha)q^(-2alpha) >= y^(-4alpha)`.

Restricting the exact positive start-energy identity to these same-bin pairs yields

`R_v(y,H)`
` >>_(alpha,v) Q_y^(-2) [y^2/(H (log y)^2)] y^(-4alpha)`
` >>_(alpha,v) 1/H`.

Together with the upper bound this proves

`R_v(y,H) asymp_(alpha,v) 1/H`

throughout the diverging strictly subcritical regime.

Unlike `VIS-191`, this lower bound does not rely only on consecutive prime pairs. The occupancy argument counts the full population of prime pairs inside Fourier-unresolved additive cells and needs only the prime number theorem.

## 4. Density-one starts diagonalize even where the absolute envelope does not

For every fixed `epsilon>0`, Chebyshev applied to the long-start average gives

`limsup_(R->infinity) (1/R) meas{0<=T<=R : |M_v(y;H,T)-1|>epsilon}`
` <= R_v(y,H)/epsilon^2`
` <<_(alpha,v) 1/(epsilon^2 H)`.

Hence if `H(y)->infinity`, the exceptional set of starts has Cesaro density tending to zero.

In particular, at

`H asymp y/log y`,

the absolute envelope of `VIS-190` is only `O(1)` and `VIS-191` shows that below this scale it cannot vanish at all. Yet the signed statistic satisfies

`R_v << log y/y ->0`.

So the unresolved short-gap population is not by itself evidence of a persistent signed quadratic signal. Its absolute mass can remain macroscopic while its start-dependent phases cancel for almost every sufficiently long-translated observation window.

This does **not** settle the stronger uniform question. A small long-start variance permits exceptional starts, and the present Cesaro limit allows the averaging horizon in `T` to go to infinity after `y,H` are fixed.

## 5. Prior art and novelty boundary

Long-parameter mean values of Dirichlet polynomials and the use of frequency orthogonality are classical. Hugh L. Montgomery, **Mean and large values of Dirichlet polynomials**, *Inventiones Mathematicae* 8 (1969), 334--345, DOI `10.1007/BF01404637`, is a standard early anchor for this mean-value viewpoint. Montgomery and Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* s2-8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`, is a classical source for the closely related quantitative mean-value machinery for separated Dirichlet frequencies.

The exact infinite-start identity here is simpler than those quantitative finite-interval theorems: it is just Cesaro orthogonality of the finitely many distinct frequencies `log(q/p)`. The prime-pair upper-bound sieve and averaged singular-series input are the same already audited in `VIS-185`, `VIS-186`, `VIS-189`, and `VIS-190`; the matching lower bound uses only the prime number theorem plus Cauchy on short-cell occupancies.

No novelty is claimed for Parseval/Cesaro orthogonality, Dirichlet-polynomial mean values, the Selberg sieve, the prime number theorem, or the general principle that translated phases decorrelate in mean. The Mathia-specific contribution is the exact placement of that classical mechanism against the `VIS-190`--`VIS-191` absolute threshold: the same unresolved prime-pair population has order-one absolute mass but only `Theta(1/H)` long-start signed energy in the strictly subcritical regime.

## Boundaries and falsification

The exponent `alpha` and taper `v` are fixed. The taper is real-valued and endpoint-zero; constants are not uniform over varying taper families or as `alpha->1/2`.

The average in `T` is a long Cesaro average taken with `y` and `H` fixed first. The result does not provide an effective averaging length in `T`, does not control a start horizon comparable to `y` or `H`, and does not prove a uniform bound for every start. Those require quantitative spacing information between the frequencies `log(q/p)` rather than only their exact distinctness.

The lower `R_v>>1/H` bound requires `H log y/y->0`; at the constant critical scale `H=c y/log y`, only the upper bound is asserted here. The absolute-envelope statements of `VIS-190` and `VIS-191` remain unchanged.

Falsify the finding by locating an error in the distinct-ratio orthogonality, the exact factor `2` in the start variance, the squared taper tail, the `G_4(D)` partial-summation bounds, the dyadic normalization, or the same-bin occupancy lower bound.

## Research consequence

The signed-cancellation question now has a precise separation of levels. The absolute method genuinely stops at `y/log y`, but long translation of the observation window already diagonalizes the signed quadratic statistic in mean square at every diverging `H`, with the subcritical fluctuation energy exactly of order `1/H`.

The remaining difficult question is therefore **effective dephasing in the start variable**: how long a finite `T`-range is needed before the distinct prime-ratio frequencies behave close to their Cesaro-orthogonal limit, especially when `H<=y/log y`. That depends on near-collisions between `log(q/p)` frequencies and is a separate coherent investigation rather than a continuation of the present proof.
