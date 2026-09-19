---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-293-wang-source-dirichlet-rh-half-plane.md
  - research/visual_exploration/findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md
  - research/visual_exploration/findings/VIS-301-wang-zero-free-localization-log-squared-window.md
  - research/visual_exploration/findings/VIS-302-wang-weighted-mean-value-log-boundary.md
  - research/visual_exploration/findings/VIS-303-wang-odd-shift-power-two-sparsity.md
  - research/visual_exploration/findings/VIS-304-wang-prime-power-spacing-loglog-boundary.md
  - research/visual_exploration/findings/VIS-305-cramer-parity-control-loglog-spacing-norm.md
  - research/visual_exploration/findings/VIS-306-bernoulli-signed-shell-hilbert-cancellation.md
  - research/visual_exploration/findings/VIS-307-prime-power-random-phase-hilbert-cancellation.md
  - research/visual_exploration/findings/VIS-308-base-prime-harmonic-phase-cancellation.md
  - research/visual_exploration/findings/VIS-309-wang-bohr-time-haar-equivalence.md
  - research/visual_exploration/findings/VIS-310-wang-hard-truncation-global-gap-quintic-horizon.md
  - research/visual_exploration/findings/VIS-311-wang-weighted-gap-cubic-horizon.md
  - research/visual_exploration/findings/VIS-312-wang-dense-ratio-spectrum-no-nearest-spacing.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The fixed-power branch is already reduced to a classical arithmetic envelope: `VIS-283`--`VIS-293` isolate the source channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. `VIS-294`--`VIS-298` remove the apparent moving lower-source barrier by exact gamma recentering.

For the moving upper pointwise branch, `VIS-301`--`VIS-304` progressively move the first generic error wall to the weighted Hilbert bound

`R_(x,H)(T)=O(x log log(3x))`,

so the current pointwise asymptotic holds under `x log log(3x)=o(H)`. `VIS-305`--`VIS-308` then show that the corresponding absolute spacing scale is not by itself a signed obstruction: parity/density controls, exact prime-power support with independent phases, and finally a completely multiplicative Steinhaus field preserving all same-base harmonics each have signed remainder far below `H` at `H asymp x log log x`.

`VIS-309` removes a broader ambiguity. For the **true deterministic** vertical phases, the long-time Bohr mean satisfies

`M_T R_(x,H)(T)=0`,

`M_T |R_(x,H)(T)|^2 = E|R_I^f|^2 << x log^3(3x)`,

where the expectation is exactly the completely multiplicative Haar control of `VIS-308`. Thus at the log-log boundary the set of starting heights with `|R_(x,H)(T)|>=eta H` has upper density

`<< log^3(3x)/(eta^2 x (log log(3x))^2) -> 0`

in the iterated Bohr-time sense. The one-parameter prime-phase relation `p^(-iT)` therefore does not generically restore the obstruction.

`VIS-310` quantified the most direct finite-window transfer and showed why it was too coarse. Hard support truncation at `Y`, followed by a single global ratio-frequency gap, gives a sufficient `o(H^2)` averaging horizon only at

`V >> x^5 log^3 x/(log log x)^2`

when `H asymp x log log x`.

`VIS-311` replaces that worst-gap step by the weighted Montgomery--Vaughan inequality. If `m_lambda` is the reduced rational height of a grouped ratio frequency, the exact Wang spectrum satisfies

`sum_lambda m_lambda |B_lambda|^2 << x^2 log^3(3x)`.

Since a frequency retained below `Y` has individual inverse spacing at most `Y m_lambda`, the finite-window bound becomes

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x L^3 + H x^(5/2)L^(3/2)V^(-1/2)`

after optimizing the same hard cutoff. At `H asymp x ell`, this is `o(H^2)` on the improved sufficient scale

`V >> x^3 L^3/ell^2`,

where `L=log(3x)` and `ell=log log(3x)`.

`VIS-312` now closes the most literal nontruncated continuation of that argument. Quotients of ordinary primes are dense in the positive reals, so their logarithms already form a dense subset of Wang's ratio-frequency spectrum. The kernel `K_H(lambda)` removes only a discrete frequency lattice, hence the **nonzero cross-base coefficient support remains dense**. For every fixed retained frequency the nearest-neighbor spacing inside `Lambda_Y` tends to zero as `Y->infinity`, and the `VIS-311` spacing functional `W_(x,H)(Y)` necessarily diverges. Thus one cannot remove the hard cutoff by simply taking the same nearest-neighbor Hilbert inequality to the full spectrum.

The remaining finite-window problem is therefore not merely “control the tail in energy.” It is to do so with an **aggregate-density representation** that remains meaningful for a dense frequency set, or else identify an explicit sparse resonance mechanism that defeats such a representation.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can one transfer the small Bohr energy of `VIS-309` to finite windows using scale-local density, smooth/dyadic frequency blocks, a large-sieve/nonharmonic-Fourier estimate, or direct finite-window-kernel control that tolerates the dense full ratio spectrum; or instead exhibit a concrete sparse resonance mechanism whose exceptional heights sustain an `H`-scale remainder near `H asymp x log log x`?

The live issue is no longer generic coefficient sensitivity, a global minimum gap, or even an unpartitioned nearest-neighbor treatment of the infinite spectrum. `VIS-311` handles coefficient weighting at finite cutoff; `VIS-312` proves that nearest-neighbor isolation disappears altogether in the full spectrum.

## Why it may matter

The sequence `VIS-301`--`VIS-312` has removed a series of apparently structural barriers or insufficient proof abstractions: localization leakage, generic coefficient majorants, ambient spacing, support-sensitive absolute spacing, density-matched signed controls, exact prime-power support, same-base multiplicative harmonics, the distinction between product-Haar phases and the actual vertical flow at long-time first/second moment level, the naive hard-truncation/global-gap bridge, most of the global-gap loss under coefficient weighting, and now the idea that the finite nearest-neighbor functional itself survives removal of the cutoff.

A successful aggregate-density finite-window estimate could still move the deterministic scale toward the natural `x log log x` range. Failure would be equally informative if it isolates an explicit family of rare ratio resonances carrying enough Wang coefficient mass to survive all existing controls.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, start from

`R_(x,H)(T)=sum_(q!=r) a_q a_r K_H(q,r) exp(-iT log(q/r))`.

The next useful result must do one of two things:

- partition or otherwise represent the **full dense ratio spectrum** so that the tail is controlled by aggregate local density and coefficient energy rather than an individual nearest-neighbor gap; quantify the resulting finite-window mean-square/large-deviation bound and determine whether its sufficient horizon beats `x^3 log^3 x/(log log x)^2`; or
- identify an explicit family of near-resonant rational-ratio frequencies and heights for which the phase sum is coherently `H`-scale, then show that this survives Wang's taper and all previously isolated errors.

A viable positive route may use smooth/dyadic height or frequency blocks, a large-sieve inequality expressed through counts in frequency intervals, or direct summation against the finite-window kernel `min(V,1/|lambda-mu|)`. It must explicitly survive the `VIS-312` density obstruction rather than silently reintroduce a positive full-spectrum nearest-neighbor spacing.

A result that only re-proves infinite-time Kronecker/Haar equidistribution, support geometry, same-base harmonic coherence, the absolute Hilbert majorant, the `VIS-310` global-gap estimate, the `VIS-311` weighted hard-cutoff estimate, or a formal `Y->infinity` limit of the same nearest-neighbor functional is already covered or ruled out.

## Evidence boundary

`VIS-304` is an upper bound, not proof that `x log log x` is attained. `VIS-305`--`VIS-308` are increasingly faithful negative controls. `VIS-309` is exact for the Bohr-time first and second moments of the actual deterministic remainder, but its density statement is **iterated**: fix `x,H`, take the long-time limit, then let `x` grow.

`VIS-310` and `VIS-311` are proof-method controls, not lower bounds on true finite-window dephasing. `VIS-311` proves that coefficient weighting materially improves the hard-cutoff transfer, but its cubic sufficient horizon still inherits the uniform tail cost from `VIS-310`.

`VIS-312` is also a proof-method obstruction. Dense frequency support makes the unpartitioned nearest-neighbor spacing vanish, but it does **not** imply a large finite-window remainder: the coefficients decay and an aggregate-density or kernel estimate may remain strong. No joint limit with `x=x(T)`, pointwise cancellation at `H asymp x log log x`, stronger RH criterion, or new prime-gap theorem is established.

## Research disposition

Outcome so far: **the moving upper-source branch has narrowed to aggregate-density finite-window control of a dense weighted ratio spectrum versus exceptional-height resonance**. The global minimum-gap loss is no longer the issue, and the finite-cutoff nearest-neighbor inequality cannot simply be continued to the full spectrum.

The clue remains accepted and live. The next contribution should quantify a block/local-density or direct-kernel energy mechanism that genuinely handles the infinite dense spectrum, or exhibit an explicit sparse resonance family; another isolated-gap estimate is no longer informative.