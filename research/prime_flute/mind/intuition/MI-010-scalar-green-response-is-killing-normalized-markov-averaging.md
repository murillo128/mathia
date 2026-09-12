# MI-010 — Source-weighted Green strength is exactly defect-scale source avoidance after low screening

**Evidence level:** proved for finite positive sections of the canonical prime-flute boundary response through PF-313; no final physical `P/H` weak/Schatten estimate, actual-source defect domination, or arithmetic discrimination theorem is claimed.

PF-303--PF-308 normalize the assembled constant chain as a killed positive network and show that nonconstant Schur relaxation destroys uniform global constant-sector protection. PF-309--PF-311 then show that the explicit screened reservoir is physical-low at entrance and that its direct post-low high-conversion energy is already small.

PF-312 identifies exactly what inversion can and cannot add. With `T=S^(-1/2)ER^(-1/2)` for the post-low constant/high block, the diagonal-normalized mixed Green block is unitarily equivalent to `-T`. Inversion does not create a new normalized angle; the raw factor `sigma/(1-sigma^2)` splits into the unchanged angle and two diagonal Green strengths.

PF-313 now characterizes those strengths without inversion. Let `F_C=S-ER^(-1)E*` and `G_C=F_C^(-1)`. For any source map `J_C`,

`||G_C^(1/2)J_C||^2 = sup_(x!=0) ||J_C* x||^2/<x,F_C x>`.

Thus `||G_C^(1/2)J_C||<=K` is equivalent to the form inequality

`J_C J_C* <= K^2 F_C`.

In whitened coordinates this is `Jhat_C Jhat_C* <= K^2(I-TT*)`. If `Tv=sigma u`, every bounded source family must therefore satisfy

`||Jhat_C* u|| <= K sqrt(1-sigma^2)`.

Near-unit canonical-correlation directions are harmless only when the physical source dies at their defect scale. The right/reassembly side has the symmetric criterion with `I-T*T`.

This converts a vague inverse problem into a source-versus-energy question. The PF-308 screened traces already give a concrete falsifier: any uniformly controlled source family must have normalized overlap with those traces tending to zero at the fully-shorted-energy rate. An order-one overlap would force the source-weighted Green strength to diverge.

The remaining mixed response still contains three logically distinct currencies: left source defect domination, the unchanged normalized angle/multiplicity, and right reassembly defect domination, with signed cancellation possible after their composition. A return-potential estimate is relevant only if it proves one of the two form dominations; bounding a raw Green block without source alignment is no longer the right target.

**Boundary.** PF-313 does not show that the actual physical source/reassembly maps satisfy the defect-scale inequalities, that `||T||` stays below one, or that divergence of one diagonal strength forces the final signed mixed response to diverge. It identifies the exact condition under which diagonal inverse amplification is invisible to the source.
