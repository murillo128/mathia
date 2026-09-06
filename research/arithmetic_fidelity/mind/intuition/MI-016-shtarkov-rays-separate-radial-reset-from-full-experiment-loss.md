# MI-016 — Shtarkov likelihood rays separate radial recanonicalization from full experiment loss

**Evidence level:** exact finite/classical results through AF-154

## Core intuition

The Shtarkov center is best viewed as one normalization of the full likelihood geometry, not as the geometry itself. Compression conditionally averages max-normalized likelihood rays. Recomputing the Shtarkov center then performs only a radial renormalization of that barycenter, so center drift measures radial conflict while sufficiency can still fail tangentially along a face of the likelihood-ray sphere.

## Strongest justified principle

AF-151 identifies the exact reset density between the propagated source center and the recomputed center with normalized local conflict `kappa`. Mean conflict gives maximal-leakage loss, while total variation, chi-square, and stronger divergences require progressively stronger control of the conflict profile. AF-152 shows that along a chain, accumulated mismatch evolves by conditional averaging followed by a new reset rather than by pointwise multiplication of conflicts. AF-153 gives the complementary endpoint formula: each reset contributes only through covariance with the final discriminator transported backward through the suffix channel.

AF-154 exposes the underlying projective geometry. The max-normalized vector of all experiment likelihoods is a canonical likelihood-ray representative. Under compression its conditional mean is the retained ray vector; the local conflict factor is exactly the inverse radial norm of that mean. The Shtarkov-reference Pearson loss instead equals the full conditional squared dispersion of the rays and has exact zero set equal to sufficiency. Thus one may have perfect center commutation with nonzero tangential information loss.

## What remains possible

A source-specific arithmetic family may force its likelihood rays into a low-complexity region where radial conflict controls the full conditional variance, or may make only a target-relative projection of the loss relevant. Such implications must be proved from source structure. General finite experiments show that neither small leakage drop nor small center drift supplies them automatically.

## Status / novelty

Shtarkov/NML centers, likelihood-ratio sufficiency, conditional expectation, divergence data processing, and projective likelihood geometry are classical ingredients. The durable synthesis is: **canonical-center reset is one radial projection of a larger likelihood-ray information loss, and composable or endpoint-useful control must be calibrated to the full geometry actually consumed downstream**.

## Falsification criterion

Invalidate the exact reset-density, conditional-averaging, transported-covariance, or likelihood-ray variance identities; produce a finite experiment for which the Shtarkov Pearson loss vanishes without sufficiency; or prove from the current general hypotheses that radial conflict alone controls all tangential ray loss.
