# MI-026 — Consecutive midpoint horizons form an irredundant Dirichlet-invertible temporal sensor

**Evidence level:** exact synthesis from [FD-166](../../findings/FD-166-unbounded-complete-field-horizons-force-the-permanent-mobius-source.md), [FD-167](../../findings/FD-167-full-field-l2-inversion-has-uniform-square-root-prefix-conditioning.md), [FD-168](../../findings/FD-168-prefix-mobius-rows-give-coordinate-minimal-stable-partial-farey-sampling.md), [FD-169](../../findings/FD-169-unrestricted-mixed-measurements-collapse-to-target-rank.md), [FD-170](../../findings/FD-170-midpoint-horizon-path-is-a-dirichlet-invertible-temporal-sensor.md), and [FD-171](../../findings/FD-171-midpoint-temporal-sensing-has-zero-exact-redundancy.md).

A Farey observation can be spatially tiny and still source-complete if the observation operator changes with horizon. FD-170 fixes the spatial point at `1/2` and records only the horizon path `P_a(H)=D_{H,a}(1/2)`. Its first difference is

`P_a(H)-P_a(H-1)=-(1/2)(u*a)(H)`,

with `u` the indicator of odd integers. Since the Dirichlet inverse of `u` is `mu` on odd divisors and zero on even divisors, every source coefficient is recovered by an explicit triangular divisor inversion.

FD-171 proves the converse is sharp over the unrestricted normalized formal source class. In the invertible coordinate `b=u*(a-mu)`, the midpoint error at horizon `H` is a cumulative prefix sum of `b`. Omitting one horizon `k` leaves the pulse pair `b=e_k-e_(k+1)` invisible at every observed horizon, and pulling it back through `u^{-1}=mu_odd` gives a fixed integer-valued permanent source perturbation. Thus even observing every horizon except one is noninjective.

On a finite prefix `2,...,K`, any selected horizon set `S` has exact row rank `|S|` and kernel dimension `K-1-|S|`. Consecutive temporal sampling is therefore not merely one sufficient inversion scheme: **every horizon row is an independent exact source constraint in this acquisition model**. There is no hidden temporal oversampling to sparsify over the unrestricted formal source space.

The point is not that one scalar compresses an arbitrary prefix. The sequence of horizon-dependent operators supplies one new scalar constraint at each step. Spatial dimension and temporal/operator dimension are different resources, and the latter must be charged row by row when the rows are independent. FD-166 supplies the complementary geometry: sparse unbounded *complete fields* can still recover a permanent source because each field contains an expanding consecutive source prefix, whereas midpoint rows do not subsume omitted earlier rows.

The inversion is quantitatively usable when all rows are present: uniform midpoint-path error `epsilon` produces coefficient error bounded by `4 epsilon 2^(omega(n_odd))=epsilon n^(o(1))`. But exact kernel comes before conditioning. Once a horizon is omitted, no noise estimate can repair the missing direction without extra source restrictions or extra measurements.

**Boundary.** FD-171 is sharp for the unrestricted normalized formal arithmetic-source class. Its pulse-pair perturbation need not preserve Möbius multiplicativity, squarefree support, or ternary coefficient structure. Sparse midpoint recovery can therefore survive only by proving that a genuinely source-faithful admissible class destroys those null directions, or by adding spatial rows and pricing a mixed space-time acquisition family. None of these acquisition results supplies the RH-critical Franel--Landau estimate.