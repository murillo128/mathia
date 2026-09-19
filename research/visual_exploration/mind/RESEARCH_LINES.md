# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-293 separate the isolated coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the RH-equivalent continuation boundary of the exact source transform. VIS-294--VIS-298 then close the apparent moving lower-source branch: after exact gamma recentering, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Resolve the deterministic prime-power phase channel beyond exact-support random-phase controls

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299--VIS-301 show that Wang's displayed localization ceiling is not structural. Decomposition isolates one inside--outside coherence term, and the unconditional Vinogradov--Korobov zero-free region suppresses it far enough that the first generic `H`-scale obstruction moves into the interior Montgomery--Vaughan mean-value estimate.

VIS-302 specializes that estimate to Wang's exact coefficients and saves one logarithm. VIS-303 uses the actual support to remove the power-of-two/odd-shift sector. VIS-304 applies the weighted Hilbert inequality on the actual prime-power logarithmic frequencies and obtains an absolute spacing cost `O(x log log x)`, moving the generic pointwise range to `x log log x=o(H)`.

VIS-305 shows that this absolute reciprocal-spacing scale is not arithmetic by itself: a parity- and density-matched Bernoulli support already has expected cost `Theta(x log log x)` under the same Wang-scale weights. VIS-306 then evaluates the signed endpoint form on that Bernoulli support and obtains expectation `O(x)`, variance `O(x log^3 x)` and hence `o_p(H)` at `H~x log log x`. Density, parity, coefficient size and short-gap harmonic tails therefore do not force an `H`-scale signed obstruction.

VIS-307 removes the remaining support-geometry ambiguity. It keeps **every actual prime power**, every prime-power spacing and every Wang coefficient magnitude, but assigns an independent Steinhaus phase to each prime-power support point. The signed quadratic remainder has mean zero and second moment

`E |R_I^epsilon|^2 << x log^3 x`,

uniformly in the interval position and length. Hence it is `o_p(H)` again at `H~x log log x`. Exact prime-power locations, all spacing correlations and the exact coefficient magnitudes are therefore still insufficient when deterministic relative phases are destroyed.

The live arithmetic object has narrowed to **phase organization**. Any genuine `H`-scale obstruction for the true Wang polynomial must use deterministic relative coefficient phases or a coherence relation coupled to them. In particular, the independent phase control deliberately destroys the harmonic relation among `p,p^2,p^3,...`; a sharper matched control should preserve one base-prime phase with powers tied coherently, or otherwise isolate a specific deterministic endpoint-phase mechanism. Refining support statistics alone no longer tests the surviving hypothesis.

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, localization leakage, cross-coherence, coefficient-specific mean-value weight, ambient versus support-sensitive frequency spacing, matched random spacing controls, signed matched-control cancellation, exact prime-power support, independent versus multiplicatively coherent phases, actual endpoint phase, deterministic gamma normalization and analytic domain of the source transform.

VIS-294--VIS-307 give a repeated control pattern. Exact deterministic pieces can be split too early; theorem parameters can hide moving uniformity; bundled errors can contain one load-bearing cross term; generic coefficient majorants can lose logarithms; support decomposition can delete whole sectors; sparse-frequency geometry can improve ambient bounds; matched support models can show an absolute norm is generic; signed controls can cancel below the apparent critical scale; and now even the exact source support can be preserved while randomizing only phase organization. A structural transition is credible only after the surviving phase/coherence mechanism itself defeats the strongest matched control.