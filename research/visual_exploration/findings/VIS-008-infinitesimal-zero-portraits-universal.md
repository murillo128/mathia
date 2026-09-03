# VIS-008 — Infinitesimal zero portraits are universal up to multiplicity

## Claim

Let `f` be holomorphic in a neighborhood of `rho`, and suppose `rho` is a zero of exact multiplicity `m>=1`. Put

`a_m = f^(m)(rho)/m! != 0`

and, for `r>0`, define the translated and Taylor-normalized zoom

`F_r(z) = f(rho + r z)/(a_m r^m)`.

For every fixed `R>0`, as `r -> 0+`,

`F_r(z) -> z^m`

uniformly on `|z|<=R`. More precisely, for sufficiently small `r` there is a constant `C_R` such that

`sup_{|z|<=R} |F_r(z)-z^m| <= C_R r`.

On every fixed annulus `eta<=|z|<=R`, `eta>0`, the normalized modulus and phase also converge uniformly to the universal multiplicity-`m` template:

`log|F_r(z)| - m log|z| = O_{eta,R}(r)`,

and, after choosing the continuous argument branch near `1`,

`arg F_r(z) - m arg z = O_{eta,R}(r)  (mod 2pi)`.

Therefore an infinitesimal domain-coloring, phase, level-set, or modulus portrait around an isolated analytic zero, after removing translation and the leading Taylor coefficient, contains no information about the ambient function beyond the zero multiplicity. In particular, the infinitesimal normalized shape around a Riemann-zeta zero cannot by itself distinguish a zero on the critical line from a hypothetical off-line zero of the same multiplicity.

**Evidence/status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + VISUAL-TO-EXACT + DECISIVE-NEGATIVE`.

This is a local complex-analysis obstruction, not a new theorem about zeta zeros and not an RH criterion.

## Exact derivation

By the definition of a zero of order `m`, factor the Taylor series as

`f(rho+w) = a_m w^m h(w)`,

where `h` is holomorphic near `0` and `h(0)=1`. Hence

`F_r(z) = z^m h(rz)`.

Fix `R`. On a sufficiently small closed disk around `0`, `h'` is bounded by some `M`. For `rR` inside that disk,

`|h(rz)-1| <= M r |z|`.

Thus

`|F_r(z)-z^m| = |z|^m |h(rz)-1| <= M R^(m+1) r`,

which gives uniform convergence with an explicit `O_R(r)` bound.

For `eta<=|z|<=R`, division by `z^m` gives

`F_r(z)/z^m = h(rz) -> 1`

uniformly. For sufficiently small `r`, this ratio stays in a simply connected neighborhood of `1` that avoids `0`, so a holomorphic logarithm is available there. Since `log h(rz)=O_R(r)`, its real and imaginary parts give the stated modulus and phase estimates. The apparent spokes, winding, and local contour shape therefore converge to those of `z^m`.

## Visual and computational audit

Visualization: [[research/visual_exploration/visualizations/simple-zero-local-universality.md]].

The retained figure uses the first nontrivial critical-line zero numerically, approximately

`rho ~= 1/2 + 14.1347251417347 i`,

and the numerically evaluated derivative `zeta'(rho)` to form the simple-zero normalization

`G_epsilon(z) = zeta(rho + epsilon z)/(epsilon zeta'(rho))`.

Domain-color portraits for `epsilon=0.8`, `0.2`, and `0.05` visibly collapse toward the universal template `z`. A coarse unit-disk audit of the complex residual gave

`sup |G_epsilon(z)-z| ~= 0.42036, 0.18570, 0.08756, 0.04254, 0.02097, 0.01041`

for `epsilon=0.8, 0.4, 0.2, 0.1, 0.05, 0.025`, respectively. The near-linear decrease is consistent with the exact `O(epsilon)` theorem, but the numerical values are only an illustration; the factorization above is the evidence.

The illustration does not assert that all zeta zeros are simple. The theorem handles arbitrary multiplicity, and the numerical derivative is used only to render this one local example.

## Prior-art and novelty assessment

The local input is standard complex analysis. NIST DLMF §1.10(i), under “Zeros,” defines a zero of multiplicity `m` by the first nonzero Taylor coefficient. The factorization `f(rho+w)=a_m w^m h(w)` with `h(0)=1` and the resulting rescaled convergence are immediate consequences of that Taylor expansion. No novelty is claimed for the theorem itself.

NIST DLMF §25.10(i) records the standard zeta-zero setting: nontrivial zeros lie in the critical strip, occur with the functional-equation symmetries, and RH asserts that they all lie on `Re(s)=1/2`. The present result uses none of RH and does not constrain zero locations; it only identifies what infinitesimal normalized pictures necessarily forget.

The research contribution here is the obstruction's role as a visual baseline: before interpreting a nested zero portrait as zeta-specific self-similarity, remove the universal local monomial normal form and ask whether any residual survives at a mesoscopic scale.

## Boundary conditions and counterarguments

The theorem is **infinitesimal**. It does not say that mesoscopic or global neighborhoods of zeta zeros are universal. Once the viewing radius reaches a non-negligible fraction of local zero spacing, neighboring zeros, the gamma factor, the functional equation, and global analytic structure can enter.

The normalization also deliberately removes the leading Taylor coefficient `a_m`. A statistic built from the magnitude or phase of that coefficient may carry function-specific information. Such a statistic would need its own mathematical interpretation and matched controls; it cannot be inferred from universal local shape alone.

Multiplicity is not removed. A multiple zero converges to `z^m`, not `z`; the local winding number detects `m`. This does not supply an on-line/off-line discriminator unless an independent theorem relates multiplicity to zero location.

Finally, finite-resolution raster effects can obscure the `O(r)` regime. The exact factorization, not visual convergence rate in a particular renderer, is the decisive control.

## Consequence for the research line

The proposed critical-strip multiscale exploration now has a mandatory baseline: **arbitrarily deep normalized zooms around individual zeros are guaranteed to classicalize to the Taylor monomial**. Any potentially RH-relevant visual residual must therefore live outside that trivial local limit or deliberately retain a quantity, such as the leading coefficient, whose information content is justified separately.

This narrows the live visual question to mesoscopic scales normalized against local zero spacing, or to cross-zero/global statistics that survive subtraction of the local monomial template.
