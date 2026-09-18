# MI-052 — Brun--Titchmarsh occupancy pushes accurate positive Euler recurrence to the Mellin endpoint

**Evidence level:** literature+derived synthesis from [NB-192](../../findings/NB-192-prime-log-dimension-forces-double-exponential-bohr-return-scale.md) through [NB-199](../../findings/NB-199-diagonal-brun-titchmarsh-localizes-vanishing-positive-euler-returns-to-the-logarithmic-mellin-endpoint.md). The Brun--Titchmarsh interval bound and phase-window counting mechanism are classical; the Mathia content is their use on the normalized positive von-Mangoldt Euler shell and the resulting exponent/tolerance tradeoff all the way to the logarithmic Mellin endpoint.

The earlier positive-recurrence frontier was tied to how accurately the true prime shell could be replaced by continuum mass cell by cell. Uniform short-interval PNT gave the `13/30` Mellin corridor, and the almost-all Guth--Maynard input plus positivity extended pointwise exclusion to `13/15`. Those exponents measured available source-resolution technology, not an intrinsic recurrence threshold.

NB-198 shows that excluding a **sufficiently accurate** positive return needs much less than an asymptotic prime count. If

`A_a(t)=sum_n w_(n,a)|exp(-it log n)-1|`

for the normalized positive von-Mangoldt shell around `x_a=exp(r_0/a)`, then a small value of `A_a(t)` forces most source mass into the short multiplicative windows where `t log n` lies near `2 pi Z`. For every fixed exponent margin `0<beta<1`, those windows have spatial length at least a fixed-power scale `x_a^beta` whenever

`|t| <= x_a^(1-beta)`.

Brun--Titchmarsh bounds the prime mass that can occupy all favorable windows. Choosing the phase tolerance proportionally to `beta` yields a fixed gap `A_a(t)>eta_beta`, so no fixed Mellin-power corridor below exponent one can contain arbitrarily accurate positive Euler returns. This is stronger in range than the short-interval approximation theorems but weaker in prescribed tolerance as `beta->0`.

NB-199 removes the artificial fixed exponent margin and follows the phase-window scale diagonally toward the endpoint. Put `X_a=log x_a=r_0/a`. Throughout

`X_a^2 <= |t| <= x_a/(U_0 X_a)`,

one has

`A_a(t) >= c * log(x_a/(|t|X_a))/X_a`.

Inverting the inequality, a return of accuracy `eta` can occur only if

`|t| >= x_a^(1-C eta)/log x_a`.

Hence if `eta_a=o(1/X_a)=o(a)`, every positive return below a constant multiple of `x_a/log x_a` is excluded. The vanishing-tolerance positive frontier is therefore compressed into the final logarithmic Mellin layer, not merely into an unspecified `x_a^(1-o(1))` region.

The reusable distinction is between **source approximation, source occupancy, and requested return accuracy**. To approximate an oscillatory shell one needs lower-and-upper asymptotics on spatial cells. To rule out a positive near-return, it is enough to show that favorable phase cells cannot carry almost all positive source mass. Once the phase-window width itself is retained, the occupancy deficit becomes an explicit function of distance from the Mellin endpoint and can be inverted against a shrinking tolerance.

This still leaves two separate gates. First, the endpoint layer `t~x_a/log x_a` is not controlled by NB-199. Second, the Nyman destination must be shown to require a positive-shell return with the corresponding accuracy. Signed or complex synthesis remains outside the occupancy argument because cancellation destroys the monotone implication from small chord average to phase concentration.

**Boundary.** NB-199 is a positive-source acquisition obstruction, not a Nyman-distance theorem. It does not exclude isolated returns in the final logarithmic endpoint layer, give a uniform large fixed tolerance all the way to exponent one, or constrain signed/complex aggregates. NB-197 can remain stronger at prescribed fixed tolerance inside its shorter corridor.