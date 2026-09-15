# MI-031 — Compressed-translation autocorrelation has no hidden same-width shape slack

**Evidence level:** exact operator extremal theorem from [WI-306](../../findings/WI-306-compressed-translation-autocorrelation-bound-is-exact.md), sharpening the first-prime obstruction WI-305.

Let `S_a` be translation by `a>0`, compressed to an interval of length `ell`, and put `N=ceil(ell/a)`. Nilpotence gives the Haagerup--de la Harpe upper bound

`w(S_a) <= cos(pi/(N+1))`.

For this interval translation the bound is exact. One smooth bump can be copied along the longest translation chain, with discrete sine weights, to embed the finite Jordan extremizer. Hence

`sup_(||chi||_2=1) rho_chi(a) = cos(pi/(ceil(ell/a)+1))`

within the normalized real smooth localizer class.

Applied to the isolated prime-power defect

`w_q=(Lambda(q)/sqrt(q))(1-rho_chi(log q))`,

this proves that WI-305's atomwise support loss is optimal. For Liu's support length `ell=2` and `q=2`, the best possible localizer still leaves

`w_2=(log 2/sqrt(2))(1-1/sqrt(2)) > 1/16`.

No clever reshaping of `chi` inside the same support can cross the compact-repair gate.

If one artificially freezes the high-frequency reserve at `1/16` and varies only support length, the first-prime transition is discrete: the `q=2` gate cannot pass until

`ell>5 log 2`,

when a sixth translation cell becomes available. This is a useful scale audit, not a prescription for the full localization, because widening the support also changes the other pieces of the certificate and may change the reserve itself.

**Boundary.** WI-306 is an exact one-lag optimization inside the tail-dropped bounded comparison. It does not prove negativity of the full Weil form, validate the unreplayed `17/16` certificate, or show that increasing support repairs the full argument. It only removes localizer-shape slack from the first active arithmetic channel.