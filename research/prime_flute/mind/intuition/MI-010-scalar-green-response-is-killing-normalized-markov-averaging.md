# MI-010 — Post-low inversion preserves the normalized angle; the remaining amplification is diagonal Green strength

**Evidence level:** proved for finite positive sections of the canonical prime-flute boundary response through PF-312; no final physical `P/H` weak/Schatten estimate, source-weighted Green bound, or arithmetic discrimination theorem is claimed.

PF-303--PF-308 normalize the assembled constant chain as a killed positive network and show that nonconstant Schur relaxation destroys uniform global constant-sector protection. PF-309 proves that the explicit screened reservoir is asymptotically physical-low at entrance, and PF-310 shows that exact witnesses confined to one fixed physical low band still saturate the screening.

PF-311 controls the first residual physical-high conversion after those low modes are shorted. For the remaining positive constant/high block

`[[S_L,E_LH],[E_LH*,R_H]] > 0`,

positivity gives

`||R_H^(-1/2) E_LH* x||^2 <= <x,S_L x>`.

The PF-310 witnesses have `<x,S_Lx>/m_0[x] -> 0`, so their absolute direct high-conversion energy is also `o(m_0)`. The known low-band reservoir cannot eject macroscopic killing-normalized high energy before inversion.

PF-312 identifies exactly what inversion can and cannot add. Let

`T_H=S_L^(-1/2) E_LH R_H^(-1/2)`

and whiten the post-low block to `Q=[[I,T_H],[T_H*,I]]`. If `G_C,G_CH,G_H` are the inverse blocks, then

`G_C^(-1/2) G_CH G_H^(-1/2) = -T_H`.

In the original physical coordinates the same normalized Green cross block is unitarily equivalent to `-T_H`. Therefore its singular values are **exactly the same** as the original post-low canonical-correlation singular values. Block inversion does not create a second or worse normalized angle.

The raw factor `sigma/(1-sigma^2)` on a near-unit singular channel is instead the product of the unchanged angle `sigma` with diagonal Green strengths `(1-sigma^2)^(-1/2)` on the two sides. For external source/reassembly maps `J_C,J_H`, the mixed response factors exactly as

`J_C* G_CH J_H = (G_C^(1/2)J_C)* Gamma_G (G_H^(1/2)J_H)`,

where `Gamma_G` is a contraction with the singular values of `T_H`.

The frontier is therefore sharper than after PF-311. One may still prove a source-relevant gap for `T_H`, but if near-unit directions survive, the missing quantity is the **source-weighted diagonal Green strength** carried by those directions: `G_C^(1/2)J_C` and `G_H^(1/2)J_H`, together with their counting/ideal behavior. The accepted return-potential route is relevant only if it can bound one of these source-weighted diagonal factors; PF-312 does not assume that identification.

**Boundary.** PF-312 does not show that `||T_H||` stays away from one, that diagonal Green blocks remain bounded along the Galerkin limit, or that physical source/reassembly maps avoid their large directions. It removes a false extra obstruction: inverse amplification changes strength, not the normalized post-low angle.