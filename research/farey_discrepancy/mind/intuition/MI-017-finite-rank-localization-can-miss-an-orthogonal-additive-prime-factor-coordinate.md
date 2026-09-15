# MI-017 — Fixed congruence localization always leaves a finer additive prime-factor direction

**Evidence level:** exact matched-control obstruction from [FD-138](../../findings/FD-138-clt-scale-rank-localization-still-hides-an-orthogonal-prime-color-ancestry-wall.md), sharpened to every exact central rank by [FD-139](../../findings/FD-139-exact-central-rank-conditioning-still-hides-the-prime-color-wall.md) and to every fixed congruence-periodic coordinate alphabet by [FD-140](../../findings/FD-140-every-fixed-congruence-coordinate-alphabet-misses-a-finer-prime-color-wall.md), using the audited squarefree Sathe--Selberg/Selberg--Delange inputs recorded there

FD-137 shows that exact multiplicative-rank conditioning exposes the moving `omega(n)` wall hidden by scale averages. FD-138 demonstrates that this repair is source-specific rather than generically coercive.

Define the additive prime-color coordinate

`D(n)=sum_(q|n) chi_4(q)`

on squarefree integers and flip the Möbius sign across the half-space `D(n)=0`, while preserving a fixed finite-rank Möbius anchor. This produces one common infinite source with positive-density coefficient disagreement.

FD-138 already shows that inside a single factor-two shell and a positive-Gaussian-mass central rank window, the mean prime-ancestry defect tends to zero uniformly over all prime directions. FD-139 removes the remaining possibility that the width of that rank window is hiding the wall. For every exact central rank `omega(n)=m` in a fixed CLT band, the squarefree Sathe--Selberg parent cell remains of order `T/sqrt(loglog T)`, while the boundary `D in {-1,0}` occupies only order `T/loglog T`. Hence the normalized ancestry defect is still `O(1/sqrt(loglog T))` uniformly over all primes inside **each exact rank cell**.

FD-140 shows that this is not repaired by adding finitely many congruence coordinates. Fix any modulus `Q` and condition on the complete vector of exact squarefree prime-factor counts in every reduced residue class modulo `Q`. Choose a new odd prime `ell` with `ell` coprime to `Q` and a nonprincipal quadratic character `psi mod ell`. The additive color

`G(n)=sum_(q|n) psi(q)`

refines every visible mod-`Q` class into two asymptotically balanced prime populations by the Chinese remainder theorem. The coarse vector fixes the sums of those refined populations but leaves a transverse signed difference with variance of order `loglog T`. Consequently the two-value ancestry wall `G in {-1,0}` has only `O((loglog T)^(-1/2))` conditional mass in every central exact coarse-vector cell, uniformly over all prime directions, while the matched source still differs from Möbius on positive density.

The obstruction is therefore stronger than “one statistic can miss another.” **Every fixed congruence-periodic alphabet has a strictly finer coprime coloring direction.** Equivalently, any finite family of strongly additive prime weights that factors through one fixed modulus can be defeated without changing the visible exact coordinate vector. Exactness of the conditioning does not compensate for missing coordinate directions.

This identifies the next genuinely different regimes. A positive coefficient-side theorem must either let arithmetic resolution grow with scale while retaining enough mass and uniform local-limit control in its exact cells, use nonperiodic/source-intrinsic prime weights justified by the Farey/Möbius construction, or prove that the physical admissible source cannot realize the transverse half-space controls at all. Merely enlarging a fixed periodic alphabet kills only finitely many already-visible colors and leaves the refinement mechanism intact.

**Boundary.** FD-138--FD-140 are matched obstructions to ancestry-to-source coercivity, not claims that the constructed sources satisfy the physical Mertens envelope or repeated-square Farey endpoint. FD-140 closes fixed congruence-periodic additive alphabets; it does not prove failure for growing moduli, nonperiodic source-native coordinates, destination-side Fourier coercivity, or every finite family of arbitrary prime weights. Those are distinct proof obligations.
