# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Estimate the q-adic terminal visible-energy distortion of the radial certificate

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`.

NB-066--NB-084 reduce persistent continuation to finite-future prediction and identify an exact actual-source Toeplitz certificate along every integer-dilation descendant ray. NB-085 settles the infinite-depth radial limit: the actual periodized density has `log W_(j,q) in L^1`, giving a strictly positive Szegő floor and reducing qualitative success to boundedness of the aggregate floor charge `S_(R,q)`.

NB-086 lower-bounds that infinite-depth charge by the normalized Gram determinant deficit of the terminal visible innovations. This turns the hidden radial future into a finite-window obstruction: divergent terminal visible correlation entropy already kills a fixed-`q` radial certificate.

NB-087 now uses exact integer branching to compress a substantial part of that test to one explicit two-scale norm ratio per complete terminal sibling block:

`eta_(j,R)^(q)= q ||J_(R/q)D_j||^2 / sum_(k=qj)^(q(j+1)-1) ||J_R D_k||^2 - 1`.

There is `c_q>0` with

`S_(R,q) >= c_q sum_(j in P_(R,q)) |eta_(j,R)^(q)|^2`.

Thus bounded radial charge forces an `l^2` budget on `asymp R` scalar visible-energy distortions: mean square `O(R^-1)`, RMS `O(R^-1/2)`, and only boundedly many fixed-size failures. Conversely, divergent squared distortion mass rules out that radial certificate without estimating any aliased Szegő floor or the full terminal correlation matrix.

The live theorem is now to estimate these matched truncated parent/child norms for the actual Nyman source at `j asymp R`. If the squared distortions diverge, the next mechanism must be cross-ray or otherwise nonradial. If they stay bounded, this necessary test passes but within-block contrast directions, cross-block correlations, earlier indices and the remaining nonterminal floor charge still require control.

## Keep stationary inverse singularities, aliasing, prediction floor, visible entropy, q-adic scalar distortion and future geometry separate

NB-083 remains the matched control for a genuine unit-circle zero of a stationary symbol. NB-084 replaces that symbol by the arithmetic alias-periodized density; NB-085 gives its positive geometric-mean floor; NB-086 exposes the terminal determinant bill; NB-087 extracts from exact branching a canonical scalar Rayleigh defect whose squared mass already pays that bill.

A bounded scalar distortion budget is only necessary, not sufficient, for bounded aggregate charge, and a bad fixed-ray charge is a failure of one restricted future geometry rather than evidence for a nonzero stable tail. The full nonstationary future may still exploit cross-ray cancellation.