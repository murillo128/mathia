# MI-025 — Source amplitude controls first-prime reflection; a uniform remainder transports the critical coefficient

**Evidence level:** exact/source-selected synthesis from [PL-326](../../findings/PL-326-fixed-aperture-endpoint-laws-do-not-orient-the-first-prime-crossing.md) through [PL-332](../../findings/PL-332-first-prime-boundary-coefficient-l2-continuity.md).

The first-prime activation isolates a shrinking reflected correlation whose positive critical profile is only of size `delta/L_delta`, with `L_delta=log(a_delta/delta)->infinity`. PL-326--PL-327 show that fixed-aperture endpoint asymptotics and canonical half-log regularity do not determine its sign: an antisymmetric residual of state amplitude `L_delta^(-1/2)` on the moving layer can reverse the reflection while remaining small in natural endpoint norms.

PL-329 shows that the **exact source equation** sees that residual at the reciprocal scale. If `S_delta` is the endpoint-source amplitude and `C_delta` the selected critical coefficient, the source equation preserves the positive reflection whenever

`(1+S_delta)/(|C_delta| sqrt(L_delta)) -> 0`.

The threshold is sharp for the known counterfamily: its state amplitude is only `L_delta^(-1/2)` while the coercive source term magnifies it to `S_delta~sqrt(L_delta)`.

PL-330 and PL-331 explain why qualitative topology cannot replace this gate. The full operator family is norm-resolvent continuous and isolated eigenbranches can be phase-aligned continuously in `L^2`, yet the hostile layer tends to zero even in every fixed logarithmic Fourier seminorm while still reversing the much smaller moving sign reserve.

PL-332 identifies the exact circumstance in which ordinary branch continuity becomes useful again. If the source estimate supplies a family-uniform endpoint expansion

`g_delta(Q)=C_delta Q^(-1/2)+O(Q^(-1))`,

then `C_delta` can be approximated uniformly from any sufficiently remote **fixed** logarithmic block. The block does not move with `delta`, so `L^2` branch convergence transports its moment and gives `C_delta -> C_0`. The uniform asymptotic remainder removes the escaping-tail freedom that made `L^2` and all-fixed-log topology too weak on their own.

This changes the dependency structure of the first-prime problem. Once the actual branch satisfies the uniform PL-329 source/remainder estimate, coefficient collapse is no longer a separate moving-family gate. It reduces to the single fixed-aperture question `C_0 != 0`; if that holds and `S_delta` is uniformly bounded, the PL-329 ratio tends to zero automatically.

The reusable lesson is that topology can transport a boundary coefficient only **after a uniform asymptotic uniqueness estimate has made that coefficient observable on a fixed region**. Without the uniform remainder, the coefficient can change on a tail escaping to infinity at exponentially small `L^2` cost.

**Boundary.** PL-332 does not prove the uniform source/envelope estimate for the actual completed-Weil eigenbranch and does not prove `C_0 != 0`. It orients only the first `p=2` activation. Later prime-power channels and global Weil positivity remain separate problems.