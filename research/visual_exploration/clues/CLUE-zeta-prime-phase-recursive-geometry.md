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
  - research/visual_exploration/findings/VIS-066-hybrid-joint-field-factor-residual-shear.md
---

# Can prime-by-prime zeta approximants be organized as a meaningful recursive geometry?

## Observation
The Euler product gives `zeta` a literal multiplicative hierarchy indexed by primes in its domain of convergence, while finite prime products and smoothed prime sums can still be formed as finite exploratory objects elsewhere. The original question was whether this hierarchy could be continued toward the critical strip in a mathematically justified way rather than through raw partial products whose apparent attractors or self-similarity may be truncation artifacts.

Prior-art audit supplies the correct baseline. Gonek, Hughes, and Keating prove an unconditional hybrid Euler–Hadamard representation in which a cutoff `X` mediates between a finite von-Mangoldt prime factor `P_X(s)` and an independently defined smoothed zero factor `Z_X(s)`, with explicit error. Gonek's later work further studies short finite-Euler-product approximation in the critical strip. Subsequent work on the splitting conjecture treats statistical separation of the prime and zero factors as an explicit prior-art problem. Thus neither the existence of the decomposition nor generic prime/zero statistical splitting is a new visual mechanism.

`VIS-010` gives the first exact control: if the complementary channel is defined merely as `R_X=zeta/P_X`, opposite scale increments are tautological. `VIS-064` closes the nearest escape by showing that for the independently defined hybrid factors the **sum** of prime and zero log-modulus scale increments is exactly the change in the explicit hybrid residual. Visually strong compensation is therefore expected whenever the hybrid approximation is accurate.

`VIS-065` sharpens the remaining linear coordinate. If

`A_XY = log|P_Y/P_X|`, `B_XY = log|Z_Y/Z_X|`, `R_XY = A_XY+B_XY`,

then the proposed contrast `C_XY=A_XY-B_XY` satisfies

`C_XY=2A_XY-R_XY=R_XY-2B_XY`.

So `(R,C)` is only an invertible reparameterization of `(A,B)`. Once the residual is controlled, the contrast contains the same remaining pointwise scalar information as either one factor increment.

`VIS-066` closes the apparent non-pointwise escape as well. Because `B=R-A` holds at every sampled height/scale index, the **entire** prime/zero increment field is an invertible shear of one factor plus the residual field. Any deterministic nonlinear, lagged, multiscale, topological, or other joint statistic `F(A,B)` can be rewritten exactly as `F(A,R-A)`. Such statistics may still detect structure, but their information belongs to the factor/residual pair rather than to an additional prime/zero degree of freedom.

## Research question
Does the justified hybrid Euler–Hadamard hierarchy contain a representation-stable **within-factor** scale statistic, or a factor/residual dependence statistic with an explicitly calibrated joint null, that carries arithmetic information beyond the product/residual identities and established individual-factor baselines?

The nearest admissible experiment is deliberately one-channel first: after freezing the hybrid construction, smoothing, scale pair, height windows, and statistic, does a prime-factor or zero-factor scale observable separate the arithmetic object from matched controls in a way that survives modest representation perturbations? A factor/residual joint statistic is also admissible if its null is defined on the joint `(factor,residual)` law and the interpretation is kept at that level.

The target is no longer raw prime-by-prime recursion, prime/zero compensation, a linear contrast interpreted as coupling, or a nonlinear recombination of the same two factor fields presented as a new interaction channel.

## Why it may matter
The hybrid formula connects the recursive/fractal intuition to a genuine arithmetic hierarchy without importing an invalid Euler product into the critical strip. Increasing `X` changes prime resolution and the complementary zero window in a mathematically controlled way, so the representation remains a natural place to search for multiscale structure.

The successive negative controls make the next positive result more meaningful. A signal that survives them would not merely rediscover quotient algebra, hybrid approximation accuracy, a coordinate rotation, or nonlinear post-processing of an exactly reconstructible channel. Conversely, failure of a frozen within-factor statistic against matched controls would close a concrete visual route without claiming that the whole hybrid representation is uninformative.

## Decisive test
Choose one admissible smoothing family and `X` regime from the hybrid Euler–Hadamard theorem. Construct `P_X`, `Z_X`, and the explicit residual `E_X=zeta/(P_X Z_X)` independently at the same evaluation points. Before inspecting confirmation windows, freeze one question and one statistic.

For the simplest first experiment, test the within-prime increment

`A_XY = log|P_Y/P_X|`

against randomized-prime-phase and shuffled/log-band controls while recording `R_XY=log|E_X/E_Y|`. Require the same predeclared statistic to separate arithmetic data from controls across separated height windows, several admissible scale pairs, and modest smoothing perturbations without post-hoc window or statistic selection. An equivalent zero-factor test is legitimate with its own matched controls.

If a proposed statistic uses both `A` and `B`, first substitute `B=R-A` everywhere. Treat the result as a factor/residual statistic, not as evidence for an additional prime/zero information channel. If its interpretation depends on dependence between factor and residual, calibrate a realizable joint null for `(A,R)` rather than comparing only marginal factor and residual laws.

Kill the within-factor route if the frozen statistic is reproduced by matched controls, deterministic window entry/exit, smoothing artifacts, or the known hybrid approximation baseline. Kill any claimed extra prime/zero coupling if it is only a deterministic functional of the reconstructible `(A,B,R)` fields with no additional independently defined structure.

## Evidence boundary
The hybrid Euler–Hadamard representation and finite-Euler-product approximation theory are established prior art. `VIS-010` proves the exact quotient-transfer control, `VIS-064` proves the residual-controlled sum constraint for independently defined hybrid factors, `VIS-065` proves that the simple modulus contrast reduces to one factor once the residual is accounted for, and `VIS-066` proves the corresponding field-level reconstruction for arbitrary deterministic post-processing.

None of these findings establishes a useful within-factor scale law, an unexpected factor/residual joint law, a canonical hybrid invariant, statistical independence, a fractal attractor, or an RH consequence. The next statistic remains exploratory until it is frozen before confirmation, survives the stated controls, and can be translated into a mathematical statement independent of the visualization.

## Research disposition
Accepted in further narrowed form. Use the hybrid Euler–Hadamard decomposition as the canonical critical-strip recursive baseline; reject quotient anticorrelation, residual-controlled compensation, the raw linear contrast, and arbitrary deterministic non-pointwise recombinations of the same factor fields as independent prime/zero coupling discoveries. The next admissible visual thread is a frozen within-factor statistic with explicit residual accounting, or an explicitly framed factor/residual dependence test with a calibrated joint null.