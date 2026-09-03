# Zero-free shell Poisson collapse

![Zero-free shell Poisson collapse](zero-free-shell-poisson-collapse.png)

## Intent

Test whether nested circular log-modulus views around an isolated `xi` zero can carry an independent cross-scale signature after the local zero monomial has been divided out.

The target comes from the accepted clue `CLUE-zeta-critical-strip-multiscale-geometry.md`, but this artifact is a baseline test rather than evidence for a new fractal signal.

## Construction

Use

`xi(s)=(1/2)s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`

and the first nontrivial zero

`rho_1 = 1/2 + 14.13472514173469... i`.

For this simple zero define

`H(w)=xi(rho_1+w)/(xi'(rho_1) w)`

and sample

`u_r(theta)=log|H(r e^{i theta})|`

on 1024 equally spaced angles at 60-decimal-digit working precision.

The plotted radii are

`r = 0.75, 1.5, 2.5, 3.5`.

The next critical-line zero is at ordinate `21.02203963877155...`, giving local separation about `6.887314497`; therefore every plotted circle lies strictly inside the same zero-free disk around `rho_1`.

For each radius, compute the discrete angular Fourier coefficients `\hat u_r(n)` and plot

`|\hat u_r(n)|/r^n`

for modes `n=2,...,8`.

## Observation

The four curves collapse visually. Across modes `2,...,8`, the largest relative spread of the normalized coefficient magnitude over the four radii is about `2.3e-10`.

This is not an empirical surprise. `VIS-013` proves that in any zero-free disk

`\hat u_r(n) = r^|n| C_n`

for radius-independent coefficients `C_n`, and for `n>=2` those coefficients are the reciprocal-power zero moments already identified by `VIS-012`.

The image therefore illustrates a **negative multiscale control**: coherent evolution of nested zero-centered shells below the nearest-zero radius is forced by harmonic Poisson continuation.

## Controls and mathematical meaning

No interpolation between radii is used as evidence, and the claim does not depend on the selected first zero, the plotted radii, or the numerical collapse. The exact proof applies to every isolated xi zero after removing its complete local monomial.

The radius restriction is decisive. If an outer circle crosses another zero, `log|H|` is no longer harmonic on the full disk and Poisson-Jensen acquires explicit zero terms. Such zero-entry events remain a legitimate mesoscopic target.

The plot also deliberately starts at mode `n=2`: mode `n=1` obeys the same radial scaling but contains the genus-one linear/gauge contribution that `VIS-012` excludes from its raw reciprocal-zero-moment formula.

## Research consequence

Promoted independently of the image as [[research/visual_exploration/findings/VIS-013-zero-free-shells-poisson-determined.md]].

The accepted multiscale clue should now treat all nested circular evolution strictly inside one zero-free neighborhood as a baseline. Future visual work should either remove this Poisson-semigroup dependence or move to a regime where zero-entry/topological events, cross-zero comparisons, or another genuinely nontrivial scale change can occur.
