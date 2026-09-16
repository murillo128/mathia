# MI-033 — Fixed-cap inertia recovery requires cofinal saturation before the source changes

**Evidence level:** proved variational consequence of the source-exact capped-tail decomposition, established in [WI-314](../../findings/WI-314-fixed-cap-threshold-recovers-source-negative-index-cofinally.md) from the WI-311/WI-313 framework.

At one fixed source aperture, suppose

`Q = D_delta + T_delta`, with `(1/2-delta)I <= T_delta <= (1/2)I`.

Writing `E_delta=(1/2)I-T_delta` gives `0<=E_delta<=delta I` and the exact identity

`D_delta + (1/2)I = Q + E_delta`.

Therefore the strict fixed-threshold count satisfies

`N_Q(-delta) <= N_D_delta(-1/2) <= N_Q(0)`.

The upper inequality is the key orientation: spectrum of `Q` at zero or above can never create a false comparison mode strictly below `-1/2`. Finite saturation error can only hide source-negative directions whose depth is at most `delta`.

For any cofinal family `delta_j -> 0` at the **same fixed source form**,

`N_Q(0) = sup_j N_D_j(-1/2)`.

If the source negative index is finite, sufficiently saturated members eventually reproduce that index exactly. Thus the moving-floor statistic of WI-313 is not necessary to avoid positive-side ambiguity: the fixed cap gives a one-sided, false-positive-free sign detector when saturation is cofinal.

The order of limits is load-bearing. If the aperture changes to `Q_L` while only one error `delta_L -> 0` is chosen, a source-negative margin may shrink faster than `delta_L`; WI-314 gives an exact one-dimensional countermodel where every fixed-cap comparison misses the negativity. Scalar tail saturation alone therefore does not justify a diagonal aperture limit.

A route from fixed-aperture recovery to the global problem needs additional source-tail alignment: a uniform lower bound on relevant negative depth, a vectorwise cap-defect estimate on the negative sector, or genuinely cofinal saturation at each fixed aperture before changing the source. This is a sign-resolution theorem, not an RH result.
