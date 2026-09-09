# MI-020 — Prime-tail localization obeys a first-order information conservation law

**Evidence level:** exact finite-source zero-error entropy splitting and stochastic rate-distortion asymptotics through AF-230

## Core intuition

For the prime-tail proximity model, localization is not merely a matter of choosing enough labels. At fixed source law and geometric resolution there is a first-order information bill that survives deterministic and stochastic reformulations.

The exact zero-error proximity graph makes the split especially transparent: separation information and localization information are complementary parts of the same source entropy. Allowing positive error replaces the combinatorial split by a rate-distortion problem, but the leading localization phase remains unchanged.

## Strongest justified principle

AF-228 identifies the deterministic localization-entropy phase at resolution `r_Q \asymp Q^{-\beta}`. AF-229 proves exact finite-source entropy conservation for the perfect prime-tail proximity graph: the information needed to distinguish proximity classes plus the information needed to localize within them equals the source entropy. AF-230 shows that stochastic positive-error coding has the same first-order phase, so randomization supplies at most lower-order relief in this model.

This strengthens the earlier warning that alphabet cardinality is not information. Compression can reduce the number of visible labels while leaving essentially the same source-information burden.

## Program consequence

A successful arithmetic-fidelity bridge should identify a mathematically justified **target quotient** before paying for localization. If the final theorem only needs a lower-dimensional relational statistic, prove that sufficiency and price its information directly. Otherwise the current proximity model says that coding ingenuity alone cannot remove the leading source-information cost.

## Counterevidence / boundary

The conservation law belongs to the established prime-tail proximity/source model and its declared distortion. It is not a universal rate-distortion theorem for every arithmetic representation. A different source law, target-dependent distortion, or nonlocal sufficient statistic can change the phase, but that change must be derived rather than inferred from a smaller encoding.

## Epistemic status

**Exact information-budget boundary for the current proximity/localization model; no claim that RH requires full prime-tail reconstruction.**

## Falsification criterion

Construct, within the AF-228--AF-230 source and distortion hypotheses, a deterministic or stochastic scheme with strictly smaller first-order localization information than the established phase. A positive escape should instead prove that the RH-facing target factors through a different sufficient statistic with a lower derived information rate.
