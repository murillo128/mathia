---
id: CLUE-mobius-cancellation-farey-selected-sliding-mertens-variance
type: research-clue
status: proposed
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/farey_discrepancy/findings/FD-311-a-quarter-power-sliding-variance-saving-would-close-balanced-capacity.md
  - research/farey_discrepancy/findings/FD-312-pointwise-mertens-envelopes-cannot-close-sliding-variance-below-source-ceiling.md
  - research/mobius_cancellation/findings/MC-176-gallagher-critical-shell-good-churchhouse-variance.md
  - research/mobius_cancellation/findings/MC-177-gallagher-diagonal-energy-direct-mertens-power.md
---

# Can Möbius source control cross the Farey-selected sliding-variance threshold?

## Observation

FD-311 turns the balanced near-capacity Farey branch into a concrete short-interval Möbius second-moment target. For

`J_mu(X,N)=sum_(X<=y<2X) |M(y+N)-M(y)|^2`,

the near-capacity premise forces

`J_mu(X,N) >= X N^(1.7451124978-o(1))`

at balanced depth. Consequently any uniform source-window estimate

`J_mu(X,N) <= X N^(2-eta+o(1))`

with strict `eta>0.2548875021...` rules out that branch. Under the RH shell localization used only to identify the aspect ratio, the selected windows satisfy `N=X^(beta+o(1))` with `1/2<=beta<=0.5464256934...`.

MC-176 isolates Good--Churchhouse-order variance near the square-root scale as a critical shell for a Gallagher route, and MC-177 prices a uniform fixed-power variance improvement through its global Mertens consequences. Those results make this an identifiable Möbius research question, but they do not supply the FD-311 estimate.

FD-312 rules out a tempting way to obtain it: first bounding `M(y+N)` and `M(y)` separately by a global pointwise envelope. In the RH-localized balanced band, the most favorable comparison would require a global Mertens exponent below `0.4767871533...`, hence below the critical-line barrier `1/2`. Even an RH-quality endpoint envelope gives at best `eta=0.1699250014...`, leaving a fixed-power deficit `0.0849625007...`. The live object is therefore cancellation in the difference or its sliding mean square, not stronger separate bounds for the two endpoints.

## Research question

Can the actual Möbius source yield a fixed-power upper bound for the exact Farey-selected sliding moment that crosses the strict FD-311 threshold, without assuming an RH-equivalent Mertens estimate, discarding the selected-window condition, or estimating the two endpoints separately?

A positive route could use signed block correlations, a variance identity, a source-compatible conductor decomposition, or additional geometry of the selected window. A negative route should identify a source-faithful obstruction showing why the present Möbius inputs still permit variance at or above the required threshold.

## Why it may matter

Crossing the threshold closes the balanced near-capacity branch in the scope of the Farey reduction. This is a one-way handoff: Farey specifies the window and the exponent its destination needs; Möbius owns the source estimate. It does not duplicate the current anti-diagonal collision clue, which concerns another source family and observable, or the historical mean-absolute Mertens question.

## Decisive test

Reconstruct the reduction and the pointwise obstruction from exactly these source files:

- `research/farey_discrepancy/findings/FD-311-a-quarter-power-sliding-variance-saving-would-close-balanced-capacity.md`
- `research/farey_discrepancy/findings/FD-312-pointwise-mertens-envelopes-cannot-close-sliding-variance-below-source-ceiling.md`

**Bounded source-reading grant:** these two findings may be read for the deterministic lower bound, strict saving threshold, selected-window quantifiers, conditional aspect-ratio localization, and the separate-endpoint no-go. No other Farey browsing is authorized by this clue.

Then either derive the required bound with one fixed `eta>0.2548875021...` uniformly over all windows permitted by the reduction; obtain it from a stronger independently justified Möbius theorem after paying conversion and exceptional-set costs; or produce a precise source-faithful obstruction identifying the additional arithmetic premise needed. Compare with MC-176--MC-177 so that a proposed theorem is not merely the already-priced Gallagher target renamed.

An almost-all estimate must pay the second-moment contribution of its exceptional starts, not only their density. A logarithmic saving or an unspecified `o(XN^2)` does not cross the fixed-power threshold. Preserve cancellation in `M(y+N)-M(y)` before any triangle inequality. The RH-localized aspect-ratio band must not silently become an unconditional description of every selected window: state explicitly whether the conclusion is conditional, or establish the needed window localization independently.

## Evidence boundary

FD-311 is a reduction and theorem-design threshold, not a new Möbius variance bound. FD-312 excludes separate pointwise endpoint majorization in its stated shell regime, not true short-interval mean-square cancellation. MC-176--MC-177 quantify the difficulty and some consequences but do not prove the requested estimate. This proposed clue establishes no transfer theorem, RH consequence, or novelty claim; it routes a precise question for the destination owner to test.
