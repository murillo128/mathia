# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Close the explicit collective-capacity gap at the blind-support frontier

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-030-multiquadratic-packaging-turns-source-cost-into-discriminant-complexity`.

MC-293--MC-297 move the problem from individual character cost to the selected subset spectrum. MC-298 shows that no fixed hierarchy of overlap marginals determines Page parity. MC-299--MC-300 price the pointwise arithmetic route: a strong Page exception triggers Deuring--Heilbronn repulsion, but with the available exceptional-zero input the uniform fixed-accuracy source band has a Lambert-W ceiling of order `log y log log log y/log log y` in log-conductor.

MC-301 supplies the distinct generic collective theorem that MC-300 left open. The multiplicative large sieve gives

`sum_(lambda!=0, Q(lambda)<=C) |x_lambda|^2 << (1+C^2/y) log y`,

so all selected source characters through conductor `sqrt(y)` have only `O(log y)` total shell-bias energy. MC-302 exploits that every source character is quadratic and moves the natural collective conductor horizon to `y`, but the reciprocal endpoint-partition extremizer carries only about `log y/R` energy at the blind-support rank `R~log_2 log y`. Even an ideal loss-free quadratic large sieve of the same `(C+y)` shape leaves an `O(log y)` capacity and therefore a factor-`R` gap.

MC-303 closes the next generic packaging move. The independent selected quadratic modes generate a multiquadratic field of degree `2^R`; the Page-forced source-cost spectrum then makes the conductor--discriminant product enormous, with `log |D_K| >= (log y)^(2-o(1))/log log y` at the blind-support floor. Standard effective Chebotarev consequently loses shell-scale uniformity by a large margin. Packaging the modes into one Frobenius problem is exact, but black-box field complexity charges the same endpoint source cost through `D_K`.

The live theorem is now source-specific rather than a request for another generic capacity theorem. One must save the missing factor `R` for the actual selected quadratic family, prove that the actual endpoint obstruction carries more energy/rank than the reciprocal extremizer, exploit arithmetic coupling among selected modes, or derive a multiquadratic mixing theorem using special family structure not summarized by generic degree/discriminant complexity.

## Keep pointwise exceptional-zero control, generic family energy, quadratic-family energy and field complexity separate

Page/Deuring--Heilbronn controls individual modes extremely strongly but only in a smaller conductor band. The generic multiplicative large sieve reaches square-root conductor collectively. The quadratic large sieve reaches linear conductor collectively, but its black-box mean-square capacity remains `O(log y)` at the relevant polynomial horizon even in an ideal loss-free form. The multiquadratic reorganization couples all modes algebraically, but generic Chebotarev pays through a discriminant inflated by the same source-cost spectrum.

MC-300 is a certificate ceiling for the pointwise channel, not a nonexistence theorem. MC-301--MC-302 are family-capacity ceilings, and MC-303 is a theorem-range obstruction for black-box Chebotarev; none proves that the selected source family lacks a stronger special theorem. Combining them requires preserving their different quantifiers and currencies rather than treating “more conductor control” or “one collective object” as automatic progress.

## Preserve matched controls and exact energy accounting as falsifiers

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. The reciprocal endpoint partition gives the sharp finite-geometric energy profile against which collective arithmetic bounds should be tested. MC-303 adds a second accounting test: a proposed algebraic packaging must be checked for whether source complexity simply reappears in degree, conductor or discriminant. Any improvement should state whether it lowers selected-family capacity, raises forced obstruction energy, couples modes beyond the generic extremizer, or supplies a genuinely cheaper source-specific field invariant.
