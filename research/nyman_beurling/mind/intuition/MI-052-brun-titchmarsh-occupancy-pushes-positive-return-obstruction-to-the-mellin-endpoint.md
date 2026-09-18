# MI-052 — Positive Euler recurrence changes from interval occupancy to atomic phase-cell capacity at the Mellin endpoint

**Evidence level:** literature+derived synthesis from [NB-192](../../findings/NB-192-prime-log-dimension-forces-double-exponential-bohr-return-scale.md) through [NB-200](../../findings/NB-200-atomic-phase-cell-packing-forces-a-2pi-exp-delta-endpoint-threshold.md). The Brun--Titchmarsh interval bound, phase-window counting and one-atom-per-subunit-cell argument are classical mechanisms; the Mathia content is their specialization to the normalized positive von-Mangoldt shell and the resulting endpoint acquisition threshold.

The earlier positive-recurrence frontier was tied to how accurately the true prime shell could be replaced by continuum mass cell by cell. Uniform short-interval PNT gave the `13/30` Mellin corridor, and almost-all source resolution plus positivity extended pointwise exclusion to `13/15`. Those exponents measured available source-resolution technology, not an intrinsic recurrence threshold.

NB-198 shows that excluding a sufficiently accurate positive return needs less than an asymptotic prime count. If

`A_a(t)=sum_n w_(n,a)|exp(-it log n)-1|`

for the normalized positive von-Mangoldt shell around `x_a=exp(r_0/a)`, then a small `A_a(t)` forces most source mass into short multiplicative windows where `t log n` lies near `2 pi Z`. Brun--Titchmarsh upper-bounds the mass those favorable windows can carry, excluding arbitrarily accurate returns throughout every fixed subunit Mellin power.

NB-199 follows the window scale diagonally toward the endpoint. With `X_a=log x_a=r_0/a`, throughout

`X_a^2 <= |t| <= x_a/(U_0 X_a)`

one has

`A_a(t) >= c log(x_a/(|t|X_a))/X_a`.

Hence `A_a(t)<=eta` implies `|t|>=x_a^(1-C eta)/log x_a`, and any tolerance `eta_a=o(1/X_a)=o(a)` is excluded below a constant multiple of `x_a/X_a`.

At exactly that scale the favorable windows stop being macroscopic intervals. NB-200 exploits the change of geometry rather than asking for a stronger short-interval prime theorem. In the endpoint strip `|t|=kappa x_a/X_a`, choose phase tolerance `delta_a=q/X_a`. Each favorable component has physical length asymptotic to `2uq/(kappa x_a)`. For fixed `kappa` and small enough `q`, every component meeting the shell has length below one, so it can contain at most one integer and therefore at most one von-Mangoldt atom.

A fixed top log-slab `[x_a e^(Delta-h),x_a e^Delta)` carries normalized source mass `h/Delta+o(1)`. It contains at most `th/(2 pi)+O(1)` favorable phase cells, and each possible atom has normalized mass at most

`(1+o(1)) X_a e^(-(Delta-h))/(x_a Delta)`.

Thus the favorable cells cannot carry the whole slab whenever `kappa<2 pi e^(Delta-h)`. Sending `h` down to the room allowed by a fixed `K<2 pi e^Delta` gives the endpoint theorem

`inf_(X_a^2 <= |t| <= K x_a/X_a) A_a(t) >= c_K/X_a`.

Equivalently, if `X_a A_a(t)->0` and `|t|X_a/x_a` stays bounded, then

`liminf |t|X_a/x_a >= 2 pi e^Delta`.

This threshold is one-sided. It says there is not enough **atomic carrying capacity** below `2 pi e^Delta`; it does not construct returns at or above that constant. The mechanism is also more primitive than unit-scale prime distribution: primality enters only through the macroscopic PNT mass of the shell, while the endpoint packing uses the integer lattice and `Lambda(n)<=log n`.

The reusable transition is therefore **continuum occupancy -> atomic capacity**. When favorable cells are wider than the lattice spacing, local source-density estimates limit how much positive mass they can hold. Once the cells are shorter than one, local density ceases to be the right currency; the hard cap is number of cells times maximal atom mass. In both regimes positivity turns a small chord average into a monotone mass-placement problem.

The next positive-source question begins at and beyond the atomic threshold: enough phase cells exist in principle, but their actual occupation by the von-Mangoldt source may still be arithmetically sparse or dephased. Independently, the Nyman destination must be shown to demand an `o(a)` positive-shell return at all; the acquisition theorem by itself is not a Nyman-distance lower bound.

**Boundary.** `2 pi e^Delta` depends on the chosen fixed log-width shell and is not claimed universal. NB-200 gives no existence/sharpness theorem above the threshold, and its positive mass argument does not constrain signed or complex synthesis. The lower high-ordinate cutoff is inherited from the previous corridor rather than asserted as a natural transition.