---
id: CLUE-mobius-cancellation-reciprocal-phase-prime-log-slab-coupling
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-033-annular-product-fiber-sign-coherence.md
  - research/mobius_cancellation/findings/MC-034-random-multiplicative-annulus-critical-rms.md
  - research/visual_exploration/visualizations/mobius-annulus-kernel-layers.md
---

# Does the reciprocal phase couple non-generically to the shrinking prime-log divisor slab?

## Observation

MC-033 removes cancellation inside each Huxley–Watt product fiber and writes the annular coefficient as `mu(a) R_N(a,b)` for `q=ab^2`. The visual control in `mobius-annulus-kernel-layers` resolves the remaining absolute pair mass by `k=omega(a)`. At `N=2000`, the large adjacent even/odd `k` layers almost cancel radially, but the resulting Möbius signed/absolute radial profile is statistically unremarkable relative to square-free-supported random multiplicative sign controls that preserve the same product-fiber coherence. Simple `omega(a)` layering therefore does not yet expose a Möbius-specific mechanism.

The same construction gives a sharper exact coordinate. Writing `a=product_j p_j` and divisors as hypercube sign vectors yields

`R_N(a,b) = #{epsilon in {-1,+1}^k : |sum_j epsilon_j log p_j| <= log(N^2/q)}`.

Hence both the central-slab width and the Huxley–Watt reciprocal phase `sin(2 pi h N^2/q)` are functions of the radial product coordinate `r=q/N^2`, while the fine structure inside the slab is carried by the actual prime-log vector of the square-free kernel.

MC-034 supplies the exact matched-control normalization for every bounded radial kernel `K`. If

`W_(N,K)(a) = sum_b R_N(a,b) K(N^2/(ab^2))`,

then independent prime-sign multiplicative controls have exact variance

`sum_(a>1) W_(N,K)(a)^2 = O(N^2 log^4 N)`.

Thus these controls already put the annular Fourier functional at the critical `N^(1+o(1))` power scale in RMS despite the `N^2` absolute coefficient mass from MC-033. The remaining arithmetic issue is not whether cross-kernel cancellation is *possible* at the right power scale, but whether the deterministic Möbius parity assignment is controllable against this particular occupancy/phase weight vector.

## Research question

After the phase-free `omega(a)` stratification is controlled away, does the **joint** distribution of prime-log slab occupancy and reciprocal phase produce arithmetic-specific cancellation for the deterministic Möbius parity character?

A concrete decomposition is

`A_(N,h,k)(I) = sum R_N(a,b) sin(2 pi h/r)`

over coprime square-free `a,b` with `N<ab^2<=N^2`, `r=ab^2/N^2 in I`, and `omega(a)=k`, so that the annular mode is `sum_k (-1)^k A_(N,h,k)`.

The full locations of the signed-log subset sums **inside** the accepted slab are not an additional observable of the Huxley–Watt mode: by MC-033, once `(a,b)` is fixed they enter the mode only through their count `R_N(a,b)`. Any finer subset-sum spectrum is relevant only insofar as it yields an independent theorem controlling that occupancy as the radial threshold varies.

The sharpened target from MC-034 is the deterministic normalized correlation

`Z_(N,K) = [sum_(a>1) (-1)^omega(a) W_(N,K)(a)] / sqrt(sum_(a>1) W_(N,K)(a)^2)`.

Determine whether source-natural arithmetic information weaker than Mertens-scale cancellation can force `Z_(N,K)=N^o(1)` for the Huxley–Watt sawtooth or reciprocal Fourier kernels, or whether natural multiplicative comparators can make the parity character align polynomially with the same weight family.

## Why it may matter

MC-033 says any gain must come from cross-product arithmetic/phase organization, joint cancellation across Fourier modes, or cancellation against another Huxley–Watt term. MC-034 now proves that the matched prime-sign ensemble already realizes the required **power** cancellation in RMS. This removes a broad probabilistic information-budget objection and isolates a genuinely deterministic question: whether the all-minus prime-sign point corresponding to Möbius is atypically correlated with the central-divisor occupancy and reciprocal phase.

A theorem giving only subpolynomial growth of the normalized correlation would already put this annular functional at the RH-compatible power scale because the exact matched-control denominator is `O(N log^2 N)`. Conversely, a source-compatible deterministic control with polynomially growing normalized correlation would show that the random-control benchmark is too weak to explain Möbius specifically.

## Decisive test

Use only information actually retained by the mode: `mu(a)`, the scalar threshold occupancy `R_N(a,b)`, `r=ab^2/N^2`, and the source-prescribed radial kernel. The first finite diagnostic is the exact `Z_(N,K)` normalization from MC-034, evaluated on fixed source-natural kernels and fixed scales rather than radial bins or Monte Carlo percentile bands.

For mathematical survival, however, finite behavior is not enough. Keep the direction only if it suggests and supports an analytic estimate for the deterministic parity correlation whose hypotheses are demonstrably weaker than the target Mertens bound. Kill or sharply narrow it if a matched square-free-supported multiplicative comparator satisfies the proposed auxiliary hypotheses while its normalized parity correlation grows polynomially, or if the required estimate can be transformed into an RH-equivalent coarse statistic with no independently controlled intermediate quantity.

## Evidence boundary

The persisted visualization is a finite experiment at `N=2000` and finds **no** arithmetic-specific anomaly in the phase-free radial `omega(a)` decomposition. MC-034 is exact for the matched random multiplicative ensemble but proves no new bound for the deterministic Möbius assignment. The prime-log slab formula is an exact rewriting of the central-divisor interval in MC-033, but no useful deterministic correlation with the reciprocal phase has been established. The classical Huxley–Watt kernel and Letendre's adjacent one-sided truncated Möbius divisor sums do not by themselves supply the required paired-cutoff phase estimate.

## Research disposition

Accepted in narrowed form. MC-033 proves the first information quotient: for fixed `(a,b)` every admissible divisor representation has the same sign and reciprocal phase, so the mode sees the prime-log subset-sum geometry only through the scalar occupancy `R_N(a,b)`. MC-034 then proves the exact second-moment benchmark: matched independent prime-sign multiplicative controls already place every bounded radial annular functional at `N^(1+o(1))` RMS scale.

The remaining live question is therefore the deterministic parity correlation `Z_(N,K)`, not generic random-like cancellation and not the fine subset-sum positions inside a fixed slab. A positive result must explain why rational-prime Möbius signs have subpolynomial normalized correlation with the specific Huxley–Watt occupancy/phase weights using arithmetic information independently weaker than RH-scale Mertens cancellation.