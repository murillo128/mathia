# VIS-018 — phase winding is divisor count

## Claim

Let `F` be meromorphic on a neighborhood of a positively oriented simple closed contour `gamma` and its interior, with no zero or pole on `gamma`. Let `N_gamma` and `P_gamma` denote the numbers of zeros and poles inside `gamma`, counted with multiplicity. Then

`Delta_gamma arg F = 2 pi (N_gamma - P_gamma)`.

Equivalently, the winding number of the image curve `F(gamma)` around the origin is exactly the divisor count `N_gamma-P_gamma`.

For an entire function such as the completed Riemann `xi` function there are no poles, so contour phase winding is exactly the number of enclosed zeros, counted with multiplicity. Around a zero `rho` of multiplicity `m`, the local phase vortex has charge `m`.

**Evidence/status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + DECISIVE-NEGATIVE/BASELINE`.

The Mathia consequence is negative but useful: once the zero divisor is already retained, complete contour hue circulation, domain-coloring vortex charge, or any equivalent winding-number rendering does not define an independent visual information channel.

## Exact derivation

The argument principle gives

`(1/(2 pi i)) integral_gamma F'(z)/F(z) dz = N_gamma - P_gamma`.

Along a parametrization `z=z(t)` of `gamma`, where `F(z(t))` never vanishes,

`d/dt log F(z(t)) = (F'(z(t))/F(z(t))) z'(t)`.

Taking imaginary parts and integrating once around the contour yields the total unwrapped phase change,

`Delta_gamma arg F = Im integral_gamma F'(z)/F(z) dz = 2 pi (N_gamma-P_gamma)`.

The local statement follows from the ordinary zero factorization. If `rho` is a zero of multiplicity `m`, then near `rho`

`F(z) = (z-rho)^m G(z)`

with `G` holomorphic and nonzero. On a sufficiently small positive circle around `rho`, the first factor contributes exactly `m` turns of phase while `G` has zero winding. Thus the local vortex charge is precisely the multiplicity.

For `xi`, which is entire, `P_gamma=0`; therefore every contour winding number is completely determined by which zeros, with what multiplicities, lie inside the contour.

## What this closes

A natural visual escape after the modulus/phase and overlap-gluing baselines was to treat the topology of phase portraits as extra structure: count hue rotations around contours, identify vortices in a domain-coloring image, compare signed circulation between nested curves, or watch the winding jump as a contour moves.

For a single holomorphic or meromorphic field these quantities reduce exactly to the divisor already being visualized. Continuous contour deformations that cross no zero or pole leave the integer unchanged. When a zero crosses the contour, the jump is its multiplicity; when a pole crosses, the jump has the opposite sign.

Therefore the following are not independent invariants once the divisor is known:

- total unwrapped phase change around a closed contour;
- winding of `F(gamma)` about zero;
- local domain-coloring vortex charge;
- changes of those integers under contour deformation.

This does not make phase visualization useless. It makes the information accounting explicit: the topological part of the phase portrait is the divisor in another coordinate system.

## Visual inspection

The retained artifact

`research/visual_exploration/visualizations/phase-winding-argument-principle.md`

uses the explicit control polynomial

`F(z)=(z-z_1)(z-z_2)(z-z_3)`

with three simple zeros and three circular contours enclosing one, two, and three of them. Direct numerical unwrapping of the phase finishes at one, two, and three turns respectively.

The image is explanatory only. The finding is established by the exact argument principle, not by numerical agreement.

## Prior art and novelty assessment

This is classical complex analysis. The standard winding-number form is recorded, for example, in the **Encyclopedia of Mathematics**, *Argument, principle of the*:

https://encyclopediaofmath.org/wiki/Argument%2C_principle_of_the

There the total change of argument divided by `2 pi` is identified with the number of zeros minus poles inside the contour, counted with multiplicity. No novelty is claimed for the theorem, local vortex interpretation, or contour-deformation invariance.

The durable Mathia contribution is the specialization as a visual negative control: after zero locations and multiplicities have already been counted as source data, phase-winding topology cannot be promoted as a separate mesoscopic zeta signal.

## Boundary conditions and falsification

The contour must avoid zeros and poles. For a meromorphic function the correct quantity is zeros minus poles; applying the statement directly to `zeta(s)` therefore requires accounting for its pole at `s=1`. Using the completed entire `xi` function removes that bookkeeping issue.

The result closes only **topological phase circulation**. It does not say that the full phase function along a contour is determined by the divisor alone without the regular holomorphic factor. It does not close phase-speed fluctuations, cross-contour phase correlations, sparse or incomplete phase measurements, non-holomorphic derived fields, or observables in which some zero/boundary information has deliberately been withheld.

Any future phase candidate must therefore state what information it retains beyond the integer winding and must survive a control in which the same divisor count is preserved.

## Research consequence

The accepted `CLUE-zeta-critical-strip-multiscale-geometry` has now lost another apparent escape. `VIS-013`–`VIS-015` classify complete concentric log-modulus shells as zero sources plus harmonic boundary data. `VIS-016` and `VIS-017` close complete local phase reconstruction and connected overlap gluing up to a global phase. `VIS-018` now closes the topological winding/vortex part of phase portraits as the divisor count itself.

The live question is narrower: whether zeta's zero configuration has a source-sensitive higher-order organization that survives matched point-process controls, or whether an explicitly incomplete or separated measurement geometry exposes a nontrivial bridge not already forced by ordinary complex analysis.

A future visual phase construction should be rejected quickly if its apparent invariant can be computed from zero multiplicities by the argument principle.
