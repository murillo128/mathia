---
id: CLUE-weil-inertia-wang-weighted-dephasing-support-localization
type: research-clue
status: rejected
origin: mind
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-354-short-interval-pair-correlation-has-a-support-localization-barrier.md
  - research/visual_exploration/findings/VIS-309-wang-bohr-time-haar-equivalence.md
  - research/visual_exploration/findings/VIS-311-wang-weighted-gap-cubic-horizon.md
---

# Can coefficient-weighted finite-height control relax Wang's support-localization barrier?

## Observation

WI-354 isolates the current short-interval obstruction in Wang's pair-correlation theorem. For `H=T^theta` and Fourier support `|alpha|<=lambda`, the evaluated statistic carries an error `O(H+T^lambda L^2)`, so relative to the `HL` main scale the support-dependent term is `T^(lambda-theta)L`. The published interface therefore needs a strict fixed gap `lambda<theta`.

A separate analysis of the same Wang coefficient system identifies a more structured signed remainder. VIS-309 shows that its true deterministic prime-phase orbit has Bohr mean square `O(x log^3(3x))`. VIS-311 keeps coefficient-weighted local ratio spacing in a finite-window Montgomery--Vaughan estimate and lowers the sufficient dephasing horizon from the earlier quintic scale to a cubic one; the remaining explicit loss is the uniform hard-tail approximation, not the global minimum ratio gap.

These are established statements at different proof interfaces. It is not established that the VIS remainder is the load-bearing source of WI-354's full `T^lambda L^2` error, nor that improving its finite-window control improves Wang's admissible Fourier support.

## Research question

Trace the exact contribution of Wang's signed prime-power remainder through the short-interval pair-correlation proof and determine whether an energy-sensitive, nontruncated finite-height estimate can replace the part of the `T^lambda L^2` error that forces `lambda<theta`.

In particular, is there a rigorously uniform estimate at `x=T^alpha`, `alpha<=lambda`, whose dependence on the observation interval is strong enough to retain a fixed positive support width as `theta` decreases, without assuming the desired zero statistics or another RH-equivalent input?

## Why it may matter

WI-354 shows that improving only the zero-side Lamzouri optimization cannot turn localization into sparse-defect exclusion because the prime-side support budget is already lost. VIS-311, meanwhile, proves that a substantial part of the finite-height loss in the same coefficient system came from a proof representation that discarded weighted spectral geometry. If the support-dependent error contains the same removable loss, the arithmetic side of the WI localization barrier could move. If it does not, the comparison identifies exactly which Wang error term is structurally independent of the finite-height dephasing problem and prevents the two lines from repeatedly attacking the same apparent bottleneck under different notation.

## Decisive test

Start from the displayed decomposition that leads to Wang's short-interval formula and isolate the term or terms contributing `xL^3` and hence `T^lambda L^2` after support integration. Preserve all other errors unchanged.

Then either derive a replacement bound using the coefficient-weighted ratio energy and an energy-level treatment of the infinite tail, uniform for the required joint regime `x=T^alpha` and height interval `H=T^theta`, or prove that the VIS signed remainder is not the load-bearing contribution to the support restriction.

A successful transfer must produce an explicit new total error and show whether the condition `lambda<theta` is quantitatively relaxed. Kill the route if another unchanged term still forces the same support gap, if the required finite-window horizon exceeds the available `H`, if the bound is only an iterated Bohr limit with fixed `x`, or if the needed input already presupposes the zero-free/correlation conclusion being sought.

## Evidence boundary

WI-354 proves only the support-localization barrier for Wang's current displayed error. VIS-309 is an infinite-time quadratic statement at fixed `x,H`, and VIS-311 is a sufficient finite-window bound that still pays a uniform hard-tail cost and remains far from the natural local scale. No existing finding establishes a theorem-level implication from VIS-311 to Wang's `T^lambda L^2` error or to enlarged Fourier support.

This clue proposes an interface audit and possible transfer, not an improved short-interval pair-correlation theorem, not a larger simple-zero proportion, and not an RH implication.

## Research disposition

**Outcome: rejected.** Primary-source audit of Wang shows that Lemma 2.4 already contributes `O(xL^3)` when the interval-zero object `A_I` is replaced by the full explicit-formula object `A`, using only zero-window endpoint localization and before any mean-square estimate for the prime polynomial `D_x`. After `x=T^alpha` support integration this alone gives `O_g(T^lambda L^2)`. Hence improving coefficient-weighted finite-height/dephasing control on `D_x` by itself cannot relax the `lambda<theta` gate; a viable route must also sharpen or reorganize the zero-window truncation. See `[[../findings/WI-439-wang-endpoint-localization-already-forces-the-support-gap]]`.