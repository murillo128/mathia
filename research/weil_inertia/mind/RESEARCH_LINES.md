# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Match the gamma block's negative spectral profile with source-conditioned repair, not only rank

**Linked intuitions:** `MI-010-pair-correlation-slack-is-a-shared-exceptional-budget`, `MI-029-post-threshold-compact-positivity-needs-noncompact-tail-retention-not-a-canonical-finite-rank-correction`, `MI-050-full-localized-weil-energy-turns-any-rh-failure-into-a-finite-radius-first-crossing`, `MI-051-local-threshold-continuity-does-not-bootstrap-cofinally-from-an-energy-budget-alone`, `MI-052-common-cut-short-preserves-inherited-pivot-without-double-spending`, `MI-053-odd-parity-couples-difference-and-image-kernels-before-half-density-transport`, and `MI-054-the-gamma-floor-carries-a-linearly-growing-negative-index`.

WI-369 gives the exact gamma-corrected archimedean decomposition with sharp lower floor `-C_Gamma I`, where `C_Gamma=pi/2+gamma+log(8 pi)`. WI-370 rules out the conservative scalar repair of the published MASTER budget: at `k=33` even the unspent direct target-ground coefficient is already below `C_Gamma` before later nonnegative debits.

WI-371 strengthens this from a scalar-floor warning to an inertia statement. Compactly supported bulk test spaces of dimension `m_A=floor(c_* A)` can be chosen so that the entire gamma block is uniformly negative on them. Hence the negative index grows at least linearly in the aperture `A`; any additive positive repair must carry rank `Omega(A)`, and a finite Schatten-`p` repair must spend at least order `A^(1/p)` norm.

WI-372 strengthens the necessary repair from aggregate size to a full spectral profile. If a bounded self-adjoint correction `K_A` makes the gamma block nonnegative, then for every `0<t<C_Gamma` its positive spectral counting function must satisfy

`liminf N_A^+(t)/A >= (1/pi) sqrt((C_Gamma-t)/M_2)`,

where `M_2=7 zeta(3)+pi^3/4`. For positive compact repairs this gives a quantile lower bound `kappa_{A,ceil(alpha A)} >= C_Gamma-pi^2 M_2 alpha^2` asymptotically for every `alpha<c_bulk`; factorized repairs `K_A=B_A^*B_A` inherit the corresponding singular-value profile. Thus matching only rank or a single Schatten norm is insufficient.

The live source question is now profile-level. What effective positive spectrum does the actual source network place on the explicit interior bulk quasimodes as `A` grows? Either the source-conditioned admissible space excludes the corresponding negative directions across the whole depth range, or its repair must overlap them with the required linear rank **and** eigenvalue/singular-value distribution. Nominal source dimension, a scalar reserve, or one large singular value cannot substitute for that comparison.

## Keep full-core inertia, source dimension and operator reserve distinct

The gamma block's spectral profile does not by itself disprove a source construction whose active geometry changes with `A`, nor does WI-372 cover non-additive rooted-Schur mechanisms. Conversely, a growing number of source coordinates does not pay the debt automatically. Future arguments must identify the source-conditioned image, its overlap with the WI-371 bulk subspaces, and the distribution of positive singular values there. Scalar reserve, nominal rank, global Schatten mass and coercive spectral profile are distinct currencies.
