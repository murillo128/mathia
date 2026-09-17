# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Separate low-frequency moment extraction from arithmetic selectivity

**Linked intuitions:** `MI-024-fixed-margin-pair-correlation-access-has-a-bandwidth-conditioning-budget` through `MI-030-low-frequency-arithmetic-jets-are-physical-moments`.

VIS-259 gives the sharp conditioning cost of an order-`2m` cusp-adapted low-frequency packet: normalized extraction of the first surviving even Taylor coefficient costs total variation `E_m^(-1)b^(-2m)`. VIS-260 propagates Rodgers' fixed-margin theorem error through that same norm. VIS-261 identifies the retained Taylor jet with the corresponding physical-space moment of the Bogomolny--Keating-minus-GUE kernel, and VIS-262 freezes every fixed even moment to an explicit functional `C_(2m)(omega)` of the admissible test weight.

VIS-263 then separates nonzero amplitude from arithmetic selectivity. There is an explicit normalized admissible weight whose Fourier support lies strictly below the first nonzero prime frequency and yet `C_2=1/(2pi^2)` exactly. Every nonconstant zeta/`B` Dirichlet frequency vanishes; the entire quadratic carrier comes from zero-frequency pole compensation.

VIS-264 makes the residual arithmetic coordinate explicit. In the fixed admissible regime,

`C_2(omega) = hat omega(0)/(2pi^2) - (1/(8pi^4)) sum_p sum_(m>=1) (log p)^2 p^(-m) hat omega''(m log p/(2pi))`,

with only finitely many prime powers contributing because `hat omega` is compactly supported. The first term is the universal DC/pole background; the second is a genuine prime-power curvature sampler. Below the first prime frequency the sampler vanishes identically, recovering VIS-263. Crossing a prime frequency is only an access condition: `hat omega''` may vanish there or different prime-power contributions may cancel.

The live support-edge question is now precise. Freeze a weight faithful to the intended edge observable and prove that its **prime-power curvature component** is nonzero at the required normalization after the pole term is removed. The accepted support-edge arithmetic-residual clue already owns that handoff, so no parallel clue is needed. A nonzero residual would establish source selectivity of this fixed-margin quadratic coordinate, not yet the moving-edge uniformity or four-level covariance needed by the original edge--edge statistic.

## Keep theorem-transfer conditioning separate from the arithmetic carrier

The packet norm, Rodgers fixed-margin error, Taylor remainder and support-edge motion are analytic-access costs. The decomposition in VIS-264 is a source-content statement. A viable route must satisfy both ledgers: the packet must reach the coefficient at controlled norm, and the coefficient surviving after pole subtraction must actually sample nonconstant prime-power frequencies. Neither a small theorem error nor a nonzero total `C_2` substitutes for the other.