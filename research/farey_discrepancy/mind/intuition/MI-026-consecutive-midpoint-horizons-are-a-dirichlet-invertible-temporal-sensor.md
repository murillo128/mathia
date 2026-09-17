# MI-026 — Consecutive midpoint horizons form a Dirichlet-invertible temporal sensor

**Evidence level:** exact synthesis from [FD-166](../../findings/FD-166-unbounded-complete-field-horizons-force-the-permanent-mobius-source.md), [FD-167](../../findings/FD-167-full-field-l2-inversion-has-uniform-square-root-prefix-conditioning.md), [FD-168](../../findings/FD-168-prefix-mobius-rows-give-coordinate-minimal-stable-partial-farey-sampling.md), [FD-169](../../findings/FD-169-unrestricted-mixed-measurements-collapse-to-target-rank.md), and [FD-170](../../findings/FD-170-midpoint-horizon-path-is-a-dirichlet-invertible-temporal-sensor.md).

A Farey observation can be spatially tiny and still source-complete if the observation operator changes with horizon. FD-170 fixes the spatial point at `1/2` and records only the horizon path `P_a(H)=D_{H,a}(1/2)`. Its first difference is

`P_a(H)-P_a(H-1)=-(1/2)(u*a)(H)`,

with `u` the indicator of odd integers. Since the Dirichlet inverse of `u` is `mu` on odd divisors and zero on even divisors, every source coefficient is recovered by an explicit triangular divisor inversion.

The point is not that one scalar compresses an arbitrary prefix. The sequence of consecutive horizons supplies one new scalar constraint at each step. Spatial dimension and temporal/operator dimension are therefore different resources. Counting only simultaneous spatial coordinates can dramatically understate the information in a multiscale observation hierarchy.

This complements FD-168 and FD-169. FD-168 prices recovery inside a fixed raw Fourier basis; FD-169 shows that unrestricted target-aware mixing trivializes output count; FD-170 shows that even a fixed spatial location can become complete when the acquisition operator itself evolves through a sufficiently rich nested family. A meaningful scarcity theorem must declare whether horizon changes are free, charged, sparse, noisy or constrained before comparing measurement counts.

The inversion is also quantitatively usable: uniform midpoint-path error `epsilon` produces coefficient error bounded by a divisor factor `4 epsilon 2^(omega(n_odd))=epsilon n^(o(1))`. Thus the temporal completeness is not merely set-theoretic.

**Boundary.** Consecutive horizons are essential to the exact triangular inversion proved in FD-170. Sparse/nonconsecutive horizon sets, constrained temporal sampling and the bridge from recovered coefficients to the Franel--Landau destination remain open. The result is an acquisition theorem, not an RH estimate.