# MI-007 — Moment-null shrinking packets pay an order-matched total-variation gate

**Evidence level:** exact finite-window moment obstruction, minimax total-variation bound, and effective-CUE calibration audit through VIS-147

## Core intuition

Vanishing moments are not selective unless the source and null occupy different functional directions after the exact observable is frozen. In the current support-edge companion, imposing zero second frequency moment cancels the quadratic low-frequency response of every smooth finite-window correction, not merely the CUE null. The first common deterministic distinction is therefore quartic or higher.

Shrinking support then imposes a matching information bill: retaining an order-one `2j`-th moment on bandwidth `b` costs at least `b^(-2j)` total variation, and any uncertainty controlled linearly by that same variation is amplified in lockstep. Rescaling cannot manufacture signal-to-error separation.

## Strongest justified principle

VIS-145 proves that for any finite-window signed kernel `H`, the centered-cosine response has leading term `2 pi^2 mu_2(H) q^2` with quartic remainder. A packet with `m_2=0` therefore removes the complete quadratic term regardless of whether `H` is universal or arithmetic. The hoped-for zeta-specific quadratic survivor is impossible inside this common representation.

VIS-146 gives the exact capacity inequality `|m_{2j}(nu_b)| <= b^(2j)||nu_b||_TV`. Quartic normalization after second-moment cancellation needs variation at least `b^-4`, and a sup-norm uncertainty `epsilon_b` produces worst-case packet error `epsilon_b||nu_b||_TV`. The robust ratio is consequently bounded by `|A_{2j}|b^(2j)/epsilon_b`, independent of packet scaling. For the quartic route, `epsilon_b=o(|A_4|b^4)` is the necessary asymptotic gate.

VIS-147 then audits the candidate source coefficient. The standard finite-height `rho_bar^-2` and `rho_bar^-3` two-point corrections are already tangent to effective finite-CUE size and scale calibration. Moreover the frozen observable uses a growing `Theta(L)` source window, so fixed-spacing remainder estimates do not control the required fourth spatial moment of the post-calibration residual.

## Program consequence

Derive the arithmetic residual **after** effective-CUE size/scale calibration in the exact bounded-source coordinate, and estimate its growing-window fourth moment together with the theorem/transfer error in a norm that survives packet integration. Test the deterministic inequality `epsilon_L=o(|A_4(L)|b_L^4)` before tuning packet shapes or computing covariance.

If that gate fails, move to a different observable or genuinely wider/nonlocal information channel rather than adding more moment cancellations, which only raises the total-variation exponent.

## Counterevidence / boundary

The argument does not prove that the quartic zeta residual vanishes. Its coefficient may grow with the source window, or structured oscillation may provide stronger error control than a worst-case sup/variation envelope. A source-specific contribution may also lie outside the common smooth centered-cosine representation.

The minimax bound is deliberately robust; additional correlation between the packet and the actual error could improve practical behavior, but such correlation would itself require a theorem and cannot be assumed.

## Epistemic status

**Exact design boundary: second-moment cancellation removes every common quadratic finite-window response, and the first surviving quartic channel must beat an order-matched `b^4` error gate that packet rescaling cannot improve; the required post-calibration growing-window zeta coefficient is not yet known.**

## Falsification criterion

Construct a smooth finite-window correction whose quadratic response survives an `m_2=0` packet, or exhibit a quartic-normalized shrinking packet with total variation `o(b^-4)`, or derive the required post-calibration zeta quartic coefficient and error bound in a regime that violates the stated minimax capacity inequality.
