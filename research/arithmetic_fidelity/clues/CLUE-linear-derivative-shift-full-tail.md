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
  - research/arithmetic_fidelity/findings/AF-434-full-column-saddle-does-not-transport-source-shell-index.md
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

AF-433 supplies the source-side correction. For

\[
h(x)=-\log\!\left(\frac{1-e^{-x}}x\right),
\]

the singularities lie at `2\pi i k`, so the source has the ordered shell radii

\[
r_m=2\pi m,\qquad m\ge1.
\]

Since `a=(c/2\pi)^2`, the source-attached shell family satisfies `c=r_m \iff a=m^2`. This makes the square family intrinsic to the source normalization, but does not by itself select one shell.

AF-434 now closes the proposed **shell/packet transfer mechanism negatively for the current determinant route**. The exact source expansion resolves each even coefficient as a sum over shell labels `j`, while the target packet index `r` is introduced later by the rectangular partition decomposition. For every fixed full-column packet, the source-shell zeta factor has zero contribution to the `n`-th-root saddle rate; the square law `L_r(b)=b^r/(r!)^2` is formed by packet combinatorics plus the scalar `b`. Even the first exact zeta prefactor is an aggregate over all source shells rather than a selector of shell `j=m`.

Thus the common integer in `c=r_m` and `a=m^2` is an exact coordinate correspondence, not a shell label transported through the present compression.

## Research question

Can the source analytic structure force a principled reciprocal-order probe, in particular the nearest-shell value `c=r_1=2\pi`, **before** target cancellation or exceptional-set membership is inspected?

AF-434 removes the previous alternative that the current determinant itself might transport the shell index into the packet index. A future shell-to-packet proposal would therefore need a genuinely enriched representation that carries shell-resolved provenance explicitly; it is no longer a live explanation of the existing AF-417--AF-432 formulas.

## Why it may matter

The source-selection issue is now isolated cleanly from the target saddle. AF-434 proves more than a notational distinction: the farther-shell contributions to coefficient order `2k` are exponentially suppressed relative to the nearest shell, so large-order source asymptotics intrinsically privilege `r_1=2\pi`. This supplies a real source-side reason to investigate nearest-shell selection.

It still does not prove that the probe family `x_n(c)=c/n` must take `c=2\pi`. All `c>0` remain analytically available, and choosing `2\pi` because it has desirable packet behavior would still reverse provenance. What is needed is an admissibility, extremality, minimality, or functoriality theorem formulated entirely on the source side.

## Decisive test

**Gate 0 — source admissibility.** Starting only from the intrinsic source analytic continuation and the reciprocal-order scaling problem, formulate an admissible class of probe selectors and determine whether nearest-shell selection

\[
S(h)=r_1=2\pi
\]

is forced, minimal, universal, or otherwise canonical inside that class. Similarity-equivariance alone is insufficient because every `\kappa R(h)` has that property. A successful criterion must distinguish the nearest singularity without inspecting downstream packet cancellation or exceptional membership.

**Gate 1 — current shell/packet transfer: closed negatively.** AF-434 shows that, in the present determinant/Cauchy--Binet mechanism, shell labels are aggregated inside the coefficient `\zeta(2k)` before packet labels are formed, and the fixed-packet zeta factor is subexponential at the saddle scale. Do not continue trying to explain `c=r_m \iff a=m^2` as transport through this mechanism. Reopen this gate only for a new construction that explicitly retains shell-resolved data.

**Gate 2 — pointwise target membership.** Only after Gate 0 supplies a source-selected probe should that fixed amplitude be tested against the exact critical or supercritical shrinking target. On the exact square family, AF-426 already closes complete adjacent-packet cancellation. For any other source-selected value, use the AF-425/AF-432 pointwise conditions rather than category or measure genericity.

**Gate 3 — next packet scale.** Only on a pointwise survivor derive the next uniform complete-packet correction. Do not spend beyond-all-orders effort before the provenance and pointwise gates survive.

## Evidence boundary

AF-433 proves that the full probe family remains free and identifies the source singularity-shell ladder. AF-434 proves that the existing square saddle does not transport that shell index: source-shell data are already aggregated at the coefficient layer, and the shell-sensitive zeta factors do not control the fixed-packet exponential saddle rate.

Neither result proves that `c=2\pi` is the unique admissible probe. AF-434 also does not rule out a different representation that carries shell marks explicitly, nor does it say that all aggregate shell information disappears from exact prefactors.

A new cross-line arithmetic construction may supply a selector. If it does, its provenance must be established independently before this clue treats the resulting amplitude as distinguished.

## Research disposition

Accepted. **The sole live branch of this clue is now source-side probe admissibility.** Investigate whether nearest-shell dominance can be upgraded to a canonical selector theorem for `c=2\pi` (or to a sharply characterized source-defined admissible family). Do not continue exceptional-set analysis for freely chosen amplitudes, and do not pursue the existing shell/packet index coincidence as a transport mechanism after AF-434.