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
  - research/visual_exploration/findings/VIS-065-hybrid-contrast-single-factor-residual-coordinate.md
---

# Can prime-by-prime zeta approximants be organized as a meaningful recursive geometry?

## Observation
The Euler product gives `zeta` a literal multiplicative hierarchy indexed by primes in its domain of convergence, while finite prime products and smoothed prime sums can still be formed as finite exploratory objects elsewhere. The original question was whether this hierarchy could be continued toward the critical strip in a mathematically justified way rather than through raw partial products whose apparent attractors or self-similarity may be truncation artifacts.

Prior-art audit supplies the correct baseline. Gonek, Hughes, and Keating prove an unconditional hybrid Euler–Hadamard representation in which a cutoff `X` mediates between a finite von-Mangoldt prime factor `P_X(s)` and an independently defined smoothed zero factor `Z_X(s)`, with explicit error. Gonek's later work further studies short finite-Euler-product approximation in the critical strip. Subsequent work on the splitting conjecture treats statistical separation of the prime and zero factors as an explicit prior-art problem. Thus neither the existence of the decomposition nor generic prime/zero statistical splitting is a new visual mechanism.

`VIS-010` gives the first exact control: if the complementary channel is defined merely as `R_X=zeta/P_X`, opposite scale increments are tautological. `VIS-064` closes the nearest escape by showing that for the independently defined hybrid factors the **sum** of prime and zero log-modulus scale increments is exactly the change in the explicit hybrid residual. Visually strong compensation is therefore expected whenever the hybrid approximation is accurate.

`VIS-065` now sharpens the remaining linear coordinate. If

`A_XY = log|P_Y/P_X|`, `B_XY = log|Z_Y/Z_X|`, `R_XY = A_XY+B_XY`,

then the proposed contrast `C_XY=A_XY-B_XY` satisfies

`C_XY=2A_XY-R_XY=R_XY-2B_XY`.

So `(R,C)` is only an invertible reparameterization of `(A,B)`. Once the residual is controlled, the contrast contains the same remaining pointwise scalar information as either one factor increment. In an accurate-hybrid regime it is quantitatively close to `2A` and `-2B`. The contrast can still be useful, but its default interpretation is therefore **within-factor scale geometry after residual accounting**, not a new prime/zero interaction.

## Research question
Does the justified hybrid Euler–Hadamard hierarchy contain a representation-stable scale statistic that carries arithmetic information beyond the product/residual identities and the established individual-factor baselines?

The nearest admissible question is now deliberately weaker: after freezing the hybrid construction, smoothing, scale pair, and statistic, does a within-factor prime or zero scale observable separate the arithmetic object from matched controls in a way that survives height windows and modest representation perturbations? If the aim is genuinely joint prime/zero geometry, can one predeclare a non-pointwise statistic whose behavior is not reconstructible from one factor together with the measured hybrid residual?

The target is no longer raw prime-by-prime recursion, prime/zero compensation, or a linear contrast interpreted as coupling. It is either a robust arithmetic statistic of one justified hybrid channel or a genuinely additional dependence structure that survives the exact reconstruction controls.

## Why it may matter
The hybrid formula connects the recursive/fractal intuition to a genuine arithmetic hierarchy without importing an invalid Euler product into the critical strip. Increasing `X` changes prime resolution and the complementary zero window in a mathematically controlled way, so the representation remains a natural place to search for multiscale structure.

The successive negative controls make the next positive result more meaningful. A signal that survives them would not merely rediscover quotient algebra, hybrid approximation accuracy, or a coordinate rotation of one factor. Conversely, failure of a frozen within-factor statistic against matched controls would close a concrete visual route without claiming that the whole hybrid representation is uninformative.

## Decisive test
Choose one admissible smoothing family and `X` regime from the hybrid Euler–Hadamard theorem. Construct `P_X`, `Z_X`, and the explicit residual `E_X=zeta/(P_X Z_X)` independently at the same evaluation points. Before inspecting confirmation windows, freeze one question and one statistic.

For the simplest first experiment, treat the modulus contrast only as a residual-corrected representation of a **single-factor** increment. Equivalently test

`A_XY = log|P_Y/P_X|`

against randomized-prime-phase and shuffled/log-band controls, while recording `R_XY=log|E_X/E_Y|`; using `C_XY=A_XY-B_XY` is acceptable only if the exact `C=2A-R` baseline is carried through. Require the same predeclared statistic to separate arithmetic data from controls across separated height windows, several admissible scale pairs, and modest smoothing perturbations without post-hoc window or statistic selection.

If the intended claim is genuinely about **joint** prime/zero organization, the test must go beyond this pointwise linear family. Predeclare a non-pointwise dependence statistic and first show that its null is not already determined by one factor plus the residual field. Compare it with the appropriate individual-factor, residual, and hybrid-splitting baselines before interpreting any cross-channel pattern.

Kill the current simple-contrast route as a coupling claim if its apparent signal is reproduced by `2A-R` or `R-2B`, by matched individual-factor controls, by deterministic zero-window entry/exit, or by the known residual accuracy. A later within-factor or genuinely joint experiment is a new coherent thread rather than rescue-by-statistic-search on the same confirmation data.

## Evidence boundary
The hybrid Euler–Hadamard representation and finite-Euler-product approximation theory are established prior art. `VIS-010` proves the exact quotient-transfer control, `VIS-064` proves the residual-controlled sum constraint for independently defined hybrid factors, and `VIS-065` proves that the simple modulus contrast is only the complementary linear coordinate to that sum and reduces to one factor once the residual is accounted for.

None of these findings establishes a useful within-factor scale law, a canonical hybrid invariant, statistical independence, a new prime/zero coupling, a fractal attractor, or an RH consequence. The next statistic remains exploratory until it is frozen before confirmation, survives the stated controls, and can be translated into a mathematical statement independent of the visualization.

## Research disposition
Accepted in further narrowed form. Use the hybrid Euler–Hadamard decomposition as the canonical critical-strip recursive baseline; reject quotient anticorrelation, residual-controlled compensation, and the raw linear contrast as independent coupling discoveries. The next admissible visual thread is a frozen within-factor statistic with explicit residual accounting, or a separately justified non-pointwise joint statistic that survives reconstruction from one factor plus the residual.