# MI-022 — Polylogarithmic horizon bundles leave dense Möbius-orientation kernels

**Evidence level:** exact synthesis from [FD-163](../../findings/FD-163-bounded-resource-ancestry-forces-positive-density-anchor.md), [FD-164](../../findings/FD-164-one-farey-horizon-leaves-dense-coefficient-orientations-undetermined.md), and [FD-165](../../findings/FD-165-polylogarithmically-many-farey-horizons-still-leave-dense-orientations-undetermined.md), with the unconditional Davenport cancellation input already audited in the line evidence.

Positive geometric exposure and repeated complete Farey observations are still not the same as Möbius orientation information. FD-163 forces a positive-density squarefree anchor under bounded ancestry resources. FD-164 shows that one complete Farey field can leave almost every sign on such a face undetermined. FD-165 proves that this is not a one-horizon accident.

For an arbitrary horizon family `H_T` with `J_T` members, collect every floor quotient used by the complete discrepancy fields. Above a fixed macroscopic cutoff `beta T`, each horizon contributes only `O_beta(1)` such breakpoints. Balanced sign flips inside the resulting blocks produce one ternary squarefree-unit source `a_T` that matches the physical Mertens function at **all** sampled breakpoints simultaneously and hence reproduces every complete Farey field in the bundle exactly.

The remaining orientation freedom has a quantitative law. If

`M_beta(T) = max_(beta T <= x <= T) |M(x)|`,

then the fraction of changed squarefree coefficients can be kept at least

`1 - beta - O_beta(J_T M_beta(T)/T) - o_beta(1)`.

Thus `J_T M_beta(T)=o(T)` is enough for a dense orientation kernel. Since Davenport gives `M_beta(T) <<_(A,beta) T/(log T)^A` for every fixed `A`, **every polylogarithmic family `J_T << (log T)^B` remains asymptotically unable to orient an arbitrarily large fraction of the squarefree source**.

This identifies the relevant horizon resource more sharply than sample count. One complete field may contain many point values or Fourier coordinates, but source-side it factors through a sparse floor-quotient staircase. Adding horizons matters only through the new source breakpoints and the compatibility they enforce. Polylogarithmically many arbitrary horizons add too little macroscopic constraint to kill the balanced-flip fibre.

The theorem still leaves a qualitatively different form of coherence open. The matched source `a_T` is common to the whole finite bundle but may depend on `T`. It is not one infinite alternative source that matches a nested unbounded horizon sequence. Permanent-source consistency can therefore be stronger than any finite-bundle count, and FD-009 shows that the full consecutive divisor hierarchy is eventually lossless by Möbius inversion.

The live discriminator is consequently **common-source rigidity across a sufficiently rich unbounded hierarchy**, not merely “more horizons.” A useful intermediate theorem should locate the sparsity threshold at which nested-horizon consistency or a genuine multiplicative/divisor law begins to orient the positive-density exposed face without simply reconstructing the entire Möbius prefix.

**Boundary.** FD-165 is an exact finite-`T` matched-control obstruction plus an unconditional asymptotic density consequence. It does not construct one infinite non-Möbius source matching infinitely many horizons, does not rule out denser sublinear horizon families outside `J_T M_beta(T)=o(T)`, and does not prove Franel--Landau coercivity once orientations are fixed.