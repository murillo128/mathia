# MI-007 — Matched first-layer packets force a span-free joint Chebyshev--Mertens capacity law

**Evidence level:** supported by RE-068--RE-073; no contradiction with known joint prime-error estimates, global fan accumulation theorem, or proof that long matched fan runs must occur is claimed.

The matched first-layer branch is exactly silent to additive endpoint prime statistics. RE-068 shows that the physical labels crossed by one matched packet are precisely the ordinary primes in the selector interval, while RE-069 shows that direct positional delay is absolutely summable after the Robin workload is applied.

RE-070 finds a pre-compression survivor. The tied common-amplitude selector expands the target interval while preserving the exact Chebyshev mass, so every sufficiently late matched packet forces a positive increment of `H_vartheta(Z)=Z-vartheta(Z)`. RE-071 adds the reciprocal coordinate: the normalized logarithmic Mertens-product error `E_l` decreases across the same packet. RE-072 proves that this opposite drift does not cancel when matched packets are concatenated through the intervening threshold cells.

On each matched cell the two errors are coupled exactly by

`-dE_l = g(Z) dH_vartheta`, with `g(Z)=1/(Z log Z)`.

RE-073 uses this common positive path measure rather than bounding the coordinates separately. Cauchy--Schwarz gives, for a matched run of threshold width `w` beginning at physical scale `X`,

`Delta_H Delta_E >>_J X^(1-2b_1) log X * w^2`.

This law is independent of the largest physical scale reached by the run. The separate reciprocal lower bound can become arbitrarily weak under superpolynomial stretch, but the **joint geometric mean cannot**: making `Delta_E` small forces a compensating increase in `Delta_H`, and conversely.

The reusable insight is that **an adaptive source path may have no useful coordinatewise lower bound while still obeying a strong joint capacity law in the natural coupled metric**. Physical stretch redistributes burden between the standard and reciprocal prime-error coordinates rather than erasing it. This is stronger than one-sided monotonicity and removes span as a bookkeeping escape for the matched branch.

The live question is global capacity. A false-RH counterexample fan may alternate maximal matched runs with higher-layer or unmatched-fringe interruptions. The next theorem must combine the span-free matched-run product budgets with the separate interruption charges and show that the same off-critical source trajectory cannot absorb the total threshold-width demand, or exhibit a coherent architecture that can.

**Boundary.** RE-073 applies only to sufficiently late common positive counterexample blocks and matched first-layer runs; its polynomial extraction uses a compact threshold interval below `1/2`. It gives no separate span-independent lower bound for either `Delta_H` or `Delta_E`, no global monotonicity in physical `x`, and no contradiction with false RH by itself.