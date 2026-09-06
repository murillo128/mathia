# MI-015 — Whole-experiment fidelity needs one common recovery profile, with a separate calibration gate

**Evidence level:** exact finite/classical results through AF-148

## Core intuition

The right experiment-level object is one reverse channel shared by the whole family. But correctness/composition of that channel and numerical calibration of a divergence certificate are independent gates: an optimal reverse map can coexist with a raw common-reference loss that worsens with family complexity.

## Strongest justified principle

AF-142--AF-144 separate local/pairwise fidelity from common recovery. AF-145 proves that coherently propagated references make Bayes reverse kernels compose and chi-square losses telescope. AF-146--AF-147 show linear and logarithmic family-size dilution for Pearson and KL on the same private-label experiment.

AF-148 unifies those examples. For every Csiszar `f`-divergence, the optimized common-reference loss on the private-label collapse is exactly the AF-050 reverse-support penalty. Its ratio to exact recovery deficiency is uniformly bounded in family size precisely when the endpoint diameter `f(0)+f_infinity` is finite; infinite endpoint diameter permits vanishing recovery defect with order-one or infinite loss. This classification is a calibration theorem for the adversarial family, not a generic reverse-kernel theorem.

## What remains possible

Source-natural arithmetic families may have bounded effective complexity or a canonical reference that gives sharper calibration. Another profile may also combine explicit recovery construction with finite-diameter robustness. Those properties must be derived from source structure.

## Status / novelty

The statistical ingredients are classical. The durable synthesis is: **common recovery is the composable information object; divergence endpoint geometry governs a distinct certificate-calibration problem**.

## Falsification criterion

Invalidate AF-145's composition, AF-148's private-label `f`-divergence formula/endpoint classification, or derive a dimension-free converse for an infinite-endpoint profile under only the stated private-label hypotheses.