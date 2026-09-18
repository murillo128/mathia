# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-286 classify the isolated coefficient-scale profile and its source boundaries. VIS-287--VIS-293 move to Wang's complete pair statistic, separate deterministic gamma structure from the arithmetic source, and show that first-half-plane holomorphy of the exact source transform is RH-equivalent rather than an independent continuation mechanism.

VIS-294--VIS-298 close the apparent moving lower-source branch. Once the explicit gamma contribution is recentered before norm estimates, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Resolve the inside--outside coherence at the true upper localization layer

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299 shows that the fixed exponent gap `x<=T^lambda`, `lambda<theta`, was also not the true pointwise boundary. Re-running Wang's displayed localization proof gives the same gamma-recentered asymptotic whenever

`x log^3 T / H -> 0`, with `H=T^theta`.

VIS-300 identifies what actually remains at the first unresolved scale. Writing `A_I` for the interval field and `R_I=A-A_I` for the omitted-zero tail, Wang's exact energy identity gives

`2pi F_I(x)-int_I |A|^2 = int_(R\I)|A_I|^2 - 2 Re int_I A_I overline(R_I) - int_I |R_I|^2`.

Both pure leakage energies are only `O(x log^2 T)`, hence already `o(H)` when `x=O(H/log^3 T)`. The extra logarithm in Wang's `O(x log^3 T)` localization bound comes solely from estimating the bilinear cross-coherence

`C_I(x)=int_I A_I(x,t) overline(A(x,t)-A_I(x,t)) dt`

by absolute values. At `x~H/log^3 T`, the whole unresolved `H`-scale problem is therefore whether `Re C_I(x)=o(H)`, has a deterministic `H`-scale correction, or can survive under an admissible control.

The live upper question is no longer “improve localization tails” in general. Their `L^2` masses are already negligible at the boundary. The next probe must exploit phase/cancellation structure of this **specific inside--outside bilinear term**, compute its leading contribution, or construct a control showing that an `H`-scale coherence term can persist. The separate fixed-power arithmetic question remains: can the prime-source envelope itself be improved with information genuinely weaker than the RH-equivalent continuation route?

## Recombine exact deterministic structure and decompose localization before interpreting an error wall

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, requested output scale, prime-power source measure, smoothing multiplier, theorem-uniformity range, pure localization leakage, cross-coherence, explicit-formula remainder, deterministic gamma normalization and analytic domain of the source Dirichlet transform.

VIS-294--VIS-300 now show three ways a nominal boundary can be misread. Exact deterministic pieces may have been split before Cauchy--Schwarz; a theorem may be packaged with fixed parameters even though its proof exposes a larger moving regime; or several error mechanisms may be bundled into one big-O even though only one coherent cross term is load-bearing at the boundary.

A genuine new source transition must survive exact recombination, proof-level uniformity, and an energy decomposition that isolates the term actually reaching output scale. The current upper candidate is not the raw ratio `x log^3 T/H` by itself but the behavior of `C_I(x)` when that ratio is order one.