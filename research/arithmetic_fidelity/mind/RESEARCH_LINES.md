# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate likelihood-ray geometry to the declared decision/recovery class and family complexity

**Linked intuitions:** `MI-015-whole-experiment-fidelity-needs-a-common-recovery-profile`, `MI-016-shtarkov-rays-separate-radial-reset-from-full-experiment-loss`, and `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-149--AF-154 identify the source-selected Shtarkov envelope, distinguish propagated from recomputed centers, and expose the full max-normalized likelihood-ray geometry. AF-155 gives the radial Shtarkov contraction an exact decision-theoretic meaning: it is the Bayes defect for one envelope-winner decision problem, while full ray variance is the squared-error risk for reconstructing the whole likelihood ray and has exact zero set equal to sufficiency.

AF-156 then closes a tempting approximate interpretation. In growing private-label experiments the true worst-case recovery deficiency can vanish, and every individual Shtarkov-reference Pearson certificate can vanish, while the radial and unnormalized whole-ray aggregate defects stay order one or tend to one. Exact-zero completeness therefore does not supply a dimension-free approximate recovery modulus. The live question is to derive a source-natural representation together with a **destination-calibrated aggregation whose constants remain controlled at the effective experiment complexity**.

## Propagate one source reference, but measure only the loss the endpoint can consume

A useful arithmetic certificate should keep one source-selected dominating reference through the compression chain while separately controlling the destination-relevant part of the loss. Local recanonicalization drift, full likelihood-ray dispersion, winner-label error, worst-case recovery deficiency, and endpoint transported covariance are different resources. A future theorem should state explicitly which decision class or discriminator is being preserved and prove the corresponding complexity-uniform transport modulus rather than infer it from a canonical center or exact sufficiency invariant.

## Classify retained interaction support before proposing repair

Linear span, sigma-algebra, interaction depth, family recovery, center reset, radial conflict, tangential likelihood-ray loss, endpoint observability, and family-size calibration are distinct information layers. Repairs should target the first layer that fails instead of treating one canonical center, divergence, or aggregate geometry as a complete fidelity metric.
