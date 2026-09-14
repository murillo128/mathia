# MI-015 — Selector-subtracted one-profile spectra are classically reproducible up to a log-squared neighborhood of square-root scale

**Evidence level:** unconditional classicalization from PC-282--PC-285 and conditional RH sharpening from PC-286--[PC-289](../../findings/PC-289-short-interval-sieve-pushes-rh-boundary-log-collapse-to-log-squared-gap.md). No converse RH criterion is claimed, and no theorem is claimed for richer observables outside the normalized one-profile singular-spectrum law.

After selector subtraction, the complete-domain remainder is a classical logarithmic/digamma Green symbol. Prime dependence in this branch survives only through source placement inside the finite section. PC-285 already reproduces that placement with the matched Li-grid control through the unconditional Vinogradov--Korobov range.

PC-287--PC-288 showed under RH that flat clipping plus one-dimensional path variation pushes the same exact statistic to `B=o(sqrt(q)/(log q)^(5/2))`. PC-289 removes another artificial loss by estimating the clipping region **after pulling it back to prime intervals**. A Brun--Titchmarsh-type bound gives arc-length mass on every logarithmic-depth band until a tiny tail, improving the clipping second moment from `epsilon log q` to `epsilon`.

With `L=log q`, the resulting deterministic transport bound is

`W_1 << sqrt(epsilon+L^3/q) + (B/sqrt(epsilon)) Delta_q + L^2/q`

under the stated long-preimage condition. RH supplies `Delta_q << q^(-1/2)L^2+L/q`; choosing `epsilon=B q^(-1/2)L^2` yields collapse whenever

`B=o(sqrt(q)/L^2)`.

The reusable lesson is now two-layered. Integrated output-path variation is cheaper than global Lipschitz control, and **source-aware mass estimates inside the singular set are cheaper than charging that set by the worst atom**. Once both losses are removed, the remaining `log^2 q` gap comes from the pointwise RH prime-to-Li source discrepancy itself.

This makes the interpretation sharper. RH drives this one-profile observable toward the classical control almost to square-root scale. Further improvement within the same architecture must beat the source discrepancy/transport interface rather than the clipping geometry. If the desired RH signature is persistent order-one prime-specific separation, a different observable must retain information that the ordered one-profile singular spectrum discards.

**Boundary.** PC-289 is still a one-way RH consequence. It uses classical short-interval sieve input plus RH prime-counting discrepancy and says nothing about multi-source, cross-level, phase-sensitive or noncommuting observables.
