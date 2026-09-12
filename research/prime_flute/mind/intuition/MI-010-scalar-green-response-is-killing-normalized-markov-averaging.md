# MI-010 — Scalar Green response is killing-normalized averaging with an ideal-neutral middle

**Evidence level:** proved for the finite scalar constant-mode pant chain by PF-303--PF-305; no full `P/H` mixed-response factorization or arithmetic discrimination is claimed.

PF-298 writes every constant-boundary pant compression as a positive conductance edge plus positive shifted Robin killing. After assembling a finite chain,

\[
H_N=L_{c,N}+D_N,
\qquad
D_N=\operatorname{diag}(d_0,\ldots,d_N),
\qquad
G_N=H_N^{-1}.
\]

PF-303 obtains the exact Green normalization `G_Nd=1`. PF-304 identifies `G_ND_N` as a reversible Markov kernel, so scalar forced response is contractive in the killing-weighted `ell^p(d)` scales. The absence of a depth-uniform scalar spectral gap is therefore not itself the forced-response obstruction.

PF-305 exposes the corresponding Hilbert/operator-ideal structure. Define

\[
S_N=D_N^{1/2}G_ND_N^{1/2}.
\]

Then

\[
0<S_N\le I,
\qquad
S_ND_N^{1/2}\mathbf1=D_N^{1/2}\mathbf1,
\qquad
\|S_N\|=1.
\]

Thus killing normalization removes apparent Green amplification but does **not** create a strict contraction. More importantly, any scalar-mediated mixed response

\[
M_N=R_NG_NF_N
\]

has the exact factorization

\[
M_N=(R_ND_N^{-1/2})\,S_N\,(D_N^{-1/2}F_N).
\]

The scalar middle cannot worsen the compactness or symmetric-ideal class of a controlled normalized conversion vertex: bounded multiplication by a contraction preserves every two-sided symmetric ideal. But it cannot manufacture the missing ideal decay either, because its norm is exactly one and the conservative direction survives.

The reusable lesson is that **return depth is not an independent compactness currency once the correct killing normalization is exposed**. Any scalar-mediated failure of the complete PF route must live at one of the two conversion interfaces—source injection relative to `D_N^{1/2}`, physical reassembly relative to the same scale—or in the failure of the true nonconstant response to factor through the scalar reservoir at all.

This changes the next calculation. Rather than estimate `G_N` more sharply, derive the actual finite `P/H` forcing and reassembly maps and test

\[
D_N^{-1/2}F_N,
\qquad
R_ND_N^{-1/2}
\]

in the physical energy spaces required by the mixed target. A compact/weak-Schatten estimate on one vertex with a uniform bound on the other propagates automatically through the scalar chain; blowup or noncompactness identifies the genuine conversion obstruction.

**Boundary.** PF-303--PF-305 are finite-section scalar statements. They do not prove that the constant mode is invariant under the complete boundary DtN/Schur problem, that the physical forcing factors through the scalar chain, or that either normalized conversion vertex has the required ideal bound. The mechanism is generic to positive conductance-plus-killing networks and carries no prime-specific information by itself.
