# MI-065 — Successive primorial boundary transport is support-determined through pairwise and one-vertex Laplacian updates

**Evidence level:** exact/asymptotic synthesis from [PC-389](../../findings/PC-389-successive-primorial-boundary-transport-is-buchstab-deletion.md) and [PC-390](../../findings/PC-390-primorial-boundary-laplacian-transport-is-next-prime-gap-degree-shedding.md).

Let `N_x` be the primorial through `x`, let `q=p_+(x)`, and take the prime-only boundary window `H=x^u`, `1<u<2`. For all sufficiently large `x`, the successive support update is exactly

`R_x^+(H)=R_x(H)\{q}`.

For the normalized pairwise inverse-chord kernel, the next-shell matrix is the principal minor obtained by deleting `q`, up to `o_op(1)`. The canonical same-window pairwise transport is therefore one Buchstab deletion followed by ordinary interlacing; it supplies no distributed cross-level carrier beyond the sieve-selected support.

The graph Laplacian keeps more of the deletion bookkeeping but no independent source datum. If `C` is the old Laplacian principal submatrix and `D=diag(kappa_N(a-q))` is the incident-degree loss, then

`A^+=C-D+o_op(1)`.

Writing `r` for the prime after `q` and `g=r-q`, monotonicity of the positive inverse-power kernel gives

`||A^+-C||_op=(tau^2+4 pi^2 g^2)^(-alpha)+o(1)`.

Thus Laplacian nonconvergence is a real arithmetic fluctuation, but its strongest one-step signal is exactly a monotone re-encoding of the next consecutive prime gap already present in the primitive support.

Kron elimination makes the same deleted star nonlocal: `M_q=D-ww*/s` is full rank on the mean-zero subspace, yet the entire mesh is determined by the single incident-weight vector `w`. Full-rank fill-in is therefore not a second carrier.

The remaining cross-level question must leave this one-step support-determined category: couple several Buchstab deletions, retain phases or changing state, use a growing history, a sign-changing/nonmonotone operator, or exhibit another invariant that cannot be reconstructed from the sequence of support-gap incident vectors.

**Boundary.** PC-389--PC-390 cover the prime-only window `1<u<2`, the declared positive monotone inverse-power chord family, and one-step pairwise/Laplacian/Kron transport. They do not classify `H>=q^2` multi-vertex deletion, sign-changing kernels, nonlinear multi-step histories, or phase/fiber operators.