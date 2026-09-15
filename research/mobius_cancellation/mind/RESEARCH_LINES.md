# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Close the explicit collective-capacity gap at the blind-support frontier

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-029-square-root-source-energy-capacity-leaves-a-logarithmic-dimension-gap`.

MC-293--MC-297 move the problem from individual character cost to the selected subset spectrum. MC-298 shows that no fixed hierarchy of overlap marginals determines Page parity. MC-299--MC-300 then price the pointwise arithmetic route: a strong Page exception triggers Deuring--Heilbronn repulsion, but with the available exceptional-zero input the uniform fixed-accuracy source band has a Lambert-W ceiling of order `log y log log log y/log log y` in log-conductor.

MC-301 supplies the distinct generic collective theorem that MC-300 left open. The multiplicative large sieve gives

`sum_(lambda!=0, Q(lambda)<=C) |x_lambda|^2 << (1+C^2/y) log y`,

so all selected source characters through conductor `sqrt(y)` have only `O(log y)` total shell-bias energy.

MC-302 then exploits a fact specific to the selected family: every source character is quadratic. Heath-Brown's quadratic large sieve improves the capacity envelope to

`E_y(C) <<_epsilon (Cy)^epsilon (1+C/y) log y`,

with Liu's explicit theorem giving a uniform subpower multiplier. The natural collective conductor horizon therefore moves from `sqrt(y)` to `y`.

The reciprocal endpoint-partition extremizer shows why that power-scale gain is still insufficient. An `R`-dimensional selected subspace carries total Fourier bias energy `2^R/R`; at the blind-support floor `R~log_2 log y`, this is about `log y/R`. Even an idealized quadratic large sieve with every subpower loss removed but the same `(C+y)` shape gives only an `O(log y)` capacity bound for `C<=y`, which can still contain the entire endpoint obstruction by a factor of order `R`. The gap is therefore not a constants or epsilon-loss issue.

The live theorem is now source-specific rather than a request for a better generic quadratic inequality: save the missing factor `R` for the actual selected quadratic family, prove that the actual endpoint obstruction carries more energy/rank than the reciprocal extremizer, or find an arithmetic coupling among selected conductors/modes that prevents the generic capacity from being freely spent.

## Keep pointwise exceptional-zero control, generic family energy and quadratic-family energy separate

Page/Deuring--Heilbronn controls individual modes extremely strongly but only in a smaller conductor band. The generic multiplicative large sieve reaches square-root conductor collectively. The quadratic large sieve reaches linear conductor collectively, but its black-box mean-square capacity remains `O(log y)` at the relevant polynomial horizon even in an ideal loss-free form.

MC-300 is a certificate ceiling for the pointwise channel, not a nonexistence theorem. MC-301 is a generic family-capacity ceiling, and MC-302 is a stronger quadratic-family ceiling, neither of which is claimed sharp for the selected source family. Combining them requires preserving their different quantifiers and currencies rather than treating “more conductor control” as one scalar resource.

## Preserve matched controls and exact energy accounting as falsifiers

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. The reciprocal endpoint partition gives the sharp finite-geometric energy profile against which collective arithmetic bounds should be tested. Any proposed improvement should state whether it lowers the selected source-family capacity, raises the forced obstruction energy, or couples modes across conductor; otherwise it has not addressed the explicit factor-`R` gap that survives MC-301--MC-302.
