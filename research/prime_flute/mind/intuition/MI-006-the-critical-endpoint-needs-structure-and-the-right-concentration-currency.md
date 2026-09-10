# MI-006 — The corrected intrinsic-six seam tangent retains a supercritical fixed-axis margin

**Evidence level:** exact Jacobi/Robin normalization, intrinsic-six ground-state geometry, anchored Gaussian control, and Davies--Gaffney fractional smoothing through PF-260

## Core intuition

The critical local geometry survives a substantial correction. The physical first-order corridor normalization does not expose the bounded Bessel-four operator `J` directly; it exposes the unbounded quarter-order sandwich `H=A^{-1/4}LA^{-1/4}`. Yet the resulting intrinsic-six graph still has enough off-diagonal locality for the square-root route.

Thus the fixed-axis smoothing gate is now positive in the form actually relevant to the thin seam. The remaining risk is stable transport of that margin through finite seam scale, the actual variable corridor, and the combined physical Robin map.

## Strongest justified principle

PF-253 gives the sharp Bessel-four fractional window for `J`, while PF-255--PF-256 show that hypercycle reparameterization and the actual corridor spectral change preserve two derivatives of high-to-low locality. PF-257 identifies the physical normalized Robin injection as the combined polar-free transform `(I+XX*)^{-1}X=X(I+X*X)^{-1}` rather than a naked polar factor.

PF-258 corrects the bridge between these results. For seam width `w=rs`, the dimensionless fixed-axis relative seam tends to `rH` with `H=A^{-1/4}LA^{-1/4}`. After the exact ground-state transform, `m_j~(j+1)^2`, `c_j~(j+1)^3`, intrinsic edge length is `~(j+1)^(-1/2)`, and origin-centered volume grows like `R^6`; jump rates are unbounded, so the Bessel-four lazy-chain argument cannot simply be reused.

PF-259 proves intrinsic Poincare/Sobolev control and the required large-time fractional decay. PF-260 closes the short-time/high-energy gap using intrinsic Davies--Gaffney--Grigor'yan locality for the unbounded graph. Together they give `|<e_i,H^sigma e_j>| \lesssim (i+1)(j+1)^(-2-sigma)` for separated indices and the sufficient Hilbert--Schmidt window `R<3/2+sigma`. At `sigma=1/2`, every strict `1<R<2` survives for the full fixed-axis tangent.

## Program consequence

Spend this **proved but smaller** margin on the actual transport problem. Control the finite-`s` crossover `rs sqrt(L)~1` uniformly in the growing corridor, then transfer some strict `R>1` exponent through `K_a`, hypercycle coordinates, reflection/Robin--Poisson factors, and the complete-lift/global reassembly. Estimate the combined normalized Robin transform directly rather than a naked polar factor.

## Counterevidence / boundary

The fixed-axis result is an upper window, not a matching sharp threshold, and it says nothing uniform about finite `s`. Strong/form convergence of the relative seam does not imply weighted high-to-low control on a growing spectral window. The actual corridor and final weak-`S_1` assembly remain separate gates.

## Epistemic status

**Corrected fixed-axis seam geometry with a proved supercritical square-root window `1<R<2`; uniform finite-seam and assembled physical transport remain open.**

## Falsification criterion

Invalidate the thin-seam tangent, intrinsic-six heat-kernel estimates, or full fixed-axis fractional bound; or show that every strict `R>1` exponent is destroyed uniformly by the finite-`s` crossover or actual corridor. A positive continuation should preserve a nonzero part of the fixed-axis margin through the physical transform.
