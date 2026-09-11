# MI-008 — Prime-Flute endpoint decay must come from relative angle on infinite heavy sectors

**Evidence level:** proved operator-theoretic boundary

## Core intuition

Unprojected reservoir transmission, extension strength, and physical low/high leakage are different currencies. Energy normalization isolates the mixed operator

`T = F_P Gamma F_H`,

where the outer positive contractions record extension strength and `Gamma` records the relative low/high extension angle. The latest findings show that the canonical physical strengths are heavy on infinite-dimensional tails, so the desired weak-trace decay cannot come from compact outer factors. It must be created by the relative angle itself, or by a threshold-dependent interaction between angle and strength.

## Strongest justified claim

PF-279 shows why an isolated corridor coefficient does not control an unprojected complete cut: exact Schur transmission also depends on endpoint-normalized reservoir extension masses. PF-280--PF-282 then match the invariant to the physical statistic. Positivity canonically defines the energy-normalized cross operator, and its singular-value class controls the mixed inverse block and reciprocal-prime commutator. On heavy sectors, the strength factors saturate and the singular values are governed by the compressed angle.

PF-283 provides a sufficient weak-trace route through heavy-angle counting. PF-284 proves the two-sided comparison and separates sufficient from necessary scales. In the symmetric thresholding, `N_(Gamma_tau)(2 tau)=O(tau^-1)` suffices, but weak trace class only implies `O(tau^-3)`. Hence an intermediate growth rate can defeat the convenient PF-283 proof without refuting the endpoint.

PF-285 shows abstractly that angle decay would be unnecessary if the two strengths had complementary weak-Schatten decay. PF-286 then excludes that cheaper mechanism in the physical Prime-Flute geometry: the low strength has infinitely many channels above every fixed threshold and the high strength is noncompact with an infinite heavy population. Neither outer factor belongs to any finite weak-Schatten class.

## Synthesis of evidence

The endpoint problem is now genuinely about **relative geometry between two individually heavy infinite-dimensional extension ranges**. Same-sector mass cannot be ignored, but it also cannot solve the problem by decaying away. The useful statistic must count or otherwise control how much of those heavy ranges remains aligned across the physical split.

This changes the order of attack. First distinguish a missed sufficient criterion from a true endpoint obstruction using the PF-284 necessary scale. Then seek a source/geometric theorem for the angle on the actual completed flute, including finite-pant and neighboring-cell coupling.

## Counterevidence / boundary cases

PF-286 does not prove `T` is noncompact. Two noncompact outer factors can still yield a compact or weak-trace product when the middle angle kills their common heavy directions. Conversely, PF-284's necessary `tau^-3` envelope is not sufficient by itself.

The heavy-angle statistic is threshold-dependent; a global weak-Schatten class for `Gamma` would be sufficient but may be unnecessarily strong. The physical theorem may use a finer joint strength-angle distribution.

## Epistemic status

**Exact endpoint narrowing:** outer-factor population decay is unavailable in the canonical physical split, and the convenient heavy-angle count is only sufficient. The remaining endpoint currency is relative extension geometry on infinite heavy sectors.

## Novelty/prior-art status

Schur complements, singular-value inequalities, weak Schatten ideals, and threshold counting retain their finding-level prior-art status. This note synthesizes their exact role in Prime Flute.

## Falsification criterion

Show that one canonical physical strength factor is actually compact/finite weak-Schatten despite PF-286, or construct a physical endpoint proof whose mechanism is independent of relative angle and does not contradict the established factorization. Alternatively, prove divergence of the PF-284 necessary statistic on a canonical sequence; that would turn the surviving route into a genuine obstruction.
