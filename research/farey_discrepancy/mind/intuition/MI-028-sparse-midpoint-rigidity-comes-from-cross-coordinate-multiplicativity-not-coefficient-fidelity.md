# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, not coefficient fidelity

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-177](../../findings/FD-177-long-dyadic-block-repair-preserves-every-subextremal-rank-window.md).

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while FD-172--FD-174 show that geometric sparse horizons certify Möbius inside a squarefree multiplicative cone. It is tempting to attribute that recovery to coefficient sparsity, the ternary Möbius alphabet, correct prime signs, or agreement on many low multiplicative-rank layers. FD-175--FD-177 separate those effects.

For integer geometric ladders with `B>=3`, FD-175--FD-176 construct permanent deletion-only sources `a(n) in {0,mu(n)}` that preserve every prime coefficient, any prescribed finite prefix, and a growing low-rank cone while agreeing with Möbius at every sampled midpoint horizon. FD-177 closes the dyadic gap. For every fixed `rho<1`, every finite cutoff and every `eta>0`, one can preserve

`omega(n) <= rho log n/log log n`

for all sufficiently large squarefree `n`, agree at **every** dyadic horizon `2^m`, and confine all deletions to a set with counting function `O(x^eta)`.

The dyadic mechanism is a **long-block repair**. Instead of repairing one new midpoint row at a time, group `k` consecutive dyadic rows. Their rounding defects span only a finite response family, and the correction demand grows like `L^(alpha_k)` with

`alpha_k=log_2(k+1)/k -> 0`.

Choosing `k` so that `alpha_k<1-rho` leaves enough high-rank squarefree composites of either Möbius sign in the fresh fixed-ratio shells to repair the whole block. The apparent `B=2` exponent obstruction in the one-step recurrence was therefore a repair-coordinate artifact, not a rigidity threshold.

The reusable lesson is stronger than coefficientwise non-rigidity. Sparse observation can remain blind even when the source agrees with Möbius on **every fixed subextremal fraction of the maximal multiplicative-rank scale** and differs only on an arbitrarily sparse set of high-rank composites. What the genuinely multiplicative cone supplies is a global product law tying those rare high-rank repair coordinates back to prime coordinates already fixed earlier. Coordinate fidelity alone, however deep, does not reproduce that coupling.

**Boundary.** FD-177 reaches every fixed `rho<1` but not the endpoint `(1-o(1)) log n/log log n`, full squarefree-rank fidelity, or another condition that couples the protected low-rank region to near-primorial composites. It does not give pairwise sparse inversion or improve the Franel--Landau destination estimate. The next structural target is therefore the extremal-rank endpoint or a genuinely cross-coordinate compatibility weaker than full multiplicativity but strong enough to make recursive shell repair impossible.