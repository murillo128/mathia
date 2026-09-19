# MI-071 — Source-frame exceptional geometry has a fixed gap above the generic Welch threshold

**Evidence level:** exact synthesis from [MC-385](../../findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md) through [MC-389](../../findings/MC-389-endpoint-affine-rank-forces-fixed-exception-gap.md), interpreted against the endpoint source-frame bounds of MC-374 and MC-381 and the analytic ceilings MC-382--MC-384.

The endpoint frame does not require uniform cancellation for every source character. Let `W` be a surviving endpoint-mode subspace, `H=|W|`, and let `G` be the Gram matrix of its normalized source rows. Exact endpoint constancy puts all rows in an `R`-dimensional space.

MC-385 shows that an ambient exceptional count is meaningful only after pullback to the source Cayley frame. MC-386 identifies the sharp generic scale: rank at most `R` forces total off-diagonal squared correlation at least `H/R-1` per row on average, so a sufficient contradiction regime is `E=o(H/R)` exceptional differences together with ordinary correlations `epsilon=o(R^(-1/2))`. Abstract annihilator-subgroup Cayley frames attain the `H/R` exceptional scale.

MC-387 proves that this sharp model is rigid near equality. A PSD Cayley kernel has a finite Bochner representation. Near-Welch equality makes the Fourier measure nearly uniform on an `R`-sized support, while concentration of physical `L^2` mass on the minimal `H/R` scale forces near-maximal additive energy. The dual support must then approach a subgroup coset and the physical exceptional set the corresponding annihilator subgroup.

MC-388 performs the decisive second pullback. For the exact endpoint partition the Bochner support is the projection of the translated coordinate simplex `1+e_z`, with positive defect weights. If `d=dim W`, its affine dimension is exactly

`d-dim(W cap <1>) >= d-1`.

Hence a high-dimensional endpoint support cannot approach the low-dimensional coset required by the MC-387 near-extremizer. In the rank-linear branch, and in particular for `d>=3R/4`, the abstract annihilator sharpness mechanism is inadmissible.

MC-389 converts that qualitative incompatibility into a fixed quantitative gap. Combining the endpoint affine-rank lower bound with restricted-sumset stability gives an absolute `delta_0>0` such that the endpoint Bochner support has additive-energy deficit

`E(S) <= (1-delta_0)|S|^3`

in the high-rank branch. Near-Welch weights then inherit a fixed fourth-moment contraction. Consequently, if all good nonzero source modes satisfy `|g(K)|<=epsilon_R` with `epsilon_R=o(R^(-1/2))`, any exceptional set `B` must obey

`|B| >= (1+c_endpoint) H/R`

for some fixed `c_endpoint>0` once `R` is large. The exact endpoint source therefore cannot merely avoid the generic `H/R` near-extremizer shape; it needs a **strict multiplicative excess** over the generic Welch exceptional count.

The reusable lesson is that source-conditioned exceptional incidence has four layers: ambient scale, near-extremal shape, source-image compatibility, and then a quantitative source gap. A generic inequality can be sharp in its ambient category while the exact arithmetic image forces every admissible near-extremizer a fixed distance away, converting source geometry into a stronger threshold without changing the ambient Welch theorem.

The remaining bottleneck has moved again. MC-389 is conditional on the analytic good-mode estimate `epsilon_R=o(R^(-1/2))` and gives only an existential fixed excess. The useful next statements are an effective deficit directly from the explicit projected-simplex support, a larger endpoint-specific exceptional gap if available, and—most importantly—the analytic estimate that puts the nonexceptional source differences below the `R^(-1/2)` frame scale.

**Boundary.** The constants in the source-frame gap are endpoint-specific and do not transfer to unrelated Mathia lines. MC-389 does not prove the required character cancellation, Möbius cancellation or RH. Low-dimensional endpoint subspaces remain outside the high-rank argument, and the fixed multiplicative improvement does not by itself determine the optimal endpoint exceptional scale.