# MI-004 — Full refinement covariance rigidifies fixed boundary data to universal or multiplicative-Toeplitz structure

**Evidence level:** supported by exact/classical completion and refinement-covariance results through PC-174

## Core intuition

The compatible Prime-Circle completion preserves exact-order labels and rational characters, but full power refinement is extremely rigid on local and fixed boundary geometry. The rigidity now extends from coefficients and domains to **all fixed distributional multiplication coefficients and all continuous weak first-order forms**.

The fixed boundary category therefore splits into two classical outcomes. Strong/local/distributional objects collapse to universal scale modes, while the genuinely larger weak form-covariant class becomes multiplicative Toeplitz after the canonical `|D|^(1/2)` normalization. Exact covariance then forbids any nonzero compact/Schatten defect inside that class. A viable arithmetic mechanism must either derive source-specific structure in the remaining noncompact ratio-lattice sector or leave the fixed-form category altogether.

## Strongest justified principle

PC-055--PC-074 establish that the adelic/solenoidal completion retains rational labels while broad commuting calculi fail to produce the desired discrete RH-scale spectrum. PC-165 identifies the compatible radial action as ordinary logarithmic dilation with the classical `-1/2+it` unitary half-density.

PC-166--PC-168 classify the local coefficient layer: full power-refinement covariance forces regular metrics to flat log-cylinder form and finite-order local coefficients to homogeneous monomials, with inverse-square as the canonical second-order scalar singularity. PC-169--PC-171 then close the fixed-domain/Robin ladder: refinement-compatible inverse-square domains are universal scale-fixed choices or nonexistent, bounded boundary corrections vanish, and strongly covariant fixed self-adjoint first-order operators collapse to four universal parameters.

PC-172 treats finitely supported distributional multiplication forms and finds only the universal anchor derivative. PC-173 removes the support hypothesis completely. Every fixed distribution `u` satisfying first-order refinement covariance lies in

`span{|D| delta_1, delta'_1}`.

Reflection kills the odd `delta'` direction, while every nonzero Hermitian member of the two-dimensional family destroys semiboundedness of the canonical bulk-plus-boundary form. Infinite support therefore does not create a fixed prime-sensitive Robin coefficient.

PC-174 closes the natural weak-form compact escape. A continuous Hermitian first-order form on `H^(1/2)` becomes, after the intrinsic `|D|^(1/2)` normalization, a bounded operator `B` satisfying `C_n^* B C_n=B`. Its Fourier matrix depends only on the rational ratio of absolute frequencies and the two orientation signs: it is exactly a matrix-valued multiplicative Toeplitz operator on the Bohr/infinite-polydisc model. If such a normalized operator is compact, then it is zero. Hence exact weak refinement admits no nonzero finite-rank, Hilbert--Schmidt, trace-class, Schatten, or ordinary Fredholm-determinant arithmetic defect.

## What remains possible

The weak noncompact multiplicative-Toeplitz sector is not proved useless; what is missing is a **source-forced prime-provenance symbol, domain, or sign theorem** that is not already generic ratio-lattice data. Other live categories leave fixed-form covariance more decisively: shell- or level-dependent singular families, genuinely cross-level relations, general renormalized boundary relations mixing trace and normal derivative, nonlinear/noncommuting couplings, or radial--arithmetic interaction before scalar/local reduction.

Choosing a Toeplitz symbol, inverse-square extension phase, singular anchor coefficient, or moving domain after inspecting the desired arithmetic is additional structure. The source must force the data before the refinement classification is applied.

## Status / novelty

Solenoids, dilation representations, homogeneous operators, inverse-square extensions, Robin/DtN theory, distributions, multiplicative Toeplitz operators, and the Bohr lift are classical. The persisted synthesis is the completion boundary: **full refinement can generate the half-density and a large weak boundary algebra, but fixed covariant data are either universal or classical ratio-lattice structure, and the compact determinant subbranch is empty**.

## Falsification criterion

Produce a fixed covariant distribution outside the PC-173 two-dimensional classification, or a nonzero compact normalized weak-covariant form contradicting PC-174. A shell-dependent, cross-level, noncompact source-forced Toeplitz, renormalized-relation, or nonlinear construction would evade rather than falsify the boundary.

## Lean-formalizable core

- Radial/solenoidal product and half-density dilation.
- Homogeneity and inverse-square domain classifications.
- Arbitrary fixed covariant distribution classification.
- Weak form normalization to `C_n^*BC_n=B`.
- Multiplicative Toeplitz Fourier classification.
- Compact fixed-point vanishing under refinement isometries.
