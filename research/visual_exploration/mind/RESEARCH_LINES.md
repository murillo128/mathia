# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Separate low-frequency moment extraction from arithmetic selectivity

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning`, `MI-030-low-frequency-arithmetic-jets-are-physical-moments`.

VIS-259 gives the sharp conditioning cost of an order-`2m` cusp-adapted low-frequency packet: normalized extraction of the first surviving even Taylor coefficient costs total variation `E_m^(-1)b^(-2m)`. VIS-260 propagates Rodgers' fixed-margin theorem error through that same norm. VIS-261 identifies the retained Taylor jet with the corresponding physical-space moment of the Bogomolny--Keating-minus-GUE kernel, and VIS-262 freezes every fixed even moment to an explicit functional `C_(2m)(omega)` of the admissible test weight.

VIS-263 then separates nonzero amplitude from arithmetic selectivity. There is an explicit normalized admissible weight whose Fourier support lies strictly below the first nonzero prime frequency and yet `C_2=1/(2pi^2)` exactly. Every nonconstant zeta/`B` Dirichlet frequency vanishes; the entire quadratic carrier comes from zero-frequency pole compensation.

VIS-264 makes the quadratic residual arithmetic coordinate explicit:

`C_2(omega) = hat omega(0)/(2pi^2) - (1/(8pi^4)) sum_p sum_(m>=1) (log p)^2 p^(-m) hat omega''(m log p/(2pi))`.

The first term is the universal DC/pole background; the second is a finite prime-power curvature sampler. Crossing a prime frequency is only an access condition: `hat omega''` may vanish there or different prime-power contributions may cancel.

VIS-269 now extends the same source/background separation to every fixed even Rodgers jet order. The source-dependent term is sampled only at nonzero prime-power frequencies through the corresponding Fourier derivative. Hence any shrinking packet family whose support eventually lies below the first prime frequency is **exactly prime-power blind at every fixed even order**. In the diagonal-safe quadratic class the remaining leading zero-frequency carrier is also killed. Raising the fixed moment order cannot rescue a representation that has already excluded the arithmetic frequency support.

The live source-content question has therefore changed. It is no longer useful to search for a quadratic, quartic or other fixed-order arithmetic residual inside the same shrinking subprime packet class. A viable route must change the support geometry — for example to a fixed-width, translated or multiband packet that reaches selected prime-power frequencies — and prove that the resulting source residual survives the required normalization and theorem-transfer error.

## Keep theorem-transfer conditioning, source localization and arithmetic content on separate ledgers

**Linked intuitions:** `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`, `MI-032-wang-leading-null-packets-need-diagonal-and-cusp-cancellation-at-no-extra-exponent-cost`.

VIS-259--VIS-260 show that extracting a low-frequency coefficient pays the packet norm `b^(-2m)` and therefore requires theorem accuracy that beats the same conditioning scale. This is an analytic-access cost, independent of whether the retained coefficient is source-specific.

VIS-265 applies Wang's 2026 short-interval Montgomery theorem. On a zero interval of length `T^theta`, pair-frequency support `[-lambda,lambda]` requires `lambda<theta`, with normalized fixed-test error controlled by `1/log T + T^(lambda-theta)log T`. Hence a bounded physical source window cannot be reached merely by taking support near the Montgomery edge.

VIS-266 corrects an overly strong reading of the word “fixed.” The proof admits `T`-dependent test functions as long as the support stays inside a fixed margin `lambda<theta` and their seminorms grow slowly enough. For such a family the normalized error is bounded by `O(||g_T'||_inf/L + ||g_T||_inf[1/L + L^(-3/2) + T^(lambda-theta)L + 1/(HL)])`, with `L=log T`.

VIS-267 makes the packet side of that budget scale-sharp. A smooth compact packet of width `b` with vanishing lower even moments and normalized `2m`-th moment must satisfy `||g_b||_inf \gtrsim b^(-(2m+1))` and `||g_b'||_inf \gtrsim b^(-(2m+2))`, with matching constructions. Feeding those unavoidable seminorms into the Wang bound gives the sufficient shrinking-window gate `1/(L b^(2m+2)) -> 0`. For `b=L^(-q)`, this is `q<1/(2m+2)`; in particular the quadratic packet needs `q<1/4` and the quartic packet `q<1/6`.

VIS-268 fixes the remaining leading-functional mismatch. Wang's main term is `g(0)+int |alpha|g(alpha)dalpha`; the VIS-267 moment class canceled the cusp pairing but did not force `g(0)=0`. A diagonal-safe smooth packet can impose both conditions together with the lower even-moment cancellations and unit `2m`-th moment. This extra constraint changes profile constants but **does not change the sharp norm exponents or the gate `q<1/(2m+2)`**.

VIS-269 shows that this generic shrinking-packet interface is now too narrow for fixed-order arithmetic selectivity once its support falls below the first prime-power frequency. The theorem-transfer gate remains mathematically correct, but satisfying it with ever narrower diagonal-safe packets only makes the representation source-blind. The next useful step must redesign the packet support first, then recompute the seminorm/error budget for that altered representation.

What Wang still does not provide is support whose edge itself approaches `theta`, a polylogarithmic physical source window beyond the current seminorm gate, a remainder automatically below every arithmetic residual, or four-level covariance. Source-height localization and pair-separation weighting also remain distinct: a theorem controlling one cannot be transferred by identifying its window with the other.