# VIS-206 — fixed-scale prime-ratio pair crowding vanishes by bounded local degree

## Claim

Keep the notation and hypotheses of `VIS-192`, `VIS-195`, and `VIS-205`. Fix `A>0` and suppose

`H=H(y)->infinity`,

`H log y / y -> 0`.

When `R_v(y,H)>0`, let

`nu(lambda)=|c_lambda|^2/R_v(y,H)`

be the coefficient-energy probability measure on

`Lambda_y={+/-log(q/p): p<q<=y, p,q prime}`,

and let

`Q_(y,H)(A)`
` = sum_(lambda!=mu, 0<|lambda-mu|<=A b_y) nu(lambda)nu(mu)`,

where

`b_y=log(1+2/y^2)`.

Then the fixed-scale near-collision graph

`G_A(y)={ {lambda,mu}: 0<|lambda-mu|<=A b_y }`

has uniformly bounded degree on its non-isolated vertices: for every fixed `A` there is a finite constant `d_A` such that, for all sufficiently large `y`, every `lambda` has at most `d_A` neighbors in `G_A(y)`.

Moreover every non-isolated frequency satisfies

`nu(lambda) <<_(A,alpha,v) H (log y)^2/y^2`.

Consequently

`Q_(y,H)(A) <<_(A,alpha,v) H (log y)^2/y^2 -> 0`.

For the autocorrelation-taper subclass of `VIS-203`, `VIS-205` therefore gives

`S_(y,H)(A)/R_v(y,H)^2 -> 0`

for every fixed `A`, throughout the full strictly subcritical regime above.

Thus the fixed normalized shell-energy obstruction left by `VIS-203`--`VIS-205` is automatically dilute at strictly subcritical scales. The square-root-log limitation of `VIS-202` belongs to the stronger one-sided crowding resource `C_(y,H)(A)` and its four-form sieve proof; it is **not** an obstruction to the weaker two-sample energy `Q_(y,H)(A)`.

**Evidence/status:** `EXACT-DERIVED + BOUNDED-DEGREE INCIDENCE + PNT NORMALIZATION + STRUCTURAL ESCAPE + NO-NOVELTY-CLAIM`.

No estimate `C_(y,H)(A)->0`, no proof that `D_v(y,H)=o(y^2)`, no uniform finite-start theorem below the `VIS-194` Hilbert horizon, and no control of windows with `A=A(y)->infinity` are claimed.

## 1. A dangerous frequency has only boundedly many dangerous neighbors

For `A<1`, `VIS-195` already gives no distinct pair at distance at most `A b_y`, because every distinct pair is separated by at least `b_y`. So assume `A>=1`.

Take a fixed signed frequency

`lambda=epsilon log(q/p)`,

with `p<q<=y` prime, and suppose it has a neighbor

`mu=eta log(s/r)`

satisfying

`0<|lambda-mu|<=A b_y`.

`VIS-195` shows that, for fixed `A` and all sufficiently large `y`, every such pair is represented by one of the determinant relations

`|qr-ps|=h`

or

`|qs-pr|=h`,

where

`h in {2,4,...,2 floor(A)}`,

and all four primes are macroscopic:

`p,q,r,s >= c_A y`

for some fixed `c_A>0` depending only on `A`. For example, the product lower bound in `VIS-195` permits a positive constant of order `1/A` after increasing the large-`y` threshold.

Now fix `p,q`, one admissible `h`, and one sign of the determinant.

For the same-sign relation

`q r - p s = +/- h`,

`gcd(p,q)=1`, and once one integer solution `(r_0,s_0)` is chosen all integer solutions are

`r=r_0+p t`,

`s=s_0+q t`,

with `t in Z`.

Because `p>=c_A y` and `0<r<=y`, only `O_A(1)` integer values of `t` are possible. Imposing primality and `r<s<=y` can only reduce that number.

For the opposite-sign relation

`q s - p r = +/- h`,

the integer solutions have the corresponding form

`r=r_0+q t`,

`s=s_0+p t`,

so again only `O_A(1)` values of `t` can lie in the prime box.

There are only finitely many choices of `h`, determinant sign, and relative frequency sign at fixed `A`. Hence every non-isolated `lambda` has at most

`d_A=O_A(1)`

neighbors. No prime-tuple estimate or determinant-surface asymptotic is required: at the fixed `y^-2` normalized scale, fixing one prime ratio turns each determinant fiber into a one-dimensional lattice whose step size is already comparable with the full box.

## 2. Every dangerous vertex carries vanishing individual coefficient energy

For a signed frequency represented by the prime pair `p<q`, `VIS-192` gives

`|c_lambda|^2`
` = Q_y^(-2) p^(-2alpha) q^(-2alpha)`
`   |kappa_v(H log(q/p))|^2`,

where

`Q_y=sum_(p<=y) p^(-2alpha)`.

Because the taper `v` is fixed and has nonzero integral,

`|kappa_v(theta)| <= ||v||_1/|int_0^1 v| = O_v(1)`

uniformly in `theta`.

A non-isolated frequency belongs to a dangerous pair, so Section 1 and `VIS-195` give

`p,q >= c_A y`.

Therefore, using `0<=alpha<1/2`,

`|c_lambda|^2`
` <<_(A,alpha,v) Q_y^(-2) y^(-4alpha)`.

The prime number theorem with partial summation gives

`Q_y asymp_alpha y^(1-2alpha)/log y`.

Hence every dangerous vertex satisfies

`|c_lambda|^2 <<_(A,alpha,v) (log y)^2/y^2`.

On the other hand, the matching lower estimate in `VIS-192` gives, under

`H->infinity`, `H log y/y->0`,

`R_v(y,H) >>_(alpha,v) 1/H`.

Dividing yields

`nu(lambda)`
` = |c_lambda|^2/R_v(y,H)`
` <<_(A,alpha,v) H (log y)^2/y^2`

for every vertex that participates in a fixed-`A` dangerous collision.

The right-hand side tends to zero because

`H (log y)^2/y^2`
` = (H log y/y)(log y/y) -> 0`.

This is the key distinction from the one-sided statistic `C(A)`: even if a non-negligible total `nu`-mass were distributed across frequencies that each have a dangerous neighbor, no single dangerous vertex can carry macroscopic normalized energy in the strictly subcritical regime.

## 3. Bounded degree converts the pointwise energy bound into `Q(A)->0`

For each `lambda`, let

`N_A(lambda)={mu!=lambda: |lambda-mu|<=A b_y}`.

By Section 1,

`#N_A(lambda)<=d_A`

whenever the set is nonempty. Let

`m_A(y,H)=max{nu(mu): N_A(mu) nonempty}`,

with `m_A=0` if there are no dangerous pairs. Then

`sum_(mu in N_A(lambda)) nu(mu) <= d_A m_A`.

Therefore

`Q_(y,H)(A)`
` = sum_lambda nu(lambda) sum_(mu in N_A(lambda)) nu(mu)`
` <= d_A m_A sum_lambda nu(lambda)`
` = d_A m_A`.

Section 2 gives

`m_A <<_(A,alpha,v) H (log y)^2/y^2`,

so

`Q_(y,H)(A) <<_(A,alpha,v) H (log y)^2/y^2 ->0`.

This estimate uses neither cancellation between determinant fibers nor an upper-bound sieve for four simultaneous prime forms. It exploits a different geometry: after one prime-ratio vertex is fixed, fixed-scale determinant proximity leaves only boundedly many lattice positions for the second vertex, while the normalized coefficient energy of each top-scale vertex tends to zero.

## 4. Consequence for the noncancelling shell-energy route

For the autocorrelation-taper subclass of `VIS-203`, the exact shell amplitudes are nonnegative. `VIS-204` bounds every dangerous exact-shell multiplicity by four, and `VIS-205` proves

`Q_(y,H)(A)`
` <= S_(y,H)(A)/R_v(y,H)^2`
` <= 4 Q_(y,H)(A)`.

The bound above therefore implies

`S_(y,H)(A)`
` <<_(A,alpha,v) R_v(y,H)^2 H (log y)^2/y^2`
` = o(R_v(y,H)^2)`

for every fixed `A` in the strictly subcritical regime.

This closes the fixed-normalized-scale necessary shell-energy condition highlighted by `VIS-203`. It does **not** by itself prove a uniform subquadratic finite-start theorem: the full error also contains shells outside every fixed multiple of `b_y`, and a finite window introduces the sinc weight across those larger scales.

The result also does not imply the stronger `VIS-195` criterion `C(A)->0`. A bounded-degree graph can have positive total vertex mass while every individual vertex mass tends to zero; its two-sample edge mass can nevertheless vanish. This is exactly the separation between `Q` and `C` isolated abstractly in `VIS-205`, now realized structurally by the actual prime-ratio coefficient profile at the level needed for the upper bound.

## Prior-art audit

The parametrization of integer solutions to a two-variable linear Diophantine equation is classical: after one solution is fixed, all others lie on a one-dimensional arithmetic progression with step determined by the coprime coefficients. The bounded-degree argument above is only this elementary fact applied after `VIS-195` has forced `p,q` to be proportional to the box size.

Determinant surfaces themselves have substantial prior art. Satadal Ganguly and Rachita Guria, **Distribution of integer points on determinant surfaces and a mod-p analogue**, *Mathematika* 72 (2026), DOI `10.1112/mtk.70093`, obtain asymptotic formulas for smoothly weighted integer solutions of `xy-zw=r`. Rachita Guria, **An asymptotic formula with power-saving error term for counting prime solutions to a binary additive problem**, arXiv `2410.10856`, studies the same determinant equation with two entries restricted to primes. These sources were already identified in `VIS-195` and confirm that determinant-surface counting is not new.

The present proof does not use or improve those counting theorems. It freezes one prime-ratio vertex first, reducing the relevant fixed-scale fiber to a linear Diophantine progression, and then combines the resulting bounded local degree with the explicit `VIS-192` coefficient normalization. The prime-number-theorem estimate for `Q_y` and the lower variance estimate are likewise classical or already established inputs. No novelty is claimed for any of these ingredients separately.

The Mathia-specific content is the synthesis showing that the weaker two-sample crowding resource introduced in `VIS-205` vanishes throughout the strictly subcritical regime even though the stronger one-sided crowding route of `VIS-195`--`VIS-202` encounters a square-root-log method threshold.

## Boundaries and falsification

The fixed-`A` hypothesis is essential. If `A=A(y)` grows, the determinant difference `h`, the number of allowed fibers, the lower bound on participating primes, and the local graph degree can all grow. The proof gives no uniform statement in such a widening collision window.

The lower normalization `R_v>>1/H` uses the strictly subcritical hypothesis `H log y/y->0` from `VIS-192`. Without a comparable lower bound on `R_v`, the normalized measure `nu` could in principle concentrate more strongly even though the raw top-scale coefficients remain small.

The bounded-degree statement concerns the graph of approximate prime-ratio collisions at scale `A b_y`, not the exact-difference-shell representation multiplicity of `VIS-204`. They are different combinatorial objects: the former fixes one frequency and counts nearby frequencies; the latter fixes a difference shell and counts representations of that shell.

No conclusion is drawn about `C(A)` or `D_v`. In particular this finding does not contradict the `VIS-202` threshold, because that threshold is explicitly a limitation of a proof architecture for the stronger one-sided crowding mass.

Falsify the finding by producing, for fixed `A`, a dangerous prime-ratio vertex with an unbounded number of dangerous neighbors as `y->infinity`; a close pair not covered by the bounded-determinant/top-scale reduction of `VIS-195`; an incorrect Diophantine progression step; or a failure of the coefficient or variance normalizations imported from `VIS-192`.

## Research consequence

The fixed-scale shell-packing question posed after `VIS-205` is resolved positively throughout the strictly subcritical regime: the dangerous two-sample mass and, for autocorrelation tapers, the associated exact-shell energy are `o(1)` after normalization.

The live boundary therefore moves outward in scale. To obtain a uniform finite-start theorem below the coarse Hilbert horizon, the next question is how the shell-energy estimate behaves when the normalized collision width grows with `y`, or how the sinc-weighted contribution from the intermediate region between order `y^-2` and the eventual dephasing scale can be summed. Reopening the fixed-`A` four-prime sieve route would address a stronger resource than this shell-energy problem now requires.