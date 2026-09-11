# MI-008 — Prime-Flute endpoint decay is essential orthogonality, now testable by local form witnesses

**Evidence level:** proved operator/form-theoretic boundary

## Core intuition

Energy normalization isolates the mixed operator `T=F_P Gamma F_H`. The canonical strength factors stay heavy on infinite-dimensional tails, so compactness cannot come from them. PF-287 identifies the remaining angle exactly with a product of heavy extension-range projections, and PF-288--PF-289 make noncompactness testable using separated local physical vectors.

The endpoint problem is therefore no longer merely “prove angular decay.” Its cheapest falsifier is a concrete **energy-normalized local low/high correlation**.

## Strongest justified claim

PF-279--PF-286 separate unprojected transmission, extension strength, and relative angle. Weak trace class has a two-sided threshold-counting formulation; the convenient `tau^-1` sufficient count is stronger than the necessary endpoint envelope, while neither physical strength factor has finite weak-Schatten population decay.

PF-287 shows that the thresholded angle is the cross-Gram of isometric unit-energy extension maps. Its singular-value counting function agrees exactly with that of the product of the orthogonal projections onto the two heavy extension ranges. It also expresses the angle directly through the normalized physical precision form, eliminating the polar-decomposition mismatch.

PF-288 proves a local noncompactness criterion. For pairwise separated low/high local families, divergent diagonal Rayleigh quotients and a uniform lower bound on `|k[u_j,v_j]|/sqrt(k[u_j]k[v_j])` force noncompactness at every fixed heavy threshold.

PF-289 observes that divergence is unnecessary for the basic endpoint falsifier. Uniform positive Rayleigh floors on both sides suffice after choosing small fixed thresholds. PF-216 already supplies a much stronger low floor and PF-227 supplies the required high floor. The only unresolved ingredient for this local obstruction is persistence of the normalized mixed correlation.

## Synthesis of evidence

The next calculation should be local before it is global. Pair the known PF-216 low-symmetric module vectors with the PF-227 physical-high singular witnesses and compute or bound their normalized mixed form correlation. A nonzero tail immediately kills compactness; systematic decay would remove the cheapest negative mechanism and justify returning to global heavy-range angle counts.

This ordering avoids proving a sophisticated weak-trace estimate before checking whether the physical ranges are already visibly non-orthogonal at module scale.

## Counterevidence / boundary cases

PF-289 does not assert that a persistently correlated high family exists. The PF-227 high witnesses may be selectable only in directions whose cross form with the PF-216 low vectors decays. Failure of this particular local witness does not prove compactness or weak trace class.

Likewise essential orthogonality at every fixed threshold is only compactness; the endpoint still needs the stronger quantitative distribution required for `S_(1,infinity)`.

## Epistemic status

**Exact endpoint narrowing plus local falsifier:** heavy strength does not decay away, the angle equals heavy-range projection geometry, and persistent normalized local correlation with fixed Rayleigh floors is enough to disprove compactness.

## Novelty/prior-art status

Projection-product geometry, form methods, compactness, and weak Schatten theory retain their finding-level prior-art status. This intuition synthesizes the physical consequence of the new form-native reductions.

## Falsification criterion

Invalidate the PF-287 singular-value equivalence or produce a family satisfying PF-289's hypotheses while the heavy angle remains compact. Strategically, prove the relevant PF-216/PF-227 normalized correlations vanish with a quantitative law strong enough to feed the endpoint count; that would cross the current local gate.