# VIS-250 — regular log-product triple Gibbs moves form one global communication class

## Claim

Continue the exact conditioned surface and three-coordinate Gibbs kernel of `VIS-247`--`VIS-249`. For `m>=3` and

`lambda < -m log m`, 

let

`S_lambda={x_i>0 : sum_i x_i=1, sum_i log x_i=lambda}`

and let `mu_lambda` be the alpha-free conditional law

`mu_lambda(dx)=Z(lambda)^(-1) J(x)^(-1) d sigma_lambda(x)`.

Assume the random-scan heat-bath kernel of `VIS-249` chooses every coordinate triple with a fixed state-independent positive probability and resamples that triple from its exact conditional law.

Then three global facts hold.

1. `S_lambda` is connected; in fact it is homeomorphic to the sphere `S^(m-2)`.
2. Finite concatenations of regular three-coordinate sum/product-preserving moves connect every pair of points of `S_lambda`.
3. The exact random-scan triple heat-bath chain is `mu_lambda`-irreducible. In particular it is topologically irreducible: from every starting point, every nonempty open subset of `S_lambda` is reached with positive probability in finitely many steps.

Thus the structural gap left open in `VIS-249` is not a disconnected-component or hidden communication-class obstruction. The remaining calibration problem is quantitative: useful mixing time, bottlenecks/conductance, numerical implementation accuracy, and Monte Carlo error remain completely open.

**Evidence/status:** `EXACT-DERIVED + CONNECTED SUPPORT + GLOBAL BLOCK ACCESSIBILITY + MU-IRREDUCIBILITY + CLASSICAL ORBIT/GIBBS GEOMETRY SPECIALIZATION + NO-NOVELTY-CLAIM`.

No spectral gap, geometric-ergodicity rate, practical burn-in bound, numerical sampler validation, prime residual, or RH consequence is claimed.

## 1. The regular log-product level is connected

Work in the affine hyperplane

`H={x in R^m : sum_i x_i=1}`

and define

`G(x)=sum_i log x_i`

on the open simplex. The function `G` is strictly concave and has its unique maximum at the barycenter

`b=(1/m,...,1/m)`,

where `G(b)=-m log m`.

For fixed `lambda<-m log m`, consider the superlevel set

`C_lambda={x in H : x_i>0, G(x)>=lambda}`.

Because a superlevel set of a concave function is convex, `C_lambda` is convex. It is compact inside the open simplex: approaching any simplex face forces one coordinate to zero and hence `G(x)->-infinity`. The barycenter is an interior point of `C_lambda`, and

`partial_H C_lambda = S_lambda`.

Every ray in `H` starting at `b` meets the boundary of the compact convex body `C_lambda` exactly once in each direction. Radial projection from `b` therefore identifies `S_lambda` with the unit sphere in the `(m-1)`-dimensional tangent space of `H`, namely `S^(m-2)`.

Hence `S_lambda` is connected for every `m>=3`. This also makes explicit why the excluded value `lambda=-m log m` is special: the level collapses to the single barycenter.

## 2. Triple-fiber vector fields span everywhere

For a coordinate triple `B={i,j,k}`, put `q_l=1/x_l` and define the smooth vector field

`V_ijk(x)`
` = (q_j-q_k)e_i + (q_k-q_i)e_j + (q_i-q_j)e_k`.

It changes only the selected triple and satisfies identically

`sum_l (V_ijk)_l = 0`,

`sum_l q_l (V_ijk)_l = 0`.

Therefore its local flow preserves both the simplex sum and `G=sum log x`; all coordinates outside the selected triple stay fixed. Its integral curves are admissible three-coordinate sum/product-preserving motions of exactly the type underlying the `VIS-249` heat-bath conditionals.

At any point of `S_lambda`, the reciprocal vector `q` is not constant because the barycenter is not on the level. Choose `a,b` with `q_a!=q_b`. `VIS-249` proves that the `m-2` vectors

`V_abk(x)`, `k notin {a,b}`,

are a basis of `T_x S_lambda`.

This pointwise spanning statement already upgrades the local rank result to global deterministic accessibility.

## 3. Every triple-flow accessibility class is open

Let `O(x)` be the set of points reachable from `x` by a finite concatenation of local flows of the fields `V_ijk`, allowing positive or negative flow times whenever the local flow is defined.

At a fixed `x`, choose `a,b` as above and enumerate the remaining indices `k_1,...,k_(m-2)`. Let `phi_r^t` be the local flow of `V_abk_r`, and form the endpoint map

`Phi(t_1,...,t_(m-2))`
` = phi_(m-2)^(t_(m-2)) o ... o phi_1^(t_1)(x)`.

At the origin, the derivative columns of `Phi` are precisely

`V_abk_1(x),...,V_abk_(m-2)(x)`,

which form a basis of the tangent space. The inverse-function theorem therefore gives a neighborhood of `0` whose image contains an open neighborhood of `x` in `S_lambda`. Consequently `O(x)` is open.

Reachability by finite reversible local flows is an equivalence relation, so the sets `O(x)` partition `S_lambda` into disjoint open classes. Since `S_lambda` is connected, there can be only one such class.

Thus every two states on the regular log-product level are connected by a finite sequence of admissible triple-fiber motions.

This is the elementary full-rank specialization of the classical orbit theorem for families of vector fields; no new general controllability theorem is claimed.

## 4. The exact heat-bath chain has full open-set support

For every nondegenerate selected triple, `VIS-248` and `VIS-249` give the exact one-dimensional conditional law on its fixed-sum/fixed-product fiber. In the discriminant coordinate `Q` the density is proportional to `Delta_p(Q)^(-1/2)` on its support, with symmetric labeling of the roots. Equivalently, on the labeled regular fiber the conditional measure assigns positive mass to every nonempty open arc.

Take a starting state `x` and a nonempty open target set `U`. By the global accessibility result above, choose a finite sequence of triple flows sending `x` to some `y in U`. Around each desired point on each fiber segment, the corresponding exact heat-bath conditional gives positive probability to a sufficiently small arc. By continuity of the finite composition, the arcs can be chosen so that any sequence of draws inside them ends in `U`.

The prescribed triple sequence itself has positive probability because every triple-selection weight is positive. Hence for some finite `n`,

`K^n(x,U)>0`.

The exact chain is therefore topologically irreducible on the whole regular conditioned surface.

## 5. Local smoothing upgrades this to `mu_lambda`-irreducibility

The target measure `mu_lambda` is equivalent to surface measure on `S_lambda`. Indeed

`J(x)^2=sum_i x_i^(-2) - (1/m)(sum_i x_i^(-1))^2`

vanishes only when all coordinates are equal, which is impossible on a regular level `lambda<-m log m`. Since `S_lambda` is compact, `J^-1` is positive and finite everywhere on the level.

At any state `z`, choose `a,b` with `q_a!=q_b`. For the `m-2` basis blocks `{a,b,k}`, restrict each exact block conditional to a small regular arc around the current block state and use a smooth local flow coordinate on that arc. The conditional law has positive density in that coordinate. Composing the `m-2` block updates gives the same endpoint map as in the inverse-function argument above; its Jacobian has full rank at the zero move.

Therefore a finite-step transition law from `z` has an absolutely continuous component with strictly positive surface density on some neighborhood of `z`.

Now let `A` be measurable with `mu_lambda(A)>0`. Choose a surface-density point `y` of `A`. Global triple-flow accessibility supplies a finite admissible route from any starting `x` to `y`; append the local full-rank block sequence at `y`. Restricting the exact heat-bath draws to small neighborhoods of the corresponding flow parameters gives positive joint probability, and the full-rank endpoint map produces positive surface density on a neighborhood of `y`. Since `y` is a density point of `A`, that neighborhood meets `A` in positive surface measure.

Thus for every `x` and every `A` with `mu_lambda(A)>0`, some finite `n` satisfies

`K^n(x,A)>0`.

So the exact random-scan chain is `mu_lambda`-irreducible.

## 6. Prior art and novelty boundary

Héctor J. Sussmann, **Orbits of families of vector fields and integrability of distributions**, *Transactions of the American Mathematical Society* 180 (1973), 171--188, DOI `10.1090/S0002-9947-1973-0321133-2`, is the classical general orbit-theorem reference. The argument above does not claim a new orbit theorem; because the admissible fields already span the full tangent space pointwise, the needed open-orbit conclusion follows directly from the inverse-function theorem and connectedness.

J. P. Hobert, C. P. Robert, and C. Goutis, **Connectedness conditions for the convergence of the Gibbs sampler**, *Statistics & Probability Letters* 33:3 (1997), 235--240, is direct prior art on support connectedness and Gibbs convergence. Luke Tierney, **Markov Chains for Exploring Posterior Distributions**, *The Annals of Statistics* 22:4 (1994), 1701--1762, DOI `10.1214/aos/1176325750`, remains the general-state-space Gibbs/MCMC background already used in `VIS-249`.

The persisted value here is Mathia-specific: the particular log-product surface is explicitly connected, the particular three-coordinate fibers from `VIS-249` generate one global accessibility class, and the exact discriminant conditionals then give `mu_lambda`-irreducibility. No novelty is claimed for the surrounding control or Gibbs theory.

## Boundaries and falsification

The result assumes `m>=3`, a regular level `lambda<-m log m`, exact block conditionals, and fixed state-independent triple-selection probabilities that are positive for every coordinate triple. A restricted block family can fail to span globally, and state-dependent selection requires a separate invariant/communication analysis.

The result concerns the exact mathematical kernel. A floating-point implementation may violate the fixed product, distort the `VIS-248` conditional, accumulate root-selection bias, or otherwise fail to realize this chain.

Irreducibility is qualitative. It does not bound the probability of traversing narrow regions, conductance, autocorrelation time, integrated effective sample size, or the number of updates needed to forget an initialization. A chain can be irreducible and still mix far too slowly for the proposed calibration.

Falsify connectedness by exhibiting a second component of the regular level despite the convex-superlevel argument. Falsify global accessibility by finding a regular state where the `VIS-249` basis directions fail or by identifying an invariant preserved by every triple flow but not constant on `S_lambda`. Falsify `mu_lambda`-irreducibility by showing that an exact nondegenerate block conditional loses support on an open fiber arc or that the local composed kernel lacks the claimed full-dimensional absolutely continuous component.

## Research consequence

The exact triple Gibbs proposal no longer has a structural communication-class ambiguity: on every regular conditioned level it has connected support, one deterministic triple-flow orbit, and an irreducible exact heat-bath chain.

The accepted critical-logarithmic-occupancy clue therefore remains live but becomes more sharply computational. The next coherent thread is still to implement the frozen `VIS-249` kernel, verify each block against the exact `VIS-248` law, and measure actual high-dimensional convergence from separated starting states. Failure to mix within the declared calibration budget would now indicate a quantitative bottleneck, metastability, or implementation problem rather than a disconnected exact state space.
