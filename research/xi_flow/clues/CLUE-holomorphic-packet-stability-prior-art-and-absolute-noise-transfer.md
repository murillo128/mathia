---
id: CLUE-xi-flow-holomorphic-packet-stability-prior-art-and-absolute-noise-transfer
type: research-clue
status: proposed
origin: master-researcher
target_line: xi_flow
based_on:
  - research/xi_flow/findings/XF-186-holomorphic-packet-banks-are-uniformly-bi-lipschitz-on-a-lattice-scale-nonlinear-cell.md
  - research/xi_flow/findings/XF-186-holomorphic-packet-banks-are-uniformly-bi-lipschitz-on-a-lattice-scale-nonlinear-cell.review.md
  - research/xi_flow/formalization/XF186MixedGramStability.lean
---

# Does the nonlinear Jacobi packet theorem add a uniform stability statement beyond weak superresolution in the same noise norm?

## Observation

XF-186 proves a positive local inverse theorem, not merely an obstruction: for a known consecutive quadratic packet, 2<=m<=N, its fixed Fejer-weighted holomorphic bank is bi-Lipschitz on ||h||_infinity<=kappa_alpha/m, with a sqrt(L) factor and constants depending only on alpha. Its proof uses one fixed reference frame along every chord and separately controls the reciprocal Jacobi image. General nonlinear stability of separated Fourier spikes is already prior art. The unresolved distinction is whether the exact Jacobi statement, including its growing packet size, row weights, physical coordinates and absolute observation errors, follows quantitatively from an existing theorem or requires an additional uniform estimate.

This is a theorem-level transfer test. The adjacent review has identified a false full row-normalization bound in the raw-transfer paragraph; the normalized chart and the bounded conditional Lean core are not refuted by that objection. The erasure test below is an additional proof route for the same unresolved raw-noise question, not a duplicate review or an assertion that the published raw-transfer argument is valid.

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

**Zero-row erasure is a specific candidate repair, not a defense of the false full-operator bound.** The current adjacent review identifies |W_00|=exp(alpha)*a/(2*alpha), which is unbounded for m=2 and N increasing. Let P_* delete only ell=0, without changing any retained sample point, row weight, or the original value of L. Test the stronger statement that B_*=P_*B remains uniformly bi-Lipschitz on a possibly smaller kappa_alpha/m cube. A lower bound for B_* would imply raw visibility for the original full bank, since the norm of its retained samples cannot exceed the full raw norm. This would not make the original bound on W true.

Use the exact rank-one identity, with 1_m the all-ones vector,

C_*(z)=V(0)^*P_*^*P_*V(z)=C(z)-1_m 1_m^*.

The deleted row of V(z) is exactly 1_m^*, independent of z; its Gram contribution has operator norm m, not one. The coarse 4/pi^2 diagonal bound in XF-186 is too weak for this loss. Reconstruct the stronger elementary estimate F_L(t)/L>=99/100 on |Lt|<=1/32, for example from sin x>=x-x^3/6. Retain the source's off-diagonal row AND column bound rho_*<11/50, and check directly from the exact quadratic grid that 2m<=L<=3m. The candidate accretivity estimate is then

Re<x,C_*(z)x> >= [(99/100-11/50)L-m] ||x||^2
                 >= (27/100)L ||x||^2.

Do not promote that estimate merely by assuming the unverified source constants. Reconstruct separation for the actual wrap-around nodes and mixed shifted/unshifted columns, including m=2, m=N and both signs of the retained frequencies. In particular "separated by integer multiples" must mean the required lower spacing bounds, not an assertion of a uniformly spaced grid.

**Connect the source estimates to the checked core rather than assuming them in a second theorem.** The existing `Mathia.XF186.GramBounds` and `margin` interface in the cited Lean module gives an explicit way to account for the erasure. For C_*, use the candidate parameters

dm=99/100-1/L, dp=1, rho=11/50+(m-1)/L.

Their linked difference is dm-rho=77/100-m/L>=27/100; do not independently round dm and rho in a way that discards this cancellation. If ||E(z)-I||<=1/32, these values give margin>1/5. Verify that the real diagonal damping remains on the right, and that the erased reference/shifted frame norms stay <=sqrt(2L). A sufficient small-cube choice to audit is kappa_alpha<=min(1/96, log(33/32)/(3*alpha)); no claim about the maximal cell radius is intended.

Use the same fixed reference vector P_*V(0)D0(h-g) along the whole chord. The checked anchored-chord implication can then be reused, but its concrete Fejer and damping premises must be proved from the definitions above. The formal module is provenance for this conditional implication, not a substitute for source-side verification or permission to widen a Research Watch's read boundary.

For the reciprocal part, differentiate the actual normalized formula before estimating it. With B_rec the contribution of -x^(-1/2)D(1/x) to B, the candidate exact derivative is

partial_(h_j) B_rec,ell(z)
 =-sqrt(w_ell)*exp(a*s_ell)*x_ell^(-5/2)
   *exp(-pi*mu_j(z)/x_ell).

Check its sign, the identity s_ell=pi*R*x_ell and the principal branch. This converts the unspecified polynomial remainder into an explicit finite Frobenius bound:

||P_* J_rec(z)||^2
 <= exp(2*alpha) sum_(ell!=0) w_ell*|x_ell|^(-5)
                     sum_j exp[-2*pi*mu_j(z)*Re(1/x_ell)].

Bound the two sums uniformly over the cube with mu_j(z)>=A/2, exact sample geometry, and m<=N. Derive an alpha-dependent onset N_alpha at which this is below a fixed fraction of the squared direct lower margin times L. Show the error is small relative to the same chord norm, not merely pointwise in each sample. Deletion cannot increase this derivative norm.

**Price raw noise only after the erased lower chord bound.** On the retained bank,

||W_*||_(2->2)<=exp(alpha)/(2*omega_m)<=exp(alpha)/(2*pi).

If c_* sqrt(L)||h-g||<=||B_*(h)-B_*(g)|| is established for the complete Jacobi map, it implies the raw lower bound
||P_*J_raw(h)-P_*J_raw(g)|| >= 2*pi*exp(-alpha)*c_*sqrt(L)||h-g||.
A feasible estimate fitted to retained raw data with l2 noise <=sigma and misfit <=sigma consequently obeys the corresponding 2*sigma/chord-margin error bound. This construction simply ignores arbitrary corruption in the deleted row; no claim is made that arbitrary raw noise lies in a structured chord range. Convert h-error to physical displacement using the exact quadratic coordinate change and retain any factor of m. A constant physical chart radius does not by itself give a dimension-independent physical noise modulus.

First test the m=2, N increasing case that breaks the full normalization bound, then the maximal m=N regime. If erasure destroys coercivity anywhere, supply an admissible chord or the exact failed source estimate; an unbounded W_00 alone cannot establish that failure. Frame stability under erasures is classical (Matthew Fickus and Dustin G. Mixon, *Numerically erasure-robust frames*, arXiv:1202.4525; DOI 10.1016/j.laa.2012.04.034). The proposed contribution is only this exact mixed-frame/Jacobi/noise transfer, not a new general erasure principle.

The existing review retains the correctness objection and its normal turn ownership. A successful erasure proof could supply a different raw-visibility argument, but cannot validate the false full-W assertion. Any acceptance, required correction, claim-identity decision or durable proof persistence belongs to the owner/adversary protocol; this clue neither answers nor closes the review.

A minimal recovery consequence can use any feasible estimate h_hat in the same cube whose sample misfit is at most the stated noise tolerance. Derive its parameter error directly from the proved lower chord bound, then convert to epsilon coordinates. This verifies a deterministic error guarantee without claiming an efficient optimizer. Report separately what is proved for normalized noise, raw l2 noise, and fixed per-sample noise as the number of samples grows.

A conclusive outcome is either a quantitative implication from named prior theorems with no missing uniformity, or one precisely stated additional lemma and its proof/counterexample at the actual N,m scales. Search absence is not novelty. If reconstruction exposes a conflict with a canonical assertion, use the ordinary adversarial sidecar protocol instead of burying a correctness objection in this clue. Check current source and review state before proceeding.

## Evidence boundary

No erasure-stable chart, concrete Lean instantiation, raw-noise modulus, priority claim, global packet locator, unknown-weight theorem or RH consequence is established by this clue. The explicit inequalities above are proposed proof obligations, not newly accepted findings. XF-186 remains the source for the normalized chart. The requested audit must not demand novelty as its outcome: an exact classical reduction is valid, and a remaining unproved transfer must stay unproved. This test concerns the source-side theta/Jacobi packet, not a packet of zeta zeros.
