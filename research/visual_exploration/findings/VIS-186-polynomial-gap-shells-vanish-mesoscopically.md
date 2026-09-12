# VIS-186 — every fixed polynomial prime-gap shell is negligible at the linear window scale

## Claim

Fix `0 <= alpha < 1/2` and write

`w_p = p^(-alpha)`,

`Q_y = sum_(p<=y) w_p^2`,

`beta = 1-2alpha > 0`.

For an averaging interval `[T,T+H]`, let

`K_(H,T)(p,q) = H^(-1) int_T^(T+H) exp(it log(p/q)) dt`.

For a gap scale `D`, define the dyadic-shell contribution

`R_shell(D;y,H,T)`
` = Q_y^(-1) | sum_(D<d<=2D) sum_(p<=y-d, p and p+d prime) w_p w_(p+d) K_(H,T)(p,p+d) |`.

For every fixed `epsilon>0`, fixed `alpha<1/2`, and `H>=c y` with fixed `c>0`, uniformly in `T` and uniformly for

`y^epsilon <= D <= y^(1-epsilon)`,

one has

`R_shell(D;y,H,T)`
` <<_(alpha,c,epsilon) (D/y)^(1+beta) (log y/log D) + 1/log y`.

Hence

`R_shell(D;y,H,T) -> 0`

uniformly throughout every fixed mesoscopic polynomial range. In particular, for every fixed `0<delta<1`, the shell `D=y^delta` is asymptotically negligible.

Together with `VIS-185`, this separates two facts that were previously conflated. A cumulative band `1<=d<=y^delta` is not proved negligible by the present absolute-value method, but **no individual multiplicative gap octave at scale `d asymp y^delta` can carry an order-one normalized contribution**. The order-one upper bound for a polynomial cumulative band can therefore arise only by accumulating contributions across `Theta(log y)` logarithmic gap scales, or from the genuinely macroscopic regime `d asymp y` not covered here.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL UNIFORM SELBERG-SIEVE INPUT + EXACT INTERVAL-KERNEL BOUND + NEGATIVE MULTISCALE CONTROL + NO-NOVELTY-CLAIM`.

No cancellation between different gap shells is assumed, and no nonzero polynomial-scale contribution is asserted.

## 1. The shell question is different from the cumulative-band question

`VIS-185` bounded the cumulative near-diagonal range `1<=d<=D` by

`R_D <<_alpha D y^(-beta/2) + (y/H) log(2D)/log y`.

At `H asymp y`, the high-prime term becomes `O(log D/log y)`. This vanishes for `D=y^(o(1))` but becomes only `O(delta)` for `D=y^delta`.

That does not show that a polynomial-scale shell survives. The logarithm came from summing the harmonic kernel weight `1/d` over **all** scales from `1` to `D`. On one dyadic shell `D<d<=2D`, the same singular-series average costs only a constant.

This finding isolates that scale-local statement.

## 2. Kernel decay

Direct integration gives, with `u=log(q/p)`,

`K_(H,T)(p,q) = exp(i(T+H/2)u) * 2 sin(Hu/2)/(Hu)`,

hence

`|K_(H,T)(p,q)| <= min(1, 2/(H|u|))`.

The estimate is independent of the interval start `T` after absolute values.

We split the shell contribution into `p<=8D` and `p>8D`.

## 3. The low-prime part is power-small for every sublinear polynomial shell

If `p<=8D` and `d>D`, then

`log((p+d)/p) = log(1+d/p) >= log(9/8)`.

Therefore

`|K_(H,T)(p,p+d)| << 1/H`.

Also `p+d>D`, so `(p+d)^(-alpha) <= D^(-alpha)`. Without using any prime-pair correlation estimate,

`M_low`
` <= H^(-1) sum_(p<=8D) p^(-alpha) sum_(D<d<=2D, p+d prime) (p+d)^(-alpha)`
` <= H^(-1) D^(1-alpha) sum_(p<=8D) p^(-alpha)`.

The standard prime-counting bound plus partial summation gives, for fixed `alpha<1`,

`sum_(p<=x) p^(-alpha) <<_alpha x^(1-alpha)/log x`.

Thus

`M_low <<_alpha D^(2-2alpha)/(H log D)`
` = D^(1+beta)/(H log D)`.

Since

`Q_y asymp_alpha y^beta/log y`,

the normalized low contribution satisfies

`M_low/Q_y`
` <<_alpha D^(1+beta) log y/(H y^beta log D)`.

When `H>=c y`, this is

`<<_(alpha,c) (D/y)^(1+beta) (log y/log D)`.

For `y^epsilon<=D<=y^(1-epsilon)`, it is power-small uniformly in `D`.

## 4. One high-prime gap octave costs only `O(1/log y)`

Now take `p>8D` and split the prime variable into dyadic blocks `x<p<=2x`. Then `x` is bounded below by a constant multiple of `D`, while `d<=2D<=x/2` after adjusting the first block by an absolute constant.

As in `VIS-185`, for `p in (x,2x]` and `q=p+d`,

`log(1+d/p) >= d/(p+d) >> d/x`,

so

`|K_(H,T)(p,p+d)| << x/(H d)`.

The same classical uniform Selberg upper-bound sieve used in `VIS-184` and `VIS-185` gives

`#{p in (x,2x] : p and p+d prime} << S(d) x/(log x)^2`,

where `S(d)` is the two-shift singular series, together with

`A(U)=sum_(d<=U) S(d) << U`.

Partial summation on a single dyadic gap shell yields

`sum_(D<d<=2D) S(d)/d << 1`.

Indeed, the endpoint terms are bounded by `A(t)/t=O(1)` and

`int_D^(2D) A(t)/t^2 dt << int_D^(2D) dt/t << 1`.

Since `w_p w_(p+d) << x^(-2alpha)`, the absolute contribution of one prime dyadic block is therefore

`<<_alpha x^(-2alpha) [x/(log x)^2] [x/H] sum_(D<d<=2D) S(d)/d`
`<<_alpha x^(1+beta)/(H (log x)^2)`.

Summing dyadically over `x` from a constant multiple of `D` to `y` is geometrically dominated by the top scale because `1+beta>0`. Under `D>=y^epsilon`, all relevant logarithms are comparable to `log y`, with constants depending on `epsilon`, so

`M_high <<_(alpha,epsilon) y^(1+beta)/(H (log y)^2)`.

After division by `Q_y`,

`M_high/Q_y <<_(alpha,epsilon) (y/H)/log y`.

For `H>=c y`, this is `O_(alpha,c,epsilon)(1/log y)`.

## 5. Multiscale consequence

Combining the two pieces proves

`R_shell(D;y,H,T)`
` <<_(alpha,c,epsilon) (D/y)^(1+beta) (log y/log D) + 1/log y`

throughout `y^epsilon<=D<=y^(1-epsilon)`.

Thus every fixed polynomial shell `d asymp y^delta`, `0<delta<1`, disappears after full-prefix normalization at the linear observation scale.

The distinction from `VIS-185` is structural. For a cumulative polynomial band `1<=d<=y^delta`, there are `Theta(log y)` dyadic gap octaves between constant and polynomial size. The high-prime estimate above assigns only `O(1/log y)` to each octave, so summing the absolute shell bounds over a positive fraction of those octaves gives merely an order-one bound. The unresolved possibility is therefore **distributed logarithmic-scale accumulation**, not concentration at one mesoscopic gap scale.

This gives a more precise picture of the remaining frontier: a putative full-prefix off-diagonal mechanism at `H asymp y` must either combine information coherently across a growing number of logarithmic gap scales, exploit cancellation/structure invisible to the current absolute-value bounds, or live at genuinely macroscopic separations `d comparable to y`.

## 6. Prior-art and novelty boundary

No new prime-pair theorem is used. The prime-pair sieve estimate and the average bound `sum_(d<=U)S(d)<<U` are exactly the classical inputs already audited and sourced in `VIS-184` and `VIS-185`, including the uniform Selberg-sieve formulation of Lichtman--Teräväinen and Gallagher's averaged singular-series framework.

The interval-kernel estimate is elementary Fourier analysis, and the passage from a cumulative harmonic sum `O(log D)` to a dyadic-shell harmonic sum `O(1)` is elementary partial summation.

The claim here is therefore a Mathia-specific negative multiscale control obtained by recombining already-audited classical ingredients. No novelty claim is made for the underlying sieve, singular-series, or mean-value estimates.

## 7. Boundaries and falsification

The exponent `alpha` is fixed below `1/2`; no uniformity as `alpha->1/2` is claimed. The critical case is controlled separately by the earlier quadratic null results.

The polynomial shell must remain mesoscopic: `D<=y^(1-epsilon)`. The argument intentionally does not treat `d comparable to y`, where the low/high decomposition and the interpretation of a local gap octave change.

The result is for full-prefix normalization and does not apply to sparse adversarial supports such as those isolated in `VIS-180`.

The high-prime argument uses absolute values inside each shell. It proves shellwise negligibility but does not prove cancellation between shells. Consequently it cannot be summed over `Theta(log y)` shells to conclude that the whole polynomial cumulative range is negligible.

Falsify the finding by locating an error in the constant-separation low-prime kernel bound, the weighted low-prime mass estimate, the uniform two-shift sieve range, the dyadic-shell singular-series estimate, the high-prime dyadic summation, or the normalization by `Q_y`.

## Research consequence

A surviving polynomial-gap contribution cannot be localized to any one fixed logarithmic gap scale below `d asymp y`. The remaining quadratic full-prefix problem is intrinsically multiscale: either many mesoscopic octaves accumulate coherently, a sharper cancellation theorem removes that accumulation, or the live contribution shifts to macroscopic prime separations.

The next coherent test should therefore analyze the **log-gap distribution of the full off-diagonal kernel** rather than widening another single local band. A useful positive signal would have to distinguish genuine arithmetic cross-scale coherence from the deterministic accumulation permitted by the present shellwise `O(1/log y)` envelope.
