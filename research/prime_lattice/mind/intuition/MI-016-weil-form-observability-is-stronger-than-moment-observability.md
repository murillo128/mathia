# MI-016 — Completed Weil order is a one-sided index ledger; finite spectral isolation transports only through the form topology

**Evidence level:** proved observability/order/exhaustion and fixed-window certification through PL-282, plus PL-283--PL-284's conditional computer-assisted spectral certificate and PL-285's exact translation-topology restriction; completed arithmetic positivity remains open.

PL-278--PL-282 separate completed high-frequency positivity, aperture monotonicity, global exhaustion, and finite fixed-window certification. They show that the negative Morse index is a one-sided ledger under aperture growth and that any fixed positive window can in principle be certified finitely, but they give no aperture-uniform coercivity.

PL-283--PL-284 provide one concrete positive base point, conditional on an external interval-arithmetic certificate: at `a=0.8` the canonical localized Weil operator has a simple even ground state, a positive lower margin `8.9e-18`, and a much larger gap to the second level. This removes local degeneracy as the immediate obstruction.

PL-285 shows why that isolation cannot be propagated by ordinary bounded-operator perturbation. On the fixed interval used in Suzuki's scaling, the active arithmetic channels contain compressed translations whose displacement is `log(n)/a`. The translation family is not continuous in `L^2` operator norm; infinitesimal nonzero displacement changes can have norm difference approaching two even when the active source set is unchanged.

Continuity reappears on the canonical logarithmic form domain. Bounded `H^log` energy suppresses the high-frequency packets responsible for the norm jump and gives a logarithmic translation modulus. This is enough for qualitative compactness/continuity but generically far too weak to turn the tiny `a=0.8` margin into a useful radius reaching the next source event.

The central distinction is therefore **fixed-window spectral isolation versus quantitative form-level transport**. The next useful theorem must control the moving ground branch in the source's actual form topology, perhaps through stronger zero/ground-state regularity, arithmetic cancellation among channels, or a direct variational inequality. Source-static support does not mean norm-static operator geometry.

**Boundary.** PL-285 proves a termwise topology obstruction and a generic `H^log` modulus; it does not prove the full finite arithmetic sum is norm-discontinuous and does not preclude source-specific cancellations. The endpoint numerical bounds remain conditional on the external certificate.