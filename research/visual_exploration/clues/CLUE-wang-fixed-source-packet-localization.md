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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The Wang analysis has now separated the generic transform mechanics from the remaining arithmetic question.

For the fixed source, `VIS-330` and `VIS-331` price genuine pointwise real-axis decay: a fixed power saving already buys a fixed zero-free half-plane, while a sublinear logarithmic decay rate remains on the analytically cheaper side of that direct Mellin comparison. `VIS-332` shows that coherent regularly varying PNT-scale secondary terms pass through the symmetric two-tail smoothing rather than disappearing. `VIS-333` gives the exact real log-frequency multiplier

`m(xi)=4(1+i xi)/(4+xi^2)`,

which has no real-frequency zero and attenuates high frequencies by only one order. `VIS-334` gives the exact causal inverse: a smooth pointwise gain in both `Q` and `Q'` transfers back to the normalized source remainder, so any transform-specific gain must store the missing scale in the derivative/high-frequency channel.

`VIS-335` shows that this surviving channel is not merely formal. For the exact half-line mode family `F_omega(u)=e^(i omega u)`, the Wang output satisfies `sup |Q_omega|=O(omega^-1)` while the derivative retains asymptotic amplitude `|omega m(omega)|->4`. Thus the filter really can make `Q` small while `Q'` remains at source scale; on this control the derivative term in the inverse is asymptotically load-bearing.

The moving-upper occupancy branch is separately closed at the required upper-bound scale by `VIS-329`, so further center-gap/Christoffel refinement is not the current bottleneck.

## Research question

For the actual normalized squared-von-Mangoldt summatory remainder

`F(u)=e^(-u)E_A(e^u)`,

can one prove genuinely scale-migrating or nonstationary log-frequency structure that makes the exact Wang output

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`

pointwise smaller than the current Korobov--Vinogradov-scale source envelope, while the missing amplitude is carried by the larger derivative channel rather than by a hidden assumption equivalent to a stronger source estimate?

If so, does Wang's complete downstream error decomposition actually use the smaller `Q` in a way that avoids paying back the order-one derivative carrier? A direct stronger estimate for `F` remains valid mathematics, but it is new source arithmetic rather than transform leverage.

## Why it may matter

The generic filter question is now settled sharply enough to stop confusing two issues. High-frequency attenuation is structurally available, and its exact price is known: one power of log frequency, recovered by differentiation. The unresolved problem is whether the arithmetic source has the required moving-frequency organization and whether the final Wang destination can benefit from it.

A positive answer would isolate a genuinely source-specific mechanism not ruled out by regular variation, bounded-frequency controls, or the inverse derivative tax. A negative answer showing that every admissible arithmetic implementation necessarily repays the derivative carrier would close the remaining transform-specific fixed-source route for a structural reason.

## Decisive test

Start from the exact signed Wang transform, not from an absolute source envelope. Identify a source-specific nonstationary mechanism for the actual `Lambda^2` remainder and quantify its local/multiscale log-frequency growth. The model must do more than reproduce `VIS-335`: that finding is only a generic high-frequency control.

Derive the resulting pointwise size of `Q` and compare it against the current Korobov--Vinogradov-scale input. If the proposed gain is described by `exp(-phi(u))`, compute the lower linear rate `liminf phi(u)/u`; any positive rate carries the zero-free-half-plane cost from `VIS-331`.

Then trace the same mechanism through Wang's complete destination. Explicitly identify every term that depends on `Q`, `Q'`, or equivalent unsmoothed information. Accept transform leverage only if the final bound retains the smaller `Q` scale without requiring derivative-sized control that reconstructs the source through `VIS-334`.

Use `VIS-332`--`VIS-335` as matched controls. Kill a candidate if it reduces to coherent regular variation, a fixed/bounded log-frequency band, a smooth simultaneous `Q,Q'` envelope, the generic pure-mode attenuation already classified by `VIS-335`, a hidden stronger bound for `F`, or a downstream term that pays back the derivative carrier.

A natural next mathematical control is a single slowly varying chirp or wave-packet family with frequency tending to infinity. It is useful only if it clarifies what quantitative adiabatic/nonstationary conditions are needed before confronting the arithmetic source; do not mistake such a control for evidence about `E_A` itself.

## Evidence boundary

`VIS-329` closes only the moving-upper occupancy obstruction at the required upper-bound scale. `VIS-330`--`VIS-334` classify generic real-axis, Mellin, regular-variation, fixed-frequency, and inverse boundaries. `VIS-335` proves only that the `Q`-small/`Q'`-large regime exists for the exact filter on a frequency-indexed model family.

None of these results proves that the actual squared-von-Mangoldt remainder migrates to increasing log frequency, improves the Korobov--Vinogradov envelope, or that Wang's final statistic avoids derivative-sensitive information. Those are the remaining arithmetic and destination-level burdens.

## Research disposition

Outcome: **narrowed**.

The clue remains `accepted`, but its transform-level possibility question is resolved by `VIS-335`: Wang's filter can suppress a sufficiently high log-frequency mode by one order while the derivative retains the source scale. The live question is now specifically whether the actual arithmetic source realizes a useful nonstationary version of that mechanism and whether the complete Wang destination preserves the gain without repaying the derivative tax.
