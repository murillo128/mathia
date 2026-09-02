# MI-005 — Canonical Hardy conductor limits classicalize into universal Hilbert/Carleman channels

**Evidence level:** supported by exact finite-trace reductions, trace-ideal classifications, and canonical conductor-limit calculations

## Core intuition

The Hardy interior/exterior split genuinely escapes finite cotangent endpoint closure, but the most canonical large-conductor limits now classicalize as well. Fixed-shell data are trace class with the wrong zero-density scale; prime-conductor strong and microlocal limits become universal Hilbert/Carleman operators; affine rescaling is unitary dilation plus a trace-class cocycle; Möbius birth extraction repeats radical blocks unitarily; and the one-new-prime corrector becomes infinitesimal in operator norm while retaining only a universal quadratic mass.

The remaining singular scalar escape is closed too: bounded scalar zooms give only zero-free Gaussian `det_2` limits, while divergent real scalar zooms destroy finite determinant normality instead of creating a new divisor.

## Strongest justified principle

PC-075 and PC-081 classify the essential finite-family layer as universal Hilbert channels plus compact remainders. PC-100--PC-107 close ordinary finite traces and fixed-shell Fredholm determinants inside cyclotomic/hyperlogarithmic and trace-class categories; in particular the reciprocal-zero summability and `o(R)` zero counting of a trace-class determinant are incompatible with Riemann's `T log T` density under an asymptotically linear normalization.

PC-108--PC-110 analyze the singular prime-conductor escape. All logarithmically divergent Hilbert--Schmidt mass concentrates in the lowest Hardy coordinate and converges strongly to the classical Hilbert matrix. Resolving the escaped residual on the conductor mesh produces the universal Carleman--Hilbert discretization defect, whose off-origin compact part is again trace class.

PC-111--PC-113 close the natural affine-scale, exact-order, and one-new-prime strong limits. Scale defects are unitary dilations of one universal object, pairwise scale differences are trace class, Möbius births repeat radical blocks unitarily, and the fixed-conductor arithmetic residual in the joint new-prime limit survives only by infinite-multiplicity reflection inflation.

PC-114--PC-119 then classify the escaping one-new-prime corrector much more sharply. After the canonical Hilbert--Schmidt normalization its operator norm tends to zero while its `S_2` mass tends to a positive universal constant; arbitrary conductor growth gives the same zero-free Gaussian `det_2` limit. Similarity, isometric unfolding, and uniformly bounded two-sided preconditioning cannot turn this infinitesimal corrector into a finite Fredholm divisor.

PC-120 closes the direct scalar singularity left outside that bounded-preconditioning theorem. For a real scalar factor `a_{p,q}`, every bounded convergent subsequence still has only a zero-free Gaussian determinant limit. If `|a_{p,q}|->infinity`, then for every fixed nonzero imaginary spectral point the absolute value of `det_2(I-z a_{p,q}X_{p,q})` diverges. A divergent scalar zoom therefore leaves the category of finite entire canonical determinant limits rather than revealing hidden Riemann zeros.

## What remains possible

A surviving Hardy route must act **before** the one-new-prime corrector becomes infinitesimal, or use a genuinely non-scalar unbounded/domain-changing transformation whose scale is forced by the Prime-Circle geometry. A jointly organized all-shell object, provenance-sensitive coupling, or nonlinear/singular operation remains logically possible only if it is not reducible to the bounded or scalar zooms already classified.

A positive mechanism must also supply an independent selector or sign theorem. Creating a new determinant by an arbitrary renormalization after the universal Hilbert/Carleman/Gaussian limits have formed is not enough.

## Status / novelty

Hilbert and Carleman operators, trace ideals, Fredholm determinants, dilation covariance, Möbius inversion, and regularized determinant products are classical. The persisted Prime-Circle contribution is the exact placement of the canonical Hardy remainder in those classes and the resulting localization of any surviving arithmetic information to a genuinely cross-level, pre-universalization sector.

## Falsification criterion

Produce a canonical conductor limit, bounded/nonbounded scalar zoom, or bounded preconditioning covered by PC-108--PC-120 whose finite nonzero spectral divisor depends on the prime level beyond the stated universal models. A positive advance should instead isolate a geometry-forced non-scalar singular operation or all-shell object outside those hypotheses.

## Lean-formalizable core

- Prime-conductor Hilbert-corner decomposition.
- Microlocal convergence to the Carleman--Hilbert defect.
- Trace-class classification of the off-origin defect.
- Dilation-cocycle and radical-unitary factorization.
- Vanishing operator norm with nonzero Hilbert--Schmidt mass.
- Imaginary-axis lower bound excluding finite `det_2` limits under divergent real scalar amplification.
