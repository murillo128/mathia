# VIS-205 — dangerous exact-shell energy is equivalent to two-sample crowding

## Claim

Keep the autocorrelation-taper setting of `VIS-203` and the fixed dangerous scale of `VIS-195` and `VIS-204`. Thus

`R=R_v(y,H)=sum_lambda b_lambda^2`,

`nu(lambda)=b_lambda^2/R`

when `R>0`, and

`B_xi=sum_(lambda-mu=xi) b_lambda b_mu >=0`.

Put

`b_y=log(1+2/y^2)`

and, for fixed `A>0`, define the normalized two-sample crowding mass

`Q_(y,H)(A)`
` = sum_(lambda!=mu, 0<|lambda-mu|<=A b_y) nu(lambda)nu(mu)`.

Also define the dangerous exact-shell energy

`S_(y,H)(A)=sum_(0<|xi|<=A b_y) B_xi^2`.

Then for every fixed `A`, all sufficiently large `y` satisfy

`Q_(y,H)(A)`
` <= S_(y,H)(A)/R^2`
` <= 4 Q_(y,H)(A)`.

Hence

`S_(y,H)(A)=o(R^2)`

if and only if

`Q_(y,H)(A)->0`

for every fixed `A` under consideration.

The comparison is exact up to the factor `4` from `VIS-204`; no spacing or prime-counting estimate is used beyond its bounded exact-shell multiplicity.

Moreover, if `C_(y,H)(A)` is the one-sample nearest-neighbor crowding mass from `VIS-195`, then

`Q_(y,H)(A) <= C_(y,H)(A)`

and therefore

`S_(y,H)(A)/R^2 <= 4 C_(y,H)(A)`.

Consequently the `VIS-195` sufficient resource

`D_v(y,H)=o(y^2)`

already implies vanishing dangerous exact-shell energy at every fixed normalized scale.

The converse implication is **not** available from probability theory alone. `Q(A)` weights both members of a close pair, whereas `C(A)` charges the entire mass of a frequency as soon as it has any close neighbor. Thus the shell-energy route is genuinely weaker than the nearest-neighbor Hilbert route: it can in principle succeed even when a substantial coefficient mass has close but extremely light partners.

**Evidence/status:** `EXACT-DERIVED + WEIGHTED-ENERGY REDUCTION + STRUCTURAL FRONTIER + NO-NOVELTY-CLAIM`.

No estimate proving `Q_(y,H)(A)->0`, no improvement of the `VIS-202` square-root-log threshold, and no claim that the abstract separation between `Q` and `C` is actually realized by the prime-ratio weights are made.

## 1. Shell energy is a representation-function second moment

For a fixed nonzero difference shell `xi`, let

`P_xi={(lambda,mu): lambda-mu=xi}`

and write

`x_(lambda,mu)=b_lambda b_mu >=0`.

Then

`B_xi=sum_(P_xi) x_(lambda,mu)`.

Because the summands are nonnegative,

`sum_(P_xi) x_(lambda,mu)^2 <= B_xi^2`.

By `VIS-204`, for fixed `A` and all sufficiently large `y`, every nonzero shell with

`|xi|<=A b_y`

has at most four ordered representations. Cauchy--Schwarz therefore also gives

`B_xi^2 <= 4 sum_(P_xi) x_(lambda,mu)^2`.

Summing over all dangerous nonzero shells partitions exactly the ordered pairs satisfying

`0<|lambda-mu|<=A b_y`.

Hence

`sum_(lambda!=mu, close) b_lambda^2 b_mu^2`
` <= S_(y,H)(A)`
` <= 4 sum_(lambda!=mu, close) b_lambda^2 b_mu^2`.

Dividing by

`R^2=(sum_lambda b_lambda^2)^2`

produces the claimed comparison with `Q_(y,H)(A)`.

The point is that after `VIS-203` removes sign cancellation and `VIS-204` removes large exact-fiber multiplicity, the shell `l^2` problem has no hidden representation-theoretic amplification left at fixed normalized scale. It is, up to a universal constant, simply the probability that two independent draws from the coefficient-energy measure land in two distinct frequencies separated by at most `A b_y`.

## 2. Pair crowding is weaker than nearest-neighbor crowding

For each frequency define

`q_A(lambda)=sum_(mu!=lambda, |lambda-mu|<=A b_y) nu(mu)`.

Then

`Q(A)=sum_lambda nu(lambda) q_A(lambda)`.

If `delta_lambda>A b_y`, there is no admissible `mu` and `q_A(lambda)=0`. Otherwise trivially `q_A(lambda)<=1`. Therefore

`q_A(lambda) <= 1_{delta_lambda<=A b_y}`

and

`Q(A)<=sum_(delta_lambda<=A b_y) nu(lambda)=C(A)`.

Combining this with Section 1 yields

`S(A)/R^2 <=4C(A)`.

`VIS-195` proved that

`D_v=o(y^2)`

is equivalent to `C(A)->0` for every fixed `A>1`. Thus any theorem strong enough to close the nearest-neighbor Hilbert resource automatically closes the fixed-scale shell-energy obstruction of `VIS-203`.

But the implication can be strict. In an abstract symmetric four-point probability measure, put mass `(1-epsilon)/2` at each of `+lambda,-lambda` and mass `epsilon/2` at each of close partners `+mu,-mu`, with no other close pairs. Every point has a close neighbor, so `C(A)=1`, while

`Q(A)=epsilon(1-epsilon)->0`.

This example is only a logical control. It does not assert that the prime-ratio coefficient measure has such an imbalance. It shows that replacing `C` by `Q` is a real weakening of the target, not a notational reformulation.

## 3. Arithmetic interpretation

By `VIS-195`, every fixed-`A` close pair is eventually a top-scale bounded-determinant incidence between prime products. By `VIS-204`, the dangerous nonzero shells are noncancelling four-prime shells with uniformly bounded exact multiplicity.

Therefore `Q_(y,H)(A)` is the **two-sided weighted incidence mass** of those bounded-determinant relations:

- `C(A)` asks how much coefficient mass sits at a frequency having at least one dangerous arithmetic neighbor;
- `Q(A)` asks how much product mass `nu(lambda)nu(mu)` is carried by the dangerous neighboring pairs themselves.

The distinction matters. A frequency with large `nu(lambda)` and only very light dangerous neighbors contributes almost its full weight to `C(A)` but only the light-partner product to `Q(A)`. This is exactly the configuration that the shell-energy formulation can tolerate and the nearest-neighbor Hilbert majorant cannot.

Thus the remaining shell-packing question should not automatically be attacked by proving the stronger `VIS-195` criterion. A direct weighted pair-incidence estimate can be sufficient even if the one-sided crowding mass is not known to vanish.

## Prior-art audit

The square-sum of representation functions is classical additive-energy language, and weighted versions are standard. For a modern reference using weighted additive energies and their moment representation, see Akshat Mudgal, **Unbounded expansion of polynomials and products**, *Mathematische Annalen* 390 (2024), 381--415, DOI `10.1007/s00208-023-02762-z`. The ordinary additive/multiplicative energy framework and Sidon interpretation are also standard and were already bounded as prior art in `VIS-204`.

No novelty is claimed for representation functions, weighted energy, Cauchy--Schwarz, or interpreting a normalized quadratic weight as a two-sample collision probability.

The Mathia-specific content is the combination of the exact nonnegative shell amplitudes from `VIS-203` with the fixed-scale multiplicity cap from `VIS-204`, yielding the constant-factor equivalence between the actual finite-start shell energy and the pair-crowding functional `Q`, and separating that weaker quadratic target from the one-sided nearest-neighbor mass `C` used by the Hilbert route.

## Boundaries and falsification

The factor-four comparison uses the fixed-`A`, sufficiently-large-`y` multiplicity theorem of `VIS-204`. It need not survive when the shell window widens toward the order-`1/y` prime/prime cancellation scale, where anchored shells can have growing multiplicity.

The lower bound uses nonnegative within-shell amplitudes and therefore belongs to the autocorrelation-taper class of `VIS-203`. Sign-changing centered tapers may have cancellation inside a shell and require a different energy decomposition.

`Q(A)<=C(A)` is deliberately one-sided. Do not infer `C(A)->0` from `Q(A)->0` without additional lower regularity on neighboring coefficient weights.

The finding treats each fixed normalized window. It does not control the contribution of shells whose normalized width `A=A(y)` grows, nor the full sinc-weighted sum outside the dangerous fixed-scale region.

Falsify the finding by finding a dangerous shell violating the `VIS-204` multiplicity cap, a failure of the nonnegative shell representation from `VIS-203`, or an ordered close pair omitted or multiply counted in the shell partition used above.

## Research consequence

The fixed-scale shell-packing frontier is now sharper. The object that must be killed is not the existence of close neighbors and not the maximum exact-shell multiplicity. It is the quadratic pair-crowding mass

`Q_(y,H)(A)`.

This leaves a potentially cheaper route than `D_v=o(y^2)`: estimate the **weighted pair incidence** of top-scale bounded-determinant prime-product collisions directly. If the actual taper weights strongly suppress one endpoint of most dangerous pairs, `Q(A)` may vanish even when the one-sided crowding statistic `C(A)` does not.

The next coherent question is therefore whether the explicit `VIS-192` coefficient profile yields a direct bound on `Q_(y,H)(A)` at or below the `VIS-202` boundary, or whether a lower-bound construction forces `Q(A)` to remain macroscopic. That is a separate problem and should be handled in a later invocation.
