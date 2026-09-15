# MI-021 — Finite-`L^q` ancestry coercivity needs quantitative anchor exposure, not connectivity alone

**Evidence level:** exact/proved obstruction from [FD-146](../../findings/FD-146-anchor-connectivity-alone-does-not-control-normalized-ancestry-energy.md), refining the exact component-orientation gauge in [FD-145](../../findings/FD-145-rank-truncated-ancestry-defects-have-an-exact-component-orientation-gauge.md).

FD-145 identifies the qualitative prerequisite: relative ancestry equations cannot determine absolute Möbius orientation on a visible component disconnected from an anchored coefficient. FD-146 deliberately restores that prerequisite completely. It uses the full squarefree ancestry graph up to `T`, which is connected to the anchor `1` and contains every local edge.

Connectivity still does not give normalized stability. Fix a rank wall `R0` and write `a_n=mu(n)b(n)` with `b(n)=+1` for `omega(n)<=R0` and `b(n)=-1` above the wall. Every nonzero ancestry defect is then concentrated on edges crossing exactly that finite-rank interface. The number of such edges is only

`O_R0(T (log log T)^R0/log T)`,

while the full squarefree graph has `Omega(T)` edges. For every fixed finite `q`, uniform edge normalization therefore gives

`||a_(pn)+a_n||_(L^q(E_T)) -> 0`

although

`||a-mu||_(L^q(V_T)) -> 2`.

Equivalently, any Poincare-type inequality with uniform vertex/edge normalization must have a coercivity constant diverging at least like `(log T/(log log T)^R0)^(1/q)`. The exact orientation gauge is gone, but the anchor is connected to most of the coefficient mass through a boundary whose normalized exposure vanishes.

The correct resource after connectivity is therefore **quantitative anchor exposure in the destination norm**. A source-native weighting can defeat this particular wall only if it gives every macroscopic orientation change a boundary of nonvanishing normalized observation mass. The distinction is norm-sensitive: the same construction has `L^infinity` edge defect exactly `2`, so full pointwise ancestry data remain information-theoretically sufficient.

This orders the coefficient-side gates. First establish an anchored component; second prove a uniform weighted cut/Poincare inequality for the actual Farey/Franel normalization; only then does the number of independent ancestry tests become the next information bottleneck. Counting observed edges before pricing their normalized cut mass confuses qualitative reachability with quantitative coercivity.

**Boundary.** FD-146 rules out uniform finite-`L^q` coercivity for the full ancestry graph under the stated uniform normalization. It does not rule out source-native nonuniform edge weights, `L^infinity` observables, direct coefficient anchors, or genuinely nonlocal Farey/Fourier functionals. It identifies the quantitative exposure property those alternatives must supply rather than proving that every ancestry-based route fails.