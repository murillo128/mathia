# MI-001 — Anchoring is necessary, but rank and same-shell noncommutativity are not arithmetic novelty

**Evidence level:** supported by exact and literature-backed negative results

## Core intuition

Breaking rotational symmetry by naming vertices or keeping an old/new block active is necessary to avoid the coarsest Prime-Circle quotients, but neither matrix rank nor same-level noncommutativity is a reliable proxy for new arithmetic information. The correction PC-047 is decisive here: the natural old/new cotangent carrier that had been interpreted as low-rank can in fact have maximal or full rank. What matters is not how many directions survive, but whether their values escape the classical character, divisor, and refinement data already forced by the shell geometry.

## Strongest justified principle

The current one-shell/canonical-refinement evidence separates **information capacity** from **information novelty**.

- PC-038 shows that pointed local spectral measures, vertex-deleted determinants, and Schur self-energies of a translation-invariant shell are derivative data of the full-shell characteristic polynomial.
- PC-039 shows that canonical inverse-square divisor refinement by Schur/Kron reduction is path independent, so staged elimination creates no refinement holonomy.
- PC-044--PC-045 reduce the first square-free primitive metric and oriented/chiral blocks to finite Dirichlet-character packages at fixed values `L(-1,chi)` and `L(0,chi)`.
- PC-047 corrects the former low-rank reading: the old/new cotangent carrier can be maximal rank, and even the metric/chiral commutator can be full rank. High rank therefore does not itself identify a new arithmetic channel.
- PC-048 then resolves the same carrier by exact birth order and multiplicative characters and finds explicit Gauss/Ramanujan factors multiplying fixed `L(0,eta)` data. PC-049 and the subsequent cotangent refinement calculations show that several natural fiber-average/pushforward operations are commuting, invertible, or affine copies of lower-level data rather than new dynamics.

The live variable is therefore **structured fine/coarse coupling before it is averaged into a character package or a commuting refinement map**, not rank by itself.

## What remains possible

A simultaneous multilevel operator can still carry information in correlations among old/new singular vectors, in noncommuting fine/coarse maps, in shell-dependent nonlinear response, or in a global uniformization that does not factor through fixed one-level character data. Those possibilities are not ruled out by PC-047--PC-049.

What no longer qualifies is an argument whose novelty claim rests on a large rank, on the mere failure of one polynomial relation, or on a canonical fiber average whose character multipliers are already explicit classical data.

## Status / novelty

The rank correction, character decompositions, path-independence identities, and commuting refinement formulas are persisted findings. The synthesis is a supported design constraint, not a theorem that every multilevel Prime-Circle construction classicalizes.

## Falsification criterion

Construct a canonical one-shell or commuting-refinement observable from the audited operators whose value is not determined by the corresponding shell spectrum, fixed Dirichlet-character data, and explicit refinement multipliers. Alternatively, exhibit a simultaneous multilevel invariant that survives after those classical packages are held fixed; that would confirm the stated boundary rather than falsify it.

## Lean-formalizable core

- Rank formulas for the old/new cotangent incidence block and the corrected same-level identities.
- Character decomposition of fixed-level old/new couplings.
- Associativity/path independence of Schur refinement.
- Commutation and invertibility of the canonical cotangent refinement pushforwards.
