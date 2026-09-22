# MI-068 — Escaping logarithmic spectral compactness can open a positive RH Weil floor

**Evidence level:** RH-conditional constructive synthesis from [WI-391](../../findings/WI-391-source-exact-dilute-carriers-open-a-positive-rh-weil-floor.md), completing the phase-stability question left open by MI-066 and sharpening the logarithmic compactness boundary of MI-067.

The fixed-width no-gap mechanism is genuinely a compactness theorem, not a consequence of source exactness or negative archimedean margin alone. WI-391 constructs source-exact fixed-width trials with a dilute high-frequency carrier whose spectral location escapes so rapidly that the logarithmically compact recurrence argument no longer applies, while the base lobe keeps a uniform negative archimedean margin.

Under RH, choose carrier frequencies `R_k` and endpoint scales `A_k` with `A_k->infinity` but `A_k/log log R_k->0`. Riemann--von Mangoldt density then supplies enough zeros in the high-frequency packet that the carrier's `1/log R_k` Fourier mass accumulates to an order-one sampled contribution. The endpoint phase factors cannot simultaneously erase that packet: the construction yields

`liminf W[f_k] >= kappa > 0`

for some fixed `kappa`, while exact prime-power source perforation remains negligible.

This closes the gap between “spectral mass can escape” and “escaped mass can support a positive floor” on the RH side. The decisive resource is controlled failure of uniform logarithmic Fourier-tail integrability together with a carrier/end-point scaling that beats phase recurrence. Exact source zeros and fixed width are compatible with that escape.

The result also fixes the interpretation of the earlier no-go. WI-387--WI-390 remain decisive for every uniformly logarithmically compact family, including uniformly superlogarithmic moment-bounded families. WI-391 does not refute them; it demonstrates that once the compactness hypothesis is deliberately violated in a source-admissible way, the zero-floor recurrence obstruction can disappear.

**Boundary.** The construction is RH-conditional and therefore is not an RH proof or an unconditional coercive gap. It does not show that every noncompact family has a positive floor, nor does it provide a converse characterization of admissible spectral escape. Its role is structural: logarithmic spectral compactness is load-bearing, and phase-stable source-exact escape is possible outside that class.