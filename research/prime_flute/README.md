# Prime Flute

## Research mandate

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

Determine whether the exact hyperbolic surface carries a nontrivial relation between prime-gap fluctuations and natural spectral or dynamical objects relevant to zeta or the critical line.

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

### Scope and exclusions

This line covers only the derived hyperbolic prime-flute. Do not develop new prime-circle cyclotomic, root-of-unity, or potential-theory findings here.

Mere restatements of prime-gap statistics, arbitrary generating functions, or operators/products introduced only because their notation resembles zeta are outside the target. Off-prime interpolation data from `cot(pi/x)` are not intrinsic unless the proposed quantity descends to the sampled endpoint/Fuchsian geometry.

### Line-specific falsification controls

For candidate mechanisms, test specifically for:

- universal cusp or background phenomena;
- noncompactness or infinite-type surface effects unrelated to the primes;
- quantities that retain only coarse gap shape while losing primality specificity;
- matched composite, shifted, dilated, or otherwise non-prime endpoint controls;
- local or finite-jet effects reproducible by a smooth matched reference;
- selected orbit sectors or truncated products whose apparent boundary disappears in the natural full object;
- dependence on an arbitrary continuum interpolation rather than the exact discrete endpoint/Fuchsian data.

### Prior-art domains

- tight flutes and train surfaces;
- infinitely generated Fuchsian groups and infinite-type hyperbolic surfaces;
- Selberg/Ruelle zeta functions and prime-geodesic theorems;
- Patterson-Sullivan theory;
- cusp scattering and essential spectrum;
- trace formulas and relative spectral theory;
- transfer-operator and thermodynamic-formalism methods;
- determinant and resonance frameworks for noncompact or infinite-type surfaces.

### Relationship to other lines

`prime_circle` is the upstream construction that supplies the ordered prime geometry from which the flute is derived. Circle-specific claims are not automatically invariants of the hyperbolic surface.