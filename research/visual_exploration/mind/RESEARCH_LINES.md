# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Finish the exact bounded-taper finite-CUE null before testing a new residual

**Linked intuitions:** `MI-001-visual-residuals-must-survive-exact-coordinate-controls`, `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`.

VIS-124--VIS-126 derive deterministic pair-weight/window/density controls. VIS-127 shows that a growing hard source window cannot be represented by one logarithmic-size CUE circle while retaining the current fixed-edge asymptotic. VIS-128 replaces it with a bounded tent taper and derives its exact squared-sinc-squared kernel plus the leading composed Montgomery edge profile. VIS-129 then supplies a non-fitted pair-correlation effective-size candidate and exposes the remaining resolution gate: uncertainty of order `1/log L_T` in the ratio `N/L_T` can mimic the desired `1/L_T` residual.

The next source experiment should therefore freeze a bounded physical taper inside the single-circle capacity, evaluate the **exact finite-`N` weighted+tapered CUE null** using the predeclared effective-size rule and integerization, and propagate any theoretically unresolved transfer error in `N(T)` into the covariance. Only then should untouched zeta windows be used to test an arithmetic residual.

## Treat hard-window growth and leading-order effective-size matching as controls

Removing the hard-window logarithmic leakage by making the window grow breaks the literal finite-circle model. Replacing it by a taper fixes capacity but leaves an `O(1/L_T)` universal correction, while knowing only `N(T)~rho_*L_T` may still be too imprecise at that same scale. A residual is meaningful only after these nuisance directions are fixed or carried explicitly in the null.
