# MI-005 — Real scalar multiplicity is closed before the complex-height frontier

**Evidence level:** exact derived certificate and quantitative complex lift through ANF-082

## Core intuition

Multiplicity complexity on the real axis is no longer a surviving obstruction for the central-notch strategy. ANF-080 temporarily localized the hard scalar class to growing sorted-prefix variation, but ANF-081 shows that this was a proof-method boundary: clipping every occupancy to `1` or `2` and charging the discarded high part to the exact affine surplus closes the certificate for **all finite real multisets** with one fixed central notch.

The first remaining geometric frontier is therefore genuinely nonreal. ANF-082 shows that even this frontier does not begin infinitesimally close to the real boundary: for `p` nonreal conjugate pairs, the all-real certificate extends to an explicit height tube `|Im z|<=h_p` with `h_p asymp p^{-1/4}` under the elementary phase-blind estimate.

## Strongest justified principle

ANF-081 combines two exact regimes. When the affine integer surplus and Montgomery--Taylor excess are small, the high-occupancy remainder has small spectral mass and the clipped `1/2` configuration lies in a uniformly controlled bounded-variation class. In the complementary regime, the same surplus/excess pays for the crude spectral loss. The splice is uniform in support, multiplicity, and geometry, and the resulting normalization still strictly improves Montgomery--Taylor.

ANF-082 then collapses each nonreal pair to its real part and uses the real theorem as a Hilbert-norm floor. Moving the pairs vertically changes the structure factor by an explicitly bounded vector. Retaining part of the normalization margin gives a quantitative complex tube uniform in horizontal complexity and real multiplicity. The `p^{-1/4}` width comes from coherent worst-case addition of `p` pair perturbations against only a `sqrt p` affine norm floor; it is not claimed sharp.

Thus the durable boundary is stronger than “large weights are hard.” **Any counterexample to this fixed central-notch certificate must use genuinely nonreal geometry outside a quantitative boundary layer, not merely unbounded real occupancy or support.**

## What remains possible

The tube may widen if horizontal phases or pairwise Gram structure reduce the coherent `p` loss. A complementary large-height estimate could instead show that all counterexamples lie in a compact intermediate-height regime. Multi-pair interactions or a higher-order carrier may also become necessary if pairwise energy cannot control that region.

What is no longer justified is to spend research effort classifying finer real multiplicity profiles unless ANF-081 itself is falsified. Prefix variation, geometric-band count, and maximum occupancy have all been subsumed by the two-level clipping theorem.

## Status / novelty

The clipping inequalities, Hilbert-space estimates, and positive Fourier-energy tools are exact persisted mathematics built from classical mechanisms. The durable synthesis is the frontier relocation: **the scalar real-multiplicity branch is closed for the fixed central-notch family, and the first unresolved boundary is quantitative nonreal conjugation geometry.** No RH consequence or publication-level novelty claim follows from this synthesis.

## Falsification criterion

Exhibit a finite real multiset violating the ANF-081 affine certificate for its fixed spectrum; invalidate the clipping/surplus splice; or exhibit a conjugation-invariant configuration inside the ANF-082 height tube that violates its lifted certificate. Any such example would reopen the corresponding boundary.