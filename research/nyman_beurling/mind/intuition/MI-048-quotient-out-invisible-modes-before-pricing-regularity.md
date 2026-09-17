# MI-048 — Quotient out invisible modes before pricing regularity

**Evidence level:** exact/literature-backed synthesis from [NB-182](../../findings/NB-182-euler-wiener-acquisition-prices-non-hilbert-phase-codes.md) through [NB-184](../../findings/NB-184-quotient-anchoring-pushes-typical-euler-acquisition-to-the-quadratic-width-scale.md).

The signed samplers in the Nyman transport problem have total mass zero. They therefore do not observe an Euler kernel `K` as an absolute function: they observe its class in `C([-B,B])/constants`. Any regularity or acquisition estimate performed before taking this quotient can pay for a constant mode that the destination cannot see.

NB-184 makes that bookkeeping error quantitative. Anchoring the genuine Euler kernel by `F_t(u)=K_(a,t)(u)-K_(a,t)(0)` leaves every zero-mass transport response unchanged. The anchored zeroth-order energy is then interpolated with derivative energy by a one-dimensional Gagliardo--Nirenberg estimate, instead of bounding the absolute representative by its full supremum.

This moves the typical-height scalar acquisition threshold to the quadratic width scale. If `a_T->0` and `T a_T^2->infinity`, then

`sqrt(a_T) mathcal H_(a_T,B)(t) -> 0`

in relative measure on `[T,2T]`. Since the generic capped-Poisson packing dimension satisfies `N(a) asymp 1/a`, the charged scalar Euler acquisition ratio beats the full `sqrt(N)` packing tariff on density-one heights throughout that regime. For power widths `a=T^(-alpha)`, every fixed `alpha<1/2` is included.

The reusable lesson is structural: **first quotient by the exact observation kernel, then price regularity, conditioning or acquisition on the surviving class**. This is not a free normalization trick. The improvement exists because additive constants are exactly invisible to the zero-mass sampler; a nonzero-mass destination would not permit the same quotient.

The result also sharpens the distinction between scalar exposure and coherent rank. Typical scalar acquisition is already supercritical well before the remaining quadratic endpoint, but NB-184 still does not assemble many such scalar channels into one source-natural response matrix with coherent phases and many large singular values.

**Boundary.** The conclusion is density-one rather than pointwise at an adversarially selected height, it does not construct coherent rank, and the exact endpoint `T a^2=O(1)` remains open. The principle applies only to modes that the declared destination annihilates exactly.