# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-286 classify the isolated coefficient-scale profile and its source boundaries. VIS-287--VIS-293 move to Wang's complete pair statistic, separate deterministic gamma structure from the arithmetic source, and show that first-half-plane holomorphy of the exact source transform is RH-equivalent rather than an independent continuation mechanism.

VIS-294--VIS-298 close the apparent moving lower-source branch. Once the explicit gamma contribution is recentered before norm estimates, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Resolve the interior mean-value budget at the true upper pointwise layer

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299 shows that the fixed exponent gap was not the true pointwise boundary. Re-running Wang's displayed localization proof gives the same gamma-recentered asymptotic whenever `x log^3 T/H -> 0`.

VIS-300 identifies the only term carrying that extra logarithm. The pure inside/outside leakage energies are already `O(x log^2 T)`, so at `x=O(H/log^3 T)` they are `o(H)`; the whole unresolved scale is the bilinear inside--outside coherence `C_I(x)`.

VIS-301 then removes that localization boundary. The unconditional Vinogradov--Korobov zero-free region inserts the near-height attenuation `x^(-eta_T)` with `eta_T asymp L^(-2/3)(log L)^(-1/3)` into both sides of the coherence term. Re-running the localization proof with that information gives `C_I(x)=o(H)` and preserves the pointwise asymptotic throughout

`x=o(H/L^2)`.

The next generic `H`-scale term is therefore the **interior Montgomery--Vaughan mean-value remainder** `O(x log^2(2x))`, which reaches output scale at `x asymp H/L^2`. The live upper question is whether Wang's exact coefficients

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`

have enough arithmetic structure to improve that generic bound, produce a stable deterministic correction, or realize the `H` scale sharply. Any continuation should attack this exact interior term. Re-estimating localization leakage or the old `H/L^3` coherence without changing the zero-free input is no longer a live boundary test.

The separate fixed-power arithmetic question remains: can the prime-source envelope itself be improved with information genuinely weaker than the RH-equivalent continuation route?

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, requested output scale, prime-power source measure, smoothing multiplier, theorem-uniformity range, pure localization leakage, cross-coherence, interior Dirichlet-polynomial mean-value error, explicit-formula remainder, deterministic gamma normalization and analytic domain of the source Dirichlet transform.

VIS-294--VIS-301 now show four ways a nominal boundary can be misread. Exact deterministic pieces may have been split before Cauchy--Schwarz; a theorem may be packaged with fixed parameters even though its proof exposes a larger moving regime; several errors may be bundled into one big-O even though only one cross term is load-bearing; and that cross term can itself fall below resolution once classical source information is inserted, exposing a different interior estimate underneath.

A genuine new source transition must survive exact recombination, proof-level uniformity, energy decomposition and coefficient-specific testing of the first remaining term at output scale. The current upper candidate is not the old ratio `xL^3/H`, but whether the exact Wang Dirichlet polynomial improves or saturates the `xL^2` mean-value horizon.