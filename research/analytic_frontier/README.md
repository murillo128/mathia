# Analytic Frontier

## Research mandate

### Primary object

The line studies the quantitative analytic-number-theory machinery surrounding the Riemann zeta function and closely related Dirichlet `L`-functions: Dirichlet polynomials, large-value estimates, zero-detecting arguments, zero-density bounds, mean values and twisted moments, mollifiers, exponential-sum and sieve inputs, and zero correlations when they function as analytic information about zero location.

For zero-density questions write `N(sigma,T)` for the number of nontrivial zeros `rho=beta+i gamma` with `beta >= sigma` and `0 < gamma <= T`, with the exact convention restated whenever a source uses a different normalization.

### Objective

Identify analytic information that could rule out every off-critical zeta zero and thereby resolve RH. Modern zero-density, correlation, and critical-line proportion estimates are tools for learning and testing such mechanisms; their quantitative improvement is welcome but does not replace the full zero-location objective.

Determine exactly which estimate, support range, moment, correlation, or uniformity statement changes the available zero-information budget and what additional step could eliminate the remaining exceptions. A certified constant improvement is useful when its complete analytic assembly is justified and exposes a reusable source of gain or a sharp limitation.

### Priority questions

- For finite-correlation test functions, can the exact multiset defect be certified on its whole admissible domain, including collision and noncompact boundaries, before optimizing further perturbations?
- Can Guth--Maynard-type large-value bounds for Dirichlet polynomials be pushed, recombined, or transferred so that the resulting zero-density information controls a new RH-relevant regime rather than only improving a known exponent?
- Which zero-detecting decompositions or mean-value estimates are currently load-bearing in the best zero-density bounds, and what precise stronger estimate would move the next barrier?
- Can Levinson--Conrey-style arguments gain more from optimized combinations of zeta and its derivatives, twisted moments, or new auxiliary functions than from mollifier length alone?
- Is there a finite amount of pair/higher-correlation or moment information that gives useful horizontal information about zeros before one assumes the full conjectural hierarchy?
- Can recent unconditional analytic estimates provide the missing source-side input for a live obstruction in `weil_inertia` or `mobius_cancellation`?
- When a classical route stalls, can the obstruction be expressed as a sharp exponent, Fourier-support, correlation-order, or uniformity threshold that another method could attack directly?

### Scope and exclusions

This line owns upstream analytic machinery and its direct quantitative consequences. It does not own the compressed Weil-form/rank-inertia construction itself, prime-circle/flute geometry, or a generic catalogue of RH equivalences.

Finite-height verification, a reformulation equivalent to RH, or a conditional theorem whose hypothesis already contains essentially the desired zero-location conclusion is not a target result. Numerical optimization must lead to a certified admissible function and a complete zero-counting consequence to establish an improved bound.

### Line-specific falsification controls

For every proposed gain, track the complete exponent and support budget through the zero detector rather than only the locally improved estimate. Check whether an apparent unconditional statement imports RH, Lindelof, a density hypothesis, Hardy--Littlewood correlations, or an unproved moment asymptotic at another step.

When using Dirichlet-polynomial or moment estimates, separate diagonal control from off-diagonal correlations and verify the exact length, coefficient class, averaging range, and uniformity needed by the downstream zero statement. Test whether the same analytic input is compatible with matched zero configurations having materially different horizontal mass; if so, it is not yet a horizontal discriminator.

For signed Fourier--Laplace perturbations, distinguish failure of a sufficient positivity envelope from an actual zero or negative value of the exact defect. Prove the common compact reduction or tail bounds, treat degeneracies separately, and propagate certified local margins through the perturbation and analytic error budget. An interval enclosure containing zero is inconclusive.

### Prior-art domains

- large values of Dirichlet polynomials and zeta/L-functions;
- zero-density and zero-detecting methods;
- mean values, twisted moments, mollifiers, and zeta-derivative combinations;
- exponential sums, large sieve, dispersion, and related sieve machinery;
- pair correlation, higher zero correlations, and zero statistics used analytically;
- primes in short intervals when the proof mechanism feeds back into zeta-zero control.

### Relationship to other lines

`analytic_frontier` is primarily an upstream supplier of quantitative analytic information. `weil_inertia` may consume new correlation, moment, zero-density, or prime-distribution input but owns the resulting compressed-Weil and inertia arguments. `mobius_cancellation` may consume new signed-sum or mean-value estimates but owns Möbius-specific cancellation mechanisms.

`xi_flow` may consume unconditional zero-spacing or correlation information as dynamical input, while retaining ownership of the de Bruijn--Newman heat flow and collision problem. Cross-line transfers should become clues only when the exact mathematical statement and decisive test are identified.