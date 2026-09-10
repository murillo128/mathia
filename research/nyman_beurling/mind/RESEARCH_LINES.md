# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-rooted-shell-mixing-needs-near-linear-discrepancy`.

The shell decomposition still reduces the useful rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force a near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Use Gram-whitened moving-tail adjacency as a certified nuisance quotient

**Linked intuitions:** `MI-001-coefficient-geometry-needs-target-coupling`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`.

NB-024--NB-029 separate low coefficient energy from target information and show why the complete adjacent-difference family cannot be removed: its closed span is the entire canonical Nyman approximation space. NB-030 strengthens the warning. A vector can have tiny normalized Gram Rayleigh quotient and large raw coefficient loading while still being almost perfectly aligned with the target after Gram whitening, so Euclidean coefficient diagnostics are not a valid target-poverty test.

NB-031--NB-032 identify the useful restricted sector. Adjacent differences pushed into the moving tail are genuinely target-poor in the Gram-whitened geometry, and projecting away their closed span preserves the full target distance asymptotically. This supplies a certified nuisance quotient without destroying the approximation problem.

The live theorem is now to exploit that quotient: isolate the head/source-locked component left after removing the moving-tail nuisance sector, quantify whether the canonical Möbius-locked vector is forced to occupy it, or extend the certified target-poor construction to a larger multiscale low-Rayleigh sector while preserving the Nyman distance. The separator must remain Hilbert/Gram-relative rather than return to raw coefficient loading.

## Treat small eigenvalues, raw target coefficients, and unrestricted adjacency as controls

Low Gram energy is generically abundant, raw Euclidean target loading can be misleading after whitening, and unrestricted adjacent differences are topologically complete. The useful positive boundary is narrower: a nuisance sector may be quotiented only after its Gram-whitened target occupation is shown to vanish and the orthogonal complement is proved to preserve the target distance.
