# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`, `MI-058-boundary-geometry-can-protect-anchored-fidelity-without-pairwise-fidelity`, `MI-059-source-point-cubes-block-stable-nonlinear-hilbert-recovery-unless-the-source-geometry-changes`, `MI-060-cube-poorness-does-not-certify-hilbert-fidelity`, `MI-061-square-root-tv-is-the-sharp-hilbert-snowflake-boundary`, `MI-062-scalar-hilbert-repair-has-square-root-and-bernstein-gates`.

AF-451--AF-465 identify the source-law secant carrier and the category obstruction: large paired-mixture cubes force the sharp Hilbert `k^(-1/2)` loss even for nonlinear encoders with finite upper TV sensitivity, while boundary/anchored geometry can behave differently from moving pairwise secants and cube-poorness is not a positive recovery certificate.

AF-466--AF-467 classify the power-metric escape. The full TV simplex is Hilbertian after `d_TV -> sqrt(d_TV)`, and `alpha=1/2` is the sharp power-snowflake threshold. AF-468 removes the power-family loophole: every scalar transform supporting complexity-independent Hilbert distortion on unrestricted mixtures must amplify small TV distances at least at square-root scale. A locally TV-Lipschitz scalar repair is therefore impossible.

AF-469 adds the exactness gate. If `g(d_TV)` is itself a squared Hilbert distance on every finite subset, then below half the source diameter `g` obeys the Bernstein alternating finite-difference laws; in the smooth case `g'` is completely monotone. Thus the remaining scalar-radial freedom is much narrower than the square-root lower-scale condition alone.

The live arithmetic question is now source-structural and destination-relative. Does the physical arithmetic source exclude the growing weighted cube/hyperrectangle configurations that force these laws? If not, can the final theorem genuinely consume a singularly expanded metric, or must the representation become non-radial/state-dependent? Any claimed escape has to preserve the rational-prime discriminator through every later quotient, spectral operation or compression rather than merely make the transport geometry Hilbertian.

## Keep identifiability, anchored provenance, pairwise stability and metric repair separate

Exact injectivity, atom separation, anchored discrimination, bounded-distortion metric repair and exact radial Hilbertization are different claims. AF-462--AF-465 separate anchored boundary geometry from pairwise source cubes; AF-466--AF-468 show that changing the metric can repair Hilbert geometry only by paying singular small-scale sensitivity; AF-469 shows that exact radial repair additionally inherits complete-alternation constraints.

A fidelity theorem must therefore state the source metric, admissible comparison class, anchored versus pairwise quantifiers, target/operator category, upper sensitivity budget, exact versus bounded-distortion requirement, and the positive lower gain actually consumed downstream. The absence of a negative witness is not a positive theorem, and a successful metric deformation is not fidelity in the original TV scale.