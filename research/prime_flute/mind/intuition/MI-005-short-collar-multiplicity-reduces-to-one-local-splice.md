# MI-005 — Short-collar assembly is quantitatively Sobolev, not generically `C^1`

**Evidence level:** exact geometric accounting and exact counterexample through PF-186, plus uniform qualitative Sobolev rigidity through PF-187

## Core intuition

Above the trace endpoint, short-collar multiplicity, annular flux, and the normalized Killing kernel are no longer the main obstruction. But PF-186 shows that the remaining nonlinear gate cannot be phrased as a generic `C^1` chart-entry theorem: exact symplectic maps can have vanishing metric strain and displacement while carrying order-one microscopic rotations in their derivative.

PF-187 identifies the correct regularity scale. Once a canonical collar germ is boundary-normalized on the fixed marked annulus, vanishing strain forces uniform qualitative `W^{1,r}` convergence to the marked identity for every `r>1`. The missing theorem is therefore quantitative and constructive: obtain an energy-linear Sobolev rigidity/boundary-normalization estimate and an exact-symplectic localization with the same cost, or derive stronger canonical structure that genuinely forces the `C^1` chart used by PF-185.

## Strongest justified principle

PF-183 makes the infinitely many true short collars harmless once one uniform local splice estimate is charged to the already summable body energy. PF-184 proves zero annular flux, and PF-185 proves uniform marked Korn coercivity plus an energy-local exact-area cutoff inside a fixed `C^1` generating chart.

PF-186 rules out deriving that chart hypothesis from the generic energy/topological data. Reflection-equivariant Hamiltonian microtwists can have metric deviation tending to zero even in `L^infinity`, zero flux, boundary identity, and `C^0` convergence, while `DH=-I` on shrinking disks. Metric strain does not select a pointwise derivative branch.

PF-187 shows that this flexibility disappears qualitatively in finite Sobolev norm. Riemannian Reshetnyak rigidity, compactness of the normalized metric family through `L=0`, and the ordered reflection marking imply that boundary-preserving maps with vanishing strain and collar mismatch converge to the identity in `W^{1,r}`. The half-turn is the only residual reflection-compatible isometry and the marking removes it. What is not supplied is the linear modulus needed for collar-by-collar summation or the exact-symplectic cutoff itself.

## What remains possible

The low-regularity route is now precise: boundary-normalize the actual canonical PF germ with controlled energy, prove a uniform estimate of `W^{1,r}` distance to the marked identity that is linear enough for PF-183, and construct an exact-area localization with comparable cost. Existing qualitative rigidity says this is not blocked by hidden Sobolev microtwists, but it does not prove the quantitative estimate.

The alternative is source-specific `C^1` entry derived from the explicit PF-179--PF-184 construction rather than from strain. The trace endpoint `r=1` remains separate, and even a completed `S_r`, `r>1`, comparison would still need a marked spectral observable that separates the prime flute from its shift clone.

## Status / novelty

The collar geometry, flux calculation, Korn estimate, Hamiltonian microtwist, and compactness reduction are exact line evidence; Riemannian Reshetnyak rigidity is classical prior art. The durable synthesis is the regularity boundary: **the post-multiplicity splice problem is quantitatively Sobolev; generic `C^1` rigidity is false, while qualitative marked `W^{1,r}` rigidity is true.**

## Falsification criterion

Produce boundary-normalized marked collar maps with strain and collar mismatch tending to zero but staying a fixed positive `W^{1,r}` distance from the identity, invalidate PF-187's isometry selection, or prove that no energy-linear exact-symplectic localization can exist even for the actual canonical germ. Otherwise the remaining gate is quantitative Sobolev localization or genuinely canonical `C^1` control, not generic chart entry.
