# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`, `MI-058-boundary-geometry-can-protect-anchored-fidelity-without-pairwise-fidelity`, `MI-059-source-point-cubes-block-stable-nonlinear-hilbert-recovery-unless-the-source-geometry-changes`, `MI-060-cube-poorness-does-not-certify-hilbert-fidelity`, `MI-061-square-root-tv-is-the-sharp-hilbert-snowflake-boundary`, `MI-062-scalar-hilbert-repair-has-square-root-and-bernstein-gates`, `MI-063-hard-support-is-a-scale-free-resource-soft-tails-are-not`, `MI-064-soft-sparse-hilbert-fidelity-has-a-sharp-tail-resolution-budget`, `MI-065-compressibility-profiles-turn-tail-decay-into-a-resolution-condition-curve`.

AF-451--AF-465 identify the source-law secant carrier and the category obstruction: large paired-mixture cubes force the sharp Hilbert `k^(-1/2)` loss even for nonlinear encoders with finite upper TV sensitivity, while boundary/anchored geometry can behave differently from moving pairwise secants and cube-poorness is not a positive recovery certificate.

AF-466--AF-471 classify the scalar radial repair branch on the unrestricted TV simplex. The square-root transform is the sharp small-scale boundary, full-diameter complete alternation is necessary, and on the physical diameter every smooth exact squared Hilbert transform is a positive mixture of overlap powers `1-(1-d/2)^n`.

AF-472 instead keeps the original TV metric and changes the source class. On the full `s`-sparse probability simplex the optimal Hilbert distortion is exactly `sqrt(s)`, attained by the coordinate inclusion and forced by a paired-support Hamming cube. A fixed hard support cap is therefore a genuine positive source-geometry certificate with a sharp complexity price.

AF-473 shows that this source escape is singular for scale-free multiplicative fidelity. If any fixed positive mass `epsilon` may live in an unrestricted tail, the `s=1` soft-sparse class already contains arbitrarily high-dimensional Hamming cubes at scale `O(epsilon)`, so its Hilbert distortion is infinite on an infinite alphabet. Small tail amplitude does not control the number of independent source directions hidden in that tail.

AF-474 supplies the positive scale-aware counterpart. If `tau_s(mu)` is the best `s`-term tail mass, the coordinate Hilbert map satisfies an additive inverse estimate with error `tau_s(mu)+tau_s(nu)`. On `tau_s<=epsilon`, source pairs separated by `delta>2epsilon` have distortion at most `sqrt(s)/(1-2epsilon/delta)`.

AF-475 packages a whole source compressibility law `tau_s<=phi(s)` into the achieved condition curve

`K_phi(delta)=inf_(s:2 phi(s)<delta) sqrt(s)/(1-2 phi(s)/delta)`.

Polynomial tails `phi(s)<=A s^(-alpha)` therefore give coordinate conditioning `O((A/delta)^(1/(2alpha)))`, while stretched-exponential tails give a polylogarithmic loss. Approximate sparsity is useful only after source approximation rate and destination resolution are coupled quantitatively.

The live arithmetic question is now concrete: prove or bound the actual prime-derived profile `phi_arith(s)`, identify the smallest source separation `delta_arith` genuinely consumed by the downstream zero/sign/rigidity mechanism, and test whether `K_(phi_arith)(delta_arith)` is useful while the retained coordinates still carry a rational-prime discriminator. A generic concentration statement is insufficient, and a different embedding may outperform the coordinate bound only if supported by additional source geometry.

## Keep identifiability, anchored provenance, pairwise stability and metric repair separate

Exact injectivity, atom separation, anchored discrimination, bounded-distortion metric repair and exact radial Hilbertization are different claims. AF-462--AF-465 separate anchored boundary geometry from pairwise source cubes; AF-466--AF-471 classify the unrestricted scalar-radial repair branch; AF-472--AF-475 separate scale-free hard-support fidelity from soft-tail fidelity whose cost depends on the full approximation profile and the declared destination resolution.

A fidelity theorem must therefore state the source metric, admissible comparison class, anchored versus pairwise quantifiers, target/operator category, upper sensitivity budget, exact versus bounded-distortion requirement, and the absolute resolution actually consumed downstream. The absence of a negative witness is not a positive theorem, a small tail is not a small structural budget, and an exact Hilbertization after metric deformation is not fidelity in the original TV scale.