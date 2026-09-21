# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`, `MI-058-boundary-geometry-can-protect-anchored-fidelity-without-pairwise-fidelity`, `MI-059-source-point-cubes-block-stable-nonlinear-hilbert-recovery-unless-the-source-geometry-changes`, `MI-060-cube-poorness-does-not-certify-hilbert-fidelity`, `MI-061-square-root-tv-is-the-sharp-hilbert-snowflake-boundary`, `MI-062-scalar-hilbert-repair-has-square-root-and-bernstein-gates`.

AF-451--AF-465 identify the source-law secant carrier and the category obstruction: large paired-mixture cubes force the sharp Hilbert `k^(-1/2)` loss even for nonlinear encoders with finite upper TV sensitivity, while boundary/anchored geometry can behave differently from moving pairwise secants and cube-poorness is not a positive recovery certificate.

AF-466--AF-470 classify the obstruction side of scalar radial repair. The full TV simplex is Hilbertian after `d_TV -> sqrt(d_TV)`, `alpha=1/2` is the sharp power threshold, every complexity-independent scalar Hilbert repair must amplify small TV distances at least at square-root scale, and every exact squared radial law on the unrestricted simplex obeys full-diameter complete alternation.

AF-471 closes the remaining smooth radial sufficiency question on the compact TV diameter. A continuous `g:[0,2]->[0,infinity)`, smooth on `(0,2)`, is an exact squared Hilbert-distance transform on every finite family exactly when its derivatives alternate in sign, equivalently when

`g(t)=sum_(n>=1) a_n [1-(1-t/2)^n]`, `a_n>=0`.

The overlap powers give an explicit tensor-Hilbert realization. This bounded class is strictly larger than restrictions of global Bernstein functions, so extending the radial variable beyond the physical TV diameter is not a legitimate extra requirement.

The live arithmetic question is therefore source-structural and destination-relative, not another smooth scalar radial transform. If the physical source excludes the private-atom/weighted-hyperrectangle tests, identify the exact restriction that does so. Otherwise a useful escape must be non-radial/source-marked, or show that the final theorem genuinely benefits from the singular square-root metric deformation. Any such structure must remain source-forced and preserve the rational-prime discriminator through later quotient, spectral or compression maps.

## Keep identifiability, anchored provenance, pairwise stability and metric repair separate

Exact injectivity, atom separation, anchored discrimination, bounded-distortion metric repair and exact radial Hilbertization are different claims. AF-462--AF-465 separate anchored boundary geometry from pairwise source cubes; AF-466--AF-468 price bounded-distortion metric repair by singular small-scale sensitivity; AF-469--AF-471 completely classify the smooth exact radial branch on the full unrestricted TV diameter.

A fidelity theorem must therefore state the source metric, admissible comparison class, anchored versus pairwise quantifiers, target/operator category, upper sensitivity budget, exact versus bounded-distortion requirement, and the positive lower gain actually consumed downstream. The absence of a negative witness is not a positive theorem, and an exact Hilbertization after metric deformation is not fidelity in the original TV scale.