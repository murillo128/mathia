# VIS-201 — averaged four-form local factors remove the pointwise log-log loss

## Claim

Keep the fixed-`A` nondegenerate top-scale prime-ratio crowding setting of `VIS-195`--`VIS-200`. Thus

`d=g d_0`, `e=g e_0`, `gcd(d_0,e_0)=1`,

`m=+/- h/g != 0`,

with `h`, `g|h`, and `m` ranging over finite `A`-dependent sets, and the four-prime fiber has local conductor

`Q=d_0 e_0 g m (m^2-g^2 d_0^2 e_0^2) != 0`.

Let `S_4(d,e)` be the four-form local-density product from `VIS-197`. For each fixed allowed `g,m` there is a nonnegative arithmetic majorant `G_A(n)` such that the admissible top-scale second gaps satisfy

`sum_(e_0 in I_A(d_0), Q!=0) S_4(g d_0,g e_0) <<_A d_0 G_A(d_0)`,

where `I_A(d_0)` denotes the possible top-scale `e_0` values, and

`G_A(n) <<_A prod_(p|c_A n) (1+C_A/p)`

for fixed `A`-dependent constants `c_A,C_A`. Consequently

`sum_(n<=D) G_A(n) <<_A D`,

and, for every fixed allowed `g` and `Y>=1`,

`sum_(d_0>=1) min(1,(Y/(g d_0))^4) G_A(d_0) <<_A Y`.

Thus the pointwise factor

`B(y)=(1+log log(3+y))^4`

in the `VIS-199`/`VIS-200` four-form sieve can be replaced after the `e`-fiber sum by a bounded-mean factor. More precisely, for the generalized cutoff

`Y=y/H`, `X=Y L`,

with `L>=1`, `H/L -> infinity`, and the same strictly subcritical assumptions as `VIS-200`,

`C_(y,H)(A)`
` <<_(A,alpha,v)`
`    (log y)^2/[log(H/L)]^4`
`    + (log y)^2/L^3`
`    + H/(y log y)`.

In particular, taking `L=log y`,

`sqrt(log y) = o(log(H/log y))`

and

`H log y/y -> 0`

are sufficient for `D_v(y,H)=o(y^2)`. Since the first condition implies `log H >> log log y`, it is equivalently enough here that

`sqrt(log y)=o(log H)`.

This removes the extra `1+log log y` multiplier in the sufficient horizon condition of `VIS-199` without changing the dephasing resource or sieve dimension.

**Evidence/status:** `LITERATURE+DERIVED + DISCRIMINANT-UNIFORM POLYNOMIAL AVERAGE + HORIZON EXTENSION + NO-NOVELTY-CLAIM`.

The discriminant-uniform averaging theorem is due to Henriot/Nair--Tenenbaum and is not new. The Mathia-specific content is the exact specialization to the `VIS-197` conductor family, verification of the corrected discriminant dependence, the bounded-mean first-gap majorant, and its insertion into the already-established `VIS-199`/`VIS-200` weighted crowding architecture.

## 1. Reduce the local conductor to three primitive polynomial values

Put

`a=g d_0`, `c=gcd(a,m)`, `A_0=a/c`, `M=m/c`.

Because `c|m` and `g,m` range over finite `A`-dependent sets, `c` ranges over a finite set depending only on `A`. Moreover

`gcd(A_0,M)=1`.

The conductor factors as

`|Q| = |d_0 g m| c^2 e_0 |M-A_0 e_0| |M+A_0 e_0|`.

Let

`f(n)=(n/phi(n))^4`.

Since the set of prime divisors of a product is the union of the prime-divisor sets of its factors,

`f(uv) <= f(u)f(v)`

for all positive integers `u,v`. The pointwise bound of `VIS-197` therefore gives

`S_4(g d_0,g e_0)`
` <<_A f(d_0) f(e_0) f(|M-A_0e_0|) f(|M+A_0e_0|)`.

The fixed factors involving `g,m,c` have been absorbed into the `A`-dependent constant.

The top-scale relation inherited from `VIS-195`--`VIS-196` is

`e p=d r+O_A(1)`

with `p,r=Theta_A(y)`. Hence

`e/d = r/p+o_A(1)`

uniformly on the dangerous fixed-`A` regime. After changing the `A`-dependent constants and absorbing finitely many small cases,

`c'_A d_0 <= e_0 <= C'_A d_0`.

Thus all admissible `e_0` lie in an interval of location and length `Theta_A(d_0)`. It is enough to average over that whole interval; it can be covered by `O_A(1)` subintervals `(x,x+z]` with

`x asymp_A z asymp_A d_0`.

## 2. Henriot's corrected discriminant-uniform bound applies uniformly in `d_0`

Consider the three primitive linear polynomials

`R_1(E)=E`,

`R_2(E)=M-A_0E`,

`R_3(E)=M+A_0E`.

They are pairwise non-proportional because `M!=0` and `gcd(A_0,M)=1`. Their product

`P(E)=E(M-A_0E)(M+A_0E)=M^2E-A_0^2E^3`

is primitive by Gauss' lemma and has coefficient norm

`||P||=M^2+A_0^2 <<_A d_0^2`.

The function

`F(n_1,n_2,n_3)=f(n_1)f(n_2)f(n_3)`

is a nonnegative multiplicative member of Henriot's Nair--Tenenbaum class: `f(p^nu)=(1-1/p)^(-4)<=16`, while the classical bound `n/phi(n)<<log log(3+n)` gives `f(n)<<_epsilon n^epsilon` for every fixed `epsilon>0`.

Choose, for example, fixed theorem parameters `delta=1/3` and `alpha=1/2`, then choose the function-class `epsilon` small enough for Henriot's hypothesis. On each `Theta_A(d_0)` interval above, for all sufficiently large `d_0`,

`x >= C_A ||P||^(1/3)`

and

`x^(1/2) <= z <= x`

after splitting into `O_A(1)` comparable subintervals when necessary. Finitely many remaining `d_0` are absorbed into the implied constant. Absolute values in Henriot's theorem handle either sign of `R_2(E),R_3(E)`; the top-scale interval is in any case far from their `O_A(1/d_0)` real roots for large `d_0`.

The 2014 erratum is load-bearing here. For non-monic factors, Corollaries 1--2 of the 2012 paper remain valid with the discriminant correction supported on

`a_* D_*`

rather than `D_*` alone, where `a_*` is the leading coefficient of the square-free product. In the present cubic,

`a_*=-A_0^2`,

`D_*=Disc(P)=4A_0^2M^6`,

so

`a_*D_*=-4A_0^4M^6`.

Therefore every prime in the corrected exceptional support divides `2A_0M`, hence divides a fixed `A`-dependent integer times `d_0`.

Henriot's explicit discriminant factor satisfies, after the erratum replacement,

`Delta_(a_*D_*) <= prod_(p|a_*D_*) (1+1/p)^C`

for a fixed constant `C` determined only by the fixed degree and multiplicative-function class.

Outside this exceptional support, the three linear factors have one root each and three distinct roots in total. The generic Euler factor in Henriot's Corollary 2 is therefore

`(1-3/p)(1+f(p)/p)^3 = 1+O(p^-2)`

for `p>3`. Its product is bounded; the finitely many small primes are absorbed into the constant. Corollary 2 consequently gives

`sum_(E in I_A(d_0)) f(E)f(|M-A_0E|)f(|M+A_0E|)`
` <<_A d_0 Delta_(a_*D_*)`.

Combining this with Section 1 proves

`sum_(e_0 in I_A(d_0), Q!=0) S_4(gd_0,ge_0)`
` <<_A d_0 G_A(d_0)`

with

`G_A(d_0)=f(d_0) Delta_(a_*D_*)`.

Since the exceptional support is contained in the primes dividing `c_A d_0`, this `G_A` obeys

`G_A(d_0) <<_A prod_(p|c_A d_0)(1+C_A/p)`.

## 3. The discriminant correction has bounded first mean

It remains to verify that the correction is harmless after the first-gap sum, not merely on each individual fiber.

For a fixed constant `C>0`,

`prod_(p|n)(1+C/p)`
` = sum_(q|n, q squarefree) C^(omega(q))/q`.

Therefore

`sum_(n<=D) prod_(p|n)(1+C/p)`
` <= D sum_(q squarefree) C^(omega(q))/q^2`
` = D prod_p (1+C/p^2)`
` <<_C D`.

The fixed primes in `c_A` change only the implied constant. Hence

`sum_(n<=D)G_A(n)<<_A D`.

The taper-weighted version follows by partial summation or dyadic decomposition. Put `Z=Y/g`. The prefix estimate gives

`sum_(n<=Z)G_A(n)<<_A Z`,

while

`Z^4 sum_(n>Z) G_A(n)/n^4`
` <<_A Z^4 sum_(j>=0) [2^j Z]/[2^j Z]^4`
` <<_A Z`.

Thus

`sum_(d_0>=1) min(1,(Y/(g d_0))^4)G_A(d_0)<<_A Y`.

This proves both stages requested by `CLUE-four-form-average-local-factor`.

## 4. Insert the average before the first-gap sum

Return to the generalized `VIS-200` cutoff `X=YL`, `Y=y/H`, and write

`M_H=H/L`.

For one nondegenerate fiber in the sieve region `d<=X`, the same dimension-four upper-bound sieve used in `VIS-199`--`VIS-200` gives

`# {dangerous prime parameters on the fiber}`
` <<_A S_4(d,e) y/[d (log M_H)^4]`.

Instead of replacing `S_4(d,e)` by its pointwise worst-case maximum and then counting `O_A(d)` second gaps, sum it first over the admissible `e`. Since `d=g d_0` with fixed `g`, Section 2 gives

`sum_e S_4(d,e) <<_A d G_A(d/g)`.

Hence the total prime-parameter count at first gap `d` is

`<<_A y G_A(d/g)/(log M_H)^4`.

The coefficient envelope from `VIS-194`--`VIS-200` is

`|c_lambda|^2 <<_(A,alpha) (log y)^2/y^2 * w_d`,

`w_d=min(1,(Y/d)^4)`.

Summing over `d<=X` and using Section 3 gives unnormalized nondegenerate collision mass

`<<_(A,alpha,v)`
` (log y)^2/[y (log M_H)^4]`
` * sum_d w_d G_A(d/g)`
` <<_(A,alpha,v)`
` (log y)^2/[H (log M_H)^4]`.

The strictly subcritical normalization remains

`R_v(y,H) asymp_(alpha,v) 1/H`.

Therefore the normalized sieve-region contribution is

`<<_(A,alpha,v) (log y)^2/[log(H/L)]^4`.

The unsieved taper tail and conductor-zero three-prime branch do not use the pointwise four-form local factor, so the `VIS-200` estimates remain unchanged:

`(log y)^2/L^3`

and

`H/(y log y)`.

This proves the bound in the claim.

With `L=log y`, the tail is `1/log y`, and the sieve term tends to zero exactly when

`log(H/log y)/sqrt(log y) -> infinity`.

Under that condition `log log y=o(log H)`, so this is equivalent at the present level to

`sqrt(log y)=o(log H)`.

The layer-cake equivalence in `VIS-195` then yields `D_v=o(y^2)`.

## Prior-art audit

Kevin Henriot, **Nair--Tenenbaum bounds uniform with respect to the discriminant**, *Mathematical Proceedings of the Cambridge Philosophical Society* 152:3 (2012), 405--424, DOI `10.1017/S0305004111000752`, is the decisive external theorem. Its Theorem 5 gives discriminant-uniform short-interval polynomial-value bounds, and Corollary 2 makes the exceptional-discriminant factor explicit. The paper itself already emphasizes that this uniformity is designed for subsequent averaging over a varying polynomial parameter.

Kevin Henriot, **Nair--Tenenbaum uniform with respect to the discriminant--ERRATUM**, *Mathematical Proceedings of the Cambridge Philosophical Society* 157:2 (2014), 375--377, DOI `10.1017/S0305004114000280`, corrects the congruence bookkeeping and the non-monic discriminant identity. The upper bounds remain valid; for Corollaries 1--2 the exceptional quantity `D_*` must be replaced by `a_*D_*`. The present derivation uses that corrected form explicitly.

Thus the polynomial-value average, discriminant correction, and its generic Euler-product mechanism are established prior art. No novelty is claimed for them, for the elementary bounded mean of `prod_(p|n)(1+C/p)`, or for the Selberg/large-sieve input already audited in `VIS-197`--`VIS-200`.

The Mathia-specific step is narrower: the exact `VIS-197` conductor happens to factor into three primitive coefficient-dependent affine values whose corrected discriminant support is carried only by the first gap `d_0` up to fixed factors. This permits the local factor to be averaged before the weighted first-gap sum and removes the `B(y)` loss from the already-established crowding estimate.

## Boundaries and falsification

The fixed normalized crowding multiplier `A` remains essential. It keeps `h`, `g`, and `m` in finite sets and supplies the uniform top-scale comparison `e_0=Theta_A(d_0)`. No theorem uniform in `A=A(y)->infinity` is claimed.

The statement treats only the nondegenerate `Q!=0` four-form fibers with Henriot averaging. The exact `Q=0` three-prime-progression branch remains separated exactly as in `VIS-197`--`VIS-200`.

The new horizon is still only sufficient for the Montgomery--Vaughan resource `D_v`. It does not show that `D_v` is necessary, does not reach `log H=Theta(sqrt(log y))`, and does not address polylogarithmic or arbitrarily slow horizons. A divergent factor beyond `sqrt(log y)` is still required by the present dimension-four sieve term.

The application of Henriot relies on the top-scale second-gap interval having both location and length comparable to `d_0`, after bounded interval subdivision, and on the corrected non-monic exceptional support. If either comparison or discriminant computation is wrong, the bounded-mean conclusion need not follow.

Falsify the finding by exhibiting an allowed nondegenerate fiber for which the normalized three-linear-factor system is not primitive/pairwise coprime, a prime outside `a_*D_*` where the generic three-root Euler factor fails, a violation of Henriot's coefficient-norm/short-interval hypotheses in the top-scale regime, an omitted discriminant prime caused by the 2014 correction, an unbounded first mean for the stated `G_A`, or an error when inserting the averaged local factor into the `VIS-200` sieve sum.

## Research consequence

`VIS-200` identified the pointwise four-form local factor as the leading non-tail bottleneck after cutoff optimization. The present result removes that bottleneck at its source: exceptional local arithmetic can be averaged across the second-gap fiber with only a bounded-mean first-gap correction.

The current proof architecture therefore reaches every strictly subcritical horizon with

`log H/sqrt(log y) -> infinity`,

without the previous additional `log log y` separation. The next independent question is no longer whether the worst local factor can be averaged; it is whether the remaining `sqrt(log y)` four-form sieve threshold can be lowered by a genuinely coupled incidence estimate, stronger use of the prime conditions, cancellation across fibers, or a different dephasing resource.
