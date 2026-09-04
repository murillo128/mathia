# MI-004 — Full refinement covariance rigidifies local coefficients, domains, and fixed boundary data to universal scale structure

**Evidence level:** supported by exact/classical completion and refinement-covariance results through PC-172

## Core intuition

The compatible Prime-Circle completion preserves exact-order labels and rational characters, but full power refinement is extremely rigid on local analytic geometry. The rigidity now extends beyond coefficients: canonical inverse-square domains, bounded nonlocal Robin repairs, strong unbounded fixed Robin operators, and even finitely supported distributional multiplication forms all collapse to universal scale structures before primitive-shell arithmetic can enter.

Thus preserving labels and obtaining a critical half-density or singular boundary object are not enough. A viable completion mechanism must derive **additional shell/root-dependent data in a category not already fixed by the naked refinement semigroup**.

## Strongest justified principle

PC-055--PC-074 establish that the adelic/solenoidal completion retains rational labels while broad commuting calculi fail to produce the desired discrete RH-scale spectrum. PC-165 identifies the compatible radial action as ordinary logarithmic dilation with the classical `-1/2+it` unitary half-density.

PC-166--PC-168 classify the local coefficient layer. Full power-refinement covariance forces regular metrics to flat log-cylinder form and every finite-order local differential coefficient to a homogeneous monomial. At second order the only scalar singularity is inverse-square type.

PC-169 closes the canonical radial domain escape. Refinement-invariant self-adjoint inverse-square domains are only the classical scale-fixed choices in the weak/critical regimes, unique when essentially self-adjoint, and nonexistent in the supercritical regime once the independent refinements `2` and `3` are both required. The familiar limit-cycle phase cannot be intrinsic to the complete power semigroup.

PC-170 closes the bounded boundary escape: exact second-order covariance forces every bounded, compact, or finite-rank Robin correction to vanish. The first nonzero covariant boundary scale is unbounded first order; in the rotation/reflection-symmetric class it is the classical Dirichlet-to-Neumann operator `c|D|`.

PC-171 closes the strongest fixed unbounded operator continuation. Under strong covariance `A C_n=n C_n A`, self-adjointness, and the common trigonometric core, the whole operator is determined by four real coefficients multiplying `|D|`, `D`, `|D|R`, and `iDR`; there is no mode- or level-dependent arithmetic slot.

PC-172 closes the most direct point-supported distributional escape left outside those operator theorems. A finitely supported distributional multiplication form with exact first-order covariance satisfies `(T_n)_*u=n u` for every `n>=2`, which forces

`u=c delta'_1`.

Finite atomic root weights therefore vanish. The sole formal survivor is universal fixed-anchor geometry, is odd under conjugation/reflection, and is not a semibounded perturbation of the canonical second-order bulk form. Allowing finite-order point singularities does not recover primitive-root provenance.

## What remains possible

A surviving boundary/completion mechanism must leave at least one classified hypothesis for a source-forced reason: weaker form covariance with primitive-direction coefficients derived from old/new root incidence, shell- or level-dependent singular families, infinite-support transfer-operator data, general renormalized boundary relations mixing trace and normal derivative, genuinely cross-level relations, nonlinear/noncommuting structure, or radial--arithmetic coupling before scalar/local reduction.

Choosing an inverse-square extension phase, bounded root matrix, first-order coefficient block, finite atomic point weight, or fixed `delta'` singularity after inspecting the arithmetic is not such a derivation.

## Status / novelty

Solenoids, dilation representations, homogeneous operators, inverse-square extensions, Robin/DtN theory, distributions, and Fourier block multipliers are classical. The persisted synthesis is the completion boundary: **full refinement covariance can generate the half-density and universal singular/first-order boundary structure while remaining blind to primitive-shell provenance**.

## Falsification criterion

Produce a source-forced local coefficient, refinement-invariant radial domain, bounded boundary correction, strongly covariant fixed self-adjoint Robin operator, or finitely supported covariant multiplication distribution outside the PC-168--PC-172 classifications under their exact hypotheses. A weaker, infinite-support, shell-dependent, renormalized-relation, or cross-level construction would evade rather than falsify them.

## Lean-formalizable core

- Radial/solenoidal product and half-density dilation.
- Homogeneity classification of local coefficients.
- Refinement-compatible inverse-square domain classification.
- Bounded Robin vanishing and four-parameter strong unbounded Robin classification.
- Finite-support push-forward eigen-distribution classification `u=c delta'_1`.
- Reflection and semiboundedness obstructions for the `delta'` survivor.
