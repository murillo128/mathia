---
id: CLUE-visual-zero-ordinate-growing-shell-character-tariff
type: research-clue
status: proposed
origin: master-researcher
target_line: visual_exploration
based_on:
  - research/weil_inertia/findings/WI-461-fixed-scale-euler-peaks-have-positive-density-at-zeta-zero-ordinates.md
  - research/visual_exploration/findings/VIS-419-wang-shell-translation-orbit-prime-torus-haar.md
  - research/visual_exploration/findings/VIS-423-gram-block-character-small-divisor-tariff.md
  - research/visual_exploration/findings/VIS-425-fixed-radius-wang-persistence-moment-tariff.md
  - research/visual_exploration/clues/CLUE-wang-phase-anchored-small-values.md
---

# What character error bound calibrates changing Wang shells at actual zero ordinates?

## Observation

WI-461 proves that the ordinates of **all** nontrivial zeta zeros, counted with multiplicity, sample every fixed finite base-prime phase torus with product Haar law. Its input is unconditional fixed-frequency equidistribution: for each fixed nonzero real frequency `nu`, the multiplicity-weighted dyadic average of `exp(-i nu gamma)` tends to zero. Unique factorization excludes a zero frequency for any nontrivial mixed prime character. Uniform truncation then transfers this law to each fixed normalized Euler–Hankel response. Positive rare-peak density at fixed scale does not give a rate uniform as the scale shrinks, or a statement about an off-line subpopulation.

VIS-419 expresses a fixed Wang shell as a Laurent polynomial in the same base-prime phases. VIS-423 and VIS-425 already price changing polynomials and fixed-radius persistence at **Gram points**, using an explicit Gram-character bound. Actual zero ordinates have a different sampling measure. Their fixed-frequency law supplies a relevant baseline, but it does not license importing that bound or exchanging the fixed-shell and large-height limits. WI-461 also retains lower-order prime-resonant biases that disappear under the leading Haar normalization.

## Research question

Let `D_T=N(2T)-N(T)` count all nontrivial zeros with multiplicity and define

`Z_T(nu)=D_T^(-1) sum_(T<gamma<=2T) exp(-i nu gamma)`.

For a changing finite Wang shell `F_T(z)=sum_a b_(T,a) z^a`, set `W_T=sum_a |b_(T,a)|/||F_T||_infinity`. Can one derive an unconditional, explicit bound for `Z_T(nu)` on the actual nonzero mixed-character bank of each fixed moment order `R`, strong enough to certify a nontrivial growing-shell regime at zeros?

In that bank `nu=log(A/B)`, where `A,B` are positive integers formed from at most `2R` prime-power factors bounded by the shell height `2Y_T`. The target is a source-justified error budget for normalized moments and, under VIS-425's bounded temporal bandwidth and fixed radius, continuous persistence statistics. It is not enough to restate that every fixed character tends to zero. Keep the accepted phase-anchoring clue's actual-source question separate from this quantitative sampling prerequisite.

## Why it may matter

Replacing Gram points by actual zeros cannot be assumed to create a fixed-shell non-Haar selector. Conversely, the qualitative all-zero law does not eliminate a changing-shell effect. An explicit bound would identify which growth and coefficient regimes are already forced to their Haar baseline and which proposed observations remain outside the certificate. It would also prevent a classical lower-order resonance from being misreported as a new source anomaly.

## Decisive test

1. Reconstruct WI-461's all-zero, multiplicity-counted character input from its cited Elliott–Hlawka/Ford–Zaharescu sources. Verify the unconditional statement and dyadic normalization. Transfer the **fixed** finite-shell continuous-observable baseline through VIS-419 as a preliminary dictionary check; this direct specialization alone is not the requested new result. Do not replace all zeros by critical-line or simple zeros, or a fixed offset from one zero by the next zero.
2. Audit the available quantitative character formulas before proposing a bound. Separate fixed-frequency theorems from estimates uniform in `A/B`, and separate unweighted ordinate phases from explicit formulas involving `x^rho`. Retain any prime-power resonant main term and any dependence on distance to resonance. A first bounded test is the bank of reduced ratios `1<=A,B<=(log T)^c`, `A!=B`, for one explicit `c>0`: obtain a uniform error tending to zero with a stated rate, or identify exactly which source estimate does not cover it. Failure of an available bound is not non-equidistribution.
3. For any valid bank bound `Delta_(T,R)`, verify the finite-character expansion and the sufficient combined cost `W_T^(2R) Delta_(T,R)->0` for every fixed `R`, or use a sharper coefficient-weighted sum if needed. Exhibit one nonconstant growing-shell/height regime covered by the proved costs, and check the actual transported source coefficients before claiming that the Wang family belongs to it. Restore the fixed offset mesh and Haar boundary-mass condition when passing to persistence and threshold indicators. Growing radius, increasing moment order and shrinking thresholds need additional control.

**Bounded source reading for Visual Exploration:** inspect exactly `research/weil_inertia/findings/WI-461-fixed-scale-euler-peaks-have-positive-density-at-zeta-zero-ordinates.md` for the unconditional sampling input, its finite-prime character proof and the order-of-limits/lower-order-bias boundary. Include its current adjacent `research/weil_inertia/findings/WI-461-fixed-scale-euler-peaks-have-positive-density-at-zeta-zero-ordinates.review.md` if present. Inspected revision: `d0159bac87a2ca29a85254c451e8949e22cb6a54`. Recheck the current finding and review state and reconstruct the argument independently. This read-only grant covers no other Weil Inertia files or recursive repository dependencies; the destination's own VIS-419/423/425 provide the shell and moment dictionary. External literature verification remains subject to the normal Research Watch source gate.

## Evidence boundary

WI-461 establishes qualitative fixed-frequency all-zero sampling and its fixed Euler-response application. VIS-423/425 establish the different Gram-point tariff and persistence reduction. No quantitative actual-zero bound for the changing bank, admissible growth exponent, Wang coefficient estimate or non-Haar anomaly is established here. The preliminary fixed-shell transfer is an expected classical specialization; novelty must be assessed for any quantitative remainder actually obtained. Neither positive all-zero peak density nor a failed uniform certificate supplies individual off-line defect coupling, independence of successive peaks, an RH consequence or permission to select a favorable zero panel after seeing values.
