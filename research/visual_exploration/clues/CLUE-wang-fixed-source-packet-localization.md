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
  - research/visual_exploration/findings/VIS-315-prime-ratio-local-density-natural-window-criterion.md
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

`VIS-314` removes one of those logarithms without changing the representation. Retaining two-prime sparsity and applying the classical dimension-two Selberg upper-bound sieve gives

`E_M << M v_x(M)^4 log^2(4M)`,

and therefore

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + x L^2 + x^3 L^2/V`,

with sufficient scale

`V >> x L^2/ell^2`.

`VIS-315` now identifies the exact missing many-frequency input. For the ordinary-prime frequencies in a dyadic shell, let `kappa_M(V)` be the maximum number of prime-ratio frequencies in a Fourier cell of width `1/V`. A coloring plus the classical separated-frequency large sieve gives

`V^(-1) integral |F_M^pp(T)|^2 dT << kappa_M(V) E_M^pp`.

A nonempty frequency cluster is, up to absolute constants, exactly a thin determinant strip

`|qv-ur| << M^2/V`

around another represented prime ratio `u/v`. If uniformly

`kappa_M(V) << 1 + A M^2/(V log^2 M)`,

then the full cutoff-free remainder obeys

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + x L^2 + A x^3/V`
`    + x^(1/2)L^4 + x^(5/2)L^4/V`.

Thus at the natural local window `V asymp H asymp x ell`, an occupancy loss `A=o(ell^3)` is sufficient for `o(H^2)` mean-square cancellation. The unresolved logarithmic gap is therefore no longer merely “many-frequency organization”: it is a concrete local-density/energy problem for prime ratios, or else a genuine exceptional represented direction that violates the average-density scale.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can one prove a uniform local-density or sparse-energy estimate strong enough to control prime-ratio clusters at resolution `1/V` near

`V asymp H asymp x log log x`,

or can one exhibit represented slopes whose thin determinant strips contain enough weighted prime-ratio mass and deterministic phase coherence to force an `H`-scale exceptional contribution?

The useful target is now quantitative. An essentially average-density estimate

`kappa_M(V) << 1 + M^2/(V log^2 M)`

would suffice, and even a worst-cell excess factor `A=o((log log x)^3)` is still compatible with the natural mean-square window.

## Why it may matter

`VIS-301`--`VIS-315` have successively removed localization leakage, generic coefficient majorants, ambient spacing, support-sensitive absolute spacing, increasingly faithful random-phase controls, generic deterministic Bohr-time alignment, hard support truncation, global minimum-gap compression, dense-spectrum nearest-neighbor failure, one logarithm caused by discarding prime-pair sparsity, and finally the ambiguity about what the remaining large-sieve improvement must measure.

The present frontier separates two materially different possibilities. If prime-ratio frequencies have near-average local occupancy at Fourier resolution, the remaining `log^2 x` finite-window tariff is another proof-packaging loss. If they do not, the violating determinant strips identify explicit arithmetic directions where an exceptional-height mechanism could live and can be tested against the actual Wang coefficients rather than inferred from a worst gap.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, start from the prime-ratio local-density reduction of `VIS-315`. A next useful result must do one of three things:

- prove `kappa_M(V) << 1 + A M^2/(V log^2 M)` uniformly over the dyadic shells and represented directions with `A=o((log log x)^3)` at `V asymp x log log x`;
- replace the maximum-occupancy condition by a weighted/additive-energy large-sieve estimate that yields the same shell bound `M v_x(M)^4 log^2 M + o((log log x)^3) M^3 v_x(M)^4/V`; or
- identify a concrete family of represented slopes `u/v` for which the determinant strips `|qv-ur|<<M^2/V` violate that scale, then show that the corresponding Wang coefficients and deterministic phases produce a quantitatively sufficient exceptional contribution rather than a large but harmless frequency cluster.

A result that merely reapplies a hard support cutoff, a global/nearest frequency gap, or the same two-point fixed-shift upper sieve is no longer informative unless it changes this local-density/energy boundary.

## Evidence boundary

`VIS-304` remains only an upper bound for the actual pointwise remainder. `VIS-305`--`VIS-309` are controls or iterated long-time statements, not pointwise cancellation at every height. `VIS-310`--`VIS-314` are finite-window proof-method reductions and improvements.

`VIS-315` proves an exact local-density reduction and a conditional sufficient criterion. It does **not** prove the required uniform prime-ratio occupancy estimate. Nearby sparse-large-sieve and Beatty-prime literature does not, by the statements audited there, automatically provide the moving-slope two-prime strip bound required here.

No stronger RH criterion, new prime-distribution theorem, pointwise Wang asymptotic, or moving-`x(T)` theorem is established.

## Research disposition

Outcome so far: **the moving upper-source branch has progressed from a polynomial finite-window barrier to a concrete prime-ratio local-density criterion at the natural window**. The remaining mean-square problem is to control the worst Fourier-resolution cluster within an `o((log log x)^3)` factor of average density, obtain an equivalent weighted-energy bound, or turn a violating cluster into a genuine exceptional-height obstruction.

The clue remains accepted and live. Another minimum-gap estimate or another two-point shell-mass refinement is superseded by `VIS-315`; the next contribution should attack the thin determinant-strip/local-energy frontier or exhibit a concrete coherent exception.