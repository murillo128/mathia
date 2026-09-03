# VIS-015 — nonzero circular log-modulus modes are Poisson–Jensen zero sources

## Claim

Let `F` be holomorphic on a neighborhood of the closed disk `|w|<=R`, with `F(0) != 0` and no zero on `|w|=R`. List the zeros in `|w|<R` as

`a_j = rho_j exp(i phi_j)`

with multiplicities `m_j`. For `0<r<R`, define the angular Fourier coefficients of the circular log modulus by

`c_n(r) = (1/(2 pi)) int_0^{2 pi} log|F(r exp(i theta))| exp(-i n theta) d theta`.

For every integer `n>=1`, there is a coefficient `b_n` coming from a zero-free holomorphic factor such that

`c_n(r) = (b_n/2) r^n - sum_j (m_j/(2n)) exp(-i n phi_j) exp(-n |log r - log rho_j|)`.

Equivalently, with `t=log r`, the exact distributional identity is

`(d^2/dt^2 - n^2) c_n(exp t)
 = sum_j m_j exp(-i n phi_j) delta(t-log rho_j)`.

Thus each zero crossing contributes an exponential cusp in every nonzero angular mode, and the radial Helmholtz operator extracts exactly the `n`th angular Fourier moment of the zero measure on that entry circle.

After subtracting these explicit zero terms, the remainder is the `n`th Fourier mode of a harmonic function and therefore scales exactly as `r^n`. One retained shell determines all smaller concentric shells. Taken over all `n`, the nonzero angular zero-entry data contain the angular zero configuration itself, not an additional multiscale channel.

Applied to the zero-normalized Riemann `xi` field

`H_rho(w)=xi(rho+w)/(a_m w^m)`

from `VIS-012`–`VIS-014`, this means that **circular log-modulus geometry across zero-entry scales is completely decomposed into the translated zero configuration plus a Poisson-determined harmonic background**. Subtracting the entered-zero contributions leaves no residual circular-shell coupling to discover.

**Evidence/status:** `CLASSICAL-POISSON-JENSEN + EXACT-DERIVED + DECISIVE-NEGATIVE/BASELINE`.

No novelty is claimed for Poisson–Jensen, harmonic factorization, Green-potential decomposition, or Fourier uniqueness. The durable Mathia consequence is the closure of the specific nonzero-angular circular-shell escape left open after `VIS-014`.

## Exact derivation

Fix `R` as above. Factor the zeros inside the disk using

`Q(w)=F(w) / product_j (1-w/a_j)^{m_j}`.

`Q` is zero-free on the simply connected disk, so it admits a holomorphic logarithm

`Q(w)=exp(g(w))`,
`g(w)=sum_{k>=0} b_k w^k`.

Hence

`log|F(w)| = Re g(w) + sum_j m_j log|1-w/a_j|`.

The `n`th positive Fourier coefficient of `Re g(r exp(i theta))` is `(b_n/2) r^n`.

For one zero `a=rho exp(i phi)`, use the convergent logarithmic series on the appropriate side of the entry radius. If `r<rho`,

`log|1-(r/rho) exp(i(theta-phi))|
 = -sum_{k>=1} (r/rho)^k cos(k(theta-phi))/k`.

If `r>rho`, factor out `(r/rho)` and expand the reciprocal ratio; the nonzero angular coefficients are the same with `r/rho` replaced by `rho/r`. Therefore the positive `n`th coefficient of the zero term is

`-(1/(2n)) exp(-i n phi) (min(r,rho)/max(r,rho))^n`

which is exactly

`-(1/(2n)) exp(-i n phi) exp(-n |log r-log rho|)`.

Summing over the zeros gives the stated formula.

For `f_n(t)=exp(-n|t-t_j|)`,

`(d^2/dt^2 - n^2) f_n = -2n delta(t-t_j)`

distributionally. Multiplying by the zero coefficient gives the source identity.

The `n=0` counterpart is exactly the Jensen hinge law from `VIS-014`: its second derivative in log radius is the radial zero-counting measure. The nonzero modes are therefore not an unrelated phenomenon; they are the angularly resolved completion of the same Poisson–Jensen source decomposition.

## Information content

At one entry radius `rho_*`, the source amplitude for mode `n` is

`M_n(rho_*) = sum_{|a_j|=rho_*} m_j exp(-i n phi_j)`.

These are precisely the Fourier coefficients of the finite angular point measure carried by the zeros on that circle. Knowing all `M_n` recovers that angular measure uniquely. Hence:

- `n=0` records only total multiplicity at the radius, reproducing the radial Jensen profile;
- `n>=1` records angular moments of the same zeros;
- after those zero-source terms are removed, only the harmonic/Poisson background remains.

There is no third circular-shell information channel between "zero configuration" and "harmonic boundary data".

For the special illustration in the retained visualization, the sampled zeta zeros are collinear on the critical line relative to the center, so their local angles are `+pi/2` or `-pi/2`. Even angular modes therefore give the same source phase for an upper and lower zero, while odd modes distinguish the two sides. That parity pattern is forced by collinearity; it is not evidence of a zeta-specific fractal mechanism.

## Visual check

The retained artifact

`research/visual_exploration/visualizations/angular-zero-entry-poisson-jensen.md`

centers on the 100th numerically tabulated critical-line zeta zero, normalizes local ordinate differences by

`Delta = 2 pi / log(Im(rho_100)/(2 pi))`,

and forms the finite zero product from indices `89..112` excluding `100`:

`P(w)=product_k (1-w/a_k)`,
`a_k = i (gamma_k-gamma_100)/Delta`.

The figure scans `0.25 <= r/Delta <= 11.3`. It shows the zero-entry source locations, the exact cusp trajectories of the first three nontrivial mode components, and the direct-quadrature agreement summary. The apparent multiscale kinks in the mode tracks occur exactly at zero-entry radii.

As a numerical integrity check only, 4096-angle direct quadrature of the finite product shell field was compared with the closed-form zero-cusp formula at 79 radii kept away from entry circles. The maximum absolute coefficient errors were

- `n=1`: `1.01e-15`;
- `n=2`: `1.33e-15`;
- `n=3`: `1.50e-15`;
- `n=4`: `1.22e-15`.

The finite product is an illustration of the exact decomposition, not an approximation claim for `xi`. The mathematical evidence is the holomorphic factorization and Poisson–Jensen identity.

## Research consequence

`VIS-013` showed that zero-free concentric shells are Poisson-determined. `VIS-014` showed that the zero-entry circular mean is exactly the radial zero-distance multiset. The remaining accepted multiscale clue therefore proposed inspecting nonzero angular content and subtracting explicit zero-entry contributions.

This finding closes that exact circular-log-modulus escape: the nonzero angular entry terms are themselves explicit zero Green/logarithmic potentials, and once they are removed the remainder is harmonic and again Poisson-determined. A visually rich stack of circular `log|H_rho|` shells can therefore contain no scale information beyond:

1. the angularly resolved zero configuration encountered by the disks; and
2. one harmonic boundary shell.

Future visual work should not promote angular shell texture, cusp tracks, or cross-radius mode coupling of `log|xi|` as an independent mechanism unless it first quotients this decomposition. A live question may instead study a statistic of the zero configuration itself against matched zero processes, a cross-center relation, or another field/observable whose information is not already equivalent to Poisson–Jensen zero sources plus harmonic boundary data.

Changing the nested domain from circles to another regular domain does not by itself create a new log-modulus information channel: the general Green-function/harmonic-measure Poisson–Jensen decomposition has the same source-plus-boundary structure. A non-circular construction would need a genuinely additional invariant, not merely a different Green kernel.

## Prior art and novelty assessment

Poisson–Jensen is classical. Thomas Ransford's *Potential Theory in the Complex Plane*, §4.5, develops the Poisson–Jensen formula through Green functions and harmonic measure; this is the appropriate prior-art boundary for the source-plus-boundary decomposition used here. The disk Poisson kernel and its Fourier multiplier `r^|n|` were already recorded for `VIS-013`, and Jensen's radial zero-counting specialization was already recorded for `VIS-014`.

The formula for `c_n` is an elementary Fourier expansion of the classical logarithmic zero potential. The distributional source identity is the polar/log-radius Fourier-mode form of the standard fact that `log|F|` is harmonic away from zeros and has point-mass Laplacian at zeros.

`VIS-015` claims no new theorem of complex analysis and no RH implication. Its contribution is a negative-control specialization for the current visual program: **the entire nonzero-angular concentric-shell channel of `log|H_rho|` is already exhausted by classical zero sources plus harmonic continuation**.

## Boundary conditions and falsification

The clean disk statement assumes `F` is holomorphic on a neighborhood of the closed disk and has no zero on the chosen outer boundary. Entry radii may be handled distributionally; the logarithmic singularity is locally integrable.

The finding does not say that the zero configuration is uninteresting. On the contrary, all angular source moments are exactly zero-configuration data, so a nontrivial statistic of those moments is a statistic of the zeros and must be judged against established zero statistics and matched point-process controls.

The finding also does not classify observables that are not functions of the circular log modulus, nor does it show that every cross-center or arithmetic/prime-zero representation is tautological. Its no-go boundary is the nested-domain `log|F|` potential channel after zero-source and harmonic-boundary information are accounted for.
