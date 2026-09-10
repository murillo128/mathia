# MI-012 — Fixed finite prime-transfer geometry closes even before complete Gram scalarization

**Evidence level:** exact packet/refinement/path-defect, finite nonlinear CRT, and shared-upper rectangular cross-Gram reductions through PC-249

## Core intuition

Escaping scalarity by adding coordinates, noncommuting refinements, path labels, complete transfer packets, arbitrary nonlinear readouts, or even pairwise rectangular common-row coupling does not create a new arithmetic variable while the lower conductor family is fixed and finite. The current constructions repeatedly factor through finite packet/shift structure and ultimately through classical lower-level residue data.

The surviving variable must therefore grow with scale or retain genuinely higher-order relational information before the finite residue or pairwise Gram contractions are taken.

## Strongest justified principle

PC-224--PC-245 classicalize the main fixed-conductor enrichments into matrix, shift, Cuntz/Bost--Connes, weighted-path, and affine polyphase structures. PC-246--PC-248 then prove that complete centered transfer Gram packets at fixed lower primes depend on the upper prime through finite signed residue data, and that any fixed synchronized nonlinear readout factors through one finite CRT group and hence a finite Dirichlet-character expansion.

PC-249 tests the explicit possibility that this loss was caused only by taking each packet's Gram separately. For fixed `p<r<q`, the rectangular packets `K_{p,q}` and `K_{r,q}` share the full upper `q`-row space. Nevertheless, once `q>pr-p-r`, their mixed block satisfies exactly `K_{p,q}^* K_{r,q}=q K_{p,r}^T`. Thus pairwise relative orientation in the common upper space eventually contains no new `q`-dependent arithmetic beyond a scalar and fixed lower packet. For every finite lower-prime family all off-diagonal blocks freeze in this way.

## Program consequence

Stop treating fixed finite pairwise packet geometry as an escape. A new candidate should let the information state itself grow: moving lower conductors, several independent upper-prime variables, higher-order tensors/intersections before pairwise contraction, source-forced composite masks, or an infinite-dimensional joint limit. Then test whether the new object distinguishes sources that agree on every fixed finite CRT/character packet.

The burden is not merely to increase dimension, but to identify a relation whose asymptotic information cannot be reconstructed from a growing collection of ordinary finite character channels.

## Counterevidence / boundary

PC-249 classifies only pairwise cross-Grams with fixed lower primes beyond the Frobenius threshold. It does not classify the full rectangular tensors, simultaneous dependence on several upper primes, lower primes growing with `q`, higher-order multilinear contractions, or source-defined composite masks. A growing character family can itself carry substantial information, so classicality of each finite stage is not a proof that every growing limit is useless.

## Epistemic status

**Exact fixed-finite closure strengthened through the first shared-row rectangular test: complete packet readouts and pairwise common-upper cross-Grams reduce to finite classical lower-level data; any surviving arithmetic channel must be genuinely growing or preserve higher-order pre-contraction relations.**

## Falsification criterion

Exhibit fixed lower primes and arbitrarily large upper primes beyond the Frobenius threshold for which the PC-249 mixed cross-Gram identity fails, or construct a fixed finite packet functional whose value distinguishes upper-prime information outside the CRT/character data already classified.
