# VIS-190 — endpoint-zero quadratic off-diagonal vanishes above the `y/log y` observation scale

## Claim

Keep the notation and hypotheses of `VIS-189`. Fix `0 <= alpha < 1/2`, put

`a_p=p^(-alpha)`, `Q_y=sum_(p<=y) a_p^2`, `beta=1-2alpha>0`,

and let `v in C^2([0,1])` satisfy

`v(0)=v(1)=0`, `V=int_0^1 v(x) dx != 0`.

For

`K^v_(H,T)(p,q)=(H V)^(-1) int_T^(T+H) v((t-T)/H) exp(it log(q/p)) dt`

and the absolute normalized off-diagonal envelope

`O_v(y;H,T)=Q_y^(-1) sum_(p<q<=y) a_p a_q |K^v_(H,T)(p,q)|`,

one has, uniformly in `T` and for `H>=1`,

`O_v(y;H,T) <<_(alpha,v) y/(H log y)` for `1<=H<=y`,

while for `H>=y`,

`O_v(y;H,T) <<_(alpha,v) y^2/(H^2 log y)`.

Consequently,

`H log y / y -> infinity`

is sufficient for

`O_v(y;H,T) -> 0`

uniformly in `T`. Equivalently, the normalized tapered mean square from `VIS-189` satisfies

`M_v(y;H,T)=1+o(1)`

throughout every observation regime with `H >> y/log y`.

In particular, for every fixed `epsilon>0`,

`H >= y/(log y)^(1-epsilon)`

gives

`|M_v(y;H,T)-1| <<_(alpha,v,epsilon) (log y)^(-epsilon)`.

At the boundary `H asymp y/log y`, this absolute-envelope argument gives only an `O(1)` off-diagonal bound. No claim is made that the boundary is sharp for the actual oscillatory mean, only that it is the natural resolution threshold of the present absolute-value sieve method.

**Evidence/status:** `LITERATURE+DERIVED + EXACT TAPER KERNEL + CLASSICAL PRIME-PAIR SIEVE INPUT + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

## 1. Use both the trivial kernel bound and the square-frequency tail

`VIS-188` gives the endpoint-zero decay

`|K^v_(H,T)(p,q)| <= C_v/(H |log(q/p)|)^2`,

uniformly in `T`. The normalized kernel also has the trivial bound

`|K^v_(H,T)(p,q)| <= B_v`,

where

`B_v = ||v||_1/|V|`.

Therefore

`|K^v_(H,T)(p,q)| <<_v min(1, 1/(H |log(q/p)|)^2)`.

The linear-scale estimate in `VIS-189` used only the decaying branch. That is sufficient for `H asymp y`, but it overcharges prime pairs whose logarithmic separation is smaller than the Fourier resolution `1/H` when `H<y`.

## 2. A dyadic prime block has an unresolved gap zone of width `x/H`

Consider

`x<p<=2x`, `p<q<3p/2`,

and write `d=q-p`. As in `VIS-189`,

`log(q/p) >= d/(3x)`.

Hence

`|K^v_(H,T)(p,p+d)| <<_v min(1,(x/(H d))^2)`.

Use the same source-audited Selberg upper-bound sieve input and averaged singular-series bound already used in `VIS-185`, `VIS-186`, and `VIS-189`:

`#{p in (x,2x] : p and p+d prime} << S(d) x/(log x)^2`,

`A(U)=sum_(d<=U) S(d) << U`.

With

`D=x/H`,

the gap aggregate is

`G(D)=sum_(d<=x) S(d) min(1,(D/d)^2)`.

If `D>=1`, split at `d=D`. The unresolved part satisfies

`sum_(d<=D) S(d) << D`,

while partial summation from `A(U)<<U` gives

`D^2 sum_(d>D) S(d)/d^2 << D`.

Thus

`G(D) << D` for `D>=1`.

If `D<1`, every integer gap lies in the decaying region and the same partial-summation estimate gives

`G(D) << D^2`.

So the transition is exactly at the local Fourier-resolution scale `d~x/H`.

## 3. Summing the near-diagonal blocks

On the block above,

`a_p a_(p+d) <= x^(-2alpha)`.

The absolute block contribution is therefore

`<<_(alpha,v) [x^beta/(log x)^2] G(x/H)`.

For `H<=x`, this is

`<<_(alpha,v) x^(beta+1)/(H (log x)^2)`,

whereas for `H>=x` it is

`<<_(alpha,v) x^(beta+2)/(H^2 (log x)^2)`.

If `1<=H<=y`, split the dyadic sum at `x~H`. The blocks with `x>H` are geometrically dominated by the top scale and contribute

`<<_(alpha,v) y^(beta+1)/(H (log y)^2)`.

The resolved blocks `x<=H` are no larger in aggregate after absorbing the finitely small initial scales. Since

`Q_y asymp_alpha y^beta/log y`,

the normalized near-pair envelope satisfies

`O_near <<_(alpha,v) y/(H log y)`.

If `H>=y`, every block is in the resolved regime, recovering the `VIS-189` estimate

`O_near <<_(alpha,v) y^2/(H^2 log y)`.

## 4. Far multiplicative pairs remain smaller

For `q>=3p/2`,

`log(q/p) >= log(3/2)`,

so the endpoint-zero kernel gives

`|K^v_(H,T)(p,q)| <<_v H^(-2)`.

Exactly as in `VIS-189`, the prime number theorem and partial summation yield

`O_far <<_(alpha,v) y/(H^2 log y)`.

For `1<=H<=y` this is bounded by the new near-pair scale `y/(H log y)`, and for `H>=y` it is smaller than `y^2/(H^2 log y)`. Combining the two regions proves the claim.

## 5. The method threshold is `y/log y`, not `y`

The strengthened estimate changes the closure boundary of the tapered quadratic channel. Linear observation length was sufficient in `VIS-189`, but it was not the real threshold supplied by the same audited ingredients. Absolute prime-pair control already forces diagonalization whenever

`H/(y/log y) -> infinity`.

At `H=c y/log y` with fixed `c>0`, the bound becomes only `O_v(1/c)`. Below that scale it ceases to imply smallness. This does **not** establish a surviving off-diagonal there: phase cancellation, stronger arithmetic information, or a more refined signed argument could still make the actual mean diagonal.

The obstruction is instead methodological and localizable. In a top block `x~y`, gaps

`d <= x/H`

are unresolved by the observation kernel, so only the trivial `O(1)` kernel bound applies. Their sieve envelope has total singular-series mass `O(x/H)`. Improving the Fourier tail beyond `1/z^2` cannot by itself remove this unresolved contribution: extra smoothness only suppresses `d>x/H`. Thus any attempt to beat the `y/log y` scale by the same absolute-envelope strategy must introduce additional arithmetic sparsity or cancellation inside the unresolved gap zone rather than merely a smoother fixed taper.

## 6. Prior-art and novelty boundary

This finding is a refinement of the Mathia-specific closure estimate in `VIS-189`, not a claim of a new Dirichlet-polynomial mean-value theorem. Smoothly weighted mean values, Fourier localization of smooth windows, Selberg upper-bound sieve estimates for prime pairs, and average singular-series bounds are classical machinery. `VIS-185`, `VIS-186`, `VIS-188`, and `VIS-189` already source-audit the exact ingredients used here, and `research/visual_exploration/SOURCES.md` records standard Dirichlet-polynomial mean-value references.

The only new content asserted here is the consequence of combining the trivial and decaying taper bounds before summing the already-audited prime-pair envelope: the sufficient observation scale improves from `H asymp y` to `H >> y/log y`, and the remaining absolute-method obstruction is isolated to the unresolved gaps `d<=x/H`.

## Boundaries and falsification

The exponent `alpha` and taper `v` are fixed as `y` grows; constants are not uniform as `alpha->1/2` or for taper families with growing norms. The statement concerns continuous averaging of the full-prefix quadratic prime polynomial and an absolute off-diagonal envelope. It says nothing by itself about hard windows, discrete sampling, higher moments, nonlinear observables, signed cancellation below the envelope, or RH.

Falsify the finding by locating an error in the combined kernel bound, the split of `G(D)` at `D=x/H`, the partial-summation consequence of `A(U)<<U`, the dyadic summation across `x~H`, the far-pair estimate, or the normalization `Q_y asymp y^beta/log y`.

## Research consequence

For this fixed smooth quadratic observable, `H~y` is no longer the interesting transition. The unresolved zone has been pushed down to observation lengths around `y/log y`. Above that scale, the full prime-pair off-diagonal vanishes even under absolute values; at and below it, any genuinely new quadratic phenomenon must come from arithmetic structure inside the kernel-unresolved short-gap population or from signed cancellation that the present sieve envelope deliberately discards.

This is a natural stopping boundary for the current invocation. Testing the critical `H~y/log y` regime with a signed argument, or changing to a higher-order/non-additive observable, is a separate research question.