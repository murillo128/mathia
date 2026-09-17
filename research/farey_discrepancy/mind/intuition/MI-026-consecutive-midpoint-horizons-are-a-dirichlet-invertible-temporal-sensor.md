# MI-026 — Midpoint temporal redundancy is relative to the admissible source class

**Evidence level:** exact synthesis from [FD-166](../../findings/FD-166-unbounded-complete-field-horizons-force-the-permanent-mobius-source.md), [FD-167](../../findings/FD-167-full-field-l2-inversion-has-uniform-square-root-prefix-conditioning.md), [FD-168](../../findings/FD-168-prefix-mobius-rows-give-coordinate-minimal-stable-partial-farey-sampling.md), [FD-169](../../findings/FD-169-unrestricted-mixed-measurements-collapse-to-target-rank.md), [FD-170](../../findings/FD-170-midpoint-horizon-path-is-a-dirichlet-invertible-temporal-sensor.md), [FD-171](../../findings/FD-171-midpoint-temporal-sensing-has-zero-exact-redundancy.md), and [FD-172](../../findings/FD-172-dyadic-midpoint-sensing-rigidifies-bounded-squarefree-multiplicative-sources.md).

A Farey observation can be spatially tiny and still source-complete if the observation operator changes with horizon. FD-170 fixes the spatial point at `1/2` and records only the horizon path `P_a(H)=D_{H,a}(1/2)`. Its first difference is

`P_a(H)-P_a(H-1)=-(1/2)(u*a)(H)`,

with `u` the indicator of odd integers. Since the Dirichlet inverse of `u` is `mu` on odd divisors and zero on even divisors, every formal source coefficient is recovered by an explicit triangular divisor inversion when every horizon is observed.

FD-171 proves this temporal family has **zero exact redundancy over the unrestricted normalized formal source class**. In the invertible coordinate `b=u*(a-mu)`, the midpoint error at horizon `H` is a cumulative prefix sum of `b`. Omitting one horizon `k` leaves the pulse pair `b=e_k-e_(k+1)` invisible at every observed horizon, and pulling it back through `u^{-1}=mu_odd` gives a fixed integer-valued permanent source perturbation. On a finite prefix `2,...,K`, any selected horizon set `S` has exact row rank `|S|` and kernel dimension `K-1-|S|`.

FD-172 shows why that rank statement is not an intrinsic information lower bound once the admissible source fibre changes. Restrict to multiplicative squarefree-supported sources with `-1<=a(p)<=1`. For odd squarefree `m`, the transformed coefficient

`F(m)=(u*a)(m)=prod_(p|m)(1+a(p))`

is nonnegative. The dyadic midpoint error decomposes into nonnegative annular contributions, so a prime defect cannot be hidden by the signed pulse cancellation used in FD-171. Exact agreement with Möbius at `H=2,4,8,...` forces `a=mu`, and agreement through `2^M` forces the whole source prefix through `2^M`. Small dyadic errors also bound each prime defect by the same error scale.

The two theorems are not contradictory. FD-171 is an ambient linear recovery statement: every temporal row is indispensable when arbitrary normalized formal perturbations are allowed. FD-172 is a **one-target rigidity theorem inside a nonlinear arithmetic cone**: multiplicativity and primewise positivity remove the pulse-pair null directions, so exponentially sparse dyadic rows suffice to certify the Möbius target. It does not prove pairwise injectivity between arbitrary admissible sources.

The reusable lesson is that observation rank and redundancy must be computed *after* the source class and target notion are fixed. A row can be linearly independent in the ambient source space yet unnecessary for testing one distinguished source when nonlinear source constraints turn all surviving defects into positive mass that a sparse cover must see.

**Boundary.** FD-172 uses bounded squarefree multiplicativity and the sign condition `-1<=a(p)<=1`. It does not show that squarefree/ternary structure without multiplicativity suffices, characterize all sparse horizon sets, or supply the RH-critical Franel--Landau estimate. The next question is exactly how much of the source architecture is needed before the ambient temporal kernel collapses.