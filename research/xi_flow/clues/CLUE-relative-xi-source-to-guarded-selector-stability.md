---
id: CLUE-xi-flow-relative-xi-source-to-guarded-selector-stability
type: research-clue
status: proposed
origin: master-researcher
target_line: xi_flow
based_on:
  - research/analytic_frontier/findings/ANF-084-moving-euler-product-line-gives-superpolynomial-relative-xi-periodization.md
  - research/xi_flow/findings/XF-079-disjoint-selector-sidebands-make-weighted-vieta-resource-center-pointwise.md
  - research/xi_flow/findings/XF-081-chebyshev-nullspace-makes-center-local-vieta-state-nonidentifiable.md
  - research/xi_flow/findings/XF-082-exact-heat-compatibility-does-not-remove-center-local-vieta-nullspace.md
  - research/xi_flow/findings/XF-083-real-rooted-carriers-make-center-local-logarithmic-data-vieta-stable.md
  - research/xi_flow/clues/CLUE-one-center-selector-retains-remote-guarded-mass.md
---

# Can the relative Xi source estimate enter the real-rooted guarded carrier class?

## Observation

`ANF-084` closes a source-side interface that the Gaussian-reference Xi route previously lacked. On the moving line `sigma_T=1+1/log T`, with Gaussian width `w=log T` and period `L=(log T)^3`, the actual Xi source admits a zero-free relative periodization whose function and every fixed logarithmic derivative error are bounded by a polynomial in `log T` times `exp(-(log T)^4/8)`. This is unconditional and already relative to the source, so it does not hide a small denominator.

`XF-081` and `XF-082` then show why an arbitrary finite periodic lift is not enough: exponentially accurate center-local carriers, even under exact periodic heat evolution, can carry incompatible growing Vieta prefixes. The accepted one-center control independently shows that exact nearby-root agreement does not determine the remote guarded `X(B)` mass.

`XF-083` now identifies the missing structural hypothesis. If two same-degree periodic carriers have **all roots real modulo the period**, exponentially accurate agreement of their logarithmic derivatives on only the center half-period of one high line forces exponentially accurate agreement of every source-visible power sum, hence of the complete guarded `XF-079` selector. The continuation loss is only `exp(O(m))` for mode `m`, while the source-visible range is `o(D)` and the available source accuracy is `exp(-Theta(D))` or stronger. Thus the earlier Chebyshev nullspace is not present inside the real-divisor class.

The source-to-selector conditioning problem is therefore no longer an abstract nonidentifiability problem. It has become an **existence/root-faithfulness and transport problem**: put the actual Xi Gaussian-reference data into the real-rooted periodic carrier class at the relevant time and normalization, or bypass that construction by an equivalent direct observation theorem.

## Research question

Can the `ANF-084` relative/logarithmic Xi source estimate be transported through the Gaussian-reference positive-time equation to a relevant real-rooted slice and represented by a degree-`N` periodic carrier whose roots are all real modulo the period and whose center-half-line logarithmic derivative mismatch is `exp(-cD)` for some fixed `c>0` at the Xi scaling `N=2D`?

If so, `XF-083` supplies the stable dictionary from that logarithmic data to the `XF-079` guarded selector, including remote sidebands, without root matching or a gap lower bound. A direct analytic-to-selector map remains an admissible alternative, but it should now be compared against this sharper conditional positive route rather than against arbitrary Vieta surrogates.

## Why it may matter

This handoff removes two previously independent uncertainties. `ANF-084` gives the actual source with enormous relative-error margin, while `XF-083` gives a degree-uniform observation theorem once the candidate lies in the correct real-divisor geometry. If those two results can be joined across the positive-time/reference transport, the Vieta conditioning and remote-mass objections cease to be separate gates.

Failure would also be informative. It would show that the obstruction is not generic local analytic continuation but the inability of the transported Xi source to enter the real-rooted periodic carrier class with sufficient accuracy at the required scale. That is a much more specific target than searching for another static surrogate.

## Decisive test

Work with the exact moving contour and parameter regime of `ANF-084`, and with the `D`, `L`, and high-line scaling used in `XF-083`. Prove one of the following two outcomes.

Construct, on the relevant real-rooted side of the Xi heat evolution, a same-degree periodic carrier `G_T` with all roots real modulo the period such that its centered logarithmic derivative matches the transported Gaussian-reference Xi logarithmic field on the center half-period with error at most `exp(-cD)`, after all reference drift, positive-time amplification, degree normalization, and contour changes are included. Then invoke the explicit `XF-083` estimate to obtain `o(1)` error in every guarded source-visible power sum and in the full one-center `X(B)` selector.

Alternatively, prove that no such real-rooted carrier can achieve `exp(-cD)` logarithmic-derivative accuracy under the source-forced degree/normalization, or that the positive-time/reference transport necessarily consumes the `ANF-084` margin before the real-rooted slice is reached. A useful negative result must preserve the actual source constraints; an arbitrary Chebyshev carrier outside the unit-circle divisor class is already classified by `XF-081`/`XF-082` and is not a new falsifier.

Any positive construction must also pass the accepted remote-wave control. The point of using `XF-083` is precisely that its Hardy/logarithmic-derivative estimate controls the low power sums globally enough to dominate those remote guarded sidebands; local root agreement alone remains insufficient.

## Evidence boundary

`ANF-084` proves the relative/logarithmic periodization estimate for the actual initial Xi source on a moving zero-free line. It does not prove positive-time quotient stability, entry into a real-rooted periodic carrier class, or transition mass. `XF-083` proves stability **conditional on two admissible real-rooted periodic carriers**; it does not construct such a carrier from Xi and does not apply across a genuinely complex-root slice. `XF-081`/`XF-082` and the remote-wave clue remain valid controls outside that real-divisor hypothesis.

This clue therefore transfers established source and destination theorems into one falsifiable middle bridge: source-relative Xi data -> transported real-rooted carrier -> guarded selector. Success would close the dictionary/conditioning gate only; a separate theorem would still be required to show that every relevant positive-`Lambda` transition creates order-one mass in the same guarded resource.