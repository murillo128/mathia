# MI-021 — A coarse RH-sufficient endpoint can still require deep source access

**Evidence level:** classical Li/Voros criterion plus exact quotient and zeta-jet reconstruction consequences through AF-236

## Core intuition

Output tolerance and source depth are different currencies. The Li criterion admits a very coarse RH-sufficient endpoint: only the exponential root rate of the coefficient sequence matters, so every subexponential additive perturbation is invisible. Yet the canonical local zeta-germ reconstruction shows that every sublinear jet depth is itself subexponential at that endpoint.

Thus a target can be robust to enormous amplitude error and still require information spread across a deep part of its source representation. Coarse fidelity does not imply shallow access.

## Strongest justified principle

AF-234 records that the trend quotient `lambda_n/(n log n)->1/2` is RH-sufficient modulo `o(n log n)` error. AF-235 weakens amplitude fidelity much further: RH is equivalent to Li root rate at most one, and any subexponential additive error preserves that class.

AF-236 applies the exact binomial transform from local zeta-germ coefficients to `lambda_n`. For every `K_n=o(n)`, the contribution of the first `K_n` jet coordinates is subexponential and therefore invisible in the AF-235 quotient, independently of whether RH holds. Any false-RH exponential root-rate signal, if present, must therefore arise beyond every sublinear jet truncation.

## Program consequence

When proposing an RH-sufficient compressed target, price not only the allowed output distortion but also the source depth needed to evaluate that quotient. For the Li root-rate route, the useful theorem must control a genuinely deep reconstruction or replace it by another source-faithful bridge; sublinear local jets cannot carry the decisive class.

## Counterevidence / boundary

AF-236 does not prove that linear jet depth is sufficient or necessary, nor that the full Li sequence is easier to control than RH itself. It is a source-access boundary inside one canonical reconstruction, not a universal lower bound for every representation of the criterion.

## Epistemic status

**Exact separation between coarse output fidelity and shallow source access; no cheaper RH proof or sufficient finite-depth statistic is established.**

## Falsification criterion

Exhibit a sublinear canonical zeta-jet contribution with exponential Li root rate, or invalidate the AF-235 root-rate stability under subexponential additive perturbations. A positive continuation should construct and price a source-faithful bridge into the root-rate class.
