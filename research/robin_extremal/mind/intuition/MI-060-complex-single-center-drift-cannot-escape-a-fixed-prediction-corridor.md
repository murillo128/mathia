# MI-060 — Complex single-center drift has a sharp finite widening-corridor microscopic threshold

**Evidence level:** exact synthesis from [RE-229](../../findings/RE-229-bounded-complex-single-center-vanishing-arcs-have-divergent-wiener-rate.md), [RE-230](../../findings/RE-230-unbounded-complex-single-centers-force-corridor-blowup.md), and [RE-231](../../findings/RE-231-large-center-widening-corridors-have-a-unit-microscopic-threshold.md), extending RE-223--RE-228.

The remaining single-center loophole after the fixed-parameter analysis was to let the complex center drift with scale. RE-229 closes the bounded-modulus vanishing-arc branch: arbitrary phase drift does not prevent the normalized negative-binomial predictor from paying a divergent Wiener rate in the relevant contracting regime.

RE-230 closes the complementary unbounded-center branch inside every fixed delay corridor. If `|a_m|->infinity` and

`N_m/(m|a_m-1|)->0`,

then on the microscopic angular scale `theta=u/m` the normalized predictor converges uniformly on compact `u`-intervals to the raw delay `e^(-iu)`. The off-center correction has become too weak to flatten the original `z^m` phase.

RE-231 resolves the finite widening transition with the complex coordinate

`kappa_m=N_m/(m(a_m-1))`.

If `kappa_m->kappa` with `Re(kappa)<1`, then

`F_m(e^(-iu/m)) -> e^(-i(1-kappa)u)`

uniformly for bounded `u`. The raw delay is just `kappa=0`; subcritical widening continuously renormalizes its phase rate to `1-kappa` rather than eliminating it. Consequently any successful family on arcs with `m alpha_m->infinity` has no finite accumulation point `kappa` with `Re(kappa)<1`.

For positive-real centers there is a sharp matched control. If `a_m>1`, `a_m->infinity`, and `kappa_m->kappa>=1`, the same compact microscopic profile converges to the constant `1`. Thus the coefficient-one boundary

`N_m/m >= (1-o(1))(a_m-1)`

is not only necessary in the bounded positive-real transition: at `kappa=1` the local delay obstruction itself disappears.

This changes the frontier. “Widen the corridor” is no longer a sufficient description of the escape. Below the unit transition the microscopic normal form still carries a residual delay; at and above it, that particular probe has no remaining leverage. Any further negative result must find a mesoscopic/macroscopic or Wiener obstruction, and any constructive result must control the growing `u=m theta` range rather than infer global prediction from compact-window flattening.

The reusable lesson is to normalize moving parameters into the dimensionless coordinate that controls the actual local normal form. A drifting parameter is neither automatically useless nor automatically an escape: the correct question is whether it crosses the value at which the source-side phase seen by the destination genuinely changes category.

**Boundary.** The supercritical flattening theorem is proved for positive-real centers; finite complex limits with `Re(kappa)>=1`, `|kappa_m|->infinity`, multi-center/minimax predictors, rational predictors and other bases remain outside the result. Compact microscopic flattening does not prove uniform prediction on arcs with `m alpha_m->infinity`, improve the universal separated-measure bound, or imply RH.