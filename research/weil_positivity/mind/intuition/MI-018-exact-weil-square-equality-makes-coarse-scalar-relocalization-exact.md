# MI-018 — Exact Weil-square equality makes coarse scalar relocalization exact before positivity is even asked

**Evidence level:** exact route closure from [WP-294](../../findings/WP-294-weil-square-exactness-forces-mobius-relocalization.md), building on cone linearization in WP-288 and scalar relocalization uniqueness in WP-293. No Weil-positivity theorem is claimed.

WP-293 shows that if a one-channel scalar arithmetic convolution recovers the Mangoldt coefficients exactly, the kernel is uniquely Möbius and the reciprocal-zeta zero screen returns. A possible escape was to keep only approximate or coarse coefficients while asking the final quadratic readout to agree exactly with the Weil finite term on autocorrelation squares.

WP-294 closes that escape. Equality on the full `C_c^infty(R)` autocorrelation cone already forces equality of the underlying Hermitian distributions. Polarization recovers all mixed convolution pairings, and Dixmier--Malliavin factorization then shows that a distribution annihilating every square difference annihilates every compact smooth test. Since the positive log-integer atoms are isolated, distributional equality forces coefficientwise equality after all.

For a scalar source-native convolution this gives the rigid chain

`exact Weil-square finite term -> exact Mangoldt distribution -> a*log = Lambda -> a=mu -> 1/zeta`.

So “approximate coefficients but exact final square form” is not a distinct one-channel scalar architecture. Exact target equality silently upgrades the coarse recovery back to exact arithmetic relocalization before any positivity argument enters.

A smooth finite-place-clean completion cannot absorb the discrepancy either. Atomic coefficient errors at `+/- log N` can be cancelled only if the supposedly non-finite channel imports compensating delta masses at those same finite places, in which case the arithmetic localization problem has simply moved channels rather than disappeared.

The surviving escape must therefore change more than coefficient accuracy. A genuinely multi-channel coupling, operator-valued or nonlinear upstream construction, non-translation-invariant/boundary-conditioned recovery, or a restricted/approximate intermediate criterion with a separate theorem reaching the exact Weil form lies outside the scalar theorem. But exactness of the final Weil quadratic form cannot itself be weakened away if the endpoint is Weil positivity.

The reusable distinction is **approximate internal representation versus exact destination equivalence**. Approximation can be meaningful only if the destination topology/test class tolerates it and an independent stability theorem transfers it. On the full exact Weil square cone, there is no annihilator in which a scalar arithmetic error can hide.

**Boundary.** WP-294 concerns direct one-channel scalar arithmetic convolution and exact equality on the full canonical test class. It does not rule out approximate equality on restricted panels, several coupled channels, operator-valued recovery, boundary-dependent maps or nonlinear source geometry. Those alternatives still need an exact endpoint theorem.