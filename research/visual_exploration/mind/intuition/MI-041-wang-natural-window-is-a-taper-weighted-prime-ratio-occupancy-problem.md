# MI-041 — Wang fragmentation renormalizes to parent-scale repetition and conductor before deeper aggregation is necessary

**Evidence level:** exact/literature-backed synthesis from VIS-313--[VIS-327](../../findings/VIS-327-wang-parent-length-decimation.md), plus classical rational mechanical/Christoffel geometry and the dimension-two Selberg upper-bound sieve. No prime-pair asymptotic or RH consequence is claimed.

The cutoff-free Wang remainder has no useful global nearest-frequency spacing, but dyadic shells reduce the finite-window loss to prime-ratio occupancy with destination taper. VIS-317--VIS-323 identify the faithful coordinates: a unimodular Bézout chart preserves both prime exclusions, the thin domain has only a few mechanical branches, center-gap decimation converts them into fixed-gap diagonal runs, and the aggregate Hardy--Littlewood weight of those runs is neutral at the relevant scale.

VIS-324 prices the first-level run length. The standard translation-uniform two-linear-form Selberg sieve gives the required two-prime upper-bound scale whenever `k<=M^(1-delta)` at the natural Wang window. VIS-325 then shows that `k>L` is not representation-final: the observed branch is a lower-denominator rational mechanical path up to `O(1)` determinant indices.

VIS-326 resolves the first Christoffel split inside that word. Put `J=floor(m/k)` and `q=m mod k`. The two parents have lengths `q` and `k-q`; their Wang monodromies are primitive consecutive-coordinate vectors. For `J>=2` both parent steps are nondegenerate, while for `J=1` the externally selected parent is axis-degenerate and the complementary parent remains nondegenerate.

VIS-327 converts that structural split into an exact finite-window arithmetic estimate. For a parent `(p,s)` with `d s-p k=±1`, an `s`-step changes the Wang prime-coordinate pair by one constant vector `G` except at at most one edge. If `s<L`, residue classes modulo `s` therefore form at most `s+1` affine runs with repeat scale `L/s`. On each run the two-form resultant satisfies the exact identity

`Delta=p h_0-s t_j(h_0)`

and the uniform bound `|Delta|<=4s`. The same renormalization that makes the step small therefore makes the arithmetic conductor small; it does not merely rearrange the word.

For a nondegenerate parent the classical two-form sieve gives

`P_j << Lambda_s [L/log^2(3+L/s)+s]`,

where `Lambda_s` grows only logarithmically with the parent-scale conductor. At the natural Wang scale, every nondegenerate `s<=M^(1-delta)` yields only `O_delta(log log M)` excess over the natural two-prime cell scale, well below the final taper allowance. Thus for `J>=2` every unresolved center must have `min(q,k-q)=M^(1-o(1))`; for `J=1`, the same conclusion applies to the complementary nondegenerate parent, while a short axis parent alone remains one-dimensional.

The reusable lesson is stronger than “fragmentation should be renormalized.” A faithful renormalization is useful when it simultaneously controls **block length, arithmetic dimension and conductor** on the finite window actually observed. Once those quantities are carried together, polynomially short nondegenerate first parents are already harmless. The remaining obstruction is genuinely near-full-scale nonrepetition, not hidden local-factor growth.

The next discriminator is therefore whether deeper continued-fraction parents or offset aggregation can create a shorter nondegenerate packet in the surviving `M^(1-o(1))` regime without enlarging the resultant or destroying the Wang taper. If no such packet exists, a discrepancy/energy formulation may be the right representation rather than further symbolic factorization.

**Boundary.** VIS-327 is an upper-bound closure for polynomially short nondegenerate first parents. It does not prove that deeper parents exist at useful scales, solve the `J=1` axis-short/complement-long case, provide a prime-pair asymptotic/lower bound, or establish the final Wang natural-window theorem. Any continuation must preserve the two-prime local arithmetic and destination taper.