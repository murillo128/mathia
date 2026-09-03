---
id: CLUE-weil-inertia-higher-zero-correlations-horizontal-rigidity
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-002-density-one-moment-tower-needs-audit.md
  - research/weil_inertia/findings/WI-005-critical-lattice-screening-defeats-depth-only-negative-mass.md
  - research/weil_inertia/findings/WI-006-critical-lattice-screening-is-matrix-equivalent-to-doubles.md
  - research/weil_inertia/findings/WI-007-support-one-is-screening-threshold-for-cross-scale-depth.md
  - research/weil_inertia/findings/WI-043-maximal-pair-discrepancy-does-not-control-locked-four-point-covariance.md
  - research/weil_inertia/findings/WI-115-tsang-pair-horizontal-signal-is-cancelled-by-critical-lattice-screening.md
  - research/prior_art/montgomery-pair-correlation.md
---

# Can richer zero correlations turn horizontal information into a stronger critical-line inertia bound?

## Observation

`WI-001` isolates the first-two-moment support-one barrier, while `WI-005`--`WI-007` show a stronger horizontal-information obstruction: at critical vertical spacing, off-line mirror pairs can be matrix-equivalent to on-line doubles for every Alpöge--Furman-type compression of support at most one. `WI-043` separately shows that even strong pair-discrepancy control need not determine a locked four-point covariance. These facts leave open whether a different zero-correlation observable can retain horizontal information that survives the screening quotient.

`WI-115` materially narrows the question using the current v3 Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh Tsang-kernel method. A complex **pair** statistic already detects horizontal displacement on a same-height mirror pair, so genuine `k>=3` information is not needed merely for local detectability. But on the WI critical screening lattice the complete support-one Tsang statistic cancels that same-height excess exactly; long natural finite blocks retain only `O(log M)=o(M)` discrepancy, and the unconditional Montgomery weight changes the block comparison only by `O(1)`. The horizontal power of the published box argument instead comes from a microscopic **termwise positivity** condition that allows the same-height sub-sum to be extracted before cross-height cancellation.

## Research question

Can one obtain an unconditional information carrier or inequality that quantitatively prevents the compensating cross-height cancellation identified in `WI-115`, and then feed that control into the Weil-inertia certificate to force a strictly larger proportion of zeros onto `Re s=1/2`?

The first targets are now more specific than “try higher correlations.” Test whether the pairs outside the Tsang positivity strip can be bounded sharply enough from established zero-density or correlation theorems; whether another arithmetically accessible pair kernel has a horizontal signal that survives the WI screening lattice at density scale; or whether crossing support one yields a usable alias without paying an unavailable prime-pair input. Only if pair-level routes fail for a structural reason should the search escalate to mixed moments or genuine finite `k`-point statistics, which must themselves be checked against the same screening configuration.

## Why it may matter

`WI-115` supplies both a positive and a negative lesson. Pair correlation does contain an exact horizontal-depth defect: under the BGSTB positivity hypothesis, retaining the quadratic remainder in `cosh` controls a same-height horizontal variance in addition to horizontal multiplicity. But support-one global summation can erase that signal at leading order. The useful research question is therefore no longer whether horizontal information exists, but whether available arithmetic can isolate it from the cross-height reservoir that screens it.

A successful controller would attack the exceptional complement directly rather than squeezing the same first-two trace moments harder. A rigorous impossibility result would also be valuable if it shows that every support-one pair-level controller compatible with the unconditional Montgomery form factor is screenable, thereby justifying escalation to supercritical support or genuinely higher correlations.

## Decisive test

Start with the exact Tsang interface in `WI-115`. Derive a decomposition of the evaluated pair sum into the same-height horizontal-defect term and the complementary cross-height contribution. Using only established unconditional inputs, either prove a lower bound on that complement strong enough that the horizontal defect survives at order `N`, or construct a zeta-count-compatible screened configuration showing that the proposed controller remains `o(N)`-blind.

For any replacement pair or `k`-point statistic, repeat the same adversarial test against the WI-005/WI-006 lattice before investing in arithmetic evaluation. A route counts as a substantive success only if the surviving statistic yields an explicit deterministic bound on off-line mass/depth and that bound can be inserted into the existing inertia/rank certificate using proved, not conjectural, correlation information.

## Evidence boundary

`WI-115` establishes local Tsang horizontal sensitivity, exact support-one lattice cancellation for the bare kernel, `O(log M)` finite-block blindness, and `O(1)` stability of that block comparison under the Montgomery weight. It does **not** prove that every pair statistic is blind, that all higher correlations collapse, or that no unconditional estimate can control the terms outside the Tsang positivity strip.

The BGSTB simple-critical proportions in a fixed narrow box remain conditional on their box/positivity hypothesis (or a suitably strong zero-density hypothesis). They are not unconditional improvements to the Mathia bound. The all-order trace-moment route in `WI-002` remains separately unverified and cannot be used as evidence for this clue.

## Research disposition

Accepted and narrowed by `WI-115`. Pair-level horizontal detectability is established, but the raw support-one Tsang/Montgomery pair statistic is screened at density scale. The live question is now whether one can **unconditionally control the compensating cross-height contribution** or construct a different finite-order observable whose horizontal signal survives the canonical screening extremizer and has an established arithmetic evaluation.
