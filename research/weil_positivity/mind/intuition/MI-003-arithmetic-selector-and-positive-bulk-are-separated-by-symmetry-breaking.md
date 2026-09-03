# MI-003 — Positive assembly can be stationary, extensive, bounded, or logarithmic while still missing exact Mangoldt birth

**Evidence level:** supported by exact positive selectors and repeated/new-prime refinement theorems through WP-138

## Core intuition

Positivity does not by itself erase arithmetic. Finite pointed covers and related operators can carry exact `log n` or prime-power information. The obstruction is the **assembly and scalarization law**: natural positive responses can have the wrong dependence on refinement depth even when they are canonical and genuinely nonzero.

The repeated/new-prime full-chord geometry now displays four distinct wrong-scale regimes. Coarse repeated-prime response is stationary; regular full-fiber repeated-prime traces are extensive; regular new-prime puncture responses are uniformly bounded; and the singular repeated-prime Green response grows logarithmically but only as generic cover-degree harmonic growth. None yields the exact finite depth-independent Mangoldt birth required by the Weil formula.

## Strongest justified principle

WP-081--WP-106 establish that positive finite selectors exist but regular cover bulk/trace scalarizations classicalize, while exact `log n` sits at a singular endpoint requiring additional structure.

WP-134--WP-136 classify regular repeated-prime full-chord assembly. The canonical coarse compression is exactly stationary, the coarse sector reduces so Feshbach self-energy vanishes, and every fixed continuous nonnegative trace over the full fiber spectrum is either zero or `I m+o(m)` in deck multiplicity. Along prime powers these give zero or extensive depth response, not `log p` per birth.

WP-137 tests the most canonical singular escape. The positive Green trace has conjugate simple endpoint poles. Uniform deck sampling converts those poles into harmonic numbers, so residue-normalized response grows like `log m` and refinement `m -> a m` has asymptotic increment `log a` for **every** integer degree multiplier. In the exact `d=2` case the response is `H_{m-1}`: the prime-power increment approaches `log 2` but is not the exact finite Mangoldt coefficient. The logarithm is cover-theoretic, not a prime selector.

WP-138 supplies the complementary new-prime control. The one-hole puncture defect is Loewner positive with uniformly bounded trace budget. Every fixed nondecreasing Lipschitz spectral response, including shifted positive log-determinants, therefore has `O_d(1)` total response as the new fiber degree `q` grows. After the critical `q^{-1/2}` normalization it misses the required `(log q)/sqrt(q)` coefficient by a factor tending to zero like `1/log q`. The singular zero-shift boundary is real but governed by universal kernel multiplicity.

## Evidence synthesis and boundaries

The message is not that singular or nonlinear positive observables are impossible. It is that the first singular logarithm and the first positive puncture response are both classified by generic cover geometry before rational-prime specificity enters.

A viable finite--archimedean construction must therefore insert the arithmetic selector before or inside the singular assembly, or derive a source-forced depth-dependent/nonlinear response whose finite coefficients are exact and whose sign survives the complete global completion. Subtracting harmonic asymptotics or choosing a degree-dependent regularizer after seeing `log p` is not a sign theorem.

## Status / novelty

Positive graph Laplacians, cyclic fibers, Green residues, harmonic sums, spectral monotonicity, and log-determinants are classical. The persisted synthesis is the selector/assembly boundary: **getting the right qualitative sign or even the right asymptotic logarithm is weaker than producing the exact finite Weil prime-power weight**.

## Falsification criterion

Produce within the covered canonical geometry a fixed regular repeated-prime response with nonzero depth-independent increment, a fixed regular new-prime response growing like `log q`, or show that the residue-normalized `d=2` Green response equals the exact finite Mangoldt increment rather than only approaching it.

## Lean-formalizable core

- Repeated-prime coarse stationarity and reducing decomposition.
- Zero-versus-extensive regular trace law.
- Endpoint Green-pole to harmonic-sum calculation.
- Uniform puncture trace budget for monotone Lipschitz functional calculus.
