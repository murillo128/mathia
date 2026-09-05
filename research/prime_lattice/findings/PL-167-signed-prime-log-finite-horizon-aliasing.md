# PL-167 — Signed prime-log characters force finite-height aliasing by logarithmic dimension

## Claim

Mixed-sign prime-lattice characters can evade the primorial high-frequency barrier of `PL-166` by cancelling prime-log energies, but sufficiently strong cancellation creates a different obstruction: by logarithmic prime dimension there is always a nontrivial signed character whose frequency is below the inverse observation horizon, so it is uniformly almost constant on the whole finite Kronecker orbit and simultaneously loses sensitivity to the horizontal zero coordinate.

Let `p_1<...<p_r` be the first `r` rational primes, put

`lambda_j=log p_j`,  `L_r=sum_(j<=r) lambda_j=theta(p_r)`,

and consider the signed dual cube `{-1,0,1}^r`. There exists a nonzero `m in {-1,0,1}^r` such that

`0 < delta_r=|<m,lambda>| <= L_r/(2^r-1)`.

For the prime Kronecker orbit

`z_r(t)=(exp(i t log p_1),...,exp(i t log p_r))`,

its character satisfies, for every `0<=t<=T`,

`|z_r(t)^m-1| <= T delta_r`.

Hence if, for any fixed `epsilon>0`,

`r=ceil((1+epsilon) log_2 T)`,

then the prime number theorem gives `L_r~p_r~r log r` and therefore

`T delta_r << (log T)(log log T)/T^epsilon -> 0`.

So a nontrivial coefficient-one signed Fourier character has Haar mean zero on `T^r` while being `1+o(1)` uniformly on the **entire** orbit segment `0<=t<=T`, and consequently on every zeta-zero phase vector with `0<gamma<=T`.

This resonance is genuinely many-prime. If `k=|supp(m)|` and `delta_r<log 2`, then writing `exp(delta_r)=a/b>1` in lowest terms gives coprime square-free products `a,b` of primes at most `p_r`, with `b>1`, and

`delta_r >= 1/(p_r^k+1)`.

For the logarithmic-dimensional choice above this forces

`k >= (1+epsilon+o(1)) log T/log log T`.

Finally, for every nontrivial zero `rho=beta+i gamma` with `0<gamma<=T`,

`exp((rho-1/2) delta_r)=1+o(1)`

uniformly whenever `T delta_r->0`. Thus the same signed cancellation that defeats the positive-semigroup primorial frequency growth also erases the `beta-1/2` weight needed to distinguish a hypothetical off-critical frontier. The resulting large character average is finite-horizon aliasing, not an RH-sensitive arithmetic resonance.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SIGNED-DUAL-BOUNDARY`. The subset-sum estimate, support lower bound, and horizontal-insensitivity statement are elementary exact deductions. Ford--Meng--Zaharescu's signed Fourier analysis and near-zero-frequency terms are prior-art context already preserved in `PL-162` and `PL-166`; no novelty is claimed for Kronecker/Diophantine aliasing or for their explicit-formula machinery. The negative scope is limited to using very low-energy mixed-sign first-moment phase characters as the growing-dimensional escape from `PL-166`.

## A coefficient-one signed character is forced close to zero frequency

Consider all `2^r` subset sums

`L_A=sum_(j in A) lambda_j`,  `A subseteq {1,...,r}`.

Every `L_A` lies in `[0,L_r]`. They are all distinct: if `L_A=L_B`, exponentiation gives

`product_(j in A) p_j = product_(j in B) p_j`,

so unique factorization forces `A=B`.

Order these `2^r` real numbers increasingly. The `2^r-1` adjacent gaps sum to `L_r`, hence one adjacent pair `A,B` satisfies

`0<|L_A-L_B|<=L_r/(2^r-1)`.

Set

`m=1_A-1_B in {-1,0,1}^r`.

After cancelling the common coordinates `A intersect B`, this is a nonzero signed exponent vector and

`delta_r=|<m,lambda>|=|L_A-L_B|`.

This is the exact dual-lattice escape that positive-semigroup arguments do not see: large positive and negative prime-log contributions can cancel even though no exact nontrivial integer relation among the prime logarithms exists.

The estimate is deliberately elementary and generic. The only prime-specific input is exact distinctness of the subset sums from unique factorization. Any sufficiently independent positive frequency list has the same finite-packing phenomenon, so the existence of the small signed frequency is not evidence for a special Riemann-zero mechanism.

## Logarithmic prime dimension destroys uniform finite-height Haar resolution

For the character indexed by `m`,

`chi_m(z_r(t))=exp(i t <m,lambda>)`.

Choose the sign of `m` so that `<m,lambda>=delta_r>0`. The elementary inequality `|e^(iu)-1|<=|u|` gives

`sup_(0<=t<=T) |chi_m(z_r(t))-1| <= T delta_r`
` <= T L_r/(2^r-1)`.

Now take `r=ceil((1+epsilon)log_2 T)`. The prime number theorem and the standard asymptotic for the `r`th prime give

`L_r=theta(p_r)~p_r~r log r`,

whereas `2^r>=T^(1+epsilon)`. Therefore

`T L_r/(2^r-1)`
` = O((log T)(log log T)/T^epsilon)`
` -> 0`.

The character `chi_m` has Haar integral zero because `m!=0`, but every probability measure supported on the orbit segment `{z_r(t):0<=t<=T}` has character moment `1+o(1)`. In particular, if `mu_T` is the empirical measure of the zeta-zero phase vectors `z_r(gamma)` for `0<gamma<=T`, then

`integral chi_m dmu_T = 1+o(1)`.

Thus one cannot ask for a growing-dimensional Haar approximation that is uniform over even the coefficient-one signed cube once `r` reaches this logarithmic scale. This does not contradict `PL-162` or Ford--Meng--Zaharescu: their simultaneous distribution theorem fixes the dimension and then lets `T` grow. Here the test character itself changes with `T` and is selected from a Fourier family whose cardinality grows exponentially with `r`.

The obstruction is stronger than merely saying that a quantitative equidistribution theorem has bad constants. At this scale a particular nontrivial character is geometrically unresolved by **any** sampling of the finite orbit segment, independently of the arithmetic nature of the sample times.

## The near-resonance necessarily uses a growing number of prime coordinates

The pigeonhole argument could be misleading if its tiny frequency were secretly produced by a fixed-prime relation. It is not.

Let `k=|supp(m)|` and orient `m` so that `delta=<m,lambda>>0`. Then

`e^delta=a/b`,

where `a` is the product of the primes with coefficient `+1` and `b` the product of the primes with coefficient `-1`. After the common subset has been cancelled these are coprime square-free integers. If `delta<log 2`, then `b>1`; otherwise `b=1` would imply the integer `a>=2` and hence `delta=log a>=log 2`.

Since `a>b`, we have `a>=b+1`. Therefore

`delta=log(a/b)`
` >= log(1+1/b)`
` >= 1/(b+1)`
` >= 1/(p_r^k+1)`.

Combining this with the subset-sum upper bound yields

`p_r^k+1 >= (2^r-1)/L_r`.

For `r=ceil((1+epsilon)log_2 T)`, taking logarithms and using `log p_r~log log T` gives

`k >= (1+epsilon+o(1)) log T/log log T`.

So the unresolved signed mode is genuinely a growing-support prime-lattice character. It does not contradict the fixed-finite-prime caps of `PL-164` and `PL-165`, and it identifies the price paid for avoiding the primorial corner of `PL-166`: cancellation must involve an increasing number of prime directions.

## Low signed energy simultaneously erases the horizontal zero coordinate

A possible hope would be that a near-zero signed frequency is vertically aliased but still retains the horizontal weight `beta-1/2` that `PL-162` showed to be essential. It does not.

Put `x=e^delta`. For an actual nontrivial zero `rho=beta+i gamma`, the normalized Landau-type factor is

`x^(rho-1/2)=exp((beta-1/2+i gamma)delta)`.

All nontrivial zeros satisfy `0<beta<1`. Hence for `0<gamma<=T`,

`|(rho-1/2)delta| <= (T+1/2)delta`.

If `T delta->0`, then uniformly over every such zero

`x^(rho-1/2)=1+o(1)`.

At the same time

`x^(i gamma)=1+o(1)`.

Thus this low-energy signed character cannot distinguish a zero with `beta=1/2` from one near a hypothetical extremal abscissa `Theta>1/2`: both the vertical phase and the horizontal exponential weight have collapsed to the same constant at the observation scale.

This is the key complement to `PL-166`. Positive mixed characters keep horizontal sensitivity but their arithmetic energy grows through primorial products; signed characters can keep the **net** energy tiny by cancellation, but once it drops below `1/T` the entire normalized zero observable becomes kinematically trivial.

## Relation to Landau--Gonek and Ford--Meng--Zaharescu

The fixed-dimensional signed Fourier framework is prior art. Ford--Meng--Zaharescu attach to an integer Fourier vector `m` the real multiplicative frequency

`x_m=exp(2 pi <m,alpha>)`,

and for prime-log coordinates `alpha_j=log p_j/(2 pi)` this is exactly

`x_m=product_j p_j^(m_j)`.

Their explicit-formula comparison has a `T`-scale arithmetic main term only at prime-power frequencies. This is already specialized in `PL-162`: for the full-rank prime-log relation matrix, the secondary density is additive along the prime coordinate axes.

For the present near-resonant `m`, once `delta<log 2` both signs occur and `x_m=a/b` is a noninteger reduced rational. It is therefore not an integer prime power, so its von-Mangoldt main term is absent. A large empirical character moment near `1` is not hidden mixed-prime arithmetic; it occurs because `log x_m=delta` is too small for a time interval of length `T` to resolve.

This is also consistent with the near-zero-frequency terms in the Ford--Meng--Zaharescu proof: when `log x` is of order `1/T` or smaller, the finite observation interval itself permits contributions of zero-count scale rather than the ordinary `T`-scale prime-power discrepancy. Their theorem treats fixed dimension and controls such Diophantine effects; the new derived step here is only the growing-prime subset-sum bookkeeping showing that a coefficient-one near-zero mode is unavoidable by logarithmic dimension.

No Euler product is analytically continued in this argument. The signed rational frequency is formed algebraically from prime logarithms, and the horizontal statement is evaluated on the already-existing nontrivial zero set.

## Prior-art and novelty audit

The closest theorem-level source is Kevin Ford, Xianchang Meng, and Alexandru Zaharescu, “Simultaneous distribution of the fractional parts of Riemann zeta zeros,” *Bulletin of the London Mathematical Society* **49**(1) (2017), 1--9, DOI `10.1112/blms.12001`, arXiv `1511.06814`. Their paper already uses signed Fourier vectors, the multiplicative frequency `x_m`, uniform explicit-formula comparison in a restricted frequency range, and special treatment of very small linear forms. Those facts are already part of the canonical evidence in `PL-162` and `PL-166`.

The infinite-torus/Kronecker background is also classical; `PL-011` and the line source ledger already record it. The subset-sum proof above is a generic pigeonhole argument and is not claimed as a new Diophantine theorem.

The durable delta relative to the current Mathia frontier is narrower. `PL-164` explicitly left mixed-sign/rational characters outside its positive-semigroup cap, and `PL-166` left a sparse cross-prime statistic with low maximal arithmetic energy as a possible escape from the primorial horizon. The present finding shows that the most extreme version of that escape has a universal counter-cost: if signed cancellation reduces the energy below inverse height by logarithmic prime dimension, the character becomes uniformly invisible to both `gamma` and `beta-1/2`. This is a finite-horizon route restriction, not a novelty claim about the underlying harmonic analysis.

## Adversarial boundaries

1. **No obstruction is proved for sublogarithmic dimension.** The argument supplies a sufficient aliasing scale. It does not determine the sharp smallest `r(T)` for prime logarithms.

2. **Moderate nonzero signed frequencies remain open.** A signed character with `T|<m,lambda>|` bounded away from zero can still oscillate and retain horizontal sensitivity. The theorem closes only the attempt to win by making the net signed energy extremely small.

3. **The result is first-moment/character-level.** Higher zero correlations, nonlinear observables, determinants, or target-relative constructions can use information not present in one character moment and are not excluded.

4. **This is not a growing-dimensional equidistribution theorem.** It proves the opposite kind of statement: uniform Haar control over a broad growing Fourier class is impossible because one test character is unresolved. It says nothing about smaller prescribed Fourier families.

5. **The character depends on the observation horizon.** There is no conflict with fixed-character Kronecker equidistribution or with fixed-dimensional Ford--Meng--Zaharescu asymptotics.

6. **The support lower bound is specific to the coefficient cube `{-1,0,1}^r`.** Allowing larger integer coefficients changes the quantitative Diophantine bookkeeping, although it cannot remove the basic finite-time principle that frequencies much smaller than `1/T` are unresolved.

7. **No sparse off-line zero sequence is constructed or excluded.** The result only shows that an inverse-height signed frequency cannot be the detector that excludes such a sequence, because it is uniformly blind to the horizontal displacement as well.

8. **The phenomenon is generic after the frequency list is fixed.** Rational primes provide exact multiplicative independence and a canonical logarithmic energy, but the packing/aliasing mechanism itself survives matched non-arithmetic controls.

A falsification would require two distinct prime subset sums to coincide, failure of the adjacent-gap pigeonhole estimate, failure of the elementary finite-time character bound, or failure of the rational support lower bound. None depends on unproved information about zeta zeros.

## Consequence for the research line

The growing-dimensional first-moment phase program now has two opposite frequency barriers. In the positive integer semigroup, genuinely full-support characters acquire primorially large energy and outrun the unconditional comparison range (`PL-166`). In the signed dual lattice, cancellations can suppress that energy, but if they suppress it to the scale needed to evade finite-height frequency cost completely, logarithmic dimension forces unresolved characters that are simultaneously blind to horizontal zero displacement.

Therefore the next mixed-prime candidate cannot be justified merely by saying that signed exponents keep `|<m,log p>|` small. A viable construction must keep the relevant signed frequencies **resolvable** on the zero-height scale while obtaining a genuinely arithmetic cross-prime signal, or it must leave first moments and use higher-order/target-relative structure. That is a materially narrower target than the low-energy sparse-statistic escape left open by `PL-166`.