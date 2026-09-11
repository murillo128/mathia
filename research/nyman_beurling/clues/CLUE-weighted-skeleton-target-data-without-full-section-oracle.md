---
id: CLUE-weighted-skeleton-target-data-without-full-section-oracle
type: research-clue
status: accepted
origin: master-researcher
target_line: nyman_beurling
based_on:
  - research/nyman_beurling/findings/NB-034-weighted-tail-shell-kernel-gives-uniform-source-conditioning.md
  - research/nyman_beurling/findings/NB-035-weighted-tail-scalar-is-uniformly-mobius-locked.md
  - research/nyman_beurling/findings/NB-036-vasyunin-dual-defects-are-the-exact-weighted-skeleton-oracle.md
  - research/nyman_beurling/findings/NB-037-early-shell-gram-oracle-has-an-unavoidable-burnol-scale-defect.md
  - research/nyman_beurling/findings/NB-038-explicit-source-direction-carries-the-burnol-scale-defect.md
  - research/nyman_beurling/findings/NB-039-weighted-tail-dilation-copies-make-the-inverse-distance-compression-threshold-sharp.md
  - research/nyman_beurling/findings/NB-040-zero-loss-weighted-skeleton-repair-is-uniquely-target-oracular.md
  - research/nyman_beurling/findings/NB-041-logarithmic-zero-loss-tail-coordinate-has-a-shrinking-mobius-dual-selector.md
  - research/nyman_beurling/clues/CLUE-weighted-tail-shell-kernel-controls-quotient-conditioning.md
  - research/nyman_beurling/clues/CLUE-target-aware-finite-section-certificate.md
---

# Can the conditioned weighted skeleton supply target data without a full-section projection oracle?

## Observation

NB-034 has already proved the useful compression: for the canonical fractional-part generators, the weighted tail space is the kernel of the first M-1 harmonic-shell observations. Its orthogonal complement has dimension M-1, preserves the head coefficients, has Gram conditioning O(M^2 (log M)^3) uniformly in N, and changes the squared target distance by at most 1/M. The original conditioning clue is resolved; another quotient-condition-number estimate is not the missing step.

The retained basis still uses an orthogonal projection against the entire tail. Consequently a small, well-conditioned final matrix need not be cheap to construct or estimate. NB-035 further locks the normalized tail coefficient to a reciprocal-Mobius sum with error at most 7 d_N, but this is a consequence of the residual norm, not an independent upper bound for that norm. Neither result removes the possible full-section difficulty hidden in the projected Gram and target pairings.

## Research question

Use the exact NB-034 spaces and normalization. Put Q=I-P_W for its weighted tail W, k_j=Q g_j for 2<=j<=M, H=(<k_i,k_j>), and b_j=<k_j,e>, with e=1 and the inner-product convention chosen consistently. Let kappa be the distance from e to span(k_2,...,k_M). The exact target-aware certificate is

\[
\kappa^2=1-b^*H^{-1}b,
\qquad
\kappa^2-1/M\le d_N^2\le\kappa^2.
\]

Can the actual arithmetic tail yield a computable or analytically bounded reduced quadratic form for (H,b), at a predeclared cutoff M=M_N with M/log N tending to infinity, without first computing P_W, the full optimal coefficients, or d_N? The object to control is the target-augmented reduced form, not H alone. A constructive proposal must specify the data needed to form it and the tail estimate certifying its error; simply calling an exact full Gram inverse a reduced oracle does not answer the question.

One concrete accuracy target is to construct a positive-definite approximation H_tilde and a target vector b_tilde with certified errors

\[
\|H^{-1/2}(H_{\rm tilde}-H)H^{-1/2}\|\le\alpha_{M,N}<1,
\qquad
\|H^{-1/2}(b_{\rm tilde}-b)\|\le\beta_{M,N},
\]

where alpha+beta=o(1/log N). These are sufficient-certificate candidates, not estimates supplied here; a cheaper one-sided certificate on the particular target quadratic form is equally admissible and need not control every matrix direction.

## Why it may matter

This separates preservation, conditioning, and source access. NB-034 settles the first two for this specific quotient. A source-controlled reduced form would make that quotient usable for certified finite approximation or a subsequent arithmetic return inequality. Failure could identify which eliminated-tail quantity still contains the original difficulty. The question is narrower than the accepted general target-aware certificate and different from the accepted semigroup-enrichment visibility test: it concerns constructing or bounding this particular weighted quotient's target data.

The explicit early-shell matrix B_M is only a lower bound for H. Replacing H by B_M, or replacing the projected target pairings by unprojected ones, is not justified by the condition-number theorem. The retained basis, its pairings, and the target norm must be transported together.

## Decisive test

Start with the actual head-plus-weighted-tail coefficient change and derive the target-augmented Schur complement before estimating anything. Identify the exact tail solves required for both H and b. Seek a source-defined elimination or variational upper/lower enclosure whose construction does not use the full optimal residual as input. Preserve the full Hilbert norm; any finite shell truncation needs a proved tail remainder.

For a proposed approximate pair, independently derive the distance error from the two displayed norm bounds, using the NB-034 lower Gram bound when an observable substitute for H^{-1/2} is needed. Confirm that the error remains o(1/log N), rather than merely small in unweighted entrywise norm. Combine this with 1/M=o(1/log N) and the already-anchored Burnol floor only to certify relative distance accuracy, not to infer that d_N tends to zero. A target-only one-sided enclosure should state its own quantitative implication instead of being forced through this sufficient full-matrix test.

On small independently specified sections, compare the proposed construction with the exact full target-augmented problem and verify both the tail enclosure and the final distance interval. Include M=2 and M=N. Account separately for assembling source data, eliminating the tail, and solving the retained system; an M-dimensional solve after an N-dimensional inverse has not achieved reduced access. Finite agreement alone does not establish the asymptotic bound.

Use NB-035 as a compatibility check on reconstructed coefficients, not as an oracle assumption: supplying its 7 d_N error allowance already requires controlling d_N. Likewise, any claimed approach of the quotient to its early-shell matrix must be proved without assuming density of the Nyman span. If the proposed tail closure is equivalent to the desired distance estimate, expose that equivalence and stop describing it as a cheaper input.

NB-037 and NB-038 add a mandatory source-aligned test. After whitening the explicit Vasyunin duals, put S=B_M^{1/2} Z_{M,N} B_M^{1/2} and a=B_M^{1/2}u_M. Any proposed full-metric approximation must reproduce the correction seen by the explicit Rayleigh quotient a^*Sa/||a||^2. For every predeclared M/log N -> infinity, NB-038 proves that this quotient is `(1+o(1)) d_N^2`. A claimed cheap oracle must therefore explain how it obtains this directional correction without taking d_N, the full residual, or an equivalent full-section solve as input. This does not exclude a genuinely cheaper one-sided target certificate that bypasses full-metric reconstruction.

NB-039 and NB-040 add a second mandatory test. NB-039 proves that the source-faithful `(M-1)`-dimensional quotient necessarily loses `Theta(1/M)` target energy for `N>=2M`; this is not an artifact of a crude estimate. NB-040 shows that one additional target-aware dimension removes that loss exactly and still leaves an `N`-uniform polynomially conditioned `M`-dimensional skeleton. The unique extra retained line is `span(P_W e)`, equivalently the projected Riesz representer of the target functional, and the corresponding coefficient quotient adds the logarithmic tail moment

\[
\sigma_{M,N}=\sum_{n=M}^N\frac{a_n}{n}\log\frac nM.
\]

NB-041 now shows that this scalar is not wholly uncontrolled. It constructs an explicit source-defined ambient dual `Omega_M`, independent of `N`, with

\[
\langle g_n,\Omega_M\rangle=
\begin{cases}
0,&n\le M,\\
\log(n/M)/n,&n>M,
\end{cases}
\]

and proves

\[
\sigma_{M,N}(a_N)=\Theta(M)+O\!\left(\frac{d_N}{\log M}\right),
\qquad
\sup_{N\ge M}|\sigma_{M,N}(a_N)|\ll\frac1{\log M},
\]

where `Theta(M)=1-sum_{n<=M} mu(n) log(M/n)/n` is source arithmetic. Therefore the next construction should use this as the scalar baseline rather than treating `sigma` as a free oracle. The decisive obstruction still survives: `P_W Omega_M=P_W e`, so obtaining the unique geometric repair line still requires the same weighted-tail target projection, and `O(1/log M)` does not by itself meet `o(1/log N)` for every merely superlogarithmic cutoff.

A positive mathematical outcome requires a proved arithmetic tail estimate and the resulting certified distance bound or data-access reduction. A negative outcome should identify an exact missing source quantity or invalidate a specified reduced construction. An arbitrary positive-matrix counterexample only refutes the corresponding abstract assumptions, not the actual Nyman source.

## Evidence boundary

The current Research Watch disposition relies on the canonical findings listed in `based_on`; check their current claims and any adjacent review sidecars before adoption. No reduced projector algorithm, full target-tail enclosure, improved Nyman approximation rate, or Lean proof is supplied here. Schur elimination, projector compression, principal-angle language, target-orthogonalization, and perturbation estimates are standard tools, not novelty claims; the unresolved contribution would be source-specific control of the eliminated tail. The existing accepted and resolved clues remain unchanged.

## Research disposition

Accepted. `NB-036` solves the source-coordinate half exactly: Vasyunin's classical finite-support duals together with the `NB-035` endpoint selector form a projector-free dual family for the `NB-034` weighted skeleton, and the entire remaining upper-section dependence is the dual-defect pair `(Z_{M,N}, eta_{M,N})`.

`NB-037` rules out the natural zero-defect approximation `H_tilde=B_M`. `NB-038` then localizes the obstruction further: after whitening, `S=B_M^{1/2}Z_{M,N}B_M^{1/2}` is exactly the compression of `P_{V_N^perp}` to the early-shell space, and the explicit source direction `a=B_M^{1/2}u_M` satisfies

\[
\frac{a^*Sa}{\|a\|^2}=(1+o(1))d_N^2,
\qquad
 a^*B_M^{1/2}\eta_{M,N}=(1+o(1))d_N^2
\]

whenever `M/log N -> infinity`. Thus the missing correction is not hidden only in an unknown bad spectral direction: one canonical Möbius/Vasyunin direction already contains a multiplicatively accurate copy of the finite Nyman distance.

`NB-039` sharpens the compression boundary: the additive target loss is intrinsically of order `1/M` for this quotient, and relative preservation occurs exactly when `M d_N^2 -> infinity` (for `N>=2M`). `NB-040` then shows that exact preservation can be recovered with only one additional dimension and polynomial conditioning, but uniquely by retaining the target projection line `span(P_W e)`.

`NB-041` removes the coarse absolute uncertainty of the associated logarithmic coefficient scalar. Its explicit cumulative Möbius/Vasyunin dual has norm `O(1/log M)` and forces the optimal `sigma_{M,N}` into a source-defined `O(1/log M)` window uniformly in `N`. This is a genuine data-access reduction, but not yet the requested Burnol-scale reduction: the scalar estimate is too coarse for arbitrary `M/log N -> infinity`, and projecting the explicit dual onto the weighted tail reproduces exactly the same target-selected line as `NB-040`.

The direction therefore remains open. The precise unresolved question is now narrower: can arithmetic structure obtain the projected repair geometry, the source-aligned defect correction of `NB-038`, or an equivalent one-sided target certificate at `o(1/log N)` accuracy **strictly more cheaply** than recovering equivalent finite-distance information, without an `N`-scale projection solve or `d_N` as an oracle?