# MI-028 — Dyadic screening forces an archimedean reserve, but the endpoint needs signed discrepancy beyond density-one cancellation

**Evidence level:** exact structural consequence from [WI-301](../../findings/WI-301-screened-prime-ladders-force-a-uniform-archimedean-reserve.md), combined with the corrected parity-free explicit-formula decomposition [WI-241](../../findings/WI-241-pole-cancels-pnt-main-density-leaving-prime-discrepancy.md).

For every nonzero real compactly supported one-signed test, dyadic screening forces

`q_arch(f) >= c_0 ||f||_2^2`,  `c_0=8.9e-18`.

Therefore a one-signed dyadically screened test with `Q_W(f)<=0` must carry at least that much unscreened arithmetic interaction. Complete prime-power screening is impossible in this class. This reserve theorem is aperture-independent and does not require the earlier first-crossing/null-mode setup.

WI-241 shows why this reserve is not yet the source coercivity needed at the endpoint. For a general compactly supported complex test, the pole contribution cancels the density-one prime main term exactly. What remains is a bounded nonnegative density-one autocorrelation remainder `R` plus the **signed** smoothed discrepancy `Delta_Lambda` of `d(psi-x)`. Schematically,

`Q_W = Q_gamma + R - 2 Delta_Lambda`.

Thus total prime-power mass and signed arithmetic discrepancy are different resources. The universal main density can be large while contributing nothing after pole cancellation. A lower bound on unscreened interaction therefore cannot be promoted to the signed deficit needed to offset a negative spectral index.

On the odd negative-index branch, if Weil positivity holds, WI-241 turns the requirement into a uniform one-sided condition on `Delta_Lambda`. Oddness is load-bearing only for that negative-index consequence; the pole/main-density cancellation itself is parity-free.

The reusable lesson is a two-stage source audit. **Screening geometry can force arithmetic mass to remain, but the explicit formula may quotient out its universal component.** The proof must identify which part of the forced mass survives that quotient with the correct sign. Here that survivor is a discrepancy relative to `psi(x)~x`, not the total prime-power reserve.

The live bridge is therefore to derive a source-specific signed `Delta_Lambda` bound from the actual prime distribution, possibly using the one-signed reserve as auxiliary structure, or to develop a different sign-changing test mechanism. Merely localizing the reserve to some odd-prime lag is insufficient unless it also controls the density-subtracted signed quantity.

**Boundary.** The constant `c_0` comes from rigorous computer-assisted interval evidence, not a Lean proof. One-sign is essential to WI-301. The signed discrepancy inequality is a necessary consequence on the stated odd/positivity branch, not an unconditional theorem about `psi-x`, and none of these results proves unrestricted Weil positivity or RH.