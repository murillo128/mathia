# MI-046 — Turán--Nazarov prices both fixed and scale-dependent Wang phase cancellation

**Evidence level:** exact harmonic-analysis synthesis from [VIS-346](../../findings/VIS-346-turan-nazarov-short-window-obstruction.md) and [VIS-347](../../findings/VIS-347-variable-wang-phase-entropy-budget.md), extending the moment obstructions of VIS-343--VIS-345 with classical Turán--Nazarov propagation. These are finite-bank multiplier obstructions, not source-specific estimates for the theta remainder.

For a fixed translated Wang bank, VIS-346 shows that short-window cancellation is not a free escape from the fiberwise moment equations. A phase-resolving reference interval supplies a coefficient lower bound and Turán--Nazarov propagates that nontriviality into shorter windows. If a fixed `B`-fiber bank has order-`r` attenuation on windows of length `ell_X`, a nonzero relevant moment can survive only once the window is microscopic enough that, at the coarse level,

`X*min(ell_X,1)^(B-1)=O(1)`.

VIS-347 shows how the obstruction changes when the bank itself varies with `X`. Group the first inverse-scale moments by translation into `S_X`, let `B_X` be the number of active phase fibers, `Delta_X` their minimum spacing, `T_X=sum_j |c_j|/a_j^2`, and define

`L_X=4(B_X-1)/Delta_X`, `e_X=min(ell_X,L_X)`, `D_X=C_0/2+2T_X`.

Order-`>=2` attenuation forces the necessary phase-entropy budget

`(B_X-1) log(A L_X/e_X) >= log( X ||S_X||_2 / (sqrt(2) D_X) )`.

If `D_X/||S_X||_2=X^(o(1))`, the budget must be `(1-o(1))log X`. Thus a fixed number of phases with `ell_X=X^(-alpha+o(1))` and `Delta_X=X^(-beta+o(1))` requires `(B-1)(alpha+beta)>=1`; with macroscopic windows and uniformly separated phases, one needs `B_X log B_X` of order at least `log X`, hence `B_X=Omega(log X/log log X)` up to constants.

The reusable lesson is that **window shrinkage, phase coalescence and phase-count growth are interchangeable only through an explicit concentration/conditioning budget**. Saying that the bank varies with scale does not evade the fixed-bank obstruction unless the varying family pays that budget. Vanishing first moments or growing `T_X` can make the inequality easy, but then the apparent gain is purchased by coefficient/scale degeneration rather than unexplained arithmetic cancellation.

**Boundary.** VIS-347 is necessary, not constructive. It does not exclude finite banks that genuinely pay the budget, frequency- or source-dependent coefficients, infinite expansions, or direct signed cancellation in `G`. No PNT or RH improvement follows. A surviving localization must still control finite-frequency leakage and prove that Wang's downstream derivative terms do not reconstruct the larger unsmoothed source scale.