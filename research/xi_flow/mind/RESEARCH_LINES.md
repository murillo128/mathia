# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Use full q-scale Toeplitz coercivity and exact Xi-budget realization as established source theorems

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-006-periodic-vieta-coordinates-diagonalize-the-nonlinear-heat-flow`, `MI-007-ultra-infrared-vieta-modes-should-be-quotiented-by-destination-energy`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-009-guarded-energy-can-enforce-static-real-divisor-feasibility`, `MI-010-endpoint-renormalization-is-source-fixed-before-discretization`.

XF-087--XF-100 close source extraction, endpoint renormalization, mesh sampling, full-prefix realization, and fixed-time periodic shadowing at the guarded low bandwidth, while showing that this entire prefix is prime-free. XF-101--XF-113 then identify the mass-preserving q-scale Toeplitz source and progressively constrain hypothetical negative witnesses; coarse support, concentration, roughness, and bad-set controls alone still admit matched negatives.

XF-114--XF-118 close the q-scale coercivity gap. Full-circle Fejer flatness is upgraded by a smooth-carrier/autocorrelation lift to

`||T_hat_K-I||_op -> 0`, hence `lambda_min(T_hat_K)=1-o(1)>0`,

for the entire natural degree-`K` Toeplitz section. Arbitrary q-scale polynomial witnesses are therefore controlled, not just plane waves.

XF-119 closes the remaining **static realization** gap at the actual Xi node budget. A backward Poisson factor at radius `r_K=e^{-gamma/K}` is a uniformly bounded Schur multiplier on the near-identity Toeplitz section. After representing the inflated moments and convolving forward with the Poisson kernel, one obtains the original first `K` Xi moments with a density uniformly bounded above and below. Equal-weight trigonometric quadrature then realizes those moments exactly for every sufficiently large node count `N>=C K`; since the Xi budget satisfies `N/K -> infinity`, the prescribed degree `N=2q^2` itself eventually works.

The low/q-scale source prefix is therefore not merely approximately admissible or positive: it has an **exact equal-weight real-divisor realization at the Xi degree budget**. The live problem starts after static source admission. A positive-`Lambda` contradiction must show that the exact transition/guarded-energy dynamics force a property incompatible with this source-faithful realized prefix, or identify a different scale where the transition sees information absent from the q-scale model.

## Force Xi-specific transition coercivity beyond the now-solved q-scale source and realization gates

XF-098--XF-100 show that the guarded low-frequency trajectory can be shadowed by prime-free periodic data. XF-114--XF-119 now strengthen the source side dramatically: the actual Xi q-scale moment matrix is asymptotically identity and those moments admit exact equal-weight degree-`N` real-divisor realization with the correct node budget.

Neither theorem is an upper bound on the de Bruijn--Newman transition time. The remaining bridge must connect a hypothetical `Lambda>0` transition to a forbidden sign, energy, collision, or transport condition for the **exact realized q-scale prefix** after endpoint renormalization and periodic Vieta evolution. If the transition theorem does not consume this q-scale resource, then the line should move scales rather than continue strengthening static feasibility that is already solved.

## Decide the q-scale versus prime-band fork explicitly

Staying below the first prime atom no longer lacks source-side positivity or real-divisor admission: XF-118--XF-119 supply both. The missing statement is a transition theorem showing that the declared positive-`Lambda` scenario cannot coexist with that exact source realization and its guarded evolution.

Moving to `xi=Theta(1)` beginning at `lambda_2` remains a separate route. It must handle distributional prime-power atoms and replace the current perturbative point-sampling/shadow estimate. Q-scale Toeplitz coercivity and equal-weight realization must not be transferred to the prime band without a new interface theorem.

## Keep source coercivity, exact realization, transport, and transition coercivity separate

XF-118 and XF-119 are genuine unconditional source theorems: full-cone positivity followed by exact Xi-budget real-divisor realization. They do not imply `Lambda<=0`. Future results should state explicitly whether they change source admission, realization, transport stability, observable bandwidth, prime-band access, or the transition inequality. The now-closed q-scale positivity and static-realization gates should not be reopened unless a later destination theorem requires a materially different matrix, moment set, or scale.