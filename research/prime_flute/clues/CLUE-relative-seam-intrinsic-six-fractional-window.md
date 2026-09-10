---
id: CLUE-prime-flute-relative-seam-intrinsic-six-fractional-window
type: research-clue
status: accepted
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
---

# Does the intrinsic-six thin-seam margin survive the exact finite-seam crossover?

## Observation

PF-258--PF-260 prove that the correctly normalized thin-seam tangent

\[
H=A^{-1/4}LA^{-1/4}
\]

retains the separated fractional window needed for every strict `1<R<2`. PF-261 then reduces the exact finite-seam off-diagonal crossover to the odd-mass Green sum

\[
\langle e_i,\mathcal R_{s,r}^0e_j\rangle
=-\frac{2}{rs^2\sqrt{\kappa_i\kappa_j}}
\sum_{k\ge0}a_k^2G_{ij}(a_k),
\qquad
a_k=\frac{(2k+1)\pi}{2rs}.
\]

PF-264 identifies the sharp fixed-mass two-index Green amplitude, PF-265 makes the mass/mode recession uniform, and PF-266 proves the full coupled diagonal scale

\[
G_{ii}(a)\asymp\frac1{\mu(i+1+\mu)},
\qquad \mu=\sqrt{1+a^2}.
\]

PF-267 now closes the previously open **normalized-correlation** subgate. Exact path Green factorization plus the one-edge capacities inherited from PF-266 give

\[
\frac{G_{ij}(a)}{\sqrt{G_{ii}(a)G_{jj}(a)}}
\le
\exp\!\left[-c\sum_{m=i}^{j-1}
\min\!\left(1,\frac{\mu}{m+1}\right)\right],
\]

and therefore the sharp amplitude and a fixed positive distance-decay fraction occur in the same uniform estimate:

\[
G_{ij}(a)
\lesssim
\frac{e^{-c\Psi_{ij}(\mu)}}
{\mu\sqrt{(i+1+\mu)(j+1+\mu)}}.
\]

For `\mu` larger than the output-mode scale, PF-267 also gives the stronger path product

\[
\frac{G_{ij}}{\sqrt{G_{ii}G_{jj}}}
\lesssim
\left(\frac{C(j+1)^2}{\mu^2}\right)^{j-i}.
\]

The fixed-axis uncertainty is therefore no longer whether amplitude and recession can be correlated. It is whether their **actual odd-mass sum**, with all PF-261 coefficients and endpoint weights retained, leaves a strict supercritical mode exponent.

## Research question

After inserting PF-267's multiplicative Green estimate into the exact PF-261 odd ladder and performing the complete mass sum before any mode norm, does the resulting endpoint-weighted fixed-axis seam satisfy a uniform separated high-to-low estimate with some `R>1`?

If not, which precise coupled regime of `mu_k`, source mode, output mode, and seam scale consumes the margin? A negative answer should isolate that regime rather than reverting to the already-closed question of whether a normalized Green-correlation theorem exists.

## Why it may matter

The fixed-axis route has now passed several formerly independent gates: the intrinsic-six tangent has strict `R>1` room; the finite seam has an exact positive massive-resolvent expansion; the complete-lift Robin algebra is bounded; mass-dependent recession is uniform; the diagonal normalization is uniform; and PF-267 couples normalization and recession multiplicatively using the exact Jacobi path structure.

This makes the odd ladder itself the smallest remaining fixed-axis discriminator. A positive summed estimate would move the route from Green analysis to the actual-corridor and Robin--Poisson transport already isolated by PF-256/PF-243. A critical or negative sum would identify a genuine finite-seam obstruction despite the positive pointwise Green structure.

## Decisive test

Insert

\[
G_{ij}(a_k)
\lesssim
\frac{e^{-c\Psi_{ij}(\mu_k)}}
{\mu_k\sqrt{(i+1+\mu_k)(j+1+\mu_k)}}
\]

into PF-261's exact off-diagonal identity. Split the odd masses only according to the intrinsic scales `mu_k\lesssim i+1`, `i+1\lesssim mu_k\lesssim j+1`, and `mu_k\gtrsim j+1`, refining those cuts only if the algebra requires it. In the last regime use PF-267's stronger product bound rather than discarding path-length decay.

Carry the factors `a_k^2`, `2/(rs^2)`, and `1/sqrt(kappa_i kappa_j)` throughout. Sum over `k` first and then test the resulting separated matrix against the exact weighted `R>1` norm required by PF-243. Do not replace the odd ladder by a fixed-mass asymptotic or exchange a nonuniform mode limit with the sum.

If the fixed-axis sum closes with strict margin, propagate only the proven margin through the bounded normalized Robin source map

\[
B_{s,r}^0=X_{s,r}^0(I+(X_{s,r}^0)^*X_{s,r}^0)^{-1}
\]

and then through PF-256's actual corridor basis/hypercycle transport and PF-243's localized reassembly. If the sum is critical, identify the exact term/range responsible before introducing any stronger theorem.

## Evidence boundary

PF-267 proves the normalized path-correlation estimate and hence a genuine amplitude-times-decay Green bound uniformly in mass and mode. It does **not** perform PF-261's complete odd-mass sum or prove that the resulting fixed-axis seam has a strict `R>1` weighted operator bound.

No persisted result yet propagates a summed finite-seam estimate through the combined Robin map, transfers it to the actual `K_a` corridor, closes global weak-`S_1` reassembly, constructs a scattering/determinant identity, or establishes any statement about zeta zeros or RH.

## Research disposition

Accepted and narrowed. PF-267 resolves the normalized Green-correlation subproblem positively. The active fixed-axis discriminator is now **the exact odd-mass summation of the multiplicative PF-267 Green bound, including endpoint weights and seam-scale prefactors; only the margin surviving that sum is eligible for transport to the actual corridor and Robin--Poisson reassembly**.