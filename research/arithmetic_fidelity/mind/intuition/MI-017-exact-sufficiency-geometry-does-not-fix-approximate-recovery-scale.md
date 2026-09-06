# MI-017 — Approximate recovery needs a recoverable reference and bounded likelihood complexity

**Evidence level:** exact finite-experiment and decision-theoretic results through AF-159

## Core intuition

Exact sufficiency geometry still does not determine a canonical approximate metric, but the missing calibration is now much sharper. A propagated common-reference Pearson defect becomes quantitatively equivalent to optimal common recovery once two conditions hold together: the reference is itself recoverable whenever the declared experiment is recoverable, and the family has uniformly bounded likelihood complexity relative to that reference.

Barycentric references provide exactly the first property. If `M` lies in the convex hull of the experiment members, every common approximate reverse that recovers those members also recovers `M`. A bounded domination radius then turns continuity of Pearson divergence into a two-sided modulus for the optimal Le Cam recovery deficiency.

## Strongest justified principle

AF-157 replaces list-dependent whole-ray aggregation by the convex-hull-invariant worst-member Shtarkov Pearson loss. It is an exact operator witness norm, has the right zero set, and lower-bounds optimal recovery deficiency. AF-158 shows that this same loss is two-sided calibrated to the Bayes reverse selected by the Shtarkov reference, with a source-complexity factor; it is not in general calibrated to the best common reverse.

AF-159 identifies the missing bridge. For a barycentric reference `M` with likelihood ceiling `L_M`,

`4 delta_rec^2 <= Gamma_M <= L_M(L_M+2) delta_rec`.

The source-only barycentric domination radius `Lambda_bar` is convex-hull invariant and selects the best universal constant available inside the class of automatically recoverable references. Thus there is a real tradeoff between unrestricted domination optimization, exemplified by Shtarkov, and reference recoverability, guaranteed by barycentricity.

The durable principle is therefore: **approximate fidelity is calibrated to the destination only after the reference-selection rule and its effective likelihood complexity are jointly controlled.** Exact-zero sufficiency alone remains insufficient, but the obstruction is no longer an unspecified family-size effect.

## What remains possible

A concrete arithmetic source family may have a uniformly bounded or slowly growing `Lambda_bar`, a canonical barycentric reference with better structure than the worst finite bound, or a destination decision class requiring less than full recovery. Conversely, an unrestricted source-optimal reference may remain preferable when the intended endpoint consumes its own Bayes reverse rather than optimal Le Cam recovery.

The remaining source question is not to find another divergence with the same zero set. It is to prove the reference recoverability and complexity bound appropriate to the actual arithmetic family and destination claim.

## Status / novelty

Sufficiency, Le Cam recovery, Pearson divergence, Bayes reversal, barycentric mixtures, and domination radii are classical ingredients. The line-specific synthesis is the calibration boundary: **recoverable reference plus bounded likelihood complexity is sufficient for a source-side divergence loss to track optimal recovery.**

## Falsification criterion

Find a finite experiment and barycentric dominating reference satisfying the stated likelihood ceiling for which AF-159's two-sided recovery inequality fails, or exhibit a sequence with uniformly bounded barycentric domination radius where Pearson loss and optimal deficiency have different zero asymptotics. Such an example would invalidate the claimed calibration mechanism.
