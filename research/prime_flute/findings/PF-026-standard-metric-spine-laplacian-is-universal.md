# PF-026 — the standard metric-spine Laplacian is universal

**Status:** NEGATIVE/OBSTRUCTION. The quantum-graph statement is standard; the substantive project consequence is that the most natural one-dimensional spectral reduction of the exact zero-twist prime-flute erases all distinguished-cuff / prime-gap information.

## Statement

Let `X_prime` be the zero-twist prime-flute and retain its canonical geodesic spine. The exact distance between consecutive marked cuff locations is already recorded in PF-011:

```text
d_n
  = 1/2 (h_n + h_{n+1})
  = 1/2 log(u_{n+1}/u_{n-1}),

h_n = log(u_n/u_{n-1}),
u_n = cot(pi/p_n).
```

Equivalently, this distance is obtained from the right-angled-hexagon seam formula in the tight pair of pants together with the exact cuff identity

```text
exp(-ell_n/2) = tanh(h_n/4).
```

It is therefore tempting to form a metric/quantum graph whose vertices are the marked consecutive pants/cuffs, whose edge lengths are the exact `d_n`, and to ask whether the graph Laplacian, its transfer matrices, resolvent, spectral measure, or determinant retains prime-gap fluctuations.

For the **standard/Kirchhoff metric-graph Laplacian**, the answer is exactly no.

The underlying combinatorial graph is a ray: every interior marked point has degree two. A degree-two vertex with standard conditions

```text
f is continuous,
(outgoing derivative on the left) + (outgoing derivative on the right) = 0
```

is only a subdivision point. Suppressing it joins the two adjacent intervals and leaves the Kirchhoff Laplacian unitarily unchanged.

Since

```text
sum_{n=m}^N d_n
  = h_m/2 + sum_{n=m+1}^N h_n + h_{N+1}/2
  -> infinity,
```

because the middle sum telescopes to logarithmic endpoint growth, the complete metric spine has infinite total arclength. Concatenating all edges by arclength is therefore an isometry

```text
G_spine  ~=  [0,infinity).
```

Under this isometry the standard graph operator is simply

```text
- d^2/ds^2
```

on the half-line, with the ordinary natural boundary condition at the initial endpoint (or whatever fixed endpoint condition is deliberately chosen there).

Consequently the standard metric-spine spectrum is independent of the entire sequence

```text
(d_n), (h_n), (ell_n), (g_n).
```

For the natural Neumann endpoint,

```text
sigma(Delta_spine) = [0,infinity)
```

with the ordinary half-line spectral measure. Choosing Dirichlet at the initial endpoint changes the endpoint condition but still does not recover the internal prime subdivision.

## Exact reason the prime data disappear

The prime information does not disappear approximately. It disappears by an exact change of coordinate.

Define cumulative arclength

```text
s_m = 0,
s_{n+1} - s_n = d_n.
```

Each graph edge is the interval `[s_n,s_{n+1}]`. At every internal mark, Kirchhoff continuity is exactly continuity of `f` and of its first derivative in the global `s` coordinate. Thus a piecewise `H^2` graph function satisfying the degree-two Kirchhoff condition is simply an `H^2` function across that point.

The points `s_n` can be erased without changing the operator. Their spacing is therefore not spectral data for this operator.

This is the standard subdivision invariance of metric quantum graphs: degree-two vertices with natural/Kirchhoff conditions are spectrally inessential.

## Consequence for transfer-matrix constructions

One can of course write a free propagation matrix on every segment,

```text
M_n(k) =
  [[cos(k d_n),       sin(k d_n)/k],
   [-k sin(k d_n),    cos(k d_n)  ]].
```

But because there is no scattering at the degree-two marks,

```text
M_m(k) M_{m+1}(k) ... M_N(k)
```

is just the free propagation matrix for the **sum** of the segment lengths. The internal subdivision cannot create resonances, gaps, localized states, or a nontrivial determinant.

Therefore any proposed one-dimensional transfer model in which the individual `d_n` create spectral scattering must introduce extra structure at the marks: a potential, delta coupling, vertex mass, non-Kirchhoff matching, branching, or another interaction. Unless such structure is derived independently from the two-dimensional hyperbolic surface, it is an added model rather than spectral data of the exact prime-flute.

## Relation to PF-011 and PF-014

This strengthens PF-011. PF-011 showed that a point zeta made from the marked spine positions essentially reconstructs the classical prime zeta. PF-026 shows that the **standard differential spectral operator on the same metric spine does even less**: after arclength parametrization it forgets the marks entirely.

This does **not** invalidate PF-014. Burger-type graph weights arise from genuine weak separating necks of the two-dimensional surface and encode conductance/capacity between large components. Those graph vertices/edges are not arbitrary degree-two subdivisions of a geodesic ray. PF-014 therefore remains a different, potentially meaningful low-energy reduction.

## Interior/exterior duality

The ambient inversion that exchanges the interior and exterior hyperbolic copies preserves arclength. Applying the same spine reduction to the exterior gives another isometric half-line. Thus the exact interior/exterior duality does not restore prime-dependent spectrum in this one-dimensional standard-Laplacian reduction.

## Novelty check

There is no novelty claim for subdivision invariance itself. It is a standard theorem in quantum-graph spectral theory: vertices of degree two with standard/Kirchhoff conditions can be removed without changing the operator or its spectrum.

The project-level conclusion is nevertheless decisive:

```text
distinguished cuffs
  -> exact zero-twist seam/spine lengths d_n
  -> standard metric graph / Kirchhoff Laplacian
```

cannot be a prime-gap spectral channel.

A meaningful one-dimensional reduction must instead derive nontrivial couplings from genuinely two-dimensional geometry, such as the multi-gap separating necks/cross-ratios in PF-004/PF-014, rather than treating the canonical spine marks as scatterers.

## References

- Standard quantum-graph subdivision invariance / inessential degree-two vertices: metric-graph literature commonly removes degree-two Kirchhoff vertices because they do not affect spectral properties; see, e.g., Kostenko and Nicolussi, *Spectral estimates for infinite quantum graphs*, Calc. Var. PDE 58 (2019), Hypothesis 2.3 and its discussion.
- The equivalent local statement is elementary: at a degree-two Kirchhoff vertex, continuity plus current conservation are exactly continuity of the function and first derivative, so the two adjacent `H^2` pieces form one `H^2` function on the joined interval.
- The prime-flute exact spine formula used here is PF-011 and ultimately the standard right-angled-hexagon seam geometry plus PF-001.