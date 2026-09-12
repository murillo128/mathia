# MI-010 — Scalar Green response is killing-normalized averaging, but nonconstant screening is visible to the full killing-normalized constant sector

**Evidence level:** proved for finite positive sections of the canonical prime-flute boundary response through PF-308; no theorem for the final physical `P/H` entrance/reassembly compression, weak/Schatten estimate, or arithmetic discrimination is claimed.

PF-298 writes every constant-boundary pant compression as a positive conductance edge plus positive shifted Robin killing. PF-303--PF-305 then normalize the assembled constant chain as

`H_N=L_(c,N)+D_N`, `G_N=H_N^-1`, `S_N=D_N^(1/2)G_ND_N^(1/2)`,

with `0<S_N<=I` and `||S_N||=1`. Scalar return depth is therefore ideal-neutral after killing normalization.

PF-306 identifies the first operator omitted when constants are embedded back into the full positive response. With `C_N=H_N^-1/2 B_N J_N^-1/2`, the constant Green block acquires the exact backreaction factor `(I-C_NC_N*)^-1`. PF-307 proves that the canonical tail geometry has no uniform angle gap: explicit long-block screening modes force `||C_(M,L(M))|| -> 1`.

PF-308 resolves the source-access question for the **entire killing-normalized constant sector**. The same PF-217 screened traces satisfy

`<t,D_M t> >= c M`

while their fully shorted energy obeys

`<t,H_(M,L)^eff t> <= C(1+log M+M P_M^-eta)`.

Hence the generalized inverse Rayleigh quotient gives

`||D_M^(1/2)(H_(M,L)^eff)^-1D_M^(1/2)|| -> infinity`.

The nearly screened directions are therefore not made harmless merely by weighting the constant source with the canonical killing. PF-305 remains exact inside the scalar chain, but the protection ends after nonconstant relaxation: the same normalization cannot simultaneously neutralize the Schur backreaction.

This narrows the surviving route again. The relevant object is no longer the full constant source space, but the **actual physical `P/H` source and reassembly maps that precede and follow it**. A positive theorem must show that those narrower maps avoid/suppress the screened profiles, that signed reassembly cancels their amplification, or that dangerous directions are sufficiently sparse for the final two-sided response to satisfy the required ideal estimate.

The reusable lesson is that **a source normalization can remove one reservoir while leaving the next conversion singular on source-accessible directions**. After a global norm is bad, it is not enough to restrict to a coarse “physical-looking” sector; the restriction must be the exact source/target range consumed by the final observable.

**Boundary.** PF-308 proves divergence of canonical finite-section killing-normalized constant Green blocks. It does not prove that the final physical `P/H` mixed response is unbounded, noncompact, or outside weak trace class, and it gives no density law for dangerous singular directions. A materially different interface representation requires its own blockwise dictionary.