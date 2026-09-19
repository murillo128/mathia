# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-293 separate the isolated coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the RH-equivalent continuation boundary of the exact source transform. VIS-294--VIS-298 then close the apparent moving lower-source branch: after exact gamma recentering, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Resolve the signed endpoint Hilbert form beyond density/parity controls

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299--VIS-301 show that Wang's displayed localization ceiling is not structural. Decomposition isolates one inside--outside coherence term, and the unconditional Vinogradov--Korobov zero-free region suppresses it far enough that the first generic `H`-scale obstruction moves into the interior Montgomery--Vaughan mean-value estimate.

VIS-302 specializes that estimate to Wang's exact coefficients and saves one logarithm. VIS-303 uses the actual support to remove the power-of-two/odd-shift sector. VIS-304 applies the weighted Hilbert inequality on the actual prime-power logarithmic frequencies and obtains an absolute spacing cost `O(x log log x)`, moving the generic pointwise range to `x log log x=o(H)`.

VIS-305 shows that this absolute reciprocal-spacing scale is not arithmetic by itself: a parity- and density-matched Bernoulli support already has expected cost `Theta(x log log x)` under the same Wang-scale weights.

VIS-306 now runs the matched control on the **signed endpoint form itself** rather than only on its absolute Hilbert majorant. For the Bernoulli-thinned odd lattice, the off-diagonal signed Dirichlet remainder has expectation `O(x)`, variance `O(x log^3 x)` and hence size `O_p(x)`. In the critical comparison regime `H~x log log x`, this is `o_p(H)`. Density, parity, coefficient size and short-gap harmonic tails therefore do not create an `H`-scale signed obstruction even though their absolute spacing norm is already `Theta(x log log x)`.

This materially narrows the live arithmetic object. A genuine prime-power obstruction must now come from phase/coherence or spacing correlations absent from independent thinning, or from another exact source feature not represented by the Bernoulli control. The `x log log x` absolute proof wall should no longer be promoted as evidence for such an obstruction.

VIS-306 is a negative control, not a theorem about prime powers. The current target is to evaluate or bound the actual prime-power signed endpoint Hilbert form at the same scale and identify which arithmetic correlations, if any, prevent the Bernoulli cancellation mechanism.

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, localization leakage, cross-coherence, coefficient-specific mean-value weight, ambient versus support-sensitive frequency spacing, matched random spacing controls, signed matched-control cancellation, actual prime-power endpoint phase, deterministic gamma normalization and analytic domain of the source transform.

VIS-294--VIS-306 give a repeated control pattern. Exact deterministic pieces can be split too early; theorem parameters can hide moving uniformity; a bundled error can contain one load-bearing cross term; generic coefficient majorants can lose logarithms; support decomposition can delete whole sectors; sparse-frequency geometry can improve an ambient bound; a matched random support can show the remaining absolute norm is generic; and the signed version of the same control can then cancel below the apparent critical scale. A structural transition is credible only after the surviving signed object itself defeats the strongest matched control.