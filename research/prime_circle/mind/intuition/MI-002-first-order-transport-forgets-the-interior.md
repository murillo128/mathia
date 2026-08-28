# MI-002 — First-order transport repeatedly forgets the interior

**Evidence level:** proved

## Core intuition

Whenever the prime-circle data are converted into a one-dimensional first-order transport law whose composition is functorial, interior vertices become gauge/subdivision data and telescope. Prime-specific information therefore cannot be expected from a flat path transport alone; it must survive in genuinely nonlocal two-dimensional structure, curvature of a moduli problem, or interactions not reducible to concatenation.

## Strongest justified impossibility principle

Three natural realizations already exhibit the same exact mechanism. Projective moving-frame transport telescopes (`K_n=rho_{n+1}rho_n^{-1}`); exact Euclidean Helmholtz transfer satisfies `T_a(k)T_b(k)=T_{a+b}(k)`; the Schwarzian factor-introduction defect is a cocycle and has zero square curvature. Thus the sequence of intermediate prime gaps is erased whenever the observable factors only through composable first-order maps along a single path.

PC-013, PC-014 and PC-018 are mathematically different constructions but share the same algebraic cause: associativity/cocycle exactness converts a path product into endpoint data. PC-017 remains important precisely because a second variation of uniformization need not share this flatness.

## Evidence against overgeneralization

This does not rule out branched transport, two-dimensional holonomy, Hessians of global actions, or operators retaining multiple homotopy classes simultaneously. It also does not say cross-ratios are trivial; it says a deterministic path transport built from them is too compressive.

## Status / novelty

Exact as an impossibility principle for the three audited constructions. The broad heuristic beyond them is supported, not a universal theorem.

## Falsification criterion

Find a canonical first-order single-path transport derived solely from the prime-circle geometry whose monodromy depends on an interior refinement after endpoints are fixed, without adding an external gauge or branching choice.

## Lean-formalizable core

- Telescoping identity for `rho_{n+1} rho_n^{-1}` products.
- Semigroup identity for the exact Helmholtz transfer matrix.
- Cocycle identity implying zero factor-introduction curvature.
