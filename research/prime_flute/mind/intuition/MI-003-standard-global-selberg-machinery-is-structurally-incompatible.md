# MI-003 — Standard global Selberg machinery is structurally incompatible with the prime flute

**Evidence level:** proved

## Core intuition

The failure of global zeta/trace/transfer constructions is not a technical regularization issue concentrated at one singular end. It is structural: the prime flute has infinitely many cusps, systole zero, primitive lengths accumulating at zero and on positive compact intervals, and infinitely many bounded-symbolic-complexity hyperbolic orbits. Any credible global spectral object must therefore differ essentially from standard Selberg/Ruelle/Fredholm machinery.

## Strongest justified impossibility principle

The ordinary heat trace and standard zeta determinant diverge; the Selberg/Ruelle products have no ordinary initial half-plane; the orbital measure is not locally finite on positive length windows; even after removing the short-orbit sector, primitive lengths accumulate in a positive interval; uniformly expanding faithful codings are impossible because the systole is zero; and the natural countable branching coding already has a divergent fixed iterate trace.

These are independent obstructions assembled from PF-033, PF-035, PF-036, PF-069, PF-070 and PF-075. PF-039/PF-040/PF-073 show that pseudo-Laplacian, parity, and unitary-twist repairs do not restore an absolute determinant. PF-062 shows that, on finite tangents, standard pinching-renormalized Selberg zeta near `s=1` contributes no information beyond the already-known small spectrum.

## Boundary cases

This does not prove that no new renormalized dynamical object can exist. It rules out objects whose renormalization is merely a routine extension of Selberg, or whose periodic trace keeps the standard positive orbit weights. A new construction could survive if spatial decomposition is built in before periodic compression, or if the geometry forces a nonstandard subtraction.

## Status / novelty

The individual analytic implications are standard once the geometric pathologies are known. Their simultaneous occurrence in this deterministic prime-derived flute is the substantive synthesis.

## Falsification criterion

Produce a faithful geometrically canonical transfer operator for the full flute with nuclear/Fredholm trace and standard periodic weights, or a canonical absolute/relative determinant whose defining trace is finite without ad hoc subtraction.

## Most informative next move

Do not search for another Euler product. Search for operator-valued local/tangent data and only then ask whether a canonical collective law exists.

## Lean-formalizable core

- Infinite product necessary-condition lemmas from factors not tending to one.
- Infinite orbital mass from infinitely many lengths in a compact interval.
- Uniform expansion implies positive systole under faithful periodic coding.
