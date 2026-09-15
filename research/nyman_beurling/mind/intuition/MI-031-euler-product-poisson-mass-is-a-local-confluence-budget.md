# MI-031 — Positive Euler-product Poisson occupancy is exactly a reflection-closure budget

**Evidence level:** exact source-specific occupancy theorem from [NB-144](../../findings/NB-144-euler-product-poisson-mass-forces-logarithmic-confluence-away-from-the-one-line.md), with endpoint correction NB-146 and the complete reflection-closure classification [NB-147](../../findings/NB-147-reflection-closure-exactly-interpolates-the-positive-poisson-occupancy-coefficient.md).

For exterior samples `s=1+delta+iv`, the explicit formula and absolutely convergent Euler product give one positive budget: zero Poisson mass is bounded by `(1/2)log G` plus the `delta^-1` Euler-side cost. NB-147 identifies the exact packet variable charged by this architecture.

For any tight interior packet `C_G`, let `J(rho)=1-conj(rho)` and let `Chat_G=C_G union J(C_G)` be the multiset reflection closure, without double-counting partners already present. Then

`sum_(rho in Chat_G) 1/(1-Re rho) <= (1/2+o(1)) log G`.

This is not merely a one-sample estimate. Arbitrary positive multi-point or continuous exterior sampling, when the prime side is controlled only by the pointwise absolute Euler-product majorant, cannot lower the leading threshold for this weighted closure mass. A single sample with `delta=(log G)^-1/2` at the packet ordinate asymptotically saturates it.

Near the critical line each closure weight is `2+o(1)`. If `d_G=|C_G|` and `b_G` is the number of packet occurrences whose reflected partner is absent from the packet, then

`d_G+b_G <= (1/4+o(1)) log G`.

With `q_G=b_G/d_G`, this is

`d_G <= (1/[4(1+q_G)]+o(1)) log G`.

Thus the old `1/8` separated coefficient and `1/4` self-dual coefficient are the endpoints of one orbit-exposure law: `q=1` when every partner lies outside, `q=0` when the packet is reflection-saturated. The Poisson kernel never jumps; only the counted packet's closure deficit changes.

A useful rigidity consequence is quantitative. If a near-critical packet approaches the maximal `1/4 log G` occupancy, then `b_G=o(log G)`: almost all reflected partners must already lie in the packet. This does not prove RH or target bearing, but it identifies exactly what positive Poisson sampling can force about packet geometry.

The reusable conclusion is therefore sharp: **within the positive exterior-sampling/absolute-Euler-majorant proof cone, reflection-closure mass is the complete local occupancy currency**. Denser positive sampling cannot improve it. Any stronger confluence theorem must use a different resource such as signed cancellation, prime correlations, higher moments, or target-projection information.

**Boundary.** The theorem requires a tight packet in a fixed compact substrip and controls local occupancy, not Nyman target coercivity. It still permits `Theta(log G)` reflection-saturated packets and does not exclude off-critical zeros. Signed combinations, correlation information and target-bearing structure remain outside the classified positive cone.