# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Declare quotient, source complexity, localization, observation algebra, bandwidth, and profile scale together

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-194 show that exact sufficiency and stable inversion are different questions. Adaptive positive source clusters can remain exactly separated while derivative-limited observations become super-algebraically close, the Euler harmonic ladder restores visibility when enough bandwidth is resolved, and finite-overlap/theta and saddle descriptions agree only at approximation strengths selected by their correction parameters.

AF-195--AF-200 identify the source-side geometry behind the remaining escape. Minimal-support moment-flat controls are Peano B-spline carriers, and even at fixed positive `W_1`, fixed quartic cancellation order, minimal five-node support, and a fixed finite Euler band, the carrier can drift into an observation-insensitive region while the discrepancy tends to zero. Source transport distance does not imply carrier localization.

AF-201--AF-204 now make that localization gate quantitative for the quartic five-node Euler model. For bounded profile `Q`, weak Peano-carrier concentration is the exact fixed-band topology. With varying `Q`, the full complex Euler-band discrepancy is two-sided comparable to the **profile-weighted real-axis localization defect** `Q Lambda_sigma(beta)`. In the five-node minimal-support class this is equivalent to the source-side gate `Q D -> 0`, where `D` is the anchored knot diameter. The stronger condition `Q^2 W_1 -> 0` is only a sufficient surrogate.

The live problem is therefore to extend this exact calibration beyond the solved quartic/minimal-support Euler class: determine which observation-specific weighted localization functional replaces `Q Lambda_sigma`, how it interacts with growing source complexity and bandwidth, and when it yields a genuine lower recovery theorem after the destination quotient. Do not replace the exact gate by generic tightness, `W_1`, or one convenient moment without proving equivalence in the declared class.

## Solve the Peano B-spline knot extremal under the exact transfer resource

AF-195 removes coefficient freedom on `m+1` distinct nodes: the unique minimal-support signed control annihilating degrees below `m` is the divided-difference functional. AF-196--AF-198 show that equispaced parity geometry is not generally extremal and that the mirror-symmetric five-node quartic optimizer is a strict local minimum modulo scale. AF-199 identifies the general scale-free shape functional through the Peano B-spline carrier.

AF-200 showed that optimizing that homogeneous shape functional alone can send the carrier out of the region where the Euler observation is informative. AF-204 now supplies the correct quartic repair: within the five-node source class, actual varying-profile transfer is equivalent to `Q D -> 0`. The next extremal question should therefore optimize shape and response **inside a declared weighted-localization class**, or derive the corresponding exact localization resource for higher cancellation order. A sharp homogeneous `Q_m` constant without the transfer gate is not a recovery theorem.

## Keep provenance and endpoint sufficiency separate from conditioning

A representation can be exactly sufficient yet lose source identity after quotienting, or preserve provenance while becoming badly conditioned on an expanding source class. Recovery claims should state separately what is reconstructible, which equivalences are harmless, which source carrier remains localized, and at what quantitative cost the inverse stays stable.