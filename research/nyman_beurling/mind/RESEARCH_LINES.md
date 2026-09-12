# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Prove a bounded finite future Gram certificate on an unbounded window sequence

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-049--NB-066 reduce persistence of the collective late quotient to one fixed stable-tail mode that is exactly natural on every finite window but globally orthogonal to the natural Nyman closure. Any such mode forces the worst exact future-extension cost `Lambda_R` to diverge; a bounded subsequence of `Lambda_R` kills the entire stable-tail space.

NB-067 removes the infinite-dimensional oracle from that criterion. The zero-trace natural space at window `R` is exactly the closed future innovation span. For a finite future horizon `N>=R`, let `A_R` be the visible prefix Gram matrix and `S_(R,N)` the Schur complement obtained after optimally eliminating innovations `D_R,...,D_N`. Then

\[
\Xi_{R,N}
=
\lambda_{\max}(A_R^{-1/2}S_{R,N}A_R^{-1/2})
\downarrow
1+\Lambda_R^2
\]

as `N->infinity`. Every finite horizon therefore gives the rigorous source-only upper bound

\[
\Lambda_R^2\le\Xi_{R,N}-1.
\]

Consequently, if there are `R_k->infinity`, finite horizons `N_k>=R_k`, and one constant `C` with

\[
S_{R_k,N_k}\preceq C^2 A_{R_k},
\]

then the stable-tail space is zero. Conversely a nonzero stable tail forces `Xi_(R,N(R))->infinity` for **every** finite horizon schedule.

The live theorem is now a concrete finite block-Gram domination problem rather than a direct infinite-dimensional right-inverse estimate. Analytically, prove such a bounded generalized-eigenvalue subsequence from the explicit causal innovations. Computationally, a certified finite matrix bound would already be globally decisive; floating-point evidence without rigorous enclosure is not enough.

## Treat local naturality, one-cell transmission, global extension cost, and finite certification separately

Exact finite-window interpolation can coexist with catastrophic global continuation cost. NB-067 adds that this global cost is nevertheless the monotone limit of finite source-only Schur complements. A finite certificate is strong because it bounds the true infinite continuation problem from above, not because finite rank or a small ordinary Gram eigenvalue is intrinsically meaningful.

Future work should target the generalized ratio relative to the visible Gram `A_R`. Global Gram conditioning alone, local rank, or cheap near-kernel directions do not control the extension norm that NB-066 identifies as decisive.
