# MI-042 — Scalar spectral smoothing changes the Korobov--Vinogradov power class only at polynomial order growth

**Evidence level:** exact asymptotic synthesis from [VIS-341](../../findings/VIS-341-vk-scale-stable-under-finite-spectral-smoothing.md) and [VIS-342](../../findings/VIS-342-vk-power-gain-requires-growing-truncation-order.md). This classifies the scalar zero-free-width/truncation model; it is not a pointwise theorem for Wang's `Q` and does not assert that an arbitrary packet has a scalar effective order.

Write the Korobov--Vinogradov width as

`nu(t)=A (log t)^(-2/3)(log log t)^(-1/3)`

and consider

`Omega_r(u)=inf_t {u nu(t)+r(u) log t}`.

VIS-341 gives, for fixed `r>0`,

`Omega_r(u) ~ C_A r^(2/5) u^(3/5) (log u)^(-1/5)`.

Thus a finite increase in polynomial high-frequency decay changes the leading constant but not the characteristic `3/5,-1/5` power class.

VIS-342 removes the loophole that a slowly growing scalar order might change that conclusion. Factoring out `r(u)` gives the exact identity

`Omega_r(u)=r(u) Omega_1(u/r(u))`.

Whenever `u/r(u)->infinity`, this yields

`Omega_r(u) ~ C_A u^(3/5) r(u)^(2/5) [log(u/r(u))]^(-1/5)`.

If `r(u)=u^(o(1))`, the `u`-power remains `3/5+o(1)`. If `r(u)=u^(alpha+o(1))` with `0<=alpha<1`, the power becomes `(3+2 alpha)/5`; a fixed gain `delta` over `3/5` therefore requires `alpha=5 delta/2` within this scalar model.

This turns “growing effective smoothing” into a quantitative gate. A scalarizable Wang-packet explanation cannot claim a new fixed power class from finitely, polylogarithmically, or otherwise subpolynomially many inverse-frequency powers. It must derive polynomial growth of the effective scalar order from the actual transform/truncation estimate while keeping leakage, constants, source norms and destination errors under control.

The alternative is genuinely non-scalar. A signed, arithmetic or nonstationary mechanism may evade this classification if its estimate cannot be reduced to `u nu(t)+r log t`; but the reason for that failure of scalarization must be explicit rather than inferred from the use of many scales or coefficients. Any surviving gain must still pass the exact inverse/derivative ledger of VIS-333--VIS-340.

**Boundary.** VIS-341--VIS-342 do not improve the PNT remainder, prove new nonstationarity of the normalized theta error, or identify Wang's multiplier with a particular `r(u)`. The transition regime `r(u)` comparable with `u` is outside the stated asymptotic, and genuinely non-scalar packet mechanisms require their own analysis.