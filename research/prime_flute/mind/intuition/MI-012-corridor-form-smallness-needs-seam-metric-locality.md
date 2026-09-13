# MI-012 — Coefficient-level shear locality is strong; seam-metric transport is the remaining direct-angle gate

**Evidence level:** exact for the two-metric obstruction of PF-319 and for the strengthened coefficient-level Pöschl--Teller locality of PF-242. PF-242 proves exponential mode separation and cut-uniform trace/Hilbert--Schmidt leakage for the raw hypercycle shear multiplier; it does not prove the seam-normalized mixed corner of the full normalized Schur difference required by PF-318.

PF-319 separates two metrics that cannot be identified for free. If positive forms `A` and `B` satisfy a small relative Loewner error, then `E=B^(-1/2)(A-B)B^(-1/2)` is small in operator norm, and low rank would convert that into the PF-318 mean-square scale **in the same `B` metric**. The physical direct angle is instead normalized by the seam form `Q`, where

`D_Q=Q^(-1/2)(A-B)Q^(-1/2)=C^* E C`, `C=B^(1/2)Q^(-1/2)`.

The two-dimensional countermodel in PF-319 shows that fixed small `||E||` gives no bound on a mixed low/high corner of `D_Q` unless the relevant source/target pieces of `C` are controlled. Thin flat corridors exhibit exactly the potentially large conversion, so a stronger corridor Loewner sandwich alone cannot close the physical angle.

The strengthened PF-242 now proves that the **canonical coefficient itself is not the source of broad mode mixing**. In the exact Pöschl--Teller basis, `cos(theta)` is tridiagonal and the hypercycle slope is an analytic function of that Jacobi operator. Consequently a jump of `d` mode indices costs `O(beta^d)`. Across an unbuffered contiguous cut, the same expansion gives uniformly

`||L_M M_b H_M||_(S_1)=O(beta)`, `||L_M M_b H_M||_(S_2)^2=O(beta^2)`.

With `beta_n=O(P_n^-1)`, the raw shear already has the squared Hilbert--Schmidt scale required by PF-318, even without paying the logarithmic low-rank factor. Thus the earlier alternative “prove actual mode locality” has been resolved at the multiplier level.

The remaining theorem is more specific: **transport this ideal locality through the physical normalization and nonlinear operator assembly**. One needs a restricted corridor-to-seam conversion on the low/high pieces that does not destroy the `P_n^-2` cut leakage, or a direct estimate showing that resolvent/Schur completion and finite-pant geometry preserve an equivalent mean-square bound. The unresolved issue is no longer whether the hypercycle coefficient can directly throw mass across the spectral cut; it is whether the physical metric and elimination map amplify that already-local coefficient.

**Boundary.** PF-242 does not imply the PF-318 seam-normalized estimate, compactness of `Z_LH`, or control of the independent channel `T_H`. PF-319 does not show that the real metric conversion is bad; it only proves that such control cannot be inferred from corridor-relative form smallness alone.