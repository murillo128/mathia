# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Close the explicit collective-capacity gap at the blind-support frontier

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-029-square-root-source-energy-capacity-leaves-a-logarithmic-dimension-gap`.

MC-293--MC-297 move the problem from individual character cost to the selected subset spectrum. MC-298 shows that no fixed hierarchy of overlap marginals determines Page parity. MC-299--MC-300 then price the pointwise arithmetic route: a strong Page exception triggers Deuring--Heilbronn repulsion, but with the available exceptional-zero input the uniform fixed-accuracy source band has a Lambert-W ceiling of order `log y log log log y/log log y` in log-conductor.

MC-301 supplies the distinct collective theorem that MC-300 left open. The multiplicative large sieve gives

`sum_(lambda!=0, Q(lambda)<=C) |x_lambda|^2 << (1+C^2/y) log y`,

so all source characters through conductor `sqrt(y)` have only `O(log y)` total shell-bias energy. This reaches vastly farther in conductor than the pointwise Page/Deuring--Heilbronn band without needing an exceptional-zero analysis.

The reciprocal endpoint-partition extremizer makes the remaining gap exact. An `R`-dimensional selected subspace carries total Fourier bias energy `2^R/R`. At the blind-support floor `R~log_2 log y`, this is only about `log y/R`, still below the generic large-sieve capacity by a factor of order `R`. The black-box collective theorem therefore misses the endpoint by roughly one additional `log_2 R` layer of independent directions; this is not a constants issue.

The live theorem is now quantitative and source-specific: recover that missing logarithmic factor by proving a smaller capacity for the actual varying-conductor source family, prove that the actual endpoint obstruction carries more energy/rank than the reciprocal extremizer, or find an arithmetic coupling that prevents the high-source spectrum from spending the generic large-sieve budget freely.

## Keep pointwise exceptional-zero control and collective family energy separate

Page/Deuring--Heilbronn control individual modes extremely strongly but only in a smaller conductor band. The multiplicative large sieve reaches square-root conductor but controls only total squared bias and permits `O(log y)` strongly biased modes. Neither theorem subsumes the other.

MC-300 is a certificate ceiling for the pointwise channel, not a nonexistence theorem. MC-301 is a family-capacity ceiling for the generic large-sieve channel, not a sharp asymptotic for the selected source family. Combining the two requires preserving their different quantifiers and currencies rather than treating “more conductor control” as one scalar resource.

## Preserve matched controls and exact energy accounting as falsifiers

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. The reciprocal endpoint partition gives the sharp finite-geometric energy profile against which collective arithmetic bounds should be tested. Any proposed improvement should state whether it lowers the source-family capacity, raises the forced obstruction energy, or couples modes across conductor; otherwise it has not addressed the explicit `R`-factor gap left by MC-301.