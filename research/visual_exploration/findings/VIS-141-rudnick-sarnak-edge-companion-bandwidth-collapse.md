# VIS-141 — Rudnick–Sarnak support forces companion bandwidth to collapse near the Montgomery edge

## Claim

Consider two translation-invariant pair statistics whose relative-frequency Fourier supports are compact sets `A,B subset R`. For the disjoint-pair covariance term, the associated four-level product test has Fourier support on permutations of

`(q,-q,r,-r)`, with `q in A` and `r in B`.

Rudnick–Sarnak's unconditional zeta `n`-level theorem applies under the strict support condition

`sum_j |xi_j| < 2`.

On the pair-pair plane this becomes

`|q|+|r| < 1`.

Therefore a tensor-product pair test with supports `A` and `B` can lie wholly inside the Rudnick–Sarnak region only if

`a+b < 1`, where `a=sup_(q in A)|q|` and `b=sup_(r in B)|r|`.

This gives two immediate operational consequences.

1. For the covariance or variance of two copies of the **same** pair statistic, `A=B`, admissibility requires `a<1/2`. Hence no same-statistic covariance whose pair-frequency support reaches the Montgomery edge `|q|=1` can be obtained by simply trimming that statistic while remaining in the classical Rudnick–Sarnak support region.
2. If one factor is retained within distance `epsilon` of the edge in the sense `a=1-epsilon`, then every independent companion pair-frequency band must satisfy `b<epsilon`. Thus for any family with `a_L -> 1`, the admissible companion bandwidth necessarily satisfies `b_L -> 0`. If the first support actually touches `|q|=1`, even `r=0` lies on the forbidden boundary and no nonempty tensor-product companion support is strictly admissible.

So the restricted-support theorem does not merely say that **edge-edge covariance** is outside its range. It imposes an exact bandwidth tradeoff: any Rudnick–Sarnak-safe redesign that keeps one factor asymptotically at the Montgomery edge becomes an **edge–low-frequency** statistic whose second factor collapses toward DC. That is a different observable, and its arithmetic relevance must be established independently.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BOUNDED DESIGN OBSTRUCTION + NO-NOVELTY-CLAIM`.

The support inequality is an elementary pullback of the classical Rudnick–Sarnak theorem; no new `n`-level correlation theorem is claimed.

## 1. Pair-pair support geometry

For a translation-invariant pair statistic, the two Fourier coordinates occur with opposite frequencies. If the first pair kernel uses relative frequency `q` and the second uses `r`, the disjoint four-point product therefore contributes at

`(q,-q,r,-r)`

up to coordinate permutation. Permutation does not change the `l^1` Fourier mass, so

`|(q,-q,r,-r)|_1 = 2|q|+2|r|`.

Rudnick and Sarnak prove the zeta `n`-level asymptotic for test functions whose Fourier transform is supported in

`sum_j |xi_j| < 2`.

Restricting that condition to the pair-pair plane gives exactly

`2|q|+2|r| < 2`,

or

`|q|+|r| < 1`.

If the two pair kernels have ordinary tensor-product Fourier support `A x B`, containing the whole product requires

`sup_(q in A,r in B)(|q|+|r|) = a+b < 1`.

This statement is about the actual support of the product kernel, not the center of a visually localized packet. Small tails or a support that merely decays outside the diamond do not satisfy a compact-support theorem without an additional quantitative truncation argument.

## 2. Identical edge statistics cannot fit

Take `A=B`. Then the support budget becomes

`2a<1`,

hence

`a<1/2`.

The Montgomery transition of interest in the current visual thread is at relative frequency `|q|=1`. A pair statistic that retains that edge cannot therefore have its variance or same-statistic disjoint-window covariance placed inside Rudnick–Sarnak's classical support domain by a small local modification. To enter the theorem with two identical factors, its entire pair-frequency support must be pulled back below `1/2`, which removes the edge rather than resolving it.

This is stronger than saying that the exact point `(q,r)=(1,1)` is unavailable. The whole identical-factor support geometry is incompatible with the edge: the diagonal `q=r` intersects the admissible diamond only for `|q|<1/2`.

## 3. An asymmetric redesign pays with a collapsing companion

Suppose instead that the first factor is deliberately kept close to the positive or negative Montgomery edge, with

`a=1-epsilon`, `epsilon>0`.

Then the support budget forces

`b<epsilon`.

Thus a fixed-width companion band `b>=b_0>0` forces the edge factor to stay a fixed distance at least `b_0` away from `|q|=1` (and in practice farther away because the support inequality is strict). Conversely, if a sequence of edge probes has `a_L -> 1`, every Rudnick–Sarnak-admissible tensor-product companion must collapse to frequency zero.

This exposes the only simple restricted-support escape route: couple a near-edge observable to an increasingly low-frequency observable. But such a cross-statistic is not the variance of the edge observable and does not inherit the original arithmetic target automatically. A low-frequency factor may principally measure coarse counting, density, window mass, or another nuisance mode unless a separate derivation proves otherwise.

The strict boundary matters. A compact support that includes `q=1` is not admissible even with `r=0`, because `|q|+|r|=1` lies on the boundary rather than inside the theorem's open support region. A family that approaches the boundary from below also raises a separate uniformity question: the fixed-test Rudnick–Sarnak theorem cannot be silently promoted to an `L`-dependent family whose support margin tends to zero.

## 4. What this rules out — and what it does not

The obstruction applies to the natural covariance product of two independently specified pair kernels, whose four-level Fourier support is the Cartesian pair-pair support above. It rules out using the classical restricted-support theorem as a direct closure for the current **edge-edge** covariance by merely narrowing two copies of the same edge statistic.

It does not rule out every conceivable four-level observable. A deliberately non-factorized four-level test could have support concentrated on a smaller subset of the Rudnick–Sarnak diamond even when its coordinates are motivated by an edge construction. That would be a new statistic, not the covariance kernel of two independent edge pair observables, and it would need a separate derivation showing that it still measures the desired arithmetic residual.

Likewise, a genuinely wider-support unconditional `n`-level theorem, a direct cross-height covariance or mixing theorem for the frozen statistic, or a quantitative approximation that replaces the original edge covariance by an admissible test with error below the target scale would bypass this specific support obstruction. None is supplied here.

## 5. Prior-art and novelty audit

The external input is Zeév Rudnick and Peter Sarnak, **Zeros of principal L-functions and random matrix theory**, *Duke Mathematical Journal* 81:2 (1996), 269–322, DOI `10.1215/S0012-7094-96-08115-6`. Their theorem gives the restricted Fourier-support condition `sum_j |xi_j|<2/m`; for the Riemann zeta function `m=1`, this is the `l^1` budget used above. The same support boundary was already audited in `VIS-140`.

The inequalities `a+b<1`, `a<1/2` for identical factors, and `b<epsilon` when `a=1-epsilon` are elementary consequences of that classical support theorem on the pair-pair Fourier plane. They are recorded because they sharpen the Mathia design fork, not as a novelty claim in analytic number theory.

A bounded literature recheck found the Rudnick–Sarnak support statement directly and did not change the prior-art boundary recorded in `VIS-140`. This finding does not assert that no later theorem can access wider support; it only states what follows from the classical restricted-support result that is currently available to this route.

## 6. Research consequence

The accepted Montgomery-edge clue should no longer treat “redesign the statistic to fit the Rudnick–Sarnak support region” as a generic escape hatch. For the original variance/covariance question, the simple identical-factor version is closed: an admissible same-statistic pair observable is confined to `|q|<1/2`, away from the support edge.

An asymmetric **edge–low-frequency** route remains mathematically possible, but it creates a new proof obligation. Before it can substitute for the original edge-edge covariance, one must define the low-frequency companion, prove that its collapsing bandwidth retains a nontrivial source-specific arithmetic signal at the required scale, and control the same finite-height/window-transfer errors. If that arithmetic bridge cannot be established, the live routes return to genuinely wider-support four-level information or a direct covariance/mixing theorem for the original frozen edge statistic.

No untouched confirmation-zero evidence is used.