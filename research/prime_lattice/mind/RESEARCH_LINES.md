# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove a uniform source-selected orientation law on the shrinking first-prime layer

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-023-the-first-prime-overlap-algebra-is-not-the-missing-rh-mechanism`.

PL-313--PL-323 close the moving Green endpoint transfer at each fixed aperture. The exact source equation, conservative singular-kernel flux identity and positive jump-kernel maximum principle force the primitive critical coefficient and `Qm(Q)->0`; there is no remaining generic analytic task to manufacture a finite endpoint limit.

PL-324 tests whether the RH-relevant odd Weil sector can supply the missing sign through standard positivity-preserving semigroup theory. Parity removes the full-space archimedean Beurling--Deny obstruction completely, so positivity survives exactly until the first rational-prime event `a=(1/2)log 2`; immediately afterward the prime translation has the wrong modulus sign.

PL-325 classicalizes the next obvious step. In the first-prime window the truncated `log 2` translation is exactly a two-edge flip with spectrum `{-1,0,1}` and infinite-dimensional `±1` sectors. Its operator norm jumps from zero to one at the threshold, but near threshold the same coupling is small relative to the singular endpoint coercive form. This exact overlap algebra, its Legendre compression and related finite-scale first-prime machinery are already public prior art and independently reconstructible.

PL-326 closes the naive bridge from the fixed-aperture endpoint law to first-crossing orientation. If `a_delta=(log 2)/2+delta`, the arithmetic reflection lives on a layer of width `2delta`. Two comparison families can have exactly the same critical endpoint germ and satisfy the pointwise `Qm(Q)->0` residual law at every fixed `delta`, while an antisymmetric bump supported inside the shrinking layer reverses the reflection sign. The bump is absolutely small in `L^2` and in the logarithmic endpoint-potential weight, yet it dominates the still smaller `delta/log(1/delta)` reflected correlation of the critical profile.

The missing quantifier is now explicit. A sufficient uniform scale is of order

`||r_delta||_2 = o(|C_delta| sqrt(delta/log(1/delta)))`,

or an equivalent source/eigen-equation estimate controlling the reflection functional directly. Neither the norm-one overlap algebra, endpoint form-smallness nor fixed-aperture boundary asymptotics supplies this moving-layer estimate.

The live theorem must therefore couple the **actual signed state selected by the full Weil operator** to the shrinking arithmetic prime-power channel uniformly across threshold: an aperture-uniform first-crossing/eigenstate-orientation law, a source/endpoint-flux estimate suppressing the antisymmetric moving-layer sector, or another signed identity that controls the first-prime reflection directly and survives beyond the single `log 2` block.

## Keep fixed-aperture transport, moving-threshold uniformity, cone positivity, overlap algebra and arithmetic orientation separate

PL-322--PL-323 are fixed-aperture real-variable/nonlocal transport results. PL-324 is an exact order-positivity classification on the odd sector. PL-325 is an exact single-shift algebra/prior-art boundary. PL-326 is a moving-threshold uniformity obstruction. None supplies the final arithmetic orientation.

The topology distinction is now twofold. Small overlap width is not small bounded-operator norm, while endpoint-weighted form control can still be small near threshold; moreover, absolute smallness in that endpoint layer is not a relative sign estimate because the critical reflected correlation is smaller still. A genuine first-crossing theorem must use the selected state or a source-specific signed identity at the correct moving-layer scale.

Future work should preserve the closed fixed-aperture Green transfer and the classified one-prime algebra as interfaces, then work directly with the signed rational-prime contribution uniformly across apertures. Reproving generic endpoint regularity, the `±1` flip sectors, Legendre compression, standard positive-semigroup continuation, or pointwise endpoint asymptotics is no longer a live direction.
