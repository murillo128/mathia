# MI-005 — Stable tails are residual discovery minus future screening after the common prediction mode is removed

**Evidence level:** supported by NB-063--NB-079. The finite-dimensional continuation, prediction, branching and q-adic information identities are exact; no arithmetic estimate proving summable residual imbalance or closing the stable-tail criterion is established.

NB-074--NB-076 write the uncancelled continuation charge as `J_(R,N)=L_R-C_(R,N)`, with `L` raw continuation volume and `C` a nonnegative cross-cut prediction charge. NB-077 shows both currencies survive exact integer branching. NB-078 then puts them on one q-adic refinement ledger: if `ell_m` and `c_m` are the new continuation and prediction charges, `J_m=J_0+sum(ell_m-c_m)`.

NB-079 removes a common mode that made that comparison unnecessarily large. At each refinement there are three nonnegative charges `G`, `P`, and `S` with

`ell=G+P`,

`c=G+S`,

so the net obstruction is exactly `P-S`. Here `G` is predictability of newly resolved fine past from the already available coarse future; it can be large but cancels identically. `P` is residual discovery: fine-past continuation information still present after coarse-future conditioning. `S` is future screening: the amount removed when the new future branch contrasts are admitted.

Along an exact q-adic ray,

`J_m=J_0+sum_(r<=m)(P_r-S_r)`.

A nonzero stable tail must therefore make this residual sum diverge on every such ray. Conversely, one unbounded ray with `P_r<=S_r+e_r` and `sum e_r<infinity` kills the stable tail. The algebraic criterion is equivalent to NB-078's raw increment criterion, but the proof burden is smaller because all refinement growth already explained by coarse-future prediction has been eliminated before any arithmetic estimate is attempted.

The live source theorem should now target the unresolved fine structure itself: edge/past-contrast continuation after coarse-future conditioning versus screening by future contrasts at the same refinement level. Mesoscopic localization remains one possible mechanism, but it is no longer necessary to control the full continuation and prediction volumes or even their common large component.

**Boundary.** Neither `P<=S` nor summability is automatic; the net increment can have either sign. The Gaussian language is an exact log-determinant representation of deterministic Gram matrices. NB-079 removes a universal common mode but supplies no Nyman-specific arithmetic inequality by itself.