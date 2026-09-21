# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`, `MI-058-boundary-geometry-can-protect-anchored-fidelity-without-pairwise-fidelity`, `MI-059-source-point-cubes-block-stable-nonlinear-hilbert-recovery-unless-the-source-geometry-changes`, `MI-060-cube-poorness-does-not-certify-hilbert-fidelity`, `MI-061-square-root-tv-is-the-sharp-hilbert-snowflake-boundary`, `MI-062-scalar-hilbert-repair-has-square-root-and-bernstein-gates`, `MI-063-hard-support-is-a-scale-free-resource-soft-tails-are-not`, `MI-064-soft-sparse-hilbert-fidelity-has-a-sharp-tail-resolution-budget`, `MI-065-compressibility-profiles-turn-tail-decay-into-a-resolution-condition-curve`, `MI-066-realizable-tail-breadth-is-the-minimax-side-of-compressibility`, `MI-067-finite-affine-moment-side-information-only-thins-sparse-positive-fibers-at-support-scale`, `MI-068-one-crossing-secants-turn-bounded-jordan-support-into-scale-free-hilbert-fidelity`.

AF-451--AF-465 identify the source-law secant carrier and the category obstruction: large paired-mixture cubes force the sharp Hilbert `k^(-1/2)` loss even for nonlinear encoders with finite upper TV sensitivity, while boundary/anchored geometry can behave differently from moving pairwise secants and cube-poorness is not a positive recovery certificate.

AF-466--AF-471 classify the scalar radial repair branch on the unrestricted TV simplex. The square-root transform is the sharp small-scale boundary, full-diameter complete alternation is necessary, and on the physical diameter every smooth exact squared Hilbert transform is a positive mixture of overlap powers `1-(1-d/2)^n`.

AF-472 keeps the original TV metric and changes the source class. On the full `s`-sparse probability simplex the optimal Hilbert distortion is exactly `sqrt(s)`, attained by coordinate inclusion and forced by a paired-support Hamming cube. AF-473 shows why a fixed positive unrestricted tail destroys this scale-free escape, while AF-474 restores a finite-resolution estimate by coupling support budget, tail mass and the destination separation.

AF-475 packages a whole source compressibility law `tau_s<=phi(s)` into the achieved coordinate condition curve

`K_phi(delta)=inf_(s:2 phi(s)<delta) sqrt(s)/(1-2 phi(s)/delta)`.

AF-476 supplies the complementary nonlinear minimax obstruction for the full profile envelope. If

`N_phi(delta)=sup {k: phi(k)>=delta/2}`,

then the envelope contains a head-plus-private-tail Hamming cube of dimension `k` at source diameter `delta`, and every globally Lipschitz Hilbert encoding has resolution condition at least `sqrt(N_phi(delta))`. For two-sided polynomial or stretched-exponential profiles this matches the AF-475 order. The lower bound is not automatic for a narrower arithmetic subclass: it requires the corresponding independent tail breadth to be genuinely realizable there.

AF-477 closes one important realizability loophole for the full positive finite-moment model. If the retained source law consists of finitely many affine statistics of affine rank `d`, then an `r`-sparse moment fiber can contain an exact positive Hamming cube of dimension `floor(r/(d+1))`; for Hilbert targets its worst-fiber distortion is therefore at least the square root of that dimension. Finite affine side information by itself cannot make large-support moment fibers uniformly Hilbert-thin. Any thinner arithmetic class must exclude the independent Radon-block switches through additional source structure, or increase the retained affine rank on the support scale.

AF-478 shows the complementary positive mechanism: realizable secant sign geometry can be much thinner than ambient support or tail breadth suggests. If every oriented pairwise difference has one Jordan side supported on at most `N` atoms, coordinate inclusion has uniform TV-to-Hilbert condition `O(sqrt(N))`. Ordered Gibbs families have exactly this property because likelihood ratios are monotone in the energy order and pairwise differences have a single sign crossing. The mechanism is scale-free but source-generic: matched nonprime ordered Gibbs families satisfy the same bound, so it is not by itself a rational-prime discriminator.

The live arithmetic question is therefore about the **actual secant geometry** of the prime-derived class, not only an upper approximation envelope or ambient support complexity. Prove an upper approximation profile `phi_arith(s)`, determine how many independent source switches are genuinely realizable at the downstream separation, and test whether ordering/sign constraints reduce every admissible secant to a bounded or slowly growing Jordan-support side. If the class is described partly by finitely many moments, identify the additional arithmetic restriction that blocks the AF-477 Radon switches. Any favorable secant restriction must still retain a rational-prime discriminator; AF-478 shows that metric conditioning alone can be completely non-arithmetic.

## Keep identifiability, anchored provenance, pairwise stability and metric repair separate

Exact injectivity, atom separation, anchored discrimination, bounded-distortion metric repair and exact radial Hilbertization are different claims. AF-462--AF-465 separate anchored boundary geometry from pairwise source cubes; AF-466--AF-471 classify the unrestricted scalar-radial repair branch; AF-472--AF-478 separate hard-support fidelity, finite-resolution soft-tail upper bounds, realizable metric breadth, finite-moment fiber breadth, and bounded-Jordan-support secant geometry.

A fidelity theorem must therefore state the source metric, admissible comparison class, anchored versus pairwise quantifiers, target/operator category, upper sensitivity budget, exact versus bounded-distortion requirement, absolute resolution consumed downstream, and whether a claimed minimax obstruction or favorable secant restriction is realized inside the actual source subclass. The absence of a negative witness is not a positive theorem, an upper tail envelope is not a lower complexity certificate, finite moment data do not by themselves imply thin positive fibers, bounded secant Jordan support does not imply arithmetic discrimination, and an exact Hilbertization after metric deformation is not fidelity in the original TV scale.