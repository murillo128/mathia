# MI-032 — Canonical Green slicing can select universal Hilbert criticality without selecting zeros

**Evidence level:** exact/classical-mechanism synthesis from [PC-316](../../findings/PC-316-cross-level-poisson-products-generate-mordell-tornheim-packets.md), [PC-319](../../findings/PC-319-small-mordell-tornheim-coupling-preserves-off-critical-zeros.md)--[PC-321](../../findings/PC-321-large-mordell-tornheim-exponent-is-zero-free-on-right-polyhalfplane.md), and [PC-322](../../findings/PC-322-canonical-green-slice-is-classical-hilbert-criticality.md).

The canonical cross-level field of PC-316 contains a continuous additive exponent `u` through `(k+l)^(-u)`. PC-319--PC-321 show that its two easy limits fail oppositely: off-critical zeros persist near `u=0`, while sufficiently large `Re u` isolates the unique lowest output mode and removes zeros from the right polyhalf-plane.

PC-322 identifies a non-fitted intermediate value. Ordinary downstream Green inversion integrates the additive semigroup once and therefore forces

`u=1`,  so the kernel is  `K_1(k,l)=1/(k+l)`.

This is not just another arbitrary slice. For real `u>0`, `K_u=(k+l)^(-u)` has an exact `ell^2` transition: it is unbounded for `0<u<1`, bounded noncompact at `u=1`, and Hilbert--Schmidt for `u>1`. Thus the original geometry canonically lands on a genuine operator-critical point.

But the critical point is universal. Writing the `u=1` Mordell--Tornheim packet as the Hilbert bilinear form between periodic Dirichlet vectors `v_a(s)=(a(k)k^(-s))`, every nonzero periodic source satisfies

`v_a(s) in ell^2  iff  Re(s)>1/2`.

The divergence at `Re(s)=1/2` depends only on the positive mean of `|a(k)|^2`, so arbitrary non-arithmetic periodic controls have the same boundary. The canonical source changes the vector inside the Hilbert space, not the location of the Hilbert-space threshold.

The reusable distinction is therefore stronger than “a critical exponent is not a proof.” A construction may **canonically select both an intermediate coupling and a `1/2` boundary**, yet still obtain them from source-independent operator geometry. Canonicality removes parameter fitting; it does not supply arithmetic selectivity or turn a matrix coefficient's zeros into the spectrum of the underlying operator.

Any continuation of this packet route must expose a zero-sensitive object beyond the Hilbert threshold itself: for example a source-forced relation among matrix coefficients, a determinant/quotient with independently analyzed divisor, or another mechanism whose matched periodic controls do not share the same critical geometry. Merely showing that the Green slice is natural, noncompact, or critical at one half repeats classical Hilbert-space structure.

**Boundary.** PC-322 does not determine the zero set of `Z_(5,7)(s,t,1)`, rule out every other intermediate `0<u<5`, or prove that every nonlinear completion classicalizes. It closes only the inference from the canonical Green choice and its universal `ell^2` boundary to RH-style zero selection.
