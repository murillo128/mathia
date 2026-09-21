# MI-066 — Negative gamma margin does not imply zeta-frequency spectral tightness

**Evidence level:** exact/classical spectral synthesis from [WI-388](../../findings/WI-388-dilute-high-frequency-sidebands-defeat-gamma-to-spectral-tightness.md), using the gamma-negative fixed profile and fixed-profile source-perforation framework of WI-385--WI-387. The Riemann--von Mangoldt and Fourier inputs are classical; the line-specific content is the scale match at the WI-387 spectral-tightness interface.

The negative archimedean budget and zeta-frequency compactness are different resources. Start from a smooth even fixed-width profile `phi` with a strict negative lobe margin `B_phi<=-3 beta`. Orthogonalize a modulation `phi(s)cos(Rs)` to obtain a normalized carrier `nu_R`. Its archimedean difference energy grows only logarithmically,

`E(nu_R)=O(log R)`.

Mix only a vanishing amount of this carrier into the base profile,

`g_R=sqrt(1-epsilon_R) phi + sqrt(epsilon_R) nu_R`,

with `epsilon_R=c/log R`. For sufficiently small fixed `c`, the total lobe energy still satisfies `B_(g_R)<=-beta`, while `||g_R'||_2` grows at least like `R/sqrt(log R)`. The family therefore leaves every uniformly `H^1`-bounded class without spending the negative gamma margin.

The same sideband carries Fourier mass of order `1/log R` across a fixed-width packet around frequency `R`. Riemann--von Mangoldt guarantees a sequence of such packets containing `Omega(log R)` zero ordinates. Along those carrier frequencies the two factors cancel exactly in scale: `Omega(log R)` samples times `Omega(1/log R)` mass per sample leave `Omega(1)` zeta-sampled energy at arbitrarily large frequencies. Hence

`lim_(T->infinity) sup_j sum_(|gamma|>T) m_gamma |G_j(i gamma)|^2 != 0`.

This is a concrete failure of the WI-387 uniform spectral-tightness hypothesis under a uniform negative archimedean margin. It does not contradict WI-387 because the constructed profiles have unbounded Sobolev complexity.

Exact source slots do not restore tightness. For each fixed sideband profile, WI-386's source-perforation convergence allows the endpoint to be taken far enough out that both the archimedean error and the Fourier perturbation are negligible relative to the `1/sqrt(log R)` sideband amplitude. A diagonal choice therefore preserves both the negative gamma margin and the escaped zero-frequency packet after exact source perforation.

The reusable mechanism is the **cost-times-sampling-density balance**. The archimedean form prices a carrier only by `log R`, so a `1/log R` mass allocation is affordable; the zeta spectrum supplies `log R` samples in a suitable fixed-width packet, so that vanishing mass still has order-one destination effect. A local or integrated negative budget cannot be treated as a compactness norm unless it directly controls the destination-weighted tail.

**Boundary.** The construction does not produce a positive Weil coercive gap, does not defeat the recurrence theorem inside its hypotheses and does not contradict RH. The endpoint phases `sin^2(gamma A_k/2)` are not controlled by the diagonal source-slot choice. What WI-388 rules out is only the implication “uniform negative gamma energy plus exact source zeros => uniform zeta-frequency tightness.” Any stronger no-go theorem for unbounded-complexity fixed-width profiles needs a genuinely stronger moment/norm or direct arithmetic tail control; any positive escape must still turn the escaped spectral mass into a phase-stable positive floor.
