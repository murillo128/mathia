---
id: CLUE-visual-exploration-zeta-prime-phase-recursive-geometry
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-010-hybrid-euler-hadamard-scale-transfer-tautology.md
---

# Can prime-by-prime zeta approximants be organized as a meaningful recursive geometry?

## Observation
The Euler product gives `zeta` a literal multiplicative hierarchy indexed by primes in its domain of convergence, while finite prime products and smoothed prime sums can still be formed as finite exploratory objects elsewhere. The original question was whether this hierarchy could be continued toward the critical strip in a mathematically justified way rather than through raw partial products whose apparent attractors or self-similarity may be truncation artifacts.

Prior-art audit supplies the correct baseline. Gonek, Hughes, and Keating prove an unconditional hybrid Euler–Hadamard representation in which a cutoff `X` mediates between a finite von-Mangoldt prime factor `P_X(s)` and an independently defined smoothed zero factor `Z_X(s)`, with explicit error. Gonek's later work further studies short finite-Euler-product approximation in the critical strip. Thus the existence of a legitimate prime/zero scale decomposition is classical rather than a new visual mechanism.

`VIS-010` adds an exact control: if the complementary channel is defined merely as `R_X = zeta/P_X`, then scale increments of `log|R_X|` are exactly the negatives of those of `log|P_X|`. Any apparent prime/residual transfer or anticorrelation produced that way is tautological.

## Research question
Using the hybrid Euler–Hadamard split, or another representation with equally explicit analytic justification, is there a **non-tautological cross-scale geometry** of the independently defined prime and zero factors?

Concretely, as `X` varies through an admissible intermediate regime, can one identify a representation-stable statistic of `P_X`, `Z_X`, their local phase/level geometry, or the hybrid approximation error that is not determined by the product relation and that changes systematically near zero configurations in a way absent from matched prime-phase or zero-surrogate controls?

The target is no longer raw prime-by-prime recursion. It is a quantitative invariant of an independently defined prime/zero scale split after exact complementarity has been quotiented out.

## Why it may matter
The hybrid formula connects the user's recursive/fractal intuition to a genuine arithmetic hierarchy without importing an invalid Euler product into the critical strip. It also gives a natural multiscale parameter: increasing `X` changes the prime resolution and the complementary zero window together.

A surviving statistic could make scale-by-scale prime/zero organization visible in a form that can be attacked analytically. A clean failure would be equally useful by showing that visually compelling recursive transfer is either quotient algebra, smoothing choice, local-zero universality, or ordinary random-phase behavior.

## Decisive test
Choose the smoothing and `X` regime from the hybrid Euler–Hadamard theorem, construct `P_X` and `Z_X` independently, and track candidate quantities across several `X` values and separated height windows. Do not use `zeta/P_X` as evidence for prime/zero coupling unless the exact quotient-transfer baseline from `VIS-010` has first been removed.

Candidates may include scale-normalized contour or phase geometry of `Z_X`, prime-band phase increments of `P_X`, statistics of the independently evaluated hybrid error `zeta/(P_X Z_X)-1`, or cross-scale features that depend on how nearby zeros enter and leave the `1/log X` window. Compare against randomized prime phases, shuffled/log-band controls, and reflection-symmetric surrogate zero configurations with matched local density.

Keep the direction only if a statistic survives smoothing/grouping and scale changes, is not algebraically forced by `P_X Z_X approx zeta`, and separates arithmetic data from matched controls in a way that can be stated without the image. Kill it if the effect reduces to exact quotient complementarity, the theorem's deterministic windowing, or generic local zero statistics.

## Evidence boundary
The hybrid Euler–Hadamard representation and finite-Euler-product approximation theory are established prior art. `VIS-010` proves only the exact quotient-transfer control. No fractal attractor, new prime/zero invariant, scale-locking law, or RH consequence has been established. Any finite visual statistic remains exploratory until its dependence on the independently defined hybrid factors and its robustness to the stated controls are demonstrated.

## Research disposition
Accepted in prior-art-narrowed form. Use the hybrid Euler–Hadamard decomposition as the canonical critical-strip recursive baseline, reject raw quotient anticorrelation as tautological, and search only for cross-scale geometry of independently defined prime/zero factors or hybrid error that survives matched controls.