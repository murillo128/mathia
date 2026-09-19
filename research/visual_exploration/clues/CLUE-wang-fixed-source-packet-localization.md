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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The fixed-power branch is already reduced to a classical arithmetic envelope: `VIS-283`--`VIS-293` isolate the source channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. `VIS-294`--`VIS-298` remove the apparent moving lower-source barrier by exact gamma recentering.

For the moving upper pointwise branch, `VIS-301`--`VIS-304` progressively move the first generic error wall to the weighted Hilbert bound

`R_(x,H)(T)=O(x log log(3x))`,

so the current pointwise asymptotic holds under `x log log(3x)=o(H)`. `VIS-305`--`VIS-308` show that this absolute spacing scale is not by itself a signed obstruction: matched density/parity controls, exact prime-power support with independent phases, and completely multiplicative same-base harmonic controls all cancel well below `H` at `H asymp x log log x`.

`VIS-309` shows that the **true deterministic** vertical phases have the same long-time quadratic mean as the completely multiplicative Haar control. Thus generic deterministic alignment across primes is not the missing mechanism.

`VIS-310`--`VIS-312` then expose and remove two proof artifacts. A hard support cutoff plus one global gap yields only a quintic finite-window horizon; coefficient-weighted local spacing lowers that to cubic; but the full ratio-frequency support is dense, so the nearest-neighbor functional itself has no cutoff-free continuation.

`VIS-313` supplies the first cutoff-free aggregate-density replacement. Split the grouped spectrum at the fixed ratio boundary `|lambda|=log 2`. The far band is pointwise `O(x)` because `sum_q a_q<<sqrt(x)`, hence already `o(H)` at `H asymp x log log x`. The strict near band contains no same-base harmonics; cross-base ratios are uniquely reduced. Decomposing them by dyadic arithmetic height `M` gives shell separation `delta_M>>M^(-2)`, while the `VIS-307` Wang shell energy is summable after the classical Montgomery--Vaughan mean-value bound. The resulting cutoff-free estimate is

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + x L^3 + x^3 L^3/V`,

so at `H asymp x ell` it is `o(H^2)` whenever

`V >> x L^3/ell^2`,

with `L=log(3x)` and `ell=log log(3x)`.

The polynomial finite-window gap has therefore disappeared. The unresolved transfer problem is now logarithmic rather than a dense-spectrum or support-cutoff obstruction.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can the cutoff-free shell estimate of `VIS-313` be sharpened from the sufficient horizon

`V >> x log^3 x/(log log x)^2`

to the natural local scale

`V asymp H asymp x log log x`,

or can one exhibit a concrete exceptional-height mechanism showing that a logarithmic loss is genuinely necessary?

The live issue is no longer generic coefficient sensitivity, a global minimum gap, a hard support tail, or dense-spectrum nearest-neighbor failure. It is the remaining logarithmic cost in the scale-local shell energy/mean-value recombination versus genuine deterministic exceptional-height coherence.

## Why it may matter

The sequence `VIS-301`--`VIS-313` has removed a long chain of nonstructural barriers: localization leakage, generic coefficient majorants, ambient spacing, support-sensitive absolute spacing, density-matched signed controls, exact support, same-base phase coherence, product-Haar versus the actual vertical flow, global-gap compression, hard-tail optimization, and finally pointwise isolation of the full dense spectrum.

`VIS-313` is qualitatively different from the preceding hard-cutoff estimates: it is already cutoff-free and loses no polynomial power of `x` relative to the natural scale. A further improvement can therefore focus on logarithmic shell energy, cancellation between shells, or the actual finite-window phase kernel rather than repairing another artificial polynomial horizon.

Failure is equally informative if it isolates an explicit exceptional family carrying enough coefficient mass to force an `H`-scale remainder despite the small Bohr energy and the new shellwise average bound.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, start from the cutoff-free decomposition of `VIS-313`. A next useful result must do one of two things:

- reduce the `log^3 x` shell-energy/large-sieve loss enough that the sufficient finite-window scale approaches `V asymp x log log x`, by a sharper shell moment, cancellation between adjacent height shells, a direct finite-window kernel estimate, or another aggregate-density argument that keeps the full support; or
- identify explicit starting heights and a quantitatively sufficient family of ratio interactions whose deterministic phases produce an `H`-scale remainder near `H asymp x log log x`, surviving the taper, the `VIS-309` small Bohr energy, and the `VIS-313` shellwise mean-square control.

A result that only reintroduces a hard support cutoff, a global or pointwise nearest-neighbor spacing, or another polynomial sufficient horizon is no longer informative unless it exposes a genuinely new obstruction not covered by `VIS-310`--`VIS-313`.

## Evidence boundary

`VIS-304` is an upper bound, not proof that `x log log x` is attained. `VIS-305`--`VIS-308` are increasingly faithful negative controls. `VIS-309` is exact for the long-time first and second moments of the deterministic remainder but remains an iterated fixed-`x,H` statement.

`VIS-310` and `VIS-311` are hard-cutoff proof-method bounds; `VIS-312` is a proof-method obstruction to taking their nearest-neighbor representation cutoff-free. `VIS-313` removes that polynomial transfer barrier only in **mean square over the starting height**. It does not prove pointwise cancellation at every `T`, does not justify a joint moving-`x(T)` limit, and does not prove that its remaining logarithmic loss is intrinsic.

No stronger RH criterion, new prime-gap theorem, or pointwise Wang asymptotic at `H asymp x log log x` is established.

## Research disposition

Outcome so far: **the moving upper-source branch has crossed from polynomial finite-window transfer loss to a cutoff-free near-linear mean-square horizon**. The remaining problem is logarithmic: sharpen the shellwise aggregate-density estimate toward the natural window, or find a genuine exceptional-height coherence mechanism that explains why this cannot be done.

The clue remains accepted and live. Another hard-cutoff or nearest-neighbor refinement is now superseded by `VIS-313`; the next contribution should address the logarithmic gap or a concrete exceptional-height obstruction.