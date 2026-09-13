# MI-013 — Sinc-weighted destination energy can vanish after raw shell dilution has stopped

**Evidence level:** exact for the autocorrelation-taper subclass through [VIS-203](../../findings/VIS-203-autocorrelation-tapers-make-exact-difference-shells-noncancelling.md)--[VIS-207](../../findings/VIS-207-growing-window-pair-crowding-bound.md), with the full noncancelling-band weighted extension [VIS-208](../../findings/VIS-208-sinc-weighted-noncancelling-shell-band.md). One-cancellation shells and uniform-in-start control remain open.

For a shifted autocorrelation taper the frequency coefficients share a linear phase, so exact-difference shell amplitudes are nonnegative. VIS-205 identifies normalized dangerous shell energy with a two-sample close-pair resource up to bounded multiplicity in the noncancelling determinant regime. VIS-207 then proves the cumulative estimate

`S_(y,H)(A)/R^2 << H A^(2+4 alpha)(log y)^2/y^2`

through a growing window. Its original dilution consequence required the right-hand side itself to tend to zero.

VIS-208 separates that raw cumulative requirement from the actual finite-start destination. The same incidence estimate remains valid uniformly throughout every constant-fraction noncancelling range `1<=A<=kappa y`, `kappa<1/2`, even when the cumulative shell mass is not small. The finite-start kernel weights a shell at normalized coordinate `a` by approximately `min(1,(A_L/a)^2)`, where `A_L~y^2/L`. Abel/Stieltjes summation converts cumulative shell growth into a much smaller weighted energy.

For `0<alpha<1/2`, the long-start normalized energy of the whole truncated noncancelling band satisfies

`W_kappa << H y^(2+4 alpha)(log y)^2/L^2`.

At `alpha=0` the same critical exponent produces only an extra logarithmic factor. Hence sufficiently long windows make the complete band below any fixed fraction of the first one-cancellation scale negligible in Cesaro mean square, even after unweighted dilution has ceased to be available. Chebyshev then gives a density-one set of starts with negligible contribution.

The reusable principle is destination-relative: **a cumulative positive resource can be too large in its native norm and still be harmless after the exact kernel of the downstream observable is charged**. A threshold obtained before applying that kernel is not automatically a barrier for the destination quantity.

The remaining boundaries are qualitatively different. At the one-cancellation scale, determinant multiplicity and shell geometry change, so the bounded-multiplicity reduction cannot simply be extended. And start-average `L^2` control permits rare coherent starts; it does not give uniform-in-`T0` dephasing. These should be treated as separate problems rather than as failures of the already-controlled noncancelling band.

**Boundary.** VIS-208 applies to the autocorrelation-taper subclass and to the truncated noncancelling band. It does not bound sign-changing tapers, shells at or above the one-cancellation scale, the full finite-start error, or worst-start amplitude. The logarithmic endpoint loss may reflect the available cumulative majorant rather than the true shell distribution.