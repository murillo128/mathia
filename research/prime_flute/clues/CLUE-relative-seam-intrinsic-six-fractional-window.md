---
id: CLUE-prime-flute-relative-seam-intrinsic-six-fractional-window
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window.md
  - research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform.md
  - research/prime_flute/findings/PF-258-thin-seam-relative-edge-is-a-linearly-weighted-jacobi-tangent-with-intrinsic-dimension-six.md
  - research/prime_flute/findings/PF-259-intrinsic-six-tangent-has-anchored-gaussian-large-time-control.md
  - research/prime_flute/findings/PF-260-davies-gaffney-closes-short-time-intrinsic-six-fractional-window.md
  - research/prime_flute/clues/CLUE-critical-jacobi-square-root-decay-window.md
---

# Does the intrinsic-six thin-seam tangent retain a supercritical fractional smoothing window?

## Observation

PF-258 corrects the fixed-axis bridge between PF-253 and PF-257. In the canonical thin-seam scaling `w=rs`, the positive relative seam does not tend to the bounded PF-247 Jacobi operator `J`; it tends instead to

\[
H=A^{-1/4}LA^{-1/4}=A^{1/4}JA^{1/4}.
\]

Each parity block is still nearest-neighbor, but after the exact PF-251 zero-mode ground-state transform it has reversible mass and conductance

\[
m_j\asymp(j+1)^2,
\qquad
c_j\asymp(j+1)^3.
\]

Its canonical intrinsic edge scale is therefore `\ell_j\asymp(j+1)^{-1/2}`, so `\rho(0,j)\asymp\sqrt{j+1}` and the reversible mass of an origin-centered intrinsic ball grows like `R^6`. The jump rates `c_j/m_j\asymp j` are unbounded, so PF-253's bounded-rate lazy-chain proof cannot be transplanted verbatim.

PF-259 proves intrinsic Poincare/Sobolev control and the predicted `R<3/2+\sigma` window for the large-time Balakrishnan contribution. PF-260 then applies the sharp intrinsic Davies--Gaffney--Grigor'yan estimate directly to the same unbounded-rate graph and proves that the complementary short-time contribution is superalgebraically local in the separated cone. Therefore the **full fixed-axis** `H^\sigma` upper estimate now has the sufficient window `R<3/2+\sigma`; at `\sigma=1/2`, every strict `1<R<2` survives.

PF-257 nevertheless needs the physical combined Robin transform, not locality of a naked polar factor. The fixed-axis route-admission question is now positive; the live obstruction has moved to uniform finite-`s` crossover and actual-corridor transfer.

## Research question

For the exact parity blocks of

\[
H=A^{1/4}JA^{1/4},
\]

can one prove a sharp separated high-to-low estimate for `H^\sigma`, especially `\sigma=1/2`, strong enough that the corresponding thin-seam combined Robin transform retains some uniform boundary-weight exponent `R>1`?

The upper half of this question is now established. PF-259 and PF-260 prove

\[
|\langle e_i,H^\sigma e_j\rangle|
\lesssim
(i+1)(j+1)^{-2-\sigma}
\qquad (j\ge2i+2),
\]

and hence the sufficient Hilbert--Schmidt window

\[
R<\frac32+\sigma.
\]

At `\sigma=1/2` this gives `1<R<2`. What remains unproved at fixed axis is **sharpness**: there is no matching lower bound showing that `R=3/2+\sigma` is the actual threshold. For the current Prime-Flute route, however, existence of a strict `R>1` window is the relevant admission gate; the higher-leverage unresolved problem is its survival through finite `s` and the actual corridor.

## Why it may matter

PF-253 gives a generous square-root window `R<3` for `J`, but PF-258 shows that this is not the operator actually seen by the thin-seam relative normalization. PF-259/PF-260 now show that paying the correct quarter-order `A` sandwich still leaves a strict `R>1` fixed-axis margin. The Jacobi/Robin route therefore survives its corrected tangent test instead of failing at high energy.

This materially changes allocation. Further fixed-axis heat-kernel work is no longer the critical route gate unless sharpness becomes independently useful. The next effort should test whether the finite-`s` relative seam and then the actual `K_a` corridor preserve any part of the proven `1<R<2` square-root margin.

## Decisive test

The fixed-axis stage has succeeded at the level needed for route admission. PF-259 verifies the intrinsic large-scale geometry and large-time fractional estimate; PF-260 supplies the missing short-time/high-energy locality by an intrinsic DGG estimate that explicitly permits unbounded graph Laplacians.

The decisive next stage is therefore the finite-`s` relative seam

\[
\mathcal R_{s,r}^0=s^{-1}A^{-1/4}f_{rs}(L)A^{-1/4},
\qquad
f_w(\lambda)=\sqrt\lambda\tanh(w\sqrt\lambda).
\]

PF-258's finite-dimensional `O(s^2)` tangent error is not uniform in the growing high-frequency window. Control the crossover `rs\sqrt L\sim1` strongly enough to retain some uniform exponent `R>1`; do not infer a weighted estimate from strong-resolvent or finite-dimensional convergence. The relevant object is the combined normalized relative-seam/Robin transform from PF-257, not a naked polar factor.

Only after that finite-`s` test succeeds should the margin be transferred through PF-256's actual corridor basis, PF-255's hypercycle transport, reflection factors, and PF-243's separated Robin--Poisson factorization. The already-accepted `CLUE-robin-homotopy-separated-poisson-shear-estimate.md` owns the downstream actual-seam smoothing target.

Kill the route if the finite-`s` crossover or actual-corridor transfer destroys every strict `R>1` window. A failure can no longer be attributed merely to unbounded short-time propagation of the fixed-axis intrinsic-six tangent.

## Evidence boundary

PF-258 establishes the thin-seam tangent `H`, its linearly weighted Jacobi coefficients, the exact transformed zero mode, the `(m_j,c_j)\asymp(j^2,j^3)` reversible geometry, and the intrinsic `R^6` volume law. PF-259 establishes the exact speed-measure time-change relation to PF-252, intrinsic Poincare and Sobolev control, a Keller--Rose anchored Gaussian upper bound for sufficiently large times, and the predicted separated `R<3/2+\sigma` window for the large-time/low-energy Balakrishnan contribution. PF-260 establishes superalgebraic separated locality of the short-time/high-energy contribution and consequently the same **full fixed-axis upper window**.

None of these findings proves a matching lower bound or sharpness of `R=3/2+\sigma`. More importantly, they do not establish a uniform weighted estimate for finite `s`, the `rs\sqrt L\sim1` crossover, the actual `K_a` corridor, or PF-243's separated Robin--Poisson map. PF-253's Bessel-four theorem remains exact for `J` but is not a theorem about `H`; PF-257's polar-free algebra remains exact on bounded regularizations but does not by itself transfer fixed-axis locality through finite `s`.

Nothing in this clue proves trace-class shear reassembly, finite-pant completion, scattering/determinant statements, a zeta-zero statement, or RH.

## Research disposition

Accepted. PF-259 and PF-260 complete the fixed-axis **upper** test strongly enough for the route: at `\sigma=1/2`, the full tangent retains every `1<R<2`, and short-time/high-energy propagation imposes no polynomial separated-weight ceiling. Sharpness of the fixed-axis threshold remains open but is no longer the highest-leverage discriminator.

The active test is now finite-`s` survival of some strict `R>1` margin through the normalized relative seam, followed by the actual-corridor/Robin--Poisson transfer already isolated by `CLUE-robin-homotopy-separated-poisson-shear-estimate.md`.