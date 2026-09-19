---
id: CLUE-linear-derivative-shift-full-tail
type: research-clue
status: accepted
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md
  - research/arithmetic_fidelity/findings/AF-421-finite-critical-windows-reduce-to-full-column-saddle-hierarchy.md
  - research/arithmetic_fidelity/findings/AF-425-second-order-square-packet-detuning-exposes-source-lattice.md
  - research/arithmetic_fidelity/findings/AF-426-exact-square-amplitude-has-irreducible-integer-source-packet-gap.md
  - research/arithmetic_fidelity/findings/AF-427-displaced-square-packet-cancellation-is-metrically-exceptional.md
  - research/arithmetic_fidelity/findings/AF-428-second-order-exceptional-amplitudes-are-residual-but-null.md
  - research/arithmetic_fidelity/findings/AF-429-supercritical-full-column-saddle-has-shrinking-integer-window.md
  - research/arithmetic_fidelity/findings/AF-430-supercritical-residual-packets-preserve-shrinking-saddle-window.md
  - research/arithmetic_fidelity/findings/AF-431-constant-rational-supercritical-sources-hit-first-saddle-window.md
  - research/arithmetic_fidelity/findings/AF-432-supercritical-packet-center-amplitudes-are-residual-but-metrically-thin.md
  - research/arithmetic_fidelity/findings/AF-433-free-left-tail-amplitude-is-not-a-source-discriminator.md
---

# Linear derivative-shift full-tail resummation

## Observation

AF-417--AF-432 reduce the left-tail derivative-shift hierarchy to increasingly fine integer-source and packet-balance conditions. In the critical regime the decisive coordinate is

\[
a=\frac{c^2}{4\pi^2},
\qquad
b_n=a n^{s_n/n-2},
\]

with square transitions `b=m^2`. AF-426 excludes exact square amplitude at the complete adjacent-packet scale. AF-427--AF-428 show that displaced critical amplitudes with infinitely many second-order hits form a set that is simultaneously residual and Lebesgue-null. For rational supercritical density `q>2`, AF-429--AF-432 refine the target to a shrinking packet-corrected integer window and again obtain a residual but metrically thin amplitude set.

AF-433 originally exposed a more basic provenance gate: the reciprocal-order path `x_n(c)=c/n` is available for every `c>0`, so exceptional-set membership for an arbitrarily chosen amplitude is not a source discriminator.

The corrected AF-433 now sharpens that conclusion. For

\[
h(x)=-\log\!\left(\frac{1-e^{-x}}x\right),
\]

the source has singularities at `2\pi i k`, hence the intrinsic ordered shell radii

\[
r_m=2\pi m,\qquad m\ge1.
\]

Since `a=(c/2\pi)^2`, the target square amplitudes satisfy

\[
a=m^2\iff c=r_m.
\]

Thus square amplitudes are not purely downstream-tuned values: they coincide exactly with a canonical source-attached shell family. What remains unresolved is stronger and cleaner: the source does not yet force **which shell**, or prove that the shell/packet index coincidence is more than a normalization identity.

## Research question

Can the source singularity structure select one admissible reciprocal-order probe, or otherwise turn the exact shell/packet index matching into a genuine transfer mechanism, **before** desired cancellation or exceptional-set membership is inspected?

There are now two distinct possibilities worth separating:

1. a principled admissibility/minimality theorem selects the nearest singularity shell `c=r_1=2\pi` (or another uniquely characterized shell) independently of the target; or
2. no unique shell is selected, but the whole source ladder `r_m` maps canonically to the target square-transition ladder and a theorem explains why the same index `m` governs both structures.

Either would be stronger than arbitrarily choosing `c`; neither follows merely from the identity `a=(c/2\pi)^2`.

## Why it may matter

The previous version of this clue treated `c=2\pi m` as merely convenient unless an independent source theorem selected it. AF-433 now supplies an independent source interpretation for the entire family: `2\pi m` is the modulus of the `m`-th singularity shell. This makes AF-426's exact-square obstruction source-relevant rather than purely target-conditioned.

At the same time, the correction does not solve the original discriminator problem. The continuum `c>0` remains admissible, and even restricting attention to the singularity ladder leaves infinitely many source-attached scales. Chasing whichever `m` has favorable target behavior would still reverse the provenance direction.

The nearest shell `r_1` is special because it is the unique radius of convergence, so `c=2\pi` is now a serious source-defined candidate rather than a numerically convenient choice. But accepting it as the uniquely relevant probe requires a mathematical criterion saying why nearest-singularity selection is the admissible operation for this compression problem.

## Decisive test

**Gate 0 — source admissibility.** Starting from the intrinsic source analytic continuation, formulate an admissible class of probe selectors and determine whether nearest-shell selection

\[
S(h)=r_1=2\pi
\]

is forced, minimal, universal, or otherwise canonical inside that class. Similarity-equivariance alone is insufficient, because every `\kappa R(h)` has that property. If no unique selector exists, characterize the strongest source-defined family that survives; AF-433 now proves that `{r_m}` is one such family.

**Gate 1 — shell/packet transfer.** Determine whether the equivalence

\[
c=r_m\iff a=m^2
\]

can be derived as a structural source-to-target mechanism rather than by substituting the normalized coordinate into AF-421's square saddle law. A positive result should identify a source quantity indexed by the singularity shell whose transport through the determinant/compression produces the adjacent-packet index. A negative result should show that the common integer label is exhausted by coordinate normalization.

**Gate 2 — pointwise target membership.** Only after Gate 0 or Gate 1 supplies genuine provenance should a fixed source-attached amplitude be tested against the exact critical or supercritical shrinking target. On the exact square family, AF-426 already closes complete adjacent-packet cancellation. For any other surviving source-selected value, use the AF-425/AF-432 pointwise conditions rather than category or measure genericity.

**Gate 3 — next packet scale.** Only on a pointwise survivor derive the next uniform complete-packet correction. Do not spend beyond-all-orders effort before the provenance and pointwise gates survive.

## Evidence boundary

AF-433 proves that the full probe family remains free and that exceptional-set membership alone is not a source statement. It now also proves that the source analytic continuation supplies the singularity-shell ladder `r_m=2\pi m`, which maps exactly to the square amplitudes `m^2`.

It does **not** prove that one shell is uniquely admissible, that the source must use the nearest shell, or that the shared index `m` reflects a causal transfer rather than an exact coordinate coincidence. AF-426 remains a valid negative theorem on every exact square fiber.

A new cross-line arithmetic construction may also supply a selector. If it does, its provenance must be established independently before this clue treats the resulting amplitude as distinguished.

## Research disposition

Accepted. The live owner question is now **source-shell admissibility and shell/packet transfer before Diophantine membership**. Do not continue exceptional-set analysis for an arbitrarily chosen amplitude. First determine whether the source forces a shell rule or whether the exact singularity-shell / square-packet index matching carries additional structure. Only then test the surviving fixed amplitude or family against AF-426/AF-432.