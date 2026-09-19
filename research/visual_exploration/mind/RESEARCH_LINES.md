# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-286 classify the isolated coefficient-scale profile and its source boundaries. VIS-287--VIS-293 move to Wang's complete pair statistic, separate deterministic gamma structure from the arithmetic source, and show that first-half-plane holomorphy of the exact source transform is RH-equivalent rather than an independent continuation mechanism.

VIS-294--VIS-298 close the apparent moving lower-source branch. Once the explicit gamma contribution is recentered before norm estimates, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Resolve the surviving even-shift off-diagonal remainder at the upper pointwise layer

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299 shows that the fixed exponent gap was not the true pointwise boundary. Re-running Wang's displayed localization proof first gives the same gamma-recentered asymptotic whenever `x log^3 T/H -> 0`.

VIS-300 identifies the only term carrying that extra logarithm. The pure inside/outside leakage energies are already `O(x log^2 T)`, so at `x=O(H/log^3 T)` they are `o(H)`; the whole unresolved scale is the bilinear inside--outside coherence `C_I(x)`.

VIS-301 removes that localization boundary. The unconditional Vinogradov--Korobov zero-free region inserts the near-height attenuation `x^(-eta_T)` with `eta_T asymp L^(-2/3)(log L)^(-1/3)` into both sides of the coherence term. Re-running the localization proof with that information gives `C_I(x)=o(H)` and preserves the pointwise asymptotic throughout `x=o(H/L^2)`.

VIS-302 then shows that the next apparent `H/L^2` wall is also not structural. For Wang's exact coefficients

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`,

the coefficient weight entering Montgomery--Vaughan has the exact asymptotic

`sum_n n a_n^2=(4/3)x log x+(8/9)x+O(x exp(-cV(log x)))`.

The displayed `O(x log^2 x)` bound loses one logarithm through the pointwise estimate on `Lambda`. Feeding the coefficient-specific moment back into the same argument preserves the complete pointwise asymptotic whenever

`x log(2x)=o(H)`.

VIS-303 now removes one complete arithmetic sector from the actual remainder at the first unresolved generic upper layer `x log x asymp H`. Splitting the Dirichlet polynomial into powers of two and odd prime powers gives a power-of-two energy `<<1/x` and weighted mean-value mass `<<1`. Hence throughout `x log(2x)=O(H)` the full off-diagonal remainder differs from the odd-prime-power remainder by `o(H)`. Since odd additive difference occurs exactly when one supported coefficient is a power of two and the other an odd prime power, **all odd additive shifts are negligible at `H` resolution**.

The live upper-source object is therefore narrower than the unrestricted off-diagonal integral: it is the exact interval-kernel sum over pairs of odd prime powers, equivalently the surviving even-shift sector. Determine whether those exact frequencies and weights yield further oscillatory cancellation, a stable deterministic `H`-scale correction, or a matched admissible lower/control construction showing that this scale is genuinely attainable. Re-estimating powers of two, odd shifts, localization leakage, the old `H/L^3` coherence, or the coarse `x log^2 x` coefficient majorant is no longer a live boundary test.

The separate fixed-power arithmetic question remains: can the prime-source envelope itself be improved with information genuinely weaker than the RH-equivalent continuation route?

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, requested output scale, prime-power source measure, smoothing multiplier, theorem-uniformity range, pure localization leakage, cross-coherence, coefficient-specific mean-value weight, actual off-diagonal Dirichlet-polynomial remainder, parity support inside that remainder, explicit-formula remainder, deterministic gamma normalization and analytic domain of the source Dirichlet transform.

VIS-294--VIS-303 now show six ways a nominal boundary can be misread. Exact deterministic pieces may have been split before Cauchy--Schwarz; a theorem may be packaged with fixed parameters even though its proof exposes a larger moving regime; several errors may be bundled into one big-O even though only one cross term is load-bearing; classical source information can suppress that term and expose a different estimate underneath; a generic theorem bound can itself be loose after specializing to the exact arithmetic coefficient sequence; and the newly exposed remainder can contain a whole source-support sector whose coefficient mass is too sparse to matter at destination resolution.

A genuine new source transition must survive exact recombination, proof-level uniformity, energy decomposition, coefficient-specific testing and support-level decomposition of the first remaining term at output scale. The current upper candidate is not `xL^3/H` or `xL^2/H`, and not the full unrestricted off-diagonal remainder at `xL/H`; it is the odd-prime-power/even-shift part of that remainder in the polynomial source regime. That is still a proof boundary, not an established transition of the pair-correlation statistic.