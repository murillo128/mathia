# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with genuinely structured joint information

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-047-low-degree-mode-dependence-is-an-endpoint-anti-dephasing-resource`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. MC-327 shows that packages saturating the floor force almost all logarithmic source mass into columns of occupancy `R/2+o(R)`, and MC-328 shows that nonnegative endpoint-polynomial weights of degree `o(R)` are exactly blind on that middle band.

MC-329--MC-331 close generic fixed-modulus bias energy, signed low-order processing and one common arbitrary coefficient vector. MC-332 closes the opposite overcorrection: arbitrary mode-dependent rows can choose the conjugate-character matched filter and erase oscillation pointwise, despite having only rank `R` across `2^R-1` modes.

MC-333 and MC-334 separate rank/energy and cross-mode variation costs. MC-335 adds a genuinely different restriction: Walsh/Fourier degree of mode dependence in the standard endpoint coordinates. Low degree there cannot approximate uniform dephasing, with exact programmability returning only near maximal degree.

MC-336 shows why that restriction is not yet coordinate-invariant. In the source-phase variables `x_i(a)=(-1)^(a·s_i)`, the dangerous matched filter is degree one because coefficient `i` can read and cancel its own phase. The exact finite-endpoint repair is **self-phase exclusion**: forbid coefficient `i` from depending on `x_i` while allowing degree-`d` dependence on the other source phases. The reachable outputs are then precisely the source monomials of degrees `1,...,d+1`, and the missing tail gives exact dephasing error `N q_d/(q_d+1)` with `q_d=sum_(k=d+2)^R binom(R,k)`. For `d=o(R)` the RMS error again tends to one; exact dephasing requires `d=R-1`.

The live linear route is therefore narrower than “find a low-rank or low-degree joint class.” It must define a **source-natural information-flow class** whose latent dimension, total coefficient energy/conditioning, cross-mode variation, source-coordinate degree and self-phase access are controlled, then prove an analytic family estimate sensitive to those same restrictions. A degree bound stated in coordinates that expose the target phase is not anti-programmability.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a recent probabilistic Möbius route fails before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting the asserted independence, and the auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired route must use a dependence law valid on a non-degenerate stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, joint rowspace rank, total coefficient norm, cross-mode variation from the best common input, coordinate-dependent degree, **self-phase access/reconstruction**, amplitude sparsity and source-natural coupling are distinct. MC-336 makes the representation audit mandatory: before treating low degree as structure, express the class in source coordinates and ask whether each coefficient can read the very phase it is meant to cancel. Future proposals should state the exact admissible information flow and the norm/variation/degree budget charged by the analytic theorem before treating joint dependence as arithmetic leverage.