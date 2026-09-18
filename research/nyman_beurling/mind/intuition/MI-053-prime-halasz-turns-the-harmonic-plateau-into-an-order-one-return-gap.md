# MI-053 — Prime Halasz turns the harmonic plateau into an order-one return gap

**Evidence level:** literature-backed synthesis from [NB-208](../../findings/NB-208-positive-euler-return-forces-a-prime-harmonic-plateau.md) through [NB-211](../../findings/NB-211-vinogradov-korobov-prime-halasz-reaches-a-log-squared-diagonal-corridor.md). The prime-supported Halasz inequality and Vinogradov--Korobov zero-free region are classical; the Mathia content is their use on the deterministic harmonic family forced by positive Euler alignment and the proof-level diagonalization of the prime correlation error.

A small positive Euler return is not an isolated large-value event. NB-208 shows that it forces a whole family of prime phase sums at the harmonics `t,2t,...` to remain near maximal. NB-209 found that generic integer-support large-value estimates lose one logarithmic dimension because they charge the ambient support rather than the density of primes.

NB-210 identifies that loss as methodological rather than intrinsic. The Matomaki--Radziwill prime-supported Halasz inequality includes the missing prime-density gain, so a fixed number of forced harmonics contradicts any sufficiently small constant positive Euler defect throughout every fixed range `log |t|<=X_a^(3/2-delta)`.

NB-211 shows that the fixed `delta` is not the natural boundary of the proof. Re-running the same prime-correlation argument with the full Vinogradov--Korobov zero-free width gives an epsilon-free off-diagonal factor and hence an order-one gap uniformly through

`log |t| <= kappa_* X_a^(3/2)/(log X_a)^2`.

This is a true moving diagonal: it eventually exceeds `X_a^(3/2-delta)` for every fixed `delta>0`. The lesson is stronger than “use a prime-supported theorem.” When a published estimate contains a fixed loss, inspect whether that loss belongs to the underlying analytic mechanism or only to a deliberately weakened proof parameter before treating it as a coupled-limit obstruction.

The refined route still does not reach the Ford frontier `X_a^(3/2)/sqrt(log X_a)`, where the earlier exponential-sum method excludes only `o(1/X_a)` returns. The remaining logarithmic-height gap is `(log X_a)^(3/2)`. At that scale the Vinogradov--Korobov contour supplies only constant exponential saving, so the polynomial prefactor in the prime correlation kernel becomes load-bearing.

This localizes the next source-side question. The forced large values are not a generic well-spaced set: they occur at the arithmetic progression `t,2t,...` and are phase-pinned near `+1`. The current Halasz inequality discards that structure by squaring moduli. Any extension toward the Ford edge must exploit this correlation or improve the prime kernel itself; adding more harmonics to the same inequality does not change the boundary.

**Boundary.** This remains a positive-source acquisition result. It does not improve the outer Ford height, prove the required Nyman destination implication, apply to arbitrary signed/complex synthesis, or establish RH. The log-squared corridor is the boundary of the current Vinogradov--Korobov-contour plus prime-Halasz method up to constants/lower logarithms, not a theorem that positive returns exist beyond it.
