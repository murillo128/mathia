# MI-016 — Weil source identity is projectively recoverable, but positivity needs a cross-band arithmetic law

**Evidence level:** supported by exact finite/projective identifiability theorems

## Core intuition

Finite-dimensionality is not the decisive obstruction in Weil-form approaches, but neither is exact source recovery the missing positivity theorem. A fixed finite Galerkin band forgets most of the detailed prime-power event stream and admits exact positive sparse aliases. The complete tower of bands removes that ambiguity and recovers the source modulo the zero-frequency endpoint. Yet this recovery is generic Fourier uniqueness and does not distinguish the rational-prime source by sign.

The unresolved currency is therefore a **cross-band arithmetic compatibility law stronger than reconstruction** that forces positivity of the original completed localized Weil form.

## Strongest justified claim

PL-259--PL-269 establish the observability/aperture hierarchy. Every RH failure is finitely visible; the CvS and Suzuki constructions evaluate the same localized completed Weil form; individual event jets are template-universal; the ground energy is strictly decreasing; and

`RH <=> lambda_a -> 0`.

This gives an exact destination but no source-side sign selector.

PL-270 shows how much one finite band forgets. Groskin's source calculus factors the prime contribution through `2N+1` real coordinates. Positive Caratheodory--Tchakaloff compression then reproduces the same entire level-`N` matrix with at most `2N+1` positively reweighted prime-power atoms selected from the active support. Finite-band eigenvalues, inertia, determinants, and all other matrix invariants inherit the same alias.

PL-271 proves that this ambiguity is not coherent across all bands. If two finite signed source measures give the same source matrix for every `N`, their difference is a multiple of the zero-frequency atom `delta_0`. On any fixed support away from zero, sufficiently many bands recover all source masses exactly. Thus the full projective source tower is information-theoretically faithful.

## Synthesis of evidence

The source-positivity problem now has three distinct layers. **Finite observability** detects bad directions. **Projective identifiability** recovers the source that generated the finite matrices. **Arithmetic positivity** must explain why that recovered source, together with the archimedean/polar completion, keeps every finite-aperture ground energy positive.

This rules out two shortcuts at once. One fixed matrix cannot appeal to detailed event identity that it does not contain. Conversely, reconstructing the entire source from the tower is not enough, because generic finite measures enjoy the same uniqueness theorem. The useful next theorem must exploit a relation among bands/cutoffs that is special to the canonical von Mangoldt weights and sign-relevant before it becomes a restatement of Weil positivity.

## Counterevidence / boundary cases

PL-270 aliases may change the canonical von Mangoldt weights and depend on `(c,N)`; they are not alternate zeta sources. PL-271 is exact but nonquantitative: it gives no useful band threshold, conditioning, or stability as prime-power frequencies cluster. Quantitative instability could be a real obstruction even after algebraic identifiability.

The zero-frequency endpoint is genuinely invisible in the sine-source representation and must be handled by the completed formulation rather than wished away.

## Epistemic status

**Exact observability/identifiability boundary:** fixed bands are source-nonidentifying, the full tower is source-identifying modulo the null endpoint, and neither fact proves the missing sign. The live target is a source-specific cross-band positivity/rigidity law.

## Novelty/prior-art status

The finite source quotient, Tchakaloff compression, Fourier uniqueness, and localized Weil results retain their finding-level prior-art classifications. This intuition synthesizes their role.

## Falsification criterion

Construct a nonzero source perturbation away from `omega=0` that leaves every Groskin band unchanged, or show that one fixed-band sign argument genuinely uses canonical source information not determined by that band's quotient. Strategically, prove a cross-band law of the canonical source that forces finite-aperture Weil positivity without simply reconstructing the explicit formula; that would cross the current gate.
