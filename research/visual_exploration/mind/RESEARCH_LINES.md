# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Separate low-frequency moment extraction from arithmetic selectivity

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning`, `MI-030-low-frequency-arithmetic-jets-are-physical-moments`.

VIS-259 gives the sharp conditioning cost of an order-`2m` cusp-adapted low-frequency packet: normalized extraction of the first surviving even Taylor coefficient costs total variation `E_m^(-1)b^(-2m)`. VIS-260 propagates Rodgers' fixed-margin theorem error through that same norm. VIS-261 identifies the retained Taylor jet with the corresponding physical-space moment of the Bogomolny--Keating-minus-GUE kernel, and VIS-262 freezes every fixed even moment to an explicit functional `C_(2m)(omega)` of the admissible test weight.

VIS-263 then separates nonzero amplitude from arithmetic selectivity. There is an explicit normalized admissible weight whose Fourier support lies strictly below the first nonzero prime frequency and yet `C_2=1/(2pi^2)` exactly. Every nonconstant zeta/`B` Dirichlet frequency vanishes; the entire quadratic carrier comes from zero-frequency pole compensation.

VIS-264 makes the residual arithmetic coordinate explicit:

`C_2(omega) = hat omega(0)/(2pi^2) - (1/(8pi^4)) sum_p sum_(m>=1) (log p)^2 p^(-m) hat omega''(m log p/(2pi))`.

The first term is the universal DC/pole background; the second is a finite prime-power curvature sampler. Crossing a prime frequency is only an access condition: `hat omega''` may vanish there or different prime-power contributions may cancel.

The live source-content question remains to freeze a weight faithful to the intended edge observable and prove that its **prime-power curvature component** is nonzero at the required normalization after the pole term is removed. The accepted support-edge arithmetic-residual clue already owns that handoff, so no parallel clue is needed. A nonzero residual would establish source selectivity of this fixed-margin quadratic coordinate, not yet the localization or higher-order covariance needed by the original edge--edge statistic.

## Keep theorem-transfer conditioning, source localization and arithmetic content on separate ledgers

VIS-259--VIS-260 show that extracting a low-frequency coefficient pays the packet norm `b^(-2m)` and therefore requires theorem accuracy that beats the same conditioning scale. This is an analytic-access cost, independent of whether the retained coefficient is source-specific.

VIS-265 adds a second transfer constraint using Wang's 2026 short-interval Montgomery theorem. On a zero interval of length `T^theta`, fixed pair-frequency support `[-lambda,lambda]` is available only for `lambda<theta`, with normalized error

`O(1/log T + T^(lambda-theta) log T)`.

Hence support near the Montgomery edge forces the source-window exponent toward one. The fixed physical tent of VIS-128, and likewise any polylogarithmic source window, has effective exponent tending to zero and is not covered for any fixed positive pair-frequency support. Wang therefore supplies genuine local-height control but does not validate the bounded-window support-edge statistic.

Its stated `O(1/log T)` normalized remainder also cannot resolve a deterministic arithmetic coefficient at the same `1/log T` scale. The current route consequently has three independent gates: the packet-conditioning budget, a theorem whose source-window/support class contains the intended statistic, and a remainder smaller than the prime-sensitive residual being extracted. Only after all three are satisfied does the VIS-264 arithmetic carrier become a theorem-valid local support-edge prediction.

Source-height localization and pair-separation weighting must remain distinct. A theorem controlling one cannot be transferred by identifying its window with the other. Moving-edge uniformity and four-level covariance remain further gates beyond the fixed two-level analysis.