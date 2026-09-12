# MI-008 — Exact recovery, target quotient, timing provenance, and accumulated local loss are different resources

**Evidence level:** supported by the specified inverse, sampling, timing, and propagation models through AF-288 and PF-302; no common universal condition number or transport theorem is claimed.

Dirichlet acquisition separates phase fibers from coupling. AF-279--AF-281 classify one-lattice aliasing, failure of separate resonant marginals, and exact recovery from genuinely joint mixed samples. AF-282--AF-285 then price the known-prefix `log2/log3` repair: joint phase spacing is `Theta(1/N)`, stable mixed degree is `Theta(N)`, and raw acquisition can be reduced to `Theta(N)` observations.

AF-286--AF-287 add timing provenance. A common clock-origin offset factors exactly as a coefficient gauge `b -> D_tau b`, while independent rowwise jitter is a genuine operator perturbation. A bounded-condition unweighted `O(N)` raw subframe removes the apparent extra `sqrt(N)` penalty, leaving the same sharp coefficient-recovery scale

\[
T_{\rm coefficient}(N)=\Theta(1/\log N)
\]

for arbitrary rowwise jitter and the common-offset subclass.

AF-288 shows that this coefficient scale is not automatically a target scale. The common gauge is vertical translation of the Dirichlet series,

\[
F(s)\mapsto F(s+i\tau),
\]

so it preserves every zero real part and therefore the RH yes/no predicate. For horizontal zero geometry, the clock origin should be quotiented rather than reconstructed. The same nuisance parameter can also be removed from the source side: two known nonzero coefficient phases at multiplicatively independent indices, such as zeta's `2` and `3`, determine `tau` exactly. Yet exact anchoring is not globally stable over an unbounded clock range because irrational torus recurrence produces arbitrarily remote near-returns. Thus **coefficient recovery, source identifiability, robust calibration, and target sufficiency are four different questions**.

Prime Flute supplies a complementary repeated-loss phenomenon. PF-297--PF-301 identify the intrinsic seam measure and show that arbitrary bounded directional attenuation coefficients accumulate according to their actual `L^1` mass; coefficient oscillation is not a separate escape. PF-302 then proves that the **sum of the two directional scalar attenuation masses diverges**:

\[
\sum_n\left(\frac{\kappa_{n,L}}{c_n}+\frac{\kappa_{n,R}}{c_n}\right)=\infty,
\]

because it dominates `sum s_n/L_n`, whose partial sums grow at least like `log log p_M`. Hence the scalar round-trip product vanishes and at least one one-way scalar transmission is extinguished.

The cross-line lesson is structural, not numerical. **Classify the transformation by the action it induces and the target it must preserve before assigning a budget.** A common-mode acquisition error may be an exact source symmetry and free after quotienting the target; source provenance may pin it exactly without making the inverse globally robust; independent jitter is controlled by frame conditioning; repeated local losses are priced by an intrinsic accumulated measure. Apparent costs can disappear when they belong to the wrong quotient, while genuine accumulated loss can remain.

**Boundary.** AF-287 is finite known-support and coefficient-`ell^2`; AF-288's RH statement concerns horizontal zero geometry under exact common vertical translation and does not make fixed zero ordinates or independent jitter invariant. PF-302 concerns the scalar pant channel and only the combined bidirectional mass; it does not identify the killed orientation or prove that the complete `P/H` response factors through the scalar compression. Neither result transfers automatically to another measurement or global response category.