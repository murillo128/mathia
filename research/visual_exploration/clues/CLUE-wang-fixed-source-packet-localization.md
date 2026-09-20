---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-293-wang-source-dirichlet-rh-half-plane.md
  - research/visual_exploration/findings/VIS-316-wang-weighted-shell-occupancy-criterion.md
  - research/visual_exploration/findings/VIS-319-wang-bezout-strip-restores-prime-sieve-dimension.md
  - research/visual_exploration/findings/VIS-320-wang-bezout-strip-subperiod-rational-rotation.md
  - research/visual_exploration/findings/VIS-324-polynomial-run-length-selberg-sieve-regime.md
  - research/visual_exploration/findings/VIS-328-minkowski-decimation-closes-maximally-fragmented-wang-branches.md
  - research/visual_exploration/findings/VIS-329-direct-minkowski-decimation-closes-wang-transition.md
  - research/visual_exploration/findings/VIS-330-wang-real-axis-power-saving-zero-free-half-plane.md
  - research/visual_exploration/findings/VIS-331-wang-subpower-envelope-mellin-strip-boundary.md
  - research/visual_exploration/findings/VIS-332-wang-regular-variation-secondary-transfer.md
  - research/visual_exploration/findings/VIS-333-wang-summatory-log-frequency-transfer.md
  - research/visual_exploration/findings/VIS-334-wang-summatory-pointwise-inverse-derivative-tax.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The Wang analysis has separated two genuinely different source routes.

For the fixed-power real-axis source, `VIS-283`--`VIS-293` isolate the arithmetic channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. `VIS-330` prices the pure power subclass directly: if

`S(x)-log x = O(x^(-delta))`

for some fixed `delta>0`, then zeta has no nontrivial zero in

`Re(s)>max(1/2,1-delta)`.

Thus every true fixed power saving already buys a fixed zero-free half-plane, and `delta>=1/2` reaches the RH boundary.

`VIS-331` identifies the exact direct-Mellin boundary between that expensive regime and the remaining subpower search space. If

`|S(e^t)-t| <= C exp(-phi(t))`

and

`a=liminf phi(t)/t`,

then the pointwise envelope alone makes the tail Mellin transform holomorphic on `Re(w)>-a` and therefore forces zero-freeness in `Re(s)>max(1/2,1-a)` when `a>0`. If `phi(t)=o(t)`, then `a=0`: the same pointwise comparison certifies no fixed open half-plane to the left of the original Mellin boundary. In particular, the Korobov--Vinogradov exponent

`V(t)=t^(3/5)(log t)^(-1/5)`

belongs to this zero-linear-rate class.

`VIS-332` removes one false mechanism inside that subpower corridor. If the summatory squared-von-Mangoldt source has a coherent regularly varying secondary term

`A(x)=x log x-x+c x^alpha L(x)(1+o(1))`,

then Wang's symmetric two-tail smoothing transfers it with multiplier

`m(alpha)=4 alpha/[(alpha+1)(3-alpha)]`

for `-1<alpha<3`, `alpha!=0`. At the PNT-relevant index `alpha=1`, the multiplier is exactly one. Hence a coherent secondary term of the form `c x L(x)` passes through to `S(x)-log x` at the same scale and with the same leading coefficient.

`VIS-333` gives the complementary exact log-frequency control. For the normalized summatory remainder

`F(u)=e^(-u)E_A(e^u)`

the adjusted Wang remainder is the output of a fixed convolution whose real-frequency multiplier is

`4(1+i xi)/(4+xi^2)`.

It has no zero for real `xi`, equals one at `xi=0`, and decays only like `4/|xi|` at high frequency. Therefore neither a fixed coherent log-frequency nor any fixed bounded frequency band can be selectively erased by Wang's transform. Any transform-induced norm gain requires source energy to migrate to unbounded log-frequency; a pointwise improvement still requires additional arithmetic control beyond that spectral observation.

`VIS-334` now converts that spectral boundary into an exact pointwise inverse. If

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`,

then

`F(u)`
` = [Q(u)-Q'(u)]/4`
`   + [Q(0)e^(-u)]/4`
`   + (3/4) integral_0^u e^(-(u-v))Q(v)dv`.

Thus for any ordinary smooth sublinear envelope `e^(-phi(u))` with eventually `0<=phi'(u)<=eta<1`, simultaneous bounds

`Q(u), Q'(u) = O(e^(-phi(u)))`

force

`F(u)=O(e^(-phi(u)))`.

A smooth pointwise gain cannot therefore be credited to Wang smoothing alone when its first log-derivative is equally small. The remaining transform-specific escape is genuinely nonstationary/high-frequency behavior in which `Q` is smaller while `Q'` carries the missing scale.

For the moving upper pointwise source, `VIS-315`--`VIS-320` reduce the natural-window problem to simultaneous-prime occupancy on at most three subperiod rational mechanical branches while preserving the full two-prime local sieve dimension. `VIS-322`--`VIS-328` progressively close center-gap regimes by diagonal, Christoffel, and short-vector decimations. `VIS-329` then removes the remaining transition and the need for the center-gap split itself: applying Minkowski decimation directly to the original period-`m=max(u,v)` rotation partitions every natural subperiod candidate branch into only `O(sqrt(M))` small-conductor affine pieces, giving the classical Selberg upper-bound scale

`P_j << L (log log M)^2/log^2 M`

uniformly in `k=|u-v|`.

Thus the moving-upper local-density channel now satisfies the `VIS-316` branchwise excess scale with

`A_M=O((log log M)^2)`

throughout the original subperiod regime. The previously live near-maximal transition `k<=L`, `k=M^(1-o(1))`, is no longer an occupancy obstruction.

## Research question

The remaining live question is now a signed, nonstationary cancellation problem in the fixed source.

Can one prove, for the actual squared-von-Mangoldt summatory remainder

`E_A(x)=sum_(n<=x) Lambda(n)^2-(x log x-x)`,

cancellation in the exact Wang transform

`S(x)-log x`
` = -x^(-2) integral_1^x E_A(t)dt`
`   +3x^2 integral_x^infinity E_A(t)t^(-4)dt`
`   -3/(4x^2)`

that yields a real-axis envelope or secondary expansion

`S(e^t)-t = O(exp(-phi(t)))`

with **sublinear logarithmic rate** `phi(t)=o(t)` and a genuine improvement over the current Korobov--Vinogradov scale?

A clean shape improvement would have `phi(t)` dominate the current `V(t)=t^(3/5)(log t)^(-1/5)` beyond a mere change of an unknown constant. `VIS-332` rules out crediting the gain to attenuation of a coherent regularly varying PNT-scale term; `VIS-333` rules out a fixed real log-frequency or fixed bounded log-frequency band as a hidden null; and `VIS-334` rules out a smooth transform-only pointwise gain when both `Q` and `Q'` obey that improved envelope.

The surviving transform-specific route must therefore quantify source-specific high-frequency or nonstationary structure for which `Q` is genuinely smaller while the derivative carries the missing scale, and then show that Wang's complete downstream error budget can exploit the smaller `Q` without reintroducing the derivative cost. A direct stronger bound for `F=E_A(e^u)e^(-u)` is also valid, but that is new source arithmetic rather than free smoothing.

Alternatively, a candidate with positive lower linear rate `a>0` may still be useful, but then the fixed zero-free half-plane `Re(s)>max(1/2,1-a)` exposed by `VIS-331` is part of the hypothesis burden and must be proved or explicitly assumed rather than treated as free source cancellation.

## Why it may matter

The moving-upper branch was the main place where frequency crowding could have manufactured an apparent localization obstruction. The exact Bezout/mechanical representation plus direct Minkowski decimation now shows that this local crowding can be controlled at a scale compatible with the taper-weighted destination. Continuing to refine center-gap or Christoffel subregimes would therefore attack a representation that is already sufficient for the required upper bound.

On the fixed-source side, `VIS-330` and `VIS-331` price the analytic cost of fixed-power and positive-linear-rate decay. `VIS-332` shows that coherent regularly varying source scales survive the smoothing, `VIS-333` shows that the exact summatory-remainder transfer has no real log-frequency blind mode and only first-order high-frequency attenuation, and `VIS-334` shows that the same transfer has a causal pointwise inverse consisting of one derivative plus exponentially weighted memory.

That focuses the remaining opportunity on genuine arithmetic organization of the actual `Lambda^2` remainder rather than on a generic smoothing effect. A positive result now needs to explain not only why `Q` is small, but where the inverse derivative tax goes and why the final Wang statistic does not pay it back. A negative result showing that every admissible arithmetic mechanism necessarily repays that derivative cost would close the remaining fixed-source route for a structural reason.

## Decisive test

Start from the exact signed transform above rather than from an absolute envelope for `E_A`. State the source-specific cancellation mechanism and derive its resulting logarithmic decay rate `phi(t)` explicitly. Compute

`a=liminf_(t->infinity) phi(t)/t`.

If `a=0`, prove that the candidate genuinely improves the current `VIS-291` Korobov--Vinogradov envelope rather than changing only a hidden constant, establish the uniformity needed for `x=T^beta` on a pre-fixed compact `beta` panel, and propagate the improvement through Wang's complete error decomposition at the natural window.

Use `VIS-332`--`VIS-334` as matched structural controls. A mechanism whose effective source model is only a coherent regularly varying term `c x^alpha L(x)`, a fixed logarithmic oscillation, or a fixed bounded band of logarithmic frequencies does not obtain a new asymptotic scale from Wang smoothing alone. Moreover, if a smooth candidate envelope also bounds `Q'`, `VIS-334` transfers that envelope back to the source. A viable transform-specific mechanism must therefore quantify the derivative/high-frequency asymmetry and convert the smaller `Q` into the required final pointwise gain without assuming the desired source estimate.

If `a>0`, use `VIS-331` as the pricing rule: the pointwise envelope forces zero-freeness in `Re(s)>max(1/2,1-a)`, with `a>=1/2` reaching RH. The argument must therefore supply or explicitly assume that analytic burden before the gain is credited.

Accept a new route only if it adds source-specific arithmetic information beyond the generic PNT input and materially improves the final Wang error scale. Kill it if the apparent gain is only a generic PNT substitution, smoothing attenuation, a coherent regularly varying secondary term, a fixed-frequency filter effect, a smooth `Q,Q'` envelope that simply transfers back to `F`, an RH-equivalent continuation assumption in disguise, a constant-level rewrite of the existing Korobov--Vinogradov bound, or a term already dominated by another Wang remainder.

Do not reopen branchwise center-gap occupancy without identifying a flaw in `VIS-329` or a destination quantity not controlled by the `VIS-316` excess criterion.

## Evidence boundary

`VIS-329` is an upper-bound occupancy closure, not a prime-pair asymptotic, lower bound, full Wang theorem, or stronger RH criterion. It shows that the previously isolated moving-upper local-density obstruction is compatible with the sufficient `VIS-316` scale in the natural subperiod regime; it does not by itself certify every global bookkeeping step outside that criterion.

`VIS-293` establishes the RH-equivalent half-plane boundary for the source transform. `VIS-330` prices pure power decay. `VIS-331` generalizes only the direct pointwise-decay/fundamental-strip mechanism: a lower linear logarithmic rate buys a fixed Mellin half-plane, while a sublinear rate does not certify one by that comparison alone.

`VIS-332` is a regular-variation transfer theorem, not a theorem about the sign or exact asymptotic form of the actual squared-von-Mangoldt remainder. `VIS-333` is an exact Fourier/resolvent control on the normalized summatory-remainder transform; it does not prove high-frequency concentration, cross-mode cancellation, or a sharper pointwise source estimate for the actual remainder. `VIS-334` is an exact inverse and conditional envelope-transfer statement; crucially, it does **not** derive a `Q'` bound from a `Q` bound, so the high-frequency/nonstationary escape remains live. The current Korobov--Vinogradov input remains only an upper envelope.

Those source-specific quantitative questions are precisely what remain open here.

## Research disposition

Outcome: **narrowed**.

The moving-upper simultaneous-prime occupancy branch is resolved at the required upper-bound scale by `VIS-329`. `VIS-330` prices fixed powers, `VIS-331` identifies zero lower logarithmic rate as the analytically cheaper side of the direct Mellin boundary, `VIS-332` shows that coherent regularly varying secondary scales survive Wang smoothing, `VIS-333` removes fixed real log-frequency nulls, and `VIS-334` shows that a smooth pointwise gain in both `Q` and `Q'` transfers back to the source. The clue remains `accepted` only for the narrower question above: prove genuinely source-specific nonstationary/high-frequency cancellation whose derivative cost does not destroy the complete Wang gain, or prove a genuinely stronger source remainder directly, while paying explicitly for any positive linear rate used.
