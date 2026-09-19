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
  - research/visual_exploration/findings/VIS-313-wang-dyadic-ratio-shell-linear-horizon.md
  - research/visual_exploration/findings/VIS-314-selberg-prime-pair-sieve-wang-shell-log-square.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The fixed-power branch is already reduced to a classical arithmetic envelope: `VIS-283`--`VIS-293` isolate the source channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. `VIS-294`--`VIS-298` remove the apparent moving lower-source barrier by exact gamma recentering.

For the moving upper pointwise branch, `VIS-301`--`VIS-304` move the first generic error wall to the weighted Hilbert bound `R_(x,H)(T)=O(x log log(3x))`. `VIS-305`--`VIS-309` then show that density, exact prime-power support, same-base harmonic phase structure, and even the true deterministic long-time quadratic mean do not by themselves explain an `H`-scale obstruction at `H asymp x log log x`.

`VIS-310`--`VIS-312` expose hard-cutoff/global-gap and full-spectrum nearest-neighbor artifacts. `VIS-313` replaces them by a cutoff-free dyadic ratio-shell decomposition and obtains, with `L=log(3x)`,

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + x L^3 + x^3 L^3/V`,

so at `H asymp x ell`, `ell=log log(3x)`, the mean square is `o(H^2)` for

`V >> x L^3/ell^2`.

`VIS-314` now removes one of those logarithms without changing the representation. The `log^3 M` shell energy in `VIS-313` came from bounding the two squared von-Mangoldt weights independently. Applying the classical dimension-two Selberg upper-bound sieve to the prime-prime pairs before summing the reciprocal gap kernel gives

`E_M << M v_x(M)^4 log^2(4M)`.

Proper prime powers are lower order. Replaying the same cutoff-free Montgomery--Vaughan/Minkowski recombination yields

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + x L^2 + x^3 L^2/V`,

and therefore the improved sufficient finite-window scale

`V >> x L^2/ell^2`.

The remaining distance to the natural local window `V asymp H asymp x ell` is still logarithmic, of relative size roughly `L^2/ell^3`, but the first residual logarithm was only a two-point coefficient-mass artifact.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can the cutoff-free finite-window estimate now be sharpened from

`V >> x log^2 x/(log log x)^2`

to the natural local scale

`V asymp H asymp x log log x`,

or can one exhibit an explicit exceptional-height mechanism showing that some residual logarithmic loss is genuinely necessary?

After `VIS-314`, another crude two-point prime-pair count is no longer the informative frontier. The live issue is the organization of many ratio frequencies over a finite window: shellwise `M^2/V` separation cost, cancellation across arithmetic-height shells, a stronger aggregate-density/large-sieve treatment, or genuine deterministic coherence at exceptional starting heights.

## Why it may matter

`VIS-301`--`VIS-314` have successively removed localization leakage, generic coefficient majorants, ambient spacing, support-sensitive absolute spacing, increasingly faithful random-phase controls, generic deterministic Bohr-time alignment, hard support truncation, global minimum-gap compression, dense-spectrum nearest-neighbor failure, and now one logarithm caused by discarding prime-pair sparsity.

The remaining finite-window gap is therefore narrower and more structural. A successful aggregate-frequency estimate could bring the deterministic mean-square window close to `H` without assuming new zeta information. Failure would be equally useful if it isolates a concrete packet of near-resonant ratio frequencies whose Wang mass and deterministic phase coherence survive all current controls.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, start from the cutoff-free decomposition of `VIS-313` with the sharpened shell energy of `VIS-314`. A next useful result must do one of two things:

- reduce the remaining `L^2` finite-window tariff enough that the sufficient scale approaches `V asymp x ell`, using an aggregate-frequency count, a sharper shellwise large-sieve/kernel estimate, cancellation between shells, or another argument that preserves the infinite support; or
- identify explicit starting heights and a quantitatively sufficient family of ratio interactions whose deterministic phases produce an `H`-scale remainder near `H asymp x ell`, surviving the `VIS-309` small Bohr energy and the `VIS-314` improved finite-window mean-square control.

A result that merely reapplies a hard support cutoff, a global/nearest frequency gap, or the same dimension-two prime-pair upper sieve is no longer informative unless it exposes a genuinely new obstruction.

## Evidence boundary

`VIS-304` remains only an upper bound for the actual pointwise remainder. `VIS-305`--`VIS-309` are controls or iterated long-time statements, not pointwise cancellation at every height. `VIS-310`--`VIS-313` are finite-window proof-method reductions.

`VIS-314` improves the cutoff-free mean-square horizon by a classical upper-sieve input. It does not prove a prime-pair asymptotic, does not prove pointwise cancellation, does not justify a joint moving `x(T)` limit, and does not show that its remaining logarithmic factor is intrinsic.

No stronger RH criterion, new prime-gap theorem, or pointwise Wang asymptotic at `H asymp x log log x` is established.

## Research disposition

Outcome so far: **the moving upper-source branch has progressed from a polynomial finite-window barrier to a cutoff-free near-linear bound whose first residual logarithm is now removed by prime-pair sparsity**. The unresolved frontier is the remaining aggregate ratio-frequency cost versus genuine exceptional-height coherence.

The clue remains accepted and live. The next contribution should attack that many-frequency finite-window structure or exhibit a concrete obstruction; another two-point shell-mass refinement is unlikely to change the current decision boundary.