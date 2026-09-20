# MI-057 — Paired-cube completion defect transfers Banach type ceilings into source-relative mixture fidelity

**Evidence level:** exact geometric synthesis from [AF-458](../../findings/AF-458-rademacher-type-controls-sparse-mixture-fidelity-through-paired-secants.md) and [AF-459](../../findings/AF-459-average-cube-completion-defect-controls-type-p-fidelity.md), interpreted against AF-456--AF-457. No arithmetic source is asserted to have small completion defect.

For a bounded barycentric marking `phi:A->Y` with `sup_a ||phi(a)||<=M`, Banach type limits source-relative TV fidelity through the geometry of the normalized completed-secant carrier `C`. For a paired block `B=((a_1,b_1),...,(a_k,b_k))`, write

`q_epsilon^B=(1/(2k)) sum_j epsilon_j (delta_(a_j)-delta_(b_j))`

and measure how well the physical carrier realizes the full sign cube by

`D_B(C)=E_epsilon dist_1(q_epsilon^B,C)`, `D_k(C)=inf_B D_B(C)`.

If `Y` has Rademacher type `p in [1,2]`, AF-459 gives the quantitative source-relative ceiling

`kappa_C(F_phi) <= M [T_p(Y) k^(1/p-1) + D_k(C)]`.

AF-458 is exactly the zero-defect case. The obstruction therefore does not require every sign orientation to be physically completable. If a fraction at least `1-theta` of the orientations of one paired cube is exactly completable, then `D_B(C)<=2 theta`; for `p>1`, asymptotically dense completion already forces the lower gain to vanish when `theta->0`.

The contrapositive identifies the source resource needed for stable bounded affine fidelity. If `kappa_C(F_phi)>=kappa_0>0`, then every admissible scale must satisfy

`D_k(C) >= max(0, kappa_0/M - T_p(Y) k^(1/p-1))`.

Thus the useful arithmetic invariant is no longer binary cube incidence but **average normalized-secant separation from every large paired sign cube**. Deleting a few bad orientations does not provide an escape; a source that keeps a uniform discriminator in a nontrivial-type target must remain quantitatively cube-poor on average.

This condition is still only a necessary obstruction. Large `D_k(C)` does not construct a positive inverse modulus, and some other family of completed secants may collapse even when paired cubes are far away. The source carrier, its normalization, and the target category remain load-bearing.

**Boundary.** The result is affine/barycentric and uses TV/`ell^1` source geometry with bounded marks. Type `p=1` gives no decaying type term. Finite alphabets impose a cutoff on `k`, and neither AF-458 nor AF-459 covers nonlinear encoders or proves that the physical prime source has any particular asymptotic completion profile.