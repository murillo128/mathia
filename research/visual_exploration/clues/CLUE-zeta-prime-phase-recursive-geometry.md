---
id: CLUE-visual-exploration-zeta-prime-phase-recursive-geometry
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-010-hybrid-euler-hadamard-scale-transfer-tautology.md
  - research/visual_exploration/findings/VIS-064-hybrid-independent-scale-transfer-error-bound.md
---

# Can prime-by-prime zeta approximants be organized as a meaningful recursive geometry?

## Observation
The Euler product gives `zeta` a literal multiplicative hierarchy indexed by primes in its domain of convergence, while finite prime products and smoothed prime sums can still be formed as finite exploratory objects elsewhere. The original question was whether this hierarchy could be continued toward the critical strip in a mathematically justified way rather than through raw partial products whose apparent attractors or self-similarity may be truncation artifacts.

Prior-art audit supplies the correct baseline. Gonek, Hughes, and Keating prove an unconditional hybrid Euler–Hadamard representation in which a cutoff `X` mediates between a finite von-Mangoldt prime factor `P_X(s)` and an independently defined smoothed zero factor `Z_X(s)`, with explicit error. Gonek's later work further studies short finite-Euler-product approximation in the critical strip. Thus the existence of a legitimate prime/zero scale decomposition is classical rather than a new visual mechanism.

`VIS-010` adds an exact control: if the complementary channel is defined merely as `R_X = zeta/P_X`, then scale increments of `log|R_X|` are exactly the negatives of those of `log|P_X|`. Any apparent prime/residual transfer or anticorrelation produced that way is tautological.

`VIS-064` closes the nearest escape from that objection. For the independently defined hybrid factors, the **sum** of the prime and zero log-modulus scale increments is exactly the change in the explicit hybrid residual, with an analogous phase statement modulo `2 pi`. Therefore visually strong prime/zero compensation remains expected background whenever the hybrid product is accurate; moving from an artificial quotient residual to the genuine hybrid zero factor does not by itself make transfer anticorrelation informative.

The remaining linear search direction is consequently a contrast rather than a sum. If

`A_XY = log|P_Y/P_X|` and `B_XY = log|Z_Y/Z_X|`,

then `VIS-064` controls `A_XY+B_XY` through the hybrid residual. A natural candidate coordinate is the orthogonal contrast `A_XY-B_XY`, or its phase analogue, provided it is frozen before confirmation and shown not to be a smoothing/window artifact. This coordinate is only a candidate observable; no arithmetic significance is established by defining it.

## Research question
Using the hybrid Euler–Hadamard split, or another representation with equally explicit analytic justification, is there a **non-tautological cross-scale geometry** in the degrees of freedom left after the residual-controlled product direction has been removed?

Concretely, as `X` varies through an admissible intermediate regime, can a predeclared contrast or within-factor statistic of `P_X` and `Z_X` remain stable across smoothing and scale, respond systematically to zero configurations, and separate the arithmetic construction from matched prime-phase and zero-surrogate controls?

The target is no longer raw prime-by-prime recursion or prime/zero compensation. It is a quantitative invariant of an independently defined prime/zero scale split living outside the product-direction constraint identified by `VIS-064`.

## Why it may matter
The hybrid formula connects the user's recursive/fractal intuition to a genuine arithmetic hierarchy without importing an invalid Euler product into the critical strip. It also gives a natural multiscale parameter: increasing `X` changes the prime resolution and the complementary zero window together.

`VIS-064` makes the next test sharper. Instead of rewarding a visually dramatic anticorrelation that the hybrid approximation already predicts, the experiment can explicitly quotient the constrained direction and ask whether any residual contrast has reproducible arithmetic organization. A clean failure would close a large class of scale-transfer pictures without closing within-factor or hybrid-error geometry more broadly.

## Decisive test
Choose one admissible smoothing family and an `X` regime from the hybrid Euler–Hadamard theorem. Construct `P_X` and `Z_X` independently and evaluate the hybrid residual `E_X=zeta/(P_X Z_X)` at the same points. Before inspecting confirmation windows, freeze one statistic that is not determined by the product-direction sum. The simplest first candidate is a normalized modulus contrast based on

`C_XY = [log|P_Y|-log|P_X|] - [log|Z_Y|-log|Z_X|]`,

with a phase contrast treated intrinsically on the circle if used. Do not count smallness of the corresponding **sum** as evidence; `VIS-064` already explains that through `E_X/E_Y`.

Test the frozen contrast across separated height windows, several admissible scale pairs, and modest smoothing perturbations. Compare against randomized prime phases, shuffled/log-band prime controls, and reflection-symmetric surrogate zero configurations with matched local density. Keep the direction only if the same predeclared statistic separates the arithmetic construction from these controls without relying on post-hoc scale/window selection and without collapsing to the hybrid residual, deterministic zero-window entry/exit, or a generic local-zero statistic.

If the simple contrast fails, that failure should be recorded before opening a different representation family. A later experiment may instead test within-factor geometry or a hybrid-error feature, but it should be treated as a new coherent thread rather than as rescue-by-statistic-search inside the same confirmation dataset.

## Evidence boundary
The hybrid Euler–Hadamard representation and finite-Euler-product approximation theory are established prior art. `VIS-010` proves the exact quotient-transfer control, and `VIS-064` proves the residual-controlled sum constraint for independently defined hybrid factors. Neither finding establishes that the proposed contrast is informative, canonical, stable under smoothing, or arithmetically specific.

No fractal attractor, new prime/zero invariant, scale-locking law, or RH consequence has been established. The contrast above is a predeclared experimental coordinate motivated by the surviving degree of freedom after the known product-direction control; it remains exploratory until it survives the stated controls and can be translated into a mathematical statement independent of the visualization.

## Research disposition
Accepted in further narrowed form. Use the hybrid Euler–Hadamard decomposition as the canonical critical-strip recursive baseline; reject both exact quotient anticorrelation and residual-controlled prime/zero compensation as discoveries. The next admissible test is a frozen statistic outside that constrained product direction, with the modulus contrast above as the simplest first candidate and matched controls required before any interpretation.