---
id: CLUE-weil-inertia-kernel-constrained-positive-cover-escape
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/clues/CLUE-four-point-weighted-cover-assembly.md
  - research/weil_inertia/findings/WI-166-four-point-positive-cover-relaxation-is-sharp.md
  - research/weil_inertia/findings/WI-171-four-point-saturation-witness-is-uniformly-gram-realizable.md
  - research/weil_inertia/findings/WI-172-c2330-four-point-candidate-awaits-kernel-check.md
  - research/weil_inertia/findings/WI-174-fixed-p2500-four-point-constant-is-below-2343e-6.md
  - research/weil_inertia/findings/WI-175-linear-gap-pressure-reweighting-is-periodic-witness-cancelled.md
  - research/weil_inertia/findings/WI-176-scalar-local-pressure-is-periodic-witness-cancelled.md
---

# Can a source-constrained cover evade the sharp positive-cover relaxation?

## Observation

WI-166 closes the arbitrary nonnegative pair-weight/gap relaxation behind the four-point positive-cover program: coefficientwise pair-energy domination admits an exact witness that makes the relaxation sharp. WI-171 closes the most immediate generic-matrix escape: that exact pair-weight witness is realized by uniformly well-conditioned positive-definite Toeplitz Gram matrices, so PSD, principal-minor, determinant, interlacing, conditioning, and generic stationary-Gram constraints alone do not exclude it.

WI-172 now closes the first bounded source-specific test **positively**. The preserved `teal-sea/zeta-lab` certificate for the genuine Montgomery--Taylor four-point functional at

\[
c=\frac{2330}{10^6},\qquad p=2500
\]

has completed independent kernel replay in its frozen environment, and Research Watch has rechecked its correspondence to the actual MT kernel, ordered additive gaps, pressure ledger and simple-critical-zero bridge. At the corrected admissible `m=432` it gives the exact theorem-level proportion

\[
0.6728603588388666595\ldots,
\]

strictly above WI-036's `0.6728529301211843197...`.

Therefore the actual source coupling does force at least one strict surplus over the WI-166 saturation resource. The open question is no longer whether *any* source-specific escape exists; it is how large and how global that escape can be.

WI-174 now closes one tempting way of enlarging that surplus. At the explicit rational MT gap triple

\[
\left(\frac{1047}{1000},\frac{1981}{1000},\frac{1047}{1000}\right)
\]

an independent interval evaluation gives `F_{4,2500}<2343/10^6`. Since WI-172 already proves `F_{4,2500}>=2330/10^6`, less than `13e-6` of local constant remains in this exact fixed-`p=2500` functional. After optimizing the corrected bridge over every admissible integer block size, merely raising this same constant can improve the certified proportion by less than `8.64943e-6`, with absolute bridge output strictly below

\[
0.6728690082686776504\ldots .
\]

WI-175 closes a broader pressure-only escape inside the same scalar shifted-block architecture. For an arbitrary fixed nonnegative linear gap pressure

\[
P_\alpha(g)=\sum_j\alpha_jg_j,
\qquad A=\sum_j\alpha_j,
\]

the interval-certified period-33 witness from WI-019 averages every relative gap position to `1/r`. Hence its mean local pressure is exactly `A/r`, while the scalar global bridge spends the same total coefficient `A`. The pressure cancels identically in the witness comparison, and every such single-MT-profile scalar assembly remains below `0.673604`. Thus merely redistributing or retuning a fixed linear pressure vector is not a genuinely new architecture.

WI-176 removes the apparent nonlinear loophole. Let `P(B)` be any translation-covariant scalar block potential, including an arbitrary nonlinear function of several gaps or a source-conditioned function of the MT kernel values on the same block. If the global proof ultimately compresses `P` to one universal scalar tax `tau`, then the period-33 phase measure forces that tax to pay at least `r` times the witness's own phase-average `P`, while the same phase average upper-bounds the universal local floor. The two appearances cancel algebraically exactly as in WI-175, again forcing the final scalar assembly below `0.673604`. Thus **nonlinearity or source conditioning is not itself an escape if it is scalarized globally**.

So further constant squeezing at fixed `p=2500`, linear pressure-vector retuning, or replacement by a more elaborate scalar local pressure with the same universal scalar-tax assembly is no longer a priority. A material source-specific gain must change the source profile/window, retain genuinely joint placement/state information as a non-scalar global object, add independent source observables, use a zeta-specific global constraint that actually excludes the period-33 witness, or couple to the exceptional block.

## Research question

How much strict surplus is forced by the actual source coupling

\[
w_{ij}=|K_{\rm MT}(y_j-y_i)|^2
\]

together with ordered additive gap geometry and the common span-pressure ledger, once one moves beyond the checked four-point floor and beyond all local pressure information that is eventually collapsed to one universal scalar tax? In particular, is there a source-realizable periodic or aperiodic family that asymptotically approaches the relaxed WI-166 resource, or does kernel/additive-gap compatibility force a quantitative extensive gap that survives a genuinely **non-scalar** global assembly?

## Why it may matter

The first source-aware test has succeeded without any new prime-side moment: the same support-one arithmetic can distinguish the true MT functional from the sharp arbitrary-weight relaxation. This identifies genuine mathematical information that WI-166 and WI-171 deliberately discard.

A uniform extensive source gap would create additional certified simple-critical mass within the current arithmetic interface. A source-realizable near-saturating family would instead close this refinement direction and redirect attention toward independent profiles, the exceptional indefinite block, or stronger arithmetic observables. WI-175 and WI-176 make the test sharper: any claimed gain coming only from the shape of a scalar local pressure must already fail on the period-33 phase average whenever its global accounting is one universal scalar tax. The surviving mechanism has to retain information that this scalarization destroys.

## Decisive test

Do not repeat the `c=2330/10^6` verification, spend effort tightening only the same `p=2500` four-point minimum, retune only a fixed nonnegative linear gap-pressure vector, replace it by an arbitrary nonlinear/source-conditioned scalar local pressure while keeping a universal scalar tax, or relax the kernel values back to arbitrary nonnegative pair weights. Preserve from the start the common variables

\[
x,\ y,\ z,\ldots
\]

that simultaneously determine every MT pair value and carry their source/state information through the global deduction without collapsing it to one number.

The next bounded test should characterize the actual MT-constrained local/periodic infimum beyond the fixed-`p=2500` constant-squeezing and scalar-pressure-cancellation routes. Preferred architectures are: a changed source profile; a vector/state-resolved potential with global accounting that preserves several components; an overlapping PSD/source certificate whose gain is not representable as `D+P` followed by one scalar tax; or a global source-placement problem with a zeta-specific admissibility constraint that the WI-019 period-33 measure cannot satisfy. A successful positive route must produce an exact lower resource materially stronger than the checked `2330/10^6` floor and show why its non-scalar information survives legitimate global accounting. A negative route should give an explicit source-realizable periodic/aperiodic family whose true MT kernel values approach the relaxed saturation resource closely enough to cap that richer object.

Generic PSD, Toeplitz, determinant, principal-minor, interlacing, or conditioning constraints are not valid decisive tests: WI-171 already supplies them for the relaxed witness.

## Evidence boundary

WI-172 establishes only a fixed four-point source surplus and its strict certified-proportion improvement. WI-174 additionally caps how much can be recovered by tightening the local constant of that exact `p=2500` functional. WI-175 caps every fixed nonnegative linear gap-pressure reweighting that retains the same single-profile scalar shifted-block assembly. WI-176 further caps arbitrary nonlinear/source-conditioned scalar local potentials whenever their global ledger is a universal scalar tax valid on the period-33 witness class. None of these results determines the optimal MT-constrained cover, excludes a genuinely non-scalar source assembly, identifies the exceptional complement, or implies RH.

The canonical objective remains individual off-line-zero coercivity and defect elimination. Further proportion improvement is useful here only insofar as it reveals source information that can later interact with the exceptional block or expose a genuinely stronger invariant.

## Research disposition

Accepted and **advanced past the formal-replay, fixed-pressure constant-squeezing, and scalar-pressure gates**. The finite source-specific escape is established by WI-172; WI-174 shows that proving a slightly larger constant for the same `p=2500` local functional has less than `8.65e-6` theorem-level payoff left; WI-175 closes arbitrary fixed nonnegative linear pressure reweighting; WI-176 shows that arbitrary nonlinear/source-conditioned local scalar pressure also cancels if the global proof remembers it only through one universal scalar tax. Continued work is restricted to a genuinely changed source-aware architecture that preserves non-scalar state/source information or introduces an admissibility constraint that excludes the periodic witness. No further candidate-status work on the already checked `c=2330/10^6` artifact is needed.