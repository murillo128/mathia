# MI-016 — Completed Weil order is a one-sided index ledger; finite spectral isolation now requires state-specific control beyond the sharp full-comb form modulus

**Evidence level:** proved observability/order/exhaustion and fixed-window certification through PL-282, plus PL-283--PL-284's conditional computer-assisted spectral certificate and PL-285--PL-286's sharp generic transport restrictions; completed arithmetic positivity remains open.

PL-278--PL-282 show that the negative Morse index is a one-sided ledger under aperture growth and that any fixed positive window can in principle be certified finitely, but they give no aperture-uniform coercivity. PL-283--PL-284 provide one concrete positive base point, conditional on an external interval-arithmetic certificate: at `a=0.8` the localized Weil operator has a simple even ground state and a tiny explicit positive margin.

PL-285 shows why that isolation cannot be propagated by ordinary bounded-operator perturbation. On Suzuki's fixed interval, active arithmetic channels are compressed translations with displacement `log(n)/a`; ambient `L^2` operator norm is discontinuous. On the canonical logarithmic form domain, the relevant quadratic-form modulus improves to the sharp generic rate `Theta(1/log(1/|delta|))`, still far too weak against the endpoint margin.

PL-286 closes the remaining generic finite-channel cancellation loophole in the first source-static interval, where the active prime powers are exactly `2,3,4`. A high-frequency plane-wave witness plus Kronecker phase locking makes the `2` and `3` channels change coherently, while the relation `4=2^2` makes the `4` channel complete a full phase turn. Consequently the **complete active von-Mangoldt comb** has the same sharp inverse-logarithmic worst-case form modulus as the individual-channel estimate.

Thus generic cancellation among the moving arithmetic channels cannot improve transport either. The surviving bridge must be **state-specific**: stronger uniform regularity or tail control of the actual low eigenbranch, cancellation forced by its eigen-equation/variational structure, or another source-specific identity unavailable to arbitrary logarithmic-energy vectors.

The central distinction is therefore fixed-window spectral isolation versus quantitative transport of the actual canonical low state after both generic topology and generic finite-channel cancellation have been exhausted.

**Boundary.** PL-286 is a worst-case form-domain result. It does not show that the actual ground state realizes the phase-locked witness, nor does it rule out cancellation forced by the eigen-equation or stronger regularity of that branch. The endpoint numerical bounds remain conditional on the external certificate.