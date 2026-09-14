# MI-011 — Fixed-depth physical data do not create critical coercivity on a reversible Farey skeleton

**Evidence level:** exact for the floor-quotient Fourier skeleton through [FD-117](../../findings/FD-117-full-cumulative-farey-discrepancy-is-invertibly-equivalent-to-quotient-mertens-data.md), [FD-118](../../findings/FD-118-floor-quotient-frequency-skeleton-is-a-minimal-linear-carrier.md), and [FD-119](../../findings/FD-119-fixed-mertens-endpoint-data-cost-only-bounded-energy-on-the-floor-quotient-fourier-skeleton.md). The countermodels below are formal quotient sources satisfying selected physical constraints; they are not claimed to be actual Mertens trajectories.

FD-117 shows that the complete cumulative Farey discrepancy field is invertibly equivalent to the quotient-Mertens staircase. FD-118 compresses its same-horizon Fourier data to the divisor-closed floor-quotient skeleton `Q_N`, of size `2 sqrt(N)+O(1)`, without losing that source.

FD-119 identifies the coercivity obstruction inside this reversible carrier. In the reindexed source coordinates the skeleton has the exact Möbius equality ray

`x_k = m mu(k)/k`,

for which every Fourier mode except the first vanishes and the normalized energy is exactly `m^2`. For every fixed `R`, the true endpoint values `M(1),...,M(R)` and the exact identity

`sum_(d<=N) y_floor(N/d) = 1`

can be grafted onto that ray with only `O_R(1)` additional energy whenever `|m_N| log N=o(N)`. Hence at the RH-critical amplitude `m_N~sqrt(N)`,

`E_N^Q(y)=m_N^2+O_R(1)`

and the relative gap tends to zero.

The reusable point is sharper than “reversible compression adds no information.” A reversible representation may expose a useful norm, but **fixed-depth physical truth can still be asymptotically invisible in the endpoint energy**. To obtain a positive relative gap one needs a restriction whose cost grows on the same scale as the endpoint: growing-depth Mertens increment/multiplicative constraints, cross-horizon coherence, or another source law that quantitatively excludes the equality ray.

This supplies a practical extremizer test for future Farey relaxations: before seeking a sharper inequality, ask whether the retained arithmetic constraints can be imposed on the skeleton equality ray at `o(m_N^2)` cost. If yes, those constraints cannot by themselves prove a critical-scale relative coercivity gap.

**Boundary.** FD-119 does not show that the physical Mertens trajectory approaches the equality ray, nor that every growing-depth constraint succeeds. It only proves that any argument using a fixed Mertens prefix plus the single global floor-quotient identity remains too weak in the native skeleton energy.