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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The Wang analysis has separated two genuinely different source routes.

For the fixed-power real-axis source, `VIS-283`--`VIS-293` isolate the arithmetic channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. `VIS-330` now prices an important real-axis subclass directly: if

`S(x)-log x = O(x^(-delta))`

for some fixed `delta>0`, then zeta has no nontrivial zero in

`Re(s)>max(1/2,1-delta)`.

Thus every true fixed power saving already buys a fixed zero-free half-plane, and `delta>=1/2` reaches the RH boundary. A power remainder is therefore not an uncosted source-specific strengthening of the current Korobov--Vinogradov envelope.

For the moving upper pointwise source, `VIS-315`--`VIS-320` reduce the natural-window problem to simultaneous-prime occupancy on at most three subperiod rational mechanical branches while preserving the full two-prime local sieve dimension. `VIS-322`--`VIS-328` progressively close center-gap regimes by diagonal, Christoffel, and short-vector decimations. `VIS-329` then removes the remaining transition and the need for the center-gap split itself: applying Minkowski decimation directly to the original period-`m=max(u,v)` rotation partitions every natural subperiod candidate branch into only `O(sqrt(M))` small-conductor affine pieces, giving the classical Selberg upper-bound scale

`P_j << L (log log M)^2/log^2 M`

uniformly in `k=|u-v|`.

Thus the moving-upper local-density channel now satisfies the `VIS-316` branchwise excess scale with

`A_M=O((log log M)^2)`

throughout the original subperiod regime. The previously live near-maximal transition `k<=L`, `k=M^(1-o(1))`, is no longer an occupancy obstruction.

## Research question

The remaining live question in this clue is the fixed-power source route, now narrowed by `VIS-330`:

Is there a **subpower** real-axis property of

`mu=sum Lambda(n)^2/n delta_(log n)`

that improves the current Korobov--Vinogradov-scale source envelope enough to survive Wang's complete source, gamma, localization, cross-term, and moving-upper error budget without already asserting a fixed Mellin half-plane?

Alternatively, can one prove a fixed-power gain together with the corresponding fixed zero-free half-plane that `VIS-330` shows it entails, and does any exponent below the RH threshold `delta<1/2` remain quantitatively useful at the natural Wang window?

The target is a source-sensitive secondary expansion, cancellation statement, or representation whose analytic cost is explicit and whose gain is not merely a repackaged generic PNT bound or an RH-equivalent continuation assumption.

## Why it may matter

The moving-upper branch was the main place where frequency crowding could have manufactured an apparent localization obstruction. The exact Bezout/mechanical representation plus direct Minkowski decimation now shows that this local crowding can be controlled at a scale compatible with the taper-weighted destination. Continuing to refine center-gap or Christoffel subregimes would therefore attack a representation that is already sufficient for the required upper bound.

`VIS-330` similarly removes another vague escape: a polynomial real-axis remainder cannot be described as merely "weaker than RH" without pricing the zero-free half-plane it forces. The genuinely cheaper search space is now the gap between the current Korobov--Vinogradov envelope and fixed-power decay, plus any explicitly justified fixed zero-free strip below the RH threshold. A positive result there would still need to add arithmetic information and survive the complete Wang bookkeeping; a negative result could show that every quantitatively sufficient gain already crosses a zero-free-region threshold too strong to be useful as an independent route.

## Decisive test

State a concrete real-axis estimate or secondary expansion for the fixed-power source term, identify the exact arithmetic hypothesis that implies it, and propagate the gain through Wang's complete error decomposition at the natural window.

The candidate must also state the analytic burden implied by its real-axis scale. For a power remainder `O(x^(-delta))`, use `VIS-330` as the pricing rule: it forces zero-freeness in `Re(s)>max(1/2,1-delta)`, and `delta>=1/2` reaches RH. For subpower gains, determine what continuation or zero-free information actually follows rather than assuming the gain is analytically cheap.

Accept a new route only if its hypothesis is demonstrably weaker than the RH-equivalent pole exclusion of `VIS-293`, or if any fixed zero-free strip it requires is stated and proved explicitly, and the resulting gain survives all other source, gamma, localization, cross-term, and moving-upper contributions. Kill the route if the proposed improvement is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption in disguise, or a term already dominated by another Wang remainder.

Do not reopen branchwise center-gap occupancy without identifying a flaw in `VIS-329` or a destination quantity not controlled by the `VIS-316` excess criterion.

## Evidence boundary

`VIS-329` is an upper-bound occupancy closure, not a prime-pair asymptotic, lower bound, full Wang theorem, or stronger RH criterion. It shows that the previously isolated moving-upper local-density obstruction is compatible with the sufficient `VIS-316` scale in the natural subperiod regime; it does not by itself certify every global bookkeeping step outside that criterion.

`VIS-293` establishes the RH-equivalent half-plane boundary for the source transform. `VIS-330` adds only a **one-way** Mellin implication from fixed-power real-axis decay to a zero-free half-plane. It does not prove the converse, does not rule out useful stretched-exponential/logarithmic/subpower improvements, and does not by itself show that any such weaker gain is large enough for Wang's final destination. Those possibilities are precisely what remain open here.

## Research disposition

Outcome: **narrowed**.

The moving-upper simultaneous-prime occupancy branch is resolved at the required upper-bound scale by `VIS-329`; its former center-gap transition is no longer a live research target. `VIS-330` also prices the entire fixed-power real-axis subclass by the zero-free half-plane it forces. The clue remains `accepted` only for the narrower source question above: subpower improvement or explicitly priced fixed zero-free-strip gain that survives the complete Wang budget.