# Prime Flute

## Research mandate

### Identity

Research line: `prime_flute`.

### Primary object

The line studies the exact zero-twist hyperbolic prime-flute built from the ordered odd primes. For consecutive odd primes `p_n`, write

```text
g_n     = p_{n+1} - p_n
u_n     = cot(pi / p_n)
Delta_n = u_{n+1} - u_n
h_n     = log(u_n / u_{n-1})
```

The increasing endpoint sequence `u_n` determines the tight flute/Fuchsian surface. The `p=2` endpoint is degenerate in this coordinate, so ratio formulas normally begin at `p=3`.

Intrinsic data include cuff lengths, multi-gap separating geodesics, cusp geometry, cross-ratios, marked endpoint data, and spectral/dynamical invariants of the resulting infinite-type surface.

### Objective

Determine whether the exact hyperbolic surface carries a nontrivial and potentially novel relation between prime-gap fluctuations and natural spectral or dynamical objects relevant to zeta or the critical line.

The target is a mechanism intrinsic to the flute itself, not a spectral object imported solely to mimic the Riemann zeta function.

### Priority questions

Study whether intrinsic flute data such as the distinguished cuff lengths

```text
ell_n ~ 2 log(4 p_n / g_n),
```

multi-gap separators, cross-ratios, cusp structure, and marked endpoint geometry induce meaningful arithmetic information in:

- the Laplacian and relative Laplacian;
- transfer operators;
- resonances and scattering;
- trace formulas;
- Patterson-Sullivan data;
- Selberg/Ruelle-type objects and prime-geodesic structures;
- determinants or other natural spectral invariants;
- genuinely global or nonlocal mechanisms capable of retaining information erased by local or scalar reductions.

Prefer invariants forced by the exact discrete endpoint/Fuchsian data over constructions depending on an arbitrary continuum interpolation.

### Scope and exclusions

This line covers only the derived hyperbolic prime-flute. Do not develop new prime-circle cyclotomic, root-of-unity, or potential-theory findings here.

Reject mere restatements of prime-gap statistics, arbitrary generating functions, or operators/products introduced only because their notation resembles zeta. Do not treat an off-prime interpolation of `cot(pi/x)` as intrinsic surface data unless the proposed quantity is shown to descend to the sampled endpoint/Fuchsian geometry.

### Falsification and novelty standard

Aggressively test whether a candidate is explained by:

- universal cusp or background phenomena;
- telescoping, gauge, coordinate, or normalization artifacts;
- noncompactness or infinite-type surface effects unrelated to the primes;
- quantities that retain only coarse gap shape while losing primality specificity;
- matched composite, shifted, dilated, or otherwise non-prime endpoint controls;
- local or finite-jet effects that can be reproduced by a smooth matched reference;
- selected orbit sectors or truncated products whose apparent boundary disappears in the natural full object.

A viable mechanism must survive relevant controls and be intrinsic to the exact surface rather than to an arbitrary representation of it.

### Prior-art audit surface

Search by mechanism and equivalent formulation across:

- tight flutes and train surfaces;
- infinitely generated Fuchsian groups and infinite-type hyperbolic surfaces;
- Selberg/Ruelle zeta functions and prime-geodesic theorems;
- Patterson-Sullivan theory;
- cusp scattering and essential spectrum;
- trace formulas and relative spectral theory;
- transfer-operator and thermodynamic-formalism methods;
- determinant and resonance frameworks for noncompact or infinite-type surfaces.

### Relationship to other lines

`prime_circle` is the upstream construction and may be read as mathematical context, but circle-specific claims are not automatically flute invariants.

`weil_positivity` may consume a canonical positive or relative spectral structure if one survives here. `prime_lattice` and `weil_inertia` are separate research objects and may be used only for comparison or explicit cross-line bridges supported by evidence.
