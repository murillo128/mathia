---
id: CLUE-prime-flute-relative-seam-intrinsic-six-fractional-window
type: research-clue
status: resolved
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/findings/PF-256-variable-corridor-graph-equivalence-transfers-two-derivative-locality-to-the-actual-transverse-scale.md
  - research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform.md
  - research/prime_flute/findings/PF-258-thin-seam-relative-edge-is-a-linearly-weighted-jacobi-tangent-with-intrinsic-dimension-six.md
  - research/prime_flute/findings/PF-259-intrinsic-six-tangent-has-anchored-gaussian-large-time-control.md
  - research/prime_flute/findings/PF-260-davies-gaffney-closes-short-time-intrinsic-six-fractional-window.md
  - research/prime_flute/findings/PF-261-finite-seam-crossover-is-a-bounded-positive-mixture-of-massive-axis-resolvents.md
  - research/prime_flute/findings/PF-264-fixed-mass-green-kernel-has-universal-two-index-leading-law.md
  - research/prime_flute/findings/PF-265-unbounded-gap-combes-thomas-makes-mass-mode-green-decay-uniform.md
  - research/prime_flute/findings/PF-266-diagonal-capacity-recovers-uniform-mass-mode-green-amplitude.md
  - research/prime_flute/findings/PF-267-path-green-correlations-multiply-and-recover-uniform-amplitude-decay.md
  - research/prime_flute/findings/PF-268-lowest-finite-seam-pole-forbids-bare-supercritical-separated-weighting.md
---

# Does the intrinsic-six thin-seam margin survive the exact finite-seam crossover?

## Observation

PF-258--PF-260 prove that the correctly normalized thin-seam tangent

\[
H=A^{-1/4}LA^{-1/4}
\]

retains the separated fractional window needed for every strict `1<R<2`. PF-261 then reduces the exact finite-seam off-diagonal crossover to the positive odd-mass Green sum

\[
\langle e_i,\mathcal R_{s,r}^0e_j\rangle
=-\frac{2}{rs^2\sqrt{\kappa_i\kappa_j}}
\sum_{k\ge0}a_k^2G_{ij}(a_k),
\qquad
a_k=\frac{(2k+1)\pi}{2rs}.
\]

PF-264 identifies the fixed-mass two-index Green asymptotic, PF-265--PF-266 make recession and amplitude uniform in mass, and PF-267 proves the missing multiplicative normalized-correlation estimate. This originally left the complete odd-mass summation as the smallest apparent fixed-axis discriminator.

PF-268 now shows that this discriminator has a decisive negative answer **for the naked relative seam**. At every fixed `s>0`, the first pole `a_0` alone has, on proportional same-parity separated mode blocks, the endpoint-normalized lower bound

\[
|\langle e_{2i+\varepsilon},\mathcal R_{s,r}^0e_{2j+\varepsilon}\rangle|
\gtrsim_{r,s,\varepsilon} N^{-2}
\]

when `i\asymp N` and `j\asymp N` with `j/i` bounded away from one. Because every pole has the same sign, higher masses cannot cancel this floor. A positive block witness then makes the separated map with input weight `N^R`, or equivalently `(K_s^0)^R` up to the fixed seam-scale factor, unbounded for every `R>1`.

## Research question

The original question was whether inserting PF-267's multiplicative Green estimate into the complete PF-261 odd ladder and summing masses before taking the endpoint-weighted mode norm could preserve some strict `R>1` margin.

PF-268 resolves that question negatively for `\mathcal R_{s,r}^0` itself. The remaining live question is different and should not be confused with this clue: can the **combined polar-free Robin source map and spatially separated Robin--Poisson propagation** suppress or reorganize the fixed-pole proportional-mode floor strongly enough to recover `R>1` only after those physical operations are included?

## Why it may matter

The negative result identifies an order-of-limits obstruction rather than a missing Green estimate. The thin-seam tangent retains `1<R<2` when `s\downarrow0` at fixed modes, but for every fixed finite `s` the arbitrarily-high-mode limit sees the first massive pole and an order-minus-two proportional-ray kernel. Therefore no uniform argument may transfer the tangent margin to the bare finite seam merely by strengthening the mass summation.

This materially redirects effort toward the structure already isolated by PF-257 and PF-243: the physical Robin factor is a combined rational transform rather than the positive relative seam alone, and the one-sided Poisson leg places a positive spatial propagation distance before the final weighted estimate.

## Decisive test

The decisive test for this clue is complete. PF-268 uses PF-261 positivity plus PF-264's fixed-mass asymptotic to retain only the first odd pole, obtains an `N^{-2}` lower floor on proportional separated blocks, and applies a normalized positive block vector to prove growth `N^{R-1}` for every `R>1`.

Any future route seeking supercritical smoothing must therefore insert the finite-seam operator into the combined Robin/Poisson structure **before** imposing the `R>1` weighted bound. Re-estimating the higher-mass tail of the naked seam cannot change the PF-268 lower bound.

## Evidence boundary

PF-268 proves only a no-go for the bare fixed-axis relative seam `\mathcal R_{s,r}^0` with a separated supercritical input weight. It does not prove failure of

\[
B_{s,r}^0=X_{s,r}^0(I+(X_{s,r}^0)^*X_{s,r}^0)^{-1},
\]

of the reflection transforms, or of PF-243's source-to-bulk maps after positive spatial separation. It also does not transfer a negative conclusion to the actual variable corridor, global weak-`S_1` reassembly, scattering/determinant identities, zeta zeros, or RH.

The linked PF-268 finding, not this clue, is the mathematical evidence.

## Research disposition

Outcome: refuted

Resolved by:
- [[research/prime_flute/findings/PF-268-lowest-finite-seam-pole-forbids-bare-supercritical-separated-weighting]]

The original bare-seam `R>1` target is false. The surviving route must test the combined Robin transform and spatially separated Poisson propagation rather than continue the odd-mass summation as an isolated smoothing gate.