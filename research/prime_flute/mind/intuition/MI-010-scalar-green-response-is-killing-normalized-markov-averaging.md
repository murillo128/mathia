# MI-010 — Scalar Green response is killing-normalized averaging; the global post-scalar Schur angle saturates

**Evidence level:** proved for finite positive sections of the canonical prime-flute boundary response through PF-307; no source-weighted Schur-resolvent bound, weak/Schatten estimate, or arithmetic discrimination is claimed.

PF-298 writes every constant-boundary pant compression as a positive conductance edge plus positive shifted Robin killing. PF-303--PF-305 then normalize the assembled constant chain as

`H_N=L_(c,N)+D_N`, `G_N=H_N^-1`, `S_N=D_N^(1/2)G_ND_N^(1/2)`,

with `0<S_N<=I` and `||S_N||=1`. Scalar return depth is therefore ideal-neutral after killing normalization: a scalar-mediated mixed response must pay compactness or ideal decay at its normalized conversion interfaces.

PF-306 identifies the first operator omitted when constants are embedded back into the full positive response. With

`A_N=[[H_N,B_N],[B_N*,J_N]]>0`,

set `K_N=H_N^-1/2 B_N J_N^-1/2`. Then `||K_N||<1` for each finite section, `||K_N||^2` is exactly the worst fraction of raw constant energy screened by nonconstant relaxation, and the constant Green block acquires `(I-K_NK_N*)^-1`.

PF-307 decides the global-gap alternative for the canonical PF-205 seam-cut response. Combining PF-216's macroscopic raw constant floor with PF-217's cheap tangential relaxation produces tail blocks and growing finite tangential cutoffs for which the normalized conversion angle `C_(M,L)` satisfies

`1-||C_(M,L(M))||^2 <= C[(1+log M)/M + P_M^-eta] -> 0`.

Thus `sup_(M,L)||C_(M,L)||=1`. A depth-uniform global Schur-angle gap is not merely unavailable; it is false in this representation. The nearly unit directions are explicit constant-to-tangential screening modes on long tail blocks.

This does **not** imply a large physical mixed response. Operator-norm saturation can be harmless if the actual normalized source and reassembly maps have vanishing overlap with the screened directions, and one witness direction per block gives no singular-value counting law. The live object is therefore source- and target-adapted, for example a bound on `(I-CC*)^-1/2 Z` for the genuine source range or the corresponding two-sided compression.

The reusable lesson is that **normalizing away scalar return exposes a conversion obstruction, but the full conversion norm is itself too pessimistic**. Once a near-unit angle is geometrically forced, the only useful currency is accessibility/multiplicity of those nearly screened directions under the actual physical vertices.

**Boundary.** PF-307 concerns the canonical PF-205 constant/nonconstant split and proves existence of saturating directions, not density of near-unit singular values, noncompactness, weak-trace failure, or an RH consequence. Any materially different interface representation needs its own blockwise dictionary before importing the numerical angle statement.