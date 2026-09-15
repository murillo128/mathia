# MI-029 — Square-root source-energy capacity leaves a logarithmic dimension gap

**Evidence level:** classical multiplicative large sieve plus exact endpoint-partition energy from [MC-301](../../findings/MC-301-multiplicative-large-sieve-source-energy-capacity.md)

The low-source problem has two quantitatively different arithmetic controls. Pointwise Page/Deuring--Heilbronn theory can nearly eliminate each nonexceptional mode but only in a comparatively small source band. MC-301 uses the multiplicative large sieve instead and reaches every selected primitive real source character through conductor `sqrt(y)`, at the price of controlling only the collective energy:

`sum_(Q(lambda)<=sqrt(y)) |x_lambda|^2 << log y`.

This is a real enlargement of arithmetic access, but the reciprocal endpoint-partition model identifies its exact deficit. An `R`-dimensional obstruction subspace has total bias energy `2^R/R`. At the known blind-support floor `R~log_2 log y`, that energy is about `log y/R`, so the generic `O(log y)` large-sieve budget can still absorb the entire obstruction. To force energy above square-root source cost by this argument requires roughly an additional `log_2 R` independent directions.

The reusable point is that **conductor reach and family capacity are separate currencies**. Extending a theorem from quasi-subpower conductors to `sqrt(y)` does not cross the endpoint if the collective budget simultaneously has enough room for the whole obstruction spectrum.

The remaining target is precise: save a factor comparable to `R` in the source-specific family capacity, force a corresponding factor more obstruction energy in the actual shell geometry, or prove a coupling law that prevents the generic large-sieve budget from being saturated. MC-301 does not show that `sqrt(y)` is an intrinsic arithmetic threshold, nor that the reciprocal partition is realized by the actual Möbius shell.