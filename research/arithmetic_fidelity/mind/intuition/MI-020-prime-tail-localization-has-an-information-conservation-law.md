# MI-020 — Prime-tail information cost is set by target geometry, not visible alphabet size

**Evidence level:** exact finite-source zero-error entropy splitting and target-relative stochastic rate-distortion asymptotics through AF-233

## Core intuition

Prime-tail localization carries a first-order information bill, but that bill belongs to the **target and distortion actually consumed by the theorem**, not to the source alphabet alone. AF-228--AF-230 show that merely relabeling or randomizing exact/approximate source localization does not remove the leading source-information cost. AF-231--AF-233 show the complementary possibility: a downstream observable can be genuinely cheaper when its geometry contracts source distinctions at the declared accuracy.

The same arithmetic observable can therefore have different first-order information phases under different fidelity metrics. Power damping creates a free-resolution region for absolute error, while logarithmic/relative error restores the ordinary prime-resolution phase.

## Strongest justified principle

AF-229 gives exact finite-source separation/localization entropy conservation in the perfect prime-tail proximity model, and AF-230 shows that positive-error stochastic coding preserves the same first-order localization phase.

AF-231 then proves that a monotone target with `|f'(x)|\asymp x^{-a-1}` has absolute-error price `(1-delta) min{(beta-a)_+,1}` at tolerance `Q^{-beta+o(1)}`. AF-232 shows that scale-normalized relative/logarithmic error for the same power-decaying target has the unshifted phase `(1-delta) min{beta,1}`.

AF-233 unifies these examples. Under its monotone `C^1` hypotheses, if

`rho = 1 + lim log|f'(x)|/log x`

and the absolute target tolerance has exponent `beta`, then

`R_Q^f / log pi(Q) -> (1-delta)[rho+beta]_0^1`.

Thus derivative scaling is an exact first-order target-geometry currency in the declared finite prime-source model.

## Program consequence

A proposed arithmetic compression should first identify the statistic the final theorem really needs and the error metric in which it needs it. Then price that target directly. A small alphabet, small amplitude, or stochastic encoder is not evidence of cheap information; conversely, full source localization need not be paid when a rigorously sufficient target quotient contracts irrelevant distinctions.

The fertile escape is therefore a **target-specific sufficient statistic with a derived cheaper fidelity phase**, not a representation that merely hides prime identity.

## Counterevidence / boundary

AF-228--AF-233 analyze explicit finite prime-source models and declared distortion metrics. They do not prove that RH factors through any monotone scalar target, nor that every arithmetic target admits a derivative-exponent phase law. Exact recovery of an injective target still retains full prime identity even when approximate absolute reproduction is cheap.

## Epistemic status

**Exact information-budget and target-geometry boundary for the current source models; no claim that the RH target has been compressed.**

## Falsification criterion

Within the hypotheses of AF-233, produce a target channel with a different first-order information phase, or within AF-230 beat the established localization phase by relabeling/randomization alone. A positive continuation should instead prove that an RH-facing target factors through a lower-information statistic and derive its actual distortion price.