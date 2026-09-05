---
id: CLUE-prime-circle-cyclotomic-signed-radial-flux-assembly
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_circle
based_on:
  - research/weil_positivity/findings/WP-162-cyclotomic-inward-radial-flux-is-positive-exactly-on-prime-powers.md
---

# Signed radial-flux assembly before Prime-Circle positivity

## Observation

`WP-162` gives an exact cyclotomic shell observable

`rho_n(s) = -d/ds log Phi_n(e^{-s})`

whose total inward radial flux is exactly `Lambda(n)`. Prime-power shells are pointwise positive, whereas every non-prime-power shell has zero total flux and therefore contains a compensating negative region. Any shellwise positive scalarization such as total variation, an `L^q` norm, squaring, or a positive local density makes every shell nonzero and destroys the exact Mangoldt support. Prime Circle's live route already uses cyclotomic logarithmic/exterior-field structure, so this is a destination-relevant selector rather than a generic analogy.

## Research question

Can Prime Circle preserve the signed cyclotomic radial flux across shells long enough for a source-canonical cross-shell and finite-archimedean assembly to produce a useful positivity statement, instead of applying positivity shell by shell before the Mangoldt selector has been assembled?

## Why it may matter

This is a concrete bridge from an exact prime-power selector to Prime Circle's surviving complex/log-potential architecture. It directly tests the current global bottleneck: whether a source-specific selector can survive the representation and assembly operations needed by the destination theorem without being classicalized into a positive statistic that has already lost arithmetic support.

## Decisive test

At a finite cutoff `N`, build the simplest source-native coupled functional `A_N` from the signed `rho_n` that includes at least one prime-power shell and one non-prime-power control shell, together with any archimedean or boundary term forced by the Prime Circle model. Compare it with a matched control in which the cross-shell coupling is removed. The clue survives only if the uncoupled or shellwise-positive version loses exact `Lambda` support as `WP-162` predicts, while the coupled source-native assembly retains exact or quantitatively vanishing response on non-prime-powers and yields a sign or margin unavailable in the matched control. If every source-natural coupling either factorizes into shellwise positivity or leaves comparable mass on non-prime-power shells, reject the clue.

## Evidence boundary

`WP-162` proves the signed shell identity and the failure of shellwise positive scalarization. It does not prove that a useful Prime-Circle global coupling exists, that an archimedean completion preserves the selector, or that any resulting positivity statement has RH strength. This clue proposes only the destination-local falsification test.
