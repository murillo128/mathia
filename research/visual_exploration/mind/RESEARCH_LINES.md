# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-293 separate the isolated coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the RH-equivalent continuation boundary of the exact source transform. VIS-294--VIS-298 then close the apparent moving lower-source branch: after exact gamma recentering, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Resolve the signed endpoint Hilbert form beyond density/parity spacing controls

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299--VIS-301 show that Wang's displayed localization ceiling is not structural. Decomposition isolates one inside--outside coherence term, and the unconditional Vinogradov--Korobov zero-free region suppresses it far enough that the first generic `H`-scale obstruction moves into the interior Montgomery--Vaughan mean-value estimate.

VIS-302 specializes that estimate to Wang's exact coefficients and saves one logarithm, extending the pointwise asymptotic to `x log x=o(H)`. VIS-303 then uses the actual support: powers of two have negligible energy and bounded weighted mass, so throughout `x log x=O(H)` every odd-additive-shift contribution is `o(H)`. VIS-304 applies the weighted Hilbert inequality on the actual prime-power logarithmic frequencies and obtains

`sum_q a_q^2/delta_q << x log log(3x)`,

moving the generic pointwise range again to `x log log(3x)=o(H)`.

VIS-305 now supplies the matched control that VIS-304 lacked. On the odd lattice, retain each site independently with probability `2/log x`, matching prime density and parity. Conditional nearest-neighbor gaps are geometric, and the exact inverse-gap expectation produces

`E sum_(q occupied in [x,2x]) b_q^2/delta(q)=Theta(x log log x)`

for Wang-scale weights. Thus the `log log x` absolute reciprocal-spacing cost already occurs in a parity- and density-matched independent support. It is not, by itself, an arithmetic signature of prime powers.

This rules out one tempting continuation: no argument that remembers essentially only density, parity, coefficient size and nearest-neighbor sparsity can uniformly improve the `x log log x` norm. The live object is more specific: the **signed endpoint Hilbert form** on the actual prime-power logarithmic frequencies, or an arithmetic spacing correlation absent from the Bernoulli control. A further gain must use source information that the matched support does not reproduce.

The `x log log x` scale remains a proof boundary, not a proven correction to Wang's statistic. VIS-305 does not lower-bound the true prime-power norm or the signed endpoint form. A matched admissible construction attaining `H` scale for the signed form would establish a genuine obstruction; a cancellation theorem would move the boundary again. The fixed-power prime-source envelope remains a separate arithmetic question.

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, localization leakage, cross-coherence, coefficient-specific mean-value weight, ambient versus support-sensitive frequency spacing, matched random spacing controls, actual signed endpoint phase, deterministic gamma normalization and analytic domain of the source transform.

VIS-294--VIS-305 give a repeated control pattern. Exact deterministic pieces can be split too early; theorem parameters can hide moving uniformity; a bundled error can contain one load-bearing cross term; generic coefficient majorants can lose logarithms; support decomposition can delete whole sectors; sparse-frequency geometry can improve an ambient bound; and a matched random support can then show that the remaining absolute norm is still generic. A structural transition is credible only after it survives all of those reductions and the surviving signed object itself is controlled or matched.
