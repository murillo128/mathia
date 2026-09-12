# MI-010 — Scalar Green response is killing-normalized Markov averaging, not spectral-gap transport

**Evidence level:** proved for the finite scalar constant-mode pant chain by PF-303--PF-304; no full `P/H` mixed-response bound or arithmetic discrimination is claimed.

PF-298 writes every constant-boundary pant compression as a positive conductance edge plus positive shifted Robin killing. After assembling a finite chain,

\[
H_N=L_{c,N}+D_N,
\qquad
D_N=\operatorname{diag}(d_0,\ldots,d_N),
\qquad
G_N=H_N^{-1}.
\]

The conductance Laplacian annihilates constants, so PF-303 obtains the exact identity

\[
H_N\mathbf1=d,
\qquad
G_Nd=\mathbf1.
\]

In return coordinates this says that the local escape deficit has exactly unit Green potential. A chain can be arbitrarily close to conservative at individual deep rows and still have a uniformly bounded response to forcing paid in the same currency as the escape.

PF-304 identifies the stronger operator structure. Define

\[
P_N:=G_ND_N.
\]

Then `P_N` is nonnegative, row stochastic, and reversible with invariant weight `d`:

\[
P_N\mathbf1=\mathbf1,
\qquad
d_i(P_N)_{ij}=d_j(P_N)_{ji}.
\]

Therefore `P_N` is a contraction on every weighted `ell^p(d)`, `1<=p<=infinity`, and every scalar forcing satisfies

\[
\boxed{
\|G_Nf\|_{\ell^p(d)}
\le
\|D_N^{-1}f\|_{\ell^p(d)}.
}
\]

The familiar pointwise condition `|f|\lesssim d` is only the `p=infinity` endpoint. At `p=1`, bounded total source mass gives a bounded killing-weighted response; at `p=2`, bounded `\sum|f_j|^2/d_j` gives a bounded killing-weighted energy response. For nonnegative forcing the `p=1` mass balance is exact.

This changes the interpretation of PF-297--PF-302. The lack of a depth-uniform scalar spectral gap is not itself the forced-response obstruction. PF-302 proves that scalar round trips are extinguished by accumulated killing; PF-303--PF-304 show simultaneously that the scalar Green inverse is perfectly normalized once source injection is measured against that killing. **Survival and forced response are different questions, and the correct response norm is source-adapted rather than gap-adapted.**

The unresolved theorem is now a representation/reassembly statement. The real finite `P/H` source extraction must be compared with `D_N`: does the PF-296 coefficient budget imply a uniform `ell^1`, `ell^2`, or `ell^infinity` bound for `D_N^{-1}f`? After scalar averaging, does the nonconstant-mode synthesis map the resulting `ell^p(d)` control into the positive Sobolev and physical-high norm needed by PF-292/PF-290? A failure should identify which source or reassembly component is not paid for by scalar killing rather than merely restating that local returns are nearly conservative.

The Markov/M-matrix mechanism is generic. Any positive conductance network with positive diagonal killing has the same stochasticization, so it carries no prime-specific or RH-specific information by itself. Arithmetic content can enter only through the actual prime-dependent source extraction, nonconstant-mode coupling, or final observable.

**Boundary.** PF-303--PF-304 are finite-section scalar statements. The constant mode is not proved invariant under the complete boundary DtN/Schur problem, small killing weights can hide large pointwise response in integrated norms, and no bounded `P/H` reassembly map is established. The result removes a scalar spectral-gap requirement; it does not prove the physical global response theorem.