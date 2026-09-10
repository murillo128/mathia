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
---

# Does the intrinsic-six thin-seam margin survive the exact finite-seam crossover?

## Observation

PF-258--PF-260 show that the correctly normalized thin-seam tangent

\[
H=A^{-1/4}LA^{-1/4}
\]

retains the fixed-axis separated fractional window needed for every strict `1<R<2`. PF-261 then identifies the finite-seam crossover exactly: its off-diagonal Gegenbauer entries are an odd-mass sum of Green matrices

\[
G_{ij}^{(\varepsilon)}(a)
=\langle e_i,(L_\varepsilon+a^2)^{-1}e_j\rangle,
\qquad
a_k=\frac{(2k+1)\pi}{2rs}.
\]

PF-264 gives the sharp fixed-mass law `G_{ij}\sim(2\mu\sqrt{ij})^{-1}(i/j)^\mu`. PF-265 makes the off-diagonal recession uniform in the coupled mass/mode regime through the metric

\[
\Phi_{ij}(\mu)
=\sum_{m=i}^{j-1}\min\left(1,\frac{c_p\mu}{m+1}\right),
\qquad \mu=\sqrt{1+a^2},
\]

but with the coarse all-mass prefactor `O(\mu^{-2})`.

PF-266 now closes the separate diagonal-amplitude discriminator. Uniformly in parity, mass, and mode,

\[
G_{ii}^{(\varepsilon)}(a)
\asymp\frac1{\mu(i+1+\mu)},
\]

and positive-resolvent Cauchy--Schwarz gives

\[
|G_{ij}^{(\varepsilon)}(a)|
\lesssim
\frac1{\mu\sqrt{(i+1+\mu)(j+1+\mu)}}.
\]

Thus the coupled transition has **no hidden diagonal amplitude blow-up**: when the modes dominate the mass this recovers the missing `1/(\mu\sqrt{ij})` factor uniformly, while the large-mass regime crosses automatically to `O(\mu^{-2})`. What remains is to keep enough of that amplitude correlated with PF-265's distance decay when the odd ladder is summed.

## Research question

Does the rigorous joint envelope

\[
|G_{ij}^{(\varepsilon)}(a)|
\le
\min\left\{
\frac{C}{\mu\sqrt{(i+1+\mu)(j+1+\mu)}},
\frac4{\mu^2}e^{-\Phi_{ij}(\mu)}
\right\}
\]

already suffice, after summing the **actual** PF-261 odd masses and inserting the outer `A^{-1/4}` endpoint weights, to retain a uniform separated high-to-low exponent `R>1`?

If the minimum loses exactly the critical power, can one prove a normalized one-dimensional Green-correlation estimate

\[
\frac{|G_{ij}^{(\varepsilon)}(a)|}
{\sqrt{G_{ii}^{(\varepsilon)}(a)G_{jj}^{(\varepsilon)}(a)}}
\lesssim e^{-c\Phi_{ij}(\mu)}
\]

for some fixed `c>0`? Together with PF-266 this would place the sharp mode amplitude and a positive fraction of PF-265's recession in the same bound rather than interpolating between two unrelated estimates.

## Why it may matter

The fixed-axis obstruction has narrowed substantially. The tangent window is positive, the complete-lift finite-seam operator and polar-free Robin algebra are closed, the nonlinear crossover has an exact massive-resolvent expansion, resonance is harmless, the fixed-mass normalization is known, the mass-dependent decay metric is uniform, and the missing diagonal amplitude is now uniform as well.

The remaining distinction is load-bearing rather than cosmetic. PF-261 needs the odd ladder summed **before** the weighted operator norm, and PF-243 ultimately requires a strict `R>1` margin. If the minimum envelope already sums with that margin, no stronger Green theorem is needed. If it lands exactly at the critical threshold, the normalized-correlation estimate isolates the smallest stronger theorem that can couple the two pieces already proved.

## Decisive test

Insert PF-265/PF-266's minimum envelope into PF-261's exact off-diagonal identity and split the odd masses only according to the regimes where the amplitude bound or the Combes--Thomas bound is smaller. Perform the complete `k`-sum first, then test the resulting separated matrix against the required weighted `R>1` norm. Do not replace the odd ladder by a fixed-mass asymptotic or interchange a nonuniform limit with the sum.

If this closes a strict margin, propagate only that surviving margin through the combined bounded source map

\[
B_{s,r}^0=X_{s,r}^0(I+(X_{s,r}^0)^*X_{s,r}^0)^{-1}
\]

and only afterwards through PF-256's actual corridor basis, the hypercycle transport, reflection factors, and PF-243 reassembly.

If the minimum is critical, prove or refute the normalized-correlation estimate above using the one-dimensional parity recurrence, Weyl/Green factorization, a ground-state/Dirichlet-form argument, or a sharpened weighted resolvent conjugation. A weaker theorem is acceptable if its **summed** consequence still leaves some strict `R>1` room.

Kill the fixed-axis route only if the actual summed Green kernel, or the combined Robin transform built from it, defeats every strict `R>1` bound. Failure to retain the full PF-264 exponent coefficient is not enough by itself.

## Evidence boundary

PF-266 proves the two-sided diagonal scale and the uniform Cauchy--Schwarz amplitude. PF-265 proves the independent all-mass/all-mode Combes--Thomas envelope. Neither finding proves that the sharp amplitude multiplies the distance factor, and simple interpolation between them necessarily spends part of one gain to retain part of the other.

No persisted result yet sums the complete PF-261 odd ladder in the required weighted operator norm, proves strict `R>1` finite-seam smoothing, propagates such a bound through the combined Robin map, or transfers it to the actual `K_a` corridor and global flute reassembly. Nothing here establishes a scattering/determinant identity, a statement about zeta zeros, or RH.

## Research disposition

Accepted and narrowed. The diagonal amplitude transition is resolved positively by PF-266. The active discriminator is now **operator-level odd-mass summation of the rigorous PF-265/PF-266 joint envelope; only if that is critical should research strengthen it to a normalized Green-correlation estimate coupling amplitude and recession**.