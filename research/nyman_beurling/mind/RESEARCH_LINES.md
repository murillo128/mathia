# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Transport the localized zeta-primitive coefficient across `Re(s)=1` without decoupling its signed structure

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-058-exact-zeta-primitive-reconstruction-loses-its-mellin-advantage-only-when-the-signed-convolution-is-decoupled`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-212 derive the current log-squared corridor. NB-213--NB-217 then show that ordinary Mellin primitivization, signs, zero mean, bounded shell moments and support widening all repay apparent gains when reconstruction is estimated by absolute norms. For an arbitrary logarithmic support `E` and `j` primitive transfers, NB-217 isolates the exact absolute reconstruction currency `2pi/J_j(E)`.

NB-218 identifies where that tariff enters. On `Re(s)>1`, the Euler shell is exactly a signed convolution of the `j`-fold zeta primitive with its matched kernel; the factors `(log n)^j` and `(log n)^(-j)` cancel coefficientwise. Because the shell is supported away from zero, the kernel annihilates every finite polynomial jet of the primitive. The positive-power Mellin tariff is therefore not present in the exact algebra; it appears when kernel and primitive are decoupled by absolute values. The native observable is a carrier-frequency Fourier coefficient of the zeta primitive.

NB-219 now removes one of the two analytic obstacles left by NB-218. For a fixed smooth moving logarithmic shell, multiply the exact vertical kernel by a smooth cutoff equal to one on `|v|<=V` and supported in `|v|<=2V`. On the natural line `sigma_X=1+r/X>1`, this localized convolution is exactly another Euler source correlation whose shell profile is the original profile convolved with a Schwartz approximate identity. The induced Euler-source error is

`O_A(V^(-A))`

for every `A`, uniformly in the vertical ordinate. Any `V_X->infinity` therefore gives `o(1)` error, while `V=X^epsilon` gives superalgebraic decay in `X`. Finite-jet annihilation survives the truncation to superalgebraic accuracy as well.

The full-line tail is therefore **not** the live source-side obstruction on the `1+` side. Smooth vertical localization can be performed before estimating the primitive, without paying the NB-217 `L^1 x L^infinity` tariff. What remains is genuinely different: moving this localized signed pairing across `Re(s)=1` to the Vinogradov--Korobov contour. Compact vertical support makes the dual logarithmic source profile Schwartz rather than compactly supported, so termwise absolute convergence is lost to the left of one. Pole/branch terms, horizontal edges, the zero-free rectangle and the noncompact source tails must be controlled without destroying the carrier-frequency cancellation.

The live source-side target is now precise: prove a contour-transport theorem for the **localized** zeta-primitive convolution that preserves its signed carrier-frequency structure. A better pointwise bound for `log zeta`, another primitive, another sign pattern or another support widening does not address this target if the proof ultimately replaces the convolution by a product of absolute norms. A separate destination theorem remains load-bearing: a Nyman approximant resolving the target must still be connected to the source condition being estimated.

## Keep moving-complexity uniformity, source representation, conditioning, localization and reconstruction explicit

The relevant currencies now include source total variation, signed conditioning, requested return tolerance, integer-cell occupancy, zero-free contour width, reciprocal support mass `J_j(E)`, the destination-visible source functional, reconstruction cost, the exact carrier-frequency coefficient, vertical localization radius `V`, the dual noncompact source tail created by that localization, and the contour terms required to cross `Re(s)=1`.

NB-219 is a useful separation principle. A large full-line Fourier domain need not be priced by the primitive's pointwise supremum; smooth high-frequency deletion can correspond to a negligible perturbation of the arithmetic source itself. But localization is not free after contour shift: its dual Schwartz tails are harmless under the positive Euler weight on `sigma>1` and potentially expensive on `sigma<1`. Progress must therefore be measured at the coupled contour interface, not by the size of the localized window alone.
