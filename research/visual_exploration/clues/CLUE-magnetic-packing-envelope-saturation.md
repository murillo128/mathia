---
id: CLUE-visual_exploration-magnetic-packing-envelope-saturation
type: research-clue
status: resolved
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-215-weighted-cycle-frustration-packing.md
  - research/visual_exploration/findings/VIS-218-subcritical-effective-edge-density-closes-magnetic-rms.md
  - research/visual_exploration/findings/VIS-219-cycle-packing-must-saturate-envelope-to-rms.md
  - research/visual_exploration/findings/VIS-220-simple-cycle-packing-universal-envelope-ceiling.md
---

# Can weighted cycle frustration saturate the prime-phase envelope to RMS precision?

## Observation

`VIS-215` gives the exact packing certificate

`max_z |G(z)| <= B-min(P_+,P_-)`.

`VIS-219` identifies its correct normalized strength:

`[B-min(P_+,P_-)]/sqrt(R)`
` = sqrt(2N_eff)[1-min(P_+,P_-)/B]`.

For the strictly subcritical prime-phase matrices of `VIS-218`, `N_eff` diverges like `y^2/[H(log y)^2]`. A positive fraction of packed frustration is therefore not enough. The two signed packing optima must jointly leave only an `O(sqrt(R))` residual, equivalently saturate `B` to relative precision `O(N_eff^(-1/2))`.

## Research question

For the canonical prime-phase graph family `A_(y,H)` in the strictly subcritical regime, does

`D_pack(y,H)`
` := [B(A_(y,H))-min(P_+,P_-)]/sqrt(R(A_(y,H)))`

remain bounded along any asymptotically meaningful range, or must it diverge?

If boundedness occurs, what arithmetic structure forces both the positive- and negative-envelope cycle packings to approach total weighted saturation, and is that saturation absent or materially weaker in matched phase-surrogate controls?

## Why it may matter

A bounded `D_pack` would make the deterministic `VIS-215` cycle-packing certificate strong enough to prove Haar-RMS-scale worst-start suppression for the exact fixed-modulus torus problem, something the normalized spectral relaxation cannot do by `VIS-218`.

A proof that `D_pack->infinity`, or even a lower bound forcing divergence throughout the subcritical regime, would close this particular packing-certificate route and prevent further work from confusing abundant local holonomy with quantitatively sufficient global frustration.

## Decisive test

First work in the exact weighted normalization. For increasing finite prime-phase graphs, compute or rigorously bound both edge-capacity fractional cycle-packing optima `P_+` and `P_-`, then track

`D_pack=[B-min(P_+,P_-)]/sqrt(R)`

and the equivalent relative deficit

`1-min(P_+,P_-)/B`.

Compare the latter against the required scale `N_eff^(-1/2)`, which by `VIS-218` is `asymp sqrt(H) log y/y` in the strictly subcritical regime. Raw cycle count, edge-disjoint-cycle density, or `P/|E|` are not substitutes for this test.

If finite experiments suggest bounded `D_pack`, isolate which cycle families carry almost all weighted capacity and derive an analytic lower bound on `min(P_+,P_-)` with residual `O(sqrt(R))`. Only after a canonical saturation signal survives should matched controls preserve the coefficient magnitudes and graph geometry while replacing arithmetic phase data, to test whether the saturation is genuinely arithmetic-specific.

Kill this certificate route if one can prove `D_pack->infinity`, or if every plausible packing family leaves a residual much larger than `sqrt(R)` for a structural reason that survives stronger cycle enumeration or LP relaxations.

## Evidence boundary

`VIS-219` establishes the saturation threshold that this certificate must meet. `VIS-220` now proves a phase-independent ceiling for the exact `VIS-215` LP: on a simple support graph every simple-cycle packing satisfies `P_+,P_-<=2B/9`, so the residual is always at least `7B/9`. The clue is therefore resolved for this certificate family. The result does not constrain stronger non-packing certificates or the exact torus optimum.

## Research disposition

Outcome: refuted

Resolved by:
- [[research/visual_exploration/findings/VIS-220-simple-cycle-packing-universal-envelope-ceiling]]

The proposed near-saturation regime is algebraically impossible for the `VIS-215` fractional simple-cycle packing certificate. `VIS-220` proves

`D_pack >= (7/9)sqrt(2N_eff)`

for every simple support graph, hence `D_pack->infinity` throughout the strictly subcritical prime-phase regime of `VIS-218`. Further work should move to the exact fixed-modulus torus optimization or to a genuinely stronger certificate rather than enlarging or reoptimizing this packing LP.