# MI-010 — Low-band Schur screening leaves only a normalized post-screening high-angle/amplification problem

**Evidence level:** proved for finite positive sections of the canonical prime-flute boundary response through PF-311; no theorem for the final physical `P/H` inverse/reassembly, normalized post-low angle gap, weak/Schatten estimate, or arithmetic discrimination is claimed.

PF-303--PF-305 normalize the assembled constant chain as a killed positive network. PF-306--PF-308 show that nonconstant Schur relaxation destroys any uniform global constant-sector protection and makes the killing-normalized constant Green block diverge on explicit screened tail traces.

PF-309 shows that the original witness is asymptotically physical-low at entrance. PF-310 closes the loophole that a tiny high-frequency tail might be load-bearing: exact witnesses confined to one fixed physical low band still have macroscopic killing mass, vanishing low-shorted energy ratio, Schur conversion norm tending to one, and divergent killing-normalized constant Green response. The near-singular reservoir is genuinely low-band.

PF-311 then controls the first residual physical-high vertex after that low screening. Decompose a finite positive boundary form into constants `C`, retained physical-low modes `L`, and physical-high modes `H`. After shorting `L`, write the remaining blocks as

`[[S_L, E_LH], [E_LH*, R_H]] > 0`.

Positivity gives the exact inequality

`||R_H^(-1/2) E_LH* x||^2 <= <x,S_L x>`.

For PF-310's witnesses, `<x,S_Lx>/m_0[x] -> 0`, so their **absolute direct residual high-conversion energy is also `o(m_0)`**, uniformly through finite high Galerkin sections. The known low-band reservoir therefore cannot immediately eject macroscopic killing-normalized energy into the high sector before inversion.

The sharp boundary is equally important. Defining the normalized post-low angle

`T_H=S_L^(-1/2) E_LH R_H^(-1/2)`,

positivity only gives `||T_H||<1` in each finite section. A scalar positive model realizes any fixed residual fraction `rho_H` in `[0,1)`, even while the absolute residual energy tends to zero. After the high sector is also shorted, the mixed inverse contains the amplifier `(I-T_HT_H*)^(-1)`. Thus small absolute coupling does **not** imply a harmless Green response.

The reusable distinction is now four-way: full-space screening, fixed-low-band screening, absolute residual high conversion, and normalized inverse-amplified high output are separate resources. PF-311 removes raw post-screening high energy as the explanation for the explicit family. The next theorem must control the post-low normalized angle away from one on the source-reached subspace, control the source/reassembly overlap with near-unit directions, or prove a multiplicity/Schatten bound strong enough to absorb the inverse amplification.

**Boundary.** PF-311 does not prove `rho_H(x^(M))->0`, a uniform gap `||T_H||<=1-delta`, or small final mixed inverse output. Its inequality is sharp at the fraction level. Later inversion/reassembly may still amplify a small residual coupling, and other source-accessible families remain possible.