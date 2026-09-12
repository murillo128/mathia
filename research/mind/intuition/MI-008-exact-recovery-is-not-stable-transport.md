# MI-008 — Exact recovery, timing provenance, and accumulated local loss are different resources

**Evidence level:** supported by the specified inverse, sampling, timing, and propagation models through AF-287 and PF-302; no common universal condition number or transport theorem is claimed.

Dirichlet acquisition separates phase fibers from coupling. AF-279--AF-281 classify one-lattice aliasing, failure of separate resonant marginals, and exact recovery from genuinely joint mixed samples. AF-282--AF-285 then price the known-prefix `log2/log3` repair: joint phase spacing is `Theta(1/N)`, stable mixed degree is `Theta(N)`, and raw acquisition can be reduced to `Theta(N)` observations.

AF-286 adds timing provenance. A common clock-origin offset factors exactly as a coefficient gauge `b -> D_tau b`; fixed relative coefficient distortion has the sharp calibration scale `Theta(1/log N)`. More observations cannot remove a gauge, so a downstream target invariant under this action needs a different accounting from full coefficient recovery.

AF-287 closes the apparent extra `sqrt(N)` cost for independent rowwise jitter. A bounded-condition unweighted `O(N)` raw subframe exists, and the exact operator expansion gives

\[
\|\widetilde A-A\|\le\|A\|\bigl(e^{T\log N}-1\bigr).
\]

Together with the common-offset subclass this yields the same sharp order

\[
T_{\rm independent\ jitter}(N)=\Theta(1/\log N).
\]

The previous stronger sufficient precision came from an `ell^1` detour and incomplete frame control, not an intrinsic information scale. The remaining timing question is therefore target-relative: which arithmetic/RH-facing functionals quotient the common clock gauge, and what changes for unknown support or infinite sources.

Prime Flute supplies a complementary repeated-loss phenomenon. PF-297--PF-301 identify the intrinsic seam measure and show that arbitrary bounded directional attenuation coefficients accumulate according to their actual `L^1` mass; coefficient oscillation is not a separate escape. PF-302 then proves that the **sum of the two directional scalar attenuation masses diverges**:

\[
\sum_n\left(\frac{\kappa_{n,L}}{c_n}+\frac{\kappa_{n,R}}{c_n}\right)=\infty,
\]

because it dominates `sum s_n/L_n`, whose partial sums grow at least like `log log p_M`. Hence the scalar round-trip product vanishes and at least one one-way scalar transmission is extinguished.

The cross-line lesson is structural, not numerical. **Classify the error or loss by the action it induces before assigning a budget.** A common-mode acquisition error can be an exact source symmetry; arbitrary rowwise jitter is an operator perturbation controlled by frame conditioning; repeated local losses are priced by an intrinsic accumulated measure. Once the correct category is used, apparent extra costs such as `sqrt(N)` jitter or arbitrary oscillatory attenuation may disappear, while a genuine global accumulation can remain.

**Boundary.** AF-287 is finite known-support and coefficient-`ell^2`; source constraints or different targets can change the timing bill. PF-302 concerns the scalar pant channel and only the combined bidirectional mass; it does not identify the killed orientation or prove that the complete `P/H` response factors through the scalar compression. Neither result transfers automatically to another measurement or global response category.