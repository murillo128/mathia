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
  - research/visual_exploration/findings/VIS-067-independent-prime-phase-scale-covariance-gram-kernel.md
  - research/visual_exploration/findings/VIS-068-shared-prime-phase-third-order-harmonic-resonances.md
  - research/visual_exploration/findings/VIS-069-shared-prime-phase-all-order-connected-resonance-cumulants.md
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

`VIS-067` calibrates the simplest within-prime randomized control. Under one independent Steinhaus phase per prime, shared across the predeclared height/scale field, the covariance of any finite log-modulus prime-factor observables is exactly the Gram kernel of their deterministic prime-power coefficient vectors. Cross-scale ridges, blocks, anisotropy, and oscillatory height covariance can therefore survive prime-phase randomization purely because the same weighted prime powers are reused. The randomized control has a structured analytic second-order baseline; it is not featureless noise.

`VIS-068` closes the most immediate higher-order escape. For the same shared-phase null, the complete joint third cumulant is an exact sum of same-prime additive harmonic resonances `k+l=m`. Prime-power coherence therefore forces potentially nonzero skewness, bispectral bands, and three-coordinate scale interactions even under independent random prime phases.

`VIS-069` now gives the all-order finite analogue. After writing each real prime contribution as a two-sided Fourier series, every block moment is the exact sum over signed prime-local frequency tuples whose total frequency is zero, and ordinary partition-lattice Möbius inversion turns those moments into the connected joint cumulant. Therefore every finite-order cumulant tensor of the shared-prime-phase null is an exact deterministic resonance polynomial in the coefficient arrays. The fourth-order null is already non-Gaussian even with only first harmonics, so escalating to kurtosis, trispectra, or still higher finite cumulants is not an automatic escape from the randomized baseline.

## Research question
Does the justified hybrid Euler–Hadamard hierarchy contain a representation-stable **within-factor residual beyond the exact prime-phase null**, or a factor/residual dependence statistic with an explicitly calibrated joint null, that carries arithmetic information beyond the product/residual identities, deterministic coefficient-Gram covariance, connected finite-order prime-phase resonance cumulants, and established individual-factor baselines?

The nearest admissible experiment remains deliberately one-channel first: after freezing the hybrid construction, smoothing, scale pair, height windows, shared-versus-resampled phase convention, and statistic, does a prime-factor or zero-factor scale observable separate the arithmetic object from matched controls in a way that survives modest representation perturbations? A factor/residual joint statistic is also admissible if its null is defined on the joint `(factor,residual)` law and the interpretation is kept at that level.

The target is no longer raw prime-by-prime recursion, prime/zero compensation, a linear contrast interpreted as coupling, a nonlinear recombination of the same two factor fields presented as a new interaction channel, covariance forced by shared coefficient overlap, third-order structure forced by same-prime harmonic closure, or a higher finite cumulant treated as though the shared-prime-phase null had no corresponding baseline.

## Why it may matter
The hybrid formula connects the recursive/fractal intuition to a genuine arithmetic hierarchy without importing an invalid Euler product into the critical strip. Increasing `X` changes prime resolution and the complementary zero window in a mathematically controlled way, so the representation remains a natural place to search for multiscale structure.

The successive negative controls make the next positive result more meaningful. A signal that survives them would not merely rediscover quotient algebra, hybrid approximation accuracy, a coordinate rotation, nonlinear post-processing of an exactly reconstructible channel, or deterministic finite-order resonance geometry of the chosen prime-phase control. Conversely, failure of a frozen within-factor statistic against the exact null would close a concrete visual route without claiming that the whole hybrid representation is uninformative.

## Decisive test
Choose one admissible smoothing family and `X` regime from the hybrid Euler–Hadamard theorem. Construct `P_X`, `Z_X`, and the explicit residual `E_X=zeta/(P_X Z_X)` independently at the same evaluation points. Before inspecting confirmation windows, freeze one question and one statistic.

For the simplest first experiment, test the within-prime increment

`A_XY = log|P_Y/P_X|`

against a randomized-prime-phase null that uses one independent phase per prime and preserves its prime-power harmonics. State explicitly whether those phases are shared across the whole height/scale field or independently resampled by cell. For the shared-phase field, compute the exact `VIS-067` coefficient Gram kernel before examining arithmetic confirmation data. If the frozen witness uses any finite cumulant order `r>=3`, compute its exact connected-resonance baseline using `VIS-069`; `VIS-068` is the explicit third-order specialization. A finite-order cumulant witness must be defined relative to these exact baselines rather than to a featureless Gaussian/noise assumption. Shuffled/log-band controls may be added only with their own realizable preserved-constraint definitions.

Record `R_XY=log|E_X/E_Y|`. Require the same predeclared statistic to separate arithmetic data from controls across separated height windows, several admissible scale pairs, and modest smoothing perturbations without post-hoc window or statistic selection. For a finite-order cumulant/polyspectral witness, subtract or compare against the exact connected-resonance tensor before interpreting the residual. For a non-cumulant nonlinear or topological statistic, calibrate its realizable shared-phase null directly rather than assuming that `VIS-069` determines it. An equivalent zero-factor test is legitimate with its own matched controls.

If a proposed statistic uses both `A` and `B`, first substitute `B=R-A` everywhere. Treat the result as a factor/residual statistic, not as evidence for an additional prime/zero information channel. If its interpretation depends on dependence between factor and residual, calibrate a realizable joint null for `(A,R)` rather than comparing only marginal factor and residual laws.

Kill the within-factor route if the frozen statistic is reproduced by the exact finite-order resonance baseline plus matched controls, deterministic window entry/exit, smoothing artifacts, or the known hybrid approximation baseline. Kill any claimed extra prime/zero coupling if it is only a deterministic functional of the reconstructible `(A,B,R)` fields with no additional independently defined structure.

## Evidence boundary
The hybrid Euler–Hadamard representation and finite-Euler-product approximation theory are established prior art. `VIS-010` proves the exact quotient-transfer control, `VIS-064` proves the residual-controlled sum constraint for independently defined hybrid factors, `VIS-065` proves that the simple modulus contrast reduces to one factor once the residual is accounted for, `VIS-066` proves the corresponding field-level reconstruction for arbitrary deterministic post-processing, `VIS-067` proves the exact second-order covariance kernel of the shared Steinhaus prime-phase null, `VIS-068` proves its exact third-order additive-harmonic resonance tensor, and `VIS-069` proves the exact connected-resonance formula for every finite joint cumulant order.

None of these findings establishes a useful within-factor arithmetic residual, an unexpected factor/residual joint law, a canonical hybrid invariant, statistical independence, a fractal attractor, or an RH consequence. `VIS-069` also does not determine arbitrary non-cumulant nonlinear statistics. The next statistic remains exploratory until it is frozen before confirmation, survives the stated controls, and can be translated into a mathematical statement independent of the visualization.

## Research disposition
Accepted in further narrowed form. Use the hybrid Euler–Hadamard decomposition as the canonical critical-strip recursive baseline; reject quotient anticorrelation, residual-controlled compensation, the raw linear contrast, arbitrary deterministic non-pointwise recombinations of the same factor fields, and any finite-order cumulant geometry already forced by the exact shared-prime-phase connected-resonance calculus as independent discoveries. The next admissible visual thread is a frozen within-factor residual relative to that exact null, a non-cumulant statistic with its own realizable calibrated null, or an explicitly framed factor/residual dependence test with a calibrated joint law.