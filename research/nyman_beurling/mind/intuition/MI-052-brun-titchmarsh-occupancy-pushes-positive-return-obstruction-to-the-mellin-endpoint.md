# MI-052 — Brun--Titchmarsh occupancy pushes accurate positive Euler recurrence to the Mellin endpoint

**Evidence level:** literature+derived synthesis from [NB-192](../../findings/NB-192-prime-log-dimension-forces-double-exponential-bohr-return-scale.md) through [NB-198](../../findings/NB-198-brun-titchmarsh-phase-occupancy-excludes-accurate-positive-euler-returns-at-every-sublinear-mellin-power.md). The Brun--Titchmarsh interval bound and phase-window counting mechanism are classical; the Mathia content is their use on the normalized positive von-Mangoldt Euler shell and the resulting exponent/tolerance tradeoff.

The earlier positive-recurrence frontier was tied to how accurately the true prime shell could be replaced by continuum mass cell by cell. Uniform short-interval PNT gave the `13/30` Mellin corridor, and the almost-all Guth--Maynard input plus positivity extended pointwise exclusion to `13/15`. Those exponents measured available source-resolution technology, not an intrinsic recurrence threshold.

NB-198 shows that excluding a **sufficiently accurate** positive return needs much less than an asymptotic prime count. If

`A_a(t)=sum_n w_(n,a)|exp(-it log n)-1|`

for the normalized positive von-Mangoldt shell around `x_a=exp(r_0/a)`, then a small value of `A_a(t)` forces most source mass into the short multiplicative windows where `t log n` lies near `2 pi Z`. For every fixed exponent margin `0<beta<1`, those windows have spatial length at least a fixed-power scale `x_a^beta` whenever

`|t| <= x_a^(1-beta)`.

Brun--Titchmarsh bounds the prime mass that can occupy all favorable windows. Choosing the phase tolerance proportionally to `beta` yields a fixed gap

`A_a(t) > eta_beta`,

uniformly from a fixed height up to `x_a^(1-beta)`, with one admissible choice

`eta_beta=sin(pi beta/32)`.

Consequently, if a coupled physical block satisfies

`limsup a_T log(2T)/r_0 < 1`,

then some fixed positive return tolerance is eventually excluded throughout `[T,2T]`. No fixed Mellin-power corridor below exponent one can therefore contain arbitrarily accurate positive Euler returns.

This does not supersede NB-197 at a prescribed large tolerance. As `beta->0`, the certified `eta_beta` also tends to zero. NB-197 remains stronger inside its `13/15` corridor when one wants to rule out every chosen fixed `eta<1`; NB-198 is stronger in range when the question is whether the recurrence can become arbitrarily accurate.

The reusable distinction is between **source approximation** and **source occupancy**. To approximate an oscillatory shell one needs lower-and-upper asymptotics on spatial cells. To rule out a positive near-return, it is enough to prove that the support cannot concentrate most of its positive mass inside the favorable phase cells. A sieve upper bound can therefore obstruct accurate recurrence far beyond the range where a continuum approximation theorem is available.

The positive frontier is compressed to the endpoint layer `t=x_a^(1-o(1))`, where favorable phase windows have subpower length and the Brun--Titchmarsh logarithmic denominator no longer gives a fixed occupancy gap. Independently, signed or complex synthesis remains outside this argument because cancellation destroys the monotone mass implication that turns a small chord average into phase occupancy.

**Boundary.** NB-198 is a positive-source acquisition obstruction, not an Nyman-distance theorem. It does not rule out isolated endpoint-layer returns, give a uniform fixed tolerance as the exponent margin tends to zero, or constrain signed/complex aggregates. A destination theorem is still needed to show that a successful Nyman approximation must realize one of these positive-shell returns.