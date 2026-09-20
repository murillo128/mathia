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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The Wang analysis has separated two genuinely different source routes.

For the fixed-power real-axis source, `VIS-283`--`VIS-293` isolate the arithmetic channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. That branch still needs a concrete source property strictly weaker than the RH-equivalent half-plane statement if it is to improve the generic Korobov--Vinogradov envelope in a way that survives the complete Wang error budget.

For the moving upper pointwise source, `VIS-315`--`VIS-320` reduce the natural-window problem to simultaneous-prime occupancy on at most three subperiod rational mechanical branches while preserving the full two-prime local sieve dimension. `VIS-322`--`VIS-328` progressively close center-gap regimes by diagonal, Christoffel, and short-vector decimations. `VIS-329` then removes the remaining transition and the need for the center-gap split itself: applying Minkowski decimation directly to the original period-`m=max(u,v)` rotation partitions every natural subperiod candidate branch into only `O(sqrt(M))` small-conductor affine pieces, giving the classical Selberg upper-bound scale

`P_j << L (log log M)^2/log^2 M`

uniformly in `k=|u-v|`.

Thus the moving-upper local-density channel now satisfies the `VIS-316` branchwise excess scale with

`A_M=O((log log M)^2)`

throughout the original subperiod regime. The previously live near-maximal transition `k<=L`, `k=M^(1-o(1))`, is no longer an occupancy obstruction.

## Research question

The remaining live question in this clue is the fixed-power source route:

Is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion isolated in `VIS-293` that improves the real-axis source envelope enough to survive Wang's complete source, gamma, localization, cross-term, and moving-upper error budget?

Equivalently, can one identify a source-sensitive secondary expansion, cancellation statement, or representation that is both genuinely weaker than RH and quantitatively relevant at the natural Wang window, rather than merely repackaging a generic PNT bound or an RH-equivalent continuation assumption?

## Why it may matter

The moving-upper branch was the main place where frequency crowding could have manufactured an apparent localization obstruction. The exact Bezout/mechanical representation plus direct Minkowski decimation now shows that this local crowding can be controlled at a scale compatible with the taper-weighted destination. Continuing to refine center-gap or Christoffel subregimes would therefore attack a representation that is already sufficient for the required upper bound.

That leaves the fixed-power source as the genuinely source-sensitive unresolved route inside this clue. A positive result there would have to add arithmetic information not already supplied by generic prime-number-theorem technology while remaining weaker than the RH-equivalent analytic continuation boundary. A negative result could instead show that every quantitatively sufficient source improvement in this framework necessarily crosses an RH-equivalent threshold.

## Decisive test

State a concrete real-axis estimate or secondary expansion for the fixed-power source term, identify the exact arithmetic hypothesis that implies it, and propagate the gain through Wang's complete error decomposition at the natural window.

Accept a new route only if the hypothesis is demonstrably weaker than the pole exclusion of `VIS-293` and the resulting gain survives all other source, gamma, localization, cross-term, and moving-upper contributions. Kill the route if the proposed improvement is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption in disguise, or a term already dominated by another Wang remainder.

Do not reopen branchwise center-gap occupancy without identifying a flaw in `VIS-329` or a destination quantity not controlled by the `VIS-316` excess criterion.

## Evidence boundary

`VIS-329` is an upper-bound occupancy closure, not a prime-pair asymptotic, lower bound, full Wang theorem, or stronger RH criterion. It shows that the previously isolated moving-upper local-density obstruction is compatible with the sufficient `VIS-316` scale in the natural subperiod regime; it does not by itself certify every global bookkeeping step outside that criterion.

`VIS-293` establishes the RH-equivalent half-plane boundary for the fixed-power source but does not prove that no weaker real-axis statement can be quantitatively useful. That possibility is precisely what remains open here.

## Research disposition

Outcome: **narrowed**.

The moving-upper simultaneous-prime occupancy branch is resolved at the required upper-bound scale by `VIS-329`; its former center-gap transition is no longer a live research target. The clue remains `accepted` only for the distinct fixed-power real-axis source question above.
