# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Classify source identity/provenance before demanding scalable whole-family recovery

**Linked intuitions:** `MI-015-whole-experiment-fidelity-needs-a-common-recovery-profile`, `MI-016-shtarkov-rays-separate-radial-reset-from-full-experiment-loss`, and `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-149--AF-159 separate exact sufficiency, Shtarkov radial decision loss, full likelihood-ray reconstruction, and optimal common recovery, then identify a sufficient calibration interface: a recoverable barycentric reference plus bounded likelihood domination makes propagated Pearson loss quantitatively equivalent to optimal Le Cam deficiency.

AF-160 now identifies the source constant exactly. The barycentric domination radius is the Shtarkov complexity multiplied by the directed order-infinity distance from the Shtarkov center to the experiment convex hull. AF-161--AF-162 show that its scaling is governed by **alternative provenance**, not merely by repeated observation. Full Cartesian product experiments tensorize the domination cost exactly and make it exponential for any nontrivial factor, whereas shared-identity repeated observations keep the cost uniformly bounded and drive the extra convex-hull penalty to zero.

The live arithmetic question is therefore to identify the actual source family and its provenance constraint before asking for a uniform recovery modulus. Does the same arithmetic alternative persist coherently across scales/coordinates, or may the hidden identity recombine independently? Prove the corresponding domination/decision-complexity law for that source rather than apply a worst-case Cartesian product bound by default.

## Propagate a recoverable reference, but measure only the loss the endpoint consumes

Reference choice and destination loss remain separate. Shtarkov is source-natural and minimax for envelope domination; barycentric references make common recovery visible. AF-160 shows exactly how much convex-hull access costs, while AF-161--AF-162 show that the cost can either multiply or saturate depending on source identity structure.

A useful theorem should state which reverse channel or decision class the endpoint consumes, select a reference whose recoverability matches that claim, and prove that its likelihood complexity remains controlled under the **actual** composition law. If full-family recovery is stronger than the destination needs, narrow the recovered family or witness class instead of treating exponential Cartesian complexity as intrinsic information loss.

## Classify retained interaction support before proposing repair

Linear span, sigma-algebra, interaction depth, family recovery, center reset, radial conflict, tangential likelihood-ray loss, endpoint observability, reference complexity, and identity provenance are distinct information layers. Repairs should target the first layer that fails instead of treating one canonical center, divergence, aggregate geometry, or generic tensor product as a complete fidelity metric.
