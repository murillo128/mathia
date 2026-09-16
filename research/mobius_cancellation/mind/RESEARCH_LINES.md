# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with genuinely structured joint information

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-045-exact-dephasing-trades-rowspace-rank-for-coefficient-energy`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. MC-327 shows that packages saturating the floor force almost all logarithmic source mass into columns of occupancy `R/2+o(R)`, and MC-328 shows that nonnegative endpoint-polynomial weights of degree `o(R)` are exactly blind on that middle band.

MC-329 reaches the same quartic boundary through fixed-common-modulus prime Halász--Montgomery bias energy, independently of the incidence argument. Optimizing its Burgess order approaches exponent four from below but cannot cross to a fixed exponent beyond four. MC-330 then closes generic signed linear/quadratic processing after `ell^2` energy compression.

MC-331 moves upstream and shows that one common arbitrary prime coefficient vector still cannot improve the endpoint balance: the coefficient-uniform theorem and endpoint operator norm charge the same top `ell^2` resource. MC-332 closes the opposite overcorrection. Arbitrary mode-dependent rows can choose the conjugate-character matched filter and erase oscillation pointwise; at the reciprocal endpoint the evaluation matrix itself has rank only `R`, so low rank relative to the `2^R-1` mode population does not prevent exact dephasing.

MC-333 makes that last boundary quantitative. If an exact all-mode dephaser for amplitudes `c_a` is constrained to matrix rank at most `d<=R`, its Frobenius energy obeys a lower bound of scale

`||W||_F^2 >= (A R/(d 2^R)) ||c||_1^2`.

For spread amplitudes such as `c_a=1`, the optimal energy is `Theta((R/d) A(2^R-1))`; full rank `R` attains the trivial matched-filter energy. Thus constant-factor-energy exact dephasing of the full endpoint population requires `d=Omega(R)`. **Rank and coefficient energy are independent currencies:** low rank does not forbid phase erasure, but making the rowspace too small forces a quantitative energy bill when the target amplitudes are spread.

The live linear route is now narrower than “find a low-rank joint class.” It must define a source-natural prime--mode coefficient class whose latent dimension, coefficient energy/conditioning and dependence on the character-evaluation geometry are all controlled, and prove an analytic family estimate that uses those restrictions. A useful class must be richer than one common vector, yet exclude or penalize the endpoint matched filter at the norm actually charged by the theorem. Sparse target amplitudes or another analytic norm may behave differently and must be audited separately.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a recent probabilistic Möbius route fails before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting the asserted independence, and the auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired route must use a dependence law valid on a non-degenerate stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, Fourier degree, common-modulus analytic horizon, placement relative to energy compression, joint rowspace rank, coefficient norm, amplitude sparsity and source-natural coupling are distinct. MC-333 shows why nominal matrix rank is as misleading as nominal mode count: what matters is whether the admissible class contains an inexpensive matched filter under the theorem's own norm. Future proposals should state the exact admissible class and its analytic cost before treating joint dependence as arithmetic leverage.
