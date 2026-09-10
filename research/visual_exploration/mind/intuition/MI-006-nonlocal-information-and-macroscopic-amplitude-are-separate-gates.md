# MI-006 — Source specificity begins only after the finite-size mean and stochastic null are resolved at the target scale

**Evidence level:** exact bounded-window finite-CUE mean calibration and realized-diagonal covariance control through VIS-132

## Core intuition

Nonlocal information and visible amplitude are not enough to identify arithmetic structure. At the Montgomery support edge, finite-circle geometry, source-window convention, effective-size transfer and stochastic normalization can all create effects at the same `1/L` scale where an arithmetic residual would be tempting to interpret.

The deterministic null is now substantially cleaner than before: using a bounded source taper as a replacement window removes the full-circle coordinate-overlap artifact and regularizes effective-size sensitivity. But this shifts the decisive burden from mean calibration to the covariance of the correctly projected off-diagonal statistic.

## Strongest justified principle

VIS-123--VIS-129 separate the failed source panel from the support-edge opportunity and identify the full-circle finite-size, Montgomery-weight, window and capacity effects. VIS-130 corrects the source model: the continuous-time full-circle CUE statistic already contains a rectangular coordinate-overlap factor, so convolving a tent on top double-windows the source. The exact bounded-tent null must instead be built directly from the local CUE kernel with the tent overlap and Montgomery weight.

VIS-131 derives that corrected mean near `q=1`: `C=1-Phi_(rho,kappa)(v)/L+O(L^-3)` with a Poisson-sampled profile and an exact reflected identity. Under a fixed capacity margin, `Phi` is regular in `rho`; therefore `delta rho=O(1/log L)` induces only `O(1/(L log L))` mean error and integerizing `N` costs only `O(L^-2)`. The earlier generic `O(1/L)` effective-size mean ambiguity is not present in this convention.

VIS-132 then computes the realized tent-diagonal contribution. Its mean is one, but its variance is `Theta(N^-2)`, so for `N=Theta(L)` it fluctuates at exactly `1/L`. This nuisance is a common mode across edge coordinates and is removable exactly by subtracting the realized diagonal or using a zero-sum coordinate contrast. The off-diagonal joint covariance after that projection is not determined by these results.

## Program consequence

Freeze the exact bounded-taper finite-CUE **mean plus projected covariance** before any fresh source test. Derive the off-diagonal covariance under the same finite-`N`, taper, weight and diagonal convention, identify its asymptotic eigen-directions and required averaging budget, and propagate finite-height unfolding/counting/effective-size uncertainty through the same frozen contrast.

Only after those nuisance directions are controlled should an independently derived arithmetic lower-order term define a residual amplitude/direction for untouched zeta data.

## Counterevidence / boundary

VIS-131 does not prove the effective-size rule itself for the tapered statistic; it only prices perturbations once a rule is fixed. VIS-132 controls only the diagonal component. The off-diagonal quadratic statistic may have a nonvanishing stochastic floor, and ordinary full-circle SFF non-self-averaging is only a warning, not a theorem for this tapered model.

## Epistemic status

**Exact deterministic bounded-taper mean null and exact removal of its realized diagonal `1/L` common mode; the projected off-diagonal covariance and source-transfer error remain open.**

## Falsification criterion

Show that the bounded-taper replacement formula or Poisson-sampled edge expansion is wrong, or that the realized diagonal is not a common mode with the stated variance scale. A positive continuation should derive the complete projected covariance/null and then survive predeclared untouched confirmation.
