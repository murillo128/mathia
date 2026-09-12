# MI-016 — Completed Weil order is a one-sided index ledger; finite spectral isolation transports only through source-specific control beyond the sharp logarithmic form modulus

**Evidence level:** proved observability/order/exhaustion and fixed-window certification through PL-282, plus PL-283--PL-284's conditional computer-assisted spectral certificate and PL-285's sharp translation-topology restriction; completed arithmetic positivity remains open.

PL-278--PL-282 show that the negative Morse index is a one-sided ledger under aperture growth and that any fixed positive window can in principle be certified finitely, but they give no aperture-uniform coercivity. PL-283--PL-284 provide one concrete positive base point, conditional on an external interval-arithmetic certificate: at `a=0.8` the localized Weil operator has a simple even ground state and a positive lower margin `8.9e-18`.

PL-285 shows why that isolation cannot be propagated by ordinary bounded-operator perturbation. On Suzuki's fixed interval, active arithmetic channels contain compressed translations with displacement `log(n)/a`; infinitesimal nonzero displacement changes can have `L^2` operator-norm difference approaching two even while the active source set is unchanged.

Continuity reappears on the canonical logarithmic form domain, and PL-285 now sharpens both relevant moduli. The full translation operator satisfies

`||T_(h+delta)-T_h||_(H^log -> L^2) ~ 2/sqrt(log(1/|delta|))`,

but the autocorrelation quadratic form relevant to the Rayleigh quotient satisfies the stronger sharp bound `Theta(1/log(1/|delta|))`. The previous Cauchy--Schwarz form estimate lost one square root.

This is an improvement in the correct direction but also a stronger route closure: the inverse-logarithmic form rate is itself sharp for generic `H^log` data. Against the tiny endpoint margin, bare logarithmic regularity still cannot transport positivity a useful macroscopic distance without source-specific structure.

The central distinction is therefore **fixed-window spectral isolation versus quantitative source-specific branch transport after the generic form topology has been optimized**. The next theorem must control the actual low-energy eigenbranch using stronger regularity, arithmetic cancellation among moving channels, or a direct variational identity unavailable to arbitrary logarithmic-energy vectors.

**Boundary.** PL-285 does not rule out cancellation in the complete finite arithmetic sum or stronger regularity of the actual ground state. The endpoint numerical bounds remain conditional on the external certificate. What is closed is improvement obtainable from generic ambient `L^2` perturbation or generic `H^log` regularity alone.