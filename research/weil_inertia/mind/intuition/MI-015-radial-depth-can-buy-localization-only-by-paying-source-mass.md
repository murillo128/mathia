# MI-015 — Radial depth trades directly against localization in the Weil screen

**Evidence level:** exact depth-split screen inequality and inherited weighted-source tariffs through WI-227

## Core intuition

The earlier `Theta(M)` scalar localization barrier is a statement about paying for the whole remote screen from one global mass budget. Once screening mass is separated by horizontal/radial depth first, a sharper alternative appears: shallow mass is forced much closer to the bow, while avoiding that localization requires the screen to move outward in depth and pay the corresponding source weight.

The relevant resource is therefore a **depth-versus-localization trade**, not one universal detector radius.

## Strongest justified principle

WI-218--WI-223 show that remote cancellation is expensive in channel rank and radial-weighted source mass. WI-224--WI-225 prove that a normalized fixed-support scalar detector which must beat the full polynomial mass budget needs natural-frequency cutoff `Theta(log T)`, corresponding to physical radius `Theta(M)`.

WI-227 changes the accounting order. Split mirror-pair screening mass at radial parameter `a=A`. For every fixed reciprocal harmonic, either the deep sector carries `Omega(M)` weighted mass `sum mu_rho cosh(k a_rho)`, or the shallow sector carries `Omega(M)` weighted mass inside ordinate radius `O((A+1)M/log T)`. Thus uniformly bounded depth returns the source to the original bow scale, and any screen with all `a=o(log T)` is forced into `o(M)` physical reach. The known sparse finite-harmonic controls escape precisely by using `a~log M`, i.e. macroscopic radial depth.

## Program consequence

Use the dichotomy rather than another scalar-window optimization. In the shallow branch, combine bow-scale localization with rank/count/multiplicity information. In the deep branch, price how many zeros with what coefficients can afford the `cosh(k a)` tariff under the source normalization. A successful theorem must show that one of these branches is impossible for an actual zeta screen.

## Counterevidence / boundary

WI-227 still measures scalar radial-weighted mass; it permits concentration on a few zeros with large coefficients and does not itself yield a zero-count contradiction. The localization radius grows with the chosen depth threshold `A`, and macroscopic-depth screens remain allowed. Source-specific sign, phase, covariance or coefficient constraints may be needed to close either branch.

## Epistemic status

**Exact depth/localization alternative that recovers bow-scale localization for shallow screens and forces macroscopic radial depth on evasive screens; conversion to an impossible zeta zero budget remains open.**

## Falsification criterion

Construct a screen satisfying the inherited cancellation hypothesis that simultaneously avoids `Omega(M)` deep weighted mass and avoids the stated shallow localization, or invalidate the per-frequency shell counting used by WI-227. A positive continuation should convert one side of the dichotomy into a zeta-specific contradiction.
