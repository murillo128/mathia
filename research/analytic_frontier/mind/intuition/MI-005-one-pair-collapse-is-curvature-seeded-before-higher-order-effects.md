# MI-005 — The scalar pair frontier is conditioning-to-geometry, not pair complexity

**Evidence level:** proved exact projection-tax reduction through ANF-088; uniform conversion to destination separability remains open

## Core intuition

The fixed central-notch scalar frontier has narrowed beyond generic nonseparability. ANF-081, ANF-083, and ANF-085 control every real finite multiset, a fixed complex-height strip independent of pair count, and all-height separable center-height occupations. ANF-086 adds a fixed destination-Hilbert tube around the separable cone. ANF-087 places every exact Montgomery--Taylor extremizer back inside that safe class.

ANF-088 now resolves the internal structure of near extremality: the excess is an exact sum of nonnegative Hilbert projection, multiplicity, tensor-signature, and spectral-tail taxes. The adapted dimensions never drop. A hypothetical fatal family must therefore exploit **quantitative ill-conditioning of finite exponential systems**, not hidden rank loss, multiplicity, height, or pair count.

## Strongest justified principle

ANF-086 shows that certificate failure requires both `d_sep(W)>=kappa_crit>0` and sufficiently small Montgomery--Taylor excess. ANF-088 decomposes that excess exactly and yields, as it tends to zero, convergence to the canonical `2/1/0` tensor signature, vanishing simple-real leakage, vanishing nonreal antisymmetric distance to the symmetric span, controlled multiplicity defects, and a small negative spectral tail.

Because the relevant exponential generators are always linearly independent, near equality cannot be explained by an exact dimension collapse. The only remaining continuous loophole is that the positive Gram determinants/Schur complements become arbitrarily small as cardinality or geometry degenerates. The decisive theorem is thus to convert ANF-088's projection-collapse regime into `d_sep(W)->0`, perhaps under successively weaker conditioning hypotheses, or to exhibit a growing ill-conditioned family for which that conversion fails.

## Counterevidence / boundary

ANF-088's canonical tensor is basis-adapted and is not itself asserted to come from an actual separable multiset. Small relative excess also need not imply the absolute multiplicity threshold when cardinality grows. Classical Ingham/Riesz-sequence theory supplies lower frame bounds only under additional frequency-separation hypotheses, while the unrestricted Mathia gate permits growing cardinality and collapsing gaps.

The result uses the strict interior positivity of the exact Montgomery--Taylor factor; a generic positive-semidefinite pair kernel need not share the same dimension/projection decomposition.

## Epistemic status

**Proved exact near-equality reduction; conditioning-to-destination geometry open.** No RH consequence is asserted.

## Falsification criterion

Construct a normalized sequence with Montgomery--Taylor excess tending to zero and `d_sep` bounded below, while satisfying the exact ANF-088 projection-tax identities. Such a family would isolate a genuine ill-conditioned scalar escape. Conversely, a uniform theorem converting those taxes to `d_sep->0` closes the remaining scalar pair frontier.