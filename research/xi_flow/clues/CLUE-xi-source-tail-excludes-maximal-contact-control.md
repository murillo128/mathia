---
id: CLUE-xi-flow-source-tail-excludes-maximal-contact-control
type: research-clue
status: proposed
origin: mind
target_line: xi_flow
based_on:
  - research/xi_flow/findings/XF-159-uniform-full-field-blindness-survives-all-subexponentially-lipschitz-postprocessing.md
  - research/xi_flow/findings/XF-160-positive-fourier-sources-retain-maximal-contact-blindness-with-asymptotically-prescribed-transition-gaps.md
  - research/xi_flow/findings/XF-161-appell-smoothing-preserves-prescribed-transition-gaps-under-strictly-positive-analytic-fourier-sources.md
---

# Does the Xi theta-source law exclude maximal-contact controls beyond positivity and analytic smoothness?

## Observation

XF-159 shows that the maximal-contact transition is exponentially hidden throughout a full blind spacetime field under every subexponentially Lipschitz decoder. XF-160 and XF-161 then remove two natural source-side escape arguments: the same transition gap can coexist with nonnegative Fourier sources and, on any prescribed finite heat window, with strictly positive analytic Gaussian-mixture source densities.

The surviving distinction is therefore not generic positivity or smoothness. The actual Riemann Xi source has much more rigid theta-series organization and superexponential tail structure, while the current controls are finite-spectrum or Gaussian-mixture constructions and XF-161 is only finite-horizon.

## Research question

Is there an explicit quantitative identity or inequality forced by the Xi theta source — for example a normalized tail ratio, log-convexity/complete-monotonicity relation, moment-growth law, discrete coefficient constraint, or one-source all-time compatibility condition — that every asymptotic maximal-contact control of XF-160/XF-161 must violate by an amount large enough to beat the XF-159 blind exponent?

The desired condition must be derived from the source before inspecting the transition and must distinguish Xi from the generic positive analytic controls already constructed.

## Why it may matter

A positive answer would move the route around the target-side conditioning wall instead of trying to out-sense it. More importantly, it would identify the precise Xi-specific information that the matched controls discard, turning the vague instruction to use the true source into a falsifiable source theorem.

A negative answer for broad candidate constraints would also be useful by showing that theta-tail regularity alone remains too generic and that deeper arithmetic coefficient structure is required.

## Decisive test

Derive one candidate constraint directly from the explicit Xi theta kernel in a normalization compatible with the heat flow. Evaluate the same normalized quantity on the XF-160 positive-spectrum companions and their XF-161 Appell-smoothed versions along the maximal-contact scaling.

Accept the direction only if the Xi source forces a uniform separation strong enough to exclude the control or improve the transition visibility exponent. Reject a candidate constraint if the matched sources satisfy it asymptotically, if its constants deteriorate exponentially at exactly the XF-159 margin, or if it is merely a restatement of positivity/analyticity already defeated by XF-160--XF-161.

## Evidence boundary

No current finding proves that superexponential theta tails, log-convexity, moment growth, or all-time compatibility excludes the maximal-contact family. XF-160--XF-161 prove only that weaker positive and analytic source classes remain noncoercive. This clue identifies the next source-side discriminator to test; it is not evidence that such a discriminator exists or that it would imply RH.