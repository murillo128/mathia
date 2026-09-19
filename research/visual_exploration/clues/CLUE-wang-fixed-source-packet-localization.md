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

in the iterated Bohr-time sense. The one-parameter prime-phase relation `p^(-iT)` therefore does not generically restore the obstruction. Any surviving `H`-scale effect must be **exceptional in height**, arise from a quantitative finite-window failure when `x` moves with `T`, or come from another error channel.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can one upgrade the Bohr-average cancellation of `VIS-309` to a quantitative finite-window or pointwise estimate strong enough when `x=x(T)`, or instead exhibit a concrete sparse resonance mechanism whose exceptional heights sustain an `H`-scale remainder near `H asymp x log log x`?

A generic cross-prime dependence model is no longer enough. The live issue is quantitative localization of exceptional coherence in the actual one-parameter prime flow.

## Why it may matter

The sequence `VIS-301`--`VIS-309` has removed a series of apparently structural barriers: localization leakage, generic coefficient majorants, ambient spacing, support-sensitive absolute spacing, density-matched signed controls, exact prime-power support, same-base multiplicative harmonics, and now the distinction between product-Haar phases and the actual vertical flow at the level of long-time first and second moments.

This leaves a sharper pointwise question. If a uniform finite-window estimate rules out the exceptional set strongly enough for moving `x(T)`, Wang's pointwise range can move beyond the present `x log log x` ceiling. If not, a genuine obstruction must identify a sparse resonant geometry that is invisible to the Bohr mean but survives the complete localization/gamma budget.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, start from

`R_(x,H)(T)=sum_(q!=r) a_q a_r K_H(q,r) exp(-iT log(q/r))`.

The next useful result must do one of two things:

- prove a quantitative mean-square/large-deviation estimate on finite height windows, with constants uniform enough in the ratio frequencies and the moving parameter `x=x(T)`, so that `R_(x,H)(T)=o(H)` in the required pointwise regime; or
- identify an explicit family of near-resonant rational-ratio frequencies and heights for which the phase sum is coherently `H`-scale, then show that this survives Wang's taper and all previously isolated errors.

A result that only re-proves infinite-time Kronecker/Haar equidistribution, support geometry, same-base harmonic coherence, or the absolute Hilbert majorant is already covered by `VIS-304`--`VIS-309`.

## Evidence boundary

`VIS-304` is an upper bound, not proof that `x log log x` is attained. `VIS-305`--`VIS-308` are increasingly faithful negative controls. `VIS-309` is exact for the Bohr-time first and second moments of the actual deterministic remainder, but its density statement is **iterated**: fix `x,H`, take the long-time limit, then let `x` grow.

It does not control a joint limit with `x=x(T)`, does not rule out sparse exceptional heights, and does not prove pointwise cancellation. No stronger RH criterion or new prime-gap theorem is established.

## Research disposition

Outcome so far: **the moving upper-source branch has narrowed from generic cross-prime phase alignment to exceptional-height coherence or quantitative finite-window failure of the prime Kronecker flow**.

The clue remains accepted and live. The next contribution should address that quantitative exceptional-set boundary rather than introduce another generic phase ensemble.