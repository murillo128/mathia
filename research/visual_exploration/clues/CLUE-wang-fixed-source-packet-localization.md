---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
---

# Does Wang packet localization preserve the fixed-source diagonal profile without manufacturing strip gain?

## Observation

`VIS-283` isolates the fixed-source coefficient-scale field energy after the exact gamma baseline is retained. On compact fixed physical-source windows, the signed prime/source cross is power-small after packet normalization, while the surviving `L^-2` arithmetic profile before packet projection is the positive diagonal quantity

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

with `x=e^(2*pi*q)`. The finding deliberately stops before projecting this profile through the test-function/packet layer. That projection is therefore the next unresolved interface: a packet can average, suppress, or emphasize regions of the fixed-source profile even when the underlying cross sector is already negligible.

## Research question

For a pre-fixed localized family of test weights in the physical-source coordinate `q`, does the normalized Wang contribution reduce, through the `L^-2` scale isolated in `VIS-283`, to a bounded linear projection of `Q_gamma(e^(2*pi*q))` with source-threshold behavior and off-critical strip gain remaining mathematically separable?

Equivalently, can one distinguish genuine variation already present in the fixed-source diagonal profile from apparent amplification or suppression created only because the packet support, width, or normalization moves toward a source boundary or another singular scaling regime?

## Why it may matter

The fixed-source analysis has removed two possible false mechanisms: zero-window localization and signed prime/source cancellation are both too small to create the coefficient-scale signal. Packet projection is now the remaining interface between that local field-energy profile and the actual test statistic. If localization itself can create an effective gain, a visually or numerically strong packet signal could be mistaken for new arithmetic information. If instead fixed compact packets preserve the profile through a controlled linear functional, the representation becomes cleaner: packet design changes what part of `Q_gamma` is observed without changing the underlying fixed-source mechanism.

## Decisive test

Choose the packet family before inspecting the resulting signal. Include at least one compact family whose support stays uniformly inside a fixed physical-source interval, and a controlled family whose support or width approaches the relevant source boundary. Derive the packet contribution from the exact normalization used in the Wang specialization rather than fitting it from finite data, keeping the `q -> x=e^(2*pi*q)` Jacobian and test-function factors explicit.

For the fixed-interior family, determine whether the entire coefficient-scale term is a uniformly bounded linear functional of `Q_gamma(e^(2*pi*q))` plus an error smaller than `L^-2`. Then repeat the derivation for the approaching-boundary family and track separately any factor responsible for the previously identified source threshold or off-critical strip gain. Use a matched source-only or diagonal-profile control with the same packet geometry to test whether any apparent gain is reproduced without new zero-sensitive structure.

Kill the direction if the claimed enhancement is generated solely by moving or narrowing the packet, by the source-boundary factor already present in the fixed-source representation, or by normalization choices. A surviving effect should require a term that cannot be reproduced from the established `Q_gamma` profile and the packet geometry alone.

## Evidence boundary

`VIS-283` establishes the fixed-source diagonal profile and the negligibility of the signed cross sector in its stated compact regime. It does not establish how a localized test packet projects that profile, uniformity for packets approaching a source threshold, or any new strip-gain theorem. This clue proposes that separation test only. It makes no claim of a new pair-correlation result, RH criterion, or arithmetic invariant.
