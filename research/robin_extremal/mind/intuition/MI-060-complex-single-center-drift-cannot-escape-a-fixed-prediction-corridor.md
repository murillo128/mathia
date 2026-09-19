# MI-060 — Center drift must cross the local phase threshold and then pay the macroscopic/Wiener cost

**Evidence level:** exact synthesis from [RE-229](../../findings/RE-229-bounded-complex-single-center-vanishing-arcs-have-divergent-wiener-rate.md), [RE-230](../../findings/RE-230-unbounded-complex-single-centers-force-corridor-blowup.md), [RE-231](../../findings/RE-231-large-center-widening-corridors-have-a-unit-microscopic-threshold.md), [RE-232](../../findings/RE-232-supercritical-large-centers-have-a-sharp-macroscopic-radius-and-a-six-plus-wiener-floor.md), and [RE-233](../../findings/RE-233-the-large-center-transition-arc-has-a-logarithmic-over-m-depth-layer.md).

The remaining single-center loophole after the fixed-parameter analysis was to let the center and corridor drift with scale. RE-229 closes bounded-modulus complex drift in the relevant contracting regime, while RE-230 shows that an unbounded center inside a fixed corridor becomes too weak to cancel the raw delay on the microscopic scale.

RE-231 identifies the right dimensionless coordinate,

`kappa_m=N_m/(m(a_m-1))`.

If `kappa_m->kappa` with `Re(kappa)<1`, the normalized predictor converges on compact `u=m theta` windows to `e^(-i(1-kappa)u)`: widening only renormalizes the residual phase. For positive-real centers, finite `kappa>=1` can flatten that compact microscopic profile. The coefficient-one boundary is therefore the exact local phase transition, not merely a heuristic corridor size.

RE-232 shows that crossing this local threshold is only the first gate. For positive-real large centers and finite `kappa>1`, global fixed-arc prediction has a sharp macroscopic radius

`alpha_*(kappa)=arccos((1+log kappa)/kappa)`.

Every fixed arc below it is predicted exponentially well and every fixed arc above it fails. But the same family pays Wiener rate `w(kappa)=kappa+1+log kappa`, and `w(kappa)/alpha_*(kappa)>6` for every `kappa>1`. The positive-real finite-supercritical escape therefore succeeds geometrically only at a cost worse than the existing `5.996390` finite-center construction.

RE-233 resolves the fixed boundary arc in a rate-achieving fast-center subfamily and exposes one more scale. At exact tuning the closed arc `alpha_*(kappa)` is predicted with `Theta(m^(-1/2))` error. The success/failure boundary depends on a `log(m)/m` detuning of `kappa_m`, so two sequences with the same limiting `kappa` can behave differently at equality. This sequence-sensitive layer refines the transition but does not lower the six-plus Wiener cost.

The reusable lesson is that moving parameters must be audited at **three different currencies**: the local normal-form threshold, the macroscopic destination region, and the global coefficient/Wiener cost. A parameter drift is useful only if it changes the destination-visible normal form and the resulting global predictor remains competitive. Solving the microscopic phase problem is not enough, and refining a zero-rate boundary does not create a new extremal architecture when the global cost is already dominated.

**Boundary.** The six-plus classification is for positive-real large centers with finite supercritical `kappa`; RE-233's sharp equality-layer criterion additionally assumes a fast-center regime. Genuinely complex supercritical limits, `kappa_m->infinity`, slower equality-layer center growth, multi-center/minimax predictors, rational predictors and other bases remain outside the result. None of these findings improves the universal separated lower bound or implies RH.