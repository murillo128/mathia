# MI-017 — Stable recovery scale is controlled by profile-weighted carrier localization

**Evidence level:** supported by exact Blaschke conditioning, adaptive Euler-cluster controls, overlap asymptotics, Peano-carrier escape, and the exact quartic weighted-localization calibration through AF-204

## Core intuition

Exact sufficiency does not determine stable recovery. The inverse scale is controlled jointly by the destination quotient/metric, admissible source geometry and complexity, the regularity and bandwidth of the observation map, algebraic structure in the kernel, and **whether the source carrier stays localized where the surviving source profile can still be observed**.

AF-200 made localization an unavoidable independent variable. AF-204 sharpens the statement: in the solved quartic five-node Euler class, localization is not merely a qualitative tightness condition. The exact transfer currency is the source profile multiplied by the observation-specific endpoint defect, `Q Lambda_sigma(beta)`, equivalently `Q D` in the source coordinates. A source may localize in an unweighted sense and still fail when its profile grows faster than the localization defect shrinks.

## Strongest justified principle

AF-180--AF-188 show that cancellation complexity, local source scale, derivative growth, and Euler bandwidth create distinct visibility regimes. AF-189--AF-194 add an approximation-strength gate: neighboring finite-overlap and saddle descriptions can agree logarithmically while failing multiplicatively until the sharper correction parameter is small.

AF-195--AF-199 identify minimal-support moment-flat controls with variable-knot Peano B-splines. AF-200 proves that `W_1` alone does not make this source class tight: at fixed positive `W_1`, a quartic five-node family can send its Peano carrier to infinity while the fixed-band Euler discrepancy vanishes.

AF-201 identifies weak carrier concentration as the exact fixed-band transfer topology when the quartic profile `Q` is two-sided bounded. AF-203 gives the stronger varying-profile sufficient condition `Q^2 W_1 -> 0`. AF-204 then finds the intrinsic varying-profile gate. The full fixed vertical-band transfer error is two-sided comparable to `Q Lambda_sigma(beta)`, where `Lambda_sigma` is the positive real-axis Euler localization defect. Hence transfer occurs if and only if `Q Lambda_sigma(beta) -> 0`; within the five-node minimal-support class this is equivalent to `Q D -> 0`. The `Q^2 W_1` condition is therefore a convenient sufficient bound, not the governing topology.

## Counterevidence / boundary

The exact `Q Lambda_sigma` / `Q D` equivalence is proved for the quartic five-node minimal-support class and a fixed Euler vertical band. It is not a universal formula for arbitrary cancellation order, arbitrary kernels, or unrestricted source measures. Observation-specific cancellation may produce a different weighted defect, and growing bandwidth can change the localization currency.

Likewise, AF-204 calibrates forward transfer to the endpoint profile; it does not by itself prove stable inversion of a larger arithmetic source class. Quotient structure, provenance, and source-complexity growth remain separate gates unless a theorem couples them.

## Epistemic status

**Exact weighted-localization law in the solved quartic Euler class; supported general principle that stable recovery requires an observation- and profile-calibrated non-escape resource.**

## Falsification criterion

Within the AF-204 source class, produce a sequence for which full fixed-band transfer holds while `Q Lambda_sigma(beta)` fails to vanish, or vice versa. Beyond that class, a recovery theorem whose uniform constant is independent of every observation-sensitive localization resource would narrow the general synthesis; the relevant comparison must allow source complexity/profile growth rather than silently fixing it.