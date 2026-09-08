# MI-017 — Stable recovery scale needs source complexity, observation structure, and carrier localization

**Evidence level:** supported by exact Blaschke conditioning, adaptive Euler-cluster controls, overlap asymptotics, and the fixed-Wasserstein Peano escape through AF-200

## Core intuition

Exact sufficiency does not determine stable recovery. The inverse scale is controlled jointly by the destination quotient/metric, admissible source geometry and complexity, the regularity and bandwidth of the observation map, algebraic structure in the kernel, **and whether the source carrier remains localized where that observation is informative**.

AF-180--AF-188 show the complexity/bandwidth interaction: increasing cancellation order can hide positive source pairs from derivative-limited observations, while the Euler harmonic ladder restores visibility once bandwidth reaches the reciprocal-separation scale. AF-200 adds a different failure that survives fixed cancellation order. At fixed positive `W_1`, a five-node quartic control can move its Peano carrier arbitrarily far into a region where every fixed vertical Euler band is exponentially insensitive, driving the discrepancy to zero.

## Strongest justified principle

For derivative-controlled kernels, AF-186 identifies an associated-function envelope governing how cancellation order and local source scale trade against available derivative growth. AF-187--AF-188 then show that this is not a kernel-independent law: the Euler harmonic structure produces super-algebraic invisibility, a continuum of algebraic exponents, and order-one visibility in different bandwidth regimes.

AF-189--AF-194 add an approximation-strength gate. Adjacent finite-overlap and saddle descriptions can agree at logarithmic scale while failing multiplicatively until the sharper correction parameter is small. A declared asymptotic category is part of the recovery statement.

AF-195--AF-199 identify minimal-support moment-flat controls with variable-knot Peano B-splines. AF-200 proves that `W_1` alone does not make this source class tight: at fixed `W_1=delta`, the quartic mirror family can have `h~delta/t -> infinity`, while the fixed-band Euler discrepancy is `~(t^2/2)M_0 ->0`. The normalized Peano carrier has exact barycenter `x+(1+t)h` and `W_1(B,delta_x)=(1+t)h`, making localization the missing variable rather than a proof artifact.

## Counterevidence / boundary

AF-200 is a decisive obstruction to a `W_1`-only fixed-band modulus, not a proof that compact support or the displayed barycenter condition is the weakest repair. Observation-specific cancellation may permit a weaker tightness notion. The exact escape is proved inside the mirror-symmetric five-node quartic family; that already kills a uniform theorem on the larger unrestricted class but does not classify every escaping shape.

Likewise, the harmonic and overlap results do not prove stable inversion for all generalized-prime sources. Source geometry, bandwidth, kernel algebra, and localization remain separate resources unless an exact theorem couples them.

## Epistemic status

**Supported mechanism-level recovery principle from exact component theorems; no universal inverse theorem is claimed.**

## Falsification criterion

Produce a positive fixed-band recovery modulus depending only on `W_1` for a source class containing the AF-200 escape, or invalidate its exact Peano-carrier representation. A positive source-class theorem should identify an intrinsic tightness/localization condition and prove a lower observation bound at the declared bandwidth without silently fixing source shape.
