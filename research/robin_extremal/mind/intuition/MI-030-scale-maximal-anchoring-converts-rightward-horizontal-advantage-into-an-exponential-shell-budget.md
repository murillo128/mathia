# MI-030 — Scale-maximal anchoring converts rightward horizontal advantage into an exponential shell budget

**Evidence level:** exact leading-layer Robin reduction from [RE-146](../../findings/RE-146-scale-maximality-turns-zero-density-into-an-exponential-rightward-shell-budget.md), combined there with the classical Ingham zero-density estimate; it sharpens the reciprocal-radius visibility accounting of [RE-145](../../findings/RE-145-reciprocal-box-visibility-has-an-exponential-scaled-radius-floor.md).

Choose the actual zeta zero whose leading Robin atom is maximal at scale `U`. For a zero farther to the right by `Delta=beta-beta_0>=0`, scale maximality gives the exact coefficient inequality

`e^(U Delta) q_rho <= 1`,

where `q_rho=|d_rho|/|d_rho0|`. Thus a rightward displacement `R/U` forces `q_rho<=e^-R` and hence forces the ordinate to grow exponentially in `R` through the Robin coefficient law `|d_rho| asymp (1+gamma^2)^-1`.

Looking at an earlier time `tU` with `t<=1-eta` turns the same maximality relation into the fractional moment bound

`|a_rho,0(tU)|/|a_rho0,0(tU)| <= q_rho^eta`.

If `2 eta` exceeds the relevant Ingham density exponent, dyadic summation makes the sufficiently-rightward shell exponentially small in the same scaled radius `R`, up to the explicit polynomial cost of the anchor ordinate. For an algebraically strong scale-maximal anchor this cost is polynomial in `U`, so a sufficiently large `R=lambda log U` kills the rightward shell.

The reusable mechanism is the **variational choice of anchor before applying a population estimate**. Zero density alone could not improve the generic rightmost-transfer loss in RE-142; scale maximality first converts horizontal advantage into coefficient/height cost, after which zero density becomes effective. This is not a stronger density theorem but a change in what quantity the density estimate is asked to sum.

Together with RE-145, both the local reciprocal-box floor and one exterior component are now priced exponentially in the same radius variable. The unresolved problem is a synchronized rate comparison at one observation point: the local witness must coexist with the earlier subwindow required for the fractional-moment estimate, while the near-left cancellation layer and vertically remote but horizontally near zeros still need separate budgets.

**Boundary.** RE-146 is leading-layer only and requires a scale-maximal anchor, an algebraic strength regime, and enough earlier-window slack to choose `eta` above half the density exponent. It does not control the near-left layer or vertically remote near-horizontal zeros and does not prove that the RE-145 local floor dominates the rightward shell. The insight is the scale-maximality-to-fractional-moment conversion, not a completed Robin/RH argument.