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
  - research/visual_exploration/findings/VIS-335-wang-high-frequency-mode-derivative-repayment.md
  - research/visual_exploration/findings/VIS-336-wang-quadratic-chirp-derivative-repayment.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The Wang analysis has now separated the generic transform mechanics from the remaining arithmetic question.

For the fixed source, `VIS-330` and `VIS-331` price genuine pointwise real-axis decay: a fixed power saving already buys a fixed zero-free half-plane, while a sublinear logarithmic decay rate remains on the analytically cheaper side of that direct Mellin comparison. `VIS-332` shows that coherent regularly varying PNT-scale secondary terms pass through the symmetric two-tail smoothing rather than disappearing. `VIS-333` gives the exact real log-frequency multiplier

`m(xi)=4(1+i xi)/(4+xi^2)`,

which has no real-frequency zero and attenuates high frequencies by only one order. `VIS-334` gives the exact causal inverse: a smooth pointwise gain in both `Q` and `Q'` transfers back to the normalized source remainder, so any transform-specific gain must store the missing scale in the derivative/high-frequency channel.

`VIS-335` shows that this surviving channel is not merely formal. For the exact half-line mode family `F_omega(u)=e^(i omega u)`, the Wang output satisfies `sup |Q_omega|=O(omega^-1)` while the derivative retains asymptotic amplitude `|omega m(omega)|->4`. Thus the filter really can make `Q` small while `Q'` remains at source scale; on this control the derivative term in the inverse is asymptotically load-bearing.

`VIS-336` removes the remaining generic family-versus-trajectory loophole. For the single quadratic chirp

`F(u)=e^(i u^2/2)`,

whose instantaneous log-frequency is `omega(u)=u`, the exact Wang half-line transform satisfies

`Q(u)=F(u)(4i/u+4/u^2+O(u^-3))`

and

`Q'(u)=-4F(u)+O(u^-1)`.

So a single nonstationary trajectory can continuously migrate to higher log frequency, make `Q` pointwise small, and retain the missing source scale in `Q'`. The generic filter-level nonstationary possibility is therefore established; further generic chirp examples are not the live bottleneck.

The moving-upper occupancy branch is separately closed at the required upper-bound scale by `VIS-329`, so further center-gap/Christoffel refinement is not the current bottleneck either.

## Research question

For the actual normalized squared-von-Mangoldt summatory remainder

`F(u)=e^(-u)E_A(e^u)`,

can one prove genuinely scale-migrating or nonstationary log-frequency structure strong enough to make the exact Wang output

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`

pointwise smaller than the current Korobov--Vinogradov-scale source envelope, while the missing amplitude is carried by a larger derivative channel rather than by a hidden assumption equivalent to a stronger source estimate?

If so, does Wang's complete downstream error decomposition actually use the smaller `Q` in a way that avoids paying back that derivative carrier? A direct stronger estimate for `F` remains valid mathematics, but it is new source arithmetic rather than transform leverage.

## Why it may matter

The generic filter question is now settled sharply enough to stop confusing three issues. High-frequency attenuation is structurally available, its exact price is one derivative, and `VIS-336` shows that the same asymmetry survives on a single scale-migrating trajectory. The unresolved problem is no longer whether nonstationarity can help an LTI filter in principle; it is whether the arithmetic source has the required organization and whether the final Wang destination can exploit it without repayment.

A positive answer would isolate a genuinely source-specific mechanism not ruled out by regular variation, bounded-frequency controls, the inverse derivative tax, or the single-chirp matched control. A negative answer showing that every admissible arithmetic implementation necessarily repays the derivative carrier would close the remaining transform-specific fixed-source route for a structural reason.

## Decisive test

Start from the exact signed Wang transform, not from an absolute source envelope. Identify a source-specific nonstationary mechanism for the actual `Lambda^2` remainder and quantify its local or multiscale log-frequency growth. The mechanism must add arithmetic information beyond `VIS-335` and `VIS-336`; those findings already establish the generic fixed-frequency and single-chirp possibilities.

Derive the resulting pointwise size of `Q` and compare it against the current Korobov--Vinogradov-scale input. If the proposed gain is described by `exp(-phi(u))`, compute the lower linear rate `liminf phi(u)/u`; any positive rate carries the zero-free-half-plane cost from `VIS-331`.

Then trace the same mechanism through Wang's complete destination. Explicitly identify every term that depends on `Q`, `Q'`, or equivalent unsmoothed information. Accept transform leverage only if the final bound retains the smaller `Q` scale without requiring derivative-sized control that reconstructs the source through `VIS-334`.

Use `VIS-332`--`VIS-336` as matched controls. Kill a candidate if it reduces to coherent regular variation, a fixed or bounded log-frequency band, a smooth simultaneous `Q,Q'` envelope, generic high-frequency attenuation, a generic slowly varying chirp, a hidden stronger bound for `F`, or a downstream term that pays back the derivative carrier.

Do not spend another research cycle producing a new abstract chirp family unless it exposes a quantitatively different obstruction needed for the actual arithmetic source or Wang destination. The next useful result must connect the frequency-migration mechanism to `E_A` itself or to the downstream repayment budget.

## Evidence boundary

`VIS-329` closes only the moving-upper occupancy obstruction at the required upper-bound scale. `VIS-330`--`VIS-334` classify generic real-axis, Mellin, regular-variation, fixed-frequency, and inverse boundaries. `VIS-335` proves that the `Q`-small/`Q'`-large regime exists for the exact filter on a frequency-indexed model family. `VIS-336` strengthens only the generic control: the same regime occurs on one quadratic chirp with increasing instantaneous frequency.

None of these results proves that the actual squared-von-Mangoldt remainder migrates to increasing log frequency, admits a useful chirp or packet decomposition, improves the Korobov--Vinogradov envelope, or that Wang's final statistic avoids derivative-sensitive information. Those are the remaining arithmetic and destination-level burdens.

## Research disposition

Outcome: **narrowed**.

The clue remains `accepted`. `VIS-335` resolved the fixed-frequency filter-possibility question, and `VIS-336` resolves the generic single-trajectory nonstationary version. The live question is now specifically arithmetic-plus-destination: whether the actual normalized `Lambda^2` remainder realizes a quantitatively useful frequency-migration mechanism and whether the complete Wang argument preserves the resulting small-`Q` scale without repaying the derivative tax.