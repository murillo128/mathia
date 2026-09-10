# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the useful rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force a near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Exploit the weighted moving-tail quotient as a source-faithful conditioned skeleton

**Linked intuitions:** `MI-001-coefficient-geometry-needs-target-coupling`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-024--NB-032 show that unrestricted low Gram energy and adjacency are not enough, but moving-tail differences form a certified target-poor nuisance sector whose quotient preserves the Nyman distance. NB-033 makes that quotient source-faithful: every coefficient below the cutoff survives unchanged, the tail collapses to one endpoint scalar, and a deterministic polylogarithmic cutoff preserves the finite-section distance multiplicatively while retaining the inverse-distance Möbius core.

NB-034 improves the metric geometry further. Weighted tail edges `n g_n-(n+1)g_{n+1}` are exactly the kernel of the first `M-1` harmonic-shell observations. Their orthogonal quotient has dimension `M-1`, preserves every head coefficient and one weighted tail sum, loses at most `1/M` in squared target distance, and has the explicit uniform bound `cond_2=O(M^2 (log M)^3)` independently of the upper section `N`. Thus a near-logarithmic-dimensional canonical skeleton can be both target-faithful and polynomially conditioned in its retained dimension.

The live theorem is now to use this explicit skeleton rather than merely certify it: prove that the Möbius-locked core or the retained weighted tail scalar obeys a quantitative constraint that forces the Nyman distance down, or enlarge the early-shell observation family while keeping target loss and conditioning controlled. The source theorem must act on the retained coordinates, not on discarded tail nuisance directions.

## Treat raw low eigenvalues and unrestricted adjacency as controls

Low Gram energy is abundant, raw Euclidean target loading can be misleading, and the full adjacent family spans the approximation space. The positive boundary is a quotient with a proved target-loss estimate, explicit source coordinates, and conditioning independent of the discarded upper tail.
