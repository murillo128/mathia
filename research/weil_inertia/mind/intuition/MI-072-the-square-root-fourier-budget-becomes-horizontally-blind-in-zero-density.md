# MI-072 — The square-root Fourier budget becomes horizontally blind in zero density

**Evidence level:** exact scalar-interface synthesis from [WI-395](../../findings/WI-395-square-root-prime-fourier-norm-contracts-coherent-horizontal-defect.md) and [WI-396](../../findings/WI-396-zero-density-makes-square-root-fourier-horizontal-sensitivity-vanish.md), using the near-line zero-density input already audited in WI-029 and sharpening MI-070--MI-071.

WI-395 closes the scalar-coherence escape left by positive carrier portfolios when the prime side is still paid through the componentwise absolute square-root Fourier envelope. For a Fourier-Stieltjes test with weighted norm

`||mu||_(1/2)=int e^(|u|/2) d|mu|(u)`,

the functional-equation paired horizontal discrepancy at every fixed interior depth `|delta|<=delta_*<1/2` is bounded by

`q(delta_*) ||mu||_(1/2)`

with a sharp constant `q(delta_*)<1`. Arbitrary scalar phases and coherent cross terms are already included. Coherence alone therefore cannot beat the square-root-prime wall while each shifted prime band is charged by its absolute `e^(|u|/2)` cost.

WI-396 makes this stronger for the actual zeta zero population. Jutila's near-line zero-density theorem forces the average of the sharp contraction factors over right-half zero occurrences in a dyadic height window to satisfy

`Q_T=(1/N_T) sum_(rho in E_T^+) q(delta_rho) -> 0`.

Consequently the normalized horizontal discrepancy between the true zero multiset and its projection to the critical line is `o(1)` uniformly over the unit ball of the square-root weighted Fourier norm. At density scale the interface is therefore not merely contractive; it becomes asymptotically blind to horizontal displacement per unit absolute prime budget.

This changes the surviving arithmetic target quantitatively. A scalar family that keeps `||mu_T||_(1/2)=O(1)` cannot retain an order-one density-scale horizontal signal. To do so through the same scalar explicit-formula channel, the **actual signed prime evaluation** must beat the componentwise absolute square-root envelope by a factor comparable to `1/Q_T`, hence by a factor that diverges. Alternatively the observable must leave this scalar interface through matrix/indefinite information, vertical correlations, collective nonlinear structure, or another source theorem whose arithmetic cost is genuinely smaller than the absolute Fourier norm.

The distinction between density-scale and sparse-defect detection is essential. Zero density permits a finite or zero-density family of fixed-depth off-line zeros, and for such a defect `q(delta)` need not tend to zero. WI-396 therefore does not turn the density statement into an RH criterion. It says that the abundant-zero background cannot supply horizontal sensitivity cheaply in this scalar norm; sparse individual failure remains a separate localization problem.

**Boundary.** The conclusion applies to scalar Fourier-Stieltjes tests with finite square-root weighted norm and to density-normalized horizontal sensitivity. It does not rule out the required signed prime cancellation, isolated off-line zeros, matrix-valued or indefinite observables, vertical-spacing information, or test families outside this normed interface. No unconditional RH conclusion or improved critical-line proportion follows.