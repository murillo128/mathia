# MI-065 — Fixed-width profile freedom cannot open a Weil coercive gap

**Evidence level:** exact spectral/explicit-formula synthesis from [WI-386](../../findings/WI-386-fixed-width-even-profile-changes-cannot-open-a-positive-weil-gap.md) and [WI-387](../../findings/WI-387-uniformly-h1-bounded-adaptive-fixed-width-profiles-still-cannot-open-a-positive-weil-gap.md), extending the cosine-specific zero-floor result of WI-385.

The fixed-width Weil quasimode mechanism is not tied to one lobe shape. For any sufficiently regular real even compactly supported fixed profile `g`, translate two copies apart with odd sign. Under RH the Weil energy is a nonnegative uniformly almost-periodic trigonometric sum that already vanishes at separation zero, so recurrence produces arbitrarily large near-zero separations. The endpoint lattice `A_k=log(k+1)` has vanishing mesh and captures a near-zero subsequence, while exact prime-power source perforation changes the full form only by `o(1)`.

WI-387 shows that even fixing the profile was unnecessary. Let the normalized fixed-width even profile `g_k` vary arbitrarily with the endpoint. If the zeta-zero spectral tails are uniformly tight,

`lim_(T->infinity) sup_k sum_(|gamma|>T) m_gamma |G_k(i gamma)|^2 = 0`,

then finite-frequency Bohr/Kronecker recurrence gives coefficient-independent common return times for the low-frequency head, and the tail is uniformly negligible. Therefore `liminf W[f_k]=0` under RH. A uniform `H^1` bound is a concrete sufficient condition for this tightness through the uniform decay `|G_k(i gamma)|<<1/|gamma|`.

The obstruction is therefore not “the wrong profile” or even “a profile that does not adapt.” It is **spectral tightness at fixed physical width**. Endpoint-dependent shape adaptation with bounded Sobolev complexity cannot open a uniform positive Weil tariff. Within this class, escaping the recurrence theorem requires increasing high-frequency/rough-profile complexity strongly enough to destroy uniform spectral tightness; this is only a necessary change of resource, not evidence of positivity.

The profile-by-profile explicit formula from WI-386 still explains the fixed-profile ledger: the recurrent arithmetic-polar reserve exactly matches the archimedean debt. WI-387 reaches the adaptive conclusion more directly through the spectral representation and does not require a common stationary profile decomposition across `k`.

**Boundary.** The RH-side zero-floor conclusion holds for uniformly spectrally tight fixed-width even families, including uniformly `H^1`-bounded ones. The stronger non-RH divergence available for suitable fixed profiles is not claimed for adaptive families, whose transforms may vary so as to suppress selected off-line contributions. Unbounded-complexity fixed-width families, growing-width, multiscale/nonlocal trials and changed graph/domain restrictions remain separate regimes.