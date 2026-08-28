# Prime-circle findings

This is the compact index for durable evidence under `research/prime_circle/findings/`. Detailed derivations, prior-art audits, boundary conditions, and research gates live in the individual finding files.

> **Legacy ID note:** two independent findings were historically persisted as `PC-015`. Preserve both IDs/files; new findings continue above the maximum existing integer rather than renumbering history.

## Indexed findings

### PC-001 — common-vertex potential is exactly von Mangoldt

**Status:** `CLASSICAL-IDENTITY` + `CANDIDATE-NEW-STRUCTURE`.

The logarithmic chord interaction of the common vertex with the primitive `n`-shell is exactly `log|Phi_n(1)|=Lambda(n)`. The geometry contains von Mangoldt intrinsically, but its ordinary Dirichlet transform is the classical `-zeta'/zeta`.

[Detailed finding](findings/PC-001-common-vertex-potential-is-von-mangoldt.md)

### PC-002 — primitive-shell resultants detect prime-power scale jumps

**Status:** `CLASSICAL-IDENTITY` + `CANDIDATE-NEW-STRUCTURE`.

Pairwise logarithmic shell interaction is the cyclotomic resultant; after normalization it is nonzero exactly across prime-power multiplicative jumps and returns `Lambda(n/m)`.

[Detailed finding](findings/PC-002-primitive-shell-resultant-detects-prime-power-jumps.md)

### PC-003 — exact harmonic interior/exterior duality

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE`.

The primitive-shell potential `U_n(z)=log|Phi_n(z)|` obeys the exact inversion relation `U_n(z)=phi(n)log|z|+U_n(1/conj(z))` and exact divisor/Möbius decomposition. This is intrinsic to the original circle.

[Detailed finding](findings/PC-003-harmonic-interior-exterior-duality.md)

### PC-004 — normalized resultants reproduce finite-prime Weil local kernels

**Status:** historical `EXACT-DERIVED` + candidate; **materially downgraded by PC-006**.

On prime-power rays, half-density normalization of off-diagonal cyclotomic resultants produces the kernel `(log p)p^{-|a-b|/2}`, matching the finite-prime local shape of Weil-type kernels.

[Detailed finding](findings/PC-004-normalized-resultants-weil-local-kernels.md)

### PC-005 — discriminant renormalization completes the prime-ray kernel

**Status:** historical `EXACT-DERIVED` + candidate; **materially downgraded by PC-006**.

A discrete scale derivative of normalized cyclotomic discriminants supplies the diagonal `log p`, completing the prime-ray Toeplitz/Poisson kernel, but the diagonal and off-diagonal pieces are not yet produced by one canonical energy.

[Detailed finding](findings/PC-005-discriminant-renormalization-completes-prime-ray-kernel.md)

### PC-006 — critical GCD kernel and potential theory downgrade PC-005

**Status:** `DECISIVE-NEGATIVE` + `NOVELTY-CORRECTION` + `EXACT-DERIVED`.

Resultant/discriminant energies belong to classical logarithmic potential theory, and `p^{-|a-b|/2}` is the prime-ray restriction of the classical critical GCD kernel `gcd(m,n)/sqrt(mn)`. A new RH mechanism would need one intrinsic object producing mutual energy, self-renormalization, and the global counterterm together.

[Detailed finding](findings/PC-006-critical-gcd-kernel-and-potential-theory-downgrade-PC005.md)

### PC-007 — cumulative new vertices are the Farey sequence

**Status:** `DECISIVE-PRIOR-ART` + `BRANCH-CLOSED-AS-NOVELTY`.

Accumulating all primitive/new vertices through level `N` gives the Farey sequence geometrically, so angular-discrepancy RH criteria in that cumulative geometry are classical rather than a new mechanism.

[Detailed finding](findings/PC-007-cumulative-new-vertices-are-farey-rh-geometry-is-classical.md)

### PC-008 — single-polygon Riesz energy and cycle spectral zeta are known RH reformulations

**Status:** `DECISIVE-PRIOR-ART` + `BRANCH-CLOSED-AS-NOVELTY`.

Natural scalar spectral/Riesz constructions on one regular polygon fall into existing RH-equivalent or classical formulations and do not provide a new geometric explanation.

[Detailed finding](findings/PC-008-single-polygon-riesz-and-cycle-spectral-zeta-are-known-rh-reformulations.md)

### PC-009 — polygon-edge crossing counts collapse to the GCD kernel

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` + `BRANCH-CLOSED-AS-NOVELTY`.

Pairwise crossing/incidence geometry of regular-polygon edges reduces exactly to GCD data, closing that unlabeled combinatorial branch as a source of new RH structure.

[Detailed finding](findings/PC-009-polygon-edge-crossing-counts-collapse-to-gcd-kernel.md)

### PC-010 — abstract refinement dynamics is the Bost–Connes cyclotomic tower

**Status:** `DECISIVE-NEGATIVE` for vertex-birth/refinement dynamics alone.

Keeping only roots of unity, birth levels, and power/refinement maps recovers the classical cyclotomic/Bost–Connes organization rather than a new dynamics.

[Detailed finding](findings/PC-010-abstract-refinement-dynamics-is-the-bost-connes-cyclotomic-tower.md)

### PC-011 — common-vertex chord correlations are Dedekind/Vasyunin sums

**Status:** `DECISIVE-NEGATIVE` for first/second angular correlations of the anchored chord fan.

Natural low-order correlations of the common-vertex chord geometry reduce to classical Dedekind/Vasyunin-type sums and known RH-adjacent structures.

[Detailed finding](findings/PC-011-common-vertex-chord-correlations-are-dedekind-vasyunin-sums.md)

### PC-012 — finite cross-level edge geometry embeds in one regular-polygon arrangement

**Status:** `DECISIVE-NEGATIVE` for unlabeled finite edge-incidence/crossing novelty.

Any finite collection of regular-polygon levels embeds into the diagonal arrangement of the single polygon at their LCM, so unlabeled finite incidence/crossing geometry contains no additional cross-level invariant.

[Detailed finding](findings/PC-012-finite-cross-level-edge-geometry-embeds-in-a-single-regular-polygon-diagonal-arrangement.md)

### PC-013 — pure projective transfer is flat and Hill spectrum needs extra gauge

**Status:** `DECISIVE-NEGATIVE`.

Canonical one-dimensional projective moving-frame transport telescopes, while a Hill/Schrödinger lift retains an alternating gauge that changes the spectrum. Prime-circle cross-ratios alone do not canonically determine a global spectral operator.

[Detailed finding](findings/PC-013-pure-projective-transfer-is-flat-and-hill-spectrum-needs-extra-gauge.md)

### PC-014 — exact Euclidean circle spectral transfer is subdivision-invariant

**Status:** `DECISIVE-NEGATIVE`.

The exact Helmholtz/Dirichlet-to-Neumann transfer on successive prime arcs composes by total arc length, so all intermediate prime-gap fluctuations disappear. Adding a gap-sensitive spectral parameter afterward would import structure not forced by the circle.

[Detailed finding](findings/PC-014-euclidean-unit-circle-spectral-transfer-is-subdivision-invariant.md)

### PC-015 — full-field Dirichlet transform is Möbius inversion

**Status:** `DECISIVE-NEGATIVE` + `LITERATURE+DERIVED` + `EXACT-DERIVED`.

The complete interior primitive-shell field, when Dirichlet-transformed over level, factors through `1/zeta(s)` because primitive-shell extraction is Möbius inversion. Spatial circle inversion leaves the same scale variable and does not implement `s -> 1-s`.

[Detailed finding](findings/PC-015-full-field-dirichlet-transform-is-moebius-inversion.md)

### PC-015 — spherical compactification is exact but fixed linear sphere spectra collapse to Ramanujan data

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE`.

Stereographic compactification makes inversion an exact equatorial reflection and orthogonal circles exact spherical caps, but every fixed round-sphere rotationally invariant linear operator sees primitive shells only through classical Ramanujan Fourier data.

[Detailed finding](findings/PC-015-spherical-compactification-and-linear-spectral-collapse.md)

### PC-016 — prime levels are exactly complete cyclic covers

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE`; no RH claim.

For the anchored birth surface, `n` is prime exactly when `z^n` realizes it as the complete unbranched cyclic cover of the thrice-punctured sphere. Multiplication by an old prime factor is an exact cover; introducing a new factor requires cover plus puncture-filling surgery.

[Detailed finding](findings/PC-016-prime-levels-are-complete-cyclic-covers.md)

### PC-017 — canonical cyclotomic uniformization defect

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE`; no RH claim.

Comparing the canonical Fuchsian projective connection of the birth surface with the explicit complete cyclic-cover connection gives an intrinsic nonlinear/accessory defect, zero exactly at prime levels. Its global accessory/monodromy part remains a live candidate because it is not a fixed linear shell observable.

[Detailed finding](findings/PC-017-cyclotomic-uniformization-defect.md)

### PC-018 — factor-introduction projective surgery is flat

**Status:** `DECISIVE-NEGATIVE`.

Uniformization/projective defects under power maps satisfy an exact cocycle, so introducing prime factors in different orders has zero canonical projective curvature/holonomy. Any surviving information must be nonlinear endpoint data rather than path-order holonomy.

[Detailed finding](findings/PC-018-projective-factor-surgery-is-flat.md)

### PC-019 — unanchored primitive-shell geometry cannot distinguish `n` from `2n`

**Status:** `DECISIVE-NEGATIVE`.

For odd `n`, `Phi_{2n}(z)=Phi_n(-z)`, so every unanchored intrinsic geometry or spectrum of one primitive shell identifies odd `n` with composite `2n`. The common vertex/absolute phase or multi-level structure is indispensable.

[Detailed finding](findings/PC-019-unanchored-birth-shell-geometry-cannot-distinguish-n-from-2n.md)

### PC-020 — the anchored local jet is classical Jordan-totient data

**Status:** `DECISIVE-NEGATIVE` for finite-order local anchored differential data.

The full Taylor jet of `log Phi_n(e^t)` at the common vertex is generated by `Lambda(n)`, `phi(n)`, even Jordan totients, and universal Bernoulli constants. A viable construction must therefore be anchored **and** nonlocal or genuinely multi-level.

[Detailed finding](findings/PC-020-anchored-local-jet-is-jordan-totient-data.md)

### PC-021 — regular linear probes are Möbius-tautological before spectralization

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for regular fixed linear ambient probes and independently transformed bounded multilinear probes.

At the level of counting measures, `R_n=sum_{d|n}P_d`; hence for `Re(s)>2`,

\[
\sum_{n\ge1}\frac{P_n}{n^s}
=\frac1{\zeta(s)}\sum_{d\ge1}\frac{R_d}{d^s}.
\]

Every fixed bounded linear observable inherits this factorization, and independent multilinear shell indices inherit one reciprocal-zeta factor each. The common-vertex logarithmic potential escapes the theorem precisely because it is a singular boundary probe: it is divergent on every full layer but finite on primitive shells. Thus the surviving region is anchored, nonlocal, and nonlinear or singularly renormalized.

[Detailed finding](findings/PC-021-regular-linear-probes-are-moebius-tautological.md)

### PC-022 — cyclic-cover spectrum has exact-order birth layers; modular zeta is inherited background

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for a direct inherited modular/Riemann-zeta spectral mechanism.

The full-root cyclic covers satisfy `L²(Y_n)=direct_sum_{d|n} H_d^birth`, where `H_d^birth` consists exactly of deck characters of order `d`; the projector onto the order-`n` layer has Ramanujan coefficients. Venkov–Zograf Artin formalism gives the matching divisor factorization of Selberg zeta. The standard modular scattering channel containing `zeta(2s-1)/zeta(2s)` lies in the universal trivial/old sector present at every level and is removed by exact-order birth extraction, so its Riemann zeros cannot be counted as a prime-specific mechanism.

[Detailed finding](findings/PC-022-cyclic-cover-spectrum-has-exact-order-birth-layers.md)

### PC-023 — exact-order Selberg birth factors are cyclotomic filters of one fixed length-winding spectrum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the canonical exact-order Selberg product/determinant as a new arithmetic mechanism.

On the absolute-convergence half-plane, grouping the twisted Selberg Euler products over all deck characters of exact order `n` gives a local factor `Phi_m(q)^(phi(n)/phi(m))`, with `m=n/gcd(n,r)` for geodesic winding `r` (and `(1-q)^phi(n)` when `n|r`). Equivalently, the logarithmic weights are exactly `c_n(jr)`. Thus the level dependence of the canonical birth determinant is only classical cyclotomic/Ramanujan filtering of the fixed base length-winding spectrum; any surviving route must use a canonically distinguished individual twist, exceptional controlled analytic behavior, or the nonlinear uniformization defect.

[Detailed finding](findings/PC-023-exact-order-selberg-birth-factors-are-cyclotomic-filters.md)
