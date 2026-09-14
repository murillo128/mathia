# MI-011 — Single-horizon physical laws can be invisible, while cross-horizon coherence is coercive

**Evidence level:** exact for the floor-quotient Fourier skeleton through [FD-117](../../findings/FD-117-full-cumulative-farey-discrepancy-is-invertibly-equivalent-to-quotient-mertens-data.md), [FD-118](../../findings/FD-118-floor-quotient-frequency-skeleton-is-a-minimal-linear-carrier.md), [FD-119](../../findings/FD-119-fixed-mertens-endpoint-data-cost-only-bounded-energy-on-the-floor-quotient-fourier-skeleton.md), [FD-120](../../findings/FD-120-squarefree-unit-increments-and-one-divisor-identity-still-saturate-the-fourier-skeleton.md), and [FD-121](../../findings/FD-121-coherent-dyadic-horizons-force-a-uniform-fourier-skeleton-energy-gap.md). The single-horizon countermodels are synthetic quotient sources; FD-121 is an exact inequality for any one common real source across two dyadic horizons.

FD-117 shows that the complete cumulative Farey discrepancy field is invertibly equivalent to the quotient-Mertens staircase. FD-118 compresses its same-horizon Fourier data to the divisor-closed floor-quotient skeleton `Q_N`, of size `2 sqrt(N)+O(1)`, without losing that source.

FD-119 identifies the coercivity obstruction inside this reversible carrier. In reindexed source coordinates the skeleton has the exact Möbius equality ray `x_k=m mu(k)/k`, for which every Fourier mode except the first vanishes and the normalized energy is exactly `m^2`. Any fixed true Mertens prefix plus the exact identity `sum_(d<=N)y_floor(N/d)=1` can be grafted onto that ray with only `O_R(1)` additional energy. At the RH-critical amplitude `m_N~sqrt(N)`, fixed-depth truth therefore has vanishing relative cost.

FD-120 shows that **depth by itself is not the missing resource**. For every sufficiently large horizon one can choose a complete increment sequence with `a_N(1)=1`, `a_N(n)=0` on nonsquarefree `n`, and `a_N(n) in {-1,+1}` on every squarefree `n`, while also satisfying the exact physical single-horizon divisor identity and `Y_N(N)=sqrt(N)+O(1)`, yet `E_N^Q(Y_N)=Y_N(N)^2+o(N)`. The construction is allowed to reprogram both squarefree signs and its witness when `N` changes.

FD-121 isolates the second freedom and shows that it is quantitatively essential. For one common source `Y`, define `Delta_H=E_H^Q(Y)-|Y(H)|^2`. Then every `N>=6` satisfies

`Delta_N + Delta_2N >= c_0 (|Y(N)|^2+|Y(2N)|^2)`,

where `c_0=(41-sqrt(1553))/64=0.0248669...`. The proof uses only the shared coordinates visible in mode `2` at horizon `N` and modes `2,4` at horizon `2N`. Therefore the same source cannot be a critical relative near-extremizer at two consecutive dyadic horizons. When both endpoint amplitudes are `Theta(sqrt(N))`, coherence alone costs `Theta(N)` energy.

This changes the reusable extremizer test. A same-horizon source restriction must still be tested against horizon-dependent repair: if it can be realized with `o(m_N^2)` excess, it cannot create a fixed critical-scale gap. But cross-horizon compatibility is different proof currency. It can exclude joint saturation even when it adds no new source coordinate and even before multiplicativity is used.

The remaining distinction is **pairwise versus pointwise coercivity**. FD-121 does not force every horizon away from the equality ray; a common source can in principle alternate between near-saturation and a costly neighboring dyadic scale. To reach an RH-relevant endpoint estimate, a continuation must prevent that alternation, transfer the dyadic excess to the designated large endpoint, or combine overlapping scale constraints with a source law such as Möbius sign correlation/multiplicativity.

**Boundary.** FD-120 does not show that the actual Mertens trajectory approaches the equality ray, and FD-121 does not show that it stays a fixed distance away at each horizon. The durable lesson is sharper: single-horizon admissibility can be asymptotically invisible, whereas exact horizon-independent reuse of one source is already visible at the critical energy scale. What remains open is whether that block-scale visibility can be converted into pointwise arithmetic control.
