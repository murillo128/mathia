# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the useful rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force a near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Use the weighted skeleton through its exact Möbius/Vasyunin dual oracle

**Linked intuitions:** `MI-001-coefficient-geometry-needs-target-coupling`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-024--NB-034 isolate a weighted moving-tail quotient that preserves target distance, every head coefficient, and one weighted tail scalar while keeping conditioning polynomial in the retained dimension and independent of the discarded upper section. NB-035 shows that the retained tail scalar is not a free compressed coordinate: a bounded reciprocal-Möbius selector recovers it exactly, so the skeleton remains source-locked.

NB-036 sharpens this into an exact dual description. Vasyunin's classical biorthogonal defects give explicit readouts for every retained skeleton coordinate; the head coordinates are the original coefficients and the endpoint coordinate is the weighted tail sum. Their norms scale only linearly with the retained index, yielding inverse-distance prefix locking. Thus the missing “target oracle” is no longer an unknown projection computation, but it is also not cheap independent information: it is explicitly Möbius-bearing.

The live theorem is to exploit this exact duality without circularity. Either derive a target-relevant aggregate of the Vasyunin defects that can be controlled strictly cheaper than the corresponding Möbius data, or prove that the weighted skeleton cannot yield an RH-scale gain without paying essentially the same source bill. Enlarging the quotient or computing its Gram matrix more accurately is secondary unless it changes that oracle complexity.

## Treat finite-dimensional compression and source cost as separate gates

A quotient can be low-dimensional, target-faithful, and well-conditioned while its coordinates remain arithmetically expensive. The Vasyunin dual basis makes that distinction explicit. Future proposals should price the source theorem needed to populate the retained coordinates, not infer tractability from dimension or condition number alone.