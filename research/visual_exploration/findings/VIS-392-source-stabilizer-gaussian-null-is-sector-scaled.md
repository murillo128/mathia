# VIS-392 — source-stabilizer invariance closes the qutrit Gaussian null family

## Claim

Let `E=diag(E_1,E_2,E_3)` be a generic qutrit source with three distinct eigenvalues, and let

`V_+ = H_12 \oplus H_13 \oplus H_23`

be the real off-diagonal tangent/root space used in `VIS-388`, with each `H_ij` a real two-plane. Let `T_E` be the diagonal source-stabilizer torus acting on `V_+` by conjugation.

Then every Gaussian probability law on `V_+` that is invariant under the full action of `T_E` has zero mean and covariance of the form

`C = sigma_12^2 I_{H_12} \oplus sigma_13^2 I_{H_13} \oplus sigma_23^2 I_{H_23}`

with `sigma_ij^2 >= 0`. Conversely, every centered Gaussian with covariance of this form is `T_E`-invariant.

Hence the nondegenerate source-stabilizer-invariant Gaussian family is exactly the independent sector-scaled isotropic family analyzed in `VIS-391`. Cross-sector Gaussian covariance and within-sector ellipticity are not additional symmetry-compatible nuisance freedom: they break the full generic source-stabilizer symmetry.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL REPRESENTATION-THEORETIC CONSEQUENCE + NULL-CLOSURE + NO-NOVELTY-CLAIM`.

## 1. Faithful root-sector representation

The representation used here is **faithful** to the intrinsic generic-source symmetry rather than a visualization quotient. For a diagonal unitary

`D=diag(e^{i theta_1},e^{i theta_2},e^{i theta_3})`,

conjugation sends an off-diagonal matrix entry `X_ij` to

`e^{i(theta_i-theta_j)} X_ij`.

Thus, after identifying each real plane `H_ij` with one complex coordinate, the three positive root sectors carry the torus characters

`alpha_12(theta)=theta_1-theta_2`,

`alpha_13(theta)=theta_1-theta_3`,

`alpha_23(theta)=theta_2-theta_3`.

For a generic source these are the three distinct `A_2` root directions, distinct up to sign as real two-dimensional torus representations. This is the same intrinsic decomposition that diagonalizes `ad_E^2` in `VIS-388`; no coordinate-dependent sector split is being added here.

## 2. Torus invariance kills the mean

Let a Gaussian law on `V_+` have mean `m` and covariance `C`. Invariance under `T_E` requires

`D m D^{-1}=m`

for every `D in T_E`.

The off-diagonal space contains no zero-weight vector: every nonzero vector in `H_ij` is rotated by the character `alpha_ij` for some torus element. Therefore the only `T_E`-fixed vector in `V_+` is zero, and any invariant Gaussian must satisfy

`m=0`.

## 3. Covariance cannot mix distinct root sectors

For a centered Gaussian, invariance under an orthogonal representation `rho(D)` is equivalent to

`rho(D) C rho(D)^T = C`

for every `D in T_E`, or equivalently to `C` commuting with the torus action.

Complexifying the real representation separates the weights into

`{+alpha_12,-alpha_12,+alpha_13,-alpha_13,+alpha_23,-alpha_23}`.

An equivariant linear map can connect only equal weights. Because the three unordered root pairs `{+/- alpha_ij}` are distinct, an equivariant covariance has no block from one real root plane `H_ij` to a different plane `H_kl`. Therefore

`C = C_12 \oplus C_13 \oplus C_23`.

This rules out every cross-sector Gaussian covariance while preserving the full generic source stabilizer.

## 4. Each root plane is isotropic

Fix one sector `H_ij`. The torus character `alpha_ij` ranges over the full circle, so the restricted action contains all planar rotations on `H_ij`.

A real linear operator commuting with all rotations has the form `a I + b J`, where `J` is the quarter-turn complex structure. A covariance operator is symmetric, while `J` is skew-symmetric, so symmetry forces `b=0`. Positive semidefiniteness then gives

`C_ij = sigma_ij^2 I_{H_ij}`

with `sigma_ij^2 >= 0`.

Thus full source-stabilizer invariance forbids within-sector ellipticity as well as cross-sector covariance.

## 5. Gaussianity turns block orthogonality into independence

A centered multivariate Gaussian is completely determined by its covariance, and jointly Gaussian blocks with zero cross-covariance are independent. Therefore the invariant law factors as three independent isotropic Gaussian root-sector blocks,

`G_ij ~ N(0, sigma_ij^2 I_{H_ij})`.

For `sigma_ij>0`, the squared radii `||G_ij||^2` are independent exponentials up to their scale factors, exactly the input used in `VIS-391`. Allowing one or more `sigma_ij=0` gives degenerate boundary members of the same closed family rather than a new Gaussian null class.

Conversely, each scalar covariance block commutes with its sector rotation and the direct sum commutes with the full torus, so every such centered block-scaled Gaussian is indeed `T_E`-invariant.

## 6. Consequence for the residual-null hierarchy

`VIS-391` introduced independent sector scales as a natural anisotropic Gaussian extension of the isotropic Dirichlet null. The present result shows that this was not merely one convenient anisotropic choice: **it is the maximal Gaussian covariance freedom compatible with the full stabilizer of a generic qutrit source**.

Accordingly, a stronger null that still preserves the same source symmetry cannot be obtained simply by adding within-sector covariance ellipses or Gaussian cross-sector correlations. A genuinely stronger symmetry-compatible nuisance family must instead leave the Gaussian class, for example through non-Gaussian radial laws, invariant mixtures, or higher-order dependencies, or must incorporate nonlinear target/admissibility structure not represented by a Gaussian tangent law.

This closes one precise loophole in the interpretation of `VIS-391` without asserting that the resulting Gaussian family is the correct physical or arithmetic null.

## Why it matters

The qutrit residual program needs to distinguish structure forced by the source symmetry from structure introduced by an unnecessarily narrow null. Before this result, a residual mismatch against `VIS-391` could still be blamed on an unmodeled symmetry-preserving Gaussian covariance.

That explanation is now unavailable for a generic source. The three sector variances are exactly the Gaussian nuisance parameters allowed by the full source stabilizer. Any residual surviving optimization over them points either to non-Gaussian/higher-order structure, nonlinear admissibility constraints, or explicit symmetry breaking rather than to a missing Gaussian covariance degree of freedom.

## Prior-art boundary

The representation-theoretic ingredients are classical: a maximal torus acts on off-diagonal matrix directions through root characters; inequivalent weight spaces cannot mix under an equivariant operator; and on a real two-dimensional root plane a symmetric operator commuting with the full circle action is scalar. The Gaussian conclusion then follows from the standard fact that a Gaussian law is determined by mean and covariance and that zero cross-covariance implies block independence.

No novelty is claimed for these general facts or for their `SU(3)`/`A_2` specialization. The Mathia contribution here is only to apply them to the exact residual-null hierarchy of `VIS-388` and `VIS-391`, thereby identifying the boundary of the symmetry-compatible Gaussian nuisance family used by this research line.

## Limitations

The claim assumes a generic source with three distinct eigenvalues. Eigenvalue collisions enlarge the stabilizer and alter the irreducible decomposition, so the same three independent scale parameters need not describe that degenerate regime.

The closure is Gaussian only. Torus invariance permits much richer non-Gaussian distributions, including arbitrary invariant radial structure and symmetry-compatible higher-order dependencies. The result also says nothing by itself about the nonlinear rank-one target manifold, cubic/phase invariants, higher-order commutator geometry, or any arithmetic specificity relevant to the wider Riemann program.

## Sources

- `research/visual_exploration/findings/VIS-388-qutrit-rank-one-source-spectrum-has-cubic-shape.md` — intrinsic qutrit root-sector decomposition and source-gap spectrum.
- `research/visual_exploration/findings/VIS-391-sector-anisotropic-qutrit-residual-null.md` — exact independent sector-scaled Gaussian residual null whose symmetry boundary is classified here.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer, 2015, DOI `10.1007/978-3-319-13467-3` — standard background on maximal tori, roots/root spaces, and equivariant representation structure.
