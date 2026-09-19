# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-293 separate the isolated coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the RH-equivalent continuation boundary of the exact source transform. VIS-294--VIS-298 then close the apparent moving lower-source branch: after exact gamma recentering, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Resolve the support-sensitive endpoint Hilbert form at the upper pointwise layer

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299--VIS-301 show that Wang's displayed localization ceiling is not structural. Decomposing the proof isolates one inside--outside coherence term, and the unconditional Vinogradov--Korobov zero-free region suppresses it far enough that the first generic `H`-scale obstruction becomes the interior Montgomery--Vaughan mean-value estimate.

VIS-302 then specializes that generic estimate to Wang's exact coefficients

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`

and proves

`sum_n n a_n^2=(4/3)x log x+(8/9)x+O(x exp(-cV(log x)))`.

This saves one logarithm and extends the pointwise asymptotic to `x log x=o(H)`.

VIS-303 decomposes the actual remainder at that exposed scale. Powers of two have negligible energy and bounded weighted mass, so throughout `x log x=O(H)` every odd-additive-shift contribution is `o(H)`. The previous `x log x asymp H` layer is therefore carried only by odd-prime-power/even-shift pairs.

VIS-304 shows that even this is not yet the generic boundary once the mean-value inequality is applied on the **actual nonzero frequency set**. For prime powers `q`, let `delta_q` be the nearest-neighbor spacing among the logarithmic frequencies `log q`. A support-sensitive Montgomery--Vaughan inequality and a Brun--Selberg reciprocal-spacing estimate give

`sum_q a_q^2/delta_q << x log log(3x)`

and hence

`int_I |D_x(t)|^2 dt = H sum_q a_q^2 + O(x log log(3x))`.

Combining this with the already controlled localization and gamma terms yields the same pointwise asymptotic whenever

`x log log(3x)=o(H)`.

The `x log x` layer was therefore another ambient-spacing artifact. VIS-303 remains a valid classification of that smaller layer, but it no longer identifies the first unresolved generic upper scale.

The live object is now the **signed endpoint Hilbert form on prime-power logarithmic frequencies** near `x log log x asymp H`. The `log log x` factor comes from an absolute reciprocal-spacing sum plus an upper-bound sieve; it is not an observed correction term in Wang's pair statistic. Determine whether the actual oscillatory endpoint form cancels below that weighted norm, whether the prime-power spacing average can be sharpened for these taper weights, or whether a matched admissible construction attains an `H`-scale contribution and proves the cost genuine.

Do not reinterpret the coincidence with other `log log` scales elsewhere in Mathia as a common mechanism: here the factor is a reciprocal frequency-spacing/sieve cost in a mean-value inequality.

The separate fixed-power arithmetic question remains: can the prime-source envelope itself be improved with information genuinely weaker than the RH-equivalent continuation route?

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, requested output scale, prime-power source support, localization leakage, cross-coherence, coefficient-specific mean-value weight, ambient versus support-sensitive frequency spacing, actual signed endpoint Hilbert form, explicit-formula remainder, deterministic gamma normalization and analytic domain of the source transform.

VIS-294--VIS-304 now give a repeated control pattern. Exact deterministic pieces can be split too early; theorem parameters can hide moving uniformity; a bundled error can contain one load-bearing cross term; source-specific classical information can suppress that term; a generic coefficient majorant can lose a logarithm; support decomposition can delete an entire parity sector; and even the frequency spacing used by a classical inequality can be too coarse if it is computed on the ambient integers rather than the actual arithmetic support.

A genuine new source transition must survive all of these reductions. The current candidate is not `H/log^3 T`, `H/log^2 T` or `H/log T`, and `H/log log x` is still only a proof boundary. The next theorem must decide the signed prime-power endpoint form itself rather than another envelope that forgets its phases.
