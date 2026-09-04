# MI-003 — Fixed-time Xi memory is mesoscopic, and triple-discriminant overlap localizes exactly to a nonlinear bulk-alignment problem

**Evidence level:** supported through XF-031; finite-jet, collision, lattice-taper, and triple finite-gap identities are exact in their stated regimes

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. Source-valid super-mesoscopic buffers can make the far exterior negligible, so the principal obstruction is no longer lack of spatial room.

The active normalized-discriminant route has now crossed an important algebraic boundary. Positive overlap repairs collision walls, lattice-order localization loss is a small Cauchy commutator for a wide taper, and for three-root blocks the **full nonlinear finite-gap localization defect enters through discrete taper differences exactly**. What remains is not an unspecified boundary term but a precise sign/coercivity problem comparing two positive-conductance operators on the same reciprocal-gap field.

## Strongest justified principle

XF-006--XF-020 establish the mesoscopic carrier: finite collision jets are universal, fixed-time memory sits at `Theta(log^2 T)` gaps, the gap flow is a nonlinear positive-conductance diffusion, and source-valid buffers control the remote tail. XF-021--XF-025 then show why compact or fixed-range centered mean-removal schemes fail through collision spikes.

XF-026--XF-028 reopen the problem in a different category. Exchange-symmetric root observables remove the raw repulsion poles; the normalized block discriminant has exact square internal production and annihilates affine exterior fields; and overlapping blocks give every positively covered collapsing pair a dominant positive `8W/epsilon^2` contribution.

XF-029 proves the taper mechanism at arithmetic-lattice quadratic order. For overlapping triples, the weighted Cauchy form splits into nonnegative production plus a localization potential involving `La`; a smooth width-`M` taper pays only `O(1/M)`. Since the Xi fixed-time wavelength is `N(T)~log^2 T` while the available buffer contains `M(T)~R(T)log^2 T` gaps, the perturbative loss is lower order by `O(1/R(T))`.

XF-030 gives the exact nonlinear triple primitive. After translation and scaling, a triple shape is one-dimensional in `d=log(g_(j+1)/g_j)`; its normalized discriminant is strictly concave, and its full exterior coupling is an absolutely convergent signed cubic divided-difference field that interpolates exactly between lattice Hessian and collision production.

XF-031 completes the algebraic localization step. For a finitely supported taper, summation by parts gives an exact product rule in which the explicit taper defect is proportional to `a_(i-1)-a_i` at arbitrary positive gaps. The cubic exterior kernel is itself a discrete coboundary. Moreover the triple contrast flux is a nearest-neighbor positive-conductance Laplacian `L_lambda` on reciprocal gaps `h_i=1/g_i`, while the exact Xi log-gap velocity uses a long-range positive-conductance Laplacian `L_w` on the same field. The locally constant-weight bulk density is therefore proportional to

`h_i (L_lambda h)_i (L_w h)_i`.

Each operator is positive as a quadratic form, but their pointwise product has no established sign. This is the remaining nonlinear bulk-alignment gate.

## What remains possible

A positive theorem should compare the two conductance Laplacians after summation over a mesoscopic core, controlling the taper-difference term on the available buffer and using XF-028 rather than absolute values near collisions. A negative theorem should construct growing-buffer positive-gap configurations where taper differences vanish but `L_lambda h` and `L_w h` remain sufficiently misaligned to produce an order-one adverse aggregate.

The algebra remains universal for ordered logarithmic repulsion, so an eventual fixed-time conclusion must also invoke Xi-specific source information that excludes the bad configurations or supplies the needed aggregate alignment.

## Status / novelty

Discrete summation by parts, graph Laplacians, divided differences, and log-gas flow are classical. The synthesis is the sharpened frontier: **the taper/localization algebra is now exact; the unresolved resource is nonlinear alignment of two source-coupled conductance operators across the mesoscopic assembly**.

## Falsification criterion

Prove a source-valid coercive comparison between the aggregate `L_lambda` and `L_w` terms with lower-order taper loss, or construct a source-compatible growing-buffer family with persistent adverse bulk alignment despite collision coverage and vanishing taper variation.

## Lean-formalizable core

- Mesoscopic `log^2 T` memory and buffer scaling.
- Triple discriminant concavity and cubic coboundary identity.
- Exact nonlinear taper product rule.
- Reciprocal-gap factorization into `L_lambda` and `L_w` conductance operators.
