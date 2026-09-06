# MI-017 — Approximate recovery complexity is reference- and provenance-dependent

**Evidence level:** exact finite-experiment and decision-theoretic results through AF-162

## Core intuition

Exact sufficiency geometry still does not determine a canonical approximate metric, but the calibration boundary is now explicit. A propagated common-reference Pearson defect becomes quantitatively equivalent to optimal common recovery when the reference is automatically recoverable with the declared experiment and the family has controlled likelihood complexity relative to that reference.

AF-160 identifies that complexity exactly for the best barycentric reference. It is the unrestricted Shtarkov complexity multiplied by a one-sided convex-hull penalty: the order-infinity divergence from the Shtarkov center to the experiment convex hull. AF-161--AF-162 then show that the scaling of this source constant depends decisively on **how alternative identity propagates across observations**. Independent evidence is not itself the obstruction; independent recombination of the hidden alternative is.

## Strongest justified principle

AF-157 replaces list-dependent whole-ray aggregation by the convex-hull-invariant worst-member Shtarkov Pearson loss. AF-158 calibrates that loss to the Shtarkov-selected Bayes reverse but not automatically to the best common reverse. AF-159 supplies the missing bridge: for a barycentric reference `M` with likelihood ceiling `L_M`,

`4 delta_rec^2 <= Gamma_M <= L_M(L_M+2) delta_rec`.

AF-160 sharpens the source constant to

`Lambda_bar = C exp(d_infty(M_Sh, conv(E)))`.

Thus the extra price of insisting on an automatically recoverable reference is exactly the convex-hull distance of the Shtarkov center. There is no barycentric price precisely when the Shtarkov center is already a mixture of experiment members.

AF-161 proves exact multiplicativity for the full Cartesian product experiment. Consequently `Lambda_bar(E^{\otimes n})=Lambda_bar(E)^n`, so a nontrivial factor makes the whole-family calibration constant grow exponentially when each coordinate may choose its alternative independently.

AF-162 isolates the opposite regime. For the shared-identity family `(P_i^{\otimes n})_i`, repeated observations make the fixed alternatives distinguishable; `Lambda_bar` stays bounded by the number of alternatives and converges to that finite value, while the normalized convex-hull penalty tends to one. The durable structural distinction is therefore: **repeated evidence can improve identification without creating an exponential recovery penalty when relational provenance keeps one common alternative identity across coordinates.**

## What remains possible

A concrete arithmetic source may preserve one alternative identity across many scales, allow only constrained recombination, or require recovery of a destination-specific quotient rather than the full Cartesian family. Its useful complexity law may therefore be bounded, additive after logarithms, intermediate between the two exact controls, or irrelevant because the endpoint consumes a smaller witness class.

The remaining source question is not to invent another divergence with the same zero set. It is to specify the actual provenance/composition structure, choose a recoverable reference matched to the destination, and prove the resulting likelihood-complexity bound.

## Status / novelty

Sufficiency, Le Cam recovery, Pearson and Rényi divergences, Bayes reversal, Shtarkov/NML centers, barycentric mixtures, tensor products, and hypothesis-testing bounds are classical ingredients. The line-specific synthesis is the calibration law: **recoverable reference plus controlled likelihood complexity is sufficient, and whether that complexity multiplies or saturates is determined by the source's identity/provenance structure.**

## Falsification criterion

Find a finite experiment violating AF-159's two-sided recovery inequality for a barycentric dominating reference, invalidate AF-160's exact convex-hull decomposition, or construct a shared-identity tensor family for which `Lambda_bar` grows without the AF-162 finite bound. Any such example would break the claimed calibration/provenance mechanism.
