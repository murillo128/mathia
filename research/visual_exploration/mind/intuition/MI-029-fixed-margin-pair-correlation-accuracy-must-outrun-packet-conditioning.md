# MI-029 — Fixed-margin pair-correlation accuracy must outrun packet conditioning

**Evidence level:** literature-plus-exact synthesis from [VIS-257](../../findings/VIS-257-cusp-annihilation-exposes-finite-window-quadratic-conditioning.md) through [VIS-260](../../findings/VIS-260-rodgers-fixed-margin-error-pays-cusp-packet-conditioning.md). The external pair-correlation theorem and its scope are inherited from the audited statement in VIS-260.

The sharp cusp-packet problem has two independent scales: how much total variation is required to isolate the first surviving carrier, and how accurately the underlying pair statistic is known uniformly over the packet support. VIS-259 solves the first scale exactly; VIS-260 shows how to compose it with a rigorous arithmetic theorem rather than reason from packet geometry alone.

After cancelling mass, the sine-kernel cusp and even moments below order `2m`, a unit `2m`-th moment costs exactly

`E_m^(-1) b^(-2m)`

in total variation on `[-b,b]`. If a theorem controls the underlying scalar pair statistic uniformly by `epsilon_T`, the packetized error is therefore at most `epsilon_T E_m^(-1)b^(-2m)`. The theorem error must beat the same conditioning exponent that the carrier extraction pays.

Rodgers supplies one concrete calibration. For fixed support margin `epsilon>0`, fixed smooth weight and any fixed `delta<epsilon/2`, the pair-correlation prediction has uniform error `O_delta(T^(-delta))`. Hence the optimally conditioned packet is certified only when

`T^(-delta)b^(-2m) -> 0`.

For a power bandwidth `b=T^(-beta)`, some admissible `delta` exists exactly when `beta<epsilon/(4m)`. Thus quadratic extraction can be certified for `beta<epsilon/4`, quartic extraction for `beta<epsilon/8`, and higher cancellation progressively narrows the theorem-supported shrinking-band regime.

This is a useful positive result because it separates an absolute conditioning obstruction from a theorem-relative one. The `b^(-2m)` cost is unavoidable, but a sufficiently accurate theorem can pay it. Conversely, quoting a decaying scalar error without multiplying by the packet norm can overstate what survives after cancellation.

The fixed-margin qualifier is load-bearing. Rodgers' theorem fixes the support margin and the weight before `T -> infinity`; it does not provide uniform control for `epsilon_T -> 0` or a family of changing windows. Nor does a two-level pair theorem supply the four-level covariance needed for the original edge--edge statistic. Those are new mathematical inputs, not parameter substitutions.

The next source-side test is therefore concrete: for one predeclared fixed-margin statistic, compute the first nonzero Taylor coefficient of the arithmetic prediction after the same cusp-adapted cancellations and compare its size directly with the conditioned theorem error. Only if that carrier survives should one spend effort on a moving-edge uniform theorem or higher-order covariance.

**Boundary.** The rate `beta<epsilon/(4m)` belongs to the specific fixed-margin theorem quoted in VIS-260 and the total-variation/sup-norm packet duality of VIS-259. It is not a universal support-edge threshold, does not justify varying `epsilon` or the test weight with `T`, and does not establish any RH implication beyond the hypotheses already assumed by the pair-correlation theorem.