# MI-062 — Growing positive compact depth and bounded Hilbert correlations are source-free conditioning resources

**Evidence level:** exact/classical conditioning synthesis from [VIS-367](../../findings/VIS-367-growing-depth-chebyshev-capacity-baseline.md) and [VIS-368](../../findings/VIS-368-uniform-positive-hilbert-correlation-is-bounded-preconditioning.md), extending the fixed-depth partition-sum audit of MI-061.

Growing polynomial depth genuinely leaves the fixed-dimensional theorem of VIS-366, but the first large effect it creates is still universal compact approximation geometry. For any positive probability measure on a compact interval of length `L`, VIS-367 factors the depth-`q` moment determinant through monic orthogonal-polynomial norms and compares each norm with the affine Chebyshev minimax polynomial. On `[-1,1]` this gives

`Z_q(mu) <= 2^(-(q-1)(q-2))`

and a raw monomial smallest-singular-value bound

`s_q(q) <= 2^(2-q)`.

Thus super-exponentially small moment determinants and exponentially bad raw monomial conditioning appear before the arithmetic source is consulted. They are a capacity/basis baseline, not evidence of localization.

VIS-368 closes a different apparent escape. Let `W` be an already priced positive diagonal coefficient covariance and `H` any positive-definite, possibly non-diagonal covariance. If `mW<=H<=MW`, then every singular value of the corresponding Wang maps differs by at most the fixed factors `sqrt(m)` and `sqrt(M)`. Uniform positive correlations can rotate singular directions and change constants, but they cannot change rank or asymptotic singular-value scale.

The two findings combine into one accounting rule. **High degree and positive correlation count only through the amount by which they leave the priced compact Hilbert geometry.** Growing depth must first quotient the universal Chebyshev/capacity collapse and pay the physical coefficient/basis-change norm. Non-diagonal positive geometry must expose degeneration of its relative spectrum; if the Loewner comparison constants remain bounded, it is only preconditioning.

Static source-independent signs or phases do not evade this rule: under a positive Hilbert budget they are a unitary gauge and leave the covariance singular spectrum unchanged. A genuinely new coefficient-topology resource therefore requires source-dependent signed selection, asymptotically degenerating metric equivalence whose cost is justified at the destination, an indefinite/non-Hilbert topology, noncompact/global geometry, nonlinear dependence, or another mechanism not reducible to positive compact polynomial sampling.

The reusable distinction is between **raw conditioning** and **net destination leverage**. A dramatic near-null direction is not useful merely because it exists; one must show that the physical coefficient norm can access it cheaply and that the complete Wang destination retains a gain after order growth, basis conversion, truncation and outer factors are charged.

**Boundary.** VIS-367 supplies an upper bound/baseline, not a proof that growing depth is useless or an optimal lower bound on every normalized polynomial basis. VIS-368 applies only to positive Hilbert metrics uniformly comparable to the chosen baseline; degenerating metrics, indefinite forms and source-dependent selectors remain outside it. Neither finding improves the Chebyshev-theta remainder or proves an RH consequence.
