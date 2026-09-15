# MI-030 — Scale-maximal anchoring prices the rightward shell; localization removes position mismatch but leaves an exponential rate gap

**Evidence level:** exact leading-layer Robin reduction from [RE-146](../../findings/RE-146-scale-maximality-turns-zero-density-into-an-exponential-rightward-shell-budget.md), sharpened near the finite edge by Pintz density in [RE-147](../../findings/RE-147-pintz-density-shrinks-the-scale-maximal-right-shell-tax-to-edge-order-three-halves.md) and synchronized with the local reciprocal-box witness in [RE-148](../../findings/RE-148-early-window-dilation-removes-location-synchronization-but-exposes-a-rate-gap.md). The local floor comes from [RE-145](../../findings/RE-145-reciprocal-box-visibility-has-an-exponential-scaled-radius-floor.md).

Choose the actual zeta zero whose leading Robin atom is maximal at scale `U`. For a zero farther to the right by `Delta=beta-beta_0>=0`, scale maximality gives the exact coefficient inequality

`e^(U Delta) q_rho <= 1`,

where `q_rho=|d_rho|/|d_rho0|`. Thus a rightward displacement `R/U` forces `q_rho<=e^-R` and hence forces the ordinate to grow exponentially in `R` through the Robin coefficient law `|d_rho| asymp (1+gamma^2)^-1`.

Looking at an earlier time `tU`, `t<=1-eta`, turns the same maximality relation into a fractional moment bound `|a_rho,0(tU)|/|a_rho0,0(tU)| <= q_rho^eta`. Once the relevant zero-density exponent is smaller than `2eta`, dyadic summation makes the sufficiently-rightward shell exponentially small in `R`, up to the explicit polynomial anchor-height factor.

RE-147 improves the density currency near a finite zero edge. If `delta=1-Theta<1/12`, Pintz's explicit high-sigma density exponent is bounded by `3 sqrt(2) delta^(3/2)+18 delta^2`. The early-window loss needed to sum the rightward shell therefore falls to

`tau_P(delta)=(3/sqrt(2)) delta^(3/2)+9 delta^2`,

rather than the linear-in-`delta` Ingham tax. This is a genuine source-side quantitative gain: near the edge, global density becomes cheaper once scale maximality has converted horizontal displacement into the coefficient/height currency it can sum.

RE-148 then removes a different obstruction. The positive-measure visibility theorem of RE-145 is exactly covariant under dilation of the observation variable, so its witness can be placed inside any fixed nonempty early subwindow where the Pintz shell estimate is uniform. The local packet and the rightward shell can therefore be evaluated at the **same observation point**. Position synchronization is no longer open.

The splice reveals that matching functional forms is not enough. With the explicit constants currently available, the localized local floor behaves as `e^(-C_loc R)` with `C_loc>19`, while the rightward shell improves only as `e^(-c_sh R)` with `c_sh<1/2`. Increasing the common reciprocal radius suppresses the certified local floor much faster than the shell upper bound. Thus the current estimates have the wrong exponential ordering for coercivity.

The reusable mechanism has two parts. First, a variational anchor can convert relational displacement into a summable source cost before a population theorem is applied. Second, once local and exterior estimates are expressed in the same scale and at the same point, **their exponents must be compared quantitatively; “both exponential” is not a bridge**. A source theorem helps only if its rate beats the visibility loss actually consumed by the destination.

The remaining Robin options are now concrete: sharpen the positive-measure/local visibility exponent by more than a constant-factor cosmetic improvement, obtain a stronger source-specific exterior exponent, or introduce phase/sign/Euler-product structure that prevents the matched near-left product organization. The near-left layer and vertically remote but horizontally near zeros also remain outside the current shell budget.

**Boundary.** RE-147 uses Pintz density in the finite-edge regime and RE-148 is still a leading-layer splice. Neither controls the near-left or vertically remote pieces, and the displayed exponent mismatch is a limitation of the presently proved constants rather than a theorem that no stronger local or source-specific estimate exists.