# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Prove a bounded finite future Gram certificate or exclude the boundary-chain mechanism arithmetically

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-049--NB-067 reduce persistence of the collective late quotient to one fixed stable-tail mode whose finite traces are all natural but whose exact global continuation cost diverges. For a finite future horizon `N>=R`, the normalized Schur certificate

\[
\Xi_{R,N}
=
\lambda_{\max}(A_R^{-1/2}S_{R,N}A_R^{-1/2})
\downarrow
1+\Lambda_R^2
\]

bounds the true continuation cost from above. A uniform finite bound on any unbounded window sequence kills the entire stable-tail space; a nonzero stable tail forces divergence for every horizon schedule.

NB-068 closes the tempting local-memory shortcut. It constructs two matched causal sources with identical visible spaces, identical defect spaces, identical newest innovations, identical one-cell defect sectors, **and identically zero canonical one-cell memory maps `Gamma_R` at every step**, yet one source has no stable tail and the other has a one-dimensional stable tail.

In the boundary-chain control,

\[
\Lambda_R^2
=
\frac{T_{<R}^2}{T_{\ge R}^2}
\to\infty,
\qquad
\Xi_{R,N}
=
1+\frac{T_{<R}^2}{T_{R:N+1}^2},
\]

so every finite Schur certificate detects the hidden global mode even though every one-cell quotient map is zero. Finite causal bandwidth, small local transmission, square-summable local leakage, and even complete absence of the canonical one-cell memory channel are therefore insufficient.

The live theorem is now genuinely global. Either prove a bounded source-defined generalized-eigenvalue subsequence for the actual Nyman innovations, or identify an arithmetic/coercive property that rules out the boundary-chain mechanism while remaining visible in those finite Schur complements. Further refinement of `Gamma_R` alone attacks a closed resource.

## Treat local naturality, one-cell memory, global continuation cost, and finite certification separately

Exact finite-window interpolation can coexist with catastrophic global continuation cost. NB-068 makes the separation strict: all canonical one-cell memory data may vanish while an infinite boundary mode survives. The obstruction is cumulative compatibility at infinity, not hidden one-step transmission.

NB-067 remains the correct finite access point because its Schur complements see precisely the continuation energy that local quotient geometry discards. Future work should target the generalized ratio relative to the visible Gram `A_R`, or derive an actual-source estimate excluding `l^2` boundary-chain modes. Global Gram conditioning, local rank, finite bandwidth, or vanishing `Gamma_R` do not control the decisive extension norm.
