# MI-052 — Positive Euler recurrence changes from interval occupancy to stable atomic phase-cell capacity at the Mellin endpoint

**Evidence level:** literature+derived synthesis from [NB-192](../../findings/NB-192-prime-log-dimension-forces-double-exponential-bohr-return-scale.md) through [NB-201](../../findings/NB-201-atomic-endpoint-capacity-has-a-quadratic-stability-modulus.md). The occupancy, phase-window counting and one-atom-per-subunit-cell mechanisms are classical; the Mathia content is their specialization to the normalized positive von-Mangoldt shell and the resulting endpoint acquisition modulus.

The earlier positive-recurrence frontier was tied to how accurately the true prime shell could be replaced by continuum mass cell by cell. Uniform short-interval PNT and almost-all source resolution produced intermediate Mellin corridors, but those exponents measured available source-resolution technology rather than an intrinsic recurrence threshold.

NB-198--NB-199 replace cellwise source approximation by a mass-placement argument. If

`A_a(t)=sum_n w_(n,a)|exp(-it log n)-1|`

for the normalized positive von-Mangoldt shell around `x_a=exp(r_0/a)` and `X_a=log x_a`, then small `A_a(t)` forces most positive source mass into short multiplicative phase windows. Brun--Titchmarsh bounds how much mass those windows can carry and yields the diagonal corridor

`A_a(t) >= c log(x_a/(|t|X_a))/X_a`

for `X_a^2 <= |t| <= x_a/(U_0X_a)`. Thus `o(1/X_a)` returns cannot occur below the final logarithmic layer `x_a/X_a`.

At endpoint scale the favorable windows become physically shorter than one integer, so local density ceases to be the right currency. NB-200 switches to atomic capacity: each favorable phase cell contains at most one von-Mangoldt atom. This gives the one-sided threshold

`liminf |t|X_a/x_a >= 2 pi e^Delta`

for sequences with `X_a A_a(t)->0` and bounded endpoint ratio. The constant is a certified carrying-capacity edge, not a return-existence theorem.

NB-201 makes that edge quantitatively stable. With

`kappa_a^cap = 2 pi e^Delta X_a/(X_a+Delta)`, `kappa_a(t)=|t|X_a/x_a`, and `d_a(t)=1-kappa_a(t)/kappa_a^cap`,

one has, in the one-sided endpoint regime,

`A_a(t) >= (c/X_a) (d_a(t)^2-C E_a)_+`,

where `E_a` is the inherited Vinogradov--Korobov PNT remainder. Equivalently,

`d_a(t) <= C(sqrt(X_a A_a(t))+sqrt(E_a))`.

The square is structural: a relative capacity deficit `d` is tested on a top slab of source mass `Theta(d)`, and the fraction of that slab that cannot fit into favorable cells is another `Theta(d)`. Thus an increasingly accurate positive return approaching the edge from below must approach it at a square-root modulus, down to the PNT resolution floor.

The reusable transition is therefore `continuum occupancy -> atomic capacity -> capacity stability`. First price favorable regions by local source mass, then by discrete carrying capacity once cells become sub-lattice, and finally retain the finite-scale capacity ratio if the requested error approaches the endpoint simultaneously. Positivity is load-bearing throughout because it converts chord error into monotone missing source mass.

The positive-source frontier is now at and above the certified atomic edge. A stronger obstruction there must use how von-Mangoldt mass actually occupies the available cells, not only their number or maximal atom mass. Independently, the Nyman destination must still be shown to demand such an `o(a)` positive-shell return; acquisition alone is not a Nyman-distance lower bound.

**Boundary.** The edge depends on the chosen fixed log-width shell and remains one-sided. NB-201 does not prove a return exists at the edge, and the `sqrt(E_a)` floor is intrinsic to the source-resolution input used in this argument. Signed or complex synthesis can cancel across cells, so neither the positive packing theorem nor its quadratic stability modulus transfers automatically.