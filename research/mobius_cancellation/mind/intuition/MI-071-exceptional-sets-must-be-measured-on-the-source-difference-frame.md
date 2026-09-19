# MI-071 — Source-frame exceptional geometry has an explicit fixed gap above the generic Welch threshold

**Evidence level:** exact synthesis from [MC-385](../../findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md) through [MC-389](../../findings/MC-389-endpoint-affine-rank-forces-fixed-exception-gap.md), interpreted against the endpoint source-frame bounds of MC-374 and MC-381 and the analytic ceilings MC-382--MC-384.

The endpoint frame does not require uniform cancellation for every source character. Let `W` be a surviving endpoint-mode subspace, `H=|W|`, and let `G` be the Gram matrix of its normalized source rows. Exact endpoint constancy puts all rows in an `R`-dimensional space.

MC-385 shows that an ambient exceptional count is meaningful only after pullback to the source Cayley frame. MC-386 identifies the sharp generic scale: rank at most `R` forces total off-diagonal squared correlation at least `H/R-1` per row on average, so a sufficient contradiction regime is `E=o(H/R)` exceptional differences together with ordinary correlations `epsilon=o(R^(-1/2))`. Abstract annihilator-subgroup Cayley frames attain the `H/R` exceptional scale.

MC-387 proves that this sharp model is rigid near equality. A PSD Cayley kernel has a finite Bochner representation. Near-Welch equality makes the Fourier measure nearly uniform on an `R`-sized support, while concentration of physical `L^2` mass on the minimal `H/R` scale forces near-maximal additive energy. The dual support must then approach a subgroup coset and the physical exceptional set the corresponding annihilator subgroup.

MC-388 performs the decisive second pullback. For the exact endpoint partition the Bochner support is the projection of the translated coordinate simplex `1+e_z`, with positive defect weights. If `d=dim W`, its affine dimension is exactly

`d-dim(W cap <1>) >= d-1`.

Hence a high-dimensional endpoint support cannot approach the low-dimensional coset required by the MC-387 near-extremizer. In the rank-linear branch, and in particular for `d>=3R/4`, the abstract annihilator sharpness mechanism is inadmissible.

MC-389 turns this source mismatch into a direct quantitative theorem without needing an additive inverse theorem. If a finite set `A` in a binary vector space has size `r` and affine dimension `k`, then every nonzero translate overlap satisfies

`|A cap (A+t)| <= 2(r-k)`.

Since additive energy is the sum of squared translate overlaps,

`E(A) <= r^2 + 2(r-k)(r^2-r)`.

For the projected endpoint simplex, `k>=d-1>=3R/4-1` and `r<=R`, so for large `R`

`E(S) <= (3/4) r^3`.

Near-Welch endpoint weights inherit a fixed fourth-moment contraction from this explicit energy deficit. Consequently, if all good nonzero source modes satisfy `|g(K)|<=epsilon_R` with `epsilon_R=o(R^(-1/2))`, any exceptional set `B` obeys

`|B| >= (1+1/4096) H/R`

for all sufficiently large `R`. The constant is deliberately non-optimized, but the source-frame excess itself is now effective.

The reusable lesson is that source-conditioned exceptional incidence has four layers: ambient scale, near-extremal shape, source-image compatibility, and then a quantitative source gap. A generic inequality can be sharp in its ambient category while the exact arithmetic image forces every admissible near-extremizer a fixed distance away. When the source support also has an explicit affine model, the final gap can sometimes be obtained by a direct combinatorial inequality rather than an abstract stability modulus.

The remaining bottleneck has therefore moved again. MC-389 is still conditional on the analytic good-mode estimate `epsilon_R=o(R^(-1/2))`, but the endpoint source gap no longer needs to be made effective. The useful next statements are the analytic estimate that puts nonexceptional source differences below the frame scale and, secondarily, an optimal endpoint-specific constant or stronger inequality extracted from the projected simplex.

**Boundary.** The `1/4096` gap is endpoint-specific and deliberately non-optimal; it does not transfer to unrelated Mathia lines. MC-389 does not prove the required character cancellation, Möbius cancellation or RH. Low-dimensional endpoint subspaces remain outside the high-rank argument, and the fixed multiplicative improvement does not by itself determine the optimal endpoint exceptional scale.
