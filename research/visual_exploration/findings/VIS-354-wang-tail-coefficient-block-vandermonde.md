# VIS-354 — the bounded Wang tail-coefficient map is a source-free block Vandermonde map

## Claim

Consider the finite translated-dilate Wang bank from `VIS-349`

`M_X(xi)=sum_j c_(j,X) exp(-i b_(j,X) xi) m(a_(j,X) xi)`,

with `a_(j,X)>0`, frequency-independent coefficients, and

`m(xi)=4(1+i xi)/(4+xi^2)`.

Fix a finite asymptotic depth `q>=1`. For one translation fiber `b`, write

`x_j=a_(j,X)^(-1)`

for the distinct inverse scales in that fiber and let `c_b` be their coefficient vector. The polynomial coefficient data in

`Q_(b,q,X)(xi)=sum_(k=1)^q beta_k S_(b,k,X) xi^(q-k)`

are exactly

`d_b = D_beta V_b c_b`,

where

`(V_b)_(k,j)=x_j^k`, `1<=k<=q`,

and `D_beta=diag(beta_1,...,beta_q)` is invertible because every Wang tail coefficient `beta_k` is nonzero.

Thus the complete raw polynomial-coefficient vector of `E_(q,X)` is a direct sum of ordinary truncated Vandermonde moment maps over the translation fibers. **The arithmetic source `G`, `theta`, and the Wang output do not enter this map at all.**

More precisely:

1. If a fiber has `n_b<=q` active distinct scales, then `V_b` has full column rank. If in addition all inverse scales lie in a fixed compact interval `[r,R] subset (0,infinity)` and satisfy `|x_j-x_l|>=eta>0`, then there is a uniform constant `sigma>0` such that

   `||d_b||_2 >= sigma ||c_b||_2`.

   Hence a fixed nondegenerate bounded scale geometry cannot create an asymptotically small Wang polynomial-coefficient vector relative to the bank weights.

2. If `n_b>q`, then `V_b` has rank `q` and kernel dimension `n_b-q`. Exact membership in that kernel is precisely the familiar moment cancellation

   `sum_j c_j a_j^(-k)=0`, `k=1,...,q`.

   Near-kernel smallness is approximate moment cancellation of the same source-free filter-design equations. It is not evidence of source localization.

3. Across distinct translations the coefficient map is block diagonal. Phase geometry acts only at the later map from these polynomial coefficients to the confluent exponential polynomial `E_(q,X)`, whose bounded collision and inter-cluster losses are already priced by `VIS-351`--`VIS-353`.

Consequently, under the accepted clue's **frequency-independent, source-independent finite-bank model**, there is no remaining mysterious “source-to-polynomial-coefficient map.” There is only a bank-weight-to-tail-coefficient Vandermonde map. Any genuinely source-specific coefficient collapse requires the bank weights, scales, translations, or another selection rule to depend on `G` or equivalent arithmetic information; that is a different source-dependent mechanism and must be proved as such.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL VANDERMONDE/MOMENT MAP + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding does not rule out growing scale count, growing tail depth, inverse scales escaping every compact set, scale collisions, source/frequency-dependent coefficients, infinite representations, or direct signed arithmetic cancellation.

## 1. Exact coefficient map

`VIS-349` gives, for each translation `b`,

`S_(b,k,X)=sum_(j:b_j=b) c_(j,X) a_(j,X)^(-k)`

and

`Q_(b,q,X)(xi)=sum_(k=1)^q beta_k S_(b,k,X) xi^(q-k)`.

Set `x_j=a_j^(-1)`. The vector of moments is

`S_b=(S_(b,1,X),...,S_(b,q,X))^T = V_b c_b`,

with `V_b=(x_j^k)`. Multiplication by the fixed invertible diagonal matrix `D_beta` only rescales these coordinates. Therefore every question about small raw polynomial coefficients is exactly a question about the truncated power-moment map of the chosen bank.

Nothing in this algebra depends on the actual source function `G`. The source is acted on by the resulting multiplier after the bank has been specified; it does not alter the coefficient map unless the bank itself is selected from source information.

## 2. Fixed nondegenerate scale geometry has a uniform lower singular value

Suppose `n_b<=q` and the inverse scales are distinct. The first `n_b` rows of `V_b` form the square matrix

`(x_j^k)_(1<=k,j<=n_b)`.

Its determinant is

`(prod_j x_j) prod_(j<l)(x_l-x_j)`,

which is nonzero. Hence `V_b` has full column rank.

Now restrict the scale geometry to

`r<=x_j<=R`,
`|x_j-x_l|>=eta`.

The admissible ordered configurations form a compact set. The smallest singular value of `D_beta V_b` is a continuous positive function on that set, so it has a positive minimum. This proves the uniform lower bound

`||d_b||_2 >= sigma ||c_b||_2`.

Therefore a polynomially small coefficient vector in a bounded fixed-dimensional fiber must be paid for by leaving this compact regime, by making the coefficient vector itself small under the chosen normalization, or by moving toward a genuine moment nullspace when more scales than constrained moments are present.

## 3. Extra scales create exactly the known moment nullspace

If `n_b>q`, choose any `q` columns of `V_b`. The corresponding `q x q` minor has the same nonzero Vandermonde determinant form, so `rank V_b=q`. Hence

`dim ker V_b=n_b-q`.

A coefficient vector lies in the kernel exactly when

`S_(b,1,X)=...=S_(b,q,X)=0`.

This is not a new source-mediated collapse. It is the exact scale-moment cancellation already identified in `VIS-343` and separated fiberwise in `VIS-344`. Choosing coefficients close to the kernel gives approximate cancellation of those same moments. Pushing the first surviving Wang tail order further requires more moment constraints and therefore more active scales, exactly the resource already counted by the earlier scale-count obstruction.

Thus the remaining conditioning of the coefficient map is completely visible in bank geometry: number of scales, their relative positions/range, and proximity to the ordinary moment nullspace.

## 4. Separate the two finite-dimensional maps

The bounded finite-bank chain now factors conceptually into two different maps:

`bank weights -> tail polynomial coefficients -> confluent exponential function`.

The first map is the block Vandermonde map proved above. The second is the phase/confluent geometry studied in `VIS-349`--`VIS-353`.

`VIS-351` removes raw phase-Vandermonde coordinate blow-up, `VIS-352` charges bounded phase collisions by their Hermite collision scale, and `VIS-353` gives a lower Riesz floor for a fixed separated family of stable cluster blocks. The current result shows that the upstream coefficient stage has no hidden arithmetic channel either: in a source-independent bank it is ordinary scale-moment linear algebra.

A candidate may still leave the compact regime. For example, inverse-scale ratios may diverge, scales may collide, the number of scales or tail depth may grow, or bank parameters may be chosen from the source. Those are explicit resources, not unexplained conditioning.

## 5. Source dependence must be stated as source dependence

Suppose a proposed construction chooses `c_(j,X)`, `a_(j,X)`, or `b_(j,X)` using `G`, `theta`, signs of the arithmetic remainder, or another source statistic. Then the resulting small coefficient vector can genuinely carry source information, but the mechanism is no longer a fixed source-independent filter.

Such a proposal must state the dependence explicitly and prove the corresponding signed/arithmetic estimate. In particular it cannot cite small `Q_(b,q,X)` coefficients as if they arose from passive Wang smoothing. The information used to choose the bank is part of the mathematical input and must survive the destination audit, including the `Q'`/inverse-derivative repayment identified earlier.

## Prior-art audit

The linear algebra is classical and already audited inside this line. `VIS-343` anchors cancellation of asymptotic powers by multiscale linear combinations to Avram Sidi, **The Richardson Extrapolation Process with a Harmonic Sequence of Collocation Points**, *SIAM Journal on Numerical Analysis* 37:5 (2000), 1729--1746, DOI `10.1137/S0036142998340137`, and derives the ordinary Vandermonde determinant for Wang's inverse-scale moments. `VIS-344` gives the phase-fiber decomposition. No novelty is claimed for Vandermonde matrices, moment nullspaces, singular-value compactness, Richardson extrapolation, or block-diagonal linear maps.

The Mathia-specific content is the bookkeeping consequence for the current Wang frontier: after `VIS-349` exposed the raw polynomial coefficients, their allegedly remaining source-to-coefficient conditioning is in fact source-free under the fixed-bank assumptions.

## Dependencies

- `VIS-333`: exact Wang multiplier and source transfer.
- `VIS-343`: inverse-scale moment/Vandermonde cancellation ceiling.
- `VIS-344`: translation-fiber decomposition of moment cancellation.
- `VIS-349`: exact polynomial coefficient formula `Q_(b,q,X)`.
- `VIS-351`--`VIS-353`: stable phase-collision coordinates, local collision budget, and separated-block Riesz floor.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed here.

## Research consequence

The bounded source-independent finite-bank branch is narrower than the clue previously stated. **Once the bank is fixed independently of the arithmetic source, its raw Wang tail coefficients cannot acquire hidden source-specific smallness: they are exactly block-Vandermonde moments of the bank weights.**

Future work should not treat the “source-to-polynomial-coefficient map” as a separate bounded conditioning loophole. A surviving mechanism must expose an explicit escaping resource — growing scale/depth/count, degenerating scale geometry, growing/global phase geometry, shrinking windows — or cross the boundary into source/frequency-dependent selection, infinite representation, or direct signed arithmetic structure. Those branches remain open and require their own quantitative tests.