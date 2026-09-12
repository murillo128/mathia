# VIS-189 — endpoint-zero taper kills the full prime off-diagonal at linear observation scale

## Claim

Fix `0 <= alpha < 1/2`, put

`a_p = p^(-alpha)`,

`Q_y = sum_(p<=y) a_p^2`,

and write `beta=1-2alpha>0`.

Let `v in C^2([0,1])` satisfy

`v(0)=v(1)=0`, `V=int_0^1 v(x) dx != 0`,

and normalize the observation kernel by

`K^v_(H,T)(p,q)`
` = (H V)^(-1) int_T^(T+H) v((t-T)/H) exp(it log(q/p)) dt`.

Define the absolute normalized off-diagonal envelope

`O_v(y;H,T)`
` = Q_y^(-1) sum_(p<q<=y) a_p a_q |K^v_(H,T)(p,q)|`.

Then, for every fixed `alpha<1/2` and fixed taper `v`, uniformly in the interval start `T`,

`O_v(y;H,T) <<_(alpha,v) y^2/(H^2 log y)`

for sufficiently large `y`.

Consequently, if `H>=c y` for any fixed `c>0`,

`O_v(y;H,T) <<_(alpha,v,c) 1/log y -> 0`

uniformly in `T`.

In particular, for the quadratic taper `v(x)=6x(1-x)` from `VIS-188`, the **entire full-prefix prime off-diagonal is asymptotically negligible at the linear observation scale**, even after taking absolute values term by term. This removes not only the rectangular-window endpoint resonance of `VIS-187`, but also the unresolved possibility in `VIS-186` that `Theta(log y)` mesoscopic gap octaves could accumulate to an order-one quadratic contribution.

Equivalently, if

`A_y(t)=sum_(p<=y) a_p p^(it)`

and the taper is normalized by `V`, then

`M_v(y;H,T)`
` = Q_y^(-1) (H V)^(-1) int_T^(T+H) v((t-T)/H) |A_y(t)|^2 dt`

satisfies

`|M_v(y;H,T)-1| <<_(alpha,v) y^2/(H^2 log y)`.

Thus `M_v -> 1` uniformly for `H>=c y`.

**Evidence/status:** `LITERATURE+DERIVED + EXACT TAPER KERNEL + CLASSICAL PRIME-PAIR SIEVE INPUT + DECISIVE NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made for hard rectangular windows, tapers whose derivative norms grow with `y`, higher moments, nonlinear observables, discrete sampling, or RH.

## 1. Endpoint-zero taper gives a square-frequency tail

`VIS-188` establishes, by two integrations by parts, that

`|K^v_(H,T)(p,q)| <= C_v/(H |log(q/p)|)^2`,

where

`C_v = (|v'(0)|+|v'(1)|+int_0^1 |v''(x)| dx)/|V|`.

The bound is uniform in `T`. The key change from the rectangular kernel used in `VIS-185`--`VIS-187` is the second power: a hard endpoint leaves a `1/(H|log(q/p)|)` tail, whereas an endpoint-zero `C^2` taper leaves `1/(H|log(q/p)|)^2`.

The present question is whether that extra power merely removes the flat deterministic null of `VIS-188`, or whether it is strong enough to control the actual complete prime-pair off-diagonal. It is.

## 2. Near multiplicative pairs are absolutely summable

Split the near pairs into dyadic prime blocks

`x < p <= 2x`, `p<q<3p/2`,

and write `d=q-p`. Then `1<=d<x`. Since `q<3p/2<=3x`,

`log(q/p)=log(1+d/p) >= d/(p+d) >= d/(3x)`.

Hence

`|K^v_(H,T)(p,p+d)| <<_v x^2/(H^2 d^2)`.

Also

`a_p a_(p+d) <= x^(-2alpha)`.

Use the same source-audited uniform Selberg upper-bound sieve input as in `VIS-185` and `VIS-186`: for the two-shift singular series `S(d)`,

`#{p in (x,2x] : p and p+d prime} << S(d) x/(log x)^2`

through the present range, together with

`A(U)=sum_(d<=U) S(d) << U`.

Partial summation now gives a convergent square-weighted aggregate,

`sum_(d<=x) S(d)/d^2 << 1`.

Therefore the absolute near-pair contribution from one dyadic block is

`<<_(alpha,v) x^(-2alpha) [x/(log x)^2] [x^2/H^2] sum_(d<=x) S(d)/d^2`

`<<_(alpha,v) x^(3-2alpha)/(H^2 (log x)^2)`

` = x^(2+beta)/(H^2 (log x)^2)`.

Because `2+beta>0`, dyadic summation is geometrically dominated by the top scale, giving

`M_near <<_(alpha,v) y^(2+beta)/(H^2 (log y)^2)`.

Since the prime number theorem and partial summation give

`Q_y asymp_alpha y^beta/log y`,

we obtain

`M_near/Q_y <<_(alpha,v) y^2/(H^2 log y)`.

This is the decisive gain over the rectangular-window shell bound in `VIS-186`: the taper changes the gap weight from `1/d` to `1/d^2`, so summing all near-diagonal gap scales no longer costs `Theta(log y)`.

## 3. Far multiplicative pairs are smaller without any pair-correlation input

For the complementary pairs `q>=3p/2`,

`log(q/p) >= log(3/2)`,

so

`|K^v_(H,T)(p,q)| <<_v H^(-2)`.

No sieve is needed. By positivity,

`M_far`
` <= C_v H^(-2) (sum_(p<=y) p^(-alpha))^2`.

For fixed `alpha<1`, the prime number theorem and partial summation give

`sum_(p<=y) p^(-alpha) <<_alpha y^(1-alpha)/log y`.

Thus

`M_far <<_(alpha,v) y^(2-2alpha)/(H^2 (log y)^2)`
` = y^(1+beta)/(H^2 (log y)^2)`.

After division by `Q_y`,

`M_far/Q_y <<_(alpha,v) y/(H^2 log y)`,

which is smaller than the stated `y^2/(H^2 log y)` bound and is `O(1/(y log y))` when `H asymp y`.

Combining the near and far regions proves the claim.

## 4. The complete tapered quadratic mean is therefore diagonal

Expand the normalized tapered mean square:

`M_v(y;H,T)`
` = Q_y^(-1) sum_(p,q<=y) a_p a_q K^v_(H,T)(p,q)`.

Because the taper is normalized by `V`,

`K^v_(H,T)(p,p)=1`.

The diagonal contribution is therefore exactly `Q_y`, while the two off-diagonal orientations are complex conjugates when `v` is real. In any case their total modulus is at most `2 Q_y O_v(y;H,T)`.

Hence

`|M_v(y;H,T)-1| <= 2 O_v(y;H,T)`

and the same `O(1/log y)` convergence follows at `H>=c y`.

For the nonnegative quadratic taper of `VIS-188`, this is an ordinary smoothly weighted mean square. The conclusion is not merely that one flat-gap control disappears: the whole prime-pair quadratic off-diagonal is absolutely too small to survive full-prefix normalization.

## 5. Prior-art and novelty boundary

Every ingredient is classical or already source-audited in the current visual line. `VIS-188` records the classical Fourier-window mechanism behind the `1/z^2` tail of endpoint-zero tapers. `VIS-185` and `VIS-186` record the uniform Selberg upper-bound sieve and averaged singular-series input used here. Smoothly weighted mean values of Dirichlet polynomials and the use of rapidly decaying Fourier transforms to control off-diagonal terms are standard analytic-number-theory machinery.

The present finding therefore makes **no novelty claim** for smooth windowing, Dirichlet-polynomial mean values, prime-pair sieve bounds, or singular-series averaging. Its value is as a Mathia-specific closure result: combining the already-audited taper and prime-pair inputs shows that the full linear-scale quadratic channel, not merely selected gap bands or a deterministic null, disappears under this admissible observation functional.

## 6. Boundaries and falsification

The exponent `alpha` is fixed below `1/2`; constants are not claimed uniform as `alpha -> 1/2`. The critical case has separate normalization behavior in the earlier variance findings.

The taper is fixed as `y` grows. A family `v=v_y` whose endpoint derivatives or second derivative norm diverge could lose the uniform `C_v` bound and is not covered.

The conclusion concerns continuous averaging and the quadratic full-prefix prime polynomial. It does not imply corresponding results for Gram sampling, higher moments, sparse adversarial supports with a different normalization, nonlinear transforms, or another observation kernel.

The use of the prime-pair sieve occurs only for the near multiplicative region `q<3p/2`; far pairs are controlled trivially from the fixed positive logarithmic separation. Thus no unproved Hardy--Littlewood asymptotic is being assumed.

Falsify the finding by locating an error in the `1/log(q/p)^2` taper bound from `VIS-188`, the near/far multiplicative split, the uniform prime-pair sieve range used already in `VIS-185`--`VIS-186`, the convergence `sum S(d)/d^2 << 1`, the dyadic summation, or the normalization by `Q_y`.

## Research consequence

The live quadratic frontier has moved again. Under a fixed endpoint-zero `C^2` taper and `H asymp y`, **there is no remaining full-prefix prime-pair off-diagonal mechanism at any gap scale**: bounded gaps, subpolynomial bands, polynomial mesoscopic shells, cross-shell accumulation, and macroscopic multiplicative separations are all contained in the vanishing absolute envelope above.

A future positive route must therefore change at least one load-bearing feature: use a harder observation functional whose leakage is itself controlled, exploit higher/growing-order information, change the normalization/support geometry, move to a different sampling mechanism, or introduce source information not reducible to this tapered quadratic prime-log field. Repeating another gap-scale decomposition inside the same tapered quadratic statistic cannot reopen the channel.