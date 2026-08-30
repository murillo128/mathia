# Prime-circle geometry

This directory records research that starts from the **original regular-polygon / roots-of-unity construction**, before imposing the hyperbolic prime-flute model.

## Research mandate

This section is the **canonical research contract** for the `prime_circle` Research Watch. The scheduled task should identify the line and stable finding prefix, then read this README for the mathematical objective, scope, priorities, exclusions, and prior-art surface. Routine Research Watch runs must not silently redefine this mandate.

### Objective

Investigate only the original **prime-circle / roots-of-unity geometry** under `research/prime_circle/`, before imposing the hyperbolic prime-flute model. Treat `research/prime_flute/` as a downstream, read-only branch when useful for comparison, not as part of this line's research scope or writable output.

Start from the regular-polygon / roots-of-unity construction with a common anchored vertex and ask whether structures forced intrinsically by that geometry yield a nontrivial and potentially novel bridge to the Riemann zeta function, its functional equation, explicit formulas, spectral/operator formulations, or the critical line.

### Priority structures and questions

Study, when they arise intrinsically from the construction:

- primitive/new-vertex layers and cyclotomic structure;
- chord distances and interactions;
- logarithmic potentials `U_n(z)=log|Phi_n(z)|`;
- the exact common-vertex von Mangoldt identity;
- pairwise shell resultants;
- Möbius/divisor decompositions;
- Fourier/Ramanujan modes;
- harmonic interior/exterior inversion;
- scale/refinement dynamics;
- spherical or projective representations;
- exact orthogonal-circle constructions;
- genuinely two-dimensional or nonlocal operators that retain information lost by scalar evaluation.

The line should prefer exact geometry and harmonic structure before importing external analytic or spectral machinery.

### Exclusions and falsification targets

Be especially alert to candidates that collapse to classical cyclotomic identities, Farey/Bost-Connes/Dedekind-Vasyunin structures, gcd kernels, Mellin/Dirichlet transforms of von Mangoldt, telescoping or projective pure gauge, or other known reformulations.

Do **not** count recovery of `-zeta'(s)/zeta(s)`, standard cyclotomic identities, or arbitrary spectral wrappers as progress by themselves. Do not develop new hyperbolic flute/cuff/cusp/scattering findings in this line; those belong to `prime_flute`.

### Prior-art audit surface

Novelty checks should search by mathematical mechanism and equivalent formulation, including classical cyclotomic polynomial/resultant theory, harmonic and potential theory on roots of unity, Ramanujan/Fourier sums, Farey and Franel-Landau-type RH criteria when relevant, Bost-Connes/cyclotomic dynamics, projective/discrete Schwarzian constructions, and known operator or spectral formulations that could already contain the candidate mechanism.

## Primary object

Let

\[
P_n=\mu_n=\{z\in\mathbb C:z^n=1\}
\]

be the vertices of the regular \(n\)-gon on a fixed circle, with the common vertex \(1\). The vertices that appear for the first time at level \(n\) are the primitive \(n\)-th roots

\[
P_n^*=\{\zeta:\operatorname{ord}(\zeta)=n\}.
\]

Thus

\[
P_n=\bigsqcup_{d\mid n}P_d^*,
\qquad |P_n^*|=\varphi(n).
\]

A prime \(p\) is characterized geometrically by

\[
P_p=P_1\sqcup P_p^*,
\]

so every non-common vertex of the \(p\)-gon is new.

## Research stance

The primary aim is to discover structures forced by this geometry itself: vertex collisions, chord distances, primitive/birth layers, logarithmic potentials, interior/exterior reciprocity, Fourier modes, scale renormalization, and interactions between layers.

Classical analytic-number-theory or spectral machinery is used mainly as a falsifier/novelty check after a candidate structure has been derived.

The hyperbolic prime-flute under `research/prime_flute/` is now treated as a secondary derived model rather than the central object.

## Evidence labels

- `EXACT-DERIVED`: exact consequence of the roots-of-unity geometry / elementary algebra.
- `CLASSICAL-IDENTITY`: exact but already standard in the literature.
- `CANDIDATE-NEW-STRUCTURE`: a new organization or operator suggested by the geometry; novelty not established.
- `NEGATIVE`: a proposed interpretation ruled out.
- `NEEDS-AUDIT`: requires source or proof verification.

## Current high-priority direction

Treat each primitive layer \(P_n^*\) as a boundary charge distribution and study its logarithmic potential

\[
U_n(z)=\sum_{\zeta\in P_n^*}\log|z-\zeta|=\log|\Phi_n(z)|.
\]

This construction simultaneously preserves the original circle geometry, the primitive/new-vertex decomposition, and an exact interior/exterior reciprocity. Canonical evidence lives under [`findings/`](findings/); [`graph/index.md`](graph/index.md) is the derived navigational view.
