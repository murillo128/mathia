# MI-011 — Single-horizon physical laws can still be asymptotically invisible on a reversible Farey skeleton

**Evidence level:** exact for the floor-quotient Fourier skeleton through [FD-117](../../findings/FD-117-full-cumulative-farey-discrepancy-is-invertibly-equivalent-to-quotient-mertens-data.md), [FD-118](../../findings/FD-118-floor-quotient-frequency-skeleton-is-a-minimal-linear-carrier.md), [FD-119](../../findings/FD-119-fixed-mertens-endpoint-data-cost-only-bounded-energy-on-the-floor-quotient-fourier-skeleton.md), and [FD-120](../../findings/FD-120-squarefree-unit-increments-and-one-divisor-identity-still-saturate-the-fourier-skeleton.md). The countermodels are synthetic quotient sources; they are not claimed to be actual Mertens trajectories.

FD-117 shows that the complete cumulative Farey discrepancy field is invertibly equivalent to the quotient-Mertens staircase. FD-118 compresses its same-horizon Fourier data to the divisor-closed floor-quotient skeleton `Q_N`, of size `2 sqrt(N)+O(1)`, without losing that source.

FD-119 identifies the coercivity obstruction inside this reversible carrier. In reindexed source coordinates the skeleton has the exact Möbius equality ray

`x_k = m mu(k)/k`,

for which every Fourier mode except the first vanishes and the normalized energy is exactly `m^2`. Any fixed true Mertens prefix plus the exact identity `sum_(d<=N)y_floor(N/d)=1` can be grafted onto that ray with only `O_R(1)` additional energy. At the RH-critical amplitude `m_N~sqrt(N)`, fixed-depth truth therefore has vanishing relative cost.

FD-120 shows that **depth by itself is not the missing resource**. For every sufficiently large horizon one can choose a complete increment sequence with

`a_N(1)=1`, `a_N(n)=0` on nonsquarefree `n`, and `a_N(n) in {-1,+1}` on every squarefree `n`,

while also satisfying the exact physical single-horizon divisor identity and `Y_N(N)=sqrt(N)+O(1)`, yet

`E_N^Q(Y_N)=Y_N(N)^2+o(N)`.

Thus even a discrete law imposed at every integer up to the horizon can leave an asymptotic equality-ray witness. What the construction is allowed to reprogram is the **correlation of the squarefree signs** and the dependence on the horizon: its signs need not be Möbius-multiplicative, and the witness for `N` need not be the restriction of one infinite source used at all smaller horizons.

The reusable extremizer test is therefore stronger than “use growing-depth physical data.” A candidate source restriction must exclude the equality ray at the scale consumed by the endpoint. If the retained constraints can still be realized by horizon-dependent repair with `o(m_N^2)` energy excess, they cannot by themselves create a fixed critical-scale coercivity gap, no matter how many pointwise constraints they impose.

For this skeleton the next genuinely different currencies are **Möbius sign correlation/multiplicativity, cross-horizon compatibility, horizon-independent coherence of one infinite sign sequence, or another source law whose violation has `Theta(N)`-relevant cost**. These are not interchangeable: FD-120 proves only that squarefree support, unit amplitudes, terminal normalization and one global divisor identity do not supply them.

**Boundary.** FD-120 does not show that the actual Mertens trajectory approaches the equality ray and does not rule out a successful growing family of divisor identities, multiplicativity constraints, or cross-horizon theorem. Its witness is deliberately nonmultiplicative and horizon-dependent. The conclusion is only that single-horizon pointwise admissibility—even across the full horizon—can be too weak when the missing arithmetic information is relational.