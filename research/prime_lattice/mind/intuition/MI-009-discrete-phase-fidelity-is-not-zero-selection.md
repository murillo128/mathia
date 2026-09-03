# MI-009 — Discrete arithmetic can compress analytic phase injectivity to a finite fingerprint without selecting the zero divisor

**Evidence level:** proved for the standard Grosswald--Schnitzer deformation class in PL-125--PL-133

## Core intuition

Prime Lattice now has an unusually clean separation between **arithmetic identifiability** and **zero localization**. Grosswald--Schnitzer deformations can share the zeta zero divisor while changing the underlying generator sequence. The relative critical-line reflection phase remembers those generators, but how much data is needed depends decisively on whether the generator coordinates are continuous or arithmetically discrete.

This demonstrates that recovering rational-prime input can be a strong theorem and still be logically independent of RH.

## Strongest justified principle

PL-130 shows that for real Grosswald--Schnitzer generators every finite family of natural critical-line phase jets and samples has exact local aliases: finitely many far-tail coordinates can compensate a change in a prescribed low generator. Smooth finite-dimensional phase data are therefore non-identifying in the continuous control class.

PL-131 gives the opposite infinite-data boundary. Equality of the reflection cocycle on any accumulating critical-line set forces equality of the whole deformation: analytic continuation, exponential-type control, Hadamard rigidity, and normalization remove the zero-free gauge.

PL-132 then shows that integrality changes the information complexity. The integer control space is a compact product of finite sets; distinct low-prefix cylinders have disjoint compact phase-arc images, hence a positive separation. Uniform equicontinuity compresses that separation to finitely many phase samples. For every fixed prime cutoff, **some finite phase fingerprint identifies the entire integer prefix uniformly over arbitrary integer tails**.

PL-133 and the earlier self-duality controls keep the logical boundary clear: reflection-axis structure and a shared zero divisor do not become a zero-selection theorem merely because the arithmetic generator is identifiable.

## Evidence synthesis and boundaries

The finite integer fingerprint is non-effective: sample complexity, optimal heights, and separation margins are not quantitatively controlled as the cutoff grows. It does not give one finite vector that recovers the infinite prime sequence.

More importantly, every member of the Grosswald--Schnitzer class already shares the relevant zeta zeros. Phase fidelity therefore answers “which arithmetic source produced this analytic quotient?” rather than “why are the common zeros on the critical line?”

## Status / novelty

The deformation theorem, compactness, identity theorem, and Hadamard factorization are classical inputs. The synthesis is the finite/accumulating and real/integer information hierarchy and its separation from zero selection.

## Falsification criterion

Produce an exact finite real-control phase fingerprint that defeats the compensating-tail theorem, or show that the integer compactness separation can collapse for a fixed prefix. For RH relevance, derive an additional positive/unitary theorem on the common zero-sensitive representation; source identifiability alone is not enough.

## Lean-formalizable core

- Local finite-data noninjectivity in a continuous product.
- Accumulating-set analytic injectivity.
- Compact finite-prefix separation and finite sampling.
- Logical independence of source identification from a shared zero divisor.
