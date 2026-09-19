# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-293 separate the isolated coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the RH-equivalent continuation boundary of the exact source transform. VIS-294--VIS-298 then close the apparent moving lower-source branch: after exact gamma recentering, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Close the polynomial finite-window gap with dyadic aggregate spectrum control

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299--VIS-304 progressively move the first generic upper error wall from localization leakage to the coefficient-specific prime-power spacing bound `x log log x=o(H)`. VIS-305--VIS-308 show that this absolute scale is not itself a signed arithmetic obstruction: density/parity controls, exact support with randomized phases, and completely multiplicative same-base harmonic controls all cancel well below `H` at the candidate boundary.

VIS-309 then compares those controls to the actual common-time orbit. For fixed `x,H`, the deterministic phases `p^(-it)` have the same long-time quadratic mean as Haar completely multiplicative phases. The Bohr mean square is `O(x log^3(3x))`, so generic deterministic alignment across primes is not the missing mechanism.

VIS-310 quantifies the crudest finite-window transfer. Hard truncating the infinite prime-power series and compressing every retained ratio frequency to one global minimum gap yields a quintic sufficient averaging horizon at the active boundary. VIS-311 keeps coefficient-weighted local spacing and lowers the horizon to cubic. VIS-312 then proves that the finite-cutoff nearest-neighbour representation itself has no infinite-spectrum limit because the supported cross-base ratio frequencies are dense.

VIS-313 replaces individual isolation by a cutoff-free aggregate decomposition. Split at `|lambda|=log 2`. The far band is pointwise `O(x)`, already `o(H)` for `H~x log log x`. In the near band, same-base harmonics disappear; grouping by dyadic arithmetic height gives within-shell spacing `delta_M>>M^(-2)`, while the Wang taper makes the shell energies summable. Shellwise Montgomery--Vaughan plus Minkowski yields

`V^(-1) integral |R_(x,H)(T)|^2 dT << x^2 + x log^3 x + x^3 log^3 x/V`.

Therefore, at `H~x log log x`, deterministic finite-window mean square is `o(H^2)` once

`V >> x log^3 x/(log log x)^2`.

The polynomial finite-window gap is no longer the live obstruction. The remaining distance to the natural local scale `V~H~x log log x` is only logarithmic, roughly `log^3 x/(log log x)^3`. The next useful result should reduce this logarithmic tariff through sharper shell energy/large-sieve accounting, cancellation between shells, or a genuinely effective signed treatment of the far band; the opposite useful result would exhibit a sparse near-resonant packet carrying enough Wang mass to show that some logarithmic loss is real. Another hard support cutoff or unpartitioned nearest-neighbour estimate is no longer informative.

The accepted clue `CLUE-wang-fixed-source-packet-localization` has therefore produced a cutoff-free aggregate-density mechanism; any further use of it should target the residual logarithmic scale or the missing prescribed-height/joint-limit quantifier rather than repeat finite-cutoff spacing.

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet variation, source exponent, localization leakage, coefficient majorants, support-sensitive spacing, random versus completely multiplicative phases, the actual prime-log time orbit, Bohr/Haar equivalence, global versus local ratio spacing, finite-cutoff versus dense-spectrum geometry, dyadic aggregate density, hard versus energy-sensitive tail treatment, finite-window length, moving-frequency limits and the analytic domain of the source transform.

VIS-294--VIS-313 give a repeated control pattern. Exact deterministic pieces can be split too early; generic majorants can lose logarithms; matched support models can show an absolute norm is generic; exact support can still cancel after phase randomization; same-base harmonic relations can be preserved without restoring the boundary; the true deterministic orbit can have the same long-time quadratic mean as Haar; finite-window proofs can manufacture polynomial horizons by compressing weighted spectrum; and dense support becomes manageable again when frequencies are grouped by arithmetic scale before inversion.

A structural transition is credible only after the surviving **finite-height/moving-frequency coherence mechanism** defeats a control that preserves the coefficient distribution, aggregate local ratio density, infinite tail and destination quantifier at the same scale. VIS-313 moves that audit to the logarithmic and pointwise/joint-limit level.
