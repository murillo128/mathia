---
id: CLUE-mobius-cancellation-reciprocal-phase-prime-log-slab-coupling
type: research-clue
status: proposed
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

over coprime square-free `a,b` with `N<ab^2<=N^2`, `r=ab^2/N^2 in I`, and `omega(a)=k`, so that the annular mode is `sum_k (-1)^k A_{N,h,k}`. Determine whether a finer version retaining the signed-log subset-sum spectrum of `a`, not just `k`, has a stable relation to the radial phase that is absent for matched random multiplicative controls and is analytically exploitable without assuming Mertens-scale cancellation.

## Why it may matter

MC-033 says any gain must come from cross-product arithmetic/phase organization, joint cancellation across Fourier modes, or cancellation against another Huxley–Watt term. The prime-log slab coordinate isolates one exact cross-product geometry left after the product-fiber no-go: a shrinking multiplicative-partition window coupled to the same radial variable that drives the reciprocal oscillation.

If that coupling has a rational-prime-specific bias, it could suggest a concrete bilinear, divisor-in-short-interval, subset-sum, or generating-function estimate to attack. If it behaves like the matched multiplicative controls, the visualization supplies a clean reason to stop pursuing kernel-layer geometry and move to another surviving mechanism.

## Decisive test

Compute phase-conditioned slab statistics for increasing `N` and for the relevant range of Fourier modes `h`, using controls that preserve square-free support, multiplicativity, the empirical prime-size profile where practical, and exact product-fiber sign coherence. Track both the full annular sum and conditional statistics at fixed radial windows and fixed `omega(a)`.

Keep the direction only if a representation-stable Möbius/control separation survives scale changes and can be translated into an analytic estimate whose hypotheses are demonstrably weaker than the target Mertens bound. Kill it if the phase-conditioned profiles remain within the matched-control scale, if the effect disappears under reasonable radial/binning changes, or if proving the required estimate is equivalent to assuming the original Möbius cancellation being sought.

## Evidence boundary

The persisted visualization is a finite experiment at `N=2000`. It finds **no** arithmetic-specific anomaly in the phase-free radial `omega(a)` decomposition and proves no power saving. The prime-log slab formula is an exact rewriting of the central-divisor interval in MC-033, but no useful correlation with the reciprocal phase has been established. This clue proposes that correlation as the next falsifiable test rather than treating the image as evidence.
