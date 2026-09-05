# MI-014 — Source-canonical spectral fidelity is category-relative, and Fisher retention is score-projection geometry

**Evidence level:** supported through AF-141 by exact projection identities, gauge classification, covariance naturality, Fisher information geometry, and score-projection loss

## Core intuition

A spectral hierarchy is meaningful only relative to source geometry that survives the admitted reparameterization category. With no source metric, full generator gauge reduces fixed-target fidelity to projection geometry. A source metric can repair that gauge, but what information the metric retains depends on how the source supplies it: covariance gives a unique affine-natural second-order metric, while a source-natural smooth statistical family can supply a genuinely full-law Fisher metric.

Canonicity still does not imply fidelity through compression. Once a statistical source is observed through a parameter-independent channel, the surviving Fisher geometry is exactly the geometry of the conditional score. The lost part is an `L^2` projection defect.

## Strongest justified principle

AF-135--AF-138 give the metric boundary. Under arbitrary invertible changes of generator coordinates, raw positive Gram eigenvalue scales are not intrinsic; fixed-target information is projection/principal-angle geometry. With an independently source-specified positive metric `M`, the invariant object is the generalized pencil `(G,M)` and the corresponding generalized Picard measure.

AF-139 classifies the covariance-only case under full affine naturality. If the source supplies only a positive-definite covariance `C`, every natural coefficient metric is `c C^{-1}`. After normalization, the generalized spectrum is exactly the nonzero output-covariance spectrum of `A C A^*`, and equal-covariance controls show that this entire repair has a strict second-order ceiling.

AF-140 shows that the ceiling belongs to the input category, not to affine naturality itself. For a source-intrinsic smooth translation family, location Fisher information `J` has the correct metric transport law, satisfies `J>=C^{-1}` with equality exactly at the Gaussian boundary, and can distinguish equal-covariance laws. Arbitrary smoothing or an imposed parametric family does not qualify as source geometry.

AF-141 then separates metric canonicity from compression fidelity. For a parameter-independent Markov observation `X->Y`, the observed score is `E[S_X|Y]` and

`I_X-I_Y = E[Cov(S_X|Y)] >= 0`.

A tangent direction survives exactly when its score component is measurable from the retained observation. Along a Markov chain these Fisher defects add stage by stage.

## What remains possible

A concrete arithmetic spectral theorem must first derive the metric or statistical experiment from the source, independently of the desired target. If covariance is the only retained probabilistic structure, no higher-order discriminator can emerge downstream. If a full-law Fisher metric is used, the statistical family itself must be canonical and the arithmetic-relevant score directions must satisfy a quantitative non-escape theorem through the actual observation/compression.

For singular covariance, discrete sources, nondominated models, or nontranslation statistical categories, the corresponding source geometry must be derived separately rather than importing the smooth Fisher construction by arbitrary regularization.

## Status / novelty

Projection geometry, Mahalanobis distance, affine equivariance, PCA, Fisher information, Cramér--Rao inequalities, score conditioning, and Fisher monotonicity are classical. The persisted synthesis is the category ladder: **projection geometry without a metric; unique second-order Mahalanobis geometry from covariance; potentially full-law Fisher geometry from a source-natural statistical family; and score-projection loss under downstream compression**.

## Falsification criterion

Produce an intrinsic raw Gram spectral scale under the full admitted generator gauge without additional coefficient geometry; a covariance-only affine-natural metric not proportional to `C^{-1}`; a regular source-natural Fisher metric violating its transport or information-loss identities; or a compressed statistical direction whose score is not retained but whose Fisher information is unchanged.

## Lean-formalizable core

- Fixed-target projection/pseudoinverse identities and generalized-pencil invariance.
- Full-affine covariance metric uniqueness.
- `J>=C^{-1}` and the Gaussian equality condition in a finite-dimensional regular model.
- Conditional-score identity and positive Fisher projection defect.
