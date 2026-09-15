# MI-029 — Linear quadratic source reach still leaves the logarithmic endpoint-energy gap

**Evidence level:** classical multiplicative/quadratic large sieve plus exact endpoint-partition energy from [MC-301](../../findings/MC-301-multiplicative-large-sieve-source-energy-capacity.md) and [MC-302](../../findings/MC-302-quadratic-large-sieve-source-horizon.md)

The low-source problem has several quantitatively different arithmetic controls. Pointwise Page/Deuring--Heilbronn theory can nearly eliminate each nonexceptional mode but only in a comparatively small source band. MC-301 uses the multiplicative large sieve collectively and reaches every selected primitive real source character through conductor `sqrt(y)`, with total energy `O(log y)`.

MC-302 uses additional structure that MC-301 deliberately ignored: every selected source character is quadratic. Heath-Brown's quadratic large sieve changes the capacity envelope to

`E_y(C) <<_epsilon (Cy)^epsilon (1+C/y) log y`,

with an explicit subpower version from Liu. The natural collective conductor horizon therefore moves from `sqrt(y)` to `y`.

This larger reach still does not cross the endpoint. The reciprocal endpoint-partition model has total obstruction energy `2^R/R`. At the blind-support floor `R~log_2 log y`, this is only about `log y/R`. Even granting an **ideal loss-free** quadratic large sieve with the same `(C+y)` theorem shape gives only `E_y(C)<<log y` throughout `C<=y`, so its capacity still exceeds the complete endpoint obstruction by a factor of order `R`.

The reusable point is sharper than “conductor reach and family capacity are separate currencies.” Once the capacity already dominates the entire obstruction energy, extending the conductor horizon by a power can leave the endpoint unchanged. Removing the explicit subpower loss, improving constants, or merely recognizing quadraticity cannot close a factor-`R` energy mismatch built into the black-box family bound.

The remaining target is therefore source-specific: save a factor comparable to `R` in the capacity of the **selected** quadratic family, force a corresponding factor more obstruction energy/rank in the actual shell geometry, or prove an arithmetic coupling among the selected conductors/modes that prevents the generic quadratic-family budget from being freely spent. MC-302 does not show that conductor `y` is an intrinsic threshold or that no thinner selected-family theorem exists.
