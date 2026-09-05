# Nyman–Beurling

## Research mandate

### Primary object

The line studies the Nyman–Beurling reformulation of the Riemann hypothesis as an approximation/closure problem in a Hilbert-space setting built from fractional-part functions, together with the Báez-Duarte discrete strengthening and closely equivalent Gram, distance, and dual-certificate formulations.

The central object is the distance from the RH target function to finite-dimensional spans of admissible Nyman–Beurling generators, including how that distance, the associated Gram geometry, and optimal coefficients behave as the span grows.

### Objective

Find constructive or quantitative structure behind the Nyman–Beurling closure criterion that is stronger than the bare equivalence to RH: effective approximation mechanisms, lower/upper bounds on best-approximation error, rigid structure of near-optimal approximants, or dual obstructions whose asymptotics would materially constrain RH.

A useful result should explain why the target can or cannot be approximated at a specific rate by the arithmetic generator family, rather than merely restating closure membership.

### Priority questions

- Do best finite-dimensional approximants exhibit a stable coefficient, Gram-spectrum, or support pattern that admits an exact asymptotic description?
- Can the Báez-Duarte discrete family be reorganized into an arithmetic basis or multiscale decomposition with controlled condition number and approximation error?
- Is there a dual certificate or separating functional whose norm converts failure of approximation into a quantitatively interpretable zero obstruction?
- Can known Möbius cancellation or zero-density information be translated into one-sided bounds for the Nyman–Beurling approximation distance without re-importing RH equivalently?
- Can a constructive approximation scheme expose a rate threshold equivalent to, weaker than, or stronger than familiar RH error terms?
- Which apparent numerical convergence phenomena survive matched non-arithmetic generator controls?

Start finite certificates from the Gram matrix together with its actual target pairings and target norm. Seek either explicit admissible approximants with norm-certified residuals or normed dual witnesses, then determine which estimates remain controlled as the arithmetic span grows.

### Scope and exclusions

This line owns the Nyman–Beurling/Báez-Duarte approximation problem and its intrinsic Hilbert-space geometry. It does not own generic functional-analysis reformulations, unrelated approximation criteria, or Möbius cancellation once the primary object becomes a summatory Möbius estimate rather than the approximation space.

Do not count the closure equivalence itself, a finite numerical least-squares fit, or a basis change that leaves the same approximation problem unchanged as progress.

### Line-specific falsification controls

Track conditioning and topology explicitly: a small residual in a finite truncation is not evidence for closure unless the approximation family and limiting norm are controlled. Test whether coefficient patterns are basis artifacts by applying equivalent generator changes and orthogonalization.

Compare target distances, not just Gram spectra: an isometric change of all generators can preserve their Gram matrix while changing their position relative to a fixed target. A matched synthetic family refutes a Gram-only target claim only when its target distance differs under the admitted hypotheses. When a proposed rate uses Möbius or zeta estimates, verify that the imported estimate is genuinely weaker than the desired RH conclusion rather than an equivalent criterion in disguise.

For spectral cutoffs, control the target mass discarded in small-eigenvalue directions under a declared coefficient geometry. Small unweighted pairing errors alone do not certify stable approximation in an ill-conditioned family. Keep a finite primal or dual certificate distinct from a uniform asymptotic rate and from closure of the full target space.

### Prior-art domains

- Nyman–Beurling criterion and Báez-Duarte strengthening;
- approximation in Hilbert spaces and Gram-matrix asymptotics;
- fractional-part functions and Mellin-transform formulations;
- Möbius summatory estimates where they enter the discrete criterion;
- Burnol, Báez-Duarte and related quantitative approximation work;
- duality/separation methods for closure and best approximation.

### Relationship to other lines

`arithmetic_fidelity` provides generic tools for asking whether a finite approximation or quotient preserves the witness needed by a limiting claim, but the arithmetic Nyman–Beurling geometry is owned here. `mobius_cancellation` may supply upstream signed estimates when they enter the Báez-Duarte coefficients, while remaining a distinct source-side program.

`visual_exploration` may inspect Gram spectra, optimal-coefficient geometry, or approximation residuals as clue generators, but durable claims about the Nyman–Beurling criterion belong to this line.