# MI-005 — Stable-tail diagnostics must price future depth against outer conditioning

**Evidence level:** supported by NB-063--NB-081. The continuation, prediction, branching, q-adic and variable-horizon identities are exact; NB-080 supplies an exact matched outer false positive for fixed depth, and NB-081 computes the sharp screening scale on the same controls. No arithmetic criterion closing the Nyman stable tail is established.

NB-074--NB-079 write the uncancelled continuation charge as a refinement ledger and remove the universal common prediction mode. At each exact q-adic refinement there are nonnegative charges `G`, `P`, and `S` with `ell=G+P`, `c=G+S`, so `J_m=J_0+sum(P-S)`. A nonzero stable tail forces this residual to diverge on every fixed-ratio refinement ray, while boundedness on one unbounded ray kills the tail.

NB-080 shows why a fixed-ratio converse fails. The boundedly invertible outer control `D_j=(I-rho V_m)e_j`, `0<rho<1`, has zero stable tail and uniformly conditioned global Gram, yet a positive-density boundary layer receives only finitely many descendant generations and keeps `J` linear in the prefix size.

NB-081 makes future enlargement an exact part of the ledger rather than an ad hoc repair. If the copied horizon is enlarged, the gain is a nonnegative screening charge `H`, giving `J^+-J=P-S-H`. On the matched outer control, a depth-`L` future horizon satisfies

`J_(R,m^L R-1) ~ R rho^(2L)`

for fixed `0<rho<1`. Thus the fixed-depth false positive disappears once `L` grows logarithmically in `R`; the critical depth is `L~log R/[2 log(1/rho)]`. At the outer but noninvertible endpoint `rho=1`, however, `J~R/(L+1)`, so boundedness requires `L` of order `R` and vanishing requires still deeper screening.

The reusable principle is that a finite-horizon prediction residual is meaningful only together with a **screening-depth/conditioning law**. The same outer source can look extensively nonlocal at fixed depth and asymptotically benign at a depth tuned to its inverse conditioning. A stable-tail diagnostic should either allow enough future depth for healthy controls, subtract the calibrated outer boundary cost, or isolate a mode that persists under arbitrarily deep screening.

**Boundary.** NB-081 calibrates explicit stationary outer controls; it does not prove that the arithmetic Nyman innovations have the same screening law. Qualitative outerness is not enough to infer logarithmic depth because the `rho=1` endpoint is much slower. The remaining arithmetic work is to derive the relevant quantitative source conditioning or a different target-sensitive certificate.