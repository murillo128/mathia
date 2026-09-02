# PL-121 — De Bruijn–Newman heat flow gives only a rank-one quadratic coupling of prime exponents

## Claim

The de Bruijn–Newman deformation is a genuine zero-dynamical mechanism closely tied to the Riemann hypothesis, and Dobner's negative-time Dirichlet-series analysis exposes an apparently rich prime-exponent interaction through the coefficient weight

`exp((t/4)(log n)^2)`.

In prime-exponent coordinates `alpha=v(n)` with `ell_p=log p`, however,

`log n = <alpha,ell>`,

so the deformation is

`exp((t/4)<alpha,ell>^2)`.

Its quadratic form on the exponent lattice therefore has formal matrix `(1/4) ell ell^T`: it has rank one and depends only on the scalar log-energy `E(alpha)=<alpha,ell>=log n`. The cross-prime terms are real but contain no transverse information about the multidimensional exponent vector.

This is a decisive obstruction to interpreting the classical de Bruijn–Newman heat deformation itself as a genuinely higher-dimensional geometry of the prime-exponent lattice. The heat threshold remains deep and RH-sensitive, but its exponent-lattice shadow factors completely through the already classical one-dimensional energy map `n -> log n`.

**Evidence/status:** `LITERATURE + EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`.

The heat deformation and Newman constant are classical prior art; the extended-Selberg analogue is also prior art. The line-specific contribution here is the exact rank-one compression audit in exponent coordinates and the resulting restriction on what a new prime-lattice mechanism would have to add.

## Exact exponent-lattice calculation

Let

`n = product_p p^(alpha_p)`,

where `alpha` has finite support. Then

`log n = sum_p alpha_p log p = <alpha,ell>`.

The quadratic coefficient appearing in the negative-time deformed Dirichlet series studied by Dobner is therefore

`Q(alpha) = (1/4)(log n)^2 = (1/4)<alpha,ell>^2`.

Expanding gives

`Q(alpha) = (1/4) sum_p alpha_p^2 (log p)^2 + (1/2) sum_(p<q) alpha_p alpha_q log p log q`.

Thus every pair of occupied prime directions appears coupled. But this all-to-all appearance is misleading: for finite-support vectors the associated bilinear form is

`B(alpha,beta) = (1/4)<alpha,ell><beta,ell>`,

so its matrix is the outer product

`(1/4) ell ell^T`.

Hence `ker B` contains every finite-support direction orthogonal to `ell`, and on every finite-dimensional prime truncation the matrix has rank exactly one. Two exponent configurations `alpha,beta` with the same log-energy satisfy

`Q(alpha)=Q(beta)`.

For integer exponent vectors unique factorization makes `E(alpha)=log n` injective on the positive cone, so this does not identify two distinct positive integers. The relevant loss is geometric rather than set-theoretic: the deformation has no independent sensitivity to angular/transverse directions, local prime neighborhoods, Hamming/square-free structure, joins/meets, or any other multidimensional relation once `log n` is fixed as the coordinate.

The same conclusion survives any finite prime cutoff. If `ell^(P)` is the vector of `log p` for `p<=P`, then the Hessian of `Q` is proportional to `ell^(P)(ell^(P))^T`; increasing the number of primes increases the ambient dimension but not the rank of the coupling.

## Relation to the de Bruijn–Newman flow

In the Rodgers–Tao normalization one considers an even entire function

`H_t(x) = integral_0^infinity exp(t u^2) Phi(u) cos(xu) du`,

with a constant `Lambda` such that all zeros of `H_t` are real exactly for `t>=Lambda`. The Riemann hypothesis is equivalent to `Lambda<=0`, while Rodgers and Tao proved Newman's conjecture `Lambda>=0`; consequently RH is equivalent to `Lambda=0`.

With this sign convention,

`partial_t H_t = - partial_x^2 H_t`,

because `partial_x^2 cos(xu)=-u^2 cos(xu)`. Increasing `t` is therefore backward heat in the standard PDE sign convention. None of this is an Euler-product identity: the deformation is defined at the level of the completed xi-function's Fourier/theta representation and its entire-function zero dynamics.

Dobner's treatment of Newman's conjecture for the extended Selberg class introduces, in the negative-time regime relevant to his argument, a deformed Dirichlet series whose coefficients contain

`exp((t/4)(log n)^2)`.

It is this specific arithmetic shadow of the heat flow that yields the rank-one exponent-lattice calculation above. The calculation must not be promoted into a claim that the heat-deformed completed zeta function globally has an Euler product or that the displayed Dirichlet series is valid as such throughout the critical strip. Analytic continuation in the de Bruijn–Newman theory comes from the completed entire-function construction, not from formally continuing an Euler product.

## Why the cross-prime terms do not supply higher-rank arithmetic geometry

At first sight

`sum_(p<q) alpha_p alpha_q log p log q`

looks like a canonical interaction between every pair of prime coordinates. But all pair coefficients factor as a product of one-coordinate weights. Consequently every mixed second derivative is constrained by

`Q_(pq)^2 = Q_(pp) Q_(qq)`

up to the common normalization, and every finite principal matrix has only one nonzero eigenvalue. There is no independent `p,q` arithmetic datum in the interaction.

Equivalently, the deformation is a scalar functional calculus of the standard logarithmic Hamiltonian

`A e_n = (log n)e_n`:

on the coefficient basis its extra weight is `exp((t/4)A^2)`. In exponent coordinates `A` is exactly the linear energy `sum_p (log p) N_p`. Squaring it produces cross terms algebraically, but introduces no operator beyond a function of the same one-dimensional Hamiltonian. This is the same failure mode repeatedly encountered in this line: nonlinear functions of `log n` can look many-body after expanding in prime occupations while remaining spectrally one-dimensional.

## Extended-Selberg matched control

Dobner proves the analogue of Newman's non-negativity phenomenon for the extended Selberg class. This is an important matched control for the prime-lattice interpretation. The bare heat-threshold mechanism is not specific to the free commutative monoid generated by the rational primes; it belongs to a substantially broader completed-L-function setting with gamma factors, functional equations, and Dirichlet coefficients.

This does not make the de Bruijn–Newman constant irrelevant to zeta. For the Riemann xi-function the statement `Lambda=0` is exactly as difficult as RH after Rodgers–Tao. It does show that the existence of a heat deformation with a real-zero threshold cannot by itself be claimed as evidence for a unique hidden geometry of the rational-prime exponent lattice.

The rational-prime lattice enters Dobner's coefficient formula through `log n=<v(n),log p>`, but the same `log n` quadratic weight exists for general Dirichlet-series coefficients independently of whether the coefficients arise from the bare zeta Euler product.

## Critical line versus exponent geometry

The de Bruijn–Newman formulation centers the completed zeta function so that its nontrivial zeros correspond to zeros of an entire function in a real-variable normalization. The symmetry axis `Re(s)=1/2` is therefore already built into the completed functional equation before the heat parameter is introduced.

The hard theorem is whether the zeros at the undeformed time are all real, equivalently whether `Lambda=0`. The rank-one quadratic form does not derive the value `1/2` from the prime-exponent geometry. It evolves a centered entire function whose symmetry axis is already fixed by the completed zeta functional equation.

This distinction is important for the research mandate. A mechanism that merely rewrites the Newman deformation as an interaction among prime occupations would re-encode an existing RH-equivalent problem. To add structure, a lattice construction must explain a localization or positivity theorem that is not already equivalent to the statement that the undeformed xi zeros are real.

## Prior art and novelty audit

The main prior-art anchors are:

- **Brad Rodgers and Terence Tao**, “The De Bruijn-Newman constant is non-negative,” *Forum of Mathematics, Pi* **8** (2020), e6, arXiv:1801.05914. This is the primary modern source for the de Bruijn–Newman flow in the Riemann case, the threshold constant `Lambda`, and the theorem `Lambda>=0`; combined with the classical equivalence `RH <=> Lambda<=0`, it yields `RH <=> Lambda=0`.
- **Alexander Dobner**, “A proof of Newman's conjecture for the extended Selberg class,” *Acta Arithmetica* **201** (2021), 29–62, arXiv:2005.05142. This is the matched-control source for the extended-Selberg result and for the negative-time deformed Dirichlet-series coefficient carrying the Gaussian log-energy weight used in the exponent-lattice audit.

A targeted novelty search around de Bruijn–Newman heat flow, Dirichlet-series heat deformations, extended Selberg classes, and the `exp(c log^2 n)` coefficient weight found the heat mechanism and its broad L-function extension to be established prior art. No novelty is claimed for the heat flow, the Newman constant, the coefficient deformation, or the RH equivalence.

The durable line-specific result is the structural reduction

`exp((t/4)(log n)^2) = exp((t/4)<v(n),ell>^2)`

with rank-one quadratic form. This is an exact obstruction to treating the classical heat deformation as higher-rank prime-exponent geometry.

## Adversarial boundaries and counterarguments

1. **Rank one does not trivialize zero dynamics.** The zeros of `H_t` interact nonlinearly under the heat flow, and the theorem `Lambda>=0` is deep. The claim here concerns only what extra geometry the coefficient weight supplies on exponent space.

2. **The positive cone is not linearly quotient-identical under energy.** Because the numbers `log p` are rationally independent over the integers, `alpha -> <alpha,ell>` is injective on integer finite-support exponent vectors. Calling the deformation rank one refers to its quadratic differential/bilinear structure, not to collisions among integers.

3. **Do not infer a critical-strip Euler product.** The heat deformation is an entire-function construction. The Dirichlet-series representation used in the negative-time analysis has its own validity domain and does not license the Euler product beyond `Re(s)>1`.

4. **The functional equation supplies the symmetry axis, not the rank-one form.** The value `1/2` enters through completion and centering. The quadratic energy does not independently single it out.

5. **Universality across the extended Selberg class is a control, not a refutation of arithmetic content.** Individual L-functions still carry arithmetic coefficients and Euler products. The control only rules out claiming that the bare heat-threshold architecture uniquely encodes the rational-prime lattice.

6. **A higher-rank deformation would need an independent bridge theorem.** Replacing `<alpha,ell>^2` by an arbitrary quadratic form `alpha^T K alpha` can create transverse lattice geometry, but without a theorem linking the resulting flow to the completed zeta function or Weil positivity it is only an engineered re-encoding.

## Decisive falsification tests

This finding would be materially weakened by either of the following:

- a canonical de Bruijn–Newman-type zeta deformation whose coefficient action involves a quadratic or nonlocal form on `v(n)` that provably does **not** factor through `log n`, while retaining a theorem connecting its zero-reality threshold to RH; or
- a theorem showing that the classical heat deformation carries additional prime-local operator data, not recoverable from the scalar logarithmic Hamiltonian, and that this extra data participates essentially in the zero-localization theorem.

Absent such a bridge, expanding `(log n)^2` into prime-coordinate cross terms does not create a new multidimensional mechanism.

## Consequence for `prime_lattice`

The route

`classical Newman heat flow -> exp(c(log n)^2) -> pairwise prime couplings -> higher-dimensional prime-lattice RH mechanism`

is blocked at the third step: the apparent coupling matrix is an outer product and has rank one.

A surviving deformation-based direction would need a canonical higher-rank/nonlocal form on exponent space whose entries contain arithmetic information not factorizable as `f(log p)g(log q)`, together with an independent analytic-continuation or positivity theorem connecting that structure to the completed zeta zero divisor. Merely applying nonlinear functional calculus to the logarithmic Hamiltonian cannot supply that missing geometry.
