# MI-026 — The threshold archimedean remainder reverses the Hopf sign

**Evidence level:** literature-backed exact synthesis from [PL-329](../../findings/PL-329-source-amplitude-controls-first-prime-reflection.md), [PL-332](../../findings/PL-332-uniform-endpoint-remainder-transports-the-first-prime-coefficient.md), and [PL-333](../../findings/PL-333-first-prime-archimedean-antimarkov-hopf-obstruction.md).

PL-329--PL-332 reduce the first-prime orientation problem to a uniform source-amplitude estimate and one fixed-threshold nonvanishing coefficient `C_0` at `a_0=(1/2)log2`. A natural attempt is to obtain that nonvanishing from positivity of the threshold state plus the Hopf boundary law for the Dirichlet logarithmic Laplacian.

PL-333 shows that the completed threshold operator has the wrong structure for that import. At `a_0`, the `p=2` translation has zero overlap, but Suzuki's archimedean remainder contributes an integral kernel

`k_0(x,y)=-a_0 r''(a_0(x-y))`

that is strictly positive on the whole square. On opposite endpoint neighborhoods this correction dominates the Markov jump cross-term in exactly the wrong direction, producing explicit `w` with

`q_(a_0)(|w|)>q_(a_0)(w)`.

The first Beurling--Deny contraction inequality therefore fails. Positivity improving for the principal logarithmic-Laplacian form is not inherited by the full completed-Weil form at the first-prime threshold.

There is a second sign reversal at the PDE level. Even if a nonnegative threshold eigenstate `u` were known independently, its equation has

`L_Delta u = scalar*u - 2 K_0 u`.

Because `K_0u` remains strictly positive up to the boundary while `u` vanishes there, `L_Delta u` approaches a strictly negative endpoint value. Near the boundary the state is a strict logarithmic-Laplacian **subsolution**, not the supersolution required by the standard Hopf theorem.

The reusable lesson is that a limiting/principal Dirichlet form can have the right boundary positivity law while a bounded completed remainder destroys precisely the order property needed to transfer it at a finite threshold. Fixed-threshold nonvanishing must be proved for the full operator or by an identity insensitive to that sign reversal; it cannot be inferred from the principal form alone.

**Boundary.** Failure of the Markov property does not prove the threshold ground state changes sign and does not prove `C_0=0`. PL-333 blocks a proof route, not the desired nonvanishing statement. The remaining gate is still `C_0!=0`, but its proof must use the full completed-Weil threshold structure.