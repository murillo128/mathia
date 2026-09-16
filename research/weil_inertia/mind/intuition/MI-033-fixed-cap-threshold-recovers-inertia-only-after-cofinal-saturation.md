# MI-033 — Nested Weil windows make vanishing-cap diagonals sign-complete

**Evidence level:** the fixed-aperture comparison bounds are proved in [WI-314](../../findings/WI-314-fixed-cap-threshold-recovers-source-negative-index-cofinally.md); [WI-315](../../findings/WI-315-nested-weil-windows-make-vanishing-cap-diagonals-inertia-complete.md) proves that the actual nested compact-support Weil family removes WI-314's abstract changing-source diagonal obstruction.

At one fixed aperture, if

`Q = D_delta + T_delta`, with `(1/2-delta)I <= T_delta <= (1/2)I`,

then `D_delta+(1/2)I = Q+E_delta` with `0<=E_delta<=delta I`, so

`N_Q(-delta) <= N_D_delta(-1/2) <= N_Q(0)`.

The strict `-1/2` threshold has no false positives; finite cap error can only hide source-negative directions shallower than `delta`.

WI-314's abstract warning allowed the source form itself to change with aperture, so its negative direction could become shallower at the same rate as the cap error. WI-315 shows that this does **not** model the compact-support Weil problem. The spaces `D_L=C_c^infty((-L,L))` are nested restrictions of one global quadratic form `Q`. Once a finite-dimensional compactly supported negative subspace appears, its negative Rayleigh margin is fixed forever as the aperture grows.

Consequently, for **any** cofinal aperture sequence `L_j->infinity` and any cap errors `delta_j->0`, the strict comparison counts below `-1/2` converge to the complete compact-support negative index of `Q`. If that index is finite, the counts are eventually exactly equal to it; if it is infinite, they diverge. No aperture-uniform negative-depth estimate, per-aperture cofinal saturation, commutation or spectral discreteness is needed.

This removes the limit-order problem for the actual Weil windows. The hard theorem is now cleaner: construct a source-exact cofinal capped-tail diagonal and prove that its comparison has **no spectrum below `-1/2`**. If such an estimate holds, the nested-domain variational theorem already transports it to Weil positivity on the compact-support criterion. The missing resource is comparison positivity/coercivity, not a separate source-margin synchronization theorem.

**Boundary.** The correction applies to the nested compact-support restrictions of the same global Weil form. WI-314's arbitrary varying-source countermodel remains valid outside that consistency structure, and WI-315 does not itself prove the required comparison lower bound or RH.
