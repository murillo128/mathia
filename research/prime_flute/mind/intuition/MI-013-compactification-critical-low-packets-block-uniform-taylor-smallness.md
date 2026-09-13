# MI-013 — Compactification-critical low packets block uniform pre-projection Taylor smallness

**Evidence level:** exact for the unprojected compactified cuff-cell form through [PF-322](../../findings/PF-322-physical-low-packets-retain-critical-compactified-transverse-energy.md). This is not a lower bound for the completed shear-deleted intrinsic `L/H` angle; the pant quotient, seam-energy normalization, physical projections and common completion may still cancel the exhibited component.

The seam scale `s_n` tends to zero, and PF-233 writes the compactified transverse form schematically as `T_(a_n)=s_n^2 T_tilde_n`. It is tempting to treat `s_n` as a uniform small parameter and apply the even Taylor expansion of the transfer function before the physical low/high angle is formed.

PF-322 gives an explicit obstruction. A fixed physical Fourier band on a cuff of length `ell_n` contains `O(ell_n)` modes. Equal-coefficient zero-mean Dirichlet packets in that band retain a fixed amount of `L^2` mass in an `O(1)` neighborhood of the receding cell seam. Under the fixed-axis compactification, the transverse potential weights that region by `cosh^2(tau)`.

The exact prime-flute geometry makes the two scales cancel:

`cosh(ell_n/2)=coth(h_n/2)`, while `s_n=(h_n+h_(n+1))/2 >= h_n/2`.

Hence `s_n cosh(ell_n/2)>1`, and for the explicit nonconstant physical-low packets

`liminf s_n^2 a_(n,cell)[U f_n] > 0`.

So **the whole physical-low sector is not uniformly small in the unprojected compactified form**, despite `s_n->0`. The issue is not the constant mode; growing low-band dimension lets admissible packets follow the seam where compactification contributes the reciprocal scale.

This does not contradict PF-320. Intrinsic positive-form angles can remain stable even when raw or intermediate energies are large because their own diagonal normalization and common completion can absorb that scale. The missing direct-channel theorem must therefore be proved after the operations that define the actual shear-deleted angle, not by a uniform Taylor estimate on the raw compactified low sector.

**Research consequence.** Propagate the seam-centered witness through the actual one-cusp-pant quotient, PF-205 seam-energy normalization, physical `L/H` projections and PF-320 completion. Either prove that those steps eliminate the critical component strongly enough to meet PF-321's superlinear angle target, or quantify the surviving singular-value/Hilbert--Schmidt leakage against the PF-318 endpoint budget.

**Boundary.** The conditional channel `T_H` is untouched, and no RH or weak-trace conclusion follows from the cell-form obstruction alone.
