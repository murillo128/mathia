# MI-006 — Arithmetic can survive bulk spectral classicalization only in a mesoscopic organization that fixed windows still miss

**Evidence level:** supported by exact finite Hessian reductions, primorial asymptotics, and fixed-window controls

## Core intuition

A finite spectral model can have a universal bulk and even a universal top eigenpair while still retaining a macroscopically large arithmetic defect subspace. That survival is not enough by itself: scalar mass, trace, Wasserstein bulk discrepancy, and every fixed Fourier edge window can still collapse to classical totient/Artin/Murata/Nicolas data.

The surviving target is therefore not "some nonuniversal eigenvalues exist" but the **growing-scale organization of those defect modes** before fixed-window or first-moment compression erases their provenance.

## Strongest justified principle

PC-131--PC-134 close the finite Hessian algebra much further. Squarefree and nonsquarefree character coefficients reduce to Dirichlet--Bernoulli data, the resultant-normalized Hessian characteristic polynomial is integral, and arbitrary finite Hessian tensor networks collapse to confluent Cauchy algebra. Finite algebraic complexity does not open a new spectral field.

PC-135 gives the strongest coherent aggregation control: the all-divisor equal-weight Hessian aggregate is exactly the full regular-polygon inverse-square Laplacian with universal spectrum. PC-136 shows that the cross-shell-only primorial aggregate approaches the same universal bulk; its natural Wasserstein defect is governed by the squared primorial totient product. PC-137 identifies the resulting RH criterion exactly with Nicolas's classical criterion.

PC-138 adds an extreme-mode control: every even level has an exact universal top eigenpair. PC-140 shows that even the substantial primitive-shell trace classicalizes to an Artin constant times the same primorial totient factor, again reducing its RH-sensitive scalar criterion to Nicolas.

The important non-collapse is PC-139. The omitted within-shell defect contains a mesoscopic number of eigenvalues of macroscopic `N^2` scale, so bulk convergence does not imply operator-norm or high-rank disappearance. Yet PC-141 shows that any fixed-width Fourier edge window around the protected alternating mode asymptotically diagonalizes and classicalizes to a Murata-type product times the same Nicolas factor. Fixed local spectral zoom is still too small.

## What remains possible

A viable prime-circle spectral mechanism must therefore use a window or relational organization whose complexity grows with the level, or a non-Fourier localization that follows the defect subspace rather than a fixed protected mode. The observable must distinguish more than the total defect mass and more than any finite collection of edge eigenvalues.

Natural tests include whether a growing band retains nontrivial off-diagonal mixing after the universal Laplacian is subtracted, whether its joint spectral measure carries provenance not determined by the totient product, and whether matched cyclotomic controls reproduce that organization.

## Status / novelty

The finite Hessian identities, totient products, Artin/Murata constants, Nicolas criterion, and Fourier asymptotics are classical or persisted exact reductions. The synthesis is the scale separation: **bulk universality does not kill mesoscopic arithmetic, but fixed windows and scalar summaries can still classicalize it**.

## Falsification criterion

Show that the PC-139 macroscopic defect subspace is completely determined, at growing rank, by the same classical totient/Dirichlet data as PC-136--PC-141; or exhibit a fixed-dimensional spectral window whose invariant provably retains information not reducible to those controls.

## Lean-formalizable core

- Universal all-divisor Hessian aggregation.
- Exact universal top eigenpair.
- Trace/Wasserstein reduction to primorial totient factors.
- Lower bound on macroscopic defect-mode multiplicity.
- Fixed Fourier-window asymptotic diagonalization.