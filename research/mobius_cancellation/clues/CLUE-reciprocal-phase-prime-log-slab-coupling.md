---
id: CLUE-mobius-cancellation-reciprocal-phase-prime-log-slab-coupling
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-033-annular-product-fiber-sign-coherence.md
  - research/visual_exploration/visualizations/mobius-annulus-kernel-layers.md
---

# Does the reciprocal phase couple non-generically to the shrinking prime-log divisor slab?

## Observation

MC-033 removes cancellation inside each Huxley–Watt product fiber and writes the annular coefficient as `mu(a) R_N(a,b)` for `q=ab^2`. The visual control in `mobius-annulus-kernel-layers` resolves the remaining absolute pair mass by `k=omega(a)`. At `N=2000`, the large adjacent even/odd `k` layers almost cancel radially, but the resulting Möbius signed/absolute radial profile is statistically unremarkable relative to square-free-supported random multiplicative sign controls that preserve the same product-fiber coherence. Simple `omega(a)` layering therefore does not yet expose a Möbius-specific mechanism.

The same construction gives a sharper exact coordinate. Writing `a=product_j p_j` and divisors as hypercube sign vectors yields

`R_N(a,b) = #{epsilon in {-1,+1}^k : |sum_j epsilon_j log p_j| <= log(N^2/q)}`.

Hence both the central-slab width and the Huxley–Watt reciprocal phase `sin(2 pi h N^2/q)` are functions of the radial product coordinate `r=q/N^2`, while the fine structure inside the slab is carried by the actual prime-log vector of the square-free kernel.

## Research question

After the phase-free `omega(a)` stratification is controlled away, does the **joint** distribution of prime-log slab occupancy and reciprocal phase produce arithmetic-specific cancellation?

A concrete decomposition is

`A_{N,h,k}(I) = sum R_N(a,b) sin(2 pi h/r)`

over coprime square-free `a,b` with `N<ab^2<=N^2`, `r=ab^2/N^2 in I`, and `omega(a)=k`, so that the annular mode is `sum_k (-1)^k A_{N,h,k}`. Determine whether the scalar occupancy `R_N(a,b)`, coupled to the radial phase and the Möbius sign across distinct square-free kernels, has a stable arithmetic-specific relation absent for matched random multiplicative controls and analytically exploitable without assuming Mertens-scale cancellation.

The full locations of the signed-log subset sums **inside** the accepted slab are not an additional observable of the Huxley–Watt mode: by MC-033, once `(a,b)` is fixed they enter the mode only through their count `R_N(a,b)`. Any finer subset-sum spectrum is relevant only insofar as it yields an independent theorem controlling that occupancy as the radial threshold varies.

## Why it may matter

MC-033 says any gain must come from cross-product arithmetic/phase organization, joint cancellation across Fourier modes, or cancellation against another Huxley–Watt term. The prime-log slab coordinate isolates one exact cross-product geometry left after the product-fiber no-go: a shrinking multiplicative-partition window coupled to the same radial variable that drives the reciprocal oscillation.

If that occupancy/phase coupling has a rational-prime-specific bias, it could suggest a concrete bilinear, divisor-in-short-interval, threshold-spectrum, or generating-function estimate to attack. If it behaves like the matched multiplicative controls, the visualization supplies a clean reason to stop pursuing kernel-layer geometry and move to another surviving mechanism.

## Decisive test

First derive an analytic or frozen computational statistic that depends only on information actually retained by the mode: `mu(a)`, the scalar threshold occupancy `R_N(a,b)`, `r=ab^2/N^2`, and the required Fourier-mode range. The test must not credit differences in the internal signed-log spectrum that leave `R_N(a,b)` unchanged.

Then compare the resulting phase-conditioned occupancy statistic across increasing `N` and matched controls that preserve square-free support, multiplicativity, the prime-size profile where practical, and exact product-fiber sign coherence. Keep the direction only if a representation-stable Möbius/control separation survives scale changes and can be translated into an analytic estimate whose hypotheses are demonstrably weaker than the target Mertens bound. Kill it if the phase-conditioned occupancy remains within the matched-control scale, if the effect disappears under the frozen radial/threshold statistic, or if proving the required estimate is equivalent to assuming the original Möbius cancellation being sought.

## Evidence boundary

The persisted visualization is a finite experiment at `N=2000`. It finds **no** arithmetic-specific anomaly in the phase-free radial `omega(a)` decomposition and proves no power saving. The prime-log slab formula is an exact rewriting of the central-divisor interval in MC-033, but no useful correlation with the reciprocal phase has been established. The classical Huxley–Watt kernel and Letendre's adjacent one-sided truncated Möbius divisor sums do not by themselves supply the required paired-cutoff phase estimate. This clue proposes that residual scalar occupancy/phase correlation as the next falsifiable target rather than treating the image as evidence.

## Research disposition

Accepted in narrowed form. MC-033 already proves a decisive information quotient: for fixed `(a,b)` every admissible divisor representation has the same sign and reciprocal phase, so the Huxley–Watt annular mode sees the prime-log subset-sum geometry only through the single central-slab occupancy `R_N(a,b)`. The visually attractive idea of coupling the phase to the *fine* positions of subset sums inside that slab is therefore not a distinct retained mechanism.

The surviving question is smaller and still nontrivial: whether the **variation of the occupancy itself across rational-prime kernels and radial thresholds**, before product-collapse identities erase the cutoff defect, has a Möbius-specific signed correlation with the reciprocal Fourier family. The current proposed numerical test is not yet delegated as a compute issue because its comparison statistic and scaling criterion must be frozen more precisely; an open-ended search for an anomaly would not satisfy the compute-design gate.