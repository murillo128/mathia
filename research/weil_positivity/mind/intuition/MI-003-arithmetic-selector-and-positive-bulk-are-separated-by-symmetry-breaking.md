# MI-003 — Positive assembly can have the right sign or logarithm while its exact finite arithmetic birth remains absent

**Evidence level:** supported by exact positive selectors and repeated/new-prime refinement theorems through WP-139

## Core intuition

Positivity does not by itself erase arithmetic. Finite pointed covers and related operators can carry exact `log n` or prime-power information. The obstruction is the **assembly and scalarization law**: natural positive responses can have the wrong dependence on refinement depth even when they are canonical, nonzero, or singular.

The repeated/new-prime full-chord geometry now displays a nearly complete first-response taxonomy. Coarse repeated-prime response is stationary; regular full-fiber traces are extensive; regular new-prime puncture responses are uniformly bounded; repeated-prime Green response grows logarithmically only as generic cover-degree harmonic growth; and the minimal singular new-prime puncture finite part is again bounded and prime-blind. None yields the exact finite Mangoldt birth required by the Weil formula.

## Strongest justified principle

WP-081--WP-106 establish that positive finite selectors exist but regular cover bulk/trace scalarizations classicalize, while exact `log n` sits at a singular endpoint requiring additional structure.

WP-134--WP-136 classify regular repeated-prime full-chord assembly. The canonical coarse compression is exactly stationary, the coarse sector reduces so Feshbach self-energy vanishes, and every fixed continuous nonnegative trace over the full fiber spectrum is either zero or `I m+o(m)` in deck multiplicity. Along prime powers these give zero or extensive depth response, not `log p` per birth.

WP-137 tests the repeated-prime singular escape. The positive Green trace has endpoint poles, and uniform deck sampling converts them into harmonic numbers. The residue-normalized response grows like `log m` and refinement `m->am` has asymptotic increment `log a` for every integer degree multiplier. At `d=2` the response is exactly `H_{m-1}`: it approaches the desired logarithm but is a generic cover law rather than an exact prime selector.

WP-138 supplies the regular new-prime control. The one-hole puncture defect is Loewner positive with uniformly bounded trace budget, so every fixed nondecreasing Lipschitz spectral response is `O_d(1)` as the new fiber degree grows. After critical half-weight normalization it misses `(log q)/sqrt(q)` by a factor tending to zero.

WP-139 closes the first singular new-prime loophole at the minimal conductor. For every odd `m`, prime or composite matched control,

`det' M_{2,m}/det' A_{2,m}^{hole}=(m-1)/(16m)`.

Thus the zero-shift log response splits into the universal nullity divergence `log(1/lambda)` plus the finite part

`-log 16 + log(1-1/m)`,

which is bounded, tends to `-log 16`, and is exactly prime-blind. The apparent logarithmic growth before normalization is only the scale dimension of the extra nonzero mode; intrinsic normalization removes it. Choosing `lambda` as a function of `m` would import a target-aware regularization rather than reveal a canonical birth coefficient.

## Evidence synthesis and boundaries

The message is not that singular or nonlinear positive observables are impossible. It is that the first regular and singular refinement responses are classified by generic cover geometry before rational-prime specificity enters.

A viable finite--archimedean construction must therefore insert the arithmetic selector before or inside a genuinely new singular/global assembly, or derive a source-forced nonlinear/depth-dependent response whose finite coefficients are exact and whose sign survives completion. Subtracting harmonic asymptotics, tuning a cutoff, or reading a universal nullity pole after seeing `log p` is not a sign theorem.

## Status / novelty

Positive graph Laplacians, cyclic fibers, Green residues, harmonic sums, spectral monotonicity, pseudodeterminants, matrix-tree identities, and log-determinants are classical. The persisted synthesis is the selector/assembly boundary: **getting the right sign, a logarithmic divergence, or even an asymptotic logarithmic increment is weaker than producing the exact finite Weil prime-power weight from source-forced geometry**.

## Falsification criterion

Produce within the covered canonical geometry a fixed regular repeated-prime response with nonzero depth-independent increment, a fixed regular new-prime response growing like `log q`, show that the repeated-prime Green response equals the exact finite Mangoldt increment, or contradict the WP-139 normalized pseudodeterminant ratio at `d=2`.

## Lean-formalizable core

- Repeated-prime coarse stationarity and reducing decomposition.
- Zero-versus-extensive regular trace law.
- Endpoint Green-pole to harmonic-sum calculation.
- Uniform puncture trace budget for monotone Lipschitz functional calculus.
- Exact minimal-conductor singular pseudodeterminant ratio and bounded finite part.
