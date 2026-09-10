# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Derive the projected off-diagonal finite-CUE covariance before testing an arithmetic edge residual

**Linked intuitions:** `MI-001-visual-residuals-must-survive-exact-coordinate-controls`, `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`.

VIS-123--VIS-129 progressively isolate support-edge finite-size, Montgomery-weight, source-window, capacity and effective-size nuisance directions. VIS-130 corrects the finite-CUE source convention: a bounded physical taper must **replace**, not compound, the full-circle coordinate-overlap window already hidden in the continuous-time spectral form factor.

VIS-131 then derives the exact bounded-tent edge mean. With fixed non-wrapping capacity, the deficit is a Poisson-sampled profile `Phi_(rho,kappa)(v)/L+O(L^-3)` and the mean depends regularly on the effective-size ratio, so an `O(1/log L)` uncertainty in `rho` now moves the null only by `O(1/(L log L))`; the previous same-order mean ambiguity is removed by the corrected windowing.

VIS-132 identifies a remaining stochastic nuisance exactly. The realized tapered diagonal fluctuates at order `1/L`, the same scale as the candidate residual, but it is a common scalar across all edge coordinates and can be removed identically by samplewise diagonal subtraction or a predeclared zero-sum contrast. The unresolved gate is therefore the **joint off-diagonal covariance after that projection**, together with finite-height zeta-to-CUE transfer/unfolding uncertainty.

Derive that projected covariance under the exact finite-`N` tent/weight convention, determine its asymptotic scale and nuisance eigendirections, and freeze the complete mean-plus-covariance null before inspecting untouched zeta confirmation data. Only then is an independently predicted arithmetic `1/L` residual interpretable.

## Treat full-circle compounding, effective-size mean drift, and realized diagonal noise as resolved controls

The bounded-source mean null no longer inherits the logarithmically amplified effective-size sensitivity of the full-circle convention, while the diagonal `1/L` fluctuation is exactly removable. Neither result implies self-averaging of the off-diagonal quadratic statistic. Do not import ordinary full-circle spectral-form-factor covariance or infer independence from visually separated height windows.
