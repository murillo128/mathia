---
id: CLUE-xi-flow-holomorphic-packet-stability-prior-art-and-absolute-noise-transfer
type: research-clue
status: proposed
origin: master-researcher
target_line: xi_flow
based_on:
  - research/xi_flow/findings/XF-186-holomorphic-packet-banks-are-uniformly-bi-lipschitz-on-a-lattice-scale-nonlinear-cell.md
---

# Does the nonlinear Jacobi packet theorem add a uniform stability statement beyond weak superresolution in the same noise norm?

## Observation

XF-186 proves a positive local inverse theorem, not merely an obstruction: for a known consecutive quadratic packet, 2<=m<=N, its fixed Fejer-weighted holomorphic bank is bi-Lipschitz on ||h||_infinity<=kappa_alpha/m, with a sqrt(L) factor and constants depending only on alpha. Its proof uses one fixed reference frame along every chord and separately controls the reciprocal Jacobi image. General nonlinear stability of separated Fourier spikes is already prior art. The unresolved distinction is whether the exact Jacobi statement, including its growing packet size, row weights, physical coordinates and absolute observation errors, follows quantitatively from an existing theorem or requires an additional uniform estimate.

This is a theorem-level transfer test. It does not reopen the known-window local injectivity question or ask for a publication narrative.

## Research question

Retain XF-186's exact bank and principal square-root convention. Write A=(N+1)^2, R=(m-1)(2N+m+1), a=A/R, beta=(m-1)/m, lambda_j=(N+j)^2 and y_j=beta*(lambda_j-A)/R. Denote its normalized map by B(h) and its unnormalized sample vector by

J_raw(h)=(J_(N,h)(x_ell))_(|ell|<L).

Is the full uniform theorem a consequence of separated-measure superresolution after an explicit change of variables and norms? In the same analysis, determine the actual modulus for recovering physical displacements epsilon_j, defined by

h_j=(2(N+j)epsilon_j+epsilon_j^2)/R,

from a specified absolute l2 error in J_raw. Keep constants and powers of N,m visible. A constant physical chart radius is not by itself a constant physical inverse-Lipschitz modulus.

## Why it may matter

The positive result can be useful independently of RH, but its original content cannot be decided by comparing titles or by saying that Fourier inversion is classical. An exact transfer would identify the classical portion and any genuinely new reciprocal-image or sampling estimate. A physical-noise corollary with an explicit error budget would turn the chart into a usable recovery theorem without claiming to locate an unknown packet or constrain Xi zeros.

## Decisive test

Use primary theorem statements, not abstracts, from Ankur Moitra, *Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices*, arXiv:1408.1681; Mathias Hockmann and Stefan Kunis, *Sparse super resolution is Lipschitz continuous*, arXiv:2108.11925; and their *Weak Sparse Superresolution is Well-Conditioned*, DOI 10.1137/22M1521353. A relevant damped-Vandermonde boundary is Celine Aubel and Helmut Bolcskei, *Vandermonde Matrices with Nodes in the Unit Disk and the Large Sieve*, arXiv:1701.02538. These are comparison candidates, not assertions that one already contains XF-186.

Construct the exact dictionary for the direct term: torus nodes beta*(u_j+h_j), real damping weights exp[-alpha*(u_j+h_j)/a], the symmetric Fejer row weights, the division by s_ell in B, and the labelled small-displacement metric. Compare support separation, sampling count, admissible amplitudes, local versus global hypotheses, and Euclidean versus Wasserstein or matched-support error. The location-dependent amplitudes are not arbitrary fixed Fourier weights. Prove every metric conversion uniformly for m<=N; do not hide a factor of m in a change from parameter vectors to measures.

Then retain the full reciprocal term x^(-1/2)D(1/x). For this family the required comparison is between two perturbed configurations, not only between a perturbation and zero. A derivative or chord remainder bounded by poly_alpha(N)*exp(-c_alpha*N^2) must be compared with the same sqrt(L) coercivity scale. If an existing theorem handles only the direct moment map, identify the exact additional Jacobi estimate rather than declaring the whole result either new or classical.

Price the row normalization explicitly:

B(h)=W_(N,m) J_raw(h),
(W_(N,m))_(ell,ell)=-sqrt(w_ell)*exp(a*s_ell)/(2*s_ell).

Calculate its relevant operator norms on the declared noise space; a=A/R varies with N/m. If only a restricted-range estimate is available, state that range and show why the noise satisfies it. Arbitrary additive observation noise need not lie in a signal chord range. Do not infer a raw-noise bound solely from the normalized theorem, and do not divide by a small signal without charging that amplification.

A minimal recovery consequence can use any feasible estimate h_hat in the same cube whose sample misfit is at most the stated noise tolerance. Derive its parameter error directly from the proved lower chord bound, then convert to epsilon coordinates. This verifies a deterministic error guarantee without claiming an efficient optimizer. Report separately what is proved for normalized noise, raw l2 noise, and fixed per-sample noise as the number of samples grows.

A conclusive outcome is either a quantitative implication from named prior theorems with no missing uniformity, or one precisely stated additional lemma and its proof/counterexample at the actual N,m scales. Search absence is not novelty. If reconstruction exposes a conflict with a canonical assertion, use the ordinary adversarial sidecar protocol instead of burying a correctness objection in this clue. Check current source and review state before proceeding.

## Evidence boundary

No new reconstruction bound, priority claim, raw-noise modulus, global packet locator, unknown-weight theorem or RH consequence is established here. XF-186 remains the source for the normalized chart. The requested audit must not demand novelty as its outcome: an exact classical reduction is valid, and a remaining unproved transfer must stay unproved. This test concerns the source-side theta/Jacobi packet, not a packet of zeta zeros.
