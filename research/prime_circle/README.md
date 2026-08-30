# Prime Circle

## Research mandate

### Identity

Research line: `prime_circle`.

### Primary object

The line starts from the original regular-polygon / roots-of-unity construction, before imposing the hyperbolic prime-flute model. Let

\[
P_n=\mu_n=\{z\in\mathbb C:z^n=1\}
\]

be the vertices of the regular `n`-gon on a fixed circle with common anchored vertex `1`, and let

\[
P_n^*=\{\zeta:\operatorname{ord}(\zeta)=n\}
\]

be the primitive/new-vertex layer. Thus

\[
P_n=\bigsqcup_{d\mid n}P_d^*,
\qquad |P_n^*|=\varphi(n),
\]

and for a prime `p`, every non-common vertex of `P_p` is new.

### Objective

Determine whether structures forced intrinsically by this roots-of-unity geometry yield a nontrivial and potentially novel bridge to the Riemann zeta function, its functional equation, explicit formulas, spectral/operator formulations, or the critical line.

The aim is not to repackage classical cyclotomic or zeta identities, but to identify additional geometric, harmonic, or nonlocal structure that retains information those scalar identities lose.

### Priority questions

Study, when they arise intrinsically from the construction:

- primitive/new-vertex layers and cyclotomic structure;
- chord distances and interactions between layers;
- logarithmic potentials `U_n(z)=log|Phi_n(z)|` and their interior/exterior reciprocity;
- the exact common-vertex von Mangoldt identity and pairwise shell resultants;
- Möbius/divisor decompositions and Fourier/Ramanujan modes;
- scale/refinement dynamics;
- spherical or projective representations and exact orthogonal-circle constructions;
- genuinely two-dimensional or nonlocal operators that retain information lost by scalar evaluation.

Prefer exact geometric or harmonic consequences before importing external analytic or spectral machinery.

### Scope and exclusions

This line covers only the original prime-circle / roots-of-unity geometry. Do not develop new hyperbolic cuff, cusp, scattering, or infinite-flute results here.

Do not count recovery of `-zeta'(s)/zeta(s)`, standard cyclotomic identities, known divisor transforms, or arbitrary spectral wrappers as progress by themselves. A proposed bridge must add a precise, falsifiable mechanism beyond a change of coordinates or notation.

### Falsification and novelty standard

Try to collapse every candidate to its simplest classical or degenerate form before treating it as new structure. In particular test for:

- cyclotomic or resultant identities in disguise;
- telescoping, coboundary, quotient, endpoint-only, or projective pure-gauge reductions;
- loss of information under scalar evaluation;
- universal behavior reproduced by matched non-prime or non-arithmetic controls;
- dependence on an arbitrary coordinate, interpolation, normalization, or hand-picked operator.

Novelty must be assessed by mathematical mechanism and equivalent formulation, not by wording.

### Prior-art audit surface

Search the closest classical and modern literature around:

- cyclotomic polynomial and resultant theory;
- harmonic and logarithmic potential theory on roots of unity;
- Ramanujan/Fourier sums and divisor decompositions;
- Farey and Franel-Landau-type RH criteria when relevant;
- Bost-Connes and related cyclotomic dynamics;
- Dedekind/Vasyunin-type structures and gcd kernels when structurally adjacent;
- projective or discrete-Schwarzian constructions;
- known operator or spectral formulations that may already contain the candidate mechanism.

### Relationship to other lines

`prime_flute` is a downstream geometric construction derived from the ordered prime vertices and may be read for comparison, but flute-specific phenomena are not evidence that the same mechanism is intrinsic to the circle construction.

`prime_lattice`, `weil_positivity`, and `weil_inertia` may provide external comparisons or consume a surviving Prime Circle mechanism, but they do not redefine this line's object or objective.
