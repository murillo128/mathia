# MI-005 — Short-collar assembly is quantitatively Sobolev, with fixed-germ confinement as the remaining entry gate

**Evidence level:** exact geometric accounting and counterexample through PF-186, plus uniform qualitative Sobolev rigidity through PF-188

## Core intuition

Above the trace endpoint, short-collar multiplicity, annular flux, and the normalized Killing kernel are no longer the main obstruction. PF-186 shows that the remaining nonlinear gate cannot be phrased as a generic `C^1` chart-entry theorem: exact symplectic maps can have vanishing metric strain and displacement while carrying order-one microscopic rotations in their derivative.

PF-187 identifies the correct regularity scale after boundary normalization. PF-188 sharpens that conclusion: **boundary normalization is not intrinsically required for qualitative marked `W^{1,r}` rigidity**. On a fixed positive-side collar mapped into one fixed larger annular germ, vanishing strain and collar mismatch force convergence to the canonical inclusion for every `r>1`. The actual unresolved entry condition is fixed-germ confinement, not boundary-to-boundary normalization.

## Strongest justified principle

PF-183 makes the infinitely many true short collars harmless once one uniform local splice estimate is charged to the already summable body energy. PF-184 proves zero annular flux, and PF-185 proves uniform marked Korn coercivity plus an energy-local exact-area cutoff inside a fixed `C^1` generating chart.

PF-186 rules out deriving that chart hypothesis from generic energy/topological data. Reflection-equivariant Hamiltonian microtwists can have metric deviation tending to zero even in `L^infinity`, zero flux, boundary identity, and `C^0` convergence, while the derivative stays order-one away from the identity on shrinking disks. Metric strain does not select a pointwise derivative branch.

PF-187 shows that this flexibility disappears qualitatively in finite Sobolev norm for boundary-normalized maps. PF-188 proves that the same branch selection already holds for maps from a fixed inner annulus into a fixed larger annulus. Riemannian Reshetnyak rigidity gives an orientation-preserving isometric immersion in the limit, and the reflection marking plus the fixed positive-side target germ forces that immersion to be the canonical inclusion, uniformly through `L=0`.

The fixed-germ condition is load-bearing. At the cusp limit, if the image is allowed to run arbitrarily deeper toward `x=0`, higher-winding exact local isometries provide genuine escape branches. Thus qualitative rigidity has moved the boundary again: **normalization at the boundary is removable, but confinement to one controlled germ is not yet removable.**

## What remains possible

The low-regularity route is now precise: prove that the actual canonical PF relative germ stays inside one fixed larger collar with a cost controlled by PF-183's local body energy, strengthen qualitative `W^{1,r}` convergence to an energy-linear modulus, and construct an exact-area localization with comparable cost. No separate boundary-normalization theorem is required merely to select the Sobolev branch.

The alternative is source-specific `C^1` entry derived from the explicit PF-179--PF-184 construction rather than from strain. The trace endpoint `r=1` remains separate, and even a completed `S_r`, `r>1`, comparison still needs a marked spectral observable that separates the prime flute from its shift clone.

## Status / novelty

The collar geometry, flux calculation, Korn estimate, Hamiltonian microtwist, and fixed-germ classification are exact line evidence; Riemannian Reshetnyak rigidity is classical prior art. The durable synthesis is the regularity boundary: **the post-multiplicity splice problem is quantitatively Sobolev; generic `C^1` rigidity is false, qualitative marked `W^{1,r}` rigidity does not require boundary normalization, and fixed-germ confinement is the remaining geometric entry gate.**

## Falsification criterion

Produce fixed-germ reflection-marked collar maps with strain and collar mismatch tending to zero but staying a fixed positive `W^{1,r}` distance from the inclusion, invalidate PF-188's isometric-immersion classification, or prove that the actual canonical germ cannot be confined to any fixed larger collar even under the available source geometry. Otherwise the remaining gate is quantitative fixed-germ Sobolev localization or genuinely canonical `C^1` control.
