# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-293 separate the isolated coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the RH-equivalent continuation boundary of the exact source transform. VIS-294--VIS-298 then close the apparent moving lower-source branch: after exact gamma recentering, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Replace pointwise frequency isolation by aggregate density-sensitive infinite-spectrum control

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299--VIS-304 progressively move the first generic upper error wall from localization leakage to the coefficient-specific prime-power spacing bound `x log log x=o(H)`. VIS-305--VIS-308 show that this absolute scale is not itself a signed arithmetic obstruction: density/parity controls, exact support with randomized phases, and completely multiplicative same-base harmonic controls all cancel well below `H` at the candidate boundary.

VIS-309 then compares those controls to the actual common-time orbit. For fixed `x,H`, the deterministic phases `p^(-it)` have the same long-time quadratic mean as Haar completely multiplicative phases. The Bohr mean square is `O(x log^3(3x))`, so generic deterministic alignment across primes is not the missing mechanism.

VIS-310 quantifies the crudest finite-window transfer. Hard truncating the infinite prime-power series and compressing every retained ratio frequency to one global minimum gap yields a sufficient averaging horizon only at

`V >> x^5 log^3 x/(log log x)^2`

when `H~x log log x`. VIS-311 keeps the local spacing of each retained rational-ratio frequency and its coefficient energy, lowering the sufficient horizon to

`V >> x^3 log^3 x/(log log x)^2`.

Two powers of `x` were therefore artifacts of global-gap compression. But VIS-312 shows that the finite-cutoff nearest-neighbor representation has no cutoff-free continuation. The nonzero cross-base prime-ratio frequencies `log(p/q)` surviving the Wang kernel are dense in `R`. Consequently every fixed retained frequency loses nearest-neighbor isolation as the cutoff grows, and the VIS-311 functional

`sum_lambda |B_lambda|^2/delta_lambda`

diverges as the cutoff tends to infinity. One cannot remove the hard tail simply by sending `Y->infinity` inside the same weighted Montgomery--Vaughan nearest-neighbor denominator.

This is a proof-method obstruction, not a lower bound on true dephasing. Dense frequency support can still have small coefficient energy. The live finite-height problem is now representation-specific: replace individual spacing by a cutoff-free quantity that remains meaningful on a dense spectrum, such as local frequency counts in blocks, a smooth/dyadic large-sieve decomposition, or direct control of the finite-window kernel `min(V,1/|lambda-mu|)` against coefficient energy. The opposite useful outcome would be an explicit sparse near-resonant family carrying enough Wang coefficient mass to force an `H`-scale remainder despite the small Bohr energy.

The accepted clue `CLUE-wang-fixed-source-packet-localization` remains aligned with this destination, but another nearest-neighbor hard-cutoff estimate is no longer the most informative move.

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet variation, source exponent, localization leakage, coefficient majorants, support-sensitive spacing, random versus completely multiplicative phases, the actual prime-log time orbit, Bohr/Haar equivalence, global versus local ratio spacing, finite-cutoff versus dense-spectrum geometry, hard versus energy-sensitive tail treatment, finite-window length, moving-frequency limits and the analytic domain of the source transform.

VIS-294--VIS-312 give a repeated control pattern. Exact deterministic pieces can be split too early; generic majorants can lose logarithms; matched support models can show an absolute norm is generic; exact support can still cancel after phase randomization; same-base harmonic relations can be preserved without restoring the boundary; the true deterministic orbit can have the same long-time quadratic mean as Haar; finite-window proofs can manufacture polynomial horizons by compressing weighted spectrum; and the nearest-neighbor geometry itself ceases to exist in the infinite dense support.

A structural transition is credible only after the surviving **finite-height/moving-frequency coherence mechanism** defeats a control that preserves the coefficient distribution, aggregate local ratio density, infinite tail and destination quantifier at the same scale.
