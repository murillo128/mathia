# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with genuinely structured joint information

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-047-low-degree-mode-dependence-is-an-endpoint-anti-dephasing-resource`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. MC-327 shows that packages saturating the floor force almost all logarithmic source mass into columns of occupancy `R/2+o(R)`, and MC-328 shows that nonnegative endpoint-polynomial weights of degree `o(R)` are exactly blind on that middle band.

MC-329--MC-331 close generic fixed-modulus bias energy, signed low-order processing and one common arbitrary coefficient vector. MC-332 closes the opposite overcorrection: arbitrary mode-dependent rows can choose the conjugate-character matched filter and erase oscillation pointwise, despite having only rank `R` across `2^R-1` modes.

MC-333 and MC-334 separate rank/energy and cross-mode variation costs. MC-335 adds a genuinely different restriction: Walsh/Fourier degree of mode dependence in the standard endpoint coordinates. Low degree there cannot approximate uniform dephasing, with exact programmability returning only near maximal degree.

MC-336 shows why that restriction is not yet coordinate-invariant. In source-phase variables `x_i(a)=(-1)^(a·s_i)`, the dangerous matched filter is degree one because coefficient `i` can read and cancel its own phase. For even source rank, the exact finite-endpoint repair is **self-phase exclusion**: forbid coefficient `i` from depending on `x_i` while allowing degree-`d` dependence on the other source phases. The missing source-character tail then gives the exact dephasing obstruction, and exact cancellation returns only at degree `R-1`.

MC-337 closes the odd-rank case and shows that literal self-phase hiding is still not the invariant notion. For odd `R`, the source phases satisfy the global relation `prod_i x_i=1`, so the source map lands on the even-parity subgroup and has kernel `{0,1}`. The forbidden phase `x_i` is therefore determined by the other `R-1` phases, but reconstructing it requires their full product. At every `d<=R-2`, the normalized best dephasing error remains `1-o(1)`; once `d>=(R-3)/2` every nonconstant quotient character is already reachable, yet the error sits on a plateau until degree `R-1`, where `prod_(j!=i) x_j=x_i` makes exact matched filtering possible.

The live linear route is therefore narrower than “find a low-rank or low-degree joint class” and narrower than “hide the own phase syntactically.” It must define a **source-natural information-flow class** whose latent dimension, total coefficient energy/conditioning, cross-mode variation, source-coordinate degree and own-phase **access or reconstructibility** are controlled, then prove an analytic family estimate sensitive to those same restrictions. A degree bound stated in coordinates that expose the target phase is not anti-programmability, and a variable-exclusion rule is not anti-programmability if a cheap source relation reconstructs the excluded variable.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a recent probabilistic Möbius route fails before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting the asserted independence, and the auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired route must use a dependence law valid on a non-degenerate stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, joint rowspace rank, total coefficient norm, cross-mode variation from the best common input, coordinate-dependent degree, **self-phase access/reconstruction complexity**, amplitude sparsity and source-natural coupling are distinct. MC-336 makes the representation audit mandatory; MC-337 makes it quotient-aware. Before treating low degree or variable exclusion as structure, express the class in source coordinates, identify algebraic relations among those coordinates, and ask how cheaply each coefficient can reconstruct the phase it is meant to cancel. Future proposals should state the exact admissible information flow and the norm/variation/degree budget charged by the analytic theorem before treating joint dependence as arithmetic leverage.