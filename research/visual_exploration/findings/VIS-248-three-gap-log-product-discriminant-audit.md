# VIS-248 — three-gap log-product conditioning reduces to a discriminant-weighted interval

## Claim

Continue the symmetric three-gap specialization of the alpha-free log-product conditional law in `VIS-247`. Let

`X=(X_1,X_2,X_3) ~ Dirichlet(alpha,alpha,alpha)`,

with `X_i>0` and `X_1+X_2+X_3=1`, and define the two nontrivial elementary symmetric coordinates

`P=X_1 X_2 X_3`,

`Q=X_1 X_2 + X_2 X_3 + X_3 X_1`.

Fix a regular product level

`0<p<1/27`,

or equivalently `Lambda=log p < -3 log 3`. Then the conditional law of `Q` given `P=p` is exactly

`f_(Q|P=p)(q)`
` = Z(p)^(-1) Delta_p(q)^(-1/2) 1_(q_-(p)<q<q_+(p))`,

where

`Delta_p(q)=q^2-4q^3-4p-27p^2+18pq`,

`q_-(p)<q_+(p)` are the two positive roots of `Delta_p(q)=0`, and

`Z(p)=integral_(q_-(p))^(q_+(p)) Delta_p(u)^(-1/2) du`.

The third root `q_0(p)` of `Delta_p(q)` is negative. The density is **exactly independent of `alpha`**.

Moreover, for every interior `(p,q)`, the unordered gap triple is the root multiset of

`t^3-t^2+q t-p=0`.

Thus, modulo permutation, a regular three-gap log-product level is one-dimensional and `Q` is a complete coordinate on it. The endpoint singularities of the conditional density are integrable inverse-square-root singularities. If

`c=(q_-+q_+)/2`,  `h=(q_+-q_-)/2`,

then the substitution

`q=c+h cos(theta)`,  `0<theta<pi`,

removes those endpoint singularities exactly:

`integral_(q_-)^(q_+) G(q) Delta_p(q)^(-1/2) dq`
` = (1/2) integral_0^pi G(c+h cos(theta)) [c+h cos(theta)-q_0]^(-1/2) dtheta`.

This gives a deterministic one-dimensional quadrature target for auditing any numerical sampler of the `VIS-247` conditional coarea law at `m=3`.

**Evidence/status:** `EXACT-DERIVED + LOW-DIMENSIONAL AUDIT LAW + REPRESENTATION QUOTIENT + NO-NOVELTY-CLAIM`.

No production sampler, high-dimensional validation, prime residual, new Dirichlet product-distribution theorem, or RH consequence is claimed.

## 1. The symmetric quotient coordinates

Write

`x=X_1`, `y=X_2`, `z=1-x-y=X_3`.

The monic cubic with roots `x,y,z` is

`(t-x)(t-y)(t-z)`
` = t^3-(x+y+z)t^2+(xy+yz+zx)t-xyz`
` = t^3-t^2+Q t-P`.

Consequently `(P,Q)` determines the unordered triple exactly. Away from repeated coordinates, the map from the labelled simplex to `(P,Q)` is six-to-one, once for each permutation of the three distinct roots.

The discriminant of the cubic `t^3-t^2+q t-p` is

`Delta_p(q)=q^2-4q^3-4p-27p^2+18pq`.

By the classical root formula for a monic cubic discriminant,

`Delta_p(q)`
` = (x-y)^2 (y-z)^2 (z-x)^2`.

Hence `Delta_p(q)>0` precisely on the regular part of the physical quotient, while `Delta_p(q)=0` at a collision of two gap coordinates.

For `0<p<1/27`, the physical quotient is the interval between the two positive roots `q_-(p),q_+(p)` of the discriminant polynomial. The third discriminant root is negative. The two physical endpoints are the two double-root configurations

`(a,a,1-2a)`

with

`a^2(1-2a)=p`,

one solution on each side of `a=1/3`. Their quotient coordinate is

`q=2a-3a^2`.

At the excluded maximum `p=1/27`, the interval collapses to the barycenter `(1/3,1/3,1/3)` and `q=1/3`, exactly matching the singular level excluded in `VIS-247`.

## 2. The root-to-coefficient Jacobian is the Vandermonde

In the ordinary simplex chart `(x,y)` with `z=1-x-y`, direct differentiation gives

`Q=-x^2-xy+x-y^2+y`,

`P=xy(1-x-y)`.

The Jacobian determinant is

`det partial(Q,P)/partial(x,y)`
` = (x-y)(x-z)(y-z)`.

Therefore

`|det partial(Q,P)/partial(x,y)|`
` = sqrt(Delta_P(Q))`.

This is the three-root specialization of the classical Vandermonde Jacobian behind the root-to-coefficient map. It also makes the quotient singularity transparent: the coordinate map loses rank exactly when two roots/gaps collide.

The labelled symmetric-Dirichlet density in the same simplex chart is proportional to

`(xyz)^(alpha-1)=P^(alpha-1)`.

Applying change of variables and summing the six labelled preimages gives the interior joint density, up to the Dirichlet normalizing constant,

`f_(P,Q)(p,q) proportional to 6 p^(alpha-1) Delta_p(q)^(-1/2)`.

Any constant factor arising from choosing induced affine-hyperplane measure instead of the `(x,y)` chart is global and cancels in the conditional law.

## 3. Conditioning on the product removes alpha explicitly

On a fixed product level `P=p`, the factor

`6 p^(alpha-1)`

is constant in `q`. Normalizing over the physical `q` interval therefore gives

`f_(Q|P=p)(q)`
` = Delta_p(q)^(-1/2) / integral_(q_-)^(q_+) Delta_p(u)^(-1/2) du`.

No `alpha` remains. Because `Lambda=log P` is a one-to-one transformation of `P`, the same formula is the pushforward of the `VIS-247` law conditioned on `Lambda=log p`.

This provides a low-dimensional exact audit of the coarea result from a different coordinate calculation. `VIS-247` derives the conditional measure geometrically on the level surface; here the three-gap symmetric quotient collapses that surface to a single interval and produces an ordinary one-dimensional density.

The result is stronger as a calibration check than merely confirming a moment. A correct symmetric three-gap sampler for the conditional law must reproduce the complete `Q` distribution above and assign the six permutations of each regular unordered triple symmetrically.

## 4. The apparent endpoint divergence is integrable and removable

Factor the discriminant using its three real roots:

`Delta_p(q)`
` = 4 (q-q_0)(q-q_-)(q_+-q)`

on the physical interval, where `q_0<0<q_-<q_+`.

Thus near either physical endpoint the density behaves like a constant times the inverse square root of the distance to that endpoint. The singularity is integrable but is awkward for naive uniform-`q` quadrature or histogram comparison.

Put

`q=c+h cos(theta)`,

with `c=(q_-+q_+)/2` and `h=(q_+-q_-)/2`. Then

`(q-q_-)(q_+-q)=h^2 sin^2(theta)`

and `|dq|=h sin(theta) dtheta`. Hence

`dq/sqrt(Delta_p(q))`
` = dtheta / [2 sqrt(q-q_0)]`,

with orientation reversed between the two endpoints. The endpoint square roots cancel exactly. Standard deterministic quadrature in `theta` therefore supplies a stable reference CDF, moments, and expectations without having to resolve an artificial integrable spike numerically.

For any permutation-symmetric statistic `F` of the three gaps, fixed `p` makes `F` a function `F_p(q)` of the quotient coordinate. Its exact conditional expectation is

`E[F | P=p]`
` = integral_(q_-)^(q_+) F_p(q) Delta_p(q)^(-1/2) dq`
`   / integral_(q_-)^(q_+) Delta_p(q)^(-1/2) dq`.

This includes the three-gap symmetric statistics used as low-dimensional controls in the current clue whenever their value depends only on the unordered gap triple.

## 5. Deterministic sampler audit

The accepted critical-logarithmic-occupancy clue requires any conditional sampler to be checked first in dimensions where deterministic integration is feasible. The three-gap case now supplies an exact target rather than a qualitative check.

For several predeclared values of `p` spanning central and more uneven gap configurations, a candidate sampler should be tested against:

- the exact support `[q_-(p),q_+(p)]`;
- the normalized discriminant-weighted CDF of `Q`;
- several low-order `Q` moments or other predeclared symmetric expectations evaluated by the nonsingular `theta` quadrature;
- the inverse-square-root endpoint mass implied by the exact density;
- permutation symmetry of the labelled sampled triples;
- the simplex and product constraints to numerical tolerance materially tighter than the eventual statistic error budget.

Passing these checks does not validate the sampler for large `m`; it removes a concrete class of implementation and weighting errors before high-dimensional use. In particular, a sampler that is uniform along the geometric level curve will generally fail this audit because the `VIS-247` coarea weight is not uniform.

## 6. Representation audit

**Collapse.** For `m=3`, fixed `sum X_i=1` and fixed product `P=p`, quotienting by permutations leaves only one continuous degree of freedom. The elementary symmetric coordinate `Q` captures it completely. Any apparent two-dimensional geometry of the labelled level curve is therefore partly representation redundancy.

**Survives.** The alpha-free conditional law survives the quotient nontrivially as the discriminant weight `Delta_p(q)^(-1/2) dq`. It is not flattened to uniform measure in the quotient coordinate, and the collision boundaries leave a precise integrable signature.

**Mixed.** The one-dimensional reduction is special to three components. For `m>3`, fixing the sum and product still leaves multiple independent elementary-symmetric coordinates, so this finding does not provide a high-dimensional sampler or justify projecting the production problem to one scalar coordinate.

The discriminant geometry is therefore useful here as an audit coordinate, not as a new arithmetic mechanism.

## 7. Prior art and novelty boundary

Every general ingredient in the derivation is classical. The symmetric Dirichlet density and its log-coordinate sufficient statistics are standard. Nadarajah and Kotz, *Exact and approximate distributions for the product of Dirichlet components*, Kybernetika 40:6 (2004), 735--744, is direct prior art that product distributions of Dirichlet components are established probability objects; this finding does not claim a new general product-distribution theory.

The identity between a polynomial discriminant and the squared Vandermonde product of its roots, the cubic discriminant formula, the elementary-symmetric root coordinates, and the multivariate change-of-variables Jacobian are also classical. A targeted literature audit found these ingredients in standard discriminant/change-of-variable references and found no basis for a novelty claim for the combined three-variable specialization.

The Mathia-specific value is narrower: `VIS-247` left a concrete validation obligation for an alpha-free conditional sampler. The present calculation turns its `m=3` case into an exact one-dimensional benchmark with explicit support, density, endpoint behavior, and a nonsingular quadrature representation. It is persisted as an audit law, not as a new theorem about Dirichlet products or cubic discriminants.

## Boundaries and falsification

The six-to-one change of variables holds only away from repeated roots; the discriminant-weighted density describes the regular interior, with the collision points appearing as integrable boundary singularities. The barycentric product `p=1/27` is singular and excluded.

The result assumes the one-parameter **symmetric** Dirichlet family. It does not apply unchanged to asymmetric Dirichlet parameters or richer spacing models whose density is not constant on a log-product level.

The quotient coordinate is complete only for unordered three-gap configurations at fixed product. Statistics sensitive to labels beyond the permutation symmetry of the null must retain the corresponding label/orientation information rather than silently replacing it by `Q`.

Falsify the density by finding a regular `(p,q)` whose six labelled preimages have a root-to-coefficient Jacobian not equal in absolute value to `sqrt(Delta_p(q))`, or by deriving a residual `alpha` factor after conditioning on `p`. Falsify the physical support description by producing a positive triple of sum one and product `p` whose `Q` lies outside `[q_-,q_+]`, or an interior `q` in that interval whose cubic fails to have three positive roots.

## Research consequence

The low-dimensional validation requirement in the accepted prime-phase critical-logarithmic-occupancy clue is now exact. A production conditional sampler should not be trusted merely because it preserves `sum X_i=1` and `Lambda`: at `m=3` it must also reproduce the discriminant-weighted quotient law above.

This closes the deterministic **audit target**, not the calibration problem itself. The next coherent thread is to implement or independently obtain a sampler for the `VIS-247` high-dimensional coarea law and require it to pass this three-gap benchmark before using it at the frozen critical prime parameters. That sampler/high-dimensional validation is intentionally not opened in this finding.