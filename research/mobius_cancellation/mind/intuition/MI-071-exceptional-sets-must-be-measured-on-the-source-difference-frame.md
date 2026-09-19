# MI-071 — Source-frame exceptional geometry is constrained twice: by Welch scale and by the exact source image

**Evidence level:** exact synthesis from [MC-385](../../findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md) through [MC-388](../../findings/MC-388-endpoint-simplex-rank-excludes-near-annihilator-sharpness.md), interpreted against the endpoint source-frame bounds of MC-374 and MC-381 and the analytic ceilings MC-382--MC-384.

The endpoint frame does not require uniform cancellation for every source character. Let `W` be a surviving endpoint-mode subspace, `H=|W|`, and let `G` be the Gram matrix of its normalized source rows. Exact endpoint constancy puts all rows in an `R`-dimensional space.

MC-385 shows that an ambient exceptional count is meaningful only after pullback to the source Cayley frame. MC-386 identifies the sharp generic scale: rank at most `R` forces total off-diagonal squared correlation at least `H/R-1` per row on average, so a sufficient contradiction regime is `E=o(H/R)` exceptional differences together with ordinary correlations `epsilon=o(R^(-1/2))`. Abstract annihilator-subgroup Cayley frames attain the `H/R` exceptional scale.

MC-387 proves that this sharp model is rigid near equality. A PSD Cayley kernel has a finite Bochner representation. Near-Welch equality makes the Fourier measure nearly uniform on an `R`-sized support, while concentration of physical `L^2` mass on the minimal `H/R` scale forces near-maximal additive energy. The dual support must then approach a subgroup coset and the physical exceptional set the corresponding annihilator subgroup.

MC-388 performs the decisive second pullback. For the exact endpoint partition the Bochner support is the projection of the translated coordinate simplex `1+e_z`, with positive defect weights. If `d=dim W`, its affine dimension is exactly

`d-dim(W cap <1>) >= d-1`.

Hence a high-dimensional endpoint support cannot be close to the low-dimensional coset required by the MC-387 near-extremizer. In the rank-linear branch `d>=cR`, and in particular in the `d>=3R/4` source-cost regime of MC-381, the abstract annihilator sharpness mechanism is inadmissible.

The reusable lesson is that **source-conditioned exceptional incidence has a scale, a near-extremal shape, and a source-image compatibility gate**. It is not enough to prove that a generic analytic bound is sharp by constructing an ambient extremizer. One should classify near-extremizers and then pull their structure through the exact arithmetic source map. A source law can exclude an otherwise sharp ambient obstruction without improving the generic inequality itself.

The remaining problem is quantitative. MC-388 excludes near-minimal coset/annihilator concentration in high dimension, but does not yet show that fewer than `Theta(H/R)` exceptional source differences suffice, because energy may spread over more physical modes or sit above the Welch floor. The next useful statement would convert the projected-simplex affine-rank lower bound into an explicit additive-energy deficit, physical-spread lower bound or improved exceptional-mode budget.

**Boundary.** No common exponent or frame estimate transfers to unrelated Mathia lines. The endpoint simplex identity uses the exact one-defect-per-shell-prime partition and high-dimensional `W`; low-dimensional source subspaces remain outside the asymptotic exclusion. MC-388 does not prove Möbius cancellation or RH. It removes one abstract sharpness mechanism and exposes the quantitative gap that arithmetic structure must now exploit.