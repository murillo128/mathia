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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The Wang analysis has separated two genuinely different source routes.

For the fixed-power real-axis source, `VIS-283`--`VIS-293` isolate the arithmetic channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. `VIS-330` prices the pure power subclass directly: if

`S(x)-log x = O(x^(-delta))`

for some fixed `delta>0`, then zeta has no nontrivial zero in

`Re(s)>max(1/2,1-delta)`.

Thus every true fixed power saving already buys a fixed zero-free half-plane, and `delta>=1/2` reaches the RH boundary.

`VIS-331` now identifies the exact direct-Mellin boundary between that expensive regime and the remaining subpower search space. If

`|S(e^t)-t| <= C exp(-phi(t))`

and

`a=liminf phi(t)/t`,

then the pointwise envelope alone makes the tail Mellin transform holomorphic on `Re(w)>-a` and therefore forces zero-freeness in `Re(s)>max(1/2,1-a)` when `a>0`. If `phi(t)=o(t)`, then `a=0`: the same pointwise comparison certifies no fixed open half-plane to the left of the original Mellin boundary. In particular, the Korobov--Vinogradov exponent

`V(t)=t^(3/5)(log t)^(-1/5)`

belongs to this zero-linear-rate class.

For the moving upper pointwise source, `VIS-315`--`VIS-320` reduce the natural-window problem to simultaneous-prime occupancy on at most three subperiod rational mechanical branches while preserving the full two-prime local sieve dimension. `VIS-322`--`VIS-328` progressively close center-gap regimes by diagonal, Christoffel, and short-vector decimations. `VIS-329` then removes the remaining transition and the need for the center-gap split itself: applying Minkowski decimation directly to the original period-`m=max(u,v)` rotation partitions every natural subperiod candidate branch into only `O(sqrt(M))` small-conductor affine pieces, giving the classical Selberg upper-bound scale

`P_j << L (log log M)^2/log^2 M`

uniformly in `k=|u-v|`.

Thus the moving-upper local-density channel now satisfies the `VIS-316` branchwise excess scale with

`A_M=O((log log M)^2)`

throughout the original subperiod regime. The previously live near-maximal transition `k<=L`, `k=M^(1-o(1))`, is no longer an occupancy obstruction.

## Research question

The remaining live question is now quantitative and source-specific:

Can one derive for the squared-von-Mangoldt source a real-axis envelope or secondary expansion

`S(e^t)-t = O(exp(-phi(t)))`

with **sublinear logarithmic rate** `phi(t)=o(t)` but a genuine improvement over the current Korobov--Vinogradov scale, together with enough uniformity on fixed source-exponent panels to improve Wang's complete source, gamma, localization, cross-term, and moving-upper error budget at the natural window?

A clean shape improvement would have `phi(t)` dominate the current `V(t)=t^(3/5)(log t)^(-1/5)` beyond a mere change of an unknown constant; a source-sensitive secondary term or cancellation law that yields a comparably decisive improvement is also admissible.

Alternatively, a candidate with positive lower linear rate `a>0` may still be useful, but then the fixed zero-free half-plane `Re(s)>max(1/2,1-a)` exposed by `VIS-331` is part of the hypothesis burden and must be proved or explicitly assumed rather than treated as free source cancellation.

The target is therefore not another generic PNT substitution. It is arithmetic information specific to the symmetric `Lambda^2` source that either improves the subpower exponent while keeping `a=0`, or pays explicitly for whatever positive linear rate it uses.

## Why it may matter

The moving-upper branch was the main place where frequency crowding could have manufactured an apparent localization obstruction. The exact Bezout/mechanical representation plus direct Minkowski decimation now shows that this local crowding can be controlled at a scale compatible with the taper-weighted destination. Continuing to refine center-gap or Christoffel subregimes would therefore attack a representation that is already sufficient for the required upper bound.

On the fixed-source side, `VIS-330` and `VIS-331` remove the remaining ambiguity about analytic cost. Fixed powers are expensive because they buy a fixed zero-free strip; genuinely subpower envelopes have zero lower linear rate, so the direct pointwise Mellin argument does not itself manufacture such a strip. That leaves a sharply defined corridor between the current Korobov--Vinogradov envelope and every positive linear logarithmic rate.

A positive result in this corridor would still need to survive the complete Wang bookkeeping, but it would no longer be dismissible merely as an RH-equivalent continuation assumption. A negative result showing that every quantitatively sufficient source gain must acquire positive lower linear rate would conversely close the remaining fixed-source route for a structural reason.

## Decisive test

State a concrete source-specific real-axis estimate or secondary expansion and write its logarithmic decay rate `phi(t)` explicitly. Compute

`a=liminf_(t->infinity) phi(t)/t`.

If `a=0`, prove that the candidate genuinely improves the current `VIS-291` Korobov--Vinogradov envelope rather than changing only a hidden constant, establish the uniformity needed for `x=T^beta` on a pre-fixed compact `beta` panel, and propagate the improvement through Wang's complete error decomposition at the natural window.

If `a>0`, use `VIS-331` as the pricing rule: the pointwise envelope forces zero-freeness in `Re(s)>max(1/2,1-a)`, with `a>=1/2` reaching RH. The argument must therefore supply or explicitly assume that analytic burden before the gain is credited.

Accept a new route only if it adds source-specific arithmetic information beyond the generic PNT input and materially improves the final Wang error scale. Kill it if the apparent gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption in disguise, a constant-level rewrite of the existing Korobov--Vinogradov bound, or a term already dominated by another Wang remainder.

Do not reopen branchwise center-gap occupancy without identifying a flaw in `VIS-329` or a destination quantity not controlled by the `VIS-316` excess criterion.

## Evidence boundary

`VIS-329` is an upper-bound occupancy closure, not a prime-pair asymptotic, lower bound, full Wang theorem, or stronger RH criterion. It shows that the previously isolated moving-upper local-density obstruction is compatible with the sufficient `VIS-316` scale in the natural subperiod regime; it does not by itself certify every global bookkeeping step outside that criterion.

`VIS-293` establishes the RH-equivalent half-plane boundary for the source transform. `VIS-330` prices pure power decay. `VIS-331` generalizes only the **direct pointwise-decay/fundamental-strip mechanism**: a lower linear logarithmic rate buys a fixed Mellin half-plane, while a sublinear rate does not certify one by that comparison alone. `VIS-331` does not rule out cancellation-based analytic continuation, does not prove that a stronger subpower estimate exists, and does not show that such an estimate would be large enough for Wang's final destination.

Those quantitative source-specific questions are precisely what remain open here.

## Research disposition

Outcome: **narrowed**.

The moving-upper simultaneous-prime occupancy branch is resolved at the required upper-bound scale by `VIS-329`. `VIS-330` prices fixed powers, and `VIS-331` identifies zero lower logarithmic rate as the analytically cheaper side of the direct Mellin boundary. The clue remains `accepted` only for the narrower source question above: improve the Korobov--Vinogradov-scale source envelope within that sublinear corridor and propagate the gain through the complete Wang budget, or pay explicitly for any positive linear rate used.