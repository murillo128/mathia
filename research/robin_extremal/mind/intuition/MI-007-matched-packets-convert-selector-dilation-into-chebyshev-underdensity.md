# MI-007 — Matched first-layer packets turn selector dilation into a one-sided Chebyshev--Mertens fan ledger

**Evidence level:** supported by RE-068--RE-072; no contradiction with known joint prime-error estimates or proof that long matched fan runs must occur is claimed.

The matched first-layer branch is exactly silent to additive endpoint prime statistics. RE-068 shows that the physical labels crossed by one matched packet are precisely the ordinary primes in the selector interval, while RE-069 shows that direct positional delay is absolutely summable after the Robin workload is applied.

RE-070 finds a pre-compression survivor. The tied common-amplitude selector expands the target interval while preserving the exact Chebyshev mass, so every sufficiently late matched packet forces a positive increment of `H_vartheta(Z)=Z-vartheta(Z)`. RE-071 adds the reciprocal coordinate: the normalized logarithmic Mertens-product error `E_l` decreases across the same packet. On sublinear packets the two increments are asymptotically tied by the factor `1/(Y log Y)`.

RE-072 proves that this opposite drift does not cancel when matched packets are concatenated through the intervening threshold cells. If every switch in a consecutive first-layer fan run is matched, the fringe bit stays zero throughout each fixed-state cell. Along the entire selected path, `H_vartheta` increases through both cells and switches while `E_l` decreases through both. The total increments are sums of positive cell and switch masses, so there is no internal sign cancellation.

The two errors are not independent currencies. On cells one has exactly `-dE_l = g(Z) dH_vartheta`, with `g(Z)=1/(Z log Z)`, and the switch law has the analogous positive weighted-average ratio. A whole matched run therefore remains inside one narrow Chebyshev--Mertens cone rather than wandering freely in two dimensions.

RE-072 also prices threshold width. If a matched fan run spans `Delta beta=beta_m-beta_1` and its lower physical scale is `X`, then the continuous cell contribution alone forces

`Delta H_vartheta >>_J X^(1-b_1) log X * Delta beta`.

A positive threshold-width run therefore spends a monotone standard-prime excursion independently of packet cardinality. This cost is meaningful but not yet contradictory: because `b_1>1-Theta`, its exponent `1-b_1` remains below the false-RH frontier `Theta`.

The live question is now global capacity. Either show that a false-RH counterexample architecture would require matched fan runs whose accumulated one-sided ledger exceeds what the coupled Chebyshev/Mertens errors can sustain, or show that the architecture must repeatedly leave the matched first-layer branch and then pay the higher-layer/fringe charges already isolated elsewhere.

**Boundary.** RE-072 proves monotonicity only along the adaptively selected matched first-layer fan path, not globally in `x`. It does not prove that such runs have positive limiting threshold width, recur indefinitely, or by itself contradict available prime-error envelopes.