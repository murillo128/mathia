# MI-025 — Möbius inverse-row support is the coordinate-minimal stable sampler for a growing prefix

**Evidence level:** exact synthesis from [FD-168](../../findings/FD-168-prefix-mobius-rows-give-coordinate-minimal-stable-partial-farey-sampling.md), building on the divisor inversion and complete-field conditioning of FD-117 and FD-167.

For horizon `H` and a target prefix `1<=r<=R<=floor(sqrt H)`, write `k_r=floor(H/r)`. The exact divisor inverse for the cumulative source coordinate `M(r)` uses only Fourier data `Y_H(d)=1+2 pi i d hat D_H(d)` at divisors `d|k_r` with `mu(k_r/d)!=0`:

`M(r)=k_r^(-1) sum_(d|k_r, mu(k_r/d)!=0) mu(k_r/d) Y_H(d)`.

Let `S_(H,R)` be the union of those nonzero row supports for `r<=R`. FD-168 proves three facts simultaneously. First, observing exactly the raw positive Fourier coordinates in `S_(H,R)` recovers the whole source prefix. Second, no proper subset of those raw coordinates can recover the prefix over the full formal real source space, even if the decoder is allowed to be nonlinear. Third, the complete-field `sqrt(30)` inverse modulus localizes to the same support:

`max_(r<=R)|A(r)-M(r)| <= sqrt(30) ||Pi_(H,R) E_H||_2`.

Thus the inverse formula itself identifies both the information support and the stability support. Coordinates outside `S_(H,R)` are not merely redundant for exact inversion; their errors do not enter the prefix stability estimate. For integer-valued sources, projected field error below `1/sqrt(30)` already snaps the recovered prefix exactly.

The support can also be genuinely sparse relative to the full square-root Fourier skeleton. FD-168 gives

`R <= |S_(H,R)| <= sum_(r<=R) 2^(omega(k_r)) <= R H^(o(1))`.

Hence for every fixed `delta>0`, if `R<=H^(1/2-delta)` then `|S_(H,R)|=o(sqrt H)`. A growing sub-square-root Möbius prefix is therefore uniformly recoverable from a vanishing fraction of the raw positive Fourier coordinates.

The reusable lesson is that **partial observation should be analyzed against the support of the actual inverse, not against the ambient transform size**. Here exact algebraic sparsity and stable inverse geometry align: the nonzero Möbius rows give the coordinate-minimal raw sampler, and deleting all other Fourier modes costs nothing for that prefix. Any stronger compression claim must change the measurement family — for example mixed linear measurements, spatial samples, coarsened data or source-restricted coding — rather than count coordinates that the inverse never uses.

**Boundary.** Coordinate minimality is relative to the raw FD-118 positive Fourier coordinates and the full formal real source space. It does not rule out fewer custom mixed measurements, nonlinear source-specific compression, or spatial sampling schemes. The `R H^(o(1))` estimate gives a vanishing fraction when `R` stays a fixed power below `sqrt H`, but it does not establish such sparsity at the full square-root prefix. Stable coefficient recovery also remains logically separate from coercivity of the Franel--Landau destination.