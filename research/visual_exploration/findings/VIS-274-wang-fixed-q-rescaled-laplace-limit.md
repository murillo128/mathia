# VIS-274 — fixed-`q` Wang probes have a rescaled Laplace limit

## Claim

Let `L=log T`, `H=T^theta`, and fix `0<lambda<theta<1`. Let

`h in C_c^infinity((0,infinity))`

be real, with compact support contained in a fixed interval `[q_-,q_+]` with `0<q_-<q_+`. Define the real even `T`-dependent Wang test

`g_T(alpha)=h(L|alpha|/(2*pi)).`

For all sufficiently large `T`, `supp(g_T) subset [-lambda,lambda]`. If `W_I(g_T)` denotes Wang's weighted short-interval pair statistic in the notation of `VIS-266`, then Wang's proof-level estimate implies the sharper rescaled asymptotic

`(2*pi/(H L)) W_I(g_T)`
` = 4*pi integral_0^infinity h(q) exp(-4*pi q) dq`
`   + (8*pi^2/L^2) integral_0^infinity q h(q) dq`
`   + O_(h,lambda,theta)(1/L).`

In particular,

`(2*pi/(H L)) W_I(g_T)`
` -> 4*pi integral_0^infinity h(q) exp(-4*pi q) dq.`

Thus a fixed-width probe in the logarithmic source coordinate `q=alpha L/(2*pi)` **is theorem-accessible at leading order**. The apparent order-one obstruction in the withdrawn `VIS-273` came from replacing Wang's concentrated exponential main term by its fixed-test approximation `g_T(0)` via the estimate

`|g_T(alpha)-g_T(0)| <= ||g_T'||_infinity alpha`.

At the fixed-`q` scale that Taylor reduction is not uniform: `||g_T'||_infinity=Theta(L)` because the test deliberately resolves the same `alpha=Theta(1/L)` layer on which `exp(-2L|alpha|)` varies. Keeping that main term intact and changing variables to `q` turns the supposed derivative loss into the explicit Laplace functional above, while the remaining proof error is only `O(1/L)` after normalization.

Consequently, if the fixed source profile is chosen to satisfy the exact null condition

`integral_0^infinity h(q) exp(-4*pi q) dq = 0`,

then Wang's present proof already gives

`(2*pi/(H L)) W_I(g_T)=O_(h,lambda,theta)(1/L).`

It does **not** identify the coefficient at that `1/L` scale. This leaves the Rodgers/Wang arithmetic-transfer question alive, but at a sharper boundary: first cancel the universal fixed-`q` Laplace mode, then any arithmetic coefficient must be resolved beneath the surviving normalized `O(1/L)` remainder.

**Evidence/status:** `LITERATURE+DERIVED + EXACT RESCALING + CORRECTION OF WITHDRAWN FINDING + FIXED-SOURCE LEADING LIMIT + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, `1/L` secondary coefficient, prime-power asymptotic transfer, or RH implication is claimed.

## 1. Keep Wang's concentrated main term instead of Taylor-expanding it

`VIS-266` extracted from the proof of Biao Wang's Theorem 2.2 the uniform estimate, for `0<=alpha<=lambda`,

`F_I(T^alpha)`
` = (H/(2*pi)) [L^2 exp(-2L alpha) + L alpha]`
`   + O_(lambda,theta)(H + H L exp(-2L alpha)`
`       + H sqrt(L) exp(-L alpha) + L^3 exp(L alpha)`
`       + L exp(-L alpha/2)).`

For an even test supported in `[-lambda,lambda]`, Fourier inversion gives

`W_I(g)=2 integral_0^lambda g(alpha) F_I(T^alpha) d alpha.`

For fixed tests, Wang reduces the concentrated exponential contribution to `L g(0)` plus an error controlled by `||g'||_infinity`. That is appropriate when `g` varies only on an `alpha` scale much larger than `1/L`.

The present family intentionally lives on the critical layer

`alpha = 2*pi q/L`.

Its support is bounded away from `alpha=0` by `2*pi q_-/L`, so `g_T(0)=0`, while the exponential spike is still order one across the rescaled support. It must therefore be integrated exactly rather than replaced by a point evaluation at zero.

## 2. Exact rescaling of the two displayed main terms

On the positive half-line write

`q=L alpha/(2*pi)`, `d alpha=(2*pi/L)dq`.

The concentrated exponential term contributes

`2 integral_0^lambda h(L alpha/(2*pi))`
`  * (H L^2/(2*pi)) exp(-2L alpha) d alpha`
` = 2 H L integral_0^infinity h(q) exp(-4*pi q)dq.`

After multiplication by `2*pi/(H L)`, this is exactly

`4*pi integral_0^infinity h(q) exp(-4*pi q)dq.`

The cusp term contributes

`2 integral_0^lambda h(L alpha/(2*pi))`
`  * (H L/(2*pi)) alpha d alpha`
` = (4*pi H/L) integral_0^infinity q h(q)dq,`

and hence, after the same normalization,

`(8*pi^2/L^2) integral_0^infinity q h(q)dq.`

So the ordinary Montgomery cusp is two powers of `L` smaller in this fixed-source scaling. The dominant object is instead the one-sided exponential/Laplace kernel inherited from Wang's concentrated diagonal term.

## 3. The remaining proof error is `O(1/L)`, not `O(1)`

Because `h` has fixed compact `q` support, all exponentials in the proof error become bounded fixed functions after the same substitution. Integrating over an `alpha` interval of width `Theta(1/L)` gives the following normalized contributions.

The bare `O(H)` term contributes `O_h(L^-2)`. The term

`O(H L exp(-2L alpha))`

contributes `O_h(L^-1)`, which is the dominant surviving error. The term

`O(H sqrt(L) exp(-L alpha))`

contributes `O_h(L^-3/2)`. The term

`O(L^3 exp(L alpha))`

contributes `O_h(L/H)`, because `exp(L alpha)=exp(2*pi q)` stays bounded on the fixed support. Finally,

`O(L exp(-L alpha/2))`

contributes `O_h((H L)^-1)` after normalization.

Thus

`(2*pi/(H L)) W_I(g_T)`
` = 4*pi <h,exp(-4*pi q)>`
`   + (8*pi^2/L^2) <h,q>`
`   + O_(h,lambda,theta)(L^-1 + L^-3/2 + L/H + L^-2),`

which proves the claim.

The `O(1/L)` term is a proof-level upper bound. This finding does not assert that it is sharp or that it contains a stable scalar secondary coefficient.

## 4. Why the derivative-budget diagnosis was too coarse

The withdrawn `VIS-273` inserted this same family into the generic moving-test estimate from `VIS-266`,

`Err_T(g_T)=O(||g_T'||_infinity/L + ...)`.

Since `||g_T'||_infinity=Theta(L)`, that bound is only `O(1)`. The calculation itself was correct, but the interpretation was not: the `||g'||/L` term in `VIS-266` was produced when Wang replaced

`2 L^2 integral_0^infinity g(alpha) exp(-2L alpha)d alpha`

by `L g(0)` and bounded the difference by a first-derivative seminorm.

For a family designed to resolve the `1/L` layer, that replacement discards an order-one structured main term. The derivative bound is therefore a **Taylor-remainder bound for the wrong limiting representation**, not evidence that the underlying fixed-`q` observable itself has order-one uncontrolled error.

This is why `VIS-273` is withdrawn rather than weakened in place. Its stable claim identity was that fixed-source localization exhausts the present theorem budget. The exact rescaling above shows instead that Wang's proof controls that localization, but with a different leading functional.

## 5. Relation to the Wang--Rodgers Green dictionary

`VIS-272` put Wang's explicit-formula coefficient field into the same fixed source coordinate,

`q=log x/(2*pi)`,

and showed that its diagonal-energy field is an exponential Green potential of the weighted Rodgers prime-power measure. The present result concerns a different but compatible layer of Wang's pair-correlation proof: after `x=T^alpha`, keeping `q=alpha L/(2*pi)` fixed exposes the universal profile

`exp(-4*pi q)`

inside the zero-pair statistic itself.

This profile should not be confused with recovery of the full prime-power field `A(q)` from `VIS-272`. The leading fixed-`q` limit above is universal and centered at the source boundary `q=0`; no fixed-prime atom has been extracted.

Its value is as a sharper control. A signed source packet can be chosen with

`<h,exp(-4*pi q)>=0`

while still overlapping any desired positive source window. Such a packet removes the complete leading fixed-`q` mode without invoking the nonuniform `g_T(0)` approximation. What remains is certified only to normalized size `O(1/L)`, precisely the scale at which a lower-order arithmetic transfer would have to be exhibited by a stronger expansion.

## 6. Prior-art and novelty boundary

The external analytic input is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), especially Theorem 2.2 and the proof-level uniform estimate already audited in `VIS-266`. The current arXiv record still lists only `v1`, submitted 7 September 2026, so no later source revision changes that audit at the time of this finding.

The present result is a direct change of variables in Wang's displayed proof estimate. Laplace rescaling of a concentrated exponential kernel is elementary, and no novelty is claimed for the limiting transform, for approximate-identity analysis, or for the principle that a moving test can resolve a boundary layer that a fixed-test Taylor expansion collapses.

The durable Mathia contribution is corrective: it identifies the correct asymptotic representation for the specific fixed-source scaling created by the `VIS-271`--`VIS-272` dictionary and removes a false theorem-interface obstruction introduced by applying the generic seminorm corollary outside the representation in which it is informative.

## Boundaries and falsification

The support of `h` is fixed and bounded away from `q=0`. This makes `g_T` smooth at `alpha=0` and keeps its support inside every fixed Wang margin for sufficiently large `T`. A source profile touching `q=0` needs a separate smoothness/accounting statement and is not covered by this formulation.

The result uses the proof-level estimate in `VIS-266`; if that audit is corrected, the error terms here must be recomputed. It also does not control a `q` window whose width or center grows with `T`.

Most importantly, annihilating the leading Laplace functional does not prove that the residual `O(1/L)` is arithmetic, nonzero, or related to Rodgers. A successful transfer still needs an explicit secondary term or a remainder `o(1/L)` for the chosen Laplace-null packet.

No untouched confirmation-zero data are used.

## Research consequence

The fixed-source branch should no longer spend effort trying to beat an order-one first-derivative barrier. That barrier arose from collapsing the very boundary layer the source coordinate was meant to resolve.

The coherent next theorem question is now narrower: for a fixed smooth `q`-packet satisfying

`integral h(q) exp(-4*pi q)dq=0`,

can Wang's short-interval explicit-formula analysis be sharpened from the present normalized `O(1/L)` control to an explicit `1/L` term, or to `o(1/L)`, in a way that preserves the prime-power Green field of `VIS-272`? Until that is shown, the Laplace-null packet is a calibrated access coordinate, not evidence of a Rodgers coefficient in short-interval pair correlation.